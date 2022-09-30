
from asyncio.windows_events import NULL
import tweepy 

import pandas as pd
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nlpdjango.settings")
import django
django.setup()
from tweet.models import Post, LatestLink

import sys

import csv

from konlpy.utils import pprint
from konlpy.tag import Okt

import config


#sys.setdefaultencoding('utf-8')




auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)  

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

location = "%s,%s,%s" % ("35.95", "128.25", "1000km")  # 검색기준(대한민국 중심) 좌표, 반지름  

keyword = "중앙대 -filter:retweets"                                      # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)                             

# wfile = open(os.getcwd()+"/twitter.txt", mode='w')        # 텍스트 파일로 출력(쓰기모드)

# twitter 검색 cursor 선언
# f = open('write.csv','w', newline='')
# wr = csv.writer(f)

cursor = tweepy.Cursor(api.search_tweets, 
                       q=keyword,
                       since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴
                       count=10,  # 페이지당 반환할 트위터 수 최대 100
                       geocode=location,
                       include_entities=True)
okt = Okt()
qs = Post.objects.all()
#print(qs[5].join_word)
for i, tweet in enumerate(cursor.items()):
    print(tweet.id)
    if tweet.id != LatestLink.objects.all()[0].link:
        LatestLink.objects.all().update(link = tweet.id)
        noun = okt.nouns(tweet.text)
        for i, v in enumerate(noun):
            if len(v)<2:
                noun.pop(i)
        sorted(noun)
        for i in range(len(noun)):
            for j in range(i,len(noun)):
                if i!=j:
                    # k = [noun[i], noun[j]]
                    # wr.writerow(k)

                    query = qs.filter(pkWord=noun[i]).filter(join_word = noun[j])
    #                print(query)
    #                jvlist = [e.join_v for e in query.all()]
                    # if len(jvlist) != 0:
                    #     query.update(join_v=)
                    if len(query) != 0:
                        query.update(join_v=query[0].join_v+1)
                    else:
                        Post(
                            pkWord = noun[i],
                            join_word = noun[j],
                            join_v = 0,
                        ).save()
    else:
        print("no tweets updated.")
    print(noun)

# keyword = "나비 -filter:retweets"
# cursor = tweepy.Cursor(api.search, 

#                        q=keyword,

#                        since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴

#                        count=300,  # 페이지당 반환할 트위터 수 최대 100

#                        geocode=location,

#                        include_entities=True)
# for i, tweet in enumerate(cursor.items()):
#     noun = okt.nouns(tweet.text)
#     for i, v in enumerate(noun):
#         if len(v) < 2:
#             noun.pop(i)
#     for i in range(len(noun)):
#         for j in range(len(noun)):
#             if i != j:
#                 k = [noun[i], noun[j]]
#                 wr.writerow(k)
#     print(noun)

# f.close()

#twitter_df = pd.DataFrame(tweet_list

#    wfile.write(tweet.text + '\n')

#wfile.close()

#https://liveyourit.tistory.com/57
#https://wikidocs.net/43280
#https://jeongwookie.github.io/2019/06/10/190610-twitter-data-crawling/
