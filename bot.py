'''
    Tutorial from:
    https://www.devdungeon.com/content/make-discord-bot-python
'''
import discord # Imports the Discord API.
import random # Imports Python's "random" library.
import store # Imports the store.py file for lists of responses.

TOKEN = 'NjMyMzE4MzgwMTI4NjAwMDg0.XamuuA.KUfrcz_EhTFocY8C1eS7PSeOZu4' # Bot's unique ID.

client = discord.Client()

@client.event
async def on_message(message): # If the user sends a message, do something.
    message_list = message.content.lower() # Converts all of the message to lower-case, so that if capitals are used, the bot can detect the word anyway.
    message_list = message_list.split()
    print(message_list) # Prints the message to the command line for error handling.
    if message.author == client.user:
        return

    if any(item in store.detectable_greetings for item in message_list): # If user sends "hello", the bot will reply with "Hello (name of user)!" + A random greeting.
        await message.channel.send('Hello {0.author.mention}! '.format(message) + random.choice(store.list_of_greetings))

    elif "good" in message_list:
        await message.channel.send(random.choice(store.list_of_goods) + " Do you require my assistance?")

    else: # If anything else is said by the user, the bot outputs a random line describing "I don't know what you mean.".
        await message.channel.send(random.choice(store.list_of_sorrys))

@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
