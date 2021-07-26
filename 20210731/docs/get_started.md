# Getting started

- https://public.bybit.com/trading/ を使って暗号資産価格データをインサートして簡単なSELECT文を発行する

1. 前準備
    - [インストール](./install.md)
1. インサートするデータの確認
    - サンプルデータを[Directory listing for /trading/](https://public.bybit.com/trading/)から適当にダウンロードして、`data` ディレクトリに配置して下さい
    - データについているヘッダーはデータベースへインサートする時は不必要なので、第一行目は削除します
    - 以下は、ダウンロード、展開、1行目削除をワンライナーで書いたコマンドです。
        ```bash
        $ wget -O - https://public.bybit.com/trading/BTCUSD/BTCUSD2021-07-22.csv.gz | gzip -d  | tail -n +2 > BTCUSD2021-07-22.csv
        ```
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
1. '2021-07-22 01:00:00'以降
    ```sql
    SELECT * FROM bybit.market WHERE timestamp > '2021-07-22 01:00:00' Limit 5 
    ```
1. タイムゾーン確認
    ```sql
    SELECT timeZoneOf(timestamp) AS date_tokyo from bybit.market LIMIT 5
    ```    
1. タイムゾーン変更
    ```sql
    SELECT toTimezone(timestamp, 'Asia/Tokyo') AS date_tokyo from bybit.market LIMIT 5
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
    - `toStartOfFiveMinute` / `toStartOfTenMinutes` / `toStartOfFifteenMinutes` など でインターバルを変更可
    - `toStartOfInterval` で、任意のインターバル可
        - `toStartOfInterval(timestamp, INTERVAL 23 minute)` : 23 分毎 
1. -If 関数を使う
    - aggregate function (sum / mean / count など ... ) に接尾辞 `If` をつけて条件を渡すことが出来る。
    ```sql
    -- 以下二つは同じ結果
    select sumIf(price, symbol='BTCUSD') from bybit.market
    select sum(price) from bybit.market where symbol = 'BTCUSD'
    ```
1. もっともよく出てくる値を出す
    ```sql
    select symbol, anyHeavy(price) from bybit.market GROUP BY symbol
    -- 指定時間よりあとで探す
    select symbol,  anyHeavyIf(price, timestamp > '2021-07-22 12:50:20' ) from bybit.market GROUP BY symbol
    ```
1. 配列で取得
    ```sql
    SELECT
        symbol,
        groupArray(5)(price)
    FROM bybit.market
    GROUP BY symbol
    ```
    - `groupArray(column)`
    - `groupArray(size)(column)`: size で配列の個数を指定
    - [groupArray ](https://clickhouse.tech/docs/en/sql-reference/aggregate-functions/reference/grouparray/)
1. ウェイト付き平均、ただしシンボル別にウェイトを変更
    ```sql
    SELECT
        avgWeightedIf(price, 0.1, symbol = 'BTCUSD'),
        avgWeightedIf(price, 1.5, symbol = 'ETHUSD'),
    FROM bybit.market
    ```
1. Group by したデータをArrayで取得
    ```sql
    SELECT
        minute,
        tickerDirection,
        groupArrayMovingAvgIf(price, symbol = 'BTCUSD')
    FROM bybit.market
    GROUP BY
        tickerDirection,
        toStartOfInterval(timestamp, toIntervalSecond(1)) AS minute
    ORDER BY minute ASC
    LIMIT 5    
    ```
