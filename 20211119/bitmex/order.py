import asyncio
import logging
import pprint
import sys

import pybotters

logging.basicConfig(level=logging.DEBUG)

base_url = "https://testnet.bitmex.com/api/v1"
apis = "apis.json"


async def order_create(
    symbol, side, order_qty, price, order_type="Limit", time_in_force="GoodTillCancel"
):
    async with pybotters.Client(base_url=base_url, apis=apis) as client:
        r = await client.post(
            "/order",
            data={
                "symbol": symbol,
                "side": side,
                "orderQty": order_qty,
                "price": price,
                "ordType": order_type,
                "timeInForce": time_in_force,
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


async def get_open_orders(symbol: str) -> dict:
    async with pybotters.Client(base_url=base_url, apis=apis) as client:
        r = await client.get("/order", data={"symbol": symbol})
        data = await r.json()
        return data


async def order_cancel_all(symbol):
    async with pybotters.Client(base_url=base_url, apis=apis) as client:
        r = await client.delete("/order/all", data={"symbol": symbol})
        data = await r.json()
        return data


# if __name__ == "__main__":
#     asyncio.run(order_create())
