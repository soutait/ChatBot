import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests

#-----------------------天気関係
url = "https://weather.tsukumijima.net/api/forecast/city/120010"
payload = {"city":"120010"}
tenki_data = requests.get(url, params=payload).json() 

#print(tenki_data)      --すべてのデータがjson形式で出力される


#タイトル(県名出力)
print(tenki_data["title"])

#日付
day="日付 :"+tenki_data["forecasts"][0]["date"]

#天気
weather="天気 :"+tenki_data["forecasts"][0]["telop"]

#風速
wave="風速 :"  +   tenki_data["forecasts"][0]["detail"]["wave"]

#降水確率 (0時~06時の観測データ)
rain="降水確率 :"  +   tenki_data["forecasts"][0]["chanceOfRain"]["T12_18"]


##-------------------------lineAPI関係

file = open('info.json','r')
info = json.load(file)


CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = "テスト送信。\n今日の天気をお伝えします。\n"
    + day +"\n"+ weather +"\n"+ wave +"\n"+ rain
)
    
    
    #line_bot_api.push_message(USER_ID,messages = messages)  自分のみに送る
    
    #ブロードキャストテスト
    line_bot_api.broadcast(messages = messages)
    
if __name__ == "__main__":
    main()