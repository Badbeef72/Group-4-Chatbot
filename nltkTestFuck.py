# necessary libraries for this bot
import io
import random
import store
import string
import warnings
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

global_user_response = []

warnings.filterwarnings('ignore')

nltk.download('popular', quiet=True)

# Reading in the corpus
with open('nltkCorpus.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

# Tokenisation
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

# Word preprocessing
# This block of code was copied from https://medium.com/analytics-vidhya/building-a-simple-chatbot-in-python-using-nltk-7c8c8215ac6e, and modified to suit our particular project
lemmer = WordNetLemmatizer()
def lemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def lemNormalize(text):
    return lemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


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
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
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
    temp_var_1 = ' '.join(global_user_response)
    temp_var_1 = str(temp_var_1.lower())
    temp_var_1 = temp_var_1.split()
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
