from PIL import Image, ImageDraw
from io import BytesIO
from fpdf import FPDF
from enums.technology import Technology

technologies = [Technology.ANDROID,]

async def transform_profile_picture() -> BytesIO:
    img = Image.open(r'F:\Coding\PersonAIs\PersonAIs.API\image\image.png').convert("RGBA")

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

async def load_image_from_enum(enum: Technology) -> BytesIO:
    with open(enum.value, 'rb') as file:
        return BytesIO(file.read())
    
async def generate():
    pdf = FPDF()
    pdf.add_font('Aptos', '', './fonts/Aptos.ttf', uni=True)
    pdf.add_font('Aptos-Bold', '', './fonts/Aptos-Bold.ttf', uni=True)
    pdf.add_page()

    pdf.set_fill_color(21, 96, 130)

    pdf.rect(0, 0, pdf.w/3, pdf.h, "F")

    img_data = await transform_profile_picture()
    pdf.image(img_data, x=15, y=1, w=40)

    pdf.set_fill_color(44, 134, 175)
    pdf.rect(0, 42, pdf.w/3, 25, "F")

    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Aptos-Bold', size=20)
    
    pdf.text(3, 50, txt="Anna Müller")

    pdf.set_font('Aptos', size=12)
    pdf.text(3, 57, txt="Marketing Managerin")
    pdf.text(3, 64, txt="Master in Betriebswirtschaftslehre")
    
    pdf.set_font('Aptos-Bold', size=20)
    pdf.text(3, 75, txt="Technologie")

    if(len(technologies) == 4):
        print(4)
    elif(len(technologies) == 3):
        print(3)
    elif(len(technologies) == 2):
        print(2)
        pdf.image(await load_image_from_enum(Technology.ANDROID), 30, 30, 20)
    elif(len(technologies) == 1):
        print(1)
        pdf.image(await load_image_from_enum(Technology.ANDROID), 30, 80, 10)

    pdf.output("hello_world.pdf")