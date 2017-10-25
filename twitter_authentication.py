import tweepy

class Keys:
    consumer_key = "AhqRDo5NYd2XRP3G3apZar7JC"
    consumer_secret = "jXlQVdMOYucOBiO6iXsmgH4ApyBfsjCSw37fjmuiToAr6dCiFO"
    access_token = "68715828-WHXCGw6z3cLDj2EtudBqPggJWVSfCtHUkPra1SAjd"
    access_token_secret = "vToagD83gYPHeGKqC9yBdUvFdcLh4KTl5ckqkmsMYX5FV"

    def authenticate (self):
        auth = tweepy.OAuthHandler(Keys.consumer_key, Keys.consumer_secret)
        auth.set_access_token(Keys.access_token, Keys.access_token_secret)
        api = tweepy.API(auth)
        return api
