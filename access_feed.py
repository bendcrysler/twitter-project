import tweepy

# Lines 4-13 authenticate this script with author's registered twitter application and account."""
consumer_key = 'AhqRDo5NYd2XRP3G3apZar7JC'
consumer_secret = 'jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO'

access_token = '68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd'
access_secret = 'vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Examples of API calls
trump_tweets = api.search('Trump')
home_timeline = api.home_timeline(count=1)

output_file = open("results.txt", "w")

for tweet in home_timeline:
    output_file.write(tweet.id_str)
    output_file.write("\n")
    output_file.write(tweet.user.name)
    output_file.write("\n")
    output_file.write(tweet.text)
    output_file.write("\n")
    output_file.write(tweet.source)
    output_file.write("\n")
    output_file.write(tweet.source_url)
    output_file.write("\n")
    # output_file.write(tweet.created_at)

output_file.close()
