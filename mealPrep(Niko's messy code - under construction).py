import discord
import random
import requests
import store
import nltk
from nltk import *


token = 'NjMyMzE4MzgwMTI4NjAwMDg0.Xbg_vw.fC5ZxaDY2T7DJhinEOULLnSoq00'
client = discord.Client()

@client.event
async def on_message(message):
    messageLowered = message.content.lower()
    tokenized_word = word_tokenize(messageLowered)
    print(tokenized_word)
    if message.author == client.user:
        return
    elif any(item in store.detectable_greetings for item in tokenized_word):
        await message.channel.send('Hello {0.author.mention}! '.format(message) + random.choice(store.list_of_greetings))
        msg = await client.wait_for('message'.lower())
        tokenized_word = word_tokenize(msg)
        print(tokenized_word)
        if any(item in store.meal_prep_keywords for item in tokenized_word):
            await message.channel.send('I can help you to prepare a meal')
            msg = await client.wait_for('message'.lower())
            tokenized_word = word_tokenize(msg)
            print(tokenized_word)
            if "lunch" in tokenized_word:
                await message.channel.send("I can give you a meal for lunch")


@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(token)
