# UPDATE と DELETE 

- 参照：
    - [How to Update Data in ClickHouse](https://clickhouse.tech/blog/en/2016/how-to-update-data-in-clickhouse/)
    - [ALTER | ClickHouse Documentation](https://clickhouse.tech/docs/en/sql-reference/statements/alter/#mutations)

## Mutations

- UPDATE と DELETE はClickHouse には無い
- 代わりに ALTER クエリを使う
- この操作のことを **Mutations** と呼ぶ
- Mutations の代表的な操作が
    - `ALTER TABLE … DELETE` 
    - `ALTER TABLE … UPDATE`
- 頻繁に使用することを想定していないので、作業が重い操作
- `MergeTree` エンジンのテーブルでは、変更や削除の処理はPartitionデータ全体を書き換えることで実行される。

### Partitionデータ全体を書き換えるとは

サンプルデータを格納した `bybit.market` というテーブルは、`PARTITION BY toYYYYMM(timestamp)` と指定していましたが、もっと細かくパーティションを切ってみます。

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
PARTITION BY toStartOfInterval(timestamp, INTERVAL 8 hour)
ORDER BY timestamp    
``` 
これで、8時間ごとにパーティションに区切りました。このテーブルにデータを入れ直します。

パーティションを確認には、system.parts というテーブルを使います。

```sql
SELECT
    partition,
    count() AS number_of_parts,
    formatReadableSize(sum(bytes)) AS sum_size
FROM system.parts
WHERE active AND (database = 'bybit') AND (table = 'market')
GROUP BY partition
ORDER BY partition ASC

Query id: 92da8922-d0a7-4785-9563-494227c891fb
┌─partition───────────┬─number_of_parts─┬─sum_size──┐
│ 2021-07-22 00:00:00             │                 3 │    15.94 MiB │
│ 2021-07-22 08:00:00             │                 3 │    18.13 MiB │
│ 2021-07-22 16:00:00             │                 3 │    10.20 MiB │
└───────────────────────────┴───────┴
``` 
8時間ごとに区切られたデータをさらに `number_of_parts` 個に区切ってストアされていることがわかります。

UPDATEやDELETEは、**操作すべきデータが入っているデータパートを書き換える**、という方法で行われます。

## DELETE 

- 例：`timestamp >= '2021-07-22 04:30:00' and timestamp <= '2021-07-22 12:00:00' ` を削除
    ```sql
    ALTER TABLE bybit.market DELETE where timestamp >= '2021-07-22 04:30:00' and timestamp <= '2021-07-22 12:00:00'
    ```
- パーティションを確認
    ```sql
    SELECT
        partition,
        count() AS number_of_parts,
        formatReadableSize(sum(bytes)) AS sum_size
    FROM system.parts
    WHERE active AND (database = 'bybit') AND (table = 'market')
    GROUP BY partition
    ORDER BY partition ASC

    Query id: aa064aab-d76d-4571-94d0-767a74815fa9

    ┌─partition───────────┬─number_of_parts─┬─sum_size──┐
    │ 2021-07-22 00:00:00             │                 3 │     8.74 MiB │
    │ 2021-07-22 08:00:00             │                 3 │    10.37 MiB │
    │ 2021-07-22 16:00:00             │                 3 │    10.20 MiB │
    └───────────────────────────┴───────┴
    ```  
- 削除したデータが入っていたパーティションだけサイズが減っていることがわかります。

## UPDATE 
- 例：`2021-07-22 16:00:00` 以降の BTCUSDで、priceが 32569以下をすべて0にする

    ```sql
    ALTER TABLE bybit.market UPDATE price = 0 where timestamp >= '2021-07-22 16:00:00' and symbol = 'BTCUSD' and price < 32569
    ```
    ```sql
    SELECT
        partition,
        count() AS number_of_parts,
        formatReadableSize(sum(bytes)) AS sum_size
    FROM system.parts
    WHERE active AND (database = 'bybit') AND (table = 'market')
    GROUP BY partition
    ORDER BY partition ASC

    Query id: 9c79da47-6fc1-437f-b3b8-fd2d7ffcf686

    ┌─partition───────────┬─number_of_parts─┬─sum_size──┐
    │ 2021-07-22 00:00:00             │                 3 │     8.74 MiB │
    │ 2021-07-22 08:00:00             │                 3 │    10.37 MiB │
    │ 2021-07-22 16:00:00             │                 3 │    10.05 MiB │
    └───────────────────────────┴───────┴
    ```
