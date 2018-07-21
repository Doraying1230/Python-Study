# coding:utf-8
# 成绩   优 良 中 差

cheng_ji = input('请输入成绩L：')
# 当对应的条件成立的时候，执行对应的内容
if cheng_ji>90:
    print '优秀'
elif cheng_ji>80:
    print '良好'
elif cheng_ji>70:
    print '中等'
elif cheng_ji>60:
    print '需要努力'

# else if 