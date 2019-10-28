import discord
import nltk
import numpy as np
import random
import string
import tkinter
import bot.py

f = open('nltkCorpus.txt', 'r', errors = 'ignore')

raw = f.read()

raw = raw.lower()

nltk.download('punkt')
nltk.download('wordnet')

sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()


def lemTokens(tokens):
  return [lemmer.lemmetize(token) for token in tokens]
  remove_punc_dict = dict((ord(punct), None) for punct in string.punctuation)


def lemNormalize(text):
  return
lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from store.py import detectable_greetings, list_of_greetings

triggerBotReponse = detectable_greetings
botResponse = list_of_greetings

#detectable_greetings = ["hello", "hi", "hey", "greetings", "yo", "sup", "what's up"]
#list_of_greetings = ["I hope you have been well?", "How are you?", "Everything going well?", "What's up?", "How's it going?"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in triggerBotReponse:
            print(random.choice(botResponse))


# This module allows us to convert a collection of raw docs into a matrix of TF-IDF features
from sklearn.feature_extraction.text import TfidVectorizer
# This module is used to find the similarity between the words from the user's input and the words in the corpus
from sklearn.metrics.pairwise import cosine_similarity


# This function searches the user's input for key words and returns multiple options for responses
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

    # If it doesn't find one of the keywords it responds "I am sorry, I don't get what you mean bud"
    if(req_tfidf==0):
        bot_reponse = bot_response + "I am sorry, I don't get what you mean bud."
        return bot_response
    else:
        bot_response = bot_response + sent_tokens[idx]
        return bot_response


# tf–idf or TFIDF, short for term frequency–inverse document frequency, is a numerical statistic that is intended to reflect how important a word is to a document in a collection or corpus. ref: https://en.wikipedia.org/wiki/Tf%E2%80%93idf
