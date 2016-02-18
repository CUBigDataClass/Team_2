from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json



#consumer key, consumer secret, access token, access secret.
ckey="Consumer key"
csecret="Consumer secret"
atoken="access-token"
asecret="access secret"

class listener(StreamListener):

    def on_data(self, data):
        print(data)
        return(True)

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['tweepy'])


