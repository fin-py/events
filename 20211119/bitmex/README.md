
# BitMEX Testnet 

## 前準備

1. ログイン
1. [BitMEX Testnet API Explorer](https://testnet.bitmex.com/api/explorer/)

## Explorer で練習
1. User情報を出す
    1. https://testnet.bitmex.com/api/explorer/#/User
    1. `Try it out!` ボタンを押す
    1. Request URL, Response Body 確認
1. Create Order
    1. https://testnet.bitmex.com/api/explorer/#!/Order/Order_new
    1. Parameters を入れる。シンボルは必須。その他はお好きに変えてください。
        - `symbol` (必須) : XBTUSD (テストネットではXBTUSDだけかと)
        - `side`: Buy 
        - `orderQty` : 100 
        - `price`: xxxxxx （テストしたいのですぐにDoneされない基準においてください）
        - `orderType`: Limit
        - `timeInForce`: GoodTillCancel
    1. `Try it out!` ボタンを押す
    1. **Curl** を確認
        > curl -X POST --header 'Content-Type: application/x-www-form-urlencoded' --header 'Accept: application/json' --header 'X-Requested-With: XMLHttpRequest' -d 'symbol=XBTUSD&side=Buy&orderQty=100&price=59400&ordType=Limit&timeInForce=GoodTillCancel 'https://testnet.bitmex.com/api/v1/order'
        - `-d` のところをスクリプトに使います
    1. https://testnet.bitmex.com/app/trade/XBTUSD の真ん中あたりの `Active Orders` で注文が確認できていればOK
        ![](https://i.imgur.com/A8xsJh5.jpg)


## コーディング

1. 適当な .py ファイル作成
1. 同じディレクトリに Key と Secret が入った `apis.json` を格納
1. コード
    ```python
    import asyncio
    import logging
    import pprint

    import pybotters

    logging.basicConfig(level=logging.DEBUG)

    async def order_create():
        async with pybotters.Client(
            base_url="https://testnet.bitmex.com/api/v1", # ベースURL
            apis="apis.json"
        ) as client:
            r = await client.post( # .post メソッド
                "/order", # エンドポイント
                data={
                    # 先程取得した -d 以下 をキーと値として入れる
                    "symbol": "XBTUSD",  
                    "side": "Buy",  
                    "ordType": "Limit",
                    "orderQty": 100,
                    "price": xxxxxx,
                    "timeInForce": "GoodTillCancel",
                },
            )
            data = await r.json()
            logging.debug(pprint.pformat(data))
            return data

    if __name__ == "__main__":
        asyncio.run(order_create())
    ```
1. 実行後、`Active Orders` で確認
