# SpringMVC 是前后端交接框架

1. 用idea基于maven创建项目:
	1. 创建maven项目:`file-> new -> project -> maven -> org.apache.maven.archetypes:maven-archetype-webapp`
	2. maven依赖:
		```
		<!--设置jdk版本为15-->
		<build>
			<plugins>
				<plugin>
					<groupId>org.apache.maven.plugins</groupId>
					<artifactId>maven-compiler-plugin</artifactId>
					<configuration>
						<source>15</source>
						<target>15</target>
					</configuration>
				</plugin>
			</plugins>
		</build>
		
		
		<!--依赖设置-->
		<dependency>
		  <groupId>org.springframework</groupId>
		  <artifactId>spring-webmvc</artifactId>
		  <version>5.3.1</version>
		</dependency>
		<dependency>
            <groupId>javax.servlet</groupId>
            <artifactId>javax.servlet-api</artifactId>
            <version>3.0.1</version>
            <scope>provided</scope>
		</dependency>
		<dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjrt</artifactId>
            <version>1.9.5</version>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.9.5</version>
        </dependency>
        <dependency>
            <groupId>aopalliance</groupId>
            <artifactId>aopalliance</artifactId>
            <version>1.0</version>
        </dependency>
		```
	3. 配置文件
		* web.xml:
		```
		<?xml version="1.0" encoding="UTF-8"?>
		<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
				 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
				 xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_4_0.xsd"
				 version="4.0">
			 <!-- 部署 DispatcherServlet -->
			<servlet>
		<!--        两个HelloMVC必须一样，随意自己取名-->
				<servlet-name>HelloMVC</servlet-name>
				<servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
				<!-- 表示容器再启动时立即加载servlet -->
				<load-on-startup>1</load-on-startup>
			</servlet>

			<servlet-mapping>
				<servlet-name>HelloMVC</servlet-name>
				<!--        <url-pattern>*.form</url-pattern>-->
				 <!-- 处理所有URL -->
				<url-pattern>/</url-pattern>
			</servlet-mapping>
		</web-app>
		```
		`解释:DispatchServlet中的servlet对象HelloMVC初始化，在WEB-INF下找HelloMVC-servlet.xml配置`
		* HelloMVC-servlet.xml:
		```
		<?xml version="1.0" encoding="UTF-8"?>
		<beans xmlns="http://www.springframework.org/schema/beans"
			   xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
			   xmlns:context="http://www.springframework.org/schema/context"
			   xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context.xsd">
			<!--    控制器类所在的包-->
			<context:component-scan base-package="controller"/>
			<bean class="org.springframework.web.servlet.view.InternalResourceViewResolver">
				<!--    /WEB-INF/page/意为页面的路径，.jsp为页面格式-->
				<property name="prefix" value="/WEB-INF/page/"/>
				<property name="suffix" value=".jsp"/>
			</bean>
		</beans>
		```
		`注意:如果你的取得名字是HelloMVC，那么与其对应的servlet名字必须是：HelloMVC-servlet.xml。格式是：自定义名称-servlet.xml`
	
	4. 编写控制类
		1. 在src-controller下新建一个类，叫IndexController:
		```
		package controller;

		import org.springframework.stereotype.Controller;
		import org.springframework.ui.Model;
		import org.springframework.web.bind.annotation.RequestMapping;
		import org.springframework.web.servlet.ModelAndView;

		import javax.servlet.http.HttpServletRequest;
		import javax.servlet.http.HttpServletResponse;

		@Controller
		public class IndexController {
			@RequestMapping("/index")
		//    public String handleRequest(Model model) throws Exception {
		//        model.addAttribute("message","这是第一个SpringMVC网页");
		//        return "index";
		//    }
			public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception{
				ModelAndView model=new ModelAndView("index");
				model.addObject("message","这是第一个SpringMVC网页");
				return model;
			}
		}
		```
	5. 在WEB-INF下设置page文件夹:
		```
		<%@ page contentType="text/html;charset=UTF-8" language="java" %>
		<html>
		<head>
			<title>SpringMVC</title>
		</head>
		<body>
		<h1>测试</h1>
		<h1>${message}</h1>
		</body>
		</html>
		```
	6. 配置tomcat：
		1. `file->Project Structure->Artifacts-> + -> Web Application: Exploded -> from module`
		2. `add configuration->tomcat->local`->`Deployment->+->Artifact->上一步的名字`
	
	7. 测试网址:`http://localhost:8080/SpringMVC_war_exploded/index`
	
	8. 打包war文件部署到服务器:
		1. 打包文件: 
			* `file->Project Structure->Artifacts-> + -> Web Application: Archive`
			* `Build -> Build Artifacts -> 上条添加的Artifacts的名字 -> Build`
			* 然后在对应路径生成了war包
		2. 将war包拷贝到tomcat的webapps文件下即可
		
		3. 通过http://localhost:8080/Artifacts的名字/index访问
			
			
			
			
			
			
			
			
			
			
			
			
			
			
			