import scrapy
import json
import re
from xinhuokol.items import XinhuokolItem


class XinhuoPostSpider(scrapy.Spider):
    name = 'xinhuo_post'
    allowed_domains = ['www.xinhuokol.com/']
    base_urls = 'https://www.xinhuokol.com/api/user/search'
    start_urls = [base_urls]

    strs = 'PHPSESSID=849dmipkvuugchtralhtfganp1; nb-referrer-hostname=www.xinhuokol.com; nb-start-page-url=https%3A%2F%2Fwww.xinhuokol.com%2F; Hm_lvt_e037a348d71ecfd35f2be661f5f59d82=1602555047,1602569857; Hm_lpvt_e037a348d71ecfd35f2be661f5f59d82=1602581679'
    strList = re.split(r';\S*', strs)
    cookie = {}
    for items in strList:
        item = items.split('=')
        key, value = item[0], item[1]
        cookie[str(key)] = str(value)

    data={
            'platform':"instagram",
            'pageNum':"2"
        }
    
    headers={'X-Requested-With':'XmlHttpRequest'}


    def start_requests(self):
        yield  scrapy.FormRequest(url=self.base_urls,headers=self.headers,formdata=self.data,cookies=self.cookie,callback=self.parse)




    def parse(self, response):
        node_list = json.loads(response.body.decode('utf8'))
        
        for node in node_list.get('data',[]):
            item = XinhuokolItem()
            item['name'] = node.get('full_name')
            item['first_type'] = node.get('category_info')[0].get('category')
            item['first_type_score'] = node.get('category_info')[0].get('score')
            item['follower_count'] = node.get("follower_count")
            item['media_count'] = node.get("media_count")
            item['region'] = '未知'
            # print(item['name'])
            break
            # yield item

        if node_list['is_end'] == False:
            self.data['pageNum'] = str(int(self.data['pageNum']) + 1)
            yield  scrapy.FormRequest(url=self.base_urls,headers=self.headers,formdata=self.data,cookies=self.cookie,callback=self.parse,dont_filter=True)


        # print(response.body.decode('utf8'))
        # pass
