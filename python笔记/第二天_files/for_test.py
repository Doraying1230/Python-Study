#coding:utf-8
# 导入时间库
import time
# while  语句是循环执行，除非到某个临界点，否则不停的执行
#for  遍历某个对象 ：字符串，list，对象，dict


# s = 'hhhhhhhhhhhhhhhh'
# print s
# print 'hhhhhhhhhhhh'
for s in 'abcdefg':
# 一个一个查找abcdefg里面的字符（遍历），查找完毕，停下来
    print s



# xrange(1,10)  包含1，不包含10
for x in range(1,10):
    print x
l = range(1,10)
print l,type(l)
# 获取当前的时间
time1 = time.time()
sum = 0
for x in range(1,1000000):
    #  用起来和range类似，但是遍历起来比range快
    sum += x
print sum
time2 = time.time()
print time2 - time1


time3 = time.time()
sum2 = 0
for x in xrange(1,1000000):
    #  用起来和range类似，但是遍历起来比range快,1000000的时候时快时慢，100000以内xrange计算快一点
    sum2 += x
print sum
time4 = time.time()
print time4 - time3

# range 和 xrange 都可以用来进行遍历，但是range（10）返回的是list，xrange（10）返回的是object
# 打印10以内的list
print range(10)
# 打印 5到10的list
print range(5,10)
# 打印2到100 的list，每隔一个数打印一次
print range(2,100,2)


