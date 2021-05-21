### JAVA网络编程

* 用HttpClient进行网络访问

* 链接:https://blog.csdn.net/justry_deng/article/details/81042379

0. 依赖:
	```
	<dependencies>
        <dependency>
            <groupId>org.apache.httpcomponents</groupId>
            <artifactId>httpclient</artifactId>
            <version>4.5.5</version>
        </dependency>
        <dependency>
            <groupId>com.alibaba</groupId>
            <artifactId>fastjson</artifactId>
            <version>1.2.47</version>
        </dependency>
    </dependencies>
	```

1. get访问:
	1. 无参get访问
	```
	HttpClient client = HttpClients.createDefault();            //client对象
	HttpGet get = new HttpGet("https://www.baidu.com");    //创建get请求
	CloseableHttpResponse response = (CloseableHttpResponse) client.execute(get);   //执行get请求
	String mes = EntityUtils.toString(response.getEntity());    //将返回体的信息转换为字符串
	System.out.println(mes);
	```
	2. 有参get访问：直接拼接就好