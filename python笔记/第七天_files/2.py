#coding:utf-8
# 集合(可以利用集合做除重操作，因为集合有互异性)
# python中集合是无序，集合中不会出现相同的数据
# 创建集合:set 后面的（）内传入可迭代的对象
# 根据字符串创建集合，字符串会进行分割，每个字符都是一个单独的数据，并且不会相同的字符出现
set_1=set('hello')
print set_1
# 执行结果:set(['h', 'e', 'l', 'o'])
#列表创建集合
set_2 = set([1,2,3,4,5,6])
print set_2
#执行结果：set([1, 2, 3, 4, 5, 6])
#元组创建集合
set_3=set((1,9,'hello',5,6,8))
print set_3
#执行结果：set([1, 5, 6, 8, 9, 'hello'])
#字典创建集合，只会字典中的key放在集合中
set_4=set({'name':'zhangsan','age':15,'sex':1})
print set_4
#执行结果set(['age', 'name', 'sex'])
#总结，新创建的集合形式为set([ 中间放的是集合中的元素])
#集合的添加：
#add添加:把要添加的数据看做是一个整体添加,add 做的只是添加的操作这个动作add不能添加列表
set_2.add((1,2,3))
print 'add后：',set_2
# add后： set([1, 2, 3, 4, 5, 6, (1, 2, 3)])

#update（更新）：把要添加的对象拆分进行添加加入
set_2.update([45,56,98])
print 'update后：',set_2
# update后： set([1, 2, 3, 4, 5, 6, 45, (1, 2, 3), 56, 98])
#for循环遍历查询集合
for x in set_2:
    #输出所有集合的元素
    print x
#集合的交集，合集，补集
#交集:&
res_set=set_2&set_3#交集
print '交集',res_set
# 交集 set([1, 5, 6])
#合集
res_set=set_2|set_3#合集
print res_set
# set([1, 2, 3, 4, 5, 6, 8, 9, 45, (1, 2, 3), 56, 98, 'hello'])
#补集;-
res_set=set_2-set_3#补集
# set3相对于set2的补集
print '--->',res_set
# set([2, 3, 4, 98, 45, (1, 2, 3), 56])
#全局变量，在整个文件中的任意函数内都可以使用
# 在函数内使用、修改全局变量的值,必须先声明
    #global name 
name = 'zhangsan'
def test(nick_name):
    # 函数内声明的变量，局部变量，作用域范围是从声明的位置开始，直到函数结束
    # 函数中的name是一个局部变量
    # name = nick_name
    global name
    # 声明该变量是一个全局的变量
    name=nick_name
    print '函数内的name：',name
test ('lisi')
print '函数外的name：',name
def test_2(string):
    global name
    name = string

test_2('wangwu')

print '测试2:',name
#异常捕获
# 异常:也是一个事件，如果执行程序时，出现无法继续执行下去的情况，发生了一个异常事件，程序不会再继续执行下方的代码
list_1 = [1,2,3]
#try except 捕获异常  基本格式
#捕获所有的异常
try:
    list_1[4]
except :
    print '你的程序出错了'
    # try:
    #     pass
    # except Exception, e:
    #     raise e
    # else:
    #     pass
# Exception :指明要检测的异常错误
# e：异常错误信息
 #     raise e 是触发异常信息
 # 当try中代码没有异常时，执行else后的代码
try:
    list_1[1]
except IndexError, e:
    print e
else:
    print '这是else后的代码'

# Exception参数可以填写多，检测多种异常信息,用()括起来，每个异常之间用逗号隔开,如果异常没在检测的异常范围内，它会自己触发异常
try:
    list_1.zhangsan()
except (IndexError,ValueError,AttributeError), e:
    # 自己处理异常的代码
    print '异常错误原因：',e 
else:
    pass

# 无论是否发生异常都会执行finally后的代码，执行完finally后的代码，再触发异常
try:
    list_1[1]
finally:
    print '这是finally后的代码'

print '这是捕获异常之后的代码'
# 自己触发异常信息
# raise+ 异常错误的类别+('异常错误原因',跟踪错误的对象)
def calc_test(x):
    if x == 0:
        raise Exception('x is not 0!')

    print 10/x

calc_test(0)
