#### Request教程
* 轻量级任务用request完成比较方便
0. 依赖库:
	* import json
	* import requests


1. 请求地址:
	```
	url = "https://www.wotokol.com/index.php/api/search/youtube?link=&price=&subscriber=0-100000&kol_country=&kol_sex=&category=820&s_country=142&s_sex=&s_age=&s_operating=&s_terminal=&wares_key=&is_brand=&token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MDQyODYyMjcsImV4cCI6MTYwNDM0NjIyNywidXNlcl9pZCI6MTU5NCwicGhvbmUiOiIxMzkyNjE3ODU3NyIsIm5hbWUiOm51bGx9.630M6TeHTwr2qHSsgDkArS8VM6BE1mM1E7D2dWh-obM&page=1&limit=10000"    #发送get请求
    r = requests.get(url)
	```
2. 返回:
	* 响应码:`print(response) `
	* String格式:`print(response.text)`
	* String转json:
2. 获取返回的json数据
	`data_list = r.json()['data']`
	