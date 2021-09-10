import asyncio
import aiohttp


async def main():
    session = aiohttp.ClientSession()
    resp = await session.get("http://httpbin.org/get")
    print(await resp.json())
    await session.close()

asyncio.run(main())