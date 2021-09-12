import asyncio
import time


async def main():
    await asyncio.gather(asyncio.sleep(2), asyncio.sleep(5))


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
