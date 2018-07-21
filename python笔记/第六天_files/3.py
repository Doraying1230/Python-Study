#coding:utf-8
#列表解析
string='asdifffgg'
[ ]
list_1=[x for x in string]
print list_1
list_2=[x*x for x in range(20) if x%2==1]
print list_2
#map函数(某个函数,可迭代的对象)
# 将可迭代对象中的每一个数据都执行一遍函数,并且以列表的形式返回
# 1.某个函数
# 2.可迭代的对象
# 将可迭代对象中的每一个数据都执行一遍函数,并且以列表的形式返回
list_3=map(lambda x:x*2,string)
print list_3
list_4=filter(lambda x:x if x%2==1 else None,[x for x in range(100)])

print list_4
list_5=filter(None ,[x for x in string])
print list_5
list_6=filter(lambda s: s if s!='i' else None ,string)
print list_6
# lambda s:s if s!='l' else None 传入一个s参数，判断s是否为字符串'l',如果不是则条件正确返回，如果是则返回空值

# filter条件筛选器,(某个函数，可迭代的对象)可迭代对象除了元组和字符串返回本身的类型之外，其他的都返回列表

'''
    1.函数(函数中添加筛选条件)
    2.可迭代的对象
    filter(function or None, sequence) -> list, tuple, or string
    返回符合判断条件的数据
    Return those items of sequence for which function(item) is true. 
    如果函数为空，返回所有为真的数据
     If function is None, return the items that are true.  
     如果序列是元组或字符串，返回相同的类型，否则返回一个列表。
     If sequence is a tuple or string, return the same type, else return a list.
     ''' 
# 结合map+lambda
# map可以传递多个参数，但是需要注意，对应的函数也应该拥有对应的参数
list_obj=map(lambda x,y:x+y,range(10),range(10))
print list_obj
# filter + lambda + 列表解析
list_number=filter(lambda x:x if x%2==1 else None,[x for x in xrange(1000)])
print list_number 