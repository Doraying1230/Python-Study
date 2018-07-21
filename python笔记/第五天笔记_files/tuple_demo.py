#coding:utf-8

# 元组，容器类，可以存任意类型的数据，不具有增删改的功能
# 元组声明方式，存储的数据用()括起来，每条数据中间用，逗号隔开
tuple_1 = (1,2,'zhangsan',3.14)

# 根据索引查询元组中的数据，索引从0开始
print tuple_1[0]

# TypeError: 'tuple' object does not support item assignment ,注意：元组中的数据不允许修改
# tuple_1[2] = 'lisi'

# 遍历查询；同列表
for x in tuple_1:
    print x

# index查询存储数据在元组中的索引
# ValueError: tuple.index(x): x not in tuple :原因：元组中没有该数据内容，检查该内容是否写错
print '元组中2的索引为',tuple_1.index('zhangsan')

# 可以把一个列表转换为元组
l = [1,2.1,3,4]
tuple_2 = tuple(l)
print tuple_2

# 元组转换为列表
l_1 = list(tuple_2)
print l_1





