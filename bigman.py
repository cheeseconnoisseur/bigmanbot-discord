import discord
import asyncio
import random
from random import randint
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
import json
import sys


print("hi")
Client = discord.Client()
client = commands.Bot(command_prefix = "?")

global attid

def extractyboi(data, typee):
    if typee == "solo":
        typeee = "p2"
    elif typee == "duo":
        typeee = "p10"
    elif typee == "squads":
        typeee = "p9"

    smallerdata = data["stats"][typeee]

    rating = smallerdata["trnRating"]["value"]
    score = smallerdata["score"]["value"]
    wins = smallerdata["top1"]["value"]
    kdr = smallerdata["kd"]["value"]
    kills = smallerdata["kills"]["value"]
    matches = smallerdata["matches"]["value"]

    return(rating,score,wins,kdr,kills,matches)

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(game=discord.Game(name='your mum'))


@client.event
async def on_message(message):
    if message.content.upper().startswith('!HELP'):
        UserID = message.author.id
        print(UserID)
        await client.send_message(message.channel,"<@{}> commands are:\n!farth\n!gay\n!help\nuganda\n!insult (name)\n if you mention uganda at any time\n!say\n!tube (link)\n!logan\n Fortnite Stuff :\n!f (platform) (name) \n!c (unlimited names , space between each name)".format(UserID))
    if message.author.id == '185465039040282624':
        bigint = random.uniform(0.0,math.pi)
        if bigint < 1:
            await client.send_message(message.channel,"fallacy")

    if message.content.upper().startswith('!GAY'):
        UserID = message.author.id

    if message.content.upper().startswith('!FOUTTAHERE'):
        await client.send_message(message.channel,'bye bitches')
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
        ww = randint(1,11)
        #ww = ww / 10
        hh = randint(1,11)
        #hh = hh / 10
        hhh = hh + hh
        www = ww + ww
        offsetw = int((img_h - img2_h) / www)
        offseth = int((img_h - img2_h) / hhh)

        img.paste(img2, (offsetw, offseth), img2)
        img.save('meme1.png')
        await client.send_file(message.channel, "meme1.png")
        os.remove("meme1.png")


    if message.author.id == '135410033524604928':
        randyems = randint(0,3)
        if randyems in (2, 3):
            yemsint = randint(0,10)
            if yemsint == 0:
                await client.send_message(message.channel,"shut up youre literally five just why just litearrly stfu")
            if yemsint == 1:
                await client.send_message(message.channel,"turn around yup turn around")
            if yemsint == 2:
                await client.send_message(message.channel,"bro i can barely even see you be quiet")
            if yemsint == 3:
                await client.send_message(message.channel,"acctually the straw that broke alfonse man just go play overwatch")
            if yemsint == 4:
                await client.send_message(message.channel,"YEeeeEEEEeeeems")
            if yemsint == 5:
                await client.send_message(message.channel,"bro is this kid still talking ^^^")
            if yemsint == 6:
                await client.send_message(message.channel,"okay yems lets just sit down mkay? just a quick lik chat")
            if yemsint == 7:
                await client.send_message(message.channel,"and you think because youre in the gang de gucci that you cool or somin just stfu")
            if yemsint == 8:
                await client.send_message(message.channel,"*facepalm*")
            if yemsint == 9:
                await client.send_message(message.channel,"https://www.wikihow.com/Leave-a-Discord-Server-on-a-PC-or-Mac")
            if yemsint == 10:
                await client.send_message(message.channel,"im acc stealing all your street cred")






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


    if message.content.upper().startswith('!C'):
        UserID = message.author.id
        args = message.content.split(" ")

        lentil = len(args)
        lentil = lentil - 1
        for i in range(lentil):
            name = args[i + 1]
            print(name)
            header = {"TRN-Api-Key": "fortntietracker api key"}
            url = "https://api.fortnitetracker.com/v1/profile/pc/" + name
            r = requests.get(url, headers= header)
            data = json.loads(r.text)
            rating,score,wins,kdr,kills,matches = extractyboi(data, "solo")
            drating,dscore,dwins,dkdr,dkills,dmatches = extractyboi(data, "duo")
            srating,sscore,swins,skdr,skills, smatches = extractyboi(data, "squads")
            overallkills = int(kills) + int(dkills) + int(skills)
            overallwins = int(wins) + int(dwins) + int(swins)
            overallmatches = int(matches) + int(dmatches) + int(smatches)
            #overallkd = (float(kdr) + float(dkdr) + float(skdr)) / 3
            overallkd = overallkills/(overallmatches - overallwins)
            overallkd = float("{0:.3f}".format(overallkd))
            await client.send_message(message.channel,"__**OVERALL for {}:**__\n overall kills: {} \n overall wins: {} \n overall kdr: {} \n overall matches: {}".format(name, overallkills, overallwins, overallkd, overallmatches))




    if message.content.upper().startswith('!F'):
        UserID = message.author.id
        args = message.content.split(" ")
        maybename = args[1]
        if maybename == "pc":
            typee = "pc"
            name = args[2]
        elif maybename == "ps4":
            typee = "psn"
            name = args[2]
        elif maybename == "xbox":
            typee = "xbl"
            name = args[2]
        else:
            typee = "pc"
            name = maybename

        header = {"TRN-Api-Key": "fortntietracker api key"}
        url = "https://api.fortnitetracker.com/v1/profile/" + typee + "/" + name
        r = requests.get(url, headers= header)
        data = json.loads(r.text)
        rating,score,wins,kdr,kills,matches = extractyboi(data, "solo")
        drating,dscore,dwins,dkdr,dkills,dmatches = extractyboi(data, "duo")
        srating,sscore,swins,skdr,skills, smatches = extractyboi(data, "squads")
        await client.send_message(message.channel,"<@{}>\n__**{}'s stats**__\n **SOLO:**\n solo kills: {} \n solo wins: {} \n solo kdr: {}\n solo matches: {} ".format(UserID, name, kills, wins, kdr , matches))
        await client.send_message(message.channel,"**DUOS:**\n duo kills: {} \n duo wins: {} \n duo kdr: {}\n duo matches: {} ".format(dkills,dwins,dkdr, dmatches))
        await client.send_message(message.channel,"**SQUADS:**\n squads kills: {} \n squads wins: {} \n squads kdr: {}\n squad matches: {}  ".format(skills, swins, skdr, smatches))
        overallkills = int(kills) + int(dkills) + int(skills)
        overallwins = int(wins) + int(dwins) + int(swins)
        overallmatches = int(matches) + int(dmatches) + int(smatches)
        #overallkd = (float(kdr) + float(dkdr) + float(skdr)) / 3
        overallkd = overallkills/(overallmatches - overallwins)
        overallkd = float("{0:.3f}".format(overallkd))
        await client.send_message(message.channel,"***OVERALL***:\n overall kills: {} \n overall wins: {} \n overall kdr: {} \n overall matches: {}".format(overallkills, overallwins, overallkd, overallmatches))


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
        await client.send_message(message.author, "I now you are but what am I:joy:")
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

    if message.content.upper().startswith('!SAY ') and message.author.id != '402062055303151627':
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))

    if message.content.upper().startswith('!DSAY ') and message.author.id != '402062055303151627':
        args = message.content.split(" ")
        await client.send_message(message.channel, "{}".format(" ".join(args[1:])))
        await client.delete_message(message)



client.run('token', reconnect=True)
