import discord
import random
import requests
import store
import nltk

from nltk import *


token = 'NjMyMzE4MzgwMTI4NjAwMDg0.Xa75vQ.dAaGjjiwD52A7qFas3MxLwe1CdI'

client = discord.Client()


@client.event
async def on_message(message): #if the user request a meal preparation
    tokenized_word = word_tokenize(message.content)
    print(tokenized_word)
    if message.author == client.user:
        return
    elif any(item in store.meal_prep_keywords for item in tokenized_word):
        await message.channel.send('I can help you with that. Are you planning to eat breakfast, lunch or dinner?')
        msg2 = await client.wait_for('message')
        msg2_tokenized = word_tokenize(msg2)
        print(msg2_tokenized)
        if "breakfast" in msg2_list:
            await message.channel.send('I will create a breakfast meal for you')
            msg_breakfast = await client.wait_for('message')
        elif "lunch" in msg2_list:
            await message.channel.send('I will create a lunch meal for you')
            msg_lunch = await client.wait_for('message')
        elif "dinner" in msg2_list:
            await message.channel.send('I will create a dinner meal for you')
            msg_dinner = await client.wait_for('message')
    else:
        await message.channel.send(random.choice(store.list_of_sorrys))





@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(token)
