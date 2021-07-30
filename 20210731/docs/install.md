# インストール
## 前提条件
- 今回は clickhouse-server を docker-compose で構築する方法を紹介します。よってこのTutorialに従う場合は docker / docker-compose のインストールをお願いします。
- 他の方法でのインストールは [Installation | ClickHouse Documentation](https://clickhouse.tech/docs/en/getting-started/install/)を参照してください


## 手順
1. 適当なディレクトリ作成して cd 
1. 必要なディレクトリとファイルを作成
    ```bash=
    $ mkdir data db users sql
    $ touch docker-compose.yml
    ```
1. `user` ディレクトリ配下にユーザー設定用ファイルを作成
    - 任意のユーザー名で、`ユーザー名.xml` を作成
    - clickhouse-server の `/etc/clickhouse-server/users.d/` ディレクトリに配置
    - 例： `read-write-user.xml` 
        ```bash
        $ touch users/read-write-user.xml
        ```
    - ユーザー設定
        ```xml
        <?xml version="1.0"?>
        <yandex>
            <users>
                <read-write-user>
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
                </read-write-user>
            </users>
        </yandex>
        ```
        - `read-write-user` タグは自分の名前に変えてください
        - <access_management>1</access_management>：**読み書き可。0であれば読みのみ可**。
        - その他の設定に関してはこちら：[User Settings | ClickHouse Documentation](https://clickhouse.tech/docs/en/operations/settings/settings-users/#user-settings)
1. `docker-compose.yml` 作成
    ```bash
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
                # コンテナのデータボリューム
                - type: bind
                  source: "./db"
                  target: "/var/lib/clickhouse"

                # ユーザファイル
                - type: bind
                  source: "./users"
                  target: "/etc/clickhouse-server/users.d"

                # .sql ファイル格納
                - type: bind
                  source: "./sql"
                  target: "/sql"

                # サンプルデータを格納
                - type: bind
                  source: "./data"
                  target: "/data"
    ```
    - 参考
        - [yandex/clickhouse-server - Docker Image | Docker Hub](https://hub.docker.com/r/yandex/clickhouse-server/)
        - [[ClickHouse] ローカルで、1分でClickHouseの環境を構築する - Qiita](https://qiita.com/xymmk/items/eeac2e9a34573006075d)
        - [xymmk/clickhouse_for_local: startup clickhouse at local](https://github.com/xymmk/clickhouse_for_local)
        - [Dockerのバックアップの考え方とその方法について](https://www.memotansu.jp/docker/489/)

1. 起動
    ```bash
    $ docker-compose up -d
    ```
1. 確認
    ```bash
    $ docker-compose ps
    ``` 
1. 停止
    ```bash
    $ docker-compose down
    ```
