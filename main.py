#!/usr/bin/python
import tweepy
import io
import sqlite3
from sqlite3 import Error
from twitter_authentication import Keys
# TODO: split this giant mess up into classes/files

# connect to twitter, database, and output_file
my_keys = Keys()
auth = tweepy.OAuthHandler(my_keys.consumer_key, my_keys.consumer_secret)
auth.set_access_token(my_keys.access_token, my_keys.access_token_secret)
api = tweepy.API(auth)
conn = create_db_connection('twitter.db')
curs = conn.cursor()
output_file = io.open("results.txt", "w", encoding="utf-8")

# function to establish SQLite connection, returns conn
def create_db_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        return None

# function that inputs a tweet set into DB, returns none
def insert_tweet_set(tweet_set, cursor):
    for tweet in tweet_set:
        insert_single_tweet(tweet, cursor)
    return None

# function that inputs a single tweet into DB
def insert_single_tweet(tweet, cursor):
    # set variables to be inserted into DB
    ID = tweet.id_str
    text = tweet.text
    u_id = tweet.user.id_str
    u_name = tweet.user.name
    u_handle = tweet.user.screen_name
    u_description = tweet.user.description
    u_protected = tweet.user.protected
    u_followers = tweet.user.followers_count
    u_following = tweet.user.friends_count
    u_listed = tweet.user.listed_count
    u_created_at = tweet.user.created_at
    u_favorites = tweet.user.favourites_count
    u_tweets = tweet.user.statuses_count
    u_language = tweet.user.lang
    u_contributors_enabled = tweet.user.contributors_enabled
    time_posted = str(tweet.created_at)
    hearts = tweet.favorite_count
    retweets = tweet.retweet_count
    source_app = tweet.source
    source_app_url = tweet.source_url
    language = tweet.lang
    hashtags = tweet.entities['hashtags']
    mentions = tweet.entities['user_mentions']
    if hasattr(tweet, 'retweeted_status'):
        retweeted_tweet = tweet.retweeted_status.id_str
        insert_single_tweet(tweet.retweeted_status, cursor)
        print("retweet referential integrity satisfied")
    else:
        retweeted_tweet = None
    if hasattr(tweet, 'quoted_status'):
        #TODO: Change quoted_tweet to quoted_tweet_id to correctly define what we're doing here
        quoted_tweet = tweet.quoted_status_id_str
        insert_single_tweet(api.get_status(quoted_tweet), cursor)
        print("quoted tweet referential integrity satisfied")
    else:
        quoted_tweet = None
    if hasattr(tweet, 'reply_to_status_id'):
        in_reply_to_tweet = tweet.in_reply_to_status_id_str
        insert_single_tweet(api.get_status(in_reply_to_tweet))
        print("in reply to tweet referential integrity satisfied")
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
    if hasattr(tweet, 'user.location'):
        u_location = tweet.user.location
    else:
        u_location = None
    if hasattr(tweet, 'user.url'):
        u_website = tweet.user.url
    else:
        u_website = None
    if hasattr(tweet, 'user.utc_offset'):
        u_utc_offset = tweet.user.utc_offset
    else:
        u_utc_offset = None
    if hasattr(tweet, 'user.timezone'):
        u_timezone = tweet.user.timezone
    else:
        u_timezone = None
    if tweet.user.geo_enabled == True:
        u_geo_enabled = 1
    else:
        u_geo_enabled = 0
    if tweet.user.verified == True:
        u_verified = 1
    else:
        u_verified = 0
    if tweet.user.contributors_enabled == True:
        u_contributors_enabled = 1
    else:
        u_contributors_enabled = 0
    if tweet.user.is_translator == True:
        u_is_translator = 1
    else:
        u_is_translator = 2
    if tweet.user.is_translation_enabled == True:
        u_translation_enabled = 1
    else:
        u_translation_enabled = 0
    if tweet.user.has_extended_profile == True:
        u_extended_profile = 1
    else:
        u_extended_profile = 0
    if tweet.user.default_profile == True:
        u_default_profile = 1
    else:
        u_default_profile = 0
    if tweet.user.default_profile_image == True:
        u_default_avatar = 1
    else:
        u_default_avatar = 0
    if tweet.user.following == True:
        u_dev_follow = 1
    else:
        u_dev_follow = 0
    if hasattr(tweet, 'user.translator_type'):
        u_translator_type = tweet.user.translator_type
    else:
        u_translator_type = None

    #set queries and variables, then run
    query1 = "INSERT INTO tweets VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19)"

    query2 = "INSERT INTO users VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26)"

    query3 = "INSERT INTO hashtags VALUES(:1, :2)"
    query4 = "INSERT INTO mentions VALUES(:1, :2)"

    variables1 = {'1':ID, '2':text, '3':u_id, '4':time_posted, '5':hearts, '6':retweets, '7':retweeted_tweet, '8':quoted_tweet, '9': in_reply_to_tweet, '10':in_reply_to_user, '11':source_app, '12':source_app_url, '13':coordinates, '14':place, '15':language, '16':contributors, '17':truncated, '18':dev_heart, '19':dev_retweet}

    variables2 = {'1':u_id, '2':u_name, '3':u_handle, '4':u_location, '5':u_description, '6':u_website, '7':u_protected, '8':u_followers, '9':u_following, '10':u_listed, '11':u_created_at, '12':u_favorites, '13':u_utc_offset, '14':u_timezone, '15':u_geo_enabled, '16':u_verified, '17':u_tweets, '18':u_language, '19':u_contributors_enabled, '20':u_is_translator, '21':u_translation_enabled, '22':u_extended_profile, '23':u_default_profile, '24':u_default_avatar, '25':u_dev_follow, '26':u_translator_type}

    try:
        cursor.execute(query1, variables1)
    except Error as e:
        e_string = str(e)
        if (e_string[:24] == "UNIQUE constraint failed"):
            pass
        else:
            print(e)
    try:
        cursor.execute(query2, variables2)
    except Error as e:
        e_string = str(e)
        if (e_string[:24] == "UNIQUE constraint failed"):
            pass
        else:
            print(e)
    for tag in hashtags:
        hash_text = tag['text']
        try:
            cursor.execute(query3, {'1':ID, '2':hash_text})
        except Error as e:
            e_string = str(e)
            if (e_string[:24] == "UNIQUE constraint failed"):
                pass
            else:
                print(e)
    for name in mentions:
        mention_text = name['screen_name']
        try:
            cursor.execute(query4, {'1':ID, '2':mention_text})
        except Error as e:
            e_string = str(e)
            if (e_string[:24] == "UNIQUE constraint failed"):
                pass
            else:
                print(e)
    return None

