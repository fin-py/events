import asyncio
import time


async def neru(n):
    await asyncio.sleep(n)
    1 / (n % 2)
    return n


async def main():
    for f in asyncio.as_completed([neru(1), neru(3), neru(2)]):
        try:
            result = await f
        except ZeroDivisionError as e:
            result = e
        print(f"{result=}")


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
