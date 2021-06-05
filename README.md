# attendance-alarm
🔔 Notify when class starts by mentioning and playing some music.\
🔔 講義の開始時にメンションを飛ばし、アラームまで鳴らす Discord ボット

## 必要なもの
### Python パッケージ
`pip install -r requirements.txt` を使用してインストールします。
* [discord.py[voice]](https://discordpy.readthedocs.io/ja/latest/)
* [PyNaCl](https://pypi.org/project/PyNaCl/)
* [PyYaml](https://pypi.org/project/PyYAML/)
### Debian 系 OS で必要なパッケージ
* libffi-dev
    ```
    sudo apt install libffi-dev
    ```
* libnacl-dev
    ```
    sudo apt install libnacl-dev
    ```

## 動かし方
1. まず、`resource/config.example.yml` を `resources/config.yml` にコピーし、これを編集します。  
   Botのトークンや使用するチャンネルのID等を記述してください。
    ```yml
    # Bot Settings
    bot-token: Please-Replace-Here-To-Bot-Token #botのトークンをここに書いてください

    # Server Settings
    server-id: 0 #Server-ID
    server-channel-text: 0 #Alarm-Channel(Text)-ID
    server-channel-voice: 0 #Alarm-Channel(Voice)-ID

    # Dev Settings
    dev-debug-mode: false #debug-mode(true|false)
    dev-channel-text: 0 #Dev-Alarm-Channel(Text)-ID
    dev-channel-voice: 0 #Dev-Alarm-Channel(Text)-ID

    # Template
    # {role}: 特定の時限のロールID
    # {weekday}: 曜日
    # {time}: 時限
    template: "<@&{role}> {weekday}曜日 {time}限 の開始時刻です。出席確認をしてください。"

    # Messages
    playing: "起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ"
    stopped: "再生を停止しました。"
    disconnected: "ボイスチャンネルから切断しました。"

    ## Role ID
    # 月曜日
    monday-1: 0
    monday-2: 0
    monday-3: 0
    monday-4: 0
    monday-5: 0

    # 火曜日
    tuesday-1: 0
    tuesday-2: 0
    tuesday-3: 0
    tuesday-4: 0
    tuesday-5: 0

    # 水曜日
    wednesday-1: 0
    wednesday-2: 0
    wednesday-3: 0
    wednesday-4: 0
    wednesday-5: 0

    # 木曜日
    thursday-1: 0
    thursday-2: 0
    thursday-3: 0
    thursday-4: 0
    thursday-5: 0

    # 金曜日
    friday-1: 0
    friday-2: 0
    friday-3: 0
    friday-4: 0
    friday-5: 0
    ```
1. 上記の「必要なもの」に従って、必須パッケージをインストールします。  
1. `python bot.py` 等で実行します。

## このリポジトリの構造
* [bot.py](https://github.com/yudete/attendance-alarm/blob/main/bot.py)  
ボット本体のソースコード。
* [attendance-alarm.service](https://github.com/yudete/attendance-alarm/blob/main/attendance-alarm.service)  
Systemd 向けのユニットファイル。Linux 等でデーモン化する際に使用します。
* [resources](https://github.com/yudete/attendance-alarm/blob/main/resource)  
設定ファイルや音声ファイルを入れるディレクトリ
    * [audio.wav](https://github.com/yudete/attendance-alarm/blob/main/resource/audio.wav)  
    アラームに使われる音声ファイル。
    * [logo.png](https://github.com/yudete/attendance-alarm/blob/main/resource/logo.png)  
    ボット アカウントに用いられているアイコン
    * [config.yml](https://github.com/yudete/attendance-alarm/blob/main/resource/config.yml)  
    トークンやチャンネルIDを設定するためのファイル

## ライセンス
このプロジェクトは画像や音声などのアセットファイルなどを除き、[MIT License](https://opensource.org/licenses/MIT)に従ってライセンスされています。
