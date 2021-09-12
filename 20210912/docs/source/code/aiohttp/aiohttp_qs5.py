import asyncio
import aiohttp


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/events") as resp:
            with open("/tmp/bigfile.txt", "wb") as f:
                while True:
                    chunk = await resp.content.read(100)  # 100b, -1 ですべて
                    # print(len(chunk))
                    if not chunk:
                        print("No chunk")
                        break
                    f.write(chunk)


asyncio.run(main())
