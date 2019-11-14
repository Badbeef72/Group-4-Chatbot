import discord # Discord is being used as the platform that the user will communicate with the chatbot. Sourse: https://discordapp.com/developers/docs/intro
import store
from py_edamam import PyEdamam # Credit:https://github.com/JarbasAl/py_edamam and https://www.edamam.com/"
import nltk
from nltk import *
nltk.download('punkt')

token = 'NjMyMzE4MzgwMTI4NjAwMDg0.XcyC7Q.dySvp_-xg3B-jNbhrxxKwCtDNdo' # Token required for the Discord in order to run
client = discord.Client()
e = PyEdamam(
            recipes_appid='f66d3fcf',
            recipes_appkey='f4f09a804c47eac41b04d4b0bc6acb08') # Id and key required for the Edamam API

@client.event
async def on_message(message):
    messageLowered = message.content.lower()
    tokenized_word = word_tokenize(messageLowered)
    print(tokenized_word)
    if message.author == client.user:
        return
    if any(item in store.meal_prep_keywords for item in tokenized_word):
        await message.channel.send('I can help you to prepare a meal')
        msg = str(await client.wait_for('message'.lower()))
        tokenized_word = word_tokenize(msg)
        print(tokenized_word)
    if "breakfast" in tokenized_word:
        await message.channel.send("What would you like to eat for breakfast?")
        msg = await client.wait_for('message')
        new_msg = str(msg.content.lower())
        # Start of modified code. Original source: https://github.com/JarbasAl/py_edamam/blob/master/example.py #
        for recipe in e.search_recipe(new_msg): # Users inputs determines the search of the recipe. Originally the input was already set, I changed so the input is being determined by the users request
            await message.channel.send("The recipe that you requested: " + str(recipe)) # Chatbot shows requested recipe to the user. I implimented it into the discord and changed the way that it is presented on the user by adding the text #
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories") # Chatbot shows calories rounded up to 2 decimal places and displays it to the user. The original code just showed the calories without rounding them at all.#
            await message.channel.send(recipe.url) # Chatbot shows URL for the recipe. I implimented it into the discord #
            break
    if "lunch" in tokenized_word:
        await message.channel.send("What would you like to eat for lunch?")
        msg = await client.wait_for('message')
        new_msg = str(msg.content.lower())
        for recipe in e.search_recipe(new_msg): # Users inputs determines the search of the recipe. Originally the input was already set, I changed so the input is being determined by the users request
            await message.channel.send("The recipe that you requested: " + str(recipe))   # Chatbot shows requested recipe to the user. I implimented it into the discord and changed the way that it is presented on the user by adding the text #
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories") # Chatbot shows requested recipe to the user. I implimented it into the discord and changed the way that it is presented on the user by adding the text #
            await message.channel.send(recipe.url) # Chatbot shows URL for the recipe. I implimented it into the discord #
            break
    if "dinner" in tokenized_word:
        await message.channel.send("What would you like to eat for dinner?")
        msg = await client.wait_for('message')
        new_msg = str(msg.content.lower())
        for recipe in e.search_recipe(new_msg):  # Users inputs determines the search of the recipe. Originally the input was already set, I changed so the input is being determined by the users request
            await message.channel.send("The recipe that you requested: " + str(recipe)) # Chatbot shows requested recipe to the user. I implimented it into the discord and changed the way that it is presented on the user by adding the text #
            await message.channel.send("This recipe has " + str(round(recipe.calories, 2)) + " calories") # Chatbot shows requested recipe to the user. I implimented it into the discord and changed the way that it is presented on the user by adding the text
            await message.channel.send(recipe.url) # Chatbot shows URL for the recipe. I implimented it into the discord
            break
    # End of modified code #

@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(token)
