# よく見るエラー

この資料を作成中に出くわしたエラーをまとめておきます。何かのおやくに立てればと。

## docker-compose up -d すると services.clickhouse.volumes contains an invalid type, it should be a string 
- 解決方法：docker-compose.yml の version を '3.2' にする
- 参照：[Invalid type in volume, it should be a string. · Issue #4763 · docker/compose](https://github.com/docker/compose/issues/4763)


## docker-compose up -d すると bind: address already in use

- エラーメッセージ
    ```bash
    $ docker-compose up -d
    Creating clickhouse_server ... 
    Creating clickhouse_server ... error

    ERROR: for clickhouse_server  Cannot start service clickhouse: driver failed programming external connectivity on endpoint clickhouse_server (237032740af583e776cf5c40213eddec6740ea1437061be2676845457f9ad5aa): Error starting userland proxy: listen tcp4 0.0.0.0:9000: bind: address already in use

    ERROR: for clickhouse  Cannot start service clickhouse: driver failed programming external connectivity on endpoint clickhouse_server (237032740af583e776cf5c40213eddec6740ea1437061be2676845457f9ad5aa): Error starting userland proxy: listen tcp4 0.0.0.0:9000: bind: address already in use
    ERROR: Encountered errors while bringing up the project.
    ``` 
- 解決方法
    - ポート9000番が何に使われているのかを確認
    ```bash
    $ lsof -i :9000
    COMMAND    PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
    python  136483 shinseitaro   44u  IPv4 996734      0t0  TCP localhost:9000 (LISTEN)

    $ ps aux |  grep 136483 
    ```

    - これで9000番を使っているサービスを特定して、終わらせてもいいものであれば終わらせる。
    - `kill -9 136483` 
    - もしくは、`docker-compose.yml` の `- 9000:9000` を 使われていないポート (例 `-9999:9999`) に変更

## docker-compose exec しても無反応

- 状況
    ```bash
    $ docker-compose exec clickhouse_server /bin/bash
    ```
    コンテナにログインできない。

- 解決方法
    - `docker-compose.yml` で service 名に指定している文字列を渡さなくては行けない。コンテナ名ではNG。
    ```bash
    $ docker-compose exec clickhouse /bin/bash
    ```

