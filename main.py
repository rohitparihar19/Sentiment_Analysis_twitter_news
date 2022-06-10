import util
import Scraping


tweet_details =Scraping.scraping()
# print(tweet_details)

# Analysing News and printing results 
for news in tweet_details:
  news = str(news)
  result = util.get_tweet_sentiment(news)
  print(result)



