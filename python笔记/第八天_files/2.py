#coding:utf-8
class People(object):
    """docstring for People"""
    def __init__(self):
        print '创建了一个对象',self
     # 实例函数(对象函数),只能通过对象使用
     # 实例函数中的隐形参数是一个实例对象
    def test(self):
        print '这是一个实例函数(对象函数)'
    #使用实例对象函数必须先通过类创建对象，再由对象调用实力函数
    # 类函数 可以通过类直接调用，也可通过实例调用
    # 对象a执行该函数，cls表示对象a所在的类型
    # 类型A调用该函数，cls表示类型A
    @classmethod
    def class_test(cls):
        print '这是一个类函数',cls
    # 静态函数
    # 静态函数没有隐形参数，可以由类和对象调用,
    @staticmethod
    def static_test2():
        print '这是一个静态函数'
    @staticmethod
    def static_text3(a,b):
        print '执行了静态函数',a+b

p=People()
# 实例函数只能由对象调用
p.test()

# 使用类型直接调用函数
# 格式：类名.类函数名
People.class_test()
# 使用实例对象执行类函数
p.class_test()
# 对象执行静态函数
p.static_test2()
# 类执行静态函数
People.static_test2()
p.static_text3(6,9)
People.static_text3(6,9)


class People(object):
    """介绍实例函数、类函数、静态函数"""
    # init初始化函数，会在创建对象的时候自动调用
    def __init__(self):
        print 'People对象被创建了'
    # 实例函数，只能通过实例对象调用
    def eat(self):
        """
            self指的对象
            对象p的内存地址：0x00000000022D2EB8
            self的内存地址：    0x00000000022D2EB8
            self指的就是对象p

            对象A执行eat函数，在函数中self指的就是对象A
        """
        print '这是一个实例函数，执行吃饭功能',self

    # 想要不创建对象就能执行函数
    # 声明一个类函数，必带一个参数
    @classmethod
    def class_test(cls):
        """
        cls指的是类型
        类型A执行该类函数，cls表示类型A
        对象a执行该函数，cls表示对象a的类型
        """
        print '这是一个类函数',cls
    # 静态函数
    @staticmethod
    def static_test():
        """
        静态函数没有隐形参数
        静态函数可以由类和对象同时调用

        """
        print '这是一个静态函数'
# 创建People类一个对象，系统自动调用init初始化函数
p=People()
p.eat()
# 使用类型执行类函数
# 格式：类名.类函数名
People.class_test()
# 使用实例对象执行类函数
p.class_test()
# 调用静态函数
# 类型.函数名
People.static_test()
# 对象.函数名
p.static_test()
#静态函数和类函数都必须什么时候使用什么时候就立即创建，每次都得声明
"""
    实例函数、类函数、静态函数之间的区别：
    1.实例函数只能由对象调用，并且含有隐形参数，该参数表示调用函数的对象
    2.类函数可以由类和对象调用，并且含有隐形参数，该参数表示类型或者对象的类型
    3.静态函数可以由类和对象调用，没有隐形参数,可以有参数也可以没有参数

"""
