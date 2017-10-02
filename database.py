import sqlite3

conn = sqlite3.connect('twitter.db')
curs = conn.cursor()

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
                    mutuals integer NOT NULL,
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
                    tweet_id text NOT NULL REFERENCES tweets(id) ON UPDATE CASCADE,
                    hashtag text NOT NULL,
                    PRIMARY KEY(tweet_id, hashtag)
                )""")

curs.execute("""CREATE TABLE
                IF NOT EXISTS mentions (
                    tweet_id text NOT NULL REFERENCES tweets(id) ON UPDATE CASCADE,
                    mention_handle text NOT NULL REFERENCES users(handle) ON UPDATE CASCADE,
                    PRIMARY KEY (tweet_id, mention_handle)
                )""")

# curs.execute("""INSERT INTO tweets (
#                 time_posted,
#                 id,
#                 tweet_text,
#                 truncated,
#                 source_app,
#                 source_app_url,
#                 user_id,
#                 retweeted_id,
#                 retweets,
#                 hearts,
#                 dev_heart,
#                 dev_retweet,
#                 language)
#               VALUES (
#                 '2017-09-27 20:42:11',
#                 '913141742299500545',
#                 'RT @cgartenberg: https://t.co/YZ8YK9MjCE',
#                 0,
#                 'TweetDeck',
#                 'https://about.twitter.com/products/tweetdeck',
#                 '717768811005526016',
#                 '989895654512365845',
#                 15,
#                 0,
#                 0,
#                 0,
#                 'und');""")

# curs.execute("SELECT * FROM tweets")
# print(curs.fetchall())

conn.commit()

conn.close()
