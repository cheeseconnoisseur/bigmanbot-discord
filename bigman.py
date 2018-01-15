import discord
import asyncio
import random
import pickle
import os
from discord.ext import commands
from discord.ext.commands import bot
import datetime
from calendarrr import maincal
MYDIR = os.path.dirname(__file__)

print("hi")
Client = discord.Client()
client = commands.Bot(command_prefix = "?")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='your mum'))
    print("bot is ready")

@client.event
async def on_message(message):
    if message.content.startswith('!help'):
        UserID = message.author.id
        print(UserID)
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda".format(UserID))
    if message.author.id == '185465039040282624':
        await client.send_message(message.channel,"fallacy")

    if message.content.startswith('!gay'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}>".format(UserID))
    if message.content.startswith('!nextcal'):
        UserID = message.author.id
        maincal(1)
        kay = []
        with open('temp.txt','r') as f:
            kay = f.read()
            kay = kay.split("\n")
            f.close()
            os.remove('temp.txt')
            print(kay)
            event = str(kay[0])
            await client.send_message(message.channel,"<@{}> next event {}".format(UserID, event))
    if message.content.startswith('!farth'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}> shut up you rabient homosexual".format(UserID))
    if message.content == 'gay':
        await client.send_message(message.channel, ":joy:")
    if message.content == 'uganda':
        bigint = random.randint(1,16)
        bigint = str(bigint)
        bigname = MYDIR + "\\imgsugan\meme" + bigint + ".jpg"
        try:
            await client.send_file(message.channel, bigname)
        except:
            bigname = bigname.replace(".jpg", ".png")
            await client.send_file(message.channel, bigname)

    if message.content.startswith('!saygay'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))

    if message.content.startswith('!cal'):
        UserID = message.author.id
        if UserID == '310469854564057088':
            args = message.content.split(" ")
            args = int(args[1])
            maincal(args)
            kay = []
            with open('temp.txt','r') as f:
                kay = f.read()
                kay = kay.split("\n")
                f.close()
                os.remove('temp.txt')
                print(kay)
            for event in reversed(kay[:-1]):
                print(kay)
                event = str(event)
                await client.send_message(message.channel,"<@{}> next event {}".format(UserID, event))
        else:
            await client.send_message(message.channel,"<@{}> and who the hell are you snooping in my calander".format(UserID))



client.run('NDAyMDYyMDU1MzAzMTUxNjI3.DT0DCQ.a6qW0wFIVqRDRluoXALaZb8oYL4', reconnect=True)
