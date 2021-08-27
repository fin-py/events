import asyncio
import random
from typing import Union

import aiohttp


async def get(symbol: str, start_time: int, end_time: int) -> Union[None, dict]:
    url = "https://api.bybit.com/v2/public/liq-records"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            params={"symbol": symbol, "start_time": start_time, "end_time": end_time},
        ) as response:
            if response.status == 200:
                return await response.json()


async def main(seed: int = 0) -> Union[None, float]:
    if seed is None:
        return

    json_data = await get("BTCUSD", 1627743600, 1627743601)
    if json_data:
        random.seed(seed)
        num = random.randrange(100)
        result = {x["id"]: x for x in json_data["result"]}
        id_ = sorted(result.keys())[num]
        price = int(result[id_]["price"])
        print(f"https://bit.ly/finpy{price}")


asyncio.run(main())
