import aiohttp
import asyncio


async def main():
    # session 作成。非同期コンテキストマネージャ async with を使うと
    # 処理終了時に session はクローズされる
    async with aiohttp.ClientSession() as session:

        # URL へアクセス。.get()時に読み込むのはヘッダー情報のみ
        async with session.get("http://python.org") as response:
            print(response.status)
            print(response.headers["content-type"])

            # body をテキストで非同期に読み込む
            html = await response.text()
            print(html[:15])


asyncio.run(main())
