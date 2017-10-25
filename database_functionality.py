import sqlite3
from sqlite3 import Error

def create_db_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        return None

def create_tables(cursor):
    try:
        cursor.execute("""CREATE TABLE
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
        cursor.execute("""CREATE TABLE
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
        cursor.execute("""CREATE TABLE
                        IF NOT EXISTS hashtags (
                            tweet_id text NOT NULL REFERENCES tweets(id),
                            hashtag text NOT NULL,
                            PRIMARY KEY(tweet_id, hashtag)
                        )""")
        cursor.execute("""CREATE TABLE
                        IF NOT EXISTS mentions (
                            tweet_id text NOT NULL REFERENCES tweets(id),
                            mention_handle text NOT NULL REFERENCES users(handle),
                            PRIMARY KEY (tweet_id, mention_handle)
                        )""")
    except Error as e:
        print(e)

def insert_tweet(tweet, cursor, api):
    # set variables to be inserted into DB
    ID = tweet.id_str
    u_id = tweet.user.id_str
    text = tweet.text
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
        insert_tweet(tweet.retweeted_status, cursor, api)
    else:
        retweeted_tweet = None
    if hasattr(tweet, 'quoted_status'):
        #TODO: Change quoted_tweet to quoted_tweet_id to correctly define what we're doing here
        quoted_tweet = tweet.quoted_status_id_str
        insert_tweet(api.get_status(quoted_tweet), cursor, api)
    else:
        quoted_tweet = None
    if hasattr(tweet, 'reply_to_status_id'):
        in_reply_to_tweet = tweet.in_reply_to_status_id_str
        insert_tweet(api.get_status(in_reply_to_tweet), cursor, api)
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

    query = "INSERT INTO tweets VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19)"

    variables = {'1':ID, '2':text, '3':u_id, '4':time_posted, '5':hearts, '6':retweets, '7':retweeted_tweet, '8':quoted_tweet, '9': in_reply_to_tweet, '10':in_reply_to_user, '11':source_app, '12':source_app_url, '13':coordinates, '14':place, '15':language, '16':contributors, '17':truncated, '18':dev_heart, '19':dev_retweet}

    try:
        cursor.execute(query, variables)
    except Error as e:
        e_string = str(e)
        if (e_string[:24] == "UNIQUE constraint failed"):
            pass
        else:
            print(e)

    insert_user(tweet.user, cursor)
    insert_hashtags(ID, hashtags, cursor)
    insert_mentions(ID, mentions, cursor, api)

    return None

def insert_user(user, cursor):
    u_id = user.id_str
    u_name = user.name
    u_handle = user.screen_name
    u_description = user.description
    u_protected = user.protected
    u_followers = user.followers_count
    u_following = user.friends_count
    u_listed = user.listed_count
    u_created_at = user.created_at
    u_favorites = user.favourites_count
    u_tweets = user.statuses_count
    u_language = user.lang
    u_contributors_enabled = user.contributors_enabled
    if hasattr(user, 'location'):
        u_location = user.location
    else:
        u_location = None
    if hasattr(user, 'url'):
        u_website = user.url
    else:
        u_website = None
    if hasattr(user, 'utc_offset'):
        u_utc_offset = user.utc_offset
    else:
        u_utc_offset = None
    if hasattr(user, 'timezone'):
        u_timezone = user.timezone
    else:
        u_timezone = None
    if user.geo_enabled == True:
        u_geo_enabled = 1
    else:
        u_geo_enabled = 0
    if user.verified == True:
        u_verified = 1
    else:
        u_verified = 0
    if user.contributors_enabled == True:
        u_contributors_enabled = 1
    else:
        u_contributors_enabled = 0
    if user.is_translator == True:
        u_is_translator = 1
    else:
        u_is_translator = 2
    if user.is_translation_enabled == True:
        u_translation_enabled = 1
    else:
        u_translation_enabled = 0
    if user.has_extended_profile == True:
        u_extended_profile = 1
    else:
        u_extended_profile = 0
    if user.default_profile == True:
        u_default_profile = 1
    else:
        u_default_profile = 0
    if user.default_profile_image == True:
        u_default_avatar = 1
    else:
        u_default_avatar = 0
    if user.following == True:
        u_dev_follow = 1
    else:
        u_dev_follow = 0
    if hasattr(user, 'translator_type'):
        u_translator_type = user.translator_type
    else:
        u_translator_type = None

    query = "INSERT INTO users VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17, :18, :19, :20, :21, :22, :23, :24, :25, :26)"

    variables = {'1':u_id, '2':u_name, '3':u_handle, '4':u_location, '5':u_description, '6':u_website, '7':u_protected, '8':u_followers, '9':u_following, '10':u_listed, '11':u_created_at, '12':u_favorites, '13':u_utc_offset, '14':u_timezone, '15':u_geo_enabled, '16':u_verified, '17':u_tweets, '18':u_language, '19':u_contributors_enabled, '20':u_is_translator, '21':u_translation_enabled, '22':u_extended_profile, '23':u_default_profile, '24':u_default_avatar, '25':u_dev_follow, '26':u_translator_type}

    try:
        cursor.execute(query, variables)
    except Error as e:
        e_string = str(e)
        if (e_string[:24] == "UNIQUE constraint failed"):
            pass
        else:
            print(e)
    return None

def insert_hashtags(tweet_ID, hashtags, cursor):
    query = "INSERT INTO hashtags VALUES(:1, :2)"
    for tag in hashtags:
        hash_text = tag['text']
        try:
            cursor.execute(query, {'1':tweet_ID, '2':hash_text})
        except Error as e:
            e_string = str(e)
            if (e_string[:24] == "UNIQUE constraint failed"):
                pass
            else:
                print(e)
    return None

def insert_mentions(tweet_ID, mentions, cursor, api):
    query = "INSERT INTO mentions VALUES(:1, :2)"
    for name in mentions:
        mention_text = name['screen_name']
        mentioned_user = api.get_user(mention_text)
        insert_user(mentioned_user, cursor)
        try:
            cursor.execute(query, {'1':tweet_ID, '2':mention_text})
        except Error as e:
            e_string = str(e)
            if (e_string[:24] == "UNIQUE constraint failed"):
                pass
            else:
                print(e)
    return None

def show_totals(cursor):
    cursor.execute("SELECT COUNT(*) FROM tweets")
    result = cursor.fetchone()
    print("Total tweets collected: " + str(result[0]))
    cursor.execute("SELECT COUNT(*) FROM users")
    result = cursor.fetchone()
    print("Total users collected: " + str(result[0]))
    cursor.execute("SELECT COUNT(*) FROM hashtags")
    result = cursor.fetchone()
    print("Total hashtags collected: " + str(result[0]))
    cursor.execute("SELECT COUNT(*) FROM mentions")
    result = cursor.fetchone()
    print("Total mentions collected: " + str(result[0]))
