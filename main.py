#!/usr/bin/python
import tweepy
import io
import sqlite3
from sqlite3 import Error
from twitter_authentication import Keys
from database_functionality import *

# connect to twitter & database
my_keys = Keys()
api = my_keys.authenticate()
conn = create_db_connection('twitter.db')
curs = conn.cursor()

# create tables in DB if they don't already exist
create_tables(curs)

# define tweet sets
trump_tweets = api.search('Trump', count=100) # maxes out at 100
home_timeline = api.home_timeline(count=200) # may max out at 194

# insert tweets into DB
for tweet in home_timeline:
    insert_tweet(tweet, curs, api)
for tweet in trump_tweets:
    insert_tweet(tweet, curs, api)

# show totals
show_totals(curs)

# commit to DB and close connection
conn.commit()
conn.close()
