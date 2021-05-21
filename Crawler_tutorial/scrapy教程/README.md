# scrapy爬虫

* 关于爬取数据提醒



![photo](./claude_monet.jpg)
<hr>

#### 爬虫基础
* 查询当前爬虫: scrapy list
* 创建爬虫: scrapy startproject 爬虫名
* 开始爬虫: scrapy crawl 爬虫名


1. ##### 创建爬虫项目
    * scrapy startproject ITcast
    * setting.py设置:
      1. 注释掉遵循robot协议 `ROBOTSTXT_OBEY = False`
      2. 更改请求头 `USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"`
      3. 添加编码方式：
           1. 输出json文件： `FEED_EXPORT_ENCODING = 'utf-8'`
           2. 输出csv文件： `FEED_EXPORT_ENCODING = 'gb18030'`


2. ##### 制作爬虫
    1. 进入ITcast/ITcast/spiders
    2. 定名和限范围:scrapy genspider itcast "www.itcast.cn" 
    3. 打印body文件看看: 
        * itcast.py 里设置 `print(response.body.decode('utf8'))`
        * scrapy crawl itcast
    4. 可选:    
        * cookie登录: 参考网站:https://blog.csdn.net/weixin_42927647/article/details/89707609
        ```
            def start_requests(self):
                strs = '复制浏览器的cookie'
                strList = re.split(r';\S*', strs)
                cookie = {}
                for items in strList:
                    item = items.split('=')
                    key, value = item[0], item[1]
                    cookie[str(key)] = str(value)
                yield scrapy.Request(self.start_urls[0],cookies=cookie, callback=self.parse)
        ```
        * selenium动态登录(去除js): 参考网站:https://www.jianshu.com/p/87ab84828a5d
            + 在middlewares.py中修改:
                ```
                from selenium import webdriver
                from selenium.webdriver.chrome.options import Options
                import time
                import scrapy

                def process_request(self, request, spider):
                    # Called for each request that goes through the downloader
                    # middleware.

                    chrome_options = Options()
                    chrome_options.add_argument('--headless')  # 使用无头谷歌浏览器模式
                    chrome_options.add_argument('--disable-gpu')
                    chrome_options.add_argument('--no-sandbox')
                    driver_url = r"D:\Apps\path\Chrome\chromedriver.exe"
                    self.driver=webdriver.Chrome(chrome_options=chrome_options,executable_path=driver_url)

                    self.driver.get(request.url)
                    time.sleep(1)
                    html = self.driver.page_source
                    self.driver.quit()
                    return scrapy.http.HtmlResponse(url=request.url, body=html.encode('utf-8'), encoding='utf-8',request=request)
                    # return None
                ```
            
            + 在settings.py中修改:
                ```
                DOWNLOADER_MIDDLEWARES = {
                'Tencent.middlewares.TencentDownloaderMiddleware': 543,
                }
                ```





3. ##### 寻找目标字段
    1. 用xpath helper寻找目标字段:
        * 姓名://div[@class='main_bot']/h2/text()
        * 职称://div[@class='main_bot']/h2/span/text()
        * 工作经验://div[@class='main_bot']/h3
        * 研发成果://div[@class='main_bot']/p


4. ##### 定义爬取字段
    1. items.py里编辑:
    ```
        name=scrapy.Field()
        title=scrapy.Field()
        experience=scrapy.Field()
        result=scrapy.Field()
    ```

5. ##### 简单爬取文件下来
    1. 返回items格式数据
    ```
    from ITcast.items import ItcastItem
    def parse(self, response):
        node_list = response.xpath("//div[@class='main_bot']")
        items = []
        for node in node_list:
            item = ItcastItem()
            name=node.xpath("./h2/text()").extract()
            item['name']=name[0]
            items.append(item)
        return items
    ```

    2. 保存至json文件代码: 
        * scrapy crawl itcast -o itcast.json
        * scrapy crawl itcast -o itcast.csv
        * json 转 excel:https://json-csv.com/
        * json 转 csv:
        ```
        import csv
        import json

        rows = []
        for line in open('xinhuo.json', 'r',encoding='utf8'):
            rows.append(json.loads(line))

        f = open('xinhuo.csv', 'w',encoding='utf8')
        csv_write = csv.writer(f)

        # writerow: 按行写入，　writerows: 是批量写入
        # 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
        csv_write.writerow(rows[0].keys())

        for row in rows:
            csv_write.writerow(row.values())
        f.close()
        ```

6. #### 正常爬文件
    1.在itcast.py编写
    ```
    from ITcast.items import ItcastItem
    def parse(self, response):
        node_list = response.xpath("//div[@class='main_bot']")
        for node in node_list:
            item = ItcastItem()
            name=node.xpath("./h2/text()").extract()
            item['name']=name[0]
            yield item

        # 下一页链接请求 
        if self.offset<610:
            self.offset += 1
            url = self.baseURL + str(self.offset)
            yield scrapy.Request(url,callback = self.parse)
    ```

    2.在pipelines.py编写管道文件
    ```
    from itemadapter import ItemAdapter
    import json

    class ItacstPipeline:
        def __init__(self):
            self.f = open("itcast.json","w",encoding='utf-8')

        def process_item(self, item, spider):
            content = json.dumps(dict(item), ensure_ascii=False) + "\n"
            self.f.write(content)
            return item
        
        def close_spider(self, spider):
            self.f.close()
    ```

    3.在settings.py中设置管道文件
    ```
    ITEM_PIPELINES = {
    'Tencent.pipelines.TencentPipeline': 300,
    }
    ```

