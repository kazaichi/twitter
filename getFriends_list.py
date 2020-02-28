# 本モジュールのget関数について
# 第1引数にはユーザーIDまたはスクリーンネームを渡す。
# 第2引数には第1引数で渡したものがIDならば1,スクリーンネームならば0を渡す。
import json, config  # 標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session  # OAithのライブラリの読み込み
import datetime, time
import pause
import errer

def get(user_info, flag):
    CK = config.CONSUMER_KEY
    CS = config.CONSUMER_SECRET
    AT = config.ACCESS_TOKEN
    ATS = config.ACCESS_TOKEN_SECRET
    twitter = OAuth1Session(CK, CS, AT, ATS)  # 認証処理

    url = "https://api.twitter.com/1.1/friends/list.json"  # タイムライン取得エンドポイント
    
    if flag:  # IDで検索
        params = {'user_id' : user_info, 'count' : 200, 'cursor' : -1}
    else:  # 名前で検索
        params = {'screen_name' : user_info, 'count' : 200, 'cursor' : -1}
    
    all_list_info = []  # return用
    while True:
        res = twitter.get(url, params = params)
        # 正常に通信できた場合
        if res.status_code == 200:
            print("Success!")
            list_info = json.loads(res.text)  # レスポンスからタイムラインリストを取得
            all_list_info.extend(list_info['users'])
            if list_info['next_cursor'] != 0:
                params['cursor'] = list_info['next_cursor']
                print("continue")
            else:
                print("end")
                limit = res.headers['x-rate-limit-remaining'] #リクエスト可能残数の取得
                reset = res.headers['x-rate-limit-reset'] #リクエスト叶残数リセットまでの時間(UTC)
                sec = int(res.headers['X-Rate-Limit-Reset']) - time.mktime(datetime.datetime.now().timetuple()) #UTCを秒数に変換
                break

        # 使用制限エラー
        elif res.status_code == 429:
            reset = res.headers['x-rate-limit-reset'] #リクエスト叶残数リセットまでの時間(UTC)
            sec = int(res.headers['X-Rate-Limit-Reset']) - time.mktime(datetime.datetime.now().timetuple()) #UTCを秒数に変換
            pause.counter(sec)

        # その他エラー
        else:
            errer.errer_code(res.status_code)
            break
    return all_list_info, limit, sec
if __name__ == '__main__':
    user_info = input("スクリーンネーム(＠を除く)を入力してください:")
    all_list_info, limit, sec = get(user_info, 0)
    for list in all_list_info:
        print(list['name'])
        print(list['id'])
        print(list['screen_name'])
        print('*******************************************')
    print ("limit: " + str(limit))
    print ("reset sec: " + str(sec))