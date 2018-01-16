import discord
import asyncio
import random
import pickle
import os
from discord.ext import commands
from discord.ext.commands import bot
import datetime
import urllib.request
import urllib

def checker(message):
    if message.content.startswith('!help'):
        UserID = message.author.id
        print(UserID)
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda".format(UserID))
    if message.author.id == '185465039040282624':
        await client.send_message(message.channel,"fallacy")

    if message.content.startswith('!gay'):
        UserID = message.author.id
        await client.send_message(message.channel,"<@{}>".format(UserID))
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
