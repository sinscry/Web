import scrapy
from xinhuokol.items import XinhuokolItem
import re
import json

'''
无限滚动页面，通过json加载数据
1.首页先按正常去爬取
2.其他的通过post获取数据
'''



class XinhuoFinalSpider(scrapy.Spider):
    name = 'xinhuo_final'
    allowed_domains = ['www.xinhuokol.com']
    start_urls = ['https://www.xinhuokol.com/instagram/follower_count-3000%2C200000']
    base_urls = 'https://www.xinhuokol.com/api/user/search'

    headers={'X-Requested-With':'XmlHttpRequest'}

    # 设置cookie，免登录设置，从浏览器复制cookie到strs即可
    strs = 'Hm_lvt_e037a348d71ecfd35f2be661f5f59d82=1602555047,1602569857,1602727354; nb-referrer-hostname=www.xinhuokol.com; nb-start-page-url=https%3A%2F%2Fwww.xinhuokol.com%2Finstagram%2Fsearch%2F; PHPSESSID=ovlagp0a8jn15pb1n8nlrc4401; Hm_lpvt_e037a348d71ecfd35f2be661f5f59d82=1602728540'
    strList = re.split(r';\S*', strs)
    cookie = {}
    for items in strList:
        item = items.split('=')
        key, value = item[0], item[1]
        cookie[str(key)] = str(value)
    data={
            'platform':"instagram",
            'follower_count': '3000,200000',
            'pageNum':"2"
        }

    # 重写初始请求代码，设置cookie达到免登录效果
    def start_requests(self):
        yield scrapy.Request(self.start_urls[0],cookies=self.cookie, callback=self.parse)


    # 首页处理代码
    def parse(self, response):  
        node_list = response.xpath("//div[@class='el-card__body']")
        for node in node_list:
            item = XinhuokolItem()
            name_region = node.xpath("./div[@class='bloger-baseinfo']/div/a/span/text()").extract()
            item['name'] = name_region[0]
            item['region'] = (name_region[1].replace("\n",'')).replace(' ','')

            first_tpye = node.xpath("./div[@class='bloger-baseinfo']/div/span/span/text()").extract()
            item['first_type'] = first_tpye[0]
            item['first_type_score'] = first_tpye[1]

            fans_photo = node.xpath("./div[@class='bloger-analysis']/div/p/text()").extract()
            item['follower_count'] = fans_photo[1]
            item['media_count'] =fans_photo[3]
            yield item
        yield  scrapy.FormRequest(url=self.base_urls,headers=self.headers,formdata=self.data,cookies=self.cookie,callback=self.parse_post,dont_filter=True)
        
    # post请求处理代码
    def parse_post(self, response):
        node_list = json.loads(response.body.decode('utf8'))
        
        for node in node_list.get('data',[]):
            item = XinhuokolItem()
            item['name'] = node.get('full_name')
            item['first_type'] = node.get('category_info')[0].get('category')
            item['first_type_score'] = node.get('category_info')[0].get('score')
            item['follower_count'] = node.get("follower_count")
            item['media_count'] = node.get("media_count")
            item['region'] = '未知'
            yield item

        if node_list['is_end'] == False:
            self.data['pageNum'] = str(int(self.data['pageNum']) + 1)
            yield  scrapy.FormRequest(url=self.base_urls,headers=self.headers,formdata=self.data,cookies=self.cookie,callback=self.parse_post,dont_filter=True)
