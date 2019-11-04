#My version of the bot redone into functions to make it easier to use and implement other things

import discord
import random
import store
import bmi
import languageProcessing


#TOKEN = 'NjQwNjg2MzE0ODI3Njc3NzE2.Xb911A.w8WubCbIOkcvJzxkpcT_IdlurCo'
client = discord.Client()


#@client.event
#async def onMessage(message):
    #if message.author == client.user:
        #return
    #else:
        #BeginConversation(message)

#def BeginConversation(UserMessage):
    #filteredMessage = languageProcessing.sentenceFilter(UserMessage.content.lower())



@client.event
async def startUp():
    print("Connected as: " + client.user.name + "(" + client.user.id + ")")
    #detectableGreetings = languageProcessing.synonymListMaker(store.detectable_greetings)
    #detectablePositives = languageProcessing.synonymListMaker(store.detectable_positives)
    #detectableNegatives = languageProcessing.synonymListMaker(store.detectable_negatives) + languageProcessing.antonymListMaker(store.detectable_positives)
    #channel = client.get_channel(640678051666984963)
    #await channel.send('Online and ready to chat.')

client.run("NjQwNjg2MzE0ODI3Njc3NzE2.Xb911A.w8WubCbIOkcvJzxkpcT_IdlurCo")
