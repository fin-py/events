import asyncio
import time


async def main():
    await asyncio.create_task(asyncio.sleep(2))
    await asyncio.create_task(asyncio.sleep(5))


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
