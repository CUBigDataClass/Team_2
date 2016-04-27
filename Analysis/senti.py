import nltk
#nltk.download('all') # run this line in the first time
from nltk import word_tokenize
import re
import json, ast

import operator 
from collections import Counter

#import sys
#sys.modules[__name__].__dict__.clear()



#In this script we can't have the double negative program, such as 'not bad' 
pos_tweets = [('I love this car', 'positive'),
              ('This view is amazing', 'positive'),
              ('I feel great this morning', 'positive'),
              ('I am so excited about the fantastic concert', 'positive'),
              ('He is my best friend', 'positive'),
	      ('She is very good', 'positive')]



neg_tweets = [('I do not like this car', 'negative'),
              ('This view is horrible', 'negative'),
              ('I feel tired this morning', 'negative'),
              ('I am not looking forward to the concert', 'negative'),
              ('Bad badly hurt', 'negative'),
              ('I hate that', 'negative'),
	      ('This is bad', 'negative')]



tweets = []
for (words, sentiment) in pos_tweets + neg_tweets:
	words_filtered = [e.lower() for e in words.split() if len(e) >= 3]
	tweets.append((words_filtered, sentiment))


print tweets;

test_tweets = [(['feel', 'happy', 'this', 'morning'], 'positive'),
	    (['larry', 'friend'], 'positive'),
	    (['not', 'like', 'that', 'man'], 'negative'),
	    (['house', 'not', 'great'], 'negative'),
	    (['your', 'song', 'annoying'], 'negative')]

print test_tweets;



def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
	  all_words.extend(words)
	return all_words

def get_word_features(wordlist):
	wordlist = nltk.FreqDist(wordlist)
	word_features = wordlist.keys()
	return word_features


word_features = get_word_features(get_words_in_tweets(tweets))

#print word_features;

def extract_features(document):
	document_words = set(document)
	features = {}
	for word in word_features:
	  features['contains(%s)' % word] = (word in document_words)
	return features

training_set = nltk.classify.apply_features(extract_features, tweets)

#print training_set;

classifier = nltk.NaiveBayesClassifier.train(training_set)

#print classifier.show_most_informative_features(32)

#Here is a test


tweet1 = 'trump is not good enough'
print 'tweets:',tweet1,'\n', 'classifying results is:', classifier.classify(extract_features(tweet1.split()))


tweet2 = 'CU is bad'
print 'tweets:',tweet2, '\n', 'classifying results is :',classifier.classify(extract_features(tweet2.split()))


tweet3 = 'CU is good'
print 'tweets:',tweet3, '\n', 'classifying results is :',classifier.classify(extract_features(tweet3.split()))

#tweet4 = 'CU is not good'
#print 'tweets:',tweet4, '\n', 'classifying results is :',classifier.classify(extract_features(tweet4.split()))

#tweet5 = 'CU is not bad'
#print 'tweets:',tweet5, '\n', 'classifying results is :',classifier.classify(extract_features(tweet5.split()))

