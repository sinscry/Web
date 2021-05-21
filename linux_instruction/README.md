# linux指令
![Image text](./bg.jpg)

* ubuntu子系统路径:`C:\Users\用户ID\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04onWindows_79rhkp1fndgsc\LocalState\rootfs`

1. 常规指令
	* 下载：`wget -P /tmp url`
	* 删除: `rm -rf 文件名`
	* 我的阿里云服务器:120.78.209.24
	* 升级pip: `pip3 install --upgrade pip`
	* 指定源安装: `pip3 install --index-url https://pypi.douban.com/simple Image`
	* 查看cpu架构:`uname -m`
	
2. 安装Anaconda：
	* 相关网站教程:https://blog.csdn.net/weixin_44776894/article/details/106159483
	* 官网:https://www.anaconda.com/products/individual
	* 下载：`wget -P /tmp https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh`
	* 安装：`bash /tmp/Anaconda3-2020.07-Linux-x86_64.sh`
	* 加载环境变量: `source ~/.bashrc`
	* 升级Anaconda：`conda update --all`
	* 如果报错：conda: command not found：`sudo vim ~/.bashrc` 在最后一行加上 `export PATH=$PATH:/home/用户名/anaconda3/bin` 加载环境变量`source ~/.bashrc`

3. SSH服务:
	1. 安装
		* `sudo apt-get install openssh-client`
		* `sudo apt-get install openssh-server`
		* 启动:`sudo /etc/init.d/ssh start`
		* 查看：` ps -e | grep ssh`
		* IP地址查看：`ifconfig -a`
		* 配置设定`sudo vim /etc/ssh/sshd_config`：
			1. 密码登录：`PasswordAuthentication yes`
			2. root用户运行：#PermitRootLogin prohibit-password下增加`PermitRootLogin yes`
	2. 使用
		* 远程登录：`ssh user@ip`
		* 数据库: `mysql -uroot -proot -h192.168.0.333 -P3306`
		* 指定端口登录： `ssh user@ip -p 端口`
		* 复制：`scp -r usr@43.224.34.73:/home/lk   /root`  //将 /home/lk 文件拷贝到本地 /root 
		* 上传：`scp /root/test.jar   usr@43.224.34.73:/home/lk`
		* 退出：`exit`
		* 内网映射：
			1. frp
			2. 花生壳：https://console.hsk.oray.com/ （当前映射www.sinscry.tech:25319）
	
	3. 错误：
		* 无法连接时：`sudo vim ~/.ssh/known_hosts`，删除ip地址那行数据
		* 运行root用户登录：`sudo vim /etc/ssh/sshd_config` PermitRootLogin prohibit-password改成PermitRootLogin yes

4. 后台服务screen教程:
	* 创建新窗口名为luohan: `screen -S luohan`
	* 运行程序: `screen python3 luohansong.py`
	* 查看screen: `screen -ls`
	* 重新连接: `screen -r screen编号`
	* 杀screen: `kill -9 screen编号`
	* 删除无法使用的screen: `screen -wipe`
	* There is no screen to be resumed matching 2865：`screen -d 2865`
	
5. Java安装
	* 链接:https://blog.csdn.net/booklijian/article/details/110921554
	1. 安装jdk15.01:
		* `wget https://download.oracle.com/otn-pub/java/jdk/15.0.1+9/51f4f36ad4ef43e39d0dfdbaf6549e32/jdk-15.0.1_linux-x64_bin.tar.gz?AuthParam=1608448595_d554e64ffd6d737ba884fbc714a24acf`
		*  `tar -xvf jdk-15.0.1_linux-x64_bin.tar.gz`
	2. 设置环境变量:
		* 所有用户环境:`vim /etc/profile`
		```
		JAVA_HOME=/opt/jdk-15.0.1
		CLASSPATH=.
		PATH=$JAVA_HOME/bin:$PATH
		export JAVA_HOME CLASSPATH PATH
		```
		* 整个系统环境:`vim /etc/environment`
		```
		JAVA_HOME=/opt/jdk-15.0.1
		```
		* 只是sudo:` vim /etc/sudoers`
	3. 激活环境变量:`source /etc/profile`
	4. 验证环境变量:`echo $JAVA_HOME`
	5. maven:
		1. 安装: `sudo install maven`
		2. 使用pom.xml: `mvn install`
		3. 输出可直接执行的jar包:
			1. pom上设置:
				```
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
						<plugin>
							<groupId>org.apache.maven.plugins</groupId>
							<artifactId>maven-jar-plugin</artifactId>
							<version>3.1.0</version>
							<configuration>
								<archive>
									<manifest>
										<addClasspath>true</addClasspath>
										<classpathPrefix>lib/</classpathPrefix>
										<mainClass>Convertible_bond.AppApplication</mainClass><!--入口类，main-->
									</manifest>
								</archive>
							</configuration>
						</plugin>
						<plugin>
							<groupId>org.springframework.boot</groupId>
							<artifactId>spring-boot-maven-plugin</artifactId><!--要通过maven进行打包操作 需要这个插件-->
							<version>2.3.5.RELEASE</version>
						</plugin>
					</plugins>
				</build>
				
				<dependencies>
					<dependency>
						<groupId>org.apache.maven.plugins</groupId>
						<artifactId>maven-compiler-plugin</artifactId>
						<version>3.8.1</version>
					</dependency>
				</dependencies>
				```
			2. 打包出jar包:
				* 在target中生成:`mvn package`
				* 执行jar包:`java -jar 包名.jar`
		
	6. MySql:
		0. 基础命令:
			* 重启MySql:`sudo service mysql restart`
		1. 先进入MySql命令行:
			* 改密码:`set password for 用户名@localhost = password('新密码');`
			* 查看所有用户:`SELECT DISTINCT CONCAT('User: ''',user,'''@''',host,''';') AS query FROM mysql.user;`
			* 创建用户:`CREATE USER '用户名'@'localhost' IDENTIFIED BY '密码';`
			* 授权访问所有数据库:`grant all privileges on *.* to '用户名'@'localhost';`
			* 远程登录mysql:
				* 阿里云服务器中安全组规则需添加3306端口入方向
				* 设置数据库可以远程登录: `update mysql.user set host = '%' where user = 'root';`
				* 远程登录mysql:`mysql -h sinscry.space -u root -p`
				
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		