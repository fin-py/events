import asyncio
import time


async def main():
    await asyncio.wait_for(asyncio.sleep(3), timeout=1)


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
