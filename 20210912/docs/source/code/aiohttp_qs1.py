import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("http://httpbin.org/get") as resp:
            print(resp.status)
            print(await resp.json())


loop = asyncio.get_event_loop()
loop.run_until_complete(main())

