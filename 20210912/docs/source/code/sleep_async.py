import asyncio
import time


async def func(cor_name, n):
    for i in range(n):
        print(f"{cor_name}: {i}")
        # time.sleep(1)
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(func("cor1", 3), func("cor2", 3))


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
