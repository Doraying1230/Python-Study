#coding:utf-8
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5 import uic
import sys
from almost import *
class Manager(QMainWindow):
    """任务管理器"""
    def __init__(self):        
        QMainWindow.__init__(self)
        self=uic.loadUi('test_12.ui',self)
    def open_calc(self):
        global calc_face
        calc_face=MyWindow()
        calc_face.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    m=Manager()
    m.show()
    calc_face=None
    sys.exit(app.exec_())  
        
        