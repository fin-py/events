import asyncio
import time

import aiohttp


async def get_status_code(n):
    url = f"https://httpbin.org/delay/{n}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print("Status:", response.status)


async def main(*args):
    task = [asyncio.create_task(get_status_code(i)) for i in args]
    await asyncio.gather(*task)


start = time.time()
asyncio.run(main(3, 5))
print(f"time: {time.time() - start}")
