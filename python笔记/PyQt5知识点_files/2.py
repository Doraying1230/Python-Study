#coding:utf-8
# import sys
# print sys.argv
# # 运行结果['2.py']
from PyQt5.QtWidgets import QMainWindow,QApplication
# uic加载ui文件
from PyQt5 import uic
import sys
# 定义函数，点击按钮时，执行该函数
def text():
    print "点我干啥"
# 创建app对象
app = QApplication(sys.argv)
# 加载test.ui文件
window = uic.loadUi('test.ui')
# 展示窗口
window.show()
# 通过window找到pushButton，点击pushButton执行test函数
window.pushButton.clicked.connect(test)
# 执行app，退出时结束进程
sys.exit(app.exec_())
