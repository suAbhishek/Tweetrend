import twitter
#import pythontwitter
import util
from config import *

BOSTON_WOEID = 2367105
api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)

def search(searchTerm):
   
    api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)
    tweets = api.GetSearch(searchTerm)
    for tweet in tweets:
        util.safe_print(tweet.GetText())

def trendingTopics():
    """
    Print the currently trending topics.

    To test this function on terminal, python twitter_api.py -t
    """
    api = twitter.Api(consumer_key=key,consumer_secret=secret,access_token_key=access_key,access_token_secret=access_secret)
    trending_topics = api.GetTrendsWoeid(BOSTON_WOEID)
    for topic in trending_topics:
        util.safe_print(topic.name)

def trendingTweets():
    """
    Print tweets for all the trending topics.

    To test this function: python twitter_api.py -w
    """
    trends1 = api.trends_place(1
    data = trends1[0]   
    # grab the trends
    trends = data['trends']
    # grab the name from each trend
    names = [trend['name'] for trend in trends]
    # put all the names together with a ' ' separating them
    trendsName = ' '.join(names)
    print(trendsName)
    pass
