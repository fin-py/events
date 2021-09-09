import asyncio
import time

import aiohttp


async def get_status_code(n):
    url = f"https://httpbin.org/delay/{n}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:

            print("Status:", response.status)


start = time.time()
asyncio.run(get_status_code(3))
print(f"time: {time.time() - start}")
