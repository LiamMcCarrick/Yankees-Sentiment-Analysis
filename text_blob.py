# import packages
import pandas as pd
import re
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from twitter_scraper import twitter_scraper

# download stop words list
nltk.download("stopwords")


# create sentiment model
def sentiment_model(query, limit):
    # gather twitter data
    player_tweets = twitter_scraper(query, limit)

    # provide sentiment score
    def clean_text(text):
        ex_list = ["rt", "http", "RT"]
        exc = "|".join(ex_list)
        text = re.sub(exc, " ", text)
        text = text.lower()
        words = text.split()
        stopword_list = stopwords.words("english")
        words = [word for word in words if not word in stopword_list]
        clean_text = " ".join(words)
        return clean_text

    # assign sentiment score to tweet
    def sentiment_score(text):
        analysis = TextBlob(text)
        if analysis.sentiment.polarity > 0:
            return 1
        elif analysis.sentiment.polarity == 0:
            return 0
        else:
            return -1

    # remove stop words from tweet content
    player_tweets["Clean text"] = player_tweets["renderedContent"].apply(clean_text)
    # add sentiment score to data frame
    player_tweets["Score"] = player_tweets["Clean text"].apply(sentiment_score)

    return player_tweets
