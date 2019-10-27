import discord
import random
import store
import bmi
import requests
import tkinter
import numpy as np
import string
import nltk
#from scipy.feature_extraction.text import sklearn
#from scipy.metrics.pairwise import cosine_similarity

TOKEN = 'NjMyMzE4MzgwMTI4NjAwMDg0.XbWPOA.w8XSPCHR4f98li-ScxBXbGyxlYc' # Bot's unique ID.


client = discord.Client()

openCorpusDoc = open('nltkCorpus.txt', 'r', errors = 'ignore')

raw = openCorpusDoc.read()

raw = raw.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()

@client.event

def lemTokens(tokens):
    return [lemmer.lemmetize(token) for token in tokens]
    remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)

def lemNormalize(text):
    return text
    lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from store import detectable_greetings, list_of_greetings

triggerBotReponse = detectable_greetings
botResponse = list_of_greetings


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in triggerBotReponse:
            print(random.choice(botResponse))

def response(user_response):
    bot_response = ' '
    sent_tokens.append(bot_response)

    TfiddVec = TfidfVectorizer(tokenizer = lemNormalize, stop_words = 'english')
    tfidf = TfidfVec.fit_transform(snet_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    reg_tfidf = flat[-2]

    if(req_tfidf==0):
        bot_reponse = bot_response + "I am sorry, I don't get what you mean bud."
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response

@client.event
# Prints successful login.
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')



client.run(TOKEN)
