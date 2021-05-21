# 最终处理结果

import json
import requests

baseurl = 'https://www.wotokol.com/index.php/api/detail/ytbBaseInfo?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDQyODYyMjcsImV4cCI6MTYwNDM0NjIyNywidXNlcl9pZCI6MTU5NCwicGhvbmUiOiIxMzkyNjE3ODU3NyIsIm5hbWUiOm51bGx9.630M6TeHTwr2qHSsgDkArS8VM6BE1mM1E7D2dWh-obM&youtube_id='

e = open("wotokol.json","w",encoding='utf-8')

i=0
with open('wotokol_origin.json', 'r',encoding='utf-8') as f:
    data_list = f
    for data in data_list:
        data = json.loads(data)
        kol_nickname = data['kol_nickname'] # 名字
        subscriber = data['subscriber'] # 粉丝数
        kol_player_num = data['kol_player_num'] # 总观看量
        kol_country = data['kol_country'] # 所在地区
        kol_interact_rate = data['kol_interact_rate'] # 互动率
        kol_player_num_mean = data['kol_player_num_mean'] # 平均播放量
        kol_wotokol_score = data['kol_wotokol_score'] # 评分
        youtube_id = data['youtube_id']
        tmpurl = baseurl+str(youtube_id)
        
        try:
            r = requests.get(tmpurl)
            price_data = r.json()['data']
            price = "￥"+price_data['kol_price_min']+'-'+price_data['kol_price_max'] # 参考价格
        except:
            price = "￥0.00-0.00"


        item = {'youtube_id':youtube_id,'kol_nickname':kol_nickname,'subscriber':subscriber,'kol_player_num':kol_player_num,'kol_country':kol_country,'kol_interact_rate':kol_interact_rate,'kol_player_num_mean':kol_player_num_mean,'price':price,'kol_wotokol_score':kol_wotokol_score}
        content = json.dumps(item, ensure_ascii=False) + "\n"
        e.write(content)

e.close()