イベントループ
==============

- コルーチンを実行

  - 非同期関数( ``async def`` )は実行しても処理されない
  - コルーチンの実態はジェネレータ
  - イベントループはコルーチンをイテレーションする

イベントループの取得
--------------------

`asyncio.get_running_loop <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.get_running_loop>`_
  現在のスレッドのイベントループを取得

`asyncio.get_event_loop <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.get_event_loop>`_
  - 現在のイベントループを取得
  - ``asyncio.set_event_loop`` が呼ばれていない場合は新しいイベントループを作成
  - 取得したループはカレントループとなる
  - より高レベルの `asyncio.run <https://docs.python.org/ja/3/library/asyncio-task.html#asyncio.run>`_ を検討できる

`asyncio.set_event_loop <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.set_event_loop>`_
  現在のスレッドのイベントループとして設定

`asyncio.new_event_loop <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.new_event_loop>`_
  - 新しいイベントループオブジェクトを作成
  - ``asyncio.set_event_loop`` でカレントループとなる

イベントループの処理
--------------------

`loop.run_until_complete <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.run_until_complete>`_
  - Futureが完了するまで実行する
  - 引数にコルーチンが渡された場合、 ``asyncio.Task`` として実行するようにスケジュールされる

`loop.run_forever <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.run_forever>`_
  ``stop`` が呼び出されるまでイベントループを実行し続ける

`loop.stop <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.stop>`_
  イベントループを停止する

`loop.is_running <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.is_running>`_
  イベントループが実行中の場合は ``True`` を返す

`loop.is_closed <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.is_closed>`_
  イベントループがクローズされた場合は ``True`` を返す

`loop.close <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.close>`_
   - イベントループをクローズする
   - 保留中のコールバックは破棄される
   - executorは終了を待たずに停止される

イベントループのファイナライズ
------------------------------

`coroutine loop.shutdown_asyncgens <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_asyncgens>`_
   - デフォルトのexecutorの ``aclose`` をスケジュールする
   - すべての非同期ジェネレータをファイナライズする
   - ``asyncio.run`` では自動で実行される

`coroutine loop.shutdown_default_executor <https://docs.python.org/ja/3/library/asyncio-eventloop.html#asyncio.loop.shutdown_default_executor>`_
   - デフォルトのexecutorのクローズをスケジュールする
   - ``ThreadPoolExecutor`` に参加するのを待つ
   - ``asyncio.run`` では自動で実行される