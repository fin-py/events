# インストール

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

## docker-compose.yml 

