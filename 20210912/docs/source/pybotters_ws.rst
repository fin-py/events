AIOHTTP-Client ハンズオン
=========================

目的
----

- Clientを使った簡単なハンズオン
- インターネット経由で取得できるデータを、並行に取得して処理する簡単なPythonを書けるようになる

内容
----


- `pybotters/ws.py at main · MtkN1/pybotters <https://github.com/MtkN1/pybotters/blob/main/pybotters/ws.py>`_ 
- ftx を使って非汎用的だが、とりあえず動くモノを作る


.. literalinclude:: ./code/pybotters_ws.py
   :linenos:

`send_str <https://docs.aiohttp.org/en/stable/web_reference.html?highlight=send_str#aiohttp.web.WebSocketResponse.send_str>`_ 
`8.8.2. async for 文 <https://docs.python.org/ja/3.8/reference/compound_stmts.html#async-for>`_


