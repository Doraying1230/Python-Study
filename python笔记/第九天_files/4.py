#coding:utf-8
#引用的模块一定要和执行模块的程序放在一个而文件夹里，否则会报错
# 1.引入模块(模块<==>文件)
import test 
# 1.第一种引入的调用方式：模块名.函数名
test.eat()
test.People.class_test()
#2.从test模块中引入eat函数
from test import eat
from test import People
#2.第二种引入的调用方式：函数名
eat()
People.class_test()
  



# 引入一个包，这个包相当于一个文件夹，该文件夹中有个叫做__init__.py的文件，在这个文件中引入了其他文件
#注意:调用包的程序和包必须放在一个文件夹里
import test_dir
#引入test_dir包后立即自动调用了__init__.py文件，等于__init__.py文件里所有引用的的模块都可以被引用。
#例如：这是第一种调用包里的模块或者说是函数的方法：
test_dir.name.name_test()
test_dir.phone.phone_test()
test_dir.test_1.eat_1.eat_1_test()
test_dir.test_1.drink.drink_test()
# as:给引入的模块或者类型起一个其他的名称，以后写代码再使用时可以直接使用别名
#这是第二种调用包里的模块或者函数的方法：
from test_dir import age as A
A.age_test()

