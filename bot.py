# Main file for the bot.
'''
    Tutorial from:
    https://www.devdungeon.com/content/make-discord-bot-python
'''

# necessary libraries for this bot
import discord
import io
import languageProcessing
import numpy as np
from nltk import *
from nltk.stem import WordNetLemmatizer
import random
import store
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings

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

            if any(item in store.detectable_yes for item in msg2_list):
                await message.channel.send("These are my function commands: \nbmi <height in metres> <weight in kgs> : I can help work out your BMI using your height and weight. \ngymfinder : I can help you find the best gym near you. \nexercises : I can give you exercises to do to work out certain muscles. \nfitnessgoals : I can give you certain lifestyle advice depending on what you want to achieve.")

    elif 'bmi' in message_list:
        await bmi.bmi_calculator(message, message_list[1], message_list[2])

global_user_response = []

warnings.filterwarnings('ignore')

download('popular', quiet=True)

# Reading in the corpus
with open('nltkCorpus.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

# Tokenisation
sent_tokens = sent_tokenize(raw)
word_tokens = word_tokenize(raw)

# Word preprocessing
# This block of code was copied from https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e, and modified to suit our particular project
lemmer = WordNetLemmatizer()
def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def lemNormalize(text):
    return lemTokens(word_tokenize(text.lower().translate(remove_punct_dict)))


# Matching greetings with responses
GREETING_INPUTS = store.detectable_greetings
GREETING_RESPONSES = store.list_of_greetings


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating the responses
# This block of code was copied from https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e, and modified to suit our particular project
def response(user_response):
    global_user_response = user_response
    bot_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf == 0):
        bot_response = bot_response + "I am sorry! I don't get you bro."
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response


flag=True
print("My name is FitnessFriend. I will answer your queries about Fitness.")
while(flag == True):
    temp_var_1 = ' '.join(global_user_response).lower()
    global_user_response = temp_var_1
    if(global_user_response != store.list_of_goodbyes):
        if(global_user_response == store.list_of_thanks):
            flag = False
            print("You're welcome bud.")
        else:
            if(greeting(global_user_response) != None):
                print(greeting(global_user_response))
            else:
                print(end="")
                print(response(global_user_response))
                sent_tokens.remove(global_user_response)
    else:
        flag = False
        print("See ya! Take it easy.")


                #################
                ## Referencing ##
                #################

# Here are some links to websites and documentation I used to create this consider
# https://www.nltk.org/
# https://scikit-learn.org/stable/modules/classes.html#module-sklearn.feature_extraction.text
# https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html
# https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e
# https://www.youtube.com/watch?v=xECXZ3tyONo
# https://www.youtube.com/watch?v=FLZvOKSCkxY

@client.event
# Prints successful login.
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
