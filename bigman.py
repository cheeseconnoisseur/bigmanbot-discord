import discord
import asyncio
import random
import pickle
import os
#from check import checker
from discord.ext import commands
from discord.ext.commands import bot
import datetime
import urllib.request
import requests
import urllib
import yaml
import json
import math
from pytube import YouTube

print("hi")
Client = discord.Client()
client = commands.Bot(command_prefix = "?")


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='your mum'))
    print("bot is ready")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!HELP'):
        UserID = message.author.id
        print(UserID)
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda\n!insult (name)\n if you mention uganda at any time\n!say".format(UserID))
    if message.author.id == '185465039040282624':
        bigint = random.uniform(0.0,math.pi)
        if bigint < 1:
            await client.send_message(message.channel,"fallacy")

    if message.content.upper().startswith('!GAY'):
        UserID = message.author.id




    if message.content.upper().startswith('!TUBE'):
        error = 0
        UserID = message.author.id
        args = message.content.split(" ")
        args = args[1]
        yt = YouTube(args)
        await client.send_message(message.channel,"<@{}> warning this is in beta".format(UserID))
        title = yt.title
        stream = yt.streams.first()
        await client.send_message(message.channel,"<@{}> downloading".format(UserID))
        stream.download()
        oldtitle = title
        await client.send_message(message.channel,"<@{}> uploading".format(UserID))
        try:
            title = title.replace(".","")
            title = title + ".mp4"
            title = title.replace(":","")
            title = title.replace(",","")
            title = title.replace("?","")
            await client.send_file(message.channel, title)
        except:
            error = error + 1
            print("lolno")
        try:
            oldtitle = oldtitle + ".webm"
            oldtitle = oldtitle.replace(":","")
            oldtitle = oldtitle.replace("?","")
            await client.send_file(message.channel, oldtitle)

        except:
            error = error + 1
            print("lolno")

        if error == 2:
            await client.send_message(message.channel,"<@{}> FATAL error has occured video probably too large , max file size: 8mb, discords limit not mine".format(UserID))

        try:
            os.remove(title)
        except:
            print("no1")
        try:
            os.remove(oldtitle)
        except:
            print("no2")

        print("lol")





    if message.content.upper().startswith('!INSULT'):
        args = message.content.split(" ")
        args = args[1]
        urllib.request.urlretrieve("https://raw.githubusercontent.com/cheeseconnoisseur/bigmanbot-discord/master/insults.yml", "insults.yml")
        #urllib.request.urlretrieve("https://raw.githubusercontent.com/cheeseconnoisseur/bigmanbot-discord/master/insults.yml")
        yamfile = yaml.load(open('insults.yml'))
        pref = 'Thou'
        col1 = random.choice(yamfile['column1'])
        col2 = random.choice(yamfile['column2'])
        col3 = random.choice(yamfile['column3'])
        insultmessage = pref + ' ' + col1 + ' ' + col2 + ' ' + col3 + '.'
        await client.send_message(message.channel,args + insultmessage)
        os.remove('insults.yml')

    if message.content.upper().startswith('!FARTH'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}> shut up you rabient homosexual".format(UserID))
    if message.content.upper() == 'GAY':
        await client.send_message(message.channel, ":joy:")
    if 'UGANDA' in message.content.upper() and not message.content.upper().startswith('UGANDA'):
        await client.send_message(message.channel, "you speak of the holy lands")
    if message.content.upper() == 'UGANDA':
        bigint = random.randint(1,16)
        bigint = str(bigint)
        try:
            bigstring = 'https://raw.githubusercontent.com/cheeseconnoisseur/bigmanbot-discord/master/imgsugan/meme' + bigint + '.jpg'
            urllib.request.urlretrieve(bigstring, "meme1.jpg")
        except:
            bigstring = 'https://raw.githubusercontent.com/cheeseconnoisseur/bigmanbot-discord/master/imgsugan/meme' + bigint + '.png'
            urllib.request.urlretrieve(bigstring, "meme1.png")
        try:
            await client.send_file(message.channel, "meme1.jpg")
            os.remove('meme1.jpg')
        except:
            await client.send_file(message.channel, "meme1.png")
            os.remove('meme1.png')

    if message.content.upper().startswith('!SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))



client.run('NDAyMDYyMDU1MzAzMTUxNjI3.DT0DCQ.a6qW0wFIVqRDRluoXALaZb8oYL4', reconnect=True)
