import snscrape.modules.twitter as sntwitter
import pandas as pd
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
import json
query = "Rajinikanth"
for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    print(vars(tweet))
    break
limit = 10
tweets = []

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    if len(tweets) == limit:
       break
    else:
        tweets.append([tweet.date,tweet.id,tweet.url,tweet.content,tweet.user.username,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount])

df = pd.DataFrame(tweets, columns=['Date', 'ID', 'URL','CONTENT','USER','REPLYCOUNT','RETWEETCOUNT','LANGUAGE','SOURCE','LIKES'])
print(df)

json=df.to_json('scraped-tweets.json', orient='records', lines=True)
print(json)

