
import json
import requests

class Pipeline:
    def __init__(self):
        self.f = open("wotokol_origin.json","w",encoding='utf-8')
        

    def process_item(self, item):
        content = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(content)

    def close(self):
        self.f.close()

if __name__ == '__main__':
    #请求地址
    # url = "https://www.wotokol.com/index.php/api/search/youtube?link=&price=&subscriber=0-100000&kol_country=&kol_sex=&category=820&s_country=142&s_sex=&s_age=&s_operating=&s_terminal=&wares_key=&is_brand=&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDQyODYyMjcsImV4cCI6MTYwNDM0NjIyNywidXNlcl9pZCI6MTU5NCwicGhvbmUiOiIxMzkyNjE3ODU3NyIsIm5hbWUiOm51bGx9.630M6TeHTwr2qHSsgDkArS8VM6BE1mM1E7D2dWh-obM&page=1&limit=10000"    #发送get请求
    r = requests.get(url)
    #获取返回的json数据
    data_list = r.json()['data']

    Pipe = Pipeline()
    
    for data in data_list:
        Pipe.process_item(data)

    Pipe.close()


