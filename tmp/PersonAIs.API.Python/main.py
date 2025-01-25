import asyncio
from models.persona import json_to_persona
from services import create_persona_file, get_aptos_font


async def main():
    
    
    jsona = """{
      "information": {
        "generate_portrait_prompt": "Ein detaillierter Promt um das Profil Bild zu generieren",
        "first_name": "Vorname",
        "last_name": "Nachname",
        "profession": "Beruf",
        "degree": "Höchster Bildungsabschluss",
        "age": 0,
        "residence": "Wohnort",
        "marital_status": "Familienstand",
        "self_description": "Selbstbeschreibung",
        "bio": "Kurze Biographie",
        "goals": ["Ziel 1", "Ziel 2", "Ziel 3"],
        "motivations": ["Motivation 1", "Motivation 2", "Motivation 3"],
        "challenges": ["Herausforderung 1", "Herausforderung 2", "Herausforderung 3"],
        "characteristics": ["Eigenschaft 1", "Eigenschaft 2", "Eigenschaft 3"],
        "hobbies": ["Hobby 1", "Hobby 2", "Hobby 3"],
        "subscribed_accounts": ["@Aboniertes Konto 1", "@Aboniertes Konto 2", "@Aboniertes Konto 3"],
        "hashtags": ["Hashtag 1", "Hashtag 2", "Hashtag 3"],
        "favorite_brands": ["Marke 1", "Marke 2", "Marke 3"],
        "favorite_apps": ["App 1", "App 2", "App 3"]
      },
      "technology_usage": {
        "devices": ["IPHONE", "ANDROID", "MAC", "WINDOWS"]
      },
      "digital_skills": {
        "technology": 0,
        "software_and_apps": 0,
        "internet": 0,
        "social_network": 0
      },
      "personality": {
        "extroverted_or_introverted": 0,
        "planner_or_spontaneous": 0,
        "thinking_or_feeling": 0,
        "conservative_or_liberal": 0,
        "leader_or_follower": 0
      },
      "browser_preferences": {
        "browsers": ["CHROME", "SAFARI", "FIREFOX", "OPERA", "EDGE"]
      },
      "app_usage": {
        "twitter": 0,
        "facebook": 0,
        "youtube": 0,
        "snapchat": 0,
        "spotify": 0,
        "instagram": 0,
        "pinterest": 0,
        "whatsapp": 0
      }
    }"""

    await create_persona_file.generate(json_to_persona(jsona))

async def setup():
  await get_aptos_font.get_font()
  await main()

asyncio.run(setup())