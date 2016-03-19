from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json
import os
import time

#Purpose
#This code checks the twitter stream and saves the content to a mongo databse. 
#make sure all the dependencies are installed before running this code. 
	#Dependencies are: tweepy, pymong, mongod
#also make sure the access key is correct

#io.open()
ckey = 'n6Z77TqskY5ENS63O0Ik7Ccqo'# remove this before git push
consumer_secret = 'tVdUiDcQ9SQAjFBMLl9110wZbsjHrRsOepXoomuYM21poCQKNM' # remove this before git push
access_token_key = '25107624-owjnkBTlYzMYkKTqjsWAOxHEh5V6AWVI5OlNiUtLC' # remove this before git push
access_token_secret = 'd99V1aahIUekjE0lxJhDLyWW552XsNbBwLSqVsOThcRNp' # remove this before git push

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

			try:
				client = MongoClient('localhost', 27017)
				db = client['twitter_db']
				collection = db['twitter_collection']
				tweet = json.loads(data)
				collection.insert(tweet)
				return True
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
			exit()
	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit = 20))
twitterStream.filter(track=keyword_list, languages = ['en'])