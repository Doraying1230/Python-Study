#coding:utf-8

print '''
*******   2*(row-0)-1
 *****     2*(row-1)-1
  ***       2*(row-2)-1
   *         2*(row-3)-1

'''
num = input('请输入一个数字：')
for x in xrange(num):
    # 2*num-1   x-1
     
    # 字符串的拼接 字符串和字符串之间用+连接
    print (x)*' '+(2*(num -x)-1)*'*'

# 不同类型之间不能拼接
# print 'aaaa'+12
#   作业：正金字塔 ； 输入两个数，比较两个数的大小
#   输入三个数，从小到大依次输出

# wingide 5.1   占内存小，运行快
#pycharm  界面好看，占内存大