# Python ClickHouse Client 

## インストール
- [Welcome to clickhouse-driver — clickhouse-driver 0.2.1 documentation](https://clickhouse-driver.readthedocs.io/en/latest/)
- Python 3.4以上
- `pip install clickhouse-driver`


## 接続

- tutorial 通り、install と getting started が終わっている仮定しています。

    ```python
    >>> from clickhouse_driver import Client
    >>> client = Client(host='localhost', user='read-write-user', port='9000')
    >>> client.execute("show databases")
    [('default',), ('system',), ('bybit',)]
    ```