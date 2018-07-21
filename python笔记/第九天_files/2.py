#coding:utf-8
# 什么叫做继承？
# 皇帝死了，太子继位
# class 类名(父类):
# 只是object 指的一个基类（最基础的类）
class People(object):
    """docstring for ClassName"""
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age 
        self.sex = sex
    def run(self):
        print '这是People中的run函数'
class Man(People):
    """docstring for ClassName""" 
    # 1.子类继承自父类，子类拥有父类的所有属性和函数
    def __init__(self,name,age,sex,g_f):
        # super(Man,self).__init__(name,age,sex)

        self.g_f=g_f
        # 使用类型执行实例函数
        People.__init__(self,name,age,sex)
        # 2.子类继承自父类，子类可以拥有自己的属性和函数
        self.g_f=g_f
    def smoking(self):
        print '这是Man中的smoking函数'

p=People('zhansan',12,1)
print p.name,p.age,p.sex
# people对象使用run函数
p.run()
# 3.子类继承自父类，父类不可以使用子类的属性和函数
# print p.g_f
# p.smoking()
m = Man('lisi',33,1,'xiaofang')
# 子类可以直接使用父类的函数
m.run()
m.smoking()
# 子类可以直接使用父类的属性
print m.name,m.age,m.sex,m.g_f

# 总结：
# 1.子类继承自父类，子类拥有父类的所有属性和函数
# 2.子类继承自父类，子类可以拥有自己的属性和函数
# 3.子类继承自父类，父类不可以使用子类的属性和函数
# 4.子类继承自父类，子类可以重写父类的函数
# 重写函数
class People(object):
    def __init__(self,weight):
        self.weight  = weight

    def eat(self):
        print '这是People中的eat'

    def work_time(self,w_time):
        # 工作时间超过8小时小于等于12小时，体重-2斤，时间超过12小时，体重减4斤
        if 8<w_time<=12:
            self.weight -= 2
        elif w_time>12:
            self.weight -=4
class Women(People):
    # 为什么要重写函数？
    # 父类中的函数满足不了或者不符合子类的需求
     # 1.完全重写，函数内执行的内容，和父类中的函数没有丝毫关系，和父类函数名称相同
     def eat(self):
        print '这是Man中的eat'
     # 2.部分重写,既保留父类函数功能，还可以添加新功能
     def work_time(self,w_time):
        # 2.1 保留父类函数功能
        People.work_time(self,w_time)
        print '小芳工作后的体重：',xiao_fang.weight
        # 2.2 添加新功能
        # 在工作减肥的同时，计算体重是否标准
        if self.weight < 90:
            print '身材偏瘦，多吃点....'
        elif self.weight<=120:
            print  '身材标准，继续保持'
        else:
            print '身材偏胖，少吃点....'
# 创建zhangsan对象，体重为200斤
zhangsan = People(200)
# 工作时间
zhangsan.work_time(13)
# 工作过后的体重
print '工作后的体重：',zhangsan.weight
xiao_fang = Women(150)
print xiao_fang.weight
xiao_fang.work_time(13)


# 两种类型
# 鸟类
class Bird(object):
    """docstring for ClassName"""
    def fly(self):
        print 'Bird类中的fly 函数执行了'
# 水栖类
class Aquatic_s(object):
    def swimming(self):
        print 'Aquatic_s类的swimming 函数执行了'
# 天鹅类继承自Bird和Aquatic_s类的# Bird和Aquatic_s两个类中的所有属性和函数，该类型的对象都可使用
# python中是有多继承,继承关系不要有太多的单一继承
class Swan(Bird,Aquatic_s):
    pass

swan = Swan()
print swan
# swan对象 可以使用Bird中的fly函数
# swan对象 可以使用Aquatic_s中的swimming函数
swan.fly()
swan.swimming()
#子类可以直接调用父类的函数和使用属性