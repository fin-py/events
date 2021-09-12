# 他の取引所データを取得してみてください。

import asyncio
import aiohttp

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("wss://stream.bybit.com/realtime") as ws:
            # サブスクライブ
            await ws.send_str(
                '{"op": "subscribe", "args": ["orderBookL2_25.BTCUSD"]}'
            )
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    logging.info(msg.data)
                else:
                    break


asyncio.run(main())
