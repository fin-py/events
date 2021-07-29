# Redashハンズオン環境

## docker-composeによる環境設定

### 起動方法

```
docker-compose -f docker-compose_redash.yml run --rm server create_db
docker-compose -f docker-compose_redash.yml up -d
```

### 停止方法

```bash
docker-compose -f docker-compose_redash.yml stop
```

### 開始方法

```bash
docker-compose -f docker-compose_redash.yml start
```

### 終了方法

```bash
docker-compose -f docker-compose_redash.yml down
```

## Redash初期設定

docker-composeが起動している状態でブラウザから `http://localhost:5000/` にアクセス

![](./img/2021-07-29-11-56-09.png)

次の項目を入力して「Setup」

- Name
- Email Address
- Password
- Organization Name

![](./img/2021-07-29-11-59-24.png)

「Settings」をクリック

![](./img/2021-07-29-12-00-11.png)

「+New Data Source」をクリック

![](./img/2021-07-29-12-01-06.png)

「Clickhouse」を選択

![](./img/2021-07-29-12-03-00.png)

下記を入力して「Create」

- Name: 任意
- Url: http://clickhouse:8123
- Password: Clickhouseで設定したもの
- User: Clickhouseで設定したもの
- Database Name: bybit

![](./img/2021-07-29-12-05-25.png)

「Test Connection」をクリックし、「Success」が表示されたらOK
