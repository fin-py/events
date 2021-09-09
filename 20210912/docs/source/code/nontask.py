import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)


async def main():
    await neru(2)
    await neru(5)


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
