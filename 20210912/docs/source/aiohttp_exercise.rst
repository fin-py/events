AIOHTTP-Client Exercise
=======================

目的
----

- Clientを使った簡単な練習問題に取組む
- インターネット経由で取得できるデータを、並行に取得して処理する簡単なPythonを書けるようになる

課題1
-----

- 暗号資産取引所 ftx の APIを利用して、取引データをウェブソケット経由で取得する
- 参考: `pybotters/ws.py at main · MtkN1/pybotters <https://github.com/MtkN1/pybotters/blob/main/pybotters/ws.py>`_ 

.. literalinclude:: ./code/aiohttp/pybotters_ws.py
   :linenos:

1. サブスクライブ時に文字列を渡していますが、json を渡すように書き換えてください。
2. :ref:`websockets` を参考にして async for ではなく ``ws.recieve()`` して、非同期イテレータを使わないどうなるのか実験してください。
3. 以下は、暗号資産APIに関する課題なので興味がある方はやってみて下さい。

   a. "BTC-PERP" 以外のマーケットをサブスクライブしてデータを取得して下さい。マーケットリストは `FTX Markets <https://ftx.com/en/markets>`_ を参照してください。
   b. ``orderbook`` チャンネルをサブスクライブしてください。参照： `Websocket API <https://docs.ftx.com/#websocket-api>`_
   c. Bybit の API を使って 適当なリアルタイムデータを取得して下さい。参照： `WebSocket Data – Bybit API Docs <https://bybit-exchange.github.io/docs/inverse/?python#t-websocket>`_

課題2
-----

- 今日のハンズオン内容をベースにした問題

4. :ref:`binary` のポケモン画像取得を非同期で150匹取得してローカルに保存して下さい
5. https://connpass.com/about/api/ を使って、キーワードが "aiohttp" のイベントを探し、event_id のみリストで取得して下さい。ただし、connpass api は ``.json()`` で取得出来ないので、 ``.text()`` で取得して下さい。




