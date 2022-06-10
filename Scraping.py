import twitter_api
import tweepy as tw
from tweepy import OAuthHandler

config = twitter_api.upload()

# Defining twitter API key to use later for authentication
def access():
    accesstoken = config.get('twitter','accesstoken') 
    accesstokensecret = config.get('twitter','accesstokensecret') 
    apikey = config.get('twitter','apikey') 
    apisecretkey = config.get('twitter','apisecretkey')
    return accesstoken,accesstokensecret,apikey,apisecretkey

# Authentication
def authentication(accesstoken,accesstokensecret,apikey,apisecretkey):
    auth = tw.OAuthHandler(apikey,apisecretkey) 
    auth.set_access_token(accesstoken,accesstokensecret) 
    api = tw.API(auth,wait_on_rate_limit=True)
    return api

#Scrapping the News headlines using tweepy 
def scraping():
    accesstoken,accesstokensecret,apikey,apisecretkey = access()
    api = authentication(accesstoken,accesstokensecret,apikey,apisecretkey)
    search_word = '#news' 
    tweets = tw.Cursor(api.search_tweets,q = search_word, lang ='en').items(100)
    tweet_details = [[tweet.text]for tweet in tweets]
    return tweet_details

# tweet_details=scraping()
# print(tweet_details)
