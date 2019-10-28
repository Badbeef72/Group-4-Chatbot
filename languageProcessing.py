from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

def synonymListMaker(wordList):
    synonyms = []
    for word in wordList:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
    synonyms = wordList + synonyms
    return synonyms

def wordPresenceCheck(inputWord, wordList):
    synonyms = synonymListMaker(wordList)
    fo40und = False
    for word in synonyms:
       if inputWord == word:
            found = True
            break
    return found

def sentenceFilter(sentence):
    stopWords = set(stopwords.words("english"))
    tokenizedSentence = word_tokenize(sentence)
    stemmedList = []
    for word in tokenizedSentence:
        stemmedList.append(stemmer.stem(word))
    filteredSentence = []
    for word in stemmedList:
        if word not in stopWords:
            filteredSentence.append(word)
    return filteredSentence



