


from datetime import datetime
from time import mktime

import feedparser
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import nltk

csvDataFrameColumns = None
csvDataArray = []

yf_rss_ticket_url = 'https://feeds.finance.yahoo.com/rss/2.0/headline?s=%s&region=US&lang=en-US'
yf_rss_url = 'https://finance.yahoo.com/news/rssindex'

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

def print_scored_news(entry):
    print("\n{} {}: {}".format(str(entry['date']), str(entry['time']), entry['headline']))
    print("    SCORE compound: {} (neg: {} new: {} pos: {})".format(entry['compound'], entry['neg'], entry['neu'], entry['pos']))

def scan_yf_news(score_threshold = 0.3, ticker = 'INTC'):
    global csvDataFrameColumns
    if(ticker != None):
        entries = get_yf_ticker_rss(ticker)
    else:
        entries = get_yf_rss()

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
        if (ticker != None):
            news.append(ticker)
        else:
            news.append("")
        news.append(dt.date())
        news.append(dt.time())
        news.append(entry['title'])
        all_news.append(news)
        # print(entry['summary'])
        # print(entry)
        i = i + 1


    columns = ['ticker', 'date', 'time', 'headline']

    # Instantiate the sentiment intensity analyzer
    nltk.download("vader_lexicon")
    vader = SentimentIntensityAnalyzer()
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
    if csvDataFrameColumns is None:
        csvDataFrameColumns = parsed_and_scored_news.columns
    for index, news_item in parsed_and_scored_news.iterrows():
        # DEBUG PRINT
        # print(str(news_item['compound']))
        if news_item['compound'] > score_threshold or news_item['compound'] < (-1*score_threshold):
            csvDataArray.append(news_item.tolist())
            if (ticker != None):
                print_scored_ticker_news(news_item)
            else:
                print_scored_news(news_item)


from tickers import tickers_pg

if __name__ == '__main__':
    dt_now = datetime.now()
    dt_string = dt_now.strftime("%Y%m%d_%H%M%S")

    scan_yf_news(score_threshold=0.65, ticker=None)
    #scan_yf_news(ticker='INTC')

    for ticker in tickers_pg:
        scan_yf_news(score_threshold=0.65, ticker=ticker)
    csvDataFrame = pd.DataFrame(csvDataArray, columns=csvDataFrameColumns)
    csvDataFrame.to_csv("C:/Users/USER/Downloads/yahoo_fin_news/" +dt_string+".csv")


