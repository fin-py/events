import asyncio
import aiohttp


async def main():
    session = aiohttp.ClientSession()
    async with session.get("http://httpbin.org/get") as resp:
        print(resp.status)
        print(await resp.json())
    await session.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
