import time
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import io
import os

#Purpose:
#This code is now deprecated. We used it to understand how the streaming API works with tweepy. it takes tweets and saves them to a file.
#Do not run this code on the server

#consumer key, consumer secret, access token, access secret.
ckey = 'n6Z77TqskY5ENS63O0Ik7Ccqo'# remove this before git push
consumer_secret = 'tVdUiDcQ9SQAjFBMLl9110wZbsjHrRsOepXoomuYM21poCQKNM' # remove this before git push
access_token_key = '25107624-jMrjYG2do0xY3eiJCTJSf9bvf8jtuOz93Zg5JepfK' # remove this before git push
access_token_secret = 'hj3vlMrmhkJZR9ii2A0bQ8rfFb9gIYvTZHZgRp6jsBXcO' # remove this before git push

start_time = time.time() #grabs the system time
keyword_list = (['election', 'bernie', 'trump', 'clinton', 'hillary', 'GOP', 'democrat', 'republican'] #track list

class listener(StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
		self.tweet_data = []
 
	def on_data(self, data):
 
		saveFile = io.open('raw_tweets.json', 'a', encoding='utf-8')
 
		while (time.time() - self.time) < self.limit:
 
			try:
 
				self.tweet_data.append(data)
 
				return True
 
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		saveFile = io.open('raw_tweets.json', 'w', encoding='utf-8')
		saveFile.write(u'[\n')
		saveFile.write(','.join(self.tweet_data))
		saveFile.write(u'\n]')
		saveFile.close()
		exit()
 
	def on_error(self, status):
 
		print status

auth = OAuthHandler(ckey, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

twitterStream = Stream(auth, listener(start_time, time_limit = 20))
twitterStream.filter(track=keyword_list, languages = ['en'])
	

