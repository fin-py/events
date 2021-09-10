AIOHTTP-Client Quickstart
==========================

- Doc: `Client — aiohttp 3.7.4.post0 documentation <https://docs.aiohttp.org/en/stable/client.html>`_ 

async with
----------

.. literalinclude:: ./code/aiohttp/aiohttp_qs1.py
   :linenos:

- 非同期のコンテキストマネージャ
- ClientSessionを使った処理が終わったら session を close してくれる。
- もし session context manager を使わない場合は以下のように ``.close()`` メソッドを呼び出し必ずクローズする。

.. literalinclude:: ./code/aiohttp/aiohttp_qs2.py
   :linenos:

with文のネスト
^^^^^^^^^^^^^^

- `Python 3.10の新機能(その2） with文のネスト: Python3.10の新機能 <https://www.python.jp/news/wnpython310/with-statement.html>`_
- これを async with でもやってみたところ出来ました。
- (実はpython3.9でも可)

.. code-block:: python

    async with (aiohttp.ClientSession() as session,
                session.get("http://httpbin.org/get") as resp):
                :
                :


async for
---------

- 非同期イテレータ/ジェネレータ用の ``for`` 文
- 下記２つは同じ意味 

.. code-block:: python

   async for a in async_iterable:
      await do_a_thing(a)

.. code-block:: python

   it = async_iterable.__aiter__()
   while True:
      try:
         a = await it.__anext__()
      except StopAsyncIteration:
         break

      await do_a_thing(a)

- 参照： `Python Asyncio Part 3 – Asynchronous Context Managers and Asynchronous Iterators <https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-3>`_


ClientSession
-------------

- `aiohttp.ClientSession <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession>`_
- クライアントセッションクラス。
- インスタンス化して(以下 ``session`` で表現)、そのオブジェクトメソッドを使ってリクエストを行う


session.request()
^^^^^^^^^^^^^^^^^
- `aiohttp.ClientSession.request <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.request>`_ 
- 非同期のHTTPリクエストを実行
- 返り値は `aiohttp.ClientResponse <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientResponse>`_ インスタンスオブジェクト
- 引数(必須)
   - ``method (str)`` – HTTP method
   - ``url`` – URL。文字列もしくは yarl URL オブジェクト
- オプション引数：ドキュメント参照

session.get()
^^^^^^^^^^^^^
- `aiohttp.ClientSession.get <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.get>`_
- GET リクエスト
- ``session.request()`` の第一引数が `GET` に固定されているメソッド
- 引数(必須)
   - ``url`` – URL。文字列もしくは yarl URL オブジェクト
- オプション引数：ドキュメント参照
- 返り値は `aiohttp.ClientResponse <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientResponse>`_ インスタンスオブジェクト

その他HTTPメソッド
^^^^^^^^^^^^^^^^^^
- `.post() <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.post>`_ `.put() <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.put>`_ `.delete() <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.delete>`_ `.patch() <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientSession.patch>`_ 等用意されている。
- 返り値は `aiohttp.ClientResponse <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientResponse>`_ インスタンスオブジェクト

URLリクエストにパラメータ を渡す
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. literalinclude:: ./code/aiohttp/aiohttp_qs3.py
   :linenos:

- ``params`` オプションで渡す
- 同じキーに対して2つ以上の値を渡したい場合は、`MultiDict <https://multidict.readthedocs.io/en/stable/multidict.html#multidict.MultiDict>`_ もしくは、タプルのリストで渡す
   - ``MultiDict({'a': [1, 3]})`` 
   - ``MultiDict([('a', 1), ('a', 3)])`` 
   - ``([('a', 1), ('a', 3)])`` 

バイナリデータ
^^^^^^^^^^^^^^

.. literalinclude:: ./code/aiohttp/aiohttp_qs4.py
   :linenos:

- バイナリデータは `response <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientResponse>`_ オブジェクトの `.read() <https://docs.aiohttp.org/en/stable/client_reference.html?highlight=async%20with#aiohttp.ClientResponse.read>`_  で取得可

streaming response
^^^^^^^^^^^^^^^^^^
- ``read()`` ``json()`` ``text()`` は メモリにロードするので、巨大なサイズのファイルの読み込みには `aiohttp.StreamReader <https://docs.aiohttp.org/en/stable/streams.html#aiohttp.StreamReader>`_  のインスタンスの ``.content`` アトリビュートの利用を検討したほうがよい
- よく使われる方法としては、chunk size を指定してファイル等に書き込むなどする

.. literalinclude:: ./code/aiohttp/aiohttp_qs5.py
   :linenos:


websockets
^^^^^^^^^^

.. literalinclude:: ./code/aiohttp/aiohttp_qs6.py
   :linenos:

- client session を確立後、`aiohttp.ClientSession.ws_connect() <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientSession.ws_connect>`_ メソッドでウェブソケットへ接続
- URL を渡して初期化すると、ウェブソケットサーバーに接続状態になる。返り値は `aiohttp.ClientWebSocketResponse <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientWebSocketResponse>`_ 。(以下 ``ws`` で表現)
- `ws.send_str <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientWebSocketResponse.send_str>`_ メソッドで ping を投げて、 `ws.receive() <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientWebSocketResponse.receive>`_ メソッドでレスポンスを待つ。
   - `ws.send_json <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientWebSocketResponse.send_json>`_ メソッドで json を投げることも可
-  `ws.receive() <https://docs.aiohttp.org/en/stable/client_reference.html#aiohttp.ClientWebSocketResponse.receive>`_ の返り値は `aiohttp.WSMessage <https://docs.aiohttp.org/en/stable/websocket_utilities.html#aiohttp.WSMessage>`_ オブジェクト。その ``type`` 属性が `aiohttp.WSMsgType <https://docs.aiohttp.org/en/stable/websocket_utilities.html#aiohttp.WSMsgType>`_ で、そのタイプによって処理を切り分ける


