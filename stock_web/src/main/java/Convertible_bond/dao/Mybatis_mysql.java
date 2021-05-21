package Convertible_bond.dao;

import Convertible_bond.pojo.MyUser;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import org.springframework.stereotype.Component;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;


@Component
public class Mybatis_mysql {
    //读取配置文件mybatis-config.xml
    private final InputStream config = Resources.getResourceAsStream("mybatis-config.xml");
    //根据配置文件构建SqlSessionFactory
    private final SqlSessionFactory ssf = new SqlSessionFactoryBuilder().build(config);
    //通过SqlSessionFactory 创建 SqlSession
    public Mybatis_mysql() throws IOException {
    }

    //查询所有用户
//    public List<MyUser> selectAll(){
//        SqlSession ss = ssf.openSession();
//        List<MyUser> listMu = ss.selectList("mapper.UserMapper.selectAllUser");
//        ss.close();
//        return listMu;
//    }

    //查询所有用户名
    public List<String> selectAllName(){
        SqlSession ss = ssf.openSession();
        List<String> name_list = ss.selectList("mapper.UserMapper.selectAllName");
        ss.close();
        return name_list;
    }

    //根据用户名查数据
    public List<MyUser> selectByName(String usr){
        SqlSession ss = ssf.openSession();
        List<MyUser> usr_list = ss.selectList("mapper.UserMapper.selectByName",usr);
        ss.close();
        return usr_list;
    }

    //增加MySQL记录
    public String addMYSQL(String name,String stock_id, String stock_nm,double oprice) {
        MyUser addmu = new MyUser();
        addmu.setUsr(name);
        addmu.setStock_id(stock_id);
        addmu.setStock_nm(stock_nm);
        addmu.setOprice(oprice);

        SqlSession ss = ssf.openSession();
        ss.insert("mapper.UserMapper.addMYSQL",addmu);
        //提交事务
        ss.commit();
        ss.close();
        return "添加成功";
    }

    //删除MySQL记录
    public String delMYSQL(String name,String stock_id) {
        MyUser delmu = new MyUser();
        delmu.setUsr(name);
        delmu.setStock_id(stock_id);

        SqlSession ss = ssf.openSession();
        ss.delete("mapper.UserMapper.delMYSQL",delmu);
        //提交事务
        ss.commit();
        ss.close();
        return "删除成功";
    }

}
