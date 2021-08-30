コルーチン
==========

コルーチン関数
  `async def <https://docs.python.org/ja/3/reference/compound_stmts.html#async-def>`_ で定義された関数
コルーチンオブジェクト
  コルーチン関数 を呼び出すと返ってくるオブジェクト.

コルーチン関数定義
------------------

- `async def <https://docs.python.org/ja/3/reference/compound_stmts.html#async-def>`_ で関数を定義すると、コルーチンとなる

.. code-block:: python

    >>> async def func():
    ...     print("呼んだ？")
    ... 
    >>> cor = func()
    >>> print(type(cor))
    <class 'coroutine'>

- 単にコルーチンを呼び出しただけでは実行されない

.. code-block:: python

    >>> func()
    <coroutine object func at 0x7f774767d6c0>

コルーチンの実行
----------------

- コルーチンを `await <https://docs.python.org/ja/3/reference/expressions.html#await-expression>`_
- awaitした関数( ``main`` )を `asyncio.run <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.run>`_ 関数から実行

.. code-block:: python

    >>> import asyncio
    >>> 
    >>> async def main():
    ...     await func()
    ... 
    >>> asyncio.run(main())
    呼んだ？

練習問題
--------

コルーチンを2つ実行してください。コルーチンの関数は渡された引数をprintします。

.. code-block:: python

   >>> asyncio.run(main("1こめ", "2こめ"))
   1こめ
   2こめ

