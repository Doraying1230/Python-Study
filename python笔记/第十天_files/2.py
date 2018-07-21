#coding:utf-8

file_obj = open('test_3.txt','r')
string =  file_obj.read(5)
print string
# 移动光标
# tell()查看光标当前的位置
print file_obj.tell()
# seek()函数
#参数1.光标移动的长度 正值：向后移动  负值:向前移动
# 参数2.光标移动的起始位置,0表示从文件开始位置移动，1表示从当前位置
file_obj.seek(3,1)
print file_obj.tell()
# 读取光标后的数据
s = file_obj.read()
print s
file_obj.close()
import os
# 利用os模块对文件进行操作（os模块相当于一个操作系统模块，可以写入读取磁盘里的东西）
# 判断某个路径下的文件是否存在
# 返回True 表示文件存在，返回False表示 文件不存在
print os.path.exists('test_3.txt')
file_obj = open('test_10.txt','w')
file_obj.write('123')
file_obj.close()
file_obj = open('test_10.txt','a')
file_obj.write('456')
file_obj.close()
# 判断要读取的文件是否存在，存在再去读取文件
if os.path.exists('test123.txt'):
    file_obj = open('test_123.txt','r')
    print file_obj.read()
else:
    print '该文件不存在，请检查...'
# 判断要读取的文件是否存在，存在再去读取文件
try:
    file_obj = open('test_123.txt','r')
    print file_obj.read()
except IOError:
    print '该文件不存在，请检查...'
# 重命名
# os.rename
# 参数1.原文件名称
# 参数2.修改后的名称
# 注：要修改的文件必须存在
os.rename('test_10.txt','123.txt')
#os.remove
# 删除某个文件
# 注：要删除的文件必须存在
# os.remove('test_3.txt')




