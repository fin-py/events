# AIOHTTPハンズオン

- connpass: https://connpass.com/event/222786/

## 参加方法

Zoomのリンクは下記の手順を実施して出力されたURLにアクセスしてください
### 事前準備

次の環境を前提としています

- Pythonが実行できる
- [AIOHTTP](https://docs.aiohttp.org/en/stable/index.html) がインストールされている( `import aiohttp` ができる)

### スクリプトの実行

GitHubリポジトリから [entrance.py](https://github.com/fin-py/events/blob/main/20210912/entrance.py) をダウンロードします

次のコマンドはwgetコマンドを利用した例です、curlコマンドやブラウザからダウンロードしても構いません

```bash
wget https://raw.githubusercontent.com/fin-py/events/main/20210912/entrance.py
```

`entrance.py` を編集し、 `main` 関数の引数に `21` を渡します

```python
asyncio.run(main(21))
```

編集した `entrance.py` を実行します

```bash
python entrance.py
```

表示されたURLにブラウザからアクセスします

## 資料

- [Webドキュメント](https://aiohttp-hands-on.readthedocs.io/)
- [スライド](https://fin-py.github.io/events/)
