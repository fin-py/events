import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/events") as resp:
            with open("/tmp/bigfile.json", "wb") as f:
                chunk = await resp.content.read(100)  # 100kb, -1 ですべて
                if not chunk:
                    print("No chunk")
                f.write(chunk)


asyncio.run(main())
