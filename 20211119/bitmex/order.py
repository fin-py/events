import asyncio
import logging
import pprint
import sys

import pybotters

logging.basicConfig(level=logging.DEBUG)


async def order_create():
    async with pybotters.Client(
        base_url="https://testnet.bitmex.com/api/v1", apis="apis.json"
    ) as client:
        r = await client.post(
            "/order",
            data={
                "symbol": "XBTUSD",  # symbol だけが必須
                "side": "Buy",  # or "Sell". Default Buy
                "ordType": "Limit",
                "orderQty": 100,
                "price": 59400,
                "timeInForce": "GoodTillCancel",
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


if __name__ == "__main__":
    asyncio.run(order_create())
