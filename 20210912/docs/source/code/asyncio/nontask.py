import asyncio
import time


async def main():
    await asyncio.sleep(2)
    await asyncio.sleep(5)


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
