import discord
import random
import requests
import store


token = 'NjMyMzE4MzgwMTI4NjAwMDg0.XazA_g.UfGa942Ck4m_t-bNOW-MiOcXijo'

client = discord.Client()

@client.event
async def on_message(message): #if the user request a meal preparation
    message_list = message.content.lower()
    message_list = message_list.split()
    print(message_list)
    if message.author == client.user:
        return
    elif message.content.lower() == "hello there":
        await message.channel.send('General Kenobi!')

    elif any(item in store.detectable_greetings for item in message_list):
        await message.channel.send('Hello {0.author.mention}! '.format(message) + random.choice(store.list_of_greetings))
        msg1 = await client.wait_for('message')
        msg1_list = msg1.content.lower()
        msg1_list = msg1_list.split()

    elif any(item in store.meal_prep_keywords for item in message_list):
        await message.channel.send('I can help you with that. Are you planning to eat breakfast, lunch or dinner?')
        msg2 = await client.wait_for('message')
        msg2_list = msg2.content.lower()
        msg2_list = msg2_list.split()
        if msg2_list == "breakfast":
            await message.chanel.send('I will create a breakfast meal for you')
            msg_breakfast = await client.wait_for('message')
        elif msg2_list == "lunch":
            await message.chanel.send('I will create a lunch meal for you')
            msg_lunch = await client.wait_for('message')
        elif msg2_list == "dinner":
            await message.chanel.send('I will create a dinner meal for you')
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
