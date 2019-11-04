from nltk.corpus import wordnet, twitter_samples, stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import FreqDist, classify, NaiveBayesClassifier
from nltk.tag import pos_tag
import re, string, random

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()

def synonymListMaker(wordList):
    synonyms = []
    for word in wordList:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())
    synonyms = wordList + synonyms
    return synonyms

def antonymListMaker(wordList):
    antonyms = []
    for word in wordList:
        for syn in wordnet.synsets(word):
            for l in syn.lemmas():
                if l.antonyms():
                    antonyms.append(l.antonyms()[0].name())
    return antonyms

def wordPresenceCheck(inputWord, wordList):
    synonyms = synonymListMaker(wordList)
    found = False
    for word in synonyms:
       if inputWord == word:
            found = True
            break
    return found

def sentenceFilter(sentence):
    stopWords = set(stopwords.words("english"))
    tokenizedSentence = word_tokenize(sentence)
    lemmatizedList = []
    for word in tokenizedSentence:
        lemmatizedList.append(lemmatizer.lemmatize(word,"v"))
    filteredSentence = []
    for word in lemmatizedList:
        if word not in stopWords:
            filteredSentence.append(word)
    return filteredSentence

def filterTweet(tokenizedTweet, stopWords = ()):
    filteredTokens = []
    for token, tag in pos_tag(tokenizedTweet):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'
        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stopWords:
            filteredTokens.append(token.lower())
        filteredTokens.append(token.lower())
    return filteredTokens

def listAllWords(filteredTokesList):
    for tokens in filteredTokesList:
        for token in tokens:
            yield token

def getModelTweets(filteredTokesList):
    for tweet_tokens in filteredTokesList:
        yield dict([token, True] for token in tweet_tokens)

def CreateSentimentData():
    posTweetTokens = twitter_samples.tokenized('positive_tweets.json')
    negTweetTokens = twitter_samples.tokenized('negative_tweets.json')
    stopWords = stopwords.words('english')
    posFilteredTweetslist = []
    negFilteredTweetslist = []
    for tokens in posTweetTokens:
        posFilteredTweetslist.append(filterTweet(tokens, stopWords))
    for tokens in negTweetTokens:
        negFilteredTweetslist.append(filterTweet(tokens, stopWords))

    posWords = listAllWords(posFilteredTweetslist)

    posFreqDistribution = FreqDist(posWords)

    posModelTokens = getModelTweets(posFilteredTweetslist)
    negModelTokens = getModelTweets(negFilteredTweetslist)

    posDataset = [(tweet_dict, "Positive")
                         for tweet_dict in posModelTokens]

    negDataset = [(tweet_dict, "Negative")
                         for tweet_dict in negModelTokens]

    dataset = posDataset + negDataset
    random.shuffle(dataset)
    train_data = dataset[:7000]
    test_data = dataset[7000:]
    classifier = NaiveBayesClassifier.train(train_data)
    print("Accuracy is:", classify.accuracy(classifier, test_data))
    return classifier
    
def returnSentiment(filteredSentence):
    print(classifier.classify(dict([token, True] for token in filteredSentence)))

classifier = CreateSentimentData()
returnSentiment(sentenceFilter("my day has been pretty good so far"))
