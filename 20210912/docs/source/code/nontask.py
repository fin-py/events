import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)


async def main():
    await neru(2)
    await neru(3)


start = time.time()
asyncio.run(main(), debug=True)
print(f"time: {time.time() - start}")
