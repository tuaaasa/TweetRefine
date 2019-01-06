# -*- coding:utf-8 -*- 
import json
import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session

from .config import twitter as twitter_config


class RefineTweets:
    def __init__(self, validated_data):
        # config.pyからキーとトークンを取得
        consumer_key, consumer_secret, access_token, access_token_secret = twitter_config()
        # セッション
        self.twitter = OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)

        # Tweet's API'sの設定
        self.url = "https://api.twitter.com/1.1/search/tweets.json"
        self.query = '#SoundCloud OR itunes filter:links from:'
        self.screen_name = validated_data['screen_name']
        self.id = validated_data['id']

    def refine(self):
        params ={'q': self.query+self.screen_name,'count': 3}
        req = self.twitter.get(self.url, params = params)

        if req.status_code == 200:
            timeline = json.loads(req.text)
            refine_tweets = []
            for tweet in timeline['statuses']:
                # Twitter Cardっぽいのに必要な要素を取得
                resp = requests.get(tweet['entities']['urls'][0]['expanded_url'])
                soup = BeautifulSoup(resp.content, 'html.parser')
                title = soup.find("meta",  property="og:title")
                image_url = soup.find("meta", property="og:image")
                # 配列に格納
                refine_tweets.append({
                    'url': tweet['entities']['urls'][0]['expanded_url'],
                    'created_at': tweet['created_at'],
                    'image_url': image_url['content'],
                    'title': title['content'],
                    'account': self.id
                })
            return refine_tweets
        else:
            # print("ERROR: %d" % req.status_code)
            return []