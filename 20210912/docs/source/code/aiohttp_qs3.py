import asyncio
import aiohttp
from pprint import pprint


async def main():
    async with aiohttp.ClientSession() as session:
        params = {"limit": "10", "offset": "20"}
        async with session.get(
            "https://pokeapi.co/api/v2/pokemon", params=params
        ) as resp:
            print(resp.status)
            pprint(await resp.json())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

