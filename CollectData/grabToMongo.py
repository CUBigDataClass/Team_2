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

class StreamListener(tweepy.StreamListener):
    def on_connect(self):
        #connection is made
        print("Running Tweepy to MongoDB")
 
    def on_error(self, status_code):
        #error occurs
        print('Error: ' + repr(status_code))
        return False
 
    def on_data(self, data):
        #receive data
        client = MongoClient('localhost', 27017)
 
        # Use New Twitter database
        db = client.New_TwitterDB

        datajson = json.loads(data)
 
        # Only English Tweets
        if "lang" in datajson and datajson["lang"] == "en":
            # store in New Twitter collection
            db.New_TwitterDB.insert(datajson)

CONSUMER_KEY = "vEonqCYTlT5WglV2OePedchly"
CONSUMER_SECRET = "AZDKA5O7ND8zxUnUA4Av261CMkHW9qDJ6tas76wqqen1UbFfL8"
ACCESS_TOKEN = "583088622-5jAKHt74mFfzJiQEoj8Cdw06pWhvKexkAAtRt0Ex"
ACCESS_TOKEN_SECRET = "UcbJpokOKdrsHlVfKu2FRKUfV2hEF1pDlqCVxNL18WW7P"

#Load credentials
#Authenticating
auth1 = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth1.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
 
l = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth1, listener=l)
streamer.filter(track=keyword_list)