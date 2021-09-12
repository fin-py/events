Task
====

`asyncio.create_task <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.create_task>`_ 関数によるTaskの作成

.. code-block:: python

    >>> import asyncio
    >>> 
    >>> async def func():
    ...     pass
    ... 
    >>> async def main():
    ...     task = asyncio.create_task(func())
    ...     print(type(task))
    ... 
    >>> asyncio.run(main())
    <class '_asyncio.Task'>

Taskオブジェクトが生成される

単にコルーチンをawaitして実行
-----------------------------

.. literalinclude:: ./code/asyncio/nontask.py
   :linenos:

実行結果: ``time: 7.0069193840026855``

Taskを作成して実行
------------------

.. literalinclude:: ./code/asyncio/task.py
   :linenos:

実行結果: ``time: 5.004063844680786``

並行なTask実行
--------------

- awaitableオブジェクトを並行して実行
- `asyncio.gather <https://docs.python.org/ja/3/library/asyncio-task.html?highlight=asyncio%20gather#asyncio.gather>`_ に渡されたシーケンスは並行実行される

asyncio.gatherにコルーチンを渡した例
------------------------------------

.. literalinclude:: ./code/asyncio/gather_coroutine.py
   :linenos:

実行結果: ``time: 5.007250785827637``

asyncio.gatherにTaskを渡した例
------------------------------

.. literalinclude:: ./code/asyncio/gather_task.py
   :linenos:

実行結果: ``time: 5.006976842880249``

練習問題
--------

次のコードの ``get_status_code`` 関数を並行に実行する ``main`` 関数を作成してください

.. literalinclude:: ./code/asyncio/aiohttp_request.py
   :linenos:
