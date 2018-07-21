#coding:utf-8

a = 12
b = input('请输入一个数字：')
# if 判断条件:
#     pass
# pass代表执行的内容，保证语义完整

# 如果条件成立，执行if语句
if b!=0:
    print a/b
else:
    #条件不成立，执行else语句
    print '除数不能是0'

if  b<60:
    print '不及格'
else:
    print '及格'