import time
import asyncio
import aiohttp

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


async def get_pokemon(s, url):
    async with s.get(url) as resp:
        pokemon = await resp.json()
        return (pokemon["id"], pokemon["name"])


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = list()
        for num in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            tasks.append(asyncio.create_task(get_pokemon(session, url)))

        for pokemon in asyncio.as_completed(tasks):
            results = await pokemon
            print(results)


start = time.time()
asyncio.run(main())
logging.info("end")
end = time.time()
logging.info(f"実行結果: time: {end-start}")
