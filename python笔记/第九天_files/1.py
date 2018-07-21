#coding:utf-8
class People(object):
    """docstring for People"""
    def __init__(self, age):
        # 判断某个对象是不是某种类型,返回bool类型的结果
        # isinstance(对象，类型)
        # 如果age的值不是整数类型
        if not isinstance(age,int):
            raise ValueError('age must be an int')
        # 如果age小于等于0或者大于120，不符合范围
        if age <=0 or age >120:
            raise  ValueError('age must be between 0~120')
        self.age = age

    # 单独写一个函数，专门用来给属性赋值
    def set_age(self,age):
        if not isinstance(age,int):
            raise ValueError('age must be an int')
        if age <=0 or age >120:
            raise  ValueError('age must be between 0~120')
        self.age = age
        # 单独写一个函数，专门获取属性值
    def get_age(self):
        
        print '执行了get_age函数'
        return self.age

p_1 = People(3)
print p_1.age 
p_1.age=100
print p_1.age
# 执行函数设置属性值 
p_1.set_age(100)
print p_1.age
# 执行函数获取属性值
p_2=p_1.get_age()
print p_2


class People(object):
    """docstring for People"""
    # 对象.函数名
    # @property 把某个函数转换为属性的调用方式
    @property
        # 获取属性值的函数
    def age(self):
        try:
            print '执行了@property后的age函数'
            return self.__age
        except AttributeError, e:
            return 0
    # 描述信息
    # 设置属性值的函数
    # 给age属性声明设置属性值的函数
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
             raise ValueError('age must be a int value')

        if value <= 0 or value > 120:
            raise ValueError('age out of range ,range is 0~120')
        self.__age  = value
p = People()
p.age =90

p=p.age
print p

class People(object):
    def __init__(self,is_smoking):
        # 声明私有属性
        self.__is_smoking = is_smoking

    # @property 把某个函数转换为属性的调用方式
    @property
    # 获取__is_smoking属性值的函数
    def is_smoking(self):
        return self.__is_smoking
    # 描述信息
    # 设置属性值的函数
    # 设置__is_smoking属性值的函数
    @is_smoking.setter
    def is_smoking(self,value):
        if not isinstance(value,bool):
            raise ValueError('value must be an bool value')
        self.__is_smoking = value
        # 除了赋值之外，还可以添加新的功能
        if value == True:
            print '这个人抽烟'
        else:
            print '这个人不抽烟'


p = People(False)
# 对象.属性名 = 值   实际上是执行设置值is_smoking函数设置__is_smoking的值
p.is_smoking = True

#  XXX = 对象.属性名 实际上是执行获取值的is_smoking函数获取__is_smoking的值
isSmoking = p.is_smoking



print p.is_smoking



#只读属性
class People(object):
    """docstring for People"""
    def __init__(self):
        # 私有属性
        self.__sex = '男'
     # 只读属性
    # @property 只写一个获取属性值的函数
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self,value):
        # 一旦执行该函数，则触发异常说明这是一个只读属性
        raise AttributeError('This Attribute is readonly!')
p=People()
p.sex='女'
print p.sex