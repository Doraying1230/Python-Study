#coding:utf-8
#什么叫做类？
# 具有相同的特点属性和行为方法的事物的抽象的集合
#人类特点，属性：姓名，年龄，身高，体重，智慧，，，，，，，，
#人类的行为：吃喝拉撒睡
#就有相同的特点属性和行为方法的事物的抽象的集合


#什么叫做对象？
#类的具体化的实例叫对象
#人类中的：特朗普，你面前的电话，动物中的神犬小七，看的到，摸得着
#class：班级，群体，就是类的统称
#用过的系统提供的类型：dict（字典），list（列表）， tuple（元组）， set（集合），
#怎么创建一个类:
#使用关键字创建类:
#class 类名称（父类名称）
        # '''''''类的描述文档''''''
class People (object):
    """类的描述文档"""
#init 初始化
#初始化函数（构造函数）
#1.self 当前类的一个实例对象
#2.arg 参数(属性值参数列表)
#人在出生的时候，都拥有身高，体重，年龄，性别.....的一些属性值
    def __init__(self, name_1,age_1,height_1 ):
        #self当前类的一个对象
        #通过.语法给对象的属性赋值
        #对象.属性名=属性值
        #属性是给对象用的
        self.name = name_1
        self.age = age_1
        self.height=height_1




#怎么创建一个对象
#格式：对象名=类型（属性值参数）
xiao_ming=People('小明',1,30)
#获取某个对象的属性值
#格式：xxx=对象.属性名
# 获取xiao_ming的name属性值
xm_name=xiao_ming.name
# 获取xiao_ming的age属性值
xm_age=xiao_ming.age
# 获取xiao_ming的height属性值
xm_height=xiao_ming.height
print xm_name,xm_age,xm_height
# 创建对象
xiao_hong = People('小红',2,50)
# 直接输出对象.属性名
print xiao_hong.name,xiao_hong.age,xiao_hong.height
# 修改或者添加对象的属性
# 对象.属性名 = 属性值
# 如果有这个属性，则修改原属性的值
# 如果没有这个属性，则添加这个属性并设置对应的值
# 添加属性，只是给该对象添加属性，其他同类型的对象不会拥有该属性
xiao_hong.sex = '女'
print '小红的sex属性值：',xiao_hong.sex
# 删除属性
del xiao_hong.sex
# AttributeError: 'People' object has no attribute 'sex' 
# 
# 错误原因：某个对象没有某个属性或者函数
# print xiao_hong.sex




class Flower(object):
    """花类"""
    # 当在构造对象时，由系统去调用init初始化函数
    def __init__(self, name,color,date,flw_lang):
        self.name = name 
        self.color = color 
        self.date = date
        self.flw_lang = flw_lang
    # 声明类中的函数时，必须携带一个self参数，但是调用函数时，不需传递self函数
    def display_flower(self):
        # 对象A执行该函数，self指的就是对象A
        print self.name,self.color,self.date,self.flw_lang
        # 函数可以传递多个参数，多个参数之间用,逗号隔开即可
    def flower_water(self,water_name):
        print '%s 浇了 %s'%(self.name,water_name)
    # 带返回值的函数
    def get_flower_name(self):
        # 获取当前对象的名称
        name = self.name
        # 把获取的结果返回
        return name
# 创建花类对象
rose = Flower('玫瑰花','红色','7','爱情')
# 执行类型中的函数:对象.函数名
rose.display_flower()
# 执行带返回值的函数
rose_name = rose.get_flower_name()
print '执行函数返回结果：',rose_name
dog_flower = Flower('狗尾巴草','绿色','90','顽强')
dog_flower.display_flower()
dog_flower.flower_water('康师傅矿泉水')
# 修改对象属性的函数
# 如果对象中有该属性，做修改，没有该属性做添加
# 1.要修改、添加的对象
# 2.要修改、添加的属性名称
#3.要修改、添加的属性内容
setattr(rose,'name','rose')
setattr(rose,'count',30)
print rose.name,rose.count
# 删除属性函数，要删除的属性一定要存在
delattr(rose,'count')
# print rose.count
# 查询某个对象的某个属性值
# 要查询的对象必须拥有查询的属性
rose_name = getattr(rose,'name')
print rose_name
#增删改查的函数都可以用.语法完成