import asyncio
import logging
import time
import pybotters

import order

logging.basicConfig(level=logging.DEBUG)

base_url = "https://testnet.bitmex.com/api/v1"
apis = "apis.json"


async def order_book_l2(symbol: str) -> dict:
    """オーダーブックを取得"""
    async with pybotters.Client(base_url=base_url, apis=apis) as client:
        r = await client.get("/orderBook/L2", params={"symbol": symbol,},)
        data = await r.json()
        return data


async def get_mid_price(symbol: str) -> float:
    "オーダーブックから仲値を取得"
    book_l2 = await order_book_l2(symbol)
    # 買い注文の最大値
    bid = max(result["price"] for result in book_l2 if result["side"] == "Buy")

    # 売り注文の最小値
    ask = min(result["price"] for result in book_l2 if result["side"] == "Sell")

    return (float(ask) + float(bid)) / 2


async def place_order(symbol: str, side: str, qty: int, drift_price: float) -> dict:
    """現在の仲値の上下に買い指値と売り指値を発注"""
    mid = await get_mid_price(symbol)
    if side == "Buy":
        order_price = mid - drift_price
    elif side == "Sell":
        order_price = mid + drift_price
    return await order.order_create(symbol, side, qty, order_price)


async def get_position_list(symbol: str) -> list:
    """ポジションを取得"""
    async with pybotters.Client(base_url=base_url, apis=apis) as client:
        r = await client.get("/position", params={"symbol": symbol})
        data = await r.json()
        return data


async def run_bot(
    symbol: str, qty: int, drift_price: float, repeat: int = 10, interval: int = 30
) -> None:
    for i, _ in enumerate(range(repeat)):
        logging.debug(f"Try: {i+1} / {repeat}")
        """
        間隔ごとに繰り返し発注

        :param symbol: 通貨ペア
        :param repeet: 繰り返し回数
        :param interval: 実行間隔
        """
        position = await get_position_list(symbol)

        if position[0]["currentQty"] != 0:
            logging.debug("placing couter order")
            size = int(position[0]["currentQty"])  # ポジションサイズ
            side = "Buy" if size > 0 else "Sell"  # 売り/買い
            if size == qty:  # ボジションがあったら反対売買をする
                if side == "Buy":
                    order_task = [
                        asyncio.create_task(
                            place_order(symbol, "Sell", qty, drift_price / 2)
                        )
                    ]
                if side == "Sell":
                    order_task = [
                        asyncio.create_task(
                            place_order(symbol, "Buy", qty, drift_price / 2)
                        )
                    ]

        else:  # ポジションがなかったら売りと買いを両方だす
            logging.debug("placing both orders")
            order_task = [
                asyncio.create_task(place_order(symbol, "Sell", qty, drift_price)),
                asyncio.create_task(place_order(symbol, "Buy", qty, drift_price)),
            ]
        done, pending = await asyncio.wait(
            order_task, return_when=asyncio.tasks.ALL_COMPLETED,
        )
        logging.debug(f"waiting: {interval} sec ... ")
        time.sleep(interval)
        logging.debug("cancelling orders ... ")
        await asyncio.wait_for(order.order_cancel_all(symbol), timeout=None)


async def main(symbol: str, qty: int, drift_price: float):
    try:
        await run_bot(symbol, qty, drift_price)
    finally:
        await order.order_cancel_all(symbol)


asyncio.run(main("XBTUSD", 100, 50))
