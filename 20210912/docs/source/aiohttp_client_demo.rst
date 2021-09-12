
AIOHTTP Client デモ
--------------------

- `PokéAPI <https://pokeapi.co/>`_ を使ってポケモンを150匹Getする方法を3つ紹介し処理の速さを比較する
   - 参照：`aiohttpとasyncioを使用したPythonの非同期HTTPリクエスト <https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp-jp>`_
- PokéAPIについて
   - 利用規約 `Documentation - PokéAPI <https://pokeapi.co/docs/v2#fairuse>`_
   - endpoint: https://pokeapi.co/docs/v2#pokemon
   - API例：
      - https://pokeapi.co/api/v2/pokemon/25 : id 25 の ピカチュウ情報URL


Requests を使った場合
~~~~~~~~~~~~~~~~~~~~~~

- `Requests <https://docs.python-requests.org/en/master/>`_ を使って通常のHTTPリクエストでAPIへアクセスする


.. code-block:: bash

   $ pip install requests

.. literalinclude:: ./code/aiohttp/pokemon1.py
   :linenos:


実行結果: ``time: 5.970675468444824``



非同期にリクエストをする場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``await resp.json()`` でbody をjsonで要求。
- bodyを待っている間に、後続のポケモンURL
- jsonが返ってきたら、URLを投げている処理を一旦止めて、ポケモン ID と name を出力

.. literalinclude:: ./code/aiohttp/pokemon2.py
   :linenos:

実行結果: ``time: 2.4725234508514404``


タスクリストを先に作って非同期にリクエストする場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- まずは非同期リクエスト用のタスクリストを作成し、 `asyncio.create_task <https://docs.python.org/3/library/asyncio-task.html#asyncio.create_task>`_ へ渡す。
- このタスクリストを `asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently>`_ へ渡して全てのタスクを並行に実行する。この実行を `await` して全部完了するまで待つ。返り値の順序は、``create_task`` で作った順序と同じ。

.. literalinclude:: ./code/aiohttp/pokemon3.py
   :linenos:

実行結果: ``time: 0.4347381591796875``


