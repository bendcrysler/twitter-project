import tweepy

consumer_key = 'AhqRDo5NYd2XRP3G3apZar7JC'
consumer_secret = 'jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO'

access_token = '68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd'
access_secret = 'vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
