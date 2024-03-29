import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://pokeapi.co/api/v2/pokemon/25") as resp:
            html = await resp.json()
            async with session.get(html["sprites"]["front_default"]) as png:
                with open("/tmp/pikachu.png", "wb") as f:
                    f.write(await png.read())


asyncio.run(main())
