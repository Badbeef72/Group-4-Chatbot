import discord
import random
import requests
import store
import nltk
from nltk import *
nltk.download('punkt')
from py_edamam import  *


token = 'NjMyMzE4MzgwMTI4NjAwMDg0.XbsuHQ.DPmI7HqIVo8EqnO_EdCa-Y_4T3A'
client = discord.Client()

@client.event
async def on_message(message):
    messageLowered = message.content.lower()
    tokenized_word = word_tokenize(messageLowered)
    print(tokenized_word)
    if message.author == client.user:
        return
    if any(item in store.detectable_greetings for item in tokenized_word):
        await message.channel.send('Hello {0.author.mention}! '.format(message) + random.choice(store.list_of_greetings))
        msg = str(await client.wait_for('message'.lower()))
        tokenized_word = word_tokenize(msg)
        print(tokenized_word)
    if any(item in store.meal_prep_keywords for item in tokenized_word):
        await message.channel.send('I can help you to prepare a meal')
        msg = str(await client.wait_for('message'.lower()))
        tokenized_word = word_tokenize(msg)
        print(tokenized_word)
    if "breakfast" and "" in tokenized_word:
        await message.channel.send("I will create a breakfast  meal for you")
    if "lunch" in tokenized_word:
        await message.channel.send("I will create a lunch meal for you")
    if "dinner" in tokenized_word:
        await message.channel.send("I will create a dinner meal for you")


@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(token)
