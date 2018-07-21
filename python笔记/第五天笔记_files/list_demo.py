#coding:utf-8

# 列表：可以存储任意类型的数据，列表具有增删改查功能

# 声明列表
# 把要存储的数据用[]括起来，每条数据之间用,逗号隔开
list_1 = [1,'zhangsan',True,3.1415926]

# 添加数据
# 1.追加数据，追加的数据是在列表的末尾位置
# append 追加
list_1.append({'name':'zhangsan'})
print list_1
list_2 = ['lisi',3,5.5]
# 2.extend 扩展 
# 将一个可迭代的对象完整的添加到列表中，添加的数据是在列表的末尾位置
list_1.extend(list_2)
print list_1
# 列表中的每一条数据都用自己的索引，第一个数据的索引为0，第二个为1，以此类推
# 3.insert 插入
# 索引值如果超出列表范围，默认加在最后
list_1.insert(2,'hello')
print list_1

#  -------------查询数据--------------

# 根据索引取出列表中某个数据
# 索引越界
# IndexError: list index out of range
s  = list_1[2]
print s
print list_1

# pop：根据索引取出对应的数据，取出之后，会列表中的数据移除
s = list_1.pop(2)
print s
print list_1

# 查询列表中所有的数据,泛型遍历
for obj in list_1:
    print obj

# 利用for循环取出某个范围之内数据
for x in xrange(1,5):
    obj = list_1[x]
    print obj
    
# -----------------删除数据--------------
# 1.del 删除列表的中的数据
# 索引越界
# IndexError: list index out of range
del list_1[1]
print 'del  删除索引1 ：',list_1
# 2.remove函数删除，根据数据内容删除
# ValueError: list.remove(x): x not in list：原因：列表中不存该数据内容
list_1.remove('lisi')
print 'remove 删除：',list_1
# 3.del 把整个列表删除,之后就不能在使用该列表，否则会触发异常
# del list_1
# print 'delete list_1 .......'
# print list_1

list_2 = ['zhangsan','lisi','wangwu','zhaoliu']


# 4.利用for循环删除列表中所有的数据内容,利用while循环删除同理
for x in range(len(list_1)):
    del list_1[0]

print 'for循环删除列表所有内容',list_1



# 反转,将列表中的内容进行反向排序
list_2.reverse()
print list_2

# sort：排序函数
list_3 = ['z',4,6,9,4,'a',43,4,74,3,'A',2458,56]

# reverse参数决定了排序使用的方式：升序、降序
list_3.sort()

print list_3

# count：计数，统计某个值在列表中出现的次数
print list_3.count(4)





# print list_1[15]




