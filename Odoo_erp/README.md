# Odoo 公司系统安装教程
* 相关网站教程:https://www.cnblogs.com/a5idc/p/13710150.html
![Image text](./bg.jpg)

1. 更新系统软件包
	* `sudo apt update`
	* `sudo apt upgrade`
	* `sudo apt install git python3-pip build-essential wget python3-dev python3-venv python3-wheel libxslt-dev libzip-dev libldap2-dev libsasl2-dev python3-setuptools node-less`

2. 安装PostgreSOL（Odoo指定数据库）
	1. `sudo apt install postgresql postgresql-client`
	2. 服务配置
		* 判断服务是否运行：`systemctl status postgresql.service`
		* 若没有开启：`sudo /etc/init.d/postgresql start`
	3. PostgreSQL数据库用户创建：
		* `sudo su postgres`
		* `createuser --createdb --username postgres --no-createrole --pwprompt USERNAME(用户名)`
	4. psql添加用户权限:
		* `psql`进入模式
		* `\du`查看用户
		* `alter user USERNAME with superuser`添加权限(superuser和createdb)
		* `createdb stable --encoding=UNICODE`
		
3. Odoo安装
	1. 下载odoo：`git clone https://www.github.com/odoo/odoo --depth=1 --branch 14.0 --single-branch`
	2. 进入odoo文件夹：`cd odoo`
	3. 安装依赖文件：
		* lxml和pillow依赖:
			* `sudo apt-get install libxml2-dev libxslt-dev`
			* `sudo apt-get install python3-lxml`
			* `sudo apt-get install libjpeg8 libjpeg62-dev libfreetype6 libfreetype6-dev`
			* `sudo apt-get install postgresql`
			* `sudo apt-get install python-psycopg2`
			* `sudo apt-get install libpq-dev`
		* `pip3 install -r requirements.txt`
		
4. 安装Wkhtmltopdf
	* `sudo apt-get install xvfb`
	* `sudo apt-get install wkhtmltopdf`
	* `sudo strip --remove-section=.note.ABI-tag /usr/lib/x86_64-linux-gnu/libQt5Core.so.5`
	* 打印中文:
		1. `sudo apt-get install ttf-wqy-zenhei`
		2. `sudo apt-get install ttf-wqy-microhei`
	* `wkhtmltopdf http://www.baidu.com/ baidu.pdf`
	
5. 授予访问权:`sudo chmod 775 odoo-bin`

6. 初始化`./odoo-bin -d sinscry`(PostgreSQL数据库用户名)

7. 使用:
	* 确保PostgreSQL开启:`sudo /etc/init.d/postgresql start`
	* 开启odoo-bin服务`./odoo-bin`
	* 端口:`localhost:8069`
	
8. 打印模板：https://www.cnblogs.com/1314520xh/p/7268899.html
	* 可以用万兴pdf进行修改