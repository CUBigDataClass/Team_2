


#This code is now depreciated. Use grabToMongo.py


from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json
import os
import time
from httplib import IncompleteRead

#Purpose
#This code checks the twitter stream and saves the content to a mongo databse. 
#make sure all the dependencies are installed before running this code. 
	#Dependencies are: tweepy, pymong, mongod
#also make sure the access key is correct

#io.open()
ckey = 'vEonqCYTlT5WglV2OePedchly'# remove this before git push
consumer_secret = 'AZDKA5O7ND8zxUnUA4Av261CMkHW9qDJ6tas76wqqen1UbFfL8' # remove this before git push
access_token_key = '583088622-5jAKHt74mFfzJiQEoj8Cdw06pWhvKexkAAtRt0Ex' # remove this before git push
access_token_secret = 'UcbJpokOKdrsHlVfKu2FRKUfV2hEF1pDlqCVxNL18WW7P' # remove this before git push

start_time = time.time() #grabs the system time

#list of keywords we want to grab
keyword_list = (['election', 
'bernie', 'Bernie', 'bernie sanders', 'Bernie Sanders', 
'trump', 'Trump', 'donald trump', "Donald Trump",
'hillary', 'Hillary', 'clinton', 'Clinton', 'hillary clinton', 'Hillary Clinton',
'cruz', 'Cruz', 'ted cruz', 'Ted Cruz',
'GOP', 'gop', 'republican', 'Republican',
'democrat', 'Democrat'])

class listener(StreamListener):
	def __init__(self, start_time, time_limit = 60):
		self.time = start_time
		self.limit = time_limit

	def on_data(self, data):
		while(time.time() - self.time) < self.limit:
				client = MongoClient('localhost', 27017)
				db = client['twitter_db']
				collection = db['twitter_collection']
				tweet = json.loads(data)
				collection.insert(tweet)
				return True

	def on_error(self, status):
		print >> sys.stderr, 'Encountered error with status code:', status_code
        return True

auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
try:
	twitterStream = Stream(auth, listener(start_time, time_limit = 20))
	twitterStream.filter(track=keyword_list, languages = ['en'])
except IncompleteRead:
	pass