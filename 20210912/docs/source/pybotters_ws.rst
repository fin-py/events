AIOHTTP-Client ハンズオン
=========================

目的
----

- Clientを使った簡単なハンズオン
- インターネット経由で取得できるデータを、並行に取得して処理する簡単なPythonを書けるようになる

内容
----

- 暗号資産取引所 ftx の APIを利用して、取引データをウェブソケット経由で取得する
- 参考: `pybotters/ws.py at main · MtkN1/pybotters <https://github.com/MtkN1/pybotters/blob/main/pybotters/ws.py>`_ 

.. literalinclude:: ./code/aiohttp/pybotters_ws.py
   :linenos:

- `send_str <https://docs.aiohttp.org/en/stable/web_reference.html?highlight=send_str#aiohttp.web.WebSocketResponse.send_str>`_ 
- `8.8.2. async for 文 <https://docs.python.org/ja/3.8/reference/compound_stmts.html#async-for>`_


課題
----

1. FTX で利用出来る銘柄をサブスクライブしてデータを取得。マーケットリストは `FTX Markets <https://ftx.com/en/markets>`_ を参照してください。
2. サブスクライブ時に文字列を渡していますが、jsonを渡すように書き換えてください
3. orderbook チャンネルをサブスクライブしてください。参照： `Websocket API <https://docs.ftx.com/#websocket-api>`_
4. :ref:`/aiohttp_client.html#websockets` を参考にして、async for ではなく ws.recieve() して、非同期イテレータを使わないどうなるのか実験してください
5. 他の取引所データを取得してみてください。各業者の API は `pybotters の Exchanges <https://github.com/MtkN1/pybotters#-exchanges>`_ を参照してください。

