#coding:utf-8
#列表解析
#表达式书写格式
#[最终添加到列表中的对象+空格+要迭代的语句],无论迭代对象是什么类型，最终返回的是一个列表
string='afdgfhgdvbdzargh'
list_1=[x for x in string ]
print list_1
list_2=[{'name':'zhangsan','age':'11'},{'name':'zhaosi','age':'52'}]
list_3=[dict_1.items() for dict_1 in list_2]
print list_3
#表达式版
# [最终添加到列表中的对象（可以是一个表达式）迭代表达式 判断表达式]
list_1=[x*x for x in range (10) if x %2==1]
print list_1
string_1 = '1234567890'
# if判断条件筛选
list_3 = [sub for sub in string_1 if sub == '1']

print list_3
