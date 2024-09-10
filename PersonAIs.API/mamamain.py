import asyncio
from services import get_aptos_font
from services import create_persona_file

async def main():
    await setup()
    await create_persona_file.generate()

async def setup():
    await get_aptos_font.get_font()

asyncio.run(main())