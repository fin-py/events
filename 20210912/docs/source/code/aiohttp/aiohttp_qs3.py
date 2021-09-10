import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        params = {"limit": "10", "offset": "20"}
        async with session.get(
            "https://pokeapi.co/api/v2/pokemon", params=params
        ) as resp:
            print(resp.status)
            print(await resp.json())


asyncio.run(main())

