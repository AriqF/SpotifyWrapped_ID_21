import tweepy
import csv
import pandas as pd
import re

access_token=""
access_token_secret=""
consumer_key=""
consumer_key_secret=""

auth = tweepy.OAuthHandler(consumer_key,consumer_key_secret)
api = tweepy.API(auth)

csvFile = open('spotifyDataset.csv', 'w', encoding='utf-8')
csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search_tweets, q='#SpotifyWrapped -filter:retweets', tweet_mode='extended',lang="id").items(5000):
    text = tweet.full_text
    user = tweet.user.name
    created = tweet.created_at
    csvWriter.writerow([created, text.encode('utf-8'), user])
csvWriter = csv.writer(csvFile)
csvFile.close()

df = pd.read_csv('spotifyDataset.csv')
headerList = ['created_at', 'text', 'username']
rm = ["b'","\n"]
df = df.replace('|'.join(rm),'', regex=True)

df.to_csv('spotifyDataset.csv', header=headerList, index=False)