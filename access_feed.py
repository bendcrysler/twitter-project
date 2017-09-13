import tweepy
import io

# Lines 4-13 authenticate this script with author's registered twitter application and account."""
consumer_key = 'AhqRDo5NYd2XRP3G3apZar7JC'
consumer_secret = 'jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO'

access_token = '68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd'
access_secret = 'vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# API calls that collect tweets
trump_tweets = api.search('Trump')
home_timeline = api.home_timeline(count=25)

# opening file for printing, utf-8 necessary for processing emoji
output_file = io.open("results.txt", "w", encoding="utf-8")

desired_properties = range(47)

def getTweetInfo(tweet_set,indicies):
    # takes a tweet set and a set of indexes that reference tweet properties
    for tweet in tweet_set:
        for index in indicies:
            if index == 0:
                output_file.write("Tweet Created At: " + (str(tweet.created_at)))
            elif index == 1:
                output_file.write("Tweet ID: " + tweet.id_str)
            elif index == 2:
                output_file.write("Tweet Text: " + tweet.text)
            elif index == 3:
                output_file.write("Tweet Truncated?: " + str(tweet.truncated))
            elif index == 4:
                hashtags = tweet.entities['hashtags']
                if len(hashtags) > 0:
                    output_file.write("Tweet Hashtags: ")
                    for tag in hashtags:
                        output_file.write("#" + tag['text'] + " ")
            # TODO: remaining entities(media,urls,user_mentions)
            elif index == 5:
                output_file.write("Tweet Source App: " + tweet.source)
            elif index == 6:
                output_file.write("Tweet Source App URL: " + tweet.source_url)
            elif index == 7:
                reply_to_status_id = tweet.in_reply_to_status_id_str
                if not reply_to_status_id == None:
                    output_file.write("In Reply to Tweet ID: " + reply_to_status_id)
            elif index == 8:
                reply_to_user_id = tweet.in_reply_to_user_id_str
                if not reply_to_user_id == None:
                    output_file.write("In Reply to User ID: " + reply_to_user_id)
            elif index == 9:
                output_file.write("User ID: " + tweet.user.id_str)
            elif index == 10:
                output_file.write("User Name: " + tweet.user.name)
            elif index == 11:
                output_file.write("User Handle: @" + tweet.user.screen_name)
            elif index == 12:
                output_file.write("User Location: " + tweet.user.location)
            elif index == 13:
                output_file.write("User Description: " + tweet.user.description)
            elif index == 14:
                user_site = tweet.user.url
                if not tweet.user.url == None:
                    output_file.write("User Website: " + tweet.user.url)
            elif index == 15:
                output_file.write("User Protected?: " + str(tweet.user.protected))
            elif index == 16:
                output_file.write("User Followers: " + str(tweet.user.followers_count))
            elif index == 17:
                output_file.write("User Friends: " + str(tweet.user.friends_count))
            elif index == 18:
                output_file.write("User Listed Count: " + str(tweet.user.listed_count))
            elif index == 19:
                output_file.write("User Created At: " + str(tweet.user.created_at))
            elif index == 20:
                output_file.write("User Favorites: " + str(tweet.user.favourites_count))
            elif index == 21:
                output_file.write("User UTC Offset: " + str(tweet.user.utc_offset))
            elif index == 22:
                timezone = tweet.user.time_zone
                if not timezone == None:
                    output_file.write("User Timezone: " + timezone)
            elif index == 23:
                output_file.write("User Geo Enabled?: " + str(tweet.user.geo_enabled))
            elif index == 24:
                output_file.write("User Verified?: " + str(tweet.user.geo_enabled))
            elif index == 25:
                output_file.write("User Tweets Count: " + str(tweet.user.statuses_count))
            elif index == 26:
                output_file.write("User Language: " + tweet.user.lang)
            elif index == 27:
                output_file.write("User Contributors Enabled?: " + str(tweet.user.contributors_enabled))
            elif index == 28:
                output_file.write("User Translator?: " + str(tweet.user.is_translator))
            elif index == 29:
                output_file.write("User Translation Enabled?: " + str(tweet.user.is_translation_enabled))
            elif index == 30:
                output_file.write("User Has Extended Profile?: " + str(tweet.user.has_extended_profile))
            elif index == 31:
                output_file.write("User Has Default Profile?: " + str(tweet.user.default_profile))
            elif index == 32:
                output_file.write("User Has Default Avatar?: " + str(tweet.user.default_profile_image))
            elif index == 33:
                output_file.write("User Followed By Developer?: " + str(tweet.user.following))
            elif index == 34:
                output_file.write("User Translator Type: " + tweet.user.translator_type)
            elif index == 35:
                geo = tweet.geo
                if not geo == None:
                    output_file.write("Tweet Geo: " + str(geo))
            elif index == 36:
                coord = tweet.coordinates
                if not coord == None:
                    output_file.write("Tweet Coordinates: " + str(coord))
            elif index == 37:
                place = tweet.place
                if not place == None:
                    output_file.write("Tweet Place: " + str(place))
            elif index == 38:
                contrib = tweet.contributors
                if not contrib == None:
                    output_file.write("Tweet Contributors: " + str(contrib))
            elif index == 39:
                if hasattr(tweet, 'retweeted_status'):
                    output_file.write("Retweeted Tweet Text: " + tweet.retweeted_status.text)
            #TODO: finish retweet functionality
            elif index == 40:
                output_file.write("Quoted Status?: " + str(tweet.is_quote_status))
            elif index == 41:
                if tweet.is_quote_status == True:
                    output_file.write("Quoted Status ID: " + tweet.quoted_status_id_str)
            #TODO: finish quote functionality
            elif index == 42:
                output_file.write("Tweet Retweets: " + str(tweet.retweet_count))
            elif index == 43:
                output_file.write("Tweet Favorites: " + str(tweet.favorite_count))
            elif index == 44:
                output_file.write("Tweet Favorited by Developer?: " + str(tweet.favorited))
            elif index == 45:
                output_file.write("Tweet Retweeted by Developer?: " + str(tweet.retweeted))
            elif index == 46:
                output_file.write("Tweet Language: " + tweet.lang)
            output_file.write("\n")
        output_file.write("-----------------------------------------------------\n")

def retweetSniffer(tweet_set):
    for tweet in tweet_set:
        if hasattr(tweet, 'retweeted_status'):
            print(tweet.retweeted_status.text)
        else:
            print("not retweet")

getTweetInfo(home_timeline, desired_properties)
getTweetInfo(trump_tweets, desired_properties)

# retweetSniffer(home_timeline)

output_file.close()
