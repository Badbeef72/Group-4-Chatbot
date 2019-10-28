# Main file for the bot.
'''
    Tutorial from:
    https://www.devdungeon.com/content/make-discord-bot-python
'''

# We need to have a look over how the robot responds and behaves; it has to respond 'like a humna', or as close to that as possible
# Also, implementing NLTK is important as it is a complex tool and will get us grades, so if everyone or someone wants a good grade. There you go.
# Also, it might be a good idea to label the code that people do to keep track of contribution.
# Never delete someone elses code. If it clashes with yours # you or their code out and discuss it with them at a meeting.


import discord # Imports the Discord API.
import random # Imports Python's "random" library.
import store # Imports the store.py file for lists of responses.
import bmi #Imports the bmi.py file to calculate a person's BMI.
#import requests # Imports the requests api, allowing us to code the bot to recieve and respond to requests.

TOKEN = 'NjMyMzE4MzgwMTI4NjAwMDg0.XbYKfg.g40KlmqJvGRvjYPSKIPRpRvQ-Rs' # Bot's unique ID.

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

            if any(item in store.detectable_positives for item in msg2_list):
                await message.channel.send(random.choice(store.list_of_goods) + ' What do you need help with?'.format(msg2))

            elif any(item in store.detectable_negatives for item in msg2_list):
                await message.channel.send('I will be here if you need me.'.format(msg2))
            # I have #'ed this out Danny as it clashes with the block of code that follows that I have added. They do the same thing.
            # If the user says yes, the bot will reply with "What with?".
#            if any(item in store.detectable_yes for item in msg2_list):
 #               await message.channel.send(random.choice(store.list_of_yes).format(msg2))
  #              msg3 = await client.wait_for('message')
   #             msg3_list = msg3.content.lower()
    #            msg3_list = msg3_list.split()
     #           if "bmi" in msg3_list:
      #              await bmi.bmi_calculator(message)
    # If anything else is said by the user, the bot outputs a random line describing "I don't know what you mean.".
    #else:
        #await message.channel.send(random.choice(store.list_of_sorrys))

        # Moagy
            # Listing its functions and then making them activated via command in the format of !command
            # The names of the functions are not set in stone, they can be subject to change

            if any(item in store.detectable_yes for item in msg2_list):
                await message.channel.send("These are my function commands: \nbmi <height in metres> <weight in kgs> : I can help work out your BMI using your height and weight. \ngymfinder : I can help you find the best gym near you. \nexercises : I can give you exercises to do to work out certain muscles. \nfitnessgoals : I can give you certain lifestyle advice depending on what you want to achieve.")

            # The robot should respond to these commands
            # List of commands the bot will respond to

    elif 'bmi' in message_list:
        await bmi.bmi_calculator(message, message_list[1], message_list[2])

    #elif message.content.upper().startswith('!GYMFINDER'):
            # The robot should respond to these commands

    #elif message.content.upper().startswith('!EXERCISES'):
            # Exercises code in here please

    #elif message.content.upper().startswith('!FITNESSGOALS'):
            # Fitness goal code in here please



@client.event
# Prints successful login.
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
