import asyncio
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%X")


async def kome():
    logging.info("米を炊くヨ")
    await asyncio.sleep(10)
    logging.info("米が炊けたヨ")


async def chori():
    logging.info("調理するヨ")

    logging.info("味噌汁つくるヨ")
    await asyncio.sleep(3)
    logging.info("味噌汁できたヨ")

    logging.info("おかずつくるヨ")
    await asyncio.sleep(6)
    logging.info("おかずできたヨ")

    logging.info("調理おわったよヨ")


def taberu():
    logging.info("いただきます")
    time.sleep(3)
    logging.info("ごちそうさまでした")


async def itadakimasu():

    logging.info("--- ご飯できるまで待つ ---")

    kome_task = asyncio.create_task(kome())
    chori_task = asyncio.create_task(chori())
    await kome_task
    await chori_task

    logging.info("--- ご飯できたので食べる ---")

    taberu()


asyncio.run(itadakimasu())