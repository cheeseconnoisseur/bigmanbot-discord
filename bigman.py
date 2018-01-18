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
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda\n!insult (name)".format(UserID))
    if message.author.id == '185465039040282624':
        bigint = random.uniform(0.0,math.pi)
        if bigint > 1:
            await client.send_message(message.channel,"fallacy")

    if message.content.startswith('!gay'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}>".format(UserID))
    if message.content.startswith('!insult'):
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
        
    if message.content.startswith('!farth'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}> shut up you rabient homosexual".format(UserID))
    if message.content == 'gay':
        await client.send_message(message.channel, ":joy:")
    if message.content == 'uganda':
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

    if message.content.startswith('!saygay'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))



client.run('NDAyMDYyMDU1MzAzMTUxNjI3.DT0DCQ.a6qW0wFIVqRDRluoXALaZb8oYL4', reconnect=True)
