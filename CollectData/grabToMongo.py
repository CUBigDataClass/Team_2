"""
#Tutorial used: https://coolprof.wordpress.com/2014/10/19/tweepy-and-pymongo-retrieving-and-storing-tweets-in-mongodb/
#Tutorial Author: Ruben Cuevas Menendez
"""
from __future__ import print_function
import tweepy
import json
from pymongo import MongoClient

keyword_list = (['election', 
'bernie', 'Bernie', 'bernie sanders', 'Bernie Sanders', 
'trump', 'Trump', 'donald trump', "Donald Trump",
'hillary', 'Hillary', 'clinton', 'Clinton', 'hillary clinton', 'Hillary Clinton',
'cruz', 'Cruz', 'ted cruz', 'Ted Cruz',
'GOP', 'gop', 'republican', 'Republican',
'democrat', 'Democrat'])
i=0
class StreamListener(tweepy.StreamListener):
    def on_connect(self):
        #connection is made
        print("Running Tweepy to MongoDB")
 
    def on_error(self, status_code):
        #error occurs
        print('Error: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        for i in range(0, 500):
        #receive data
            client = MongoClient('localhost', 27017)
            i += 1
        # Use New Twitter database
            db = client.New_TwitterDB

            datajson = json.loads(data)
 
        # Only English Tweets
            if "lang" in datajson and datajson["lang"] == "en":
            # store in New Twitter collection
                db.New_TwitterDB.insert(datajson)
                i -= 1

CONSUMER_KEY = ""
CONSUMER_SECRET = ""
ACCESS_TOKEN = ""
ACCESS_TOKEN_SECRET = ""

#Load credentials
#Authenticating
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
l = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth1, listener=l)
streamer.filter(track=keyword_list)