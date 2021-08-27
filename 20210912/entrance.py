import asyncio
import json
from typing import Union

import aiohttp


async def get() -> Union[None, dict]:
    url = "https://raw.githubusercontent.com/fin-py/events/main/20210912/price.json"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
        ) as response:
            if response.status == 200:
                return json.loads(await response.text())


async def main(num: int = 0) -> Union[None, float]:
    json_data = await get()
    if json_data:
        result = {x["id"]: x for x in json_data["result"]}
        id_ = sorted(result.keys())[num]
        price = int(result[id_]["price"])
        print(f"https://bit.ly/finpy{price}")


asyncio.run(main())
