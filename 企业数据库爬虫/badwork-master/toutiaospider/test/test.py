# -*- coding: utf-8 -*-
"""
 @Time: 2018/3/5 13:45
 @Author: sunxiang
"""

s = set()
with open('error_log.txt', 'r') as f:
    content = [f.split(" ")[-1].strip() for f in f.readlines()]


for c in content:
    s.add(c)

print len(s)
for o in s:
    print o
