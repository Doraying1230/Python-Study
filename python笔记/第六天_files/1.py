#coding:utf-8
dict_1={'name':'zhangsan','age':'12','sex':1,
'height':180,'weight':80,'love':'Write Code'}
# 字典存储数据以键值模式存储
# 创建一个字典
# 字典中的key必须是唯一的
# 字典中的key必须是不可变的，例如字符串、数字、元组，但是列表list是可变的，不可以作为字典的key
# 往字典中添加新数据
# 如果字典中没有phone这个key，做添加数据的操作
dict_1['phone'] = 110
print dict_1
# 字典中有name这个key,做修改的操作
dict_1['name'] = 'wangwu'
print dict_1
# 删除字典中的数据
#根据键删除数据
#KeyError: 'sex'，原因：字典中 没有该key
del dict_1['name']
print '根据key删除字典内容:',dict_1
#使用pop函数根据键取出并移除数据
value =  dict_1.pop('age')
print '使用pop函数取出并移除数据:', value
print '使用pop函数后的字典：',dict_1
# 随机移除字典中的某个数据
# 使用场景：要逐条删除字典的数据，可以利用循环使用popitem()移除
item = dict_1.popitem()
print 'popitem函数执行：',item
print 'popitem函数执行后：',dict_1
# 删除字典中所有的数据
# dict_1.clear()
# print '删除字典中所有数据：',dict_1
# 删除字典这个对象
# del dict_1
# NameError: name 'dict_1' is not defined 原因：变量名称没有被定义
# 查询数据
# 根据某个key查询对应的值
value = dict_1['sex']
print value
# 获取字典中所有的key，并以列表形式返回
all_keys = dict_1.keys()
print all_keys
# 获取字典中所有的值，并以列表形式返回
all_values = dict_1.values()
print all_values
# 查询字典中所有的数据
for key in all_keys:
    # 根据key取出对应的值
    print key,dict_1[key]
# 获取字典中所有的key，value并以列表的形式返回,key，value值放在一个元组中
kv_list = dict_1.items()
print kv_list
# for循环列表，取出元组
for x in dict_1.items():
    # 取出元组中对应的值
    key,value = x 
    print key,value
# for遍历列表，取出元组中的数据
for key,value in dict_1.items():
    print key,'--->',value
# 取出元组中的数据
a,b = (10,20)
print a,b

s = ['name','age']
# 生成一个新字典，接收该字典进行使用
# 字典对应的值默认为空
dic_2 = dict_1.fromkeys(s,'zhangsan')
print dic_2
#setdefault()给字典同时添加值和键，值可以为元组，列表或者字典。默认值为None,一次只能添加一组键值
dict_2 = dict_1.setdefault('namekll',{'hdjs':18})
print dict_2
print dict_1
# 根据key获取对应的值
print dic_2['name']
print dic_2.get('name')
# has_key 判断字典是否拥有某个key
# 有该key，返回True，没有返回False
print dic_2.has_key('sex')
# 把其他字典中的内容更新到该字典中
diq_2={'naj':'sjj'}
diq_1={'jaj':'ama','jj':'lkk'}
diq_1.update(diq_2)
print diq_2
print diq_1
dict_10 = {
    'name_list':['zhangsan','lisi','wangwu'],
    'age_tuple':(22,23,24,25,26)
}

for key,value in dict_10.items():
    # value是一个容器类
    for x in value:
        print x




