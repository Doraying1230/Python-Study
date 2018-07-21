#coding:utf-8
#什么叫做函数？
# 人：吃喝拉撒睡
#函数（功能，方法）：需要多次执行的代码，并且是以模块化的形式书写
#type()查看某个对象的类型
#在Python中，万物皆对象
#怎么声明一个函数？
#def（define定义）def是关键字
#()是参数列表
#函数名称：必须以字母开头，每个单词之间用_隔开，名称要有含义，做到见名知意
#def 函数名称(参数列表):
def eat():
    print '执行了eat函数'
    
#函数的调用
#函数只有被调用才执行，
eat()
#假如函数没有返回值，默认函数返回None值
    #return，一旦函数遇到return，表示该函数结束，return下方的代码不会再执行了
def eat_1():
    
    return(2)
b=eat_1()
print b

#带参数的类型
#功能需求：买水函数，买水用到钱，把钱作为参数传到函数中
'''
money=1  买康师傅矿泉水
money=2  买农夫山泉水
money=10 买恒大冰泉水
'''
# 参数名：必须以字母开头，每个单词之间用_隔开，名称要有含义，做到见名知意
def buy_water (money):
    '''
    对函数的描述文本
    参数：
    money：买水所需要的钱
    使用方法：
    method.buy_water(money)
    '''

#多个参数之间用逗号隔开
#必备参数：只要调用该函数，必须把所有参数传递进去
def my_sum(a,b,c):
    '''
    函数说明文档

    '''
    print a+b+c
#执行多参数函数
my_sum(1,2,3)
#缺省函数
#缺省参数不要求所有的参数都必须传递，但是需要设置缺省函数的初始值
def print_soming(name,age=25):
    print name,age
#执行函数
#缺省参数可以不用进行传递
print_soming ('zhnegshuo')
#缺省参数传递则覆盖缺省参数初始值
print_soming('zhangsan',50)
#不定长参数
def my_sum(a,*tuple_1):
    '''
    函数文本说明
    '''
    print a
    #tuple_1元组，假如想要取出所有的参数，需要进行遍历
    for x in tuple_1:
        print x
my_sum(10,'hello',2,True,4,5)
#关键字参数
def method_1(name,age ):
    '''
    函数文本说明

    '''
    print name, age
#使用关键字传递参数，可以不按照定义函数时参数的顺序传递
method_1(age=19,name='zhangsans') 
#不定常数的加法运算
def sum_1(a,*tuple_2):

    '''
    函数说明
    '''
    #让所有的参数累加，输出结果
    number=a
    #用for循环遍历元组中所有的参数
    for x in tuple_2:
        #累加
        number+=x
    print number 
sum_1(10,32,23,454,55,67,8980)   
#带有返回值的函数
def eat():
    #函数执行完毕，返回执行结果
    return '今天你吃了吗？'
#声明变量，接受函数返回的结果
result=eat()
print result
#计算多个数字的和
def sum_5(a,*tuple_3):
    number =a
    for x in tuple_3:
        number+=x
    #把number作为结果返回
    #功能1：返回结果
    return number
#创建变量接受函数返回的值
result_num=sum_5(10,45,56,15)
#匿名函数
#lambda关键字创建匿名函数
#lambda参数列表：函数返回结果（运算公式）
sum_9=lambda a,b:a*b
#调用匿名函数
result_number=sum_9(10,20)
print result_number
'''
使用匿名函数的好处
1.匿名函数不需要起函数名称，使用起来方便。只需要一句话就可以定义一个函数
2.方便以后维护和管理函数
3.非常符合Python特性，简洁，人生苦短，用Pytho
'''
# 作业：写一个函数，传进来一个整数list，返回一个新的列表，新的列表中，new_list[0]是新列表中的最小值，new_list[-1]是新列表中的最大值

