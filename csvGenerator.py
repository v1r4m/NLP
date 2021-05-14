
import tweepy 

import pandas as pd
import os

import sys

import csv

from konlpy.utils import pprint
from konlpy.tag import Okt


#sys.setdefaultencoding('utf-8')



consumer_key = "kZADq17e01p6ILN0u3vdgU1DH"

consumer_secret = "7bKnY3aGD1LZIDWbS6tVzru8zFZNV492oN9I51g7b6HctxC8Kb"

access_token = "266449908-riSJfN9LFhHcRlm2NNkaA2EA30JGHEZf5rBnJPZR"

access_token_secret = "BZVZx7nxSAYbsYkpCnPQLpVVlQyFMFIaZ2T49vSbPFasE"



auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)  



location = "%s,%s,%s" % ("35.95", "128.25", "1000km")  # 검색기준(대한민국 중심) 좌표, 반지름  

keyword = "중앙대 -filter:retweets"                                      # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)                             

# wfile = open(os.getcwd()+"/twitter.txt", mode='w')        # 텍스트 파일로 출력(쓰기모드)

# twitter 검색 cursor 선언
f = open('write.csv','w', newline='')
wr = csv.writer(f)

cursor = tweepy.Cursor(api.search, 

                       q=keyword,

                       since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴

                       count=300,  # 페이지당 반환할 트위터 수 최대 100

                       geocode=location,

                       include_entities=True)
okt = Okt()
for i, tweet in enumerate(cursor.items()):
    noun = okt.nouns(tweet.text)
    for i, v in enumerate(noun):
        if len(v)<2:
            noun.pop(i)
    print(noun)
    wr.writerow(noun)

keyword = "나비 -filter:retweets"
cursor = tweepy.Cursor(api.search, 

                       q=keyword,

                       since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴

                       count=300,  # 페이지당 반환할 트위터 수 최대 100

                       geocode=location,

                       include_entities=True)
for i, tweet in enumerate(cursor.items()):
    noun = okt.nouns(tweet.text)
    for i, v in enumerate(noun):
        if len(v)<2:
            noun.pop(i)
    print(noun)
    wr.writerow(noun)

f.close()

#twitter_df = pd.DataFrame(tweet_list

#    wfile.write(tweet.text + '\n')

#wfile.close()

#https://liveyourit.tistory.com/57
#https://wikidocs.net/43280
#https://jeongwookie.github.io/2019/06/10/190610-twitter-data-crawling/