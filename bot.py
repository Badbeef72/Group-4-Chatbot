# Main file for Kong Fuzi, setup, connect to Discord etc.
# Initialisation code used from this tutorial:
# -- https://realpython.com/how-to-make-a-discord-bot-python/
##########################################################
import os                      # Imports necessary libraries.
import discord
from dotenv import load_dotenv # Dotenv allows environment variables to be stored in a separate file, such as usernames, IDs etc.

load_dotenv()                       # Initialises variables.
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!') # Print statement when client connects to Discord.

client.run(token)
