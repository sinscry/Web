# Vue心法

1. 基础教程:
	0. 安装:
		* <script src="https://cdn.staticfile.org/vue/2.2.2/vue.min.js"></script>(国内)
		* <script src="./js/vue.min.js"></script>(本地)
		* <script src="https://unpkg.com/vue/dist/vue.js"></script>(国外)

	1. 插值:
		* 插值.html
		* 重点:双向绑定
		<input v-model="v_model">
	2. 条件判断:
		* 插值.html
		* 重点:序号4
		<p v-if="use">now u see me</p>
	3. 循环:
		* 循环.html
	4. 监听:
		* 监听.html
	5. 样式绑定:
		* 插值.html
		* 重点:序号3
	6. 事件处理:
		* 事件处理.html
	7. 表单:
		* 表单.html
	8. ajax:
		* Ajax.html
	
	9. 函数传参:
		* Vue写法
		```
		axios_add_stock:function (name,stock_id,oprice){
            console.log(name,stock_id,oprice);
            axios.post("/axios_add_stock",{
                name:name,stock_id:stock_id,oprice:oprice
            }).then(res=>(alert(res.data)))
       }
	   ```
	   * SpringBoot写法:
		```
		@RequestMapping("/axios_add_stock")
		@ResponseBody
		public String axios_add_stock(@RequestBody axios_add_stock axios_add_stock){
			return axios_add_stock.getStock_id();
		}
		```
	10. 界面刷新:
		* 不访问服务器:`this.$forceUpdate();`
		* 访问服务器:`location.reload();`
	11. vue<a>跳转带参数:
		* `<a :href="'https://xueqiu.com/S/'+s.stock_id" target="_blank">`
		* 其中s.stock_id是变量

2. 问题	
	1. axios请求出错:
		* CORS（跨域存取问题）:
			* 前端无法解决，通过后端取
			* 在服务器添加允许跨域存取的许可：
				* Controller设置允许跨域访问：@CrossOrigin
			* 后台Http请求转发：
				```
				HttpClient client = HttpClients.createDefault();            //client对象
				HttpGet get = new HttpGet("http://localhost:8080/test");    //创建get请求
				CloseableHttpResponse response = httpClient.execute(get);   //执行get请求
				String mes = EntityUtils.toString(response.getEntity());    //将返回体的信息转换为字符串
				System.out.println(mes);
				```
		* axios是异步操作：
			* 通过await async方式进行同步:
			```
			axios_sim_stock:async function (url) {
				var tmp;
				await axios.get("/axios_sim_stock", {params: {url: url}})
				   .then(function (res) {
					   tmp=res.data;
				   });
				return tmp;
	 	    }
			```
			* 直接返回会是promise object(要用then):
			```
			this.axios_sim_stock("http://hq.sinajs.cn/list=s_sh000001").then(v=>{
				that.sh_sz.sh_exp=v.split(",")[1];
				that.sh_sz.sh_ch=v.split(",")[3];
			});
			```
			
			
			