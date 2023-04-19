# import packages
import pandas as pd
import numpy as np
from twitter_scraper import twitter_scraper

# define parameters
adv_search = '"yankees" "volpe" OR "donaldson" OR "judge" OR "falefa" OR "ikf" OR "hicks" lang:en until:2023-04-18 since:2023-04-04'
test_search = '"iron man" OR "tony stark"'
max_search = 50000
test_max = 10

player_tweets = twitter_scraper(adv_search, test_max)

print(player_tweets)
