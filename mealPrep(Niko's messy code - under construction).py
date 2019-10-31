import discord
import random
import requests
import store
import nltk
from nltk import *
nltk.download('punkt')


token = 'NjMyMzE4MzgwMTI4NjAwMDg0.XbsNhQ.3QSZjHfHY_170vijeFhzBmDZMZg'
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
        tokenized_word1 = word_tokenize(msg)
        print(tokenized_word1)
    if any(item in store.meal_prep_keywords for item in tokenized_word or tokenized_word1):
        await message.channel.send('I can help you to prepare a meal')
        msg1 = str(await client.wait_for('message'.lower()))
        tokenized_word2 = word_tokenize(msg1)
        print(tokenized_word2)
        if "lunch" in tokenized_word2:
            await message.channel.send("I can give you a meal for lunch")


@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(token)
