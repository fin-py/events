import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)


async def main():
    task1 = asyncio.create_task(neru(2))
    task2 = asyncio.create_task(neru(5))
    await task1
    await task2


start = time.time()
asyncio.run(main(), debug=True)
print(f"time: {time.time() - start}")
