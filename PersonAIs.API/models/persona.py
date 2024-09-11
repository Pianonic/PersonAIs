import json
from dataclasses import dataclass
from typing import List
from enums.browser import Browser
from enums.technology import Technology

@dataclass
class Persona:
    # Information
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

    # Technology
    devices: List[Technology]

    # Digital Skills (in %)
    technology: int
    software_and_apps: int
    internet: int
    social_network: int

    # Personality (in %)
    extroverted_or_introverted: int
    planner_or_spontaneous: int
    thinking_or_feeling: int
    conservative_or_liberal: int
    leader_or_follower: int

    # Browser
    browsers: List[Browser]

    # App Usage (in %)
    twitter: int
    facebook: int
    youtube: int
    snapchat: int
    spotify: int
    instagram: int
    pinterest: int
    whatsapp: int

def json_to_persona(json_data: str) -> Persona:
    data = json.loads(json_data)
    
    # Convert list of strings to Technology enum objects
    data['devices'] = [Technology[tech] for tech in data['devices']]
    
    # Convert list of strings to Browser enum objects
    data['browsers'] = [Browser[br] for br in data['browsers']]
    
    # Create Persona object using the parsed data
    persona = Persona(**data)
    
    return persona