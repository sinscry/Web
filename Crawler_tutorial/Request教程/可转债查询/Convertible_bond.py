import json
import requests

parameter = {
    "type":"KZZ_LB2.0",
    "token":"70f12f2f4f091e459a279469fe49eca5",
    "cmd":"",
    "st":"YJL",
    "sr":"-1",
    "ps":"50",
    "js":"var%20tbzXIoUm={pages:(tp),data:(x),font:(font)}",
    "rt":"53608498",
    "p":"1"
}




url = "http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get"
r = requests.get(url,params=parameter)
# print(r.text)
text = r.text
text = text.split("data:")[1]

# text = r.text[28:-2]
text= text.split(',font',1)[0]

text = '{'+'"data":'+text+'}'
data = json.loads(text)['data']
for d in data:
    print(d)