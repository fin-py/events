 AIOHTTP
 =======

- Doc :  [Welcome to AIOHTTP — aiohttp 3.7.4.post0 documentation](https://docs.aiohttp.org/en/stable/index.html)
- 今日の大目的： pybotters の wb.py を読めるようになる、自分で同じコードを書けるようになる。 （非汎用的なやつでいいから）


特徴
----

- 非同期通信するための HTTP Client / Server ツール

インストール
------------

.. code-block:: bash

   $ pip install aiohttp

Getting Started
---------------


Client
~~~~~~

.. literalinclude:: ./code/aiohttp_gs_client.py
   :linenos:

- アクセス先の利用規約を必ず確認する

Server
~~~~~~

- pass 


Misc
----

AIOHTTP を使う際によく使うツール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- [multidict](https://pypi.org/project/multidict/)
   - URLにパラメタを渡す時に使う
- [yarl](https://pypi.org/project/yarl/)
   - `ClientSession.get()` は、文字列もしくは yarl.URL インスタンスを引き取る



.. literalinclude:: ./code/aiohttp_gs_misc.py
   :linenos:


