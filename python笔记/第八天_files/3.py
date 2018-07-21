#coding:utf-8(object):
class People (object):
    """docstring for ClassName"""
    # 类变量：在整个实例化的对象是公用的
    # 一般使用，类名.变量名，不会使用对象.类变量名，为了防止值修改的时候只修改某个对象的值
    create_count = 0

    def __init__(self, name,age ):
        self.name = name
        self.age=age
        # 利用类名.类变量名更改类变量值
        People.create_count+=1
p_1=People('zhangsan',22)
#第一次创建p_1对象
print People.create_count ,p_1.create_count
p_2=People('wanwu',25)
# 第二次创建p_2对象
print People.create_count,p_2.create_count
p_3 = People('lisi',44)
print p_1.create_count,p_2.create_count,p_3.create_count
#类变量对类中所有的对象是公用的，都是一样的


#私有变量，私有函数
class People(object):
    """docstring for People"""
    #声明私有变量：变量名称前加__双下划线
    #私有变量只能在当前类中使用
    #__变量名
    __private_age=30
    age=10#公有变量
    def __init__(self):
        print '在当前类中使用私有变量',People.__private_age
        #在当前类中使用私有变量
        self.__test()
    #声明私有函数：函数名前加__双下划线
    def __test(self):
        print '这是一个实例函数'
# 创建People类一个对象
p=People()
# 在类外不能访问私有函数
# p.__test()
print p.age
# 在类的外面访问私有变量是不允许的
# print p.__private_age
# print People.__private_age 
# 可以通过间接的方式访问类的私有变量值
# 格式：对象._类名+私有变量名
print'间接方式得到的私有变量: ' ,p._People__private_age




        