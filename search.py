import tweepy
import config
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)

auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)
location = "%s,%s,%s" % ("35.95", "128.25", "1000km")  # 검색기준(대한민국 중심) 좌표, 반지름  
kword = "디스커버리"
keyword = kword+" -투어오퍼레이터 -filter:media -filter:retweets"                                      # OR 로 검색어 묶어줌, 검색어 5개(반드시 OR 대문자로)                             

cursor = tweepy.Cursor(api.search_tweets, 
                       q=keyword,
                       since='2015-01-01', # 2015-01-01 이후에 작성된 트윗들로 가져옴
                       count=10,  # 페이지당 반환할 트위터 수 최대 100
                       lang='ko',
                       geocode=location,
                       include_entities=True)

for i, tweet in enumerate(cursor.items(10)):
    print(tweet.text)