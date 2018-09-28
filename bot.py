import discord
import random
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import more_itertools.locate as mit

bot = commands.Bot(command_prefix = '!')

@bot.event
async def onready():
    print ("Dictator-san ready for action!")
    await bot.say("I'm here kids!")

@bot.event
async def on_message(message):
    # Ping command
    if message.content.startswith('!ping'):
        userID = message.author.id
        await bot.send_message(message.channel, "<@%s> Pong!" % (userID))
    elif message.content.startswith("!pin"):
        pin_message(message.content)

    # Poll system
    if message.content.startswith("!poll"):
        userID = message.author.id
        if message.content != "!poll " + int + String: #need quotation marks
            await bot.send_message(message.channel, "<@%s> Please make your poll request in this format: \n !poll + amount of choices + \"title\"" % (userID))
        else:
            number = 
            title = findTitle(message)
            counter = 1
            choices = []
            # Asks for choices and puts them into array
            while number >= counter:
                if counter % 10 == 1 and counter % 100 != 11:
                    await bot.send_message(message.channel, "What is the title of the " + counter + "st choice?")
                if counter % 10 == 2 and counter % 100 != 12:
                    await bot.send_message(message.channel, "What is the title of the " + counter + "nd choice?")
                if counter % 10 == 3 and counter % 100 != 13:
                    await bot.send_message(message.channel, "What is the title of the " + counter + "rd choice?")
                else:
                    await bot.send_message(message.channel, "What is the title of the " + counter + "th choice?")
                choices.append(userID.nextmessage)
                counter++
            
            await bot.say(embed = embed)

def findTitle(message):
    newlist = list(mit.locate(message, lambda x: x == "\""))
    first = newlist[0]
    last = newlist[newlist.count -  1]
    return message.substring(first + 1, last)


bot.run("")