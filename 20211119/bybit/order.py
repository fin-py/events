import asyncio
import pprint

import pybotters


async def order_create():
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/create",
            data={
                "side": "Buy",
                "symbol": "BTCUSD",
                "order_type": "Limit",
                "qty": 1,
                "price": 10000,
                "time_in_force": "GoodTillCancel",
            },
        )
        data = await r.json()
        pprint.pprint(data)


async def order():
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.get(
            "/v2/private/order",
            params={
                "symbol": "BTCUSD",
            },
        )
        data = await r.json()
        pprint.pprint(data)


async def order_cancel():
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/cancel",
            data={
                "symbol": "BTCUSD",
                "order_id": "e747750b-1c57-4356-8cae-103e926d2fe5",
            },
        )
        data = await r.json()
        pprint.pprint(data)


async def order_calcell_all():
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.post(
            "/v2/private/order/cancelAll",
            data={
                "symbol": "BTCUSD",
            },
        )
        data = await r.json()
        pprint.pprint(data)
