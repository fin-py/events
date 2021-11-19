import asyncio
import logging
import time

import pybotters

import order

logging.basicConfig(level=logging.DEBUG)


async def order_book_l2(symbol: str) -> dict:
    """オーダーブックを取得"""
    async with pybotters.Client(
        base_url="https://api-testnet.bybit.com/", apis="apis.json"
    ) as client:
        r = await client.get(
            "/v2/public/orderBook/L2",
            params={
                "symbol": symbol,
            },
        )
        data = await r.json()
        return data


async def get_mid_price(symbol: str) -> float:
    "オーダーブックから仲値を取得"
    book_l2 = await order_book_l2(symbol)
    # 買い注文の最大値
    bid = max(
        result["price"]
        for result in book_l2["result"]
        if result["symbol"] == symbol and result["side"] == "Buy"
    )
    # 売り注文の最小値
    ask = min(
        result["price"]
        for result in book_l2["result"]
        if result["symbol"] == symbol and result["side"] == "Sell"
    )
    return (float(ask) + float(bid)) / 2


async def place_order(symbol: str, side: str, qty: int, drift_price: float) -> dict:
    """現在の仲値の上下に買い指値と売り指値を発注"""
    mid = await get_mid_price(symbol)
    if side == "Buy":
        order_price = mid - drift_price
    elif side == "Sell":
        order_price = mid + drift_price
    return await order.order_create(symbol, side, qty, order_price)


async def run_bot(
    symbol: str, qty: int, drift_price: float, repeet: int = 5, interval: int = 30
) -> None:
    for _ in range(repeet):
        """
        間隔ごとに繰り返し発注

        :param symbol: 通貨ペア
        :param repeet: 繰り返し回数
        :param interval: 実行間隔
        """
        order_task = [
            asyncio.create_task(place_order(symbol, "Sell", qty, drift_price)),
            asyncio.create_task(place_order(symbol, "Buy", qty, drift_price)),
        ]
        done, pending = await asyncio.wait(
            order_task,
            return_when=asyncio.tasks.ALL_COMPLETED,
        )
        time.sleep(interval)
        await asyncio.wait_for(order.order_cancel_all(symbol), timeout=1)


async def main(symbol: str, qty: int, drift_price: float):
    try:
        await run_bot(symbol, qty, drift_price)
    finally:
        await order.order_cancel_all(symbol)


asyncio.run(main("BTCUSD", 1, 30))
