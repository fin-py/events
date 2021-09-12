Wait
====

- awaitableオブジェクト（Taskやコルーチン）はさまざまな条件で待機できる
- タイムアウトを設定できる
- 例外に応じて処理を制御できる

タイムアウト
  - `asyncio.wait_for <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.wait_for>`_
要素の終了待機
  - `asyncio.as_completed <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.as_completed>`_
  - `asyncio.wait <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.wait>`_

Future
------

- 非同期処理の最終結果を表現する特別な低レベルのawaitableオブジェクト

    - pending
    - finished
    - cancelled

- コルーチンはFutureの結果が返されるか例外が送出されるまでawaitされる

asyncio.wait_for
----------------

- awaitableオブジェクトが完了するかタイムアウトになるのを待つ
- awaitableオブジェクトがコルーチンだった場合はTaskとしてスケジュールされる
- タイムアウトの場合はTaskをキャンセルし、 `asyncio.TimeoutError <https://docs.python.org/ja/3/library/asyncio-exceptions.html#asyncio.TimeoutError>`_ を送出する

.. literalinclude:: ./code/asyncio/await_for.py
   :linenos:

``asyncio.TimeoutError`` になる

asyncio.as_completed
--------------------

- awaitableオブジェクトを同時に実行する
- 完了した順に、イテレータを返す
- イテレーションが完了する前にタイムアウトした場合は ``asyncio.TimeoutError`` を送出する

.. literalinclude:: ./code/asyncio/as_completed.py
   :linenos:

.. literalinclude:: ./code/asyncio/as_completed.txt

asyncio.wait
------------

- awaitableオブジェクトを同時に実行する
- 完了したタスクと保留中のタスクのset（集合）を返す
- ``return_when`` でいつ結果を返すかを指定する

.. literalinclude:: ./code/asyncio/wait.py
   :linenos:

.. literalinclude:: ./code/asyncio/wait.txt

return_when
^^^^^^^^^^^

asyncio.waitがいつ返すかを指定

FIRST_COMPLETED
  - いずれかのFutureが終了したかキャンセルされたときに返す
FIRST_EXCEPTION
  - いずれかのFutureが例外の送出で終了した場合に返す
  - 例外を送出したFutureがない場合は、 ``ALL_COMPLETED`` と等価になる
ALL_COMPLETED
  - すべてのFutureが終了したかキャンセルされたときに返す（デフォルト）

.. literalinclude:: ./code/asyncio/wait_FIRST_COMPLETED.py
   :linenos:

.. literalinclude:: ./code/asyncio/wait_FIRST_COMPLETED.txt

練習問題
--------

1. ``asyncio.as_completed`` に複数のコルーチンを渡し、うち1つのコルーチンは例外を送出してください
2. 1.の例外をtry-except処理してください
