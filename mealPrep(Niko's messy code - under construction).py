import discord
import random
import requests
import store
import py_edamam
from py_edamam import PyEdamam #Credit:https://github.com/JarbasAl/py_edamam and https://www.edamam.com/"
import nltk
import json
from nltk import *
nltk.download('punkt')

r = requests.get('https://api.edamam.com/search?app_id=${f66d3fcf}&app_key=${f4f09a804c47eac41b04d4b0bc6acb08')
print(r.status_code)
print(r.text)
print(r.peek)

token = 'NjMyMzE4MzgwMTI4NjAwMDg0.Xb9O7g.oz1dRI8uGJtFkMsDwgBPCdDM0a0'
client = discord.Client()
e = PyEdamam(
            recipes_appid='f66d3fcf',
            recipes_appkey='f4f09a804c47eac41b04d4b0bc6acb08')

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
    if "breakfast" in tokenized_word:
        await message.channel.send("I will create a breakfast  meal for you")
        for recipe in e.search_recipe("breakfast") :
            await message.channel.send("The recipe that you requested: " + str(recipe))
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories")
            await message.channel.send(recipe.url)
            break
    if "lunch" in tokenized_word:
        await message.channel.send("I will create a lunch meal for you")
        for recipe in e.search_recipe("lunch"):
            await message.channel.send("The recipe that you requested: " + str(recipe))
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories")
            await message.channel.send(recipe.url)
            break
    if "dinner" in tokenized_word:
        await message.channel.send("I will create a dinner meal for you")
        for recipe in e.search_recipe("dinner"):
            await message.channel.send("The recipe that you requested: " + str(recipe))
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories")
            await message.channel.send(recipe.url)
            break


@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(token)
