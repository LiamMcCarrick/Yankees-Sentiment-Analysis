# import packages
import tweepy
import pandas as pd
import numpy as np
from secrets_key import consumer_key, consumer_secret, access_token, access_secret

# define variables
tweetsPerQry = 100
maxTweets = 1500
keyword = "yankees"

# authenticate twitter project
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_secret)
api = tweepy.API(
    authentication, wait_on_rate_limit=True, wait_on_rate_limit_notify=True
)
maxId = -1
tweetCount = 0

meta_list = []

# scrape twitter for tweets with keyword
while tweetCount < maxTweets:
    if maxId <= 0:
        newTweets = api.search(
            q=keyword, count=tweetsPerQry, result_type="recent", tweet_mode="extended"
        )
    else:
        newTweets = api.search(
            q=keyword,
            count=tweetsPerQry,
            max_id=str(maxId - 1),
            result_type="recent",
            tweet_mode="extended",
        )

    if not newTweets:
        print("Done")
        break

    # store pulled tweets
    for tweet in newTweets:
        username = tweet.user.name
        created_at = str(tweet.created_at)
        tweet_text = tweet.full_text
        tweet_text_sent = tweet.full_text
        retweet_count = tweet.retweet_count
        fav_count = tweet.favorite_count
        media_source = tweet.source
        data_dict = {
            "username": username,
            "created_at": created_at,
            "tweet_text": tweet_text,
            "retweet_count": retweet_count,
            "fav_count": fav_count,
            "media_source": media_source,
        }
        meta_list.append(data_dict)
    tweetCount += len(newTweets)
    maxId = newTweets[-1].id

print(meta_list)
