import tweepy
import io
import sqlite3
from sqlite3 import Error

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, tweet):
        print(tweet.text)

    def on_error(self, status_code):
        if status_code == 420:
            return False
        else:
            print("Stream Error" + str(status_code))

# function to establish twitter connection, returns api
def authenticate_to_twitter(c_key, c_secret, a_token, a_secret):
    auth = tweepy.OAuthHandler(c_key, c_secret)
    auth.set_access_token(a_token, a_secret)
    api = tweepy.API(auth)
    return api

api = authenticate_to_twitter('AhqRDo5NYd2XRP3G3apZar7JC', 'jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO', '68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd', 'vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV')

myStreamListener = MyStreamListener()
twitterStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
twitterStream.filter(track=["Donald Trump"], async=True)
