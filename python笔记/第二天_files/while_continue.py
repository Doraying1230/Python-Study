#coding:utf-8
num = 0
while num<100:
    num += 1
    # 当if语句条件成立的时候，会调用continue，那么while语句内的continue之后的代码不执行
    #  遇见10的倍数就跳过
    # == 比较值是否相等，ctrl + '/' 注释
    if num%10==0:
        continue

    print num
    # print '123'
    # print '345'

