#coding:utf-8

print '''
1*1 = 1
2*1 = 2     2*2 = 4
3*1 = 3     3*2 = 6     3*3 = 9
...
...
...
'''

for i in range(1,10):
    for j in range(1,i+1):
        # ',' 可以让当前for循环输出的语句连成一行
        print '%d*%d = %d' %(i,j,i*j),
    print '\n'