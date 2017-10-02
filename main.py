import tweepy
import io
import sqlite3

# Establish twitter connection
consumer_key = 'AhqRDo5NYd2XRP3G3apZar7JC'
consumer_secret = 'jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO'
access_token = '68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd'
access_secret = 'vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

# establish SQLite connection
conn = sqlite3.connect('twitter.db')
if (conn):
    print ("connection successful")
else:
    print ("connection failed")
curs = conn.cursor()

# opening file for printing, utf-8 necessary for processing emoji
output_file = io.open("results.txt", "w", encoding="utf-8")

# Collect tweets
trump_tweets = api.search('Trump')
home_timeline = api.home_timeline(count=25)

def getTweetInfo(tweet_set,indicies):
    # inputs a tweet set into DB
    for tweet in tweet_set:
        # set variables to be inserted into DB
        ID = tweet.id_str
        text = tweet.text
        user_id = tweet.user.id_str
        time_posted = str(tweet.created_at)
        hearts = tweet.favorite_count
        retweets = tweet.retweet_count
        source_app = tweet.source
        source_app_url = tweet.source_url
        language = tweet.lang
        if hasattr(tweet, 'retweeted_status'):
            retweeted_tweet = tweet.retweeted_status.id_str
        else:
            retweeted_tweet = None
        if tweet.is_quote_status == True:
            quoted_tweet = tweet.quoted_status_id_str
        else:
            quoted_tweet = None
        if hasattr(tweet, 'reply_to_status_id'):
            in_reply_to_tweet = tweet.in_reply_to_status_id_str
            in_reply_to_user = tweet.in_reply_to_user_id_str
        else:
            in_reply_to_tweet = None
            in_reply_to_user = None
        if hasattr(tweet, 'coordinates'):
            coordinates = str(tweet.coordinates)
        else:
            coordinates = None
        if hasattr(tweet, 'place'):
            place = str(tweet.place)
        else:
            place = None
        if hasattr(tweet, 'contributors'):
            contributors = str(tweet.contributors)
        else:
            contributors = None
        if tweet.truncated == True:
            truncated = 1
        else:
            truncated = 0
        if tweet.favorited == True:
            dev_heart = 1
        else:
            dev_heart = 0
        if tweet.retweeted == True:
            dev_retweet = 1
        else:
            dev_retweet = 0

        #set query using variables and run
        query = "INSERT INTO tweets VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19)"
        variables = {'1':ID, '2':text, '3':user_id, '4':time_posted, '5':hearts, '6':retweets, '7':retweeted_tweet, '8':quoted_tweet, '9': in_reply_to_tweet, '10':in_reply_to_user, '11':source_app, '12':source_app_url, '13':coordinates, '14':place, '15':language, '16':contributors, '17':truncated, '18':dev_heart, '19':dev_retweet}
        curs.execute(query, variables)

getTweetInfo(home_timeline, desired_properties)
getTweetInfo(trump_tweets, desired_properties)

conn.commit()
conn.close()
output_file.close()
