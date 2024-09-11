import enum
from typing import List, Optional
from PIL import Image, ImageDraw
from io import BytesIO
from fpdf import FPDF
from enums.info import Info
from enums.social_media import SocialMedia
from enums.technology import Technology
from models.persona import Persona

SIDENAV_WIDTH = 0

def draw_percentage_bar(pdf: FPDF, label: str, percentage: int, x: int, y: int):
    pdf.set_font('Aptos', size=12)
    pdf.text(x, y, txt=label)
    
    pdf.set_font('Aptos', size=6)
    pdf.text(SIDENAV_WIDTH - 8, y + 1, txt=f'{percentage}%')

    pdf.set_fill_color(200, 200, 200)
    pdf.rect(x, y + 2, SIDENAV_WIDTH - 6, 1, "F")

    pdf.set_fill_color(255, 255, 255)
    pdf.rect(x, y + 2, (((SIDENAV_WIDTH)/100) * percentage) - 6, 1, "F")

def draw_rather_bar(pdf: FPDF, label1: str, label2: str, percentage: int, x: int, y: int):
    pdf.set_xy(2, y - 3)
    pdf.set_font('Aptos', size=12)
    pdf.cell(w=pdf.w/6.4, text=label1, align='L')
    pdf.cell(w=pdf.w/6.4, text=label2, align='R')

    line_width = SIDENAV_WIDTH - 6
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

async def draw_enum_icons(pdf: FPDF, technologies: List[Technology], icon_height: int = 12, y_position: int = 0, x_position: int = 0, available_width: int = 0, labels: Optional[List[str]] = None):
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
    
    remaining_space = available_width - total_icon_width
    gap_size = remaining_space / (len(technologies) + 1)

    x = gap_size
    label_height = 5

    for i, technology in enumerate(technologies):
        image_data, size = await load_image_and_size_from_enum(technology)
        old_width, old_height = size
        aspect_ratio = old_width / old_height
        new_width = aspect_ratio * new_height

        pdf.image(image_data, x=x + x_position, y=y_position, h=new_height)

        if labels:
            pdf.set_y(y_position + new_height + 1)
            pdf.set_x(x + x_position)
            pdf.set_font('Arial', 'B', 8)
            pdf.cell(new_width, label_height, labels[i], 0, 1, 'C')

        x += new_width + gap_size

async def draw_bullet_list(pdf: FPDF, items, bullet='•', x_position: int = 0, y_position: int = 0, max_width: int = 10):
    for item in items:
        pdf.set_xy(x_position, y_position)
        pdf.multi_cell(max_width, text=f"{bullet} {item}", align='L')
        y_position = y_position + 6

