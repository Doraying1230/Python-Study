#coding:utf-8
#使用sqlite3，需要先引入该包
import sqlite3
#connect()连接到某个数据库文件， .db：数据库文件后缀
# 如果连接的数据库文件不存在，则在当前目录创建该文件
# 接收数据库连接对象
conn = sqlite3.connect('database.db')
# 创建操作数据库文件的游标
 conn.cursor()
 # 接收数据库文件的游标
 cursor = conn.cursor()
 # 准备sql语句
 # primary key 设置主键 非空 唯一 如果主键是integer类型，那么主键是自增的
 # integer 整数 float浮点  boolen布尔 text字符串
 # 创建表的sql语句
 # sql="create table Student(id inteder primary key,name text,age integer"
 # 删除表的sql语句
 # sql="drop table  Student"
 # 插入数据的sql语句
 # sql="insert into Student(id,name,age) values(1,'zhangsan',22)"
 # 准备执行sql语句
 cursor.execute(sql)
 # 关闭cursor游标
 cursor.close()
 # 提交操作
 conn.commit()
 # 关闭数据库连接
 conn.close()

# 删除的sql语句
    # and 多个条件成立  or一个条件成立即可
    sql = 'delete from Student where id>2 and id<6'
sql = "update Student set name='%s',age = %d where id = 2"%(name,age)



# sql = 'insert into Student (name,age) values (?,?)'
# 准备执行sql语句
# unicode 对中文字符进行编码 (unicode(name,'utf-8')
# cursor.execute(sql,(unicode(name,'utf-8'),age))

# 准备sql语句
# 拼接好sql语句
# 
 a=sql = 'select * from Student'
   # 查询时，会返回 一个cursor对象，该对象中放的就是查询的结果# 类似于容器类。存放 结果(以元组的形式存放的)
for遍历查询所有数据
for x in a:
    print x
# 直接取出元组中的数据
for id,name,age in a:
    print id,name,age
# 张% 匹配以张字符开头的数据
    # %丰 匹配以丰字结尾的数据
    # %三% 匹配包含三字符的数据
    # 张_ 匹配以张开头并且匹配张后的一个字符
    # __丰 匹配以丰字符结束，并且匹配丰前2个字符的数据
conn.execute() = conn.cursor().execute()
#execute()函数本身已经创建了游标，不用再写创建游标的函数
# 为了不写关闭的数据库的操作
        # 使用该语法可以自动关闭数据库，同时也关闭了游标
with self.connect() as conn:
    # conn.execute(sql) 执行一条sql语句
 #conn.executescript() 执行多条sql语句,用分号;隔开每个sql语句
conn.executescript(sql_1+';'+sql_2)








