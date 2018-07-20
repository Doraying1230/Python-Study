#coding:utf-8
import os
if __name__ == "__main__":
    path = "D:\\21cnjy\\20180115\\categories_param\\"
    # a = os.listdir(path)
    # print(a)
    # for x in a:
    #     b = os.listdir(path+x)
    #     print(b)
    c = os.walk(path)
    for rt, dirs, files in c:
        if dirs == []:

            if 'math' in rt:
                print(rt, files)

            # d=os.path.join(rt,files[0])
            # print(d)

    x = ("home", "me", "mywork")
    print(x)


