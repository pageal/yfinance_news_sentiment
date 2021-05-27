- main is 
   + at yahoo_fin/news.py for Yahoo Finance flow
   + at yahoo_fin/news.py for free cache flow
- developed in PyCharm
- libs to install in PyCharm to have this working:
   * feedparser
   * nltk
   * pandas
   * numpy

Example results for INTC (note how positive or negative compound scores match the corresponding news):
C:\Users\USER\AppData\Local\Programs\Python\Python39-32\python.exe C:/Users/USER/Downloads/yahoo_fin-0.8.8/yahoo_fin/news.py
[nltk_data] Downloading package vader_lexicon to
[nltk_data]     C:\Users\USER\AppData\Roaming\nltk_data...
[nltk_data]   Package vader_lexicon is already up-to-date!

2021-05-04 17:38:31: Treasury Secretary Janet Yellen calls estimated $7 trillion tax gap 'shocking and distressing'
    SCORE compound: -0.5574 (neg: 0.314 new: 0.581 pos: 0.105)

2021-05-04 22:38:54: Five Best Chinese Stocks To Buy And Watch Now
    SCORE compound: 0.6369 (neg: 0.0 new: 0.656 pos: 0.344)

2021-05-03 21:10:35: Warren Buffett Buys More Of His New Favorite Stock, Confirms Successor
    SCORE compound: 0.5994 (neg: 0.0 new: 0.647 pos: 0.353)

2021-05-05 03:32:40: Jessica  Alba’s Honest Co., Investors Raise $413 Million in IPO
    SCORE compound: 0.5106 (neg: 0.0 new: 0.732 pos: 0.268)

2021-05-04 22:54:00: Teladoc Stock is Down Another 8% This Week. Don’t Just Blame Poor Earnings.
    SCORE compound: -0.6705 (neg: 0.333 new: 0.667 pos: 0.0)

2021-05-04 22:11:03: Biden Tax Rule Would Rip Billions From Big Fortunes at Death
    SCORE compound: -0.5994 (neg: 0.281 new: 0.719 pos: 0.0)

2021-05-04 21:53:04: These Are The 5 Best Stocks To Buy And Watch Now
    SCORE compound: 0.6369 (neg: 0.0 new: 0.682 pos: 0.318)

2021-05-03 16:37:00: My employer paid me in crypto. It rose 700% in value. Now he wants employees to return the crypto and accept dollars
    SCORE compound: 0.6124 (neg: 0.0 new: 0.8 pos: 0.2)

2021-05-03 17:14:30: Rich Americans switch up money plans to soften Biden's proposed tax hikes
    SCORE compound: 0.5574 (neg: 0.0 new: 0.753 pos: 0.247)

2021-05-03 14:21:24: Robinhood responds to Buffett and Munger after they 'insulted new generation' of investors
    SCORE compound: -0.5106 (neg: 0.216 new: 0.784 pos: 0.0)
[nltk_data] Downloading package vader_lexicon to
[nltk_data]     C:\Users\USER\AppData\Roaming\nltk_data...
[nltk_data]   Package vader_lexicon is already up-to-date!

INTC - 2021-05-05 05:00:00: Europe Looks to Secure Chip Supply After ‘Naive’ Past Approach
    SCORE compound: 0.34 (neg: 0.0 new: 0.789 pos: 0.211)

INTC - 2021-05-04 13:39:42: Intel Announces Massive Investments In Improving Its Products
    SCORE compound: 0.4215 (neg: 0.0 new: 0.714 pos: 0.286)

INTC - 2021-05-04 01:45:00: Intel: $3.5 billion investment at New Mexico facility is critical to microchip future
    SCORE compound: -0.3182 (neg: 0.161 new: 0.839 pos: 0.0)

INTC - 2021-05-03 23:36:00: Intel to Invest $3.5 Billion to Expand New Mexico Manufacturing Operations
    SCORE compound: 0.3182 (neg: 0.0 new: 0.813 pos: 0.187)

INTC - 2021-05-03 18:29:54: Intel, TSM Anticipate Semiconductor Crisis To Extend Beyond 2021: Bloomberg
    SCORE compound: -0.5267 (neg: 0.297 new: 0.58 pos: 0.123)

INTC - 2021-05-03 12:45:00: Qualcomm's Quarterly Results Portend Good Things for the Semiconductor Industry
    SCORE compound: 0.4404 (neg: 0.0 new: 0.756 pos: 0.244)

INTC - 2021-05-03 01:28:00: Intel CEO stresses more U.S. chip production, fewer stock buybacks
    SCORE compound: -0.4588 (neg: 0.25 new: 0.75 pos: 0.0)

Process finished with exit code 0
