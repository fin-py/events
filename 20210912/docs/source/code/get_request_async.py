import asyncio
import time
import urllib.request


def _get_status_code(url):
    with urllib.request.urlopen(url) as res:
        return res.status


async def get_status_code(cor_name, n):
    loop = asyncio.get_event_loop()
    url = f"https://httpbin.org/delay/{n}"
    http_status = await loop.run_in_executor(None, _get_status_code, url)
    print(f"{cor_name}: {http_status}")


async def main():
    await asyncio.gather(
        get_status_code("cor1", 2), get_status_code("cor2", 5)
    )


start = time.time()
asyncio.run(main())
print(f"time: {time.time() - start}")
