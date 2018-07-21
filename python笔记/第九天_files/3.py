#coding:utf-8
#内存管理
'''
    创建一个对象，实际上是在内存中开辟了一块空间来存放这个对象

'''
class People(object):
    """docstring for People"""
    def __init__(self):
        print 'People对象创建了'
    # 对象被移除的时候执行该函数
    def __del__(self):
        print 'People对象被删除了'
#引用计数：当一个对象被创建出来的时候，它的引用计数为1，当对象a引用该对象时，引用计数会+1，当对象a不再引用该对象时，引用计数-1，当对象的引用计数为0时，系统会在合适的时候将其从内存中抹除，
#（当对象不再使用时，创建时的引用计数会被系统减掉）
p = People()

p_1 = p

del p

print '删除p后的代码'

def test():
    p = People()
    p.name = 'zhangsan'
    print '3'
    p.name = 'lisi'

print '1'
test()
print '2'



