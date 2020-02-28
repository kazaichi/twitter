def errer_code(code):
    if code == 304:
        print(str(code) + ":Not Modified")
        print("新たなデータは取得されませんでした。")
    elif code == 400:
        print(str(code) + "Bad Request")
        print("このリクエストは無効、もしくはサポートされていません。")
    elif code == 401:
        print(str(code) + ":Unauthorized")
        print("	認証資格情報 が不足しているか、正しくありません。")
    elif code == 403:
        print(str(code) + ":Forbidden")
        print("リクエストの形式は問題ありませんが、それが拒否されたかアクセスが認められていません。")
    elif code == 404:
        print(str(code) + ":Not Found")
        print("リクエストしたURLが無効か、ユーザー情報などのリクエストしたリソースが存在しません。またリクエストした形式が、リクエスト対象のメソッドでサポートされていない場合があります。")
    elif code == 406:
        print(str(code) + ":Not Acceptable")
        print("リクエストの設定が不正な形式です。")
    elif code == 410:
        print(str(code) + ":Gone")
        print("このリソースは廃止されています。")
    elif code == 420:  # APIバージョン１における速度制限なので必要ないかも
        print(str(code) + ":Enhance Your Calm")
        print("速度制限にかかりました。")
    elif code == 422:
        print(str(code) + ":Unprocessable Entity")
        print("POST account / update_profile_bannerへアップロードした画像の処理ができませんでした。")
    elif code == 500:
        print(str(code) + ":Internal Server Error")
        print("何かが破損しています。\n開発者フォーラムへ報告することでTwitterチームが調査可能です。")
    elif code == 502:
        print(str(code) + "Bad Gateway")
        print("Twitter がダウンしているか、更新作業中です。")
    elif code == 503:
        print(str(code) + ":Service Unavailable")
        print("Twitter のサーバは起動していますが、リクエストが多すぎる状態です。時間を置いて再試行してください。")
    elif code == 504:
        print(str(code) + "Gateway timeout")
        print("Twitter サーバは起動していますが、スタック内でなんらかの障害が発生したためリクエストを処理できませんでした。時間を置いて再試行してください。")
    else:
        print(code)
        print("unknown")
