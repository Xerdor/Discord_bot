import discord

from discord import Client
from discord import Message

voice_channels = []

async def join(message: Message, client: Client):

    found_member = False

    if client.is_voice_connected(message.server) is True:
        print("Replace with fail safe.")
    else:
        for channel in message.server.channels:
            if channel.type == discord.ChannelType.voice:
                if message.author in channel.voice_members:

                    voice_channels.append( await client.join_voice_channel(channel))
                    player = voice_channels[0].create_ytdl_player('https://www.youtube.com/watch?v=C9yO0k_QauY')
                    player.start()
                    found_member = True
                    break

        if found_member:
            voice_channels[0]
        else:
            return message.author.mention + " not in a channel"



async def leave(message: Message, client: Client):
    vc = client.voice_client_in(message.server)
    if vc is not None:
        await vc.disconnect()
