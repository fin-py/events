import asyncio
import time


async def neru(n):
    loop.run_in_executor(None, time.sleep, n)


async def main():
    asyncio.gather(asyncio.create_task(neru(3)), asyncio.create_task(neru(5)))


start = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.run_until_complete(loop.shutdown_default_executor())
print(f"time: {time.time() - start}")