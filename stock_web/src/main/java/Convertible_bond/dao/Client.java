package Convertible_bond.dao;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import org.springframework.stereotype.Component;

import java.io.IOException;

@Component
public class Client{
    private static HttpClient client = HttpClients.createDefault();
    public String get(String url) throws IOException {
        HttpGet get = new HttpGet(url);    //创建get请求
        CloseableHttpResponse response = (CloseableHttpResponse) client.execute(get);   //执行get请求
        String mes = EntityUtils.toString(response.getEntity());    //将返回体的信息转换为字符串
        return mes;
    }

}
