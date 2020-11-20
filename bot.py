# coding: utf-8

# import
import discord
from discord.ext import tasks
from datetime import datetime
import os
import yaml

# リソースの読み込み
AUDIO_PATH = os.getcwd() + os.path.sep + "resources" + os.path.sep + "audio.wav"

# クライアントオブジェクトを生成
client = discord.Client()

# 設定ファイルの読み込み
path = os.getcwd() + os.path.sep + "resources" + os.path.sep + "config.yml"
with open(path, 'r', encoding="utf-8") as file:
    ymlobj = yaml.safe_load(file)
    TOKEN = ymlobj['bot-token']
    GUILD_ID = ymlobj['server-id']
    CHANNEL_TEXT = ymlobj['server-channel-text']
    CHANNEL_VOICE = ymlobj['server-channel-voice']
    DEV_DEBUG_MODE = ymlobj['dev-debug-mode']
    DEV_CHANNEL_TEXT = ymlobj['dev-channel-text']
    DEV_CHANNEL_VOICE = ymlobj['dev-channel-text']  # not implemented
    TEMPLATE = ymlobj['template']  # 通知メッセージのテンプレート
    PLAYING = ymlobj['playing']
    STOPPED = ymlobj['stopped']
    DISCONNECTED = ymlobj['disconnected']

# DEV_DEBUG_MODE が有効だった場合、ボットの起動時に config を表示する
if DEV_DEBUG_MODE:
    print("> ボットの設定 ▼")
    print("> TOKEN: " + TOKEN)
    print("> GUILD_ID: " + str(GUILD_ID))
    print("> CHANNEL_TEXT: " + str(CHANNEL_TEXT))
    print("> CHANNEL_VOICE: " + str(CHANNEL_VOICE))
    print("> DEV_CHANNEL_TEXT: " + str(DEV_CHANNEL_TEXT))
    print("> DEV_CHANNEL_VOICE: " + str(DEV_CHANNEL_VOICE))

# グローバル変数の初期化
voice = None
player = None


# 起動通知
@client.event
async def on_ready():
    print("ボットを起動しました。discord.py バージョン", discord.__version__)  # 起動確認メッセージ
    if PLAYING != None:
        await client.change_presence(activity=discord.Game(name=PLAYING))  # __ をプレイ中


@client.event
async def on_message(message):
    weekday = datetime.now().weekday()
    global voice, player
    if message.content == '!debug':
        # ボイスチャンネルに参加、音声を再生
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        if player is None:  # もし何も再生されていなかったら？
            # 全員に音声が流れるのを防ぐ
            # 一旦、全員をスピーカーミュートする。
            bot_vc = client.get_channel(CHANNEL_VOICE)
            for member in bot_vc.members:
                await member.edit(deafen=True)
            # 特定のロールのみミュート解除する。
            guild = client.get_guild(GUILD_ID)
            role_id = 778897396317814865  # Debug role
            role = guild.get_role(role_id)
            for member in bot_vc.members:
                if role in member.roles:
                    await member.edit(deafen=False)
            # 音声を再生する。
            player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
        else:
            print('Already playing on VC.')

        # 月曜日
        if weekday == 0:
            await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="月", time="TEST"))
        # 火曜日
        if weekday == 1:
            await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE.format(role="776685230748729344", weekday="火", time="TEST"))
        # 水曜日
        if weekday == 2:
            await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE.format(role="776685706415177748", weekday="水", time="TEST"))
        # 木曜日
        if weekday == 3:
            await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE.format(role="776685777597890570", weekday="木", time="TEST"))
        # 金曜日
        if weekday == 4:
            await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE.format(role="776685877371863090", weekday="金", time="TEST"))
#template.format("", "", "TEST")
    if message.content == '!stop':
        voice.stop()
        await client.get_channel(DEV_CHANNEL_TEXT).send(STOPPED)

    if message.content == '!disconnect':
        voice.disconnect()
        await client.get_channel(DEV_CHANNEL_TEXT).send(DISCONNECTED)

    if message.content == '!deafen on':  # テスト用: 全員をスピーカーミュートする。
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
            bot_vc = client.get_channel(CHANNEL_VOICE)
        for member in bot_vc.members:
            await member.edit(deafen=True)

    if message.content == '!deafen off':  # テスト用: 全員のスピーカーミュートを解除する。
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        bot_vc = client.get_channel(CHANNEL_VOICE)
        for member in bot_vc.members:
            await member.edit(deafen=False)

    if message.content == '!template':  # テスト用: テンプレートを表示する。
        await client.get_channel(DEV_CHANNEL_TEXT).send(TEMPLATE)


@tasks.loop(seconds=60)
async def loop():
    global voice, player
    weekday = datetime.now().weekday()
    now = datetime.now().strftime('%H:%M')
    if now == '09:00':
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        # 月曜日
        if weekday == 0:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685010110513152
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="月", time="1"))
        # 火曜日
        if weekday == 1:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685230748729344
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="火", time="1"))
        # 水曜日
        if weekday == 2:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685706415177748
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="水", time="1"))
        # 木曜日
        if weekday == 3:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685777597890570
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="木", time="1"))
        # 金曜日
        if weekday == 4:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685877371863090
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685010110513152", weekday="金", time="1"))
    if now == '10:40':
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        # 月曜日
        if weekday == 0:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685103203483657
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685103203483657", weekday="月", time="2"))
        # 火曜日
        if weekday == 1:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685270154084362
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685270154084362", weekday="火", time="2"))
        # 水曜日
        if weekday == 2:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685729551876126
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685729551876126", weekday="水", time="2"))
        # 木曜日
        if weekday == 3:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685834472652850
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685834472652850", weekday="木", time="2"))
        # 金曜日
        if weekday == 4:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685909868412938
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685909868412938", weekday="金", time="2"))
    if now == '13:00':
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        # 月曜日
        if weekday == 0:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685163769626645
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685163769626645", weekday="月", time="3"))
        # 火曜日
        if weekday == 1:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685649473962059
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685649473962059", weekday="火", time="3"))
        # 水曜日
        if weekday == 2:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685741249527850
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685741249527850", weekday="水", time="3"))
        # 木曜日
        if weekday == 3:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685844853162005
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685844853162005", weekday="木", time="3"))
        # 金曜日
        if weekday == 4:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685918543151175
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685918543151175", weekday="金", time="3"))
    if now == '14:40':
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        # 月曜日
        if weekday == 0:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685183939641375
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685183939641375", weekday="月", time="4"))
        # 火曜日
        if weekday == 1:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685653303754762
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685653303754762", weekday="火", time="4"))
        # 水曜日
        if weekday == 2:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685753106432012
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685753106432012", weekday="水", time="4"))
        # 木曜日
        if weekday == 3:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685854030037002
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685854030037002", weekday="木", time="4"))
        # 金曜日
        if weekday == 4:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685928583790623
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685928583790623", weekday="金", time="4"))
    if now == '16:20':
        # ボイスチャンネルに参加
        if voice is None:  # もし参加していなかったら？
            voice = await client.get_channel(CHANNEL_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        # 月曜日
        if weekday == 0:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685208967577631
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send('<@&> 曜日 5限 の開始時刻です。出席確認をしてください。')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685208967577631", weekday="月", time="5"))
        # 火曜日
        if weekday == 1:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685694272929837
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send('<@&> 曜日 5限 の開始時刻です。出席確認をしてください。')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685694272929837", weekday="火", time="5"))
        # 水曜日
        if weekday == 2:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685765299404800
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send('<@&> 曜日 5限 の開始時刻です。出席確認をしてください。')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685765299404800", weekday="水", time="5"))
        # 木曜日
        if weekday == 3:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685863358300161
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send('<@&> 曜日 5限 の開始時刻です。出席確認をしてください。')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685863358300161", weekday="木", time="5"))
        # 金曜日
        if weekday == 4:
            if player is None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(CHANNEL_VOICE)
                for member in bot_vc.members:
                    await member.edit(deafen=True)
                # 特定のロールのみミュート解除する。
                guild = client.get_guild(GUILD_ID)
                role_id = 776685937312137236
                role = guild.get_role(role_id)
                for member in bot_vc.members:
                    if role in member.roles:
                        await member.edit(deafen=False)
                # 音声を再生する。
                player = voice.play(discord.FFmpegPCMAudio(AUDIO_PATH))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL_TEXT).send('<@&> 曜日 5限 の開始時刻です。出席確認をしてください。')
            await client.get_channel(CHANNEL_TEXT).send(TEMPLATE.format(role="776685937312137236", weekday="金", time="5"))


# ループ開始
loop.start()

client.run(TOKEN)
