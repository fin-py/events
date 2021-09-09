ブロッキング/ノンブロッキング
=============================

ブロッキング
------------

- 処理が終了するまで待つ
- 待っている間はほかの処理を行えない

``time.speep`` はブロッキングするので、完了を待ってから次の処理に移る

.. literalinclude:: ./code/blocking.py
   :linenos:

実行結果: ``time: 7.009732246398926``

ノンブロッキング
----------------

- ブロッキングされない
- ほかの処理ができる

``asyncio.speep`` はノンブロッキング処理なので、待っている間に次の処理に移れる

.. literalinclude:: ./code/task.py

実行結果: ``time: 5.004534006118774``

ノンブロッキング関数の実装
--------------------------

- ``loop.run_in_executor`` を利用
- Executorは非同期呼び出しをするためのクラス

  - ThreadPoolExecutor
  - ProcessPoolExecutor

.. literalinclude:: ./code/nonblocking_function.py

実行結果: ``time: 5.005532503128052``

練習問題
--------

次のコードを非同期(ノンブロッキング)に実装してください

.. literalinclude:: ./code/get_request.py