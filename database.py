import sqlite3

conn = sqlite3.connect('twitter.db')
curs = conn.cursor()

curs.execute("""CREATE TABLE
                IF NOT EXISTS tweets (
                    time_posted text NOT NULL,
                    id text PRIMARY KEY,
                    tweet_text text NOT NULL,
                    truncated integer NOT NULL,

                    source_app text NOT NULL,
                    source_app_url text NOT NULL,
                    language text NOT NULL,
                    hearts integer NOT NULL,
                    retweets integer NOT NULL,

                    place text,
                    coordinates text,
                    geo text,
                    contributors text,
                
                    dev_heart integer NOT NULL,
                    dev_retweet integer NOT NULL,

                )""")

conn.commit()

conn.close()
