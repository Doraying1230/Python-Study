#coding:utf-8
#占位符
#  字符串str  %s
# 整数型int   %d
#浮点型float   %f

# %s  这个是万能的占位符
a = 1
b = 0.6
print 'a---->%d' %a
# 默认六位小数
print 'b->>>>>>>%f' %b
# 保留两位小数  0.2f  .2f  
print 'b------>%0.2f' %b
s = '今天真下雪了'
print '小明说\'%s\'' %s

print '老王家孩子小王%s岁了,身高有%s米' %(a,b)

# chr()把数字转成ASCII码
print chr(90)
#ord()把一个字符转换成整数
c=ord('a')
print c,type(c)
