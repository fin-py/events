import asyncio
import time


async def neru(n):
    time.sleep(n)


async def main():
    asyncio.gather(asyncio.create_task(neru(2)), asyncio.create_task(neru(3)))


start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print(f"time: {time.time() - start}")

