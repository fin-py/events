import time
import asyncio

import aiohttp
from logzero import logger


async def get_pokemon(s, url):
    async with s.get(url) as resp:
        pokemon = await resp.json()
        return (pokemon["id"], pokemon["name"])


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = list()
        for num in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            tasks.append(asyncio.ensure_future(get_pokemon(session, url)))

        pokemons = await asyncio.gather(*tasks)
        for pokemon in pokemons:
            logger.info(f"{id}: {pokemon}")


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    logger.info("end")
    end = time.time()
    logger.info(end - start)
