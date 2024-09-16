import json
from dataclasses import dataclass
from typing import List
from enums.browser import Browser
from enums.technology import Technology

@dataclass
class Information:
  generate_portrait_prompt: str
  first_name: str
  last_name: str
  profession: str
  degree: str
  age: int
  residence: str
  marital_status: str
  self_description: str
  bio: str
  goals: List[str]
  motivations: List[str]
  challenges: List[str]
  characteristics: List[str]
  hobbies: List[str]
  subscribed_accounts: List[str]
  hashtags: List[str]
  favorite_brands: List[str]
  favorite_apps: List[str]

@dataclass
class TechnologyUsage:
  devices: List[Technology]

@dataclass
class DigitalSkills:
  technology: int
  software_and_apps: int
  internet: int
  social_network: int

@dataclass
class Personality:
  extroverted_or_introverted: int
  planner_or_spontaneous: int
  thinking_or_feeling: int
  conservative_or_liberal: int
  leader_or_follower: int

@dataclass
class BrowserPreferences:
  browsers: List[Browser]

@dataclass
class AppUsage:
  twitter: int
  facebook: int
  youtube: int
  snapchat: int
  spotify: int
  instagram: int
  pinterest: int
  whatsapp: int

@dataclass
class Persona:
  information: Information
  technology_usage: TechnologyUsage
  digital_skills: DigitalSkills
  personality: Personality
  browser_preferences: BrowserPreferences
  app_usage: AppUsage

def json_to_persona(json_data: str) -> Persona:
    data = json.loads(json_data)

    # Convert technology usage
    try:
        data['technology_usage']['devices'] = [Technology[tech] for tech in data['technology_usage']['devices']]
    except KeyError as e:
        raise ValueError(f"Invalid technology enum value: {e}")

    # Convert browser preferences
    try:
        data['browser_preferences']['browsers'] = [Browser[br] for br in data['browser_preferences']['browsers']]
    except KeyError as e:
        raise ValueError(f"Invalid browser enum value: {e}")

    # Create dataclass instances
    information = Information(**data['information'])
    technology_usage = TechnologyUsage(**data['technology_usage'])
    digital_skills = DigitalSkills(**data['digital_skills'])
    personality = Personality(**data['personality'])
    browser_preferences = BrowserPreferences(**data['browser_preferences'])
    app_usage = AppUsage(**data['app_usage'])

    persona = Persona(
        information=information,
        technology_usage=technology_usage,
        digital_skills=digital_skills,
        personality=personality,
        browser_preferences=browser_preferences,
        app_usage=app_usage
    )

    return persona

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
    "devices": ["IPHONE", "MAC", "WINDOWS"]
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
    "browsers": ["CHROME", "SAFARI", "FIREFOX"]
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

#print(json_to_persona(jsona))