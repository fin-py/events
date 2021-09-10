import asyncio
import aiohttp

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


async def main():
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect("wss://ftx.com/ws") as ws:
            await ws.send_str('{"op":"ping"}')
            # await ws.send_json({"op":"ping"})
            msg = await ws.receive()
            if msg.type == aiohttp.WSMsgType.TEXT:
                logging.info(msg.json())

asyncio.run(main())