#My version of the bot redone into functions to make it easier to use and implement other things

import discord
import random
import store
import bmi
import languageProcessing

client = discord.Client()
@client.event
async def on_message(userMessage):
    if userMessage.author == client.user:
        return
    else:
        await beginConversation(userMessage)

async def beginConversation(userMessage):
    filteredMessage = languageProcessing.sentenceFilter(userMessage.content.lower())
    if any(item in languageProcessing.synonymListMaker(store.detectable_greetings) for item in filteredMessage):
        await userMessage.channel.send('Hello {0.author.mention}! '.format(userMessage) + random.choice(store.list_of_greetings))
        userMessage = await client.wait_for('message')
        filteredMessage = languageProcessing.sentenceFilter(userMessage.content.lower())
        if any(item in languageProcessing.synonymListMaker(store.detectable_positives) for item in filteredMessage):
            await userMessage.channel.send(random.choice(store.list_of_goods) + ' Do you require my assistance?'.format(userMessage))
            userMessage = await client.wait_for('message')
            #filteredMessage = languageProcessing.sentenceFilter(userMessage.content.lower())
            #cant use filteredmessage until i add Lemmatization
            if any(item in store.detectable_yes for item in userMessage.content.lower().split()):
                await branchToTopics()
            else:
                await userMessage.channel.send('I will be here if you need me.'.format(userMessage))
                return
        elif any(item in languageProcessing.synonymListMaker(store.detectable_negatives) for item in filteredMessage):
            await userMessage.channel.send("That's a shame. Do you require my assistance?".format(userMessage))
            userMessage = await client.wait_for('message')
            if any(item in store.detectable_yes for item in userMessage.content.lower().split()):
                await branchToTopics()
            else:
                await userMessage.channel.send('I will be here if you need me.'.format(userMessage))
                return
    else:
        return

async def branchToTopics():
    channel = client.get_channel(640678051666984963)
    await channel.send("Anything in particular you need help with?")
    #weighting goes  here

@client.event
async def on_ready():
    print('Connected as: ' + client.user.name + '(' + str(client.user.id) + ')')
    channel = client.get_channel(640678051666984963)
    await channel.send('Online and ready to chat.')

client.run("NjQwNjg2MzE0ODI3Njc3NzE2.Xb911A.w8WubCbIOkcvJzxkpcT_IdlurCo")
