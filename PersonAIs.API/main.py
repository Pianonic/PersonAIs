import asyncio
from enums.browser import Browser
from enums.technology import Technology
from models.persona import Persona
from services import get_aptos_font
from services import create_persona_file

async def main():
    await setup()

    # persona = Persona(
    #     generate_portrait_prompt="A tech-savvy young professional with a passion for social media and digital trends.",
    #     first_name="Alex",
    #     last_name="Smith",
    #     profession="Digital Marketing Specialist",
    #     degree="Bachelor's in Marketing",
    #     age=28,
    #     residence="San Francisco, CA",
    #     marital_status="Single",
    #     self_description="Creative, driven, and always up-to-date with the latest trends in digital marketing.",
    #     bio="Alex is a digital marketing specialist with a knack for social media strategies and a deep understanding of consumer behavior.",
    #     goals=["Become a marketing director", "Expand professional network", "Enhance digital skills"],
    #     motivations=["Career advancement", "Creative expression", "Networking opportunities"],
    #     challenges=["Keeping up with trends", "Work-life balance", "Managing multiple projects"],
    #     characteristics=["Innovative", "Detail-oriented", "Adaptable"],
    #     hobbies=["Photography", "Traveling", "Gaming"],
    #     subscribed_accounts=["TechCrunch", "MarketingProfs", "AdAge"],
    #     hashtags=["#DigitalMarketing", "#SocialMedia", "#TechTrends"],
    #     favorite_brands=["Apple", "Nike", "Adobe"],
    #     favorite_apps=["LinkedIn", "Slack", "Zoom"],
    #     devices=[Technology.ANDROID, Technology.WINDOWS, Technology.MAC],
    #     technology=85,
    #     software_and_apps=90,
    #     internet=95,
    #     social_network=80,
    #     extroverted_or_introverted=60,
    #     planner_or_spontaneous=70,
    #     thinking_or_feeling=50,
    #     conservative_or_liberal=40,
    #     leader_or_follower=55,
    #     browsers=[Browser.CHROME, Browser.SAFARI, Browser.OPERA],
    #     twitter=60,
    #     facebook=40,
    #     youtube=70,
    #     snapchat=30,
    #     spotify=50,
    #     instagram=80,
    #     pinterest=25,
    #     whatsapp=65
    # )

    persona = Persona(
        generate_portrait_prompt="A tech-savvy young professional with a passion for social media and digital trends.",
        first_name="Alex",
        last_name="Smith",
        profession="Digital Marketing Specialist",
        degree="Bachelor's in Marketing",
        age=28,
        residence="San Francisco, CA",
        marital_status="Single",
        self_description="Ich liebe es, kreative Lösungen für komplexe Probleme zu finden und dabei immer den Kunden im Fokus zu behalten.",
        bio="Anna Müller, 34, aus Zürich, arbeitet seit fünf Jahren als Marketing Managerin. Sie ist verheiratet, hat zwei Kinder und jongliert Karriere und Familie. Aktuell denkt sie über die Balance zwischen Beruf und Familie sowie die nächste grosse Marketingkampagne nach.",
        goals=["Become a marketing director", "Expand professional network", "Enhance digital skills"],
        motivations=["Career advancement", "Creative expression", "Networking opportunities"],
        challenges=["Keeping up with trends", "Work-life balance", "Managing multiple projects"],
        characteristics=["Innovative", "Detail-oriented", "Adaptable"],
        hobbies=["Photography", "Traveling", "Gaming"],
        subscribed_accounts=["TechCrunch", "MarketingProfs", "AdAge"],
        hashtags=["#DigitalMarketing", "#SocialMedia", "#TechTrends"],
        favorite_brands=["Apple", "Nike", "Adobe"],
        favorite_apps=["LinkedIn", "Slack", "Zoom"],
        devices=[Technology.ANDROID, Technology.WINDOWS, Technology.MAC],
        technology=85,
        software_and_apps=90,
        internet=95,
        social_network=80,
        extroverted_or_introverted=60,
        planner_or_spontaneous=70,
        thinking_or_feeling=50,
        conservative_or_liberal=40,
        leader_or_follower=55,
        browsers=[Browser.CHROME, Browser.SAFARI, Browser.OPERA],
        twitter=60,
        facebook=40,
        youtube=70,
        snapchat=30,
        spotify=50,
        instagram=80,
        pinterest=25,
        whatsapp=65
    )

    await create_persona_file.generate(persona)

async def setup():
    await get_aptos_font.get_font()

asyncio.run(main())