#coding:utf-8
a = 12
#  input 只能输入数字
b = input('请输入一个数字：')
print b,type(b)
# 某些情况需要做一些判断，才可以继续操作
if b!=0:
    print a/b
#  输入一个字符
s  = raw_input('请输入一个字符：')
# type 可以用来获取当前变量的数据类型
print type(s) ,s 

print 4
print '4'
# print 4，'4'   这种情况下输出的是一样的
# demo  例子
