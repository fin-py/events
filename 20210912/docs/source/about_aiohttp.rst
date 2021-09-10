AIOHTTP
========

- Doc :  `Welcome to AIOHTTP — aiohttp 3.7.4.post0 documentation <https://docs.aiohttp.org/en/stable/index.html>`_

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

.. literalinclude:: ./code/aiohttp/aiohttp_gs_client.py
   :linenos:

- アクセス先の利用規約を必ず確認する

Server
~~~~~~

- 参照： `Server — aiohttp 3.7.4.post0 documentation <https://docs.aiohttp.org/en/stable/web.html>`_ 

Misc
----

AIOHTTP を使う際によく使うツール
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- `multidict <https://pypi.org/project/multidict/>`_ : URLにパラメタを渡す時に使う
- `yarl <https://pypi.org/project/yarl/>`_ : `ClientSession.get()` は、文字列もしくは yarl.URL インスタンスを引き取る


.. literalinclude:: ./code/aiohttp/aiohttp_gs_misc.py
   :linenos:

出力

.. code-block:: 

    https://connpass.com/explore
    https://connpass.com/search?q=aiohttp
