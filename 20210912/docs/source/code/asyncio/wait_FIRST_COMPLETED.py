import asyncio
import time
from asyncio.tasks import FIRST_COMPLETED


async def main():
    tasks = [
        asyncio.create_task(asyncio.sleep(1)),
        asyncio.create_task(asyncio.sleep(3)),
    ]
    done, pending = await asyncio.wait(tasks, timeout=2, return_when=FIRST_COMPLETED)

    for t in tasks:
        print(f"{t} in done: {t in done}")
        print(f"{t} in pending: {t in pending}")


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
