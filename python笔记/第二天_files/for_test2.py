#coding:utf-8
a = input('请输入一个数字a：')
b = 10
# if a>b:
#     print 'a>b'
# else:
#     print 'a<b'


# 高级写法
print 'a>b' if a>b else 'a<b'

# for x in range(1,10):
#     print x*x


print [x*x for x in range(10)]

#  当把变量插入字符串中的时候，需要使用占位符，整数是%d
print '今年我%d了' %a

# 一行代码写出来，拼接图片名字
# 01,02,03....,10,11,12....20
for x in range(20):
    # %02d    不够位数，补零
    print 'panda_%02d.jpg' %x
# 根据运行出来的效果，理解
print ['xxx_%02d.jpg' %x for x in xrange(20)]

print ['panda_0%d.jpg' %x if x<10 else 'panda_%d.jpg' %x for x in range(20) ]