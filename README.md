# twitter APIモジュール
## モジュール
### 完成
[twitter API](https://developer.twitter.com/en/docs/api-reference-index)における
- GET followers/ids (getFollowers_ids.py)
- GET followers/list (getFollowers_list.py)
- GET friends/ids (getFriends_ids.py)
- GET friends/list (getFriends_list.py)
- GET statuses/user_timeline (getStatuses_user_timeline.py)<br> 
<p>を作成した。</p>

### 作成途中(使えないこともない)　
- POST statuses/update (postTweet.py)
他のAPIについても順次作成予定

## 必要なもの
- errer.py (twitter APIにおけるエラー処理)
- pause.py (使用制限がかかった際に一時停止用モジュール)
- config.py (キーやトークンが保存されたモジュール)

## config.pyは各自で作成する必要あり
各自、ご自分のアカウントのキーやトークンに書き換えたconfig.pyを作成してください。
```python:config.py
CONSUMER_KEY = "********"
CONSUMER_SECRET = "********"
ACCESS_TOKEN = "********"
ACCESS_TOKEN_SECRET = "********"
```
