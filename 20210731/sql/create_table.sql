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