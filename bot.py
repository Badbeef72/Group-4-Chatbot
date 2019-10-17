'''
    Initialisation code courtesty of:
    https://www.devdungeon.com/content/make-discord-bot-python
    
'''
import discord # Imports the Discord API.

TOKEN = 'NjMyMzE4MzgwMTI4NjAwMDg0.Xaj5xA.WugioJKVjRc2c3HnKhYwuzN6EyQ' # Bot's unique ID.

client = discord.Client()

@client.event
async def on_message(message): # If the user sends a certain message, do something.
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready(): # Prints successful login.
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)