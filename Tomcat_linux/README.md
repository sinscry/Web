# Tomcat_linux
linux系统下配置Tomcat教程
* 我的服务器地址:120.78.209.24

* 配置步骤：
	* java 配置:
		1. 安装java:
			* `sudo apt update`
			* `sudo apt install openjdk-11-jdk`
		2. 设置JAVA_HOME表示java位置:
			1. 找到java安装路径:`sudo update-alternatives --config java`
			2. 打开/etc/environment文件:`sudo vim /etc/environment`
			3. 在文件末尾加上:`JAVA_HOME="/usr/lib/jvm/java-11-openjdk-amd64/bin/java";`
			4. 生效shell:`source /etc/environment`
			5. 验证JAVA_HOME环境变量:`echo $JAVA_HOME`
			
	* Tomcat配置:
		1. 创建tomcat文件夹:`sudo mkdir /usr/local/tomcat`
		2. 下载Tomcat包( 官网:http://tomcat.apache.org/download-70.cgi ):`sudo wget https://apache.website-solution.net/tomcat/tomcat-7/v7.0.106/bin/apache-tomcat-7.0.106.tar.gz`
		3. 解压Tomcat包:`sudo tar -zxvf apache-tomcat-7.0.106.tar.gz`
		4. 给予用户所有访问权限:`sudo chmod -R 777 ./apache-tomcat-7.0.106`
		5. 进入文件夹:`cd /usr/local/tomcat/apache-tomcat-7.0.106/bin/`
		6. 开启tomcat服务:`./catalina.sh start`
		7. 配置服务自启动:
			1. 配置服务名
				1. 增加文件:`sudo vim /etc/init.d/tomcat` 
				2. 编辑tomcat文件:
					```
					#!/bin/bash
					# description: Tomcat7 Start Stop Restart
					# processname: tomcat7
					# chkconfig: 234 20 80
					### BEGIN INIT INFO

					# Provides:          tomcat

					# Required-Start:    $remote_fs $network

					# Required-Stop:     $remote_fs $network

					# Default-Start:     2 3 4 5

					# Default-Stop:      0 1 6

					# Short-Description: The tomcat Java Application Server

					### END INIT INFO

					CATALINA_HOME=/usr/local/tomcat/apache-tomcat-7.0.106

					case $1 in
							start)
									sh $CATALINA_HOME/bin/startup.sh
									;;
							stop)
									sh $CATALINA_HOME/bin/shutdown.sh
									;;
							restart)
									sh $CATALINA_HOME/bin/shutdown.sh
									sh $CATALINA_HOME/bin/startup.sh
									;;
							*)
									echo 'please use : tomcat {start | stop | restart}'
							;;
					esac
					exit 0
					```
				3. 赋予访问权限：`cd /etc/init.d/`->`sudo chmod 777 ./tomcat`
				4. 注册服务:`sudo update-rc.d tomcat defaults`
			2. 服务指令：
				* 启动:`service tomcat start`
				* 停止:`service tomcat stop`
				* 重启:`service tomcat restart`
			3. 配置自启动:
				1. 向chkconfig添加 tomcat 服务的管理:
					1. 添加源:
						* `cd /etc/apt`
						* `vim sources.list`添加:`deb http://archive.ubuntu.com/ubuntu/ trusty main universe restricted multiverse`
						* `sudo apt-get update` -> `sudo apt-get install sysv-rc-conf `
					2. 更名:`cp /usr/sbin/sysv-rc-conf /usr/sbin/chkconfig`
					3. 赋予权限:`chmod 755 chkconfig`
				2.`chkconfig --add tomcat`
				3. 设置tomcat服务自启动:`chkconfig tomcat on`
				4. 查看tomcat的启动状态:`chkconfig --list | grep tomcat`
			
			4. 部署web项目:
				* 进入tomcat下的webapps目录
				* 把web项目打包出来的war拷贝并解压
				
				
				
				
				
				
				