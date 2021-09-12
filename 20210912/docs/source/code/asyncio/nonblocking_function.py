import asyncio
import time


async def neru(n):
    loop = asyncio.get_running_loop()
    loop.run_in_executor(None, time.sleep, n)


async def main():
    await asyncio.create_task(neru(3))
    await asyncio.create_task(neru(5))


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
