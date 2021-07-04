# attendance-alarm
🔔 Notify when class starts by mentioning and playing some music.\
🔔 講義の開始時にメンションを飛ばし、アラームまで鳴らす Discord ボット

## 必要なもの
### Python パッケージ
`pip install -r requirements.txt` を使用してインストールします。
* [discord.py[voice]](https://discordpy.readthedocs.io/ja/latest/)
* [PyNaCl](https://pypi.org/project/PyNaCl/)
* [PyYaml](https://pypi.org/project/PyYAML/)
### OS パッケージ
* libffi-dev

## セットアップ
### Docker を使う方法 (Docker Compose)
1. `app/resource/config.example.yml` と `docker-compose.yml` をダウンロードし、同じディレクトリに配置します。作業ディレクトリ内は以下のようになるはずです。
```
$ exa --tree ./
.
├── config.example.yml
└── docker-compose.yml
```
1. `config.example.yml` を `config.yml` にリネームし、これを編集します。\
Botのトークンや使用するチャンネルのID等を記述してください。
1. `docker-compose.yml` が配置されているディレクトリ内で、`docker-compose up -d` を実行します。

### Docker を使わない方法
1. まず、`app/resource/config.example.yml` を `app/resources/config.yml` にコピーし、これを編集します。\
Botのトークンや使用するチャンネルのID等を記述してください。
1. 上記の「必要なもの」に従って、必須パッケージをインストールします。  
1. `python bot.py` 等で実行します。

## リポジトリの構造

* `app/`: ボット本体のソースコード。
* `Dockerfile`: Docker コンテナイメージをビルドするためのファイル
* `docker-compose.yml`: Docker Compose でボットを実行するための定義ファイル

## ライセンス
このプロジェクトは画像や音声などのアセットファイルなどを除き、[MIT License](https://opensource.org/licenses/MIT)に従ってライセンスされています。
