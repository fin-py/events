import asyncio


async def func(n):
    print(n)


async def main(*args):
    await func(args[0])
    await func(args[1])


asyncio.run(main("1こめ", "2こめ"))
