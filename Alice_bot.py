import json
import traceback
import discord

import Alice_commands

from discord.message import Message

client = discord.Client()

with open('config', 'r') as configfile:
    config = json.load(configfile)

opus_location = config["opus_location"]
command_tag = ";;"


@client.event
async def on_ready():
    # Login information
    print("Logged in as: " + client.user.name)
    print("With user ID: " + client.user.id)

    # Start Opus
    discord.opus.load_opus(opus_location)
    # Check if Opus has been loaded properly
    print(discord.opus.is_loaded())


@client.event
async def on_message(message: Message):

    if message.author == client.user:
        return

    if not message.content.startswith(command_tag):
        return

    message.content = message.content[len(command_tag):]
    command = message.content.split()[0]
    message.content = message.content[len(command) + 1:]
    try:
        method_result = await getattr(Alice_commands, command)(message, client)
    except:
        method_result = "Command unknown" + "\n" + command
        print(traceback.format_exc())

    if method_result is not None:
        await client.send_message(destination=message.channel, content=method_result)

with open('token', 'r') as token:

    token_string = str(token.read())[:-1]
client.run(token_string)
