


from datetime import datetime
from time import mktime

import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

yf_rss_url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=US&lang=en-US'
#yf_rss_url = 'https://www.yahoo.com/news/rss'

def get_yf_rss(ticker):

    feed = feedparser.parse(yf_rss_url % ticker)
#    feed = feedparser.parse(yf_rss_url)

    return feed.entries

if __name__ == '__main__':
    ticker = 'INTC'
#    entries = get_yf_rss("AAPL")
    entries = get_yf_rss(ticker)

    i = 0
    all_news = []
    for entry in entries:
        #print("\nSUMMARY " + str(i))
        print("\nTITLE #" + str(i) + ":" + entry['title'])
        published = entry['published_parsed']
        dt = datetime.fromtimestamp(mktime(published))
        print("   Publshed at " + str(dt.date()) + " " + str(dt.time()))
        news = []
        news.append(ticker)
        news.append(dt.date())
        news.append(dt.time())
        news.append(entry['title'])
        all_news.append(news)
        #print(entry['summary'])
        #print(entry)
        i = i+1

    # Instantiate the sentiment intensity analyzer
    nltk.download("vader_lexicon")
    vader = SentimentIntensityAnalyzer()

    columns = ['ticker', 'date', 'time', 'headline']

    # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
    parsed_and_scored_news = pd.DataFrame(all_news, columns=columns)

    # Iterate through the headlines and get the polarity scores using vader
    scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()

    i = 0
    for score in scores:
        print("#{} neg: {} new: {} pos{} compound {}".format(i, score['neg'], score['neu'], score['pos'], score['compound']))
        i = i + 1
