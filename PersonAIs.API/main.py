import asyncio
import json
from openai import OpenAI

from models.persona import json_to_persona
from services import create_persona_file, get_aptos_font

# def generate_persona_part(client, part_name, prompt, context_text):
#     response = client.chat.completions.create(
#         model="lmstudio-community/Phi-3.1-mini-4k-instruct-GGUF",
#         messages=[
#             {"role": "system", "content": f"Du bist jetzt ein Persona-Generator. Generiere den {part_name} basierend auf dem folgenden Prompt: {prompt}"},
#             {"role": "user", "content": context_text}
#         ],
#         temperature=0.7,
#     )
#     return response.choices[0].message

async def main():
    # client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

    # # Initialisiere das JSON-Dokument
    # persona_json = {
    #     "information": {},
    #     "technology_usage": {},
    #     "digital_skills": {},
    #     "personality": {},
    #     "browser_preferences": {},
    #     "app_usage": {}
    # }

    # # Definition der Prompts
    # prompts = {
    #     "information": {
    #         "generate_portrait_prompt": "Ein detailliertes Portrait der Person erstellen",
    #         "first_name": "Vorname der Person",
    #         "last_name": "Nachname der Person",
    #         "profession": "Beruf der Person",
    #         "degree": "Höchster Bildungsabschluss der Person",
    #         "age": "Alter der Person",
    #         "residence": "Wohnort der Person",
    #         "marital_status": "Familienstand der Person",
    #         "self_description": "Selbstbeschreibung der Person",
    #         "bio": "Kurze Biographie der Person",
    #         "goals": "Ziele der Person (3 Ziele)",
    #         "motivations": "Motivationen der Person (3 Motivationen)",
    #         "challenges": "Herausforderungen der Person (3 Herausforderungen)",
    #         "characteristics": "Eigenschaften der Person (3 Eigenschaften)",
    #         "hobbies": "Hobbys der Person (3 Hobbys)",
    #         "subscribed_accounts": "Abonnierte Konten der Person (3 Konten)",
    #         "hashtags": "Hashtags der Person (3 Hashtags)",
    #         "favorite_brands": "Lieblingsmarken der Person (3 Marken)",
    #         "favorite_apps": "Lieblings-Apps der Person (3 Apps)"
    #     },
    #     "technology_usage": {
    #         "devices": "Verwendete Geräte der Person (3 Geräte)"
    #     },
    #     "digital_skills": {
    #         "technology": "Digitale Fähigkeiten der Person in Technologie (0-100)",
    #         "software_and_apps": "Digitale Fähigkeiten der Person in Software und Apps (0-100)",
    #         "internet": "Digitale Fähigkeiten der Person im Internet (0-100)",
    #         "social_network": "Digitale Fähigkeiten der Person in sozialen Netzwerken (0-100)"
    #     },
    #     "personality": {
    #         "extroverted_or_introverted": "Persönlichkeit der Person: extrovertiert oder introvertiert (0-100)",
    #         "planner_or_spontaneous": "Persönlichkeit der Person: Planer oder spontan (0-100)",
    #         "thinking_or_feeling": "Persönlichkeit der Person: denkend oder fühlend (0-100)",
    #         "conservative_or_liberal": "Persönlichkeit der Person: konservativ oder liberal (0-100)",
    #         "leader_or_follower": "Persönlichkeit der Person: Anführer oder Anhänger (0-100)"
    #     },
    #     "browser_preferences": {
    #         "browsers": "Bevorzugte Browser der Person (3 Browser)"
    #     },
    #     "app_usage": {
    #         "twitter": "Nutzung von Twitter in Prozent",
    #         "facebook": "Nutzung von Facebook in Prozent",
    #         "youtube": "Nutzung von YouTube in Prozent",
    #         "snapchat": "Nutzung von Snapchat in Prozent",
    #         "spotify": "Nutzung von Spotify in Prozent",
    #         "instagram": "Nutzung von Instagram in Prozent",
    #         "pinterest": "Nutzung von Pinterest in Prozent",
    #         "whatsapp": "Nutzung von WhatsApp in Prozent"
    #     }
    # }

    # # Generiere die einzelnen Teile des JSON
    # for section, prompts_dict in prompts.items():
    #     for key, prompt in prompts_dict.items():
    #         context_text = json.dumps(persona_json) if section in persona_json else ''
    #         part = generate_persona_part(client, key, prompt, context_text)
    #         # Füge die generierten Daten in das JSON-Dokument ein
    #         if section not in persona_json:
    #             persona_json[section] = {}
    #         persona_json[section][key] = part

    # print(json.dumps(persona_json, indent=4))
    
    jsona = """{
  "information": {
    "generate_portrait_prompt": "Erstelle ein Bild einer Person mit kurzen braunen Haaren, Brille und einem freundlichen Lächeln. Die Person trägt ein einfaches, modernes Outfit und wirkt engagiert und interessiert. Die Person steht vor einem Computerbildschirm und sieht konzentriert aus.",
    "first_name": "Anna",
    "last_name": "Müller",
    "profession": "Informatik-Berufslernende",
    "degree": "Berufsausbildung",
    "age": 20,
    "residence": "Zürich",
    "marital_status": "Ledig",
    "self_description": "Ich bin eine motivierte Informatik-Lernende, die gerne neue Technologien ausprobiert und ihre Fähigkeiten ständig verbessert.",
    "bio": "Anna ist eine engagierte und technikbegeisterte junge Frau, die in Zürich lebt und ihre Ausbildung im Bereich Informatik macht. Sie interessiert sich besonders für Softwareentwicklung und Datenanalyse.",
    "goals": ["Effiziente Projektverwaltung", "Schneller Fortschritt bei Modulen", "Optimierung der Lernmethoden"],
    "motivations": ["Erfolgreiche Prüfungen", "Lernen von neuen Technologien", "Karriereaufstieg"],
    "challenges": ["Zeitmanagement", "Überwältigende Menge an Aufgaben", "Selbstdisziplin"],
    "characteristics": ["Analytisch", "Zielorientiert", "Technikaffin"],
    "hobbies": ["Lesen", "Programmieren", "Wandern"],
    "subscribed_accounts": ["@Tim Cook", "@Mark Zuckerberg", "@Linus Torvalds"],
    "hashtags": ["#Techie", "#Programming", "#Learning"],
    "favorite_brands": ["Apple", "Google", "Microsoft"],
    "favorite_apps": ["VS Code", "Slack", "Trello"]
  },
  "technology_usage": {
    "devices": ["IPHONE", "MAC", "WINDOWS"]
  },
  "digital_skills": {
    "technology": 89,
    "software_and_apps": 92,
    "internet": 87,
    "social_network": 60
  },
  "personality": {
    "extroverted_or_introverted": 30,
    "planner_or_spontaneous": 70,
    "thinking_or_feeling": 60,
    "conservative_or_liberal": 40,
    "leader_or_follower": 50
  },
  "browser_preferences": {
    "browsers": ["EDGE", "SAFARI"]
  },
  "app_usage": {
    "twitter": 10,
    "facebook": 20,
    "youtube": 25,
    "snapchat": 5,
    "spotify": 15,
    "instagram": 10,
    "pinterest": 5,
    "whatsapp": 10
  }
}
"""

    await create_persona_file.generate(json_to_persona(jsona))

async def setup():
    await get_aptos_font.get_font()

asyncio.run(main())