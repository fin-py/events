AIOHTTP-Client
==============

- Doc: `Client — aiohttp 3.7.4.post0 documentation <https://docs.aiohttp.org/en/stable/client.html>`_ 

いつ使うべき
------------

- 参照：`aiohttpとasyncioを使用したPythonの非同期HTTPリクエスト <https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp-jp>`_
- `PokéAPI <https://pokeapi.co/>`_ を使ってポケモンを150匹Getする方法を3つ紹介し処理の速さを比較する
- 利用規約 `Documentation - PokéAPI <https://pokeapi.co/docs/v2#fairuse>`_
- endpoint: https://pokeapi.co/docs/v2#pokemon


request を使った場合
~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./code/pokemon1.py
   :linenos:


.. code-block:: 

   ❯ python src/pokemon1.py 
   :
   :
   [I 210906 16:34:57 pokemon:46] 5.724557876586914

- ポケモンURLにリスクエストを投げて、レスポンスを待ち、受け取ったらポケモン ID と name を出力
- これを1から150番まで順番に行う

非同期にリクエストをする場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./code/pokemon2.py
   :linenos:

.. code-block:: 

   ❯ python src/pokemon2.py 
   :
   :
   [I 210906 16:46:24 pokemon:47] 2.2340128421783447

- `pokemon = await resp.json()` でbody をjsonで要求するリクエストを投げて戻ってくるのを待つ。
- 待っている間に、次のポケモンのリクエストURLを投げる
- 投げている間に、jsonが返ってきたら、ポケモン ID と name を出力

リクエストタスクを先に作って非同期にリクエストする場合
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ./code/pokemon3.py
   :linenos:

.. code-block:: 

   ❯ python src/pokemon3.py 
   :
   :
   [I 210906 16:52:55 pokemon_2:30] 0.4318504333496094

- まずは非同期リクエスト用のタスクリストを作成し、 `asyncio.ensure_future <https://docs.python.org/3/library/asyncio-future.html#asyncio.ensure_future>`_ へ渡す。 これで、出力時にタスクを登録したリストの順序が維持される。
- このタスクリストを `asyncio.gather <https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently>`_ へ渡して全てのタスクを同時に実行する。この実行を `await` して全部完了するまで待つ


Quickstart
----------
- about_aiohttp.rst よりももうちょっと踏み込んで書く

request 
~~~~~~~

- make request

.. literalinclude:: ./code/aiohttp_qs1.py
   :linenos:

- `async with` : session context manager. 処理が終わったら session を close してくれる。
- もし session context manager を使わない場合は以下のように `.close()` メソッドを呼び出し必ずクローズする。

.. literalinclude:: ./code/aiohttp_qs2.py
   :linenos:

- pass parametar

.. literalinclude:: ./code/aiohttp_qs3.py
   :linenos:



- response    
   - get contents
   - status code 
   - binary code 
   - json 
   - text
   - streaming response の扱いかた

- websockets
- timeouts

