# WebAPIを使うときに便利なライブラリ
import requests

# 郵便番号を変数にセットする
zipcode = "1600022"  

# 窓口（API）の場所
url = "https://zipcloud.ibsnet.co.jp/api/search?zipcode="

# リクエストを送信し、返ってきたデータ（レスポンス）をresponseに格納
# 例）url + zipcode は https://zipcloud.ibsnet.co.jp/api/search?zipcode=1600022 になります。
response = requests.get(url + zipcode)


# レスポンスからデータを取り出す
data = response.json()

# 結果を表示
print(data)
