# import packages
import pandas as pd
from sentiment_analysis import sentiment_model

# define parameters
adv_search = '"yankees" "volpe" OR "donaldson" OR "judge" OR "falefa" OR "ikf" OR "hicks" lang:en until:2023-04-18 since:2023-04-04'
test_search = '"yankees" "hicks" lang:en until:2023-04-18 since:2023-04-04'
max_search = 50000
test_max = 10

tweet_collection = sentiment_model(test_search, test_max)

print(tweet_collection)

tweet_collection.to_csv("player_tweets.csv")
