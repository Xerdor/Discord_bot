import os

import discord
import asyncio

import time
from discord.message import Message

client = discord.Client()

pits = []


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    discord.opus.load_opus("C:\\Users\\kevin\\Desktop\\opusfile-0.7-win32\\libopus-0")
    if os.path.isfile('pitslist'):
        with open('pitslist', 'r') as pitlistfile:
            for line in pitlistfile:
                pits.append((line[:-1]))

    print("list of pits")
    for x in pits:
        print(x)

    print(discord.opus.is_loaded())


@client.event
async def on_message(message: Message):

    if message.author == client.user:
        return

    if message.channel.id in pits:
        time.sleep(2)
        await client.delete_message(message)
        return

    if message.content.startswith("!register-pit"):
        with open('pitslist', 'a') as pitlistfile:
            pitlistfile.write(str(message.channel.id)+"\n")
            pits.append(message.channel.id)
            print("adding pit:" + message.channel.id)

    if message.content.startswith("!echo"):
        await client.send_message(message.channel, "@everyone " + message.author.name + " heeft iets gezegd.")

    if message.content.startswith("!join"):
        voicechannels = []

        for channel in message.server.channels:
            if channel.type == discord.ChannelType.voice:
                if message.author in channel.voice_members:
                    voicechannels.append( await client.join_voice_channel(channel))
                    break

        voicechannels[0]

with open('token', 'r') as token:

    tokenstr = token.read()
client.run(tokenstr)
