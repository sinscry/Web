package Convertible_bond.controller;

import Convertible_bond.dao.Client;
import Convertible_bond.pojo.MyUser;
import Convertible_bond.dao.Mybatis_mysql;
import Convertible_bond.pojo.axios_stock;
import com.alibaba.fastjson.JSONArray;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

@Controller
public class StockIndexController {

    //访问数据类
    @Autowired
    private Client Client;


    //数据库操作类
    @Autowired
    private Mybatis_mysql Mybatis_mysql;

    @RequestMapping("/stock")
    public String stock(){
        return "可转债";
    }

    //可转债数据
    @RequestMapping("/stock_json")
    @ResponseBody
    @CrossOrigin
    public String stock_json() throws IOException {
        //后台Http请求转发解决跨域问题
        return Client.get("https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1608430043802");
    }
    //单纯转发数据
    @RequestMapping(value="/axios_sim_stock")
    @ResponseBody
    @CrossOrigin
    public String axios_sim_stock(@RequestParam(value = "url") String url) throws IOException {
        //后台Http请求转发解决跨域问题
        return Client.get(url);
    }




    //用户数据
    @RequestMapping("/usr_json")
    @ResponseBody
    @CrossOrigin
    public String usr_json() throws IOException {
        //获取用户名数组
        List<String> name_list = Mybatis_mysql.selectAllName();

        List<String> Result_list=new ArrayList<String>();
        //根据用户名构建Result_list:[{'name':'"+name+"','stock_list':"+stock_list+"}]
        for (String name:name_list){
            //根据用户名获取信息
            List<MyUser> usr_list=Mybatis_mysql.selectByName(name);
            List<String> stock_list=new ArrayList<String>();
            //根据每股代码构建stock_list
            for (MyUser usr:usr_list){
                String get_info[] = Client.get("http://hq.sinajs.cn/list="+usr.stock_id).split(",");

                String sprice=get_info[3];//现价
                String yprice = get_info[2];//昨天价格
                String hprice = get_info[4];//当日最高价
                String stock_li = "{'stock_id':'"+usr.stock_id+"','stock_nm':'"+usr.stock_nm+"','sprice':'"+sprice+"','oprice':'"+usr.oprice+"','yprice':'"+yprice+"','hprice':'"+ hprice +"'}";
                stock_list.add(stock_li);
            }
            String Result_li = "{'name':'"+name+"','stock_list':"+stock_list+"}";
            Result_list.add(Result_li);
        }
        JSONArray jsonArray = JSONArray.parseArray(Result_list.toString());
        return jsonArray.toString();
    }

    //添加数据
    @RequestMapping("/axios_add_stock")
    @ResponseBody
    public String axios_add_stock(@RequestBody axios_stock axios_add_stock) throws IOException {
        String[] info = Client.get("http://hq.sinajs.cn/list="+axios_add_stock.getStock_id()).split(",");
        if (info.length==1) return "查无此股";
        String stock_nm=info[0].split("=\"")[1];
        return Mybatis_mysql.addMYSQL(axios_add_stock.getName(),axios_add_stock.getStock_id(),stock_nm,axios_add_stock.getOprice());
    }

    //减少数据
    @RequestMapping("/axios_del_stock")
    @ResponseBody
    public String axios_del_stock(@RequestBody axios_stock axios_del_stock) throws IOException {
        return Mybatis_mysql.delMYSQL(axios_del_stock.getName(),axios_del_stock.getStock_id());
    }



    @RequestMapping("/test")
    @ResponseBody
    @CrossOrigin
    public String test() throws IOException {
        return "t";
    }



}
