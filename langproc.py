import nltk
import store
import random

from nltk.corpus import wordnet 

print("Testing natural dialogue with nltk, start conversation like you would with the bot in the discord")
currentMessage = input()
synonyms = []
for word in store.detectable_greetings:
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
synonyms = synonyms + store.detectable_greetings
for greeting in synonyms:
    if currentMessage == greeting:
        print(random.choice(store.detectable_greetings))
        print(random.choice(store.list_of_greetings))
        break

currentMessage = input()
synonyms = []
antonyms = []
synonyms = synonyms + store.detectable_greetings
for word in store.detectable_greetings:

    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name())
            if l.antonyms(): 
                antonyms.append(l.antonyms()[0].name())
for word in synonyms:
    if currentMessage == word:
        synonymFound = True
    else:
        synonymFound = False
antonymFound = False
if synonymFound == True:
    print(random.choice(store.list_of_goods))
else:
    for word in antonyms:
        if currentMessage == word:
            antonymFound = True
    if antonymFound == True:
        print("That's a shame")
    else:
        antonymFound = False

print("Is there anything health and fitness related I could help you with?")

currentMessage = input()
currentMessageWords = currentMessage.split()

loseWeightWords = ["lose", "weight", "get", "shape", "slim", "thin", "slimmer", "thinner"]
synonyms = []
for word in loseWeightWords:
    for syn in wordnet.synsets(word): 
        for l in syn.lemmas(): 
            synonyms.append(l.name())
synonyms = synonyms + loseWeightWords

loseWeightChance = 0

for word in currentMessageWords:
    for syn in synonyms:
        if word == syn:
            loseWeightChance = loseWeightChance + 1

if loseWeightChance >= 2:
    print("You want help losing weight? I can help you.")

