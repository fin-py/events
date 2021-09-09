import asyncio
import time


async def neru(loop, n):
    loop.run_in_executor(None, time.sleep, n)


async def main():
    loop = asyncio.get_event_loop()
    await neru(loop, 2)
    await neru(loop, 3)


start = time.time()
asyncio.run(main(), debug=True)
print(f"time: {time.time() - start}")
