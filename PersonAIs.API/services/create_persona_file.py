import enum
from typing import List, Optional
from PIL import Image, ImageDraw
from io import BytesIO
from fpdf import FPDF
from enums.social_media import SocialMedia
from enums.technology import Technology
from models.persona import Persona

def draw_percentage_bar(pdf: FPDF, label: str, percentage: int, x: int, y: int):
    pdf.set_font('Aptos', size=12)
    pdf.text(x, y, txt=label)

    pdf.set_font('Aptos', size=6)
    pdf.text(pdf.w/3 - 8, y + 1, txt=f'{percentage}%')

    pdf.set_fill_color(200, 200, 200)
    pdf.rect(x, y + 2, pdf.w/3 - 6, 1, "F")

    pdf.set_fill_color(255, 255, 255)
    pdf.rect(x, y + 2, (((pdf.w/3)/100) * percentage) - 6, 1, "F")

def draw_rather_bar(pdf: FPDF, label1: str, label2: str, percentage: int, x: int, y: int):

    pdf.set_xy(2, y - 3)
    pdf.set_font('Aptos', size=12)
    pdf.cell(w=pdf.w/6.4, text=label1, align='L')
    pdf.cell(w=pdf.w/6.4, text=label2, align='R')

    line_width = pdf.w/3 - 6
    pdf.set_fill_color(200, 200, 200)
    pdf.rect(x, y + 2, line_width, 1, "F")

    ball_x = x + (line_width * (percentage / 100))

    ball_radius = 2.5
    pdf.set_fill_color(255, 255, 255)
    pdf.ellipse(ball_x - ball_radius, y + 1.25, ball_radius, ball_radius, "F")

async def transform_profile_picture() -> BytesIO:
    img = Image.open('./image/image.png').convert("RGBA")
    mask = Image.new('L', img.size, 0)
    image_draw = ImageDraw.Draw(mask)

    width, height = img.size
    image_draw.ellipse((0, 0, width - 50, height - 50), fill=255)

    result = Image.new('RGBA', img.size)

    circle_image = Image.new('RGBA', (width, height))
    image_draw = ImageDraw.Draw(circle_image)

    circle_radius = min(width, height) // 2
    circle_center = (width // 2, height // 2)
    circle_color = 'white'

    # Draw a circle
    image_draw.ellipse(
        [circle_center[0] - circle_radius, circle_center[1] - circle_radius,
        circle_center[0] + circle_radius, circle_center[1] + circle_radius],
        outline=circle_color,
        fill=circle_color
    )

    result.paste(circle_image, (0, 0))
    result.paste(img, (25, 25), mask)

    img_byte_arr = BytesIO()
    result.save(img_byte_arr, format='PNG')
    img_byte_arr.seek(0)
    return img_byte_arr

async def load_image_and_size_from_enum(enum: Technology) -> tuple[BytesIO, tuple[int, int]]:
    with open(enum.value, 'rb') as file:
        image_data = BytesIO(file.read())
        image = Image.open(image_data)
        size = image.size

    return image_data, size

async def draw_enum_icons(pdf: FPDF, technologies: List[Technology], icon_height: int = 12, y_position: int = 0, labels: Optional[List[str]] = None):
    if labels is None:
        labels = []

    if len(labels) > 0 and len(technologies) != len(labels):
        raise ValueError("The number of technologies must match the number of labels if labels are provided.")

    new_height = icon_height
    total_icon_width = 0

    for technology in technologies:
        image_data, size = await load_image_and_size_from_enum(technology)
        old_width, old_height = size
        aspect_ratio = old_width / old_height
        new_width = aspect_ratio * new_height
        total_icon_width += new_width

    available_width = pdf.w / 3
    remaining_space = available_width - total_icon_width
    gap_size = remaining_space / (len(technologies) + 1)

    x_position = gap_size
    label_height = 5

    for i, technology in enumerate(technologies):
        image_data, size = await load_image_and_size_from_enum(technology)
        old_width, old_height = size
        aspect_ratio = old_width / old_height
        new_width = aspect_ratio * new_height

        pdf.image(image_data, x=x_position, y=y_position, h=new_height)

        if labels:
            pdf.set_y(y_position + new_height + 1)
            pdf.set_x(x_position)
            pdf.set_font('Arial', 'B', 8)
            pdf.cell(new_width, label_height, labels[i], 0, 1, 'C')

        x_position += new_width + gap_size

async def generate(persona: Persona):
    pdf = FPDF()
    pdf.add_font('Aptos', '', './fonts/Aptos.ttf', uni=True)
    pdf.add_font('Aptos-Bold', '', './fonts/Aptos-Bold.ttf', uni=True)
    pdf.add_page()

    pdf.set_fill_color(21, 96, 130)
    pdf.rect(0, 0, pdf.w/3, pdf.h, "F")

    # Add profile picture
    img_data = await transform_profile_picture()
    pdf.image(img_data, x=15, y=1, w=40)

    pdf.set_fill_color(44, 134, 175)
    pdf.rect(0, 42, pdf.w/3, 25, "F")

    # Add Name, Title, and Education
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 50, txt=f"{persona.first_name} {persona.last_name}")

    pdf.set_font('Aptos', size=12)
    pdf.text(3, 57, txt=persona.profession)
    pdf.text(3, 64, txt=persona.degree)

    # Section Title for Technologies
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 75, txt="Technologie")

    # Draw technology icons
    await draw_enum_icons(pdf, persona.devices, icon_height=12, y_position=81)

    # Section Title for Digital Skills
    pdf.text(3, 105, txt="Digitale Fähigkeiten")

    # Draw Percentage Bars
    draw_percentage_bar(pdf, "Technologie", persona.technology, 3, 112)
    draw_percentage_bar(pdf, "Software und Apps", persona.software_and_apps, 3, 121)
    draw_percentage_bar(pdf, "Internet", persona.internet, 3, 130)
    draw_percentage_bar(pdf, "Social Network", persona.social_network, 3, 139)

    # Section Title for Personality
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 151, txt="Persönlichkeit")

    draw_rather_bar(pdf, "Extrovertiert", "Introvertiert", persona.extroverted_or_introverted, 3, 157)
    draw_rather_bar(pdf, "Planer", "Spontan", persona.planner_or_spontaneous, 3, 166)
    draw_rather_bar(pdf, "Denken", "Fühlen", persona.thinking_or_feeling, 3, 175)
    draw_rather_bar(pdf, "Konservativ", "Liberal", persona.conservative_or_liberal, 3, 184)
    draw_rather_bar(pdf, "Anführer", "Nachahmer", persona.leader_or_follower, 3, 193)

    # Section Title for Browser
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 205, txt="Browser")

    await draw_enum_icons(pdf, persona.browsers, icon_height=9, y_position=208)

    # Section Title for Browser
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 224, txt="Appausnutzung")

    await draw_enum_icons(pdf, [SocialMedia.TWITTER, 
                                SocialMedia.FACEBOOK, 
                                SocialMedia.YOUTUBE,
                                SocialMedia.SNAPCHAT, 
                                SocialMedia.SPOTIFY, 
                                SocialMedia.INSTAGRAM, 
                                SocialMedia.PINTEREST, 
                                SocialMedia.WHATSAPP], 
                                icon_height=6, 
                                y_position=227, 
                                labels=[f"{persona.twitter}%",
                                f"{persona.facebook}%",
                                f"{persona.youtube}%",
                                f"{persona.snapchat}%",
                                f"{persona.spotify}%",
                                f"{persona.instagram}%",
                                f"{persona.pinterest}%",
                                f"{persona.whatsapp}%"])

    pdf.output("hello_world.pdf")