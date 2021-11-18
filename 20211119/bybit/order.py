import asyncio
import logging
import pprint
import sys

import pybotters

logging.basicConfig(level=logging.DEBUG)


async def order_create(
    symbol: str,
    side: str,
    qty: int,
    price: int,
    order_type: str = "Limit",
    time_in_force: str = "GoodTillCancel",
) -> dict:
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/create",
            data={
                "side": side,
                "symbol": symbol,
                "order_type": order_type,
                "qty": int(qty),
                "price": float(price),
                "time_in_force": time_in_force,
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


async def order(symbol: str) -> dict:
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.get(
            "/v2/private/order",
            params={
                "symbol": symbol,
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


async def order_cancel(symbol: str, order_id: str) -> dict:
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/cancel",
            data={
                "symbol": symbol,
                "order_id": order_id,
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


async def order_cancel_all(symbol: str) -> dict:
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/cancelAll",
            data={
                "symbol": symbol,
            },
        )
        data = await r.json()
        logging.debug(pprint.pformat(data))
        return data


if __name__ == "__main__":
    if len(sys.argv) > 0:
        asyncio.run(globals()[sys.argv[1]](*sys.argv[2:]))
