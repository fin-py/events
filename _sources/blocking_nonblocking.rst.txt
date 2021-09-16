ブロッキング/ノンブロッキング
=============================

ブロッキング
------------

- 処理が終了するまで待つ
- 待っている間はほかの処理を行えない

`time.sleep <https://docs.python.org/ja/3/library/time.html#time.sleep>`_ はブロッキングするので、完了を待ってから次の処理に移る

.. literalinclude:: ./code/asyncio/blocking.py
   :linenos:

実行結果: ``time: 7.009732246398926``

ノンブロッキング
----------------

- ブロッキングされない
- ほかの処理ができる

`asyncio.sleep <https://docs.python.org/ja/3/library/asyncio-task.html#sleeping>`_ はノンブロッキング処理なので、待っている間に次の処理に移れる

.. literalinclude:: ./code/asyncio/task.py
   :linenos:

実行結果: ``time: 5.004534006118774``

ノンブロッキング関数の実装
--------------------------

- `loop.run_in_executor <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.run_in_executor>`_ を利用
- `Executor <https://docs.python.org/ja/3/library/concurrent.futures.html#concurrent.futures.Executor>`_ は非同期呼び出しをするためのクラス

  - `ThreadPoolExecutor <https://docs.python.org/ja/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor>`_
  - `ProcessPoolExecutor <https://docs.python.org/ja/3/library/concurrent.futures.html#processpoolexecutor>`_

.. literalinclude:: ./code/asyncio/nonblocking_function.py
   :linenos:

実行結果: ``time: 5.005532503128052``

練習問題
--------

次のコードを非同期(ノンブロッキング)に実装してください

.. literalinclude:: ./code/asyncio/get_request.py
   :linenos:
