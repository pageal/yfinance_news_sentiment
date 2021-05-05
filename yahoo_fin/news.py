


from datetime import datetime
from time import mktime

import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

yf_rss_ticket_url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=US&lang=en-US'
yf_rss_url = 'https://www.yahoo.com/news/rss'

def get_yf_rss():
    feed = feedparser.parse(yf_rss_url)
    return feed.entries

def get_yf_ticker_rss(ticker):
    feed = feedparser.parse(yf_rss_ticket_url % ticker)
    return feed.entries

def print_ticker_news(ticker, entry, score):
    print("\n{} TITLE: {}".format(ticker, entry['title']))
    published = entry['published_parsed']
    dt = datetime.fromtimestamp(mktime(published))
    print("   Published at " + str(dt.date()) + " " + str(dt.time()))
    print("   Score compound {}: neg: {} new: {} pos{} ".format(score['compound'], score['neg'], score['neu'], score['pos']))

def print_scored_ticker_news(entry):
    print("\n{} - {} {}: {}".format(entry['ticker'], str(entry['date']), str(entry['time']), entry['headline']))
    print("    SCORE compound: {} (neg: {} new: {} pos: {})".format(entry['compound'], entry['neg'], entry['neu'], entry['pos']))

def scan_ticker_news():
    ticker = 'INTC'
    #    entries = get_yf_rss("AAPL")
    entries = get_yf_ticker_rss(ticker)

    i = 0
    all_news = []
    for entry in entries:
        published = entry['published_parsed']
        dt = datetime.fromtimestamp(mktime(published))

        # DEBUG prints
        # print("\nSUMMARY " + str(i))
        # print("\nTITLE #" + str(i) + ":" + entry['title'])
        # print("   Publshed at " + str(dt.date()) + " " + str(dt.time()))

        news = []
        news.append(ticker)
        news.append(dt.date())
        news.append(dt.time())
        news.append(entry['title'])
        all_news.append(news)
        # print(entry['summary'])
        # print(entry)
        i = i + 1

    # Instantiate the sentiment intensity analyzer
    nltk.download("vader_lexicon")
    vader = SentimentIntensityAnalyzer()

    columns = ['ticker', 'date', 'time', 'headline']

    # Convert the parsed_news list into a DataFrame called 'parsed_and_scored_news'
    parsed_and_scored_news = pd.DataFrame(all_news, columns=columns)

    # Iterate through the headlines and get the polarity scores using vader
    scores = parsed_and_scored_news['headline'].apply(vader.polarity_scores).tolist()

    # DEBUG PRINT
    # i = 0
    # for score in scores:
    #    #print("#{} neg: {} new: {} pos{} compound {}".format(i, score['neg'], score['neu'], score['pos'], score['compound']))
    #    if score['compound'] > 0.3 or score['compound'] < -0.3:
    #        print_ticker_news(ticker, entries[i], score)
    #    i = i + 1

    # Convert the 'scores' list of dicts into a DataFrame
    scores_df = pd.DataFrame(scores)
    # Join the DataFrames of the news and the list of dicts
    parsed_and_scored_news = parsed_and_scored_news.join(scores_df, rsuffix='_right')
    # Convert the date column from string to datetime
    parsed_and_scored_news['date'] = pd.to_datetime(parsed_and_scored_news.date).dt.date

    parsed_and_scored_news.head()
    for index, news_item in parsed_and_scored_news.iterrows():
        # DEBUG PRINT
        # print(str(news_item['compound']))
        if news_item['compound'] > 0.3 or news_item['compound'] < -0.3:
            print_scored_ticker_news(news_item)


if __name__ == '__main__':
    scan_ticker_news()
