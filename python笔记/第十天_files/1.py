#coding:utf-8
# bit  位
# Byte(字节) = 8bit
# kb(千字节) = 1024Byte
# Mb(兆) = 1024kb
# GB = 1024 Mb
# TB =1024GB
# 读取内存中的数据
# dict_1 = {'name':'zhangsan'}
# print dict_1
# 读取和写入磁盘文件
# 使用python中的内置函数 open，创建一个file对象
# 1.name :要打开的文件名称
# 2.mode：打开文件时，使用的方式：读取(r\r+\rb)、写入、追加
# r:只读(默认) r+:读取加写入 (前提是文件之前存在)rb+：以二进制方式读取写入
# w：只写入 w+:写入和读取  wb+ :以二进制方式读取写入
# a:只能追加数据  a+：追加和读取 ab+:以二进制方式读取写入
# 3.buffering:使用的缓存策略，0：不使用缓存策略，直接做写入的操作，1在文本模式下，使用缓存策略，大于1，该数字指的就是缓存区的大写，该参数不传递，使用默认缓存策略
# 路径下文件存在，则打开，不存在，则创建文件
# w(直接写入)模式，原文件中的内容都会在下一次写入时被覆盖
# a模式(追加)，原文件中的内容不会被覆盖，会在文件的末尾继续追加数据
# file_obj = open('test.txt','w')
# write()函数：可以将一个字符串或者二进制数据写入已打开的文件，不会在字符串末尾添加换行符
# file_obj.write('second write')
# 关闭文件
# close()函数：使用了缓存策略，则把缓存中的所有数据立即写入文件，关闭文件，文件一旦关闭不能再进行读取和写入操作
# file_obj.close()
# 打开文件进行读取写入操作
file_obj = open('test.txt','r')
# read()函数，用来读取文件中的内容
# 参数：要读取的文件长度，不填参数，默认尽可能多的读取文件内容，有可能是全部内容
# 建议：如果文件比较小，可以直接使用该函数进行全部读取，如果文件的比较大不建议使用这种读取方式
# 接收读取的内容
# read()函数读取内容时，光标停留在最后读取的位置，再次读取时，从该位置开始读取
string =  file_obj.read(5)
print string
string_2 = file_obj.read(5)
print '这是第二次读取',string_2
file_obj.close()
file_obj = open('test.txt')
# 读取一行数据
string_1 = file_obj.readline()
print string_1
# 读取所有行的数据,# 会把每一行后的换行也读取出来\n,以列表的形式返回
data_list =  file_obj.readlines()
print data_list
# 遍历列表查询每一行数据
for string in data_list:
    print string 
file_obj.close()
file_obj = open('test_3.txt','w')
file_obj.write('dghagsdhgj')
# 可以把一个列表直接写入文件，列中放的是字符或者二进制数据
# write不会自动添加换行，如需要则自己添加换行符
file_obj.writelines(['name\n','age\n','phone\n'])
file_obj.close()