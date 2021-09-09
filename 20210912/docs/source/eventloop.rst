イベントループ
==============

- コルーチンを実行

  - 非同期関数( ``async def`` )は実行しても処理されない
  - コルーチンの実態はジェネレータ
  - イベントループはコルーチンをイテレーションする

イベントループの取得
--------------------

asyncio.get_running_loop
  現在のスレッドのイベントループを取得

asyncio.get_event_loop
  - 現在のイベントループを取得
  - ``asyncio.set_event_loop`` が呼ばれていない場合は新しいイベントループを作成
  - 取得したループはカレントループとなる
  - より高レベルの ``asyncio.run`` を検討できる

asyncio.set_event_loop
  現在のスレッドのイベントループとして設定

asyncio.new_event_loop
  - 新しいイベントループオブジェクトを作成
  - ``asyncio.set_event_loop`` でカレントループとなる

イベントループの処理
--------------------

loop.run_until_complete
  - Futureが完了するまで実行する
  - 引数にコルーチンが渡された場合、 ``asyncio.Task`` として実行するようにスケジュールされる

loop.run_forever
  ``stop`` が呼び出されるまでイベントループを実行し続ける

loop.stop
  イベントループを停止する

loop.is_running
  イベントループが実行中の場合は ``True`` を返す

loop.is_closed
  イベントループがクローズされた場合は ``True`` を返す

loop.close
   - イベントループをクローズする
   - 保留中のコールバックは破棄される
   - executorは終了を待たずに停止される

イベントループのファイナライズ
------------------------------

coroutine loop.shutdown_asyncgens
   - デフォルトのexecutorの ``aclose`` をスケジュールする
   - すべての非同期ジェネレータをファイナライズする
   - ``asyncio.run`` では自動で実行される

coroutine loop.shutdown_default_executor
   - デフォルトのexecutorのクローズをスケジュールする
   - ``ThreadPoolExecutor`` に参加するのを待つ
   - ``asyncio.run`` では自動で実行される