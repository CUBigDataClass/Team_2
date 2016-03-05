from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json
import os
import time

client = MongoClient('localhost', 27017)
db = client['twitter_db']
collection = db['twitter_collection']

tweets_iterator = collection.find()
for tweet in tweets_iterator:
	# collection.find({'text' : 'This will return tweets with only this exact string.'})
	# tweets = collection.find({'user.screen_name' : 'exactScreenName'})
	# tweets = collection.find({'text': { '$regex' : 'word'}})
	# collection.find({"retweeted_status" : { "$exists" : "true"}})
	
	try:
		text = tweet['text']
		print text.encode('utf-8')
	except:
		print ' no texxt for this tweet'
	try:
		user_screen_name = tweet['user']['screen_name']
		print user_screen_name
	except:
		print ' no user screen name for this user'
	try:
		user_name = tweet['user']['name']
		print user_name
	except:
		print ' no user name for this user'
	try:
		retweet_count = tweet['retweeted_status']['retweet_count']
		print retweet_count
	except:
		print ' no retweet count for this'
	try:
		retweeted_name = tweet['retweeted_status']['user']['name']
		print retweeted_name
	except:
		print ' no retweet name for this'
	try:
		retweeted_screen_name = tweet['retweeted_status']['user']['screen_name']
		print retweeted_screen_name
	except:
		print ' no retweet screen name for this '

