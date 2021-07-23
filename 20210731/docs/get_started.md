# Getting started

- https://public.bybit.com/trading/ を使って暗号資産価格データをインサートして簡単なSELECT文を発行する

1. 前準備
    - [インストール](./install.md)
1. コンテナにログイン
    ```
    docker-compose exec clickhouse /bin/bash
    ```
1. 必要なツールをインストール
    ```bash
    apt update
    apt install curl -y
    apt install xz-utils
    ```
1. インサートするデータの確認
    - 今回は data ディレクトリに、サンプルデータを [Directory listing for /trading/](https://public.bybit.com/trading/)から適当にダウンロードして起きました。
    - データについているヘッダーはデータベースへインサートする時は不必要なので、第一行目は削除しています
    - 以下は、ダウンロード、展開、1行目削除をワンライナーで書いたコマンドです。
        ```bash
        $ wget -O - https://public.bybit.com/trading/BTCUSD/BTCUSD2021-07-22.csv.gz | gzip -d  | tail -n +2 > BTCUSD2021-07-22.csv
        ```
1. DataBase 作成
    ```
    clickhouse-client -q "CREATE DATABASE IF NOT EXISTS bybit"
    ``` 
1. Table 作成
    ```
    clickhouse-client < /sql/create_table.sql
    ```
1. データインサート
    ```bash
    for x in ./data/*.csv; do
    time clickhouse-client --query "INSERT INTO bybit.market FORMAT CSV" --max_insert_block_size=100000 < $x
    done
    ```
1. 確認
    ```
    clickhouse-client -q "SELECT COUNT(*) FROM bybit.market"
    ```

##  サンプルクエリ

1. SELECT 
    ```SQL
    SELECT * FROM bybit.market LIMIT 5
    ```
1. symbol ごとに平均
    ```sql
    SELECT symbol, avg(price) FROM bybit.market GROUP BY symbol
    ```
1. 分単位でグループ化して、OHLC と 平均を出す
    ```sql
    SELECT
        minute,
        symbol,
        any(price) AS Open,
        max(price) AS High,
        min(price) AS Low,
        anyLast(price) AS Last,
        avg(price) AS Mean    
    FROM bybit.market 
    GROUP BY symbol, toStartOfMinute(timestamp) AS minute
    ORDER BY minute
    LIMIT 10
    ```
    - [any](https://clickhouse.tech/docs/en/sql-reference/aggregate-functions/reference/any/#agg_function-any): Selects the first encountered value
    - [anyLast](https://clickhouse.tech/docs/en/sql-reference/aggregate-functions/reference/anylast/):Selects the last value encountered 

