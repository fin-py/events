# Getting started

https://public.bybit.com/trading/ を使って暗号資産価格データをインサートして簡単なSELECT文を発行してみましょう

## データインサート
### 手順
1. インサートしたいデータをホストの `data` ディレクトリへ保存
1. データインサート用のSQLを作成
1. コンテナへログイン
1. データベースとテーブルを作成
1. データをインサート
1. 確認

### 作業

1. 前準備
    - [ClickHouse-server インストール](./install.md)
1. インサートするデータのダウンロード
    - サンプルデータを[Directory listing for /trading/](https://public.bybit.com/trading/)から適当にダウンロードして、`data` ディレクトリに格納。
    - 一行目のヘッダーは不要なので削除。
    - 以下は、ダウンロード、展開、1行目削除をワンライナーで書いたコマンドです。
        ```bash
        $ wget -O - https://public.bybit.com/trading/BTCUSD/BTCUSD2021-07-22.csv.gz | gzip -d  | tail -n +2 > data/BTCUSD2021-07-22.csv
        ```
1. データインサート用のSQL作成
    - テーブル作成sql
        ```bash
        $ touch sql/create_table.sql
        ```
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
        - [Data Types | ClickHouse Documentation](https://clickhouse.tech/docs/en/sql-reference/data-types/)
        - [FixedString(N) | ClickHouse Documentation](https://clickhouse.tech/docs/en/sql-reference/data-types/fixedstring/)

1. コンテナにログイン
    ```
    docker-compose exec clickhouse /bin/bash
    ```
    <!-- 1. 必要なツールをインストール
        ```bash
        apt update
        apt install curl -y
        apt install xz-utils
        ``` -->
1. CLI を使ってクエリを実行
    - `clickhouse-client` 
    - [Command-Line Client | ClickHouse Documentation](https://clickhouse.tech/docs/en/interfaces/cli/#command-line-options)
    ```bash
    clickhouse-client --version
    ClickHouse client version 21.7.4.18 (official build).
    ```

1. DataBase 作成
    ```bash
    clickhouse-client -q "CREATE DATABASE IF NOT EXISTS bybit"
    ``` 
    - `-q` もしくは `--query` オプションでクエリ実行
1. Table 作成
    ```
    clickhouse-client < /sql/create_table.sql
    ```
    - sql ファイルのクエリを実行
1. データインサート
    - ファイルデータをインサートする
        - `clickhouse-client -q "INSERT INTO bybit.market FORMAT CSV" --max_insert_block_size=[一度にインサートする行数] < [ファイルパス]`
        - `--max_insert_block_size=` で一度にインサートする行を指定
        - `FORMAT `でファイルタイプを指定
        - 対応ファイル一覧はこちら：[Input and Output Formats | ClickHouse Documentation](https://clickhouse.tech/docs/en/interfaces/formats/)
    - 例
        ```bash
        clickhouse-client -q "INSERT INTO bybit.market FORMAT CSV" --max_insert_block_size=100000 < ./data/BTCUSD.csv
        ```
    - ループでインサートする
        ```bash
        for x in ./data/*.csv; do
        time clickhouse-client -q "INSERT INTO bybit.market FORMAT CSV" --max_insert_block_size=100000 < $x
        done
        ```

1. 確認
    ```bash
    clickhouse-client -q "SELECT COUNT(*) FROM bybit.market"
    ```

## クライアントにログイン

- default ユーザとしてログイン
    ```bash
    clickhouse-client
    ```
- 特定のユーザとしてログイン
    ```bash
    clickhouse-client -u read-write-user --password xxxxx
    ```
- [Command-Line Client | ClickHouse Documentation](https://clickhouse.tech/docs/en/interfaces/cli/#command-line-options)

##  サンプルクエリ

1. SELECT 
    ```SQL
    SELECT * FROM bybit.market LIMIT 5
    ```
1. symbol ごとに平均
    ```sql
    SELECT symbol, avg(price) FROM bybit.market GROUP BY symbol
    ```
1. Where 句
    ```sql
    SELECT 
    * 
    FROM bybit.market 
    WHERE timestamp > '2021-07-22 01:00:00' and tickerDirection = 'ZeroMinusTick'
    ```
1. タイムゾーン確認
    ```sql
    SELECT timeZoneOf(timestamp) AS TimeZone, * from bybit.market LIMIT 5
    ```    
1. 東京時間を追加
    ```sql
    SELECT toTimezone(timestamp, 'Asia/Tokyo') AS date_tokyo, * from bybit.market LIMIT 5
    ```
1. 分単位でグループ化して、OHLC と 平均をSymbolごとに出力
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
        avgWeightedIf(price, 0.1, symbol = 'BTCUSD') as avgBTCUSD,
        avgWeightedIf(price, 1.5, symbol = 'ETHUSD') as avgETHUSD
    FROM bybit.market
    ```
1. Group by したデータをArrayで取得。配列のデータは移動平均。
    ```sql
    SELECT minute, symbol, groupArrayMovingAvg(5)(price) as ma5 
    from bybit.market
    group by symbol,toStartOfMinute(timestamp) AS minute
    ORDER BY minute ASC
    limit 10
    ```
    - `groupArrayMovingAvg(5)(price)` : `5` がwindow size。`price` がターゲット。
    - [groupArrayMovingAvg | ClickHouse Documentation](https://clickhouse.tech/docs/en/sql-reference/aggregate-functions/reference/grouparraymovingavg/#agg_function-grouparraymovingavg)

