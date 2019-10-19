# Main file for the bot.
'''
    Tutorial from:
    https://www.devdungeon.com/content/make-discord-bot-python
'''
import discord # Imports the Discord API.
import random # Imports Python's "random" library.
import store # Imports the store.py file for lists of responses.
import bmi #Imports the bmi.py file to calculate a person's BMI.
#import requests # Imports the requests api, allowing us to code the bot to recieve and respond to requests.

TOKEN = 'NjMyMzE4MzgwMTI4NjAwMDg0.XapN2Q.k30CS29SNQ_56D8w7yuiNbZzFmo' # Bot's unique ID.

client = discord.Client()

@client.event
# If the user sends a message, do something.
async def on_message(message):
    # Converts all of the message to lower-case, so that if capitals are used, the bot can detect the word anyway.
    message_list = message.content.lower()
    message_list = message_list.split()
    # Prints the message to the command line for error handling.
    print(message_list)
    if message.author == client.user:
        return
    elif message.content.lower() == "hello there":
        await message.channel.send('General Kenobi!')

    # If user sends a greeting, the bot will reply with "Hello (name of user)!" + A random greeting.
    elif any(item in store.detectable_greetings for item in message_list): 
        await message.channel.send('Hello {0.author.mention}! '.format(message) + random.choice(store.list_of_greetings))
        msg1 = await client.wait_for('message')
        msg1_list = msg1.content.lower()
        msg1_list = msg1_list.split()

        # If user sends a confirming word, i.e: "good", the bot will reply with a random confirmation statement + "Do you require my assistance?".
        if any(item in store.detectable_positives for item in msg1_list):
            await message.channel.send(random.choice(store.list_of_goods) + ' Do you require my assistance?'.format(msg1))
            msg2 = await client.wait_for('message')
            msg2_list = msg2.content.lower()
            msg2_list = msg2_list.split()

            # If the user says yes, the bot will reply with "What with?".
            if any(item in store.detectable_yes for item in msg2_list):
                await message.channel.send(random.choice(store.list_of_yes).format(msg2))
                msg3 = await client.wait_for('message')
                msg3_list = msg3.content.lower()
                msg3_list = msg3_list.split()
                if "bmi" in msg3_list:
                    await bmi.bmi_calculator(message)
    # If anything else is said by the user, the bot outputs a random line describing "I don't know what you mean.".
    #else: 
        #await message.channel.send(random.choice(store.list_of_sorrys))

@client.event
# Prints successful login.
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
