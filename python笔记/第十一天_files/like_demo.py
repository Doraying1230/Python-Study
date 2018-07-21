#coding:utf-8

import sqlite3

def select_like():
    conn  = sqlite3.connect('database.db')
    # 张% 匹配以张字符开头的数据
    # %丰 匹配以丰字结尾的数据
    # %三% 匹配包含三字符的数据
    # 张_ 匹配以张开头并且匹配张后的一个字符
    # __丰 匹配以丰字符结束，并且匹配丰前2个字符的数据
    sql = "select count (*) from Student"

    res = conn.cursor().execute(sql)

    # 取出结果中的数字
    # 查询结果集中的下一条数据
    print  res.next()[0]

    # for stu_id,stu_name,stu_age,stu_grade in res:

    #     print stu_id,stu_name,stu_age,stu_grade

    conn.cursor().close()
    conn.close()

select_like()





















