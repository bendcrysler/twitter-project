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

desired_properties = [10,11,2,17]

def getTweetInfo(tweet_set,indicies):
    # takes a tweet set and a set of indexes that reference tweet properties
    for tweet in tweet_set:
        for index in indicies:
            if index == 0:
                output_file.write("Created At: " + (str(tweet.created_at)) + "\n")
            elif index == 1:
                output_file.write("ID: " + tweet.id_str + "\n")
            elif index == 2:
                output_file.write("Text: " + tweet.text + "\n")
            elif index == 3:
                output_file.write("Truncated: " + str(tweet.truncated) + "\n")
            elif index == 4:
                # TODO: break entities up
                output_file.write("Entities: " + str(tweet.entities) + "\n")
            elif index == 5:
                output_file.write("Source App: " + tweet.source + "\n")
            elif index == 6:
                output_file.write("Source App URL: " + tweet.source_url + "\n")
            elif index == 7:
                reply_to_status_id = tweet.in_reply_to_status_id_str
                if not reply_to_status_id == None:
                    output_file.write("In Reply to ID: " + reply_to_status_id + "\n")
                else:
                    output_file.write("not a reply\n")
            elif index == 8:
                reply_to_user_id = tweet.in_reply_to_user_id_str
                if not reply_to_user_id == None:
                    output_file.write("In Reply to User ID: " + reply_to_user_id + "\n")
                else:
                    output_file.write("not a reply\n")
            elif index == 9:
                output_file.write("User ID: " + tweet.user.id_str + "\n")
            elif index == 10:
                output_file.write("User Name: " + tweet.user.name + "\n")
            elif index == 11:
                output_file.write("User Handle: @" + tweet.user.screen_name + "\n")
            elif index == 12:
                output_file.write("User Location: " + tweet.user.location + "\n")
            elif index == 13:
                output_file.write("User Description: " + tweet.user.description + "\n")
            elif index == 14:
                user_site = tweet.user.url
                if not tweet.user.url == None:
                    output_file.write("User Website: " + tweet.user.url + "\n")
                else:
                    output_file.write("User does not supply site")
            elif index == 15:
                output_file.write("User Protected?: " + str(tweet.user.protected) + "\n")
            elif index == 16:
                output_file.write("User Followers: " + str(tweet.user.followers_count) +"\n")
            elif index == 17:
                output_file.write("User Friends: " + str(tweet.user.friends_count) + "\n")
            else:
                print ("invalid index")



        output_file.write("-----------------------------------------------------\n")

getTweetInfo(home_timeline, desired_properties)

output_file.close()
