# Yankees-Sentiment-Analysis Project Overview
*   Scraped twitter to analyze fan discourse on certain Yankee players
*   Gathered 25,000 tweets since the beginning of the season on 5 different Yankee players
*   Josh Donaldson has a 63% positive/neutral sentiment score
*   Aaron Judge has an 82% positive/neutral sentiment score
*   Model results deployed along with visualizations in tableau dashboard

## Code and Resources Used
**Python Version:** 3.9.7           
**Scraper Information:**            
https://medium.com/analytics-vidhya/how-i-built-a-twitter-dashboard-4d5d0e53c36c            
https://medium.com/swlh/how-to-scrape-tweets-by-location-in-python-using-snscrape-8c870fa6ec25          
**Sentiment Analysis Information:**             
https://towardsdatascience.com/social-media-sentiment-analysis-in-python-with-vader-no-training-required-4bc6a21e87b8

## Dashboard Link
**Tableau Portfolio:**          
https://public.tableau.com/app/profile/william.mccarrick/viz/YankeePlayerSentimentDashboard/YankeesPlayerSentimentDashboard

## Web Scraping
There are two available options to get twitter data: utilze the twitter API or scrape the data. The free account of twitter developer doesn't allow you to search for tweets so I had to use snscarpe to scrape twitter. The search returned tweets that mentioned the players in question from the start of the season to the current point in time.            
Here is the data collected from each tweet:
*   date
*   renderedContent
*   retweetCount
*   likeCount
*   quoteCount
*   viewCount           

I was able to scrape 25,000 tweets since the start of the 2023 MLB season on five different Yankees players: Aaron Judge, Anthony Volpe, Aaron hicks, Josh Donaldson and Isiah Kiner-Falefa. I chose these players as Judge is the new Yankee captain, Volpe is the number one overall prospect for the Yankees and hicks, donaldson and ikf have been under the most scrutiny from the media.

## Sentiment Analysis
To perfrom the sentiment analysis I could either use text blob or VADER. As we are looking at twitter data, I decided to use VADER as this model has been trained to specifically test social media data. As taken from the sentiment analysis link above, the underlying score is represented as the following:           
*   a positive sentiment, compound ≥ 0.05
*   a negative sentiment, compound ≤ -0.05
*   a neutral sentiment, the compound is between [-0.05, 0.05]          

The scores were converted to the texts "positive", "negative", "ueutral".
The percentage of each positive/neutral and negative scores for each player was computed in tableu. Here are the results for each player:           
*   **Aaron Judge:** 81.43% positive/neutral, 18.57% negative
*   **Anthony Volpe:** 82.48% positive/neutral, 17.52% negative
*   **Aaron Hicks:** 68.36% positive/neutral, 31.64% negative
*   **Isiah Kiner-Falefa:** 68.71% positive/neutral, 31.29% negative
*   **Josh Donaldson:** 63.04% positive/neutral, 36.96% negative

## Productionization
I deployed the model results in a tableau dashboard along with various visualizations and KPIs like the weekly trends of positive, negative and neutral tweets for each player and number of tweets during each day of the week. A screenshot of the dashboard can be seen below.           
<img src="https://github.com/LiamMcCarrick/Yankees-Sentiment-Analysis/blob/main/Dashboard_Screenshot.PNG" width="700" height="500">         
The dashboard can be interacted with at the following link :            
https://public.tableau.com/app/profile/william.mccarrick/viz/YankeePlayerSentimentDashboard/YankeesPlayerSentimentDashboard