import aiohttp 
import asyncio 

async def main():
    # session 作成 
    # async with することで全処理が終わった時に session をちゃんとクローズしてくれる
    async with aiohttp.ClientSession() as session:
        # URL へアクセス。
        async with session.get('http://python.org') as response:
            # .get()時に読み込むのはヘッダー情報のみ
            print(response.status)
            print(response.headers['content-type'])
            # body をテキストとして非同期に読み込む
            # だから await をつけている
            html = await response.text() 
            print(html[:15])

    # ブロックが終わると残っている全てのリソースを閉じていることを確認してくれる
    # なので閉じ忘れることはない

# 非同期通信イベントを管理してくれるEventLoopオブジェクト作成 (`<class 'asyncio.unix_events._UnixSelectorEventLoop'>`)
loop = asyncio.get_event_loop()
# EventLoopオブジェクトに main() をタスクとして渡し、非同期に処理の管理実行してもらう
loop.run_until_complete(main())

