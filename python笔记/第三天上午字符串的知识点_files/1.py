#coding:utf-8
#str字符串类型:创建字符串,使用''单引号或者""双引号创建，创建字符串的时候，只需要把字符串的值赋值给一个变量就可以了，注意：字符串也有索引位置，可以根据索引查找字符
string_1='hello word!'
#查看变量类型
print type(string_1)
#访问字符串中特定位置的字符
print string_1[0]
#访问字符串中某个指定范围内的字符
#[0:n]包括索引0位置字符，不包括索引n位置的字符
print string_1[0:7]
#[n:]访问索引n(包含n)位置，直到最后位置的字符
print string_1[2:]
#[:n]从字符串开始的位置访问，直到索引为n-1
print string_1[:8]
#字符串的运算+：加号，连接字符串，把多个字符串连接在一起，可以把运算的结果赋值给某个变量使用
string_2=string_1[:6]+'xiaoming'
print string_2
s_1='hello'+' '+'word'+'!'
print s_1
#字符串中的转义字符
#r/R：原样字符串，假如字符串中有转义字符，如果还用原样字符串，则不会进行转译操作，直接按照文本原来的意思打印输出
print r'\n'
#*:乘法运算，重复输出字符串
s_2='hello   '
print s_2*10
#根据索引获取指定位置的某个字符
s_3=s_2[1]
print s_3
s_4='Life short ,use python'
#判断某个字符是否在某个字符串中
#in 运算，'e'在s_4返回bool类型的值，Ture:在字符串中，False:不在字符串中
if 'short'in s_4:
    print 's在字符串中'
else:
    print 's不在字符串中'
#  判断某个字符不在某个字符串中
# 'e' not  in s_4 返回bool类型的值，Ture：不在，False:在
if 'e'not in s_4:
    print 'e不在字符串中'
else:
    print 'e在字符串中'
#遍历字符串
#string 表示字符串中的每一个单独的字符
for string in s_4:
    print string 
#字符串中的占位符
#%s :字符串
#%d:整数类型
#%0nd:整数位数不够n,数字前自动补0
#%f:float,浮点型占位符
#%0.2f保留小数点后两位
s='你好'
number=1100
s_pluse='小明说：%s%d'%(s,number)
print s_pluse
t=9
print '小明说：%08d'%t
print '小明说：%.3f'%t
g=u'你现在好吗？'
#u 是字符集，把汉字转化成ASCII码，再把ASCII转化成字符，和uft-8的功能差不多，u适用于多国语言
for string in g:
    print string 
print '你好\n你好'
print r'你好\n你好'