# Getting started

- https://public.bybit.com/trading/ を使って暗号資産価格データをインサートして簡単なSELECT文を発行する

1. 前準備
    - [インストール](./install.md)
1. `docker-compose exec clickhouse /bin/bash` 
1. 必要なツールをインストール
    ```bash
    apt update
    apt install curl -y
    apt install xz-utils
    ```
1. インサートしたいデータをダウンロード
    1.     


- TODO ：データのダウンロードからインサートまでは、どりらんさんのを参考にする

## クライアントコンテナにログイン
- `docker run -it --rm --link <サーバーのコンテナ名>:clickhouse-server yandex/clickhouse-client --host clickhouse-server --user <ユーザー名>`
- 例
    ```
    $ docker run -it --rm --link some-clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server --user shinseitaro

    ClickHouse client version 21.6.5.37 (official build).
    Connecting to clickhouse-server:9000 as user shinseitaro.
    Connected to ClickHouse server version 21.6.5 revision 54448.

    9942c50ba5cf :)     
    ```

## データベースの作成
- 例： `bybit` 用データベースを作成
```sql
CREATE DATABASE IF NOT EXISTS bybit
``` 
## テーブルの作成・INSERT
```sql
CREATE TABLE bybit.market
    (
        `timestamp` DateTime64,
        `symbol` String,
        `side` FixedString(4),
        `size` Float32,
        `price` Float64,
        `tickerDirection` FixedString(15),
        `trdMatchID` String,
        `grossValue` Float64,
        `homeNotional` Float64,
        `foreignNotional` Float64
    )
    ENGINE = MergeTree
    PARTITION BY toYYYYMM(timestamp)
    ORDER BY timestamp
```
- https://clickhouse.tech/docs/en/sql-reference/statements/insert-into/
- `INSERT INTO [db.]table [(c1, c2, c3)] FORMAT Values (v11, v12, v13), (v21, v22, v23), ...
`    にしたほうが早い
- TODO: どりらんさんのを確認

## サンプルクエリ