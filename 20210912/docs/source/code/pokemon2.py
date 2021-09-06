import time 
import asyncio

import aiohttp 
from logzero import logger 

async def main():
    async with aiohttp.ClientSession() as s: 
        for num in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            async with s.get(url) as resp:
                pokemon = await resp.json()
                logger.info(f"{pokemon['id']}: {pokemon['name']}")

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    logger.info(end-start)