# create tables in DB if they don't already exist
curs.execute("""CREATE TABLE
                IF NOT EXISTS tweets (
                    id text PRIMARY KEY NOT NULL,
                    tweet_text text NOT NULL,
                    user_id text NOT NULL REFERENCES users(id),
                    time_posted text NOT NULL,
                    hearts integer NOT NULL,
                    retweets integer NOT NULL,
                    retweeted_tweet text REFERENCES tweets(id),
                    quoted_tweet text REFERENCES tweets(id),
                    in_reply_to_tweet text REFERENCES tweets(id),
                    in_reply_to_user text REFERENCES users(id),
                    source_app text NOT NULL,
                    source_app_url text NOT NULL,
                    coordinates text,
                    place text,
                    language text NOT NULL,
                    contributors text,
                    truncated integer NOT NULL,
                    dev_heart integer NOT NULL,
                    dev_retweet integer NOT NULL
                )""")
curs.execute("""CREATE TABLE
                IF NOT EXISTS users (
                    id text PRIMARY KEY NOT NULL,
                    name text NOT NULL,
                    handle text NOT NULL,
                    location text,
                    description text NOT NULL,
                    website text,
                    protected integer NOT NULL,
                    followers integer NOT NULL,
                    following integer NOT NULL,
                    listed integer NOT NULL,
                    created_at text NOT NULL,
                    favorites integer NOT NULL,
                    utc_offset integer,
                    timezone text,
                    geo_enabled integer NOT NULL,
                    verified integer NOT NULL,
                    tweets integer NOT NULL,
                    language text NOT NULL,
                    contributors_enabled integer NOT NULL,
                    translator integer NOT NULL,
                    translation_enabled integer NOT NULL,
                    extended_profile integer NOT NULL,
                    default_profile integer NOT NULL,
                    default_avatar integer NOT NULL,
                    dev_follow integer NOT NULL,
                    translator_type text
                    )""")
curs.execute("""CREATE TABLE
                IF NOT EXISTS hashtags (
                    tweet_id text NOT NULL REFERENCES tweets(id),
                    hashtag text NOT NULL,
                    PRIMARY KEY(tweet_id, hashtag)
                )""")
curs.execute("""CREATE TABLE
                IF NOT EXISTS mentions (
                    tweet_id text NOT NULL REFERENCES tweets(id),
                    mention_handle text NOT NULL REFERENCES users(handle),
                    PRIMARY KEY (tweet_id, mention_handle)
                )""")

# define tweet sets
trump_tweets = api.search('Trump', count=100) # maxes out at 100
home_timeline = api.home_timeline(count=200) # may max out at 194

# insert tweets into DB
insert_tweet_set(home_timeline, curs)
insert_tweet_set(trump_tweets, curs)

# select all tweets
curs.execute("SELECT tweet_text FROM tweets")
results = curs.fetchall()
for row in results:
    output_file.write(str(row) + "\n\n\n")

# commit to DB and close connection
conn.commit()
conn.close()
