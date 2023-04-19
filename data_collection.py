# import packages
import pandas as pd
from sentiment_analysis import sentiment_model

# define parameters
juddge_search = '"yankees" "judge" lang:en until:2023-04-18 since:2023-03-30'
volpe_search = '"yankees" "volpe" lang:en until:2023-04-18 since:2023-03-30'
donaldson_search = '"yankees" "donaldson" lang:en until:2023-04-18 since:2023-03-30'
ikf_search = '"yankees" "falefa" OR "ikf" lang:en until:2023-04-18 since:2023-03-30'
hicks_search = '"yankees" "hicks" lang:en until:2023-04-18 since:2023-03-30'
max_search = 45000

# export each player tweets to csv
tweet_judge = sentiment_model(juddge_search, max_search)
tweet_judge.to_csv("judge_tweets.csv")

tweet_volpe = sentiment_model(volpe_search, max_search)
tweet_volpe.to_csv("volpe_tweets.csv")

tweet_donaldson = sentiment_model(donaldson_search, max_search)
tweet_donaldson.to_csv("donaldson_tweets.csv")

tweet_ikf = sentiment_model(ikf_search, max_search)
tweet_ikf.to_csv("ikf_tweets.csv")

tweet_hicks = sentiment_model(hicks_search, max_search)
tweet_hicks.to_csv("hicks_tweets.csv")
