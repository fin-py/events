# Redashの機能を利用したクエリ

- クエリに `{{}}` を含めると，その部分がパラメータになる
- UIが実装される
    - Text
    - Number
    - Dropdown List
    - Query Based Dropdown List
- クエリのAS句に `カラム名::filter` または `カラム名::multi-filter` にするとフィルタリングができる
    - WHERE句を自動的に処理
    - Clickhouseには対応していない？

## クエリ例

### パラメータ付きクエリ

日付の範囲と通貨ペアをUIで指定

```sql
SELECT `timestamp`,
       `symbol`,
       `price`
FROM bybit.market
WHERE `timestamp` >= {{from_}}
  AND `timestamp` <= {{to_}}
  AND `symbol` = {{symbol}}
```

- 単一選択: Text
- 複数選択: Dropdown List
- クエリベース: Query Based Dropdown List

### 書式付きクエリ

```sql
-- WITH yesterday() as yesterday
WITH
  (SELECT date_sub(DAY, 1, toDate('2021-07-19 00:00:00'))) AS yesterday

SELECT symbol,
       (anyLast(price) - any(price)) / any(price) AS pctchange,
       CASE
           WHEN pctchange > 0 THEN '<div class="bg-success">やったー</div>'
           WHEN pctchange < 0 THEN '<div class="bg-warning">しょぼーん</div>'
        END AS Color
FROM bybit.market
WHERE `timestamp` >= yesterday
GROUP BY symbol,
         toStartOfDay(`timestamp`) AS oneday
ORDER BY pctchange DESC
```