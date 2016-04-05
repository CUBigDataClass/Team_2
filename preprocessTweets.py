import nltk
#nltk.download('all') # run this line in the first time
from nltk import word_tokenize
import re
import json, ast

import operator 
from collections import Counter
 

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


with open('raw_tweets.json', 'r') as tweet_data:
    json_data = json.load(tweet_data)

file = open("newfile.txt", "r+")

                
for tweets in json_data:
	try:    
		
		#text = tweets['text']
		#print text.encode('utf-8')
		#print preprocess(tweets['text']) #get rid of space.
		preprocessWord= preprocess(tweets['text'])       		
		#file.write(preprocessWord)                
		print ast.literal_eval(json.dumps(preprocessWord)) #get rid of space
                preprocessWord= ast.literal_eval(json.dumps(preprocessWord))
		print >> file, preprocessWord, newfile.txt

		# Update the counter
		#print terms_all
        	# Create a list with all the terms		
		count_all = Counter()        	
		terms_all = [term for term in preprocessWord]
				
        	# Update the counter
        	count_all.update(terms_all)
		# Print the first 5 most frequent words
		print(count_all)
		#sum(Counte_all).value()        
	except:
		pass

file.close() 

fname = "newfile.txt"

num_lines = 0
num_words = 0
num_chars = 0


with open(fname, 'r') as newfile:
    for line in newfile:
        words = line.split()
        num_lines += 1
        num_words += len(words)
        num_chars += len(line)

print(num_words) #words
print(num_chars) # number of chars


file=open("newfile.txt","r")

wordcount={}

for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1

for k,v in wordcount.items():
    print k, v

