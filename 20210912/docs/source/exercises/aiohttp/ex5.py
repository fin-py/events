import json
import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        params = {"keyword": "aiohttp"}
        async with session.get(
            "https://connpass.com/api/v1/event/", params=params
        ) as resp:
            html = await resp.text()
            to_dict = json.loads(html)
            print([id["event_id"] for id in to_dict["events"]])


asyncio.run(main())
