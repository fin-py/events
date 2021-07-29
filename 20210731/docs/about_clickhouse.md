# ClickHouseとは



## ClickHouse とは
- ウェブサイト：[ClickHouse - fast open-source OLAP DBMS](https://clickhouse.tech/)
- ソースコード: [ClickHouse/ClickHouse: ClickHouse® is a free analytics DBMS for big data](https://github.com/ClickHouse/ClickHouse)
- 公式ドキュメント: https://clickhouse.tech/docs/en/
- オープンソース
- データ分析のためのデータベースマネジメントシステム
- 時系列データの保存、集計に特化
- クエリ検索パフォーマンスがとても優れている

### 作者
- Yandex.Metrica
- [2011年Nasdaqに上場](https://finance.yahoo.com/quote/YNDX/)
- ウェブ解析プラットフォーム用に開発
- ロシア人
 
### ユーザー
- [Adopters](https://clickhouse.tech/docs/en/introduction/adopters/)：実際にビジネスで使っている会社一覧
    - 中国やロシアの会社が多い, Alibaba, Tencent
    - microsoft, ebay, Deutsche Bank などもある
### ユースケース
- Logging, Monitering, Geo, Data Processing, Analytics, などなど
- 主にOLAP（Online Analytical Processing オンライン分析処理)分野での利用が多いらしい

### 特徴
- 得意なこと
    - データ検索速度が超高速
    - データ集計（GroupByなど）速度が超高速
    - 大量データの一括登録(Insert)速度が超高速
    - データサイズがとても小さい(Partition)
    - 時系列に強い
- 苦手なこと
    - [Features that Can Be Considered Disadvantages](https://clickhouse.tech/docs/en/introduction/distinctive-features/#clickhouse-features-that-can-be-considered-disadvantages)
    - すでに挿入されているデータを高レートかつ低レイテンシーで修正・削除する機能はない。
    - DELETE / UPDATE は出来るけど、独自方法で行う
    - 単一の行の検索


### テーブルエンジン
- [Table Engines | ClickHouse Documentation](https://clickhouse.tech/docs/en/engines/table-engines/)
- データの種類によってテーブルエンジンを変えてよりよいパフォーマンスを得る
- エンジンによって以下のことが決定
    - データの保存場所、書き込み場所、読み込み場所
    - サポートされるクエリ
    - データへの同時アクセス
    - インデックスの使い方（もしあれば）
    - マルチスレッドでのリクエストを出来るかどうか
    - データレプリケーションのパラメータ
- 結局いちばんメジャーな `MergeTree` がよく使われる（と聞いた）


エンジンファミリー|説明|特徴|エンジン
---|---|---|---
MergeTree|一番メジャー。<br>高負荷な作業に最も向いてる。|レプリケーション、<br>パーティション、<br>secondary data-skipping indexes<br>などの機能をサポート|MergeTree<br> ReplacingMergeTree<br> SummingMergeTree<br> AggregatingMergeTree<br> CollapsingMergeTree<br> VersionedCollapsingMergeTree<br> GraphiteMergeTree
Log|機能最小限、軽量エンジン。<br>100万行までのデータに最適||TinyLog<br> StripeLog<br> Log
Integration |他のデータストレージとの<br>コミュニケーションエンジン||ODBC<br> JDBC<br> MySQL<br> MongoDB<br> HDFS<br> S3<br> Kafka<br> EmbeddedRocksDB<br> RabbitMQ<br> PostgreSQL
Special|||Distributed<br> MaterializedView<br> Dictionary<br> Merge (注意：MergeはMergeTreeでは無い)<br> File<br> Null<br> Set<br> Join<br> URL<br> View<br> Memory<br> Buffer


#### MergeTree ファミリーについて補足
- このファミリーに入っているテーブルエンジンが最も堅牢
- 超巨大なデータを挿入するための設計
- テーブルはパーティションに区切られて、バックグラウンドでマージするルールが適用される仕組み
- データレプリケーションに対応
    - レプリケーションについての詳細はこちら：[Data Replication ](https://clickhouse.tech/docs/en/engines/table-engines/mergetree-family/replication/) 
