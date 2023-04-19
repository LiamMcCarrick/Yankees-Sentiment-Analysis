# import packages
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from twitter_scraper import twitter_scraper

# create sentiment analysis object
analyzer = SentimentIntensityAnalyzer()


def sentiment_model(query, limit):
    # gather twitter data
    player_tweets = twitter_scraper(query, limit)

    # provide sentiment score
    def score_output(output_dict):
        sent_score = "neutral"

        if output_dict["compound"] >= 0.05:
            sent_score = "positive"

        elif output_dict["compound"] <= -0.05:
            sent_score = "negative"

        return sent_score

    def predict_sentiment(tweet_content):
        sent_score = analyzer.polarity_scores(tweet_content)
        return score_output(sent_score)

    player_tweets["Sentiment Score"] = player_tweets["renderedContent"].apply(
        predict_sentiment
    )

    return player_tweets
