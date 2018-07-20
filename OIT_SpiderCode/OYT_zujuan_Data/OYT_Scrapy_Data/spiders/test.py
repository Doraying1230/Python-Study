#coding:utf-8
# a = 'D:\\xiti10001\\picture\\{}\\'
# b = a[3:].replace('\\','/')
# print(b)
# def text():
#     comment = 0
#     for x in range(1,19):
#         # comment+=1
#         # if comment > 10:
#         #     continue
#         # else:
#         #     print(x)
#         print('第一层循环的次数：',x)
#         for x in range(1,5):
#             if x > 2:
#                 continue
#             else:
#                 print('小亓')
#
#
# text()
# class La(object):
#     biaoji = True
#
#     def text(self):
#         for x in range(0,20):
#             print('xiaoqi;',x)
#             for i in range(10):
#
#                 if self.biaoji == True:
#                     print('二层循环一层的：',x)
#                     self.text2(i)
#                 else:
#                     print(self.biaoji)
#                     self.biaoji = True
#                     continue
#     def text2(self,x):
#         if x < 3:
#             print('解析层的数据：',x)
#         else:
#             self.biaoji = False
# if __name__ =='__main__':
#     w= La()
#     w.text()
#     for x in range(10):
#         print('q11',x)
# for x in range(10):
#     if x > 5:
#         continue
if __name__ == "__main__":
    a = 8005
    b = 10
    div = a // b
    mod = a % b
    print(type(div),div)
    print(123456)
    print(type(mod),mod)