async def generate(persona: Persona):
    global SIDENAV_WIDTH
    pdf = FPDF()
    pdf.add_font('Aptos', '', './fonts/Aptos.ttf', uni=True)
    pdf.add_font('Aptos-Bold', '', './fonts/Aptos-Bold.ttf', uni=True)
    pdf.add_page()

    SIDENAV_WIDTH = pdf.w / 3
    MAIN_WIDTH = pdf.w - SIDENAV_WIDTH
    MAIN_START_WITH_GAP = SIDENAV_WIDTH + 3

    BORDER_GAP = 3

    SINGLE_TEXT_WIDTH = MAIN_WIDTH - 5
    DUAL_TEXT_WIDTH = SINGLE_TEXT_WIDTH / 2

    # Sidenav Section
    pdf.set_fill_color(21, 96, 130)
    pdf.rect(0, 0, SIDENAV_WIDTH, pdf.h, "F")

    # Profile picture Section
    img_data = await transform_profile_picture()
    pdf.image(img_data, x=15, y=1, w=40)

    # Accent Rectangle Section
    pdf.set_fill_color(44, 134, 175)
    pdf.rect(0, 42, SIDENAV_WIDTH, 25, "F")

    # Name, Title, and Education Section
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(BORDER_GAP, 50, txt=f"{persona.first_name} {persona.last_name}")

    pdf.set_font('Aptos', size=12)
    pdf.text(BORDER_GAP, 57, txt=persona.profession)
    pdf.text(BORDER_GAP, 64, txt=persona.degree)

    # Technologies Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(BORDER_GAP, 75, txt="Technologie")

    await draw_enum_icons(pdf, persona.devices, icon_height=12, y_position=81, available_width=SIDENAV_WIDTH)

    # Digital Skills Section 
    pdf.text(BORDER_GAP, 105, txt="Digitale Fähigkeiten")

    draw_percentage_bar(pdf, "Technologie", persona.technology, BORDER_GAP, 112)
    draw_percentage_bar(pdf, "Software und Apps", persona.software_and_apps, BORDER_GAP, 121)
    draw_percentage_bar(pdf, "Internet", persona.internet, BORDER_GAP, 130)
    draw_percentage_bar(pdf, "Social Network", persona.social_network, BORDER_GAP, 139)

    # Personality Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(BORDER_GAP, 155, txt="Persönlichkeit")

    draw_rather_bar(pdf, "Extrovertiert", "Introvertiert", persona.extroverted_or_introverted, 3, 161)
    draw_rather_bar(pdf, "Planer", "Spontan", persona.planner_or_spontaneous, BORDER_GAP, 170)
    draw_rather_bar(pdf, "Denken", "Fühlen", persona.thinking_or_feeling, BORDER_GAP, 179)
    draw_rather_bar(pdf, "Konservativ", "Liberal", persona.conservative_or_liberal, BORDER_GAP, 188)
    draw_rather_bar(pdf, "Anführer", "Nachahmer", persona.leader_or_follower, BORDER_GAP, 197)

    # Browser Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(BORDER_GAP, 212, txt="Browser")

    await draw_enum_icons(pdf, persona.browsers, icon_height=9, y_position=216, available_width=SIDENAV_WIDTH)

    # Appusage Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(BORDER_GAP, 234, txt="Appausnutzung")
    
    await draw_enum_icons(pdf, [SocialMedia.TWITTER, 
                                SocialMedia.FACEBOOK, 
                                SocialMedia.YOUTUBE,
                                SocialMedia.SNAPCHAT, 
                                SocialMedia.SPOTIFY, 
                                SocialMedia.INSTAGRAM, 
                                SocialMedia.PINTEREST, 
                                SocialMedia.WHATSAPP], 
                                icon_height=6, 
                                y_position=238, 
                                labels=[f"{persona.twitter}%",
                                f"{persona.facebook}%",
                                f"{persona.youtube}%",
                                f"{persona.snapchat}%",
                                f"{persona.spotify}%",
                                f"{persona.instagram}%",
                                f"{persona.pinterest}%",
                                f"{persona.whatsapp}%"],
                                available_width=SIDENAV_WIDTH)

    # Self Description Section
    pdf.set_xy(SIDENAV_WIDTH, 9)
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Aptos', size=12)

    pdf.multi_cell(w=MAIN_WIDTH, txt=persona.self_description, align='C')

    # Accent Rectangle Section
    pdf.set_fill_color(44, 134, 175)
    pdf.rect(SIDENAV_WIDTH, 42, MAIN_WIDTH, -15, "F")

    # Info Section
    pdf.set_text_color(255, 255, 255)
    available_big_width = MAIN_WIDTH
    await draw_enum_icons(pdf, 
                          [Info.BIRTHDAY, Info.LOCATION, Info.MARIAGE], 
                            icon_height=6, 
                            y_position=29, 
                            x_position=SIDENAV_WIDTH,
                            labels=[f"{persona.age} Jahre", persona.residence, persona.marital_status], 
                            available_width=available_big_width)

    # Bio Section
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(SIDENAV_WIDTH + BORDER_GAP, 51, txt="Szenario/Bio")

    pdf.set_xy(SIDENAV_WIDTH + 2, 54)
    pdf.set_font('Aptos', size=12)
    pdf.multi_cell(w=SINGLE_TEXT_WIDTH, txt=persona.bio, align='J')

    # Goals and Motivation Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP, 80, txt="Ziele")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.goals, x_position = MAIN_START_WITH_GAP, y_position=83, max_width=DUAL_TEXT_WIDTH)

    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, 80, txt="Motivation")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.motivations, x_position = MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, y_position=83, max_width=DUAL_TEXT_WIDTH)

    # Challenges Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP, 109, txt="Herausforderungen")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.challenges, x_position = MAIN_START_WITH_GAP, y_position=112, max_width=SINGLE_TEXT_WIDTH)

    # Character and Hobbies Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP, 137, txt="Charakter")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.characteristics, x_position = MAIN_START_WITH_GAP, y_position=140, max_width=DUAL_TEXT_WIDTH)

    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, 137, txt="Hobbys")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.hobbies, x_position = MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, y_position=140, max_width=DUAL_TEXT_WIDTH)

    # Subscribed Accounts and Hashtags Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP, 165, txt="Abos")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.subscribed_accounts, x_position = MAIN_START_WITH_GAP, y_position=168, max_width=DUAL_TEXT_WIDTH)

    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, 165, txt="Hashtags")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.hashtags, x_position = MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, y_position=168, max_width=DUAL_TEXT_WIDTH)

    # Favorite Brands and Apps Section
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP, 194, txt="Lieblingsmarken")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.favorite_brands, x_position = MAIN_START_WITH_GAP, y_position=197, max_width=DUAL_TEXT_WIDTH)

    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, 194, txt="Lieblingsapps")

    pdf.set_font('Aptos', size=12)
    await draw_bullet_list(pdf, persona.favorite_apps, x_position = MAIN_START_WITH_GAP + DUAL_TEXT_WIDTH, y_position=197, max_width=DUAL_TEXT_WIDTH)

    pdf.output("hello_world.pdf")