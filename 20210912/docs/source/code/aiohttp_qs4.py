import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pokeapi.co/api/v2/pokemon/25") as resp:
            with open("/tmp/pikachu.png", "wb") as f:
                html = await resp.json()
                async with session.get(html["sprites"]["front_default"]) as png:
                    f.write(await png.read())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

