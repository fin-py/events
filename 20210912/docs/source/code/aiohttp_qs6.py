import asyncio
import aiohttp

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("wss://ftx.com/ws") as ws:
            await ws.send_str('{"op":"ping"}')
            msg = await ws.receive()
            if msg.type == aiohttp.WSMsgType.TEXT:
                logging.info(msg.json())

            # async for msg in ws:
            #     if msg.type == aiohttp.WSMsgType.TEXT:
            #         logging.info(msg.data)

            # await ws.send_str(
            #     '{"op": "subscribe", "channel": "trades", "market": "BTT-PERP"}'
            # )
            # async for msg in ws:
            #     if msg.type == aiohttp.WSMsgType.TEXT:
            #         logging.info(msg.data)
            #     else:
            #         break


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
