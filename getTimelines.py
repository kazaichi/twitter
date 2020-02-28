import json, config  # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session  # OAithのライブラリの読み込み

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

url = "https://api.twitter.com/1.1/statuses/user_timeline.json"  # タイムライン取得エンドポイント

params = {'count' : 5}  # 取得数
res = twitter.get(url, params = params)

if res.status_code == 200:  # 正常に通信できた場合
    print("true")
    timelines = json.loads(res.text)  # レスポンスからタイムラインリストを取得
    print(timelines)
    for line in timelines:
        print(line['user']['name']+'::'+line['text'])
        print(line['created_at'])
        print('*******************************************')
else:
    print("Failed: %d" % res.status_code)
