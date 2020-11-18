# [yudete](https://github.com/yudete) / attendance-alarm
Discord ボット: 出席ボタンを押す通知を送信

## Requirements
* [discord.py](https://discordpy.readthedocs.io/ja/latest/) **including VOICE** for whole operating
    ```
    pip install discord.py[voice]
    ```
* [PyNaCl](https://pypi.org/project/PyNaCl/) for play audio file
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

## Repository structure
* [bot.py](https://github.com/yudete/attendance-alarm/blob/main/bot.py)  
Source code
* [attendance-alarm.service](https://github.com/yudete/attendance-alarm/blob/main/attendance-alarm.service)  
Unit file (Systemd)
* [audio.wav](https://github.com/yudete/attendance-alarm/blob/main/audio.wav)  
Audio file for alarm
* [logo.png](https://github.com/yudete/attendance-alarm/blob/main/logo.png)  
LOOK AT FILE NAME

## License
This project is under the MIT License. EXCLUDING ASSETS