# #coding:utf-8
# 编程一个字符串中每个字符出现的次数
# s='hxjchdhfdgfiofgifioo'
# dict_1={}
# for string in s:
#     #如果字典中没有该字符key
#     if dict_1.has_key(string)==False:
#         #把string作为字典的key,把string在字符串中出现的次数作为对应的值
#         dict_1[string]=s.count(string)
# #循环遍历字典，取出对应值输出
# for key in dict_1.keys():
#     print '%s在字符串中出现的次数为：%d'%(key,dict_1[key])
# #has_key(里面写键)，判断字典里是否含有该键
#获取第一个Python字符串中p相对于整个字符串所在的索引值，假如字符串中没有，就输出-1.
s_1 = 'dahfjdhkakjhfdjahsjdpythondkadqnpythondka'
substring = 'python'
is_find=False
for x in xrange(0,len(s_1)):
    if s_1[x:x+len(substring)]==substring:
        print '在字符串中第一个Python中p的 索引为：%d'%x
        is_find=True
        break
if is_find==False:
    print '没找到该字符，-1' 
    #find()函数 字符串中查找子串第一个字符所在的索引，找到该字符，输出字符索引位置，没找到则输出-1
    '''1.要查找的子串的内容
       2.查找开始的位置
       3.查找结束的位置
       注意:默认查找的范围是整个字符串
 '''
number=s_1.find ('uuuuuu')
print number
 #index(),查找子串在字符串中开始位置的字符的索引，有则输出索引，没有则直接错误异常
'''
 1.要查找的子串内容
 2.查找开始的位置
 3.查找结束的位置
 注意：默认查找范围是整个字符串
'''
num=s_1.index('python')
print num
s='a,d,f,g,h'
print '分割前字符串',s
#字符串内置函数:split函数
'''
1.根据参数1的str分割字符串，并以列表的形式返回结果
2.number，分割为number+1个字符串
'''
s_1=s.split(',',5)
print '分割后的列表',s_1
#根据某个字符将列表中的对象拼接成一个新的字符串

string='='.join (s_1)
print '拼接后的字符串',string