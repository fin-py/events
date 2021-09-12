import asyncio
import time


async def neru(n):
    time.sleep(n)


async def main():
    await asyncio.create_task(neru(2))
    await asyncio.create_task(neru(5))


start = time.time()
asyncio.run(main(), debug=True)
print(f"time: {time.time() - start}")
