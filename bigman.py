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
import time
from pytube import YouTube
from PIL import Image

print("hi")
Client = discord.Client()
client = commands.Bot(command_prefix = "?")

global attid


@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(game=discord.Game(name='your mum'))


@client.event
async def on_message(message):
    if message.content.upper().startswith('!HELP'):
        UserID = message.author.id
        print(UserID)
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda\n!insult (name)\n if you mention uganda at any time\n!say\n!tube (link)\n!logan".format(UserID))
    if message.author.id == '185465039040282624':
        bigint = random.uniform(0.0,math.pi)
        if bigint < 1:
            await client.send_message(message.channel,"fallacy")

    if message.content.upper().startswith('!GAY'):
        UserID = message.author.id

    if message.content.upper().startswith('!FOUTTAHERE'):
        Client.close()


    try:
        if message.attachments[0]:
            attid = message.id
            with open("oetg.txt", "w") as f:
                f.write(message.id)
    except:
        joe = 1

    if message.content.upper().startswith('!YEMS'):
        #try:
        #    global attid
        #except:
            #joe = 1
        try:
            with open("oetg.txt", "r") as f:
                mmmh = f.read()
        except:
            joe = 1


        msg = await client.get_message(message.channel, mmmh)
        await client.send_message(message.channel,"memefying in process")
        url = msg.attachments[0]
        url = url['proxy_url']
        bigstring = url
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(bigstring, "meme1.png")

        img = Image.open('meme1.png', 'r')
        img_w, img_h = img.size
        img2 = Image.open('yems.png', 'r')
        img2_w, img2_h = img2.size
        offsetw = int((img_h - img2_h) / 2)
        offseth = int((img_h - img2_h) / 2)

        img.paste(img2, (offsetw, offseth), img2)
        img.save('meme1.png')
        await client.send_file(message.channel, "meme1.png")
        os.remove("meme1.png")


    #if message.author.id == '310469854564057088':






    #    with open("lyrics.txt", "r") as f:
    ##    UserID = message.author.id
    #    for i in range(200):
        #    time.sleep(3)
            #await client.change_presence(game=discord.Game(name= 'lol{}'.format(i)))







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
    if message.content.upper().startswith('!LOGAN'):
        bigstring = 'https://raw.githubusercontent.com/cheeseconnoisseur/bigmanbot-discord/master/lp.png'
        urllib.request.urlretrieve(bigstring, "logan.png")
        await client.send_file(message.channel, "logan.png")
        os.remove('logan.png')
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

    if message.content.upper().startswith('!SAY ') and not message.content.upper().startswith('!SAY !SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))



client.run('NDAyMDYyMDU1MzAzMTUxNjI3.DUY1OA.qgF-TBc9-f6tR__z3cIjFqTjvak', reconnect=True)
