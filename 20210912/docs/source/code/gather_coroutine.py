import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)


async def main():
    await asyncio.gather(neru(2), neru(3))


start = time.time()
asyncio.run(main(), debug=True)
print(f"time: {time.time() - start}")
