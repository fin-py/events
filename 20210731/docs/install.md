# インストール

## 手順
1. `user` ディレクトリ配下にユーザー設定用ファイルを作成
1. `docker-compose.yml` があるディレクトリに移動
1. `docker-compose up -d` 
1. `docker-compose exec clickhouse /bin/bash` 

## ユーザー設定用ファイルの説明
- `ユーザー名.xml` を clickhouse-server の `/etc/clickhouse-server/users.d/` に設置することでユーザーを作成出来る
- `access_management` : 1が読み書きできるユーザ、0がReadOnlyのユーザー
- ファイル例
    - `shinseitaro.xml`
    ```xml
    <?xml version="1.0"?>
    <yandex>
        <users>
            <shinseitaro> <!-- 名前書き換え -->
                <password></password>
                <networks>
                    <ip>::/0</ip>
                </networks>
                <!-- Settings profile for user. -->
                <profile>default</profile>
                <!-- Quota for user. -->
                <quota>default</quota>
                <!-- User can create other users and grant rights to them. -->
                <access_management>1</access_management>
            </shinseitaro><!-- 名前書き換え -->
        </users>
    </yandex>
    ```
- 参照：[User Settings | ClickHouse Documentation](https://clickhouse.tech/docs/en/operations/settings/settings-users/#user-settings)

## docker-compose の説明

```dockerfile
version: '3'
services: 
    clickhouse: # サービス名 docker-compose exec する時に使う名前
        image: yandex/clickhouse-server # DockerHub にあるイメージ
        container_name: clickhouse_server 
        ports:
            # httpリクエストに使うポート
            - 8123:8123
            # クライアントポート
            - 9000:9000
        volumes: 
            - type: bind 
              source: "./db" # コンテナのデータボリューム
              target: "/var/lib/clickhouse"
            - type: bind 
              source: "./users" # ユーザファイル
              target: "/etc/clickhouse-server/users.d"
            - type: bind
              source: "./sql" # .sql ファイル格納
              target: "/sql"
            - type: bind
              source: "./data" # サンプルデータを格納
              target: "/data"

```

### 参考
- [yandex/clickhouse-server - Docker Image | Docker Hub](https://hub.docker.com/r/yandex/clickhouse-server/)
- [[ClickHouse] ローカルで、1分でClickHouseの環境を構築する - Qiita](https://qiita.com/xymmk/items/eeac2e9a34573006075d)
- [xymmk/clickhouse_for_local: startup clickhouse at local](https://github.com/xymmk/clickhouse_for_local)
- [Dockerのバックアップの考え方とその方法について](https://www.memotansu.jp/docker/489/)