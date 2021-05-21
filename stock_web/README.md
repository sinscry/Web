#### Data_analyst_web

* 他山之石：https://www.doctorxiong.club/#/stock/detail

* 初步逻辑:
	* 基本资料:
		* 服务器地址: 120.78.209.24
			* maven构建执行包:
				1. 构建jar执行包：`mvn package`
				2. 进入target：`cd target`
				3. 执行jar包：`sudo java -jar Data_analyst_web-1.0-SNAPSHOT.jar`
		* 域名:sinscry.space
		* 股票数据来源:
			* 可选债:https://www.jisilu.cn/data/cbnew/#cb
			* 新浪股票api:https://www.jianshu.com/p/108b8110a98c
			* 历史股票数据（搜狐）：https://www.cnblogs.com/ldlchina/archive/2004/01/13/5392670.html
		* 远程MySql数据库的数据表: stock_usr.usrs;
	0. 当前目标:
		* 构建选股网站（www.sinscry.space:80/stock）:
			* 界面用materilize实现
			    1. MySQL数据库的stock_usr.usrs记载数据:
					* 远程MySql:`mysql -h sinscry.space -u sinscry -p`
			        * `create database stock_usr`
			        * 数据结构:(usr,stock_id,stock_nm,oprice)//对应(用户，代码，股名，购入价)
		            * 建表	        
						```
						CREATE TABLE IF NOT EXISTS stock_usr.usrs(
							usr varchar(30),
							stock_id varchar(20),
							stock_nm varchar(20),
							oprice double,
							update_time timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
							id bigint(20) NOT NULL AUTO_INCREMENT COMMENT '自增长id',
							PRIMARY KEY (`id`),
							KEY `key_usr` (`usr`)
						)
						```   
                   * 插入数据:`INSERT INTO stock_usr.usrs (usr,stock_id,stock_nm,oprice) VALUES   ("梁鸿振","sh600000","浦发银行",9.717);`
				   * 删除数据:`delete from stock_usr.usrs where usr=“测试”`
				   INSERT INTO stock_usr.usrs (usr,stock_id,stock_nm,oprice) VALUES   ("意愿","sh600000","浦发银行",1);
				   INSERT INTO stock_usr.usrs (usr,stock_id,stock_nm,oprice) VALUES   ("梁鸿振","sz002597","金禾实业",39.68);
				2. 使用mybatis查询数据
					* name,stock_id,stock_nm,oprice在MySQL数据库取
					* sprice(现价)通过新浪股票api:`String sprice=Client.get("http://hq.sinajs.cn/list="+stock_id).split(",")[3];`
					* 构建目标json:
						```
						//查询结构
						//String name='梁鸿振'
						//String stock_list = "[{'stock_id':'sh600000','stock_nm':'浦发银行','sprice':'9.72','oprice':'9.71'}]";
						String Result_json="[{'name':'"+name+"','stock_list':"+stock_list+"}]";
						JSONArray jsonArray = JSONArray.parseArray(Result_json);
						return jsonArray.toString();
						```
			3. 添加访问日志（logback）
			5. 添加点评区（双击击可修改的那种）
				1. 在mysql建立新表特地存放点评（根据不同用户显示）
				2. 添加时可以设置
				3. 自动绑定
			6. 到目标股价发邮箱提醒
				1. 定时查询
				2. 自动计算
				3. 邮件发回
			7. 设置实操和意愿根据用户列（如lhz意愿+实操）
			9. 添加交易历史日志
			10. 开头显示大盘数据
			13. 美国国债利率实时数据
				* url:https://cn.investing.com/rates-bonds/government-bond-spreads
					
	1. done需求
		1. 显示可转债按正转比排序：(done)
		2. 显示本人选股和价格：(done)
		3. 添加持仓数据功能:(done)
		4. 删除持仓数据功能:(done)
		5. 添加跳转股票数据链接(done+用的是雪球网:https://xueqiu.com/S/sz000060)
		6. vue更改购入价限制，从大于0改成大于等于0(done)
		7. 添加icon(done)
			* 生成图标网站:https://tool.lu/favicon/
			* 必须重命名为favicon.ico
			* 放在 main/resources/static下
		8. 在选股隔壁放大盘指数(done)
			* 上证:http://hq.sinajs.cn/list=s_sh000001
			* 深证:http://hq.sinajs.cn/list=s_sz399001
				
* 拓展思维
	* 相关性分析美债和A股
			
	