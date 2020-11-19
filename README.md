# [yudete](https://github.com/yudete) / attendance-alarm
講義の開始時にメンションを飛ばし、アラームまで鳴らす Discord ボット

## 必要なもの
* [discord.py](https://discordpy.readthedocs.io/ja/latest/) *voice モジュール込み。*
    ```
    pip install discord.py[voice]
    ```
* [PyNaCl](https://pypi.org/project/PyNaCl/)
    ```
    pip install pynacl
    ```
* libffi-dev
    ```
    sudo apt install libffi-dev
    ```
* libnacl-dev
    ```
    sudo apt install libnacl-dev
    ```

## 動かし方
1. まず、環境変数 `TOKEN` にボットのトークンを追加します。
    * Windows
        ```
        set TOKEN=GOES_HERE
        ```
    * Linux
        ```
        export TOKEN=GOES_HERE
        ```
    以上は**一時的に**環境変数を追加するものですが、必要にしたがってそれぞれのOSの手段で恒久的に環境変数を設定することもできます。
1. 上記の「必要なもの」に従って、必須パッケージをインストールします。  
1. `python bot.py` 等で実行します。
    正常な動作にはソースコード中のチャンネルIDやロールIDが稼働させるサーバー内のものと一致している必要があるため、多くの改変が必要になる場合があります。

## このリポジトリの構造
* [bot.py](https://github.com/yudete/attendance-alarm/blob/main/bot.py)  
ボット本体のソースコード。
* [attendance-alarm.service](https://github.com/yudete/attendance-alarm/blob/main/attendance-alarm.service)  
Systemd 向けのユニットファイル。
* [audio.wav](https://github.com/yudete/attendance-alarm/blob/main/audio.wav)  
アラームに使われる音声ファイル。
* [logo.png](https://github.com/yudete/attendance-alarm/blob/main/logo.png)  
ファイル名を見なさい

## License
このプロジェクトは画像や音声ファイルなどのアセットファイルなどを除き、[MIT License](https://opensource.org/licenses/MIT)に従ってライセンスされています。