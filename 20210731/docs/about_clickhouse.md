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
