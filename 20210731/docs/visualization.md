# 可視化

公式ドキュメント: https://redash.io/help/user-guide/visualizations/visualizations-how-to

## 可視化クエリの例

### Counter

騰落率トップ

```sql
-- WITH yesterday() as yesterday
WITH
  (SELECT date_sub(DAY, 1, toDate('2021-07-19 00:00:00'))) AS yesterday

SELECT symbol,
       (anyLast(price) - any(price)) / any(price) AS pctchange
FROM bybit.market
WHERE `timestamp` >= yesterday
GROUP BY symbol,
         toStartOfDay(`timestamp`) AS oneday
ORDER BY pctchange DESC
LIMIT 1
```

### Chart

```sql
-- WITH yesterday() as yesterday
WITH (SELECT date_sub(DAY, 1, toDate('2021-07-18 23:59:59'))) as yesterday

SELECT
    minute,
    anyLast(price) AS Price
FROM bybit.market 
WHERE `timestamp` >= yesterday AND symbol = '{{symbol}}'
GROUP BY toStartOfMinute(timestamp) AS minute
ORDER BY minute
```