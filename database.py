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
                    in_reply_to_id text REFERENCES tweets(id),
                    in_reply_to_user text REFERENCES users(id),
                    user_id text NOT NULL REFERENCES users(id) ON UPDATE CASCADE,
                    geo text,
                    coordinates text,
                    place text,
                    contributors text,
                    retweeted_id text REFERENCES tweets(id),
                    quoted_id text REFERENCES tweets(id),
                    retweets integer NOT NULL,
                    hearts integer NOT NULL,
                    dev_heart integer NOT NULL,
                    dev_retweet integer NOT NULL,
                    language text NOT NULL
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
conn.commit()

conn.close()
