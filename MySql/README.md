#### 数据库基础
mysql版本:`select version();`

1. ##### 数据类型:
    * int
    * varchar(20)

2. ##### 数据库
    + 连接数据库:`mysql -u root -p`
    + 查询数据库:`show databases;`
    + 使用数据库:`use 数据库名;`
    + 创建数据库:`create DATABASE RUNOOB`
    + 查看当前所在数据库:`select database();`

3. ##### 数据表
    1. 查询操作:
        + 查询所有表:`show tables;`
        + 查询指定数据库的表:`show tables from 数据库名;`
        + 查询表的结构:`desc 表名`
        + 查询表中数据:
            1. 所有：`select * from 表名;`
            2. 单列：`select id from 表名;`
            3. 多列：`select id,name from 表名;` 
            4. 常量：`select id;`
            5. 表达式：`100%98;`
            6. 函数:`select version();`
            7. 起小名：
                *  `select id As 序列号, name As 名 from 表名`
                *  `select id 序列号, name 名 from 表名`
                * 合成：`select concat(last_name,firstname) As 姓名 from 表名`
                    - 若为空则变为梁:`ifnull(last_name,'梁')`
            8. 不重复：`select distinct id from 表名` 
        + 条件查询：
            * 精准查询：
                1. `SELECT * FROM 表名 WHERE id >= 1 AND last_name='again';`
                2. `SELECT * FROM 表名 WHERE id BETWEEN 2 AND 1;`
            * 模糊查询：
                + 含特定字符即可：`SELECT * FROM 表名 WHERE last_name LIKE '%a%';`
                + 字符顺序也得相同：`SELECT * FROM 表名 WHERE last_name LIKE 'a_a%;`
    
    2. 更改操作:
        + 创建表: 
        ```
        create table 表名(
        id int primary key,
        name varchar(20),
        status int default 1,
        );
        ```
        + 删除表:`drop table 表名;`
        + 清空表:`truncate table 表名;`
        - 插入新的行:`insert into 表名(id,name) values(1,'john);`
        + 插入新的列:`alter table 表名 add 列名 数据类型;`
        + 更新数据:`update 表名 set name='lilei' where id=1;`
        + 删除数据:`delete from 表名 where id=0`
        + 列操作:
            1. 设置主键:`alter table 表名 add primary key(id)`
            2. 更改字段长度:`ALTER TABLE 表名 MODIFY COLUMN id VARCHAR(50);`


4. ##### pymysql
    + message = cursor.fetchall() # 数据提取
