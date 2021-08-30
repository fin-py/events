asyncioの実装
=============

コルーチン
----------

- async/await構文で宣言
- asyncioを使ったアプリケーションを書くのに推奨される方法
- ``asyncio.run`` 関数で実行できる

.. code-block:: python
   :linenos:

    import asyncio

    async def main():
        print('hello')
        await asyncio.sleep(1)
        print('world')

    asyncio.run(main())

Taskの作成
----------

- ``asyncio.create_task`` 関数でコルーチンをTaskにラップ
- Taskオブジェクトを返す

.. code-block:: python

    async def coro():
        ...

    # In Python 3.7+
    task = asyncio.create_task(coro())
    ...

    # This works in all Python versions but is less readable
    task = asyncio.ensure_future(coro())
    ...
