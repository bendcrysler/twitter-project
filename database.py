import sqlite3

conn = sqlite3.connect('twitter.db')
curs = conn.cursor()

curs.execute("""CREATE TABLE
                IF NOT EXISTS tweets (
                    time_posted text NOT NULL,
                    id text PRIMARY KEY NOT NULL,
                    tweet_text text NOT NULL,
                    truncated integer NOT NULL,
                    source_app text NOT NULL,
                    source_app_url text NOT NULL,
                    in_reply_to_id text,
                    in_reply_to_user text,
                    user_id text NOT NULL REFERENCES users(id) ON UPDATE CASCADE,
                    language text NOT NULL,
                    hearts integer NOT NULL,
                    retweets integer NOT NULL,
                    place text,
                    coordinates text,
                    geo text,
                    contributors text,
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
conn.commit()

conn.close()
