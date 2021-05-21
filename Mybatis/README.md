##### Mybatis

* 通过mybatis连接数据库方便使用
* 逻辑: 
	* 测试类加载mybatis-config.xml构造SqlSessionFactory，然后通过具体的mapper实施sql语句
	* mybatis-config.xml会装载mapper文件
	



0. 依赖:
	```
	<dependencies>
        <!-- 添加junit -->
        <dependency>
            <groupId>junit</groupId>
            <artifactId>junit</artifactId>
            <version>4.11</version>
            <scope>test</scope>
        </dependency>

        <!-- 添加log4j -->
        <dependency>
            <groupId>log4j</groupId>
            <artifactId>log4j</artifactId>
            <version>1.2.17</version>
        </dependency>

        <!-- 添加mybatis -->
        <dependency>
            <groupId>org.mybatis</groupId>
            <artifactId>mybatis</artifactId>
            <version>3.5.6</version>
        </dependency>

        <!-- 添加mysql驱动 -->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>5.1.12</version>
        </dependency>
    </dependencies>
	```

1. MySQL建表:
	```
	CREATE DATABASE mybatis;
	USE mybatis;
	DROP TABLE IF EXISTS `user`;
	CREATE TABLE user(
		uid int NOT NULL,
		uname varchar(20) DEFAULT NULL,
		usex varchar(10) DEFAULT NULL,
		update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
		id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增长id',
		PRIMARY KEY (id)
	)ENGINE=InnoDB DEFAULT CHARSET=utf8;
	```

2. 创建日志文件:
	* 在 myBatis应用的 src 目录下创建 log4j.properties 文件
	```
	# Global logging configuration
	log4j.rootLogger=ERROR,stdout
	# MyBatis logging configuration...
	log4j.logger.com.mybatis=DEBUG
	# Console output...
	log4j.appender.stdout=org.apache.log4j.ConsoleAppender
	log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
	log4j.appender.stdout.layout.ConversionPattern=%5p [%t] - %m%n
	```

3. 创建持久类
	```
	package po;
	/**
	* springtest数据库中user表的持久类
	*/
	public class MyUser {
		private Integer uid; // 主键
		private String uname;
		private String usex;
		// 此处省略setter和getter方法
		
		@Override
		public String toString(){ //为了方便查看结果，重写了toString方法
			return "User[uid=" + uid + ",uname=" + uname + ",usex=" + usex + "]";
		}
	}
	```

4. 创建映射文件
	* 在mapper包下创建隐射文件UserMapper.xml
	```
	<?xml version="1.0" encoding="UTF-8"?>
	<!DOCTYPE mapper
			PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
			"http://mybatis.org/dtd/mybatis-3-mapper.dtd">
	<mapper namespace="mapper.UserMapper">
		<!-- 根据uid查询一个用户信息 -->
		<select id="selectUserById" parameterType="Integer"
				resultType="po.MyUser">
			select * from user where uid = #{uid}
		</select>
		<!-- 查询所有用户信息 -->
		<select id="selectAllUser" resultType="po.MyUser">
			select * from user
		</select>
		<!-- 添加一个用户，#{uname}为 com.mybatis.po.MyUser 的属性值 -->
		<insert id="addUser" parameterType="po.MyUser">
			insert into user (uid,uname,usex)
			values(#{uid},#{uname},#{usex})
		</insert>
		<!--修改一个用户 -->
		<update id="updateUser" parameterType="po.MyUser">
			update user set uname =
			#{uname},usex = #{usex} where uid = #{uid}
		</update>
		<!-- 删除一个用户 -->
		<delete id="deleteUser" parameterType="Integer">
			delete from user where uid
			= #{uid}
		</delete>
	</mapper>
	```
5. 创建 MyBatis 的配置文件：
	* 在 src 目录下创建 MyBatis 的核心配置文件 mybatis-config.xml
	```
	<?xml version="1.0" encoding="utf-8"?>
	<!DOCTYPE configuration PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
			"http://mybatis.org/dtd/mybatis-3-config.dtd">
	<configuration>
		<settings>
			<setting name="logImpl" value="LOG4J" />
		</settings>
		<!-- 配置mybatis运行环境 -->
		<environments default="development">
			<environment id="development">
				<!-- 使用JDBC的事务管理 -->
				<transactionManager type="JDBC" />
				<dataSource type="POOLED">
					<!-- MySQL数据库驱动 -->
					<property name="driver" value="com.mysql.jdbc.Driver" />
					<!-- 连接数据库的URL -->
					<property name="url"
							  value="jdbc:mysql://localhost:3306/mybatis?characterEncoding=utf8" />
					<property name="username" value="root" />
					<property name="password" value="root" />
				</dataSource>
			</environment>
		</environments>
		<!-- 将mapper文件加入到配置文件中 -->
		<mappers>
			<mapper resource="mapper/UserMapper.xml" />
		</mappers>
	</configuration>
	```

6. 创建测试类
	```
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
	```
	
	
	
	
	
	