# import packages
import itertools
import pandas as pd
import snscrape.modules.twitter as sntwitter


# create scraper function
def twitter_scraper(query, limit):
    # create tweets list
    scraped_tweets = sntwitter.TwitterSearchScraper(query).get_items()

    # slicing the generator to keep only the first n tweets
    sliced_scraped_tweets = itertools.islice(scraped_tweets, limit)

    # storing each tweet in a dataframe
    df = pd.DataFrame(sliced_scraped_tweets)[
        [
            "date",
            "renderedContent",
            "retweetCount",
            "likeCount",
            "quoteCount",
            "viewCount",
        ]
    ]

    return df
