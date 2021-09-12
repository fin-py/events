import os
import asyncio
import aiohttp


async def get_pokemon(s, url, dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

    async with s.get(url) as resp:
        html = await resp.json()
        name = html["name"]
        async with s.get(html["sprites"]["front_default"]) as png:
            with open(os.path.join(dir, f"{name}.png"), "wb") as f:
                f.write(await png.read())


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = list()
        for num in range(1, 151):
            url = f"https://pokeapi.co/api/v2/pokemon/{num}"
            tasks.append(asyncio.create_task(get_pokemon(session, url, "/tmp")))

        await asyncio.gather(*tasks)


asyncio.run(main())
