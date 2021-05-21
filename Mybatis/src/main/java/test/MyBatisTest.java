package test;



import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import po.MyUser;

import java.io.IOException;
import java.io.InputStream;
import java.util.List;

public class MyBatisTest {
    public static void main(String[] args){
        try{
            //读取配置文件mybatis-config.xml
            InputStream config = Resources.getResourceAsStream("mybatis-config.xml");
            //根据配置文件构建SqlSessionFactory
            SqlSessionFactory ssf = new SqlSessionFactoryBuilder().build(config);
            //通过SqlSessionFactory 创建 SqlSession
            SqlSession ss = ssf.openSession();
            //SqlSession执行映射文件定义的SQL，并返回映射结果

            //查询一个用户
            MyUser mu = ss.selectOne("mapper.UserMapper.selectUserById", 2);
            System.out.println(mu);

            //查询所有用户
            List<MyUser> listMu = ss.selectList("mapper.UserMapper.selectAllUser");
            for (MyUser myUser: listMu){
                System.out.println(myUser);
            }

            //添加一个用户
            MyUser addmu = new MyUser();
            addmu.setUname("sinscry3");
            addmu.setUsex("男");
            addmu.setUid(0);
            ss.insert("mapper.UserMapper.addUser", addmu);

            //修改一个用户
            MyUser updatemu = new MyUser();
            updatemu.setUid(2);
            updatemu.setUname("梁某");
            updatemu.setUsex("男");
            ss.update("mapper.UserMapper.updateUser", updatemu);

            //删除一个用户
            ss.delete("mapper.UserMapper.deleteUser", 2);

            //提交事务
            ss.commit();
            //关闭SqlSession
            ss.close();

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
