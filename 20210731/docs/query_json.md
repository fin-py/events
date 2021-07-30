# JSONのクエリ

- 公式ドキュメント: https://redash.io/help/data-sources/querying/json-api#Return-an-inner-object
- YAML記法でクエリ

## BYBIT APIの例

- APIリファレンス: https://bybit-exchange.github.io/docs/inverse/

```yaml
url: https://api.bybit.com/v2/public/orderBook/L2?symbol=BTCUSD
path: result
fields: [price, size]
```

```yaml
# url: https://api.bybit.com/v2/public/kline/list?symbol=BTCUSD&interval=1&limit=20&from=1581231260

url: https://api.bybit.com/v2/public/kline/list
params:
    symbol: BTCUSD
    interval: 1
    limit: 20
    from: 1581231260
path: result
```