# coding: utf-8

# import
import discord
from discord.utils import get
from discord.ext import tasks
from datetime import datetime
import os

client = discord.Client()
CHANNEL = 776686999851630613
TOKEN = os.getenv('TOKEN')
DEV_CHANNEL = 777780662013919283
ALARM_VOICE = 777780340864712734
GUILD_ID = 776684934952779786
voice = None
player = None


# 起動通知
@client.event
async def on_ready():
    print("ボットを起動しました。discord.py バージョン", discord.__version__)
    await client.change_presence(activity=discord.Game(name="起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ起きろ"))


@client.event
async def on_message(message):
    weekday = datetime.now().weekday()
    global voice, player
    if message.content == '!debug':
        # ボイスチャンネルに参加、音声を再生
        if voice == None:  # もし参加していなかったら？
            voice = await client.get_channel(ALARM_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        if player == None:  # もし何も再生されていなかったら？
            # 全員に音声が流れるのを防ぐ
            # 一旦、全員をスピーカーミュートする。
            bot_vc = client.get_channel(ALARM_VOICE)
            for member in bot_vc.members:
                await member.edit(deafen=True)
            # 特定のロールのみミュート解除する。
            guild = client.get_guild(GUILD_ID)
            role_id = 778841949279879188  # Debug role
            role = guild.get_role(role_id)
            for member in bot_vc.members:
                if role in member.roles:
                    await member.edit(deafen=False)
            # 音声を再生する。
            player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
        else:
            print('Already playing on VC.')

        # 月曜日
        if weekday == 0:
            print("<@&776685010110513152> 月曜日 限 の開始時刻です。出席確認をしてください。")
            await client.get_channel(DEV_CHANNEL).send('<@&776685010110513152> 月曜日 限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            print("<@&776685230748729344> 火曜日 限 の開始時刻です。出席確認をしてください。")
            await client.get_channel(DEV_CHANNEL).send('<@&776685230748729344> 火曜日 限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            print("<@&776685706415177748> 水曜日 限 の開始時刻です。出席確認をしてください。")
            await client.get_channel(DEV_CHANNEL).send('<@&776685706415177748> 水曜日 限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            print("<@&776685777597890570> 木曜日 限 の開始時刻です。出席確認をしてください。")
            await client.get_channel(DEV_CHANNEL).send('<@&776685777597890570> 木曜日 限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            print("<@&776685877371863090> 金曜日 限 の開始時刻です。出席確認をしてください。")
            await client.get_channel(DEV_CHANNEL).send('<@&776685877371863090> 金曜日 限 の開始時刻です。出席確認をしてください。')

    if message.content == '!stop':
        voice.stop()

    if message.content == '!disconnect':
        voice.disconnect()

    if message.content == '!deafen on':
        # ボイスチャンネルに参加
        if voice == None:  # もし参加していなかったら？
            voice = await client.get_channel(ALARM_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
            bot_vc = client.get_channel(ALARM_VOICE)
        for member in bot_vc.members:
            await member.edit(deafen=True)

    if message.content == '!deafen off':
        # ボイスチャンネルに参加
        if voice == None:  # もし参加していなかったら？
            voice = await client.get_channel(ALARM_VOICE).connect(reconnect=True)
        else:
            print('Already connected to the VC.')
        bot_vc = client.get_channel(ALARM_VOICE)
        for member in bot_vc.members:
            await member.edit(deafen=False)


@tasks.loop(seconds=60)
async def loop():
    global voice, player
    weekday = datetime.now().weekday()
    now = datetime.now().strftime('%H:%M')
    if now == '09:00':
        # 月曜日
        if weekday == 0:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685010110513152> 月曜日 1限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685230748729344> 火曜日 1限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685706415177748> 水曜日 1限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685777597890570> 木曜日 1限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685877371863090> 金曜日 1限 の開始時刻です。出席確認をしてください。')
    if now == '10:40':
        # 月曜日
        if weekday == 0:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685103203483657> 月曜日 2限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685270154084362> 火曜日 2限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685729551876126> 水曜日 2限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685834472652850> 木曜日 2限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685909868412938> 金曜日 2限 の開始時刻です。出席確認をしてください。')
    if now == '13:00':
        # 月曜日
        if weekday == 0:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685163769626645> 月曜日 3限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685649473962059> 火曜日 3限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685741249527850> 水曜日 3限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685844853162005> 木曜日 3限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685918543151175> 金曜日 3限 の開始時刻です。出席確認をしてください。')
    if now == '14:40':
        # 月曜日
        if weekday == 0:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685183939641375> 月曜日 4限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685653303754762> 火曜日 4限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685753106432012> 水曜日 4限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685854030037002> 木曜日 4限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685928583790623> 金曜日 4限 の開始時刻です。出席確認をしてください。')
    if now == '16:20':
        # 月曜日
        if weekday == 0:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685208967577631> 月曜日 5限 の開始時刻です。出席確認をしてください。')
        # 火曜日
        if weekday == 1:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685694272929837> 火曜日 5限 の開始時刻です。出席確認をしてください。')
        # 水曜日
        if weekday == 2:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685765299404800> 水曜日 5限 の開始時刻です。出席確認をしてください。')
        # 木曜日
        if weekday == 3:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685863358300161> 木曜日 5限 の開始時刻です。出席確認をしてください。')
        # 金曜日
        if weekday == 4:
            if player == None:  # もし何も再生されていなかったら？
                # 全員に音声が流れるのを防ぐ
                # 一旦、全員をスピーカーミュートする。
                bot_vc = client.get_channel(ALARM_VOICE)
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
                player = voice.play(discord.FFmpegPCMAudio('audio.wav'))
            else:
                print('Already playing on VC.')
            await client.get_channel(CHANNEL).send('<@&776685937312137236> 金曜日 5限 の開始時刻です。出席確認をしてください。')


# ループ開始
loop.start()

client.run(TOKEN)
