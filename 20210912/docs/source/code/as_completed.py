import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)
    return n


async def main():
    for f in asyncio.as_completed([neru(2), neru(4), neru(1)], timeout=3):
        result = await f
        print(f"{result=}")


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
