import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)


async def main():
    task1 = asyncio.create_task(neru(2))
    task2 = asyncio.create_task(neru(5))
    await asyncio.gather(task1, task2)


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
