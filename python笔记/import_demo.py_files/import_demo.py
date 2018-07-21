#coding:utf-8
# 1.引入模块(模块<==>文件)
# 2.从test模块中引入eat函数
# from test import eat
# from test import People

# 3.从test模块中引入所有的函数或者类型
# from test import *

# 1.第一种引入的调用方式：模块名.函数名
test.eat()
# People.class_test()

# 2.第二中引入的调用方式：函数()
# eat()





# coding:utf-8
# QtWidgets所有控制模块包
# 引入PyQt5模块中MainWindow模块
# QApplication应用程序包
from PyQt5.QtWidgets import QMainWindow, QApplication
# PyQt5.QtWidgets相当于文件夹，QMainWindow,QApplication相当于类，她们中有很多函数，可以通过类，创建对象，由对象调用。
# 引入sys库
import sys

# sys.argv获取当前文件名称，并用列表返回
# 创建应用程序对象，把当前文件名称作为参数传递
app = QApplication(sys.argv)
# 创建window窗口
window = QMainWindow()  # 设置当前窗口的大小
window.resize(600, 400)
# 移动窗口，不过不设置移动，则默认在屏幕中间显示
# x,y轴坐标：x越往右越大，y越往下越大
window.move(100, 100)
# 设置当前窗口的名称
window.setWindowTitle('我的第一个pyqt程序')
# 引入QIcon模块
from PyQt5.QtGui import *

# 创建icon图标对象
icon = QIcon('1.png')
# 设置当前窗口的图标
window.setWindowIcon(icon)
# 创建QPalette调色板对象
palette = QPalette()
# 设置调色板颜色
# 1.要设置的对象的某个颜色属性
# 2.QColor要设置的颜色值 RGB(红绿蓝) 0~255
palette.setColor(window.backgroundRole(), QColor(0, 0, 0))
# 设置背景图片
palette.setBrush(window.backgroundRole(), QBrush(QPixmap('icon.png')))
# 设置当前窗口的背景颜色
window.setPalette(palette)
# 展示窗口
window.show()
# 执行应用程序
app.exec_()
# 当程序退出时，结束该程序进程
sys.exit(app.exec_())
# 加警告框，
from PyQt5.QtWidgets import QMessageBox

# 1.要给谁添加这个警告框
# 2.警告框的标题
# 3.警告内容
# 4.按钮选项Yes\No按钮
# 5.默认选择的选项(不填该参数则默认选择Yes)
box = QMessageBox.question(self, '警告！', '请填写完信息后提交查询！！', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
from PyQt5 import uic

self = uic.loadUi('text_1.ui', self)
conn = sqlite3.connect('database.db')
with sqlite3.connect('database.db') as conn:
# 省去写关闭数据库文件的操作,同时游标也关闭了
execute()#执行函数，本身就自动创建了游标，不用创建游标
cursor.execute() = conn.execute()

# coding:utf-8
# import sys
# print sys.argv
# # 运行结果['2.py']
from PyQt5.QtWidgets import QMainWindow, QApplication
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

# coding:utf-8
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from almost import *


class Manager(QMainWindow):
    """任务管理器"""

    def __init__(self):
        QMainWindow.__init__(self)
        self = uic.loadUi('test_12.ui', self)

    def open_calc(self):
        global calc_face
        calc_face = MyWindow()
        calc_face.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    m = Manager()
    m.show()
    calc_face = None
    sys.exit(app.exec_())

# coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# Qt 枚举
from PyQt5.QtCore import Qt
import sys


# QDialog 对话窗口的基类
class MyTable(QDialog):
    """人员信息表"""

    def __init__(self, list_arg=None):
        QDialog.__init__(self)
        self.list_arg = list_arg
        # 设置当前窗口标题
        self.setWindowTitle('人员信息表')
        # 设置当前窗口图标
        self.setWindowIcon(QIcon('logo.png'))
        # 设置当前窗口大小
        self.resize(640, 300)
        # 设置当前窗口最大大小
        self.setMaximumSize(640, 300)
        # 设置当前窗口最小大小
        self.setMinimumSize(640, 300)
        # 设置当前窗口按钮选项，只有关闭按钮
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        # 建立表格的model，设置表格显示的行数\列数
        self.model = QStandardItemModel(len(list_arg), 6)
        # 设置表格表头
        self.model.setHorizontalHeaderLabels(['编号', '姓名', '年龄', '性别', '出生日期', '联系方式'])
        for x in xrange(len(list_arg)):
            # 先取出小元组
            tuple_1 = list_arg[x]
            for j in xrange(0, 6):
                # 创建单元格
                item = QStandardItem('%s' % tuple_1[j])
                # 设置单元格居中
                item.setTextAlignment(Qt.AlignCenter)
                #  填充表格中的单元格
                # 1.行号 2.列号 3.填充单元格对象
                self.model.setItem(x, j, item)

        # 创建tableView表格对象
        self.tableView = QTableView()
        # 设置表格的model
        self.tableView.setModel(self.model)
        # 设置表格不可编辑
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 创建VBoxLayout对象
        layout = QVBoxLayout()
        # 把表格添加到layout对象中
        layout.addWidget(self.tableView)
        # 把设置当前窗口的布局
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 数据源
    list_1 = [(31001, '张三', 22, '女', '20170310', '13243255555'), (31002, '李四', 33, '女', '20170310', '13243255555'),
              (31003, '王五', 22, '女', '20170310', '13243255555'), (31004, '赵六', 22, '女', '20170310', '13243255555'),
              (31005, '田七', 22, '女', '20170310', '13243255555'), (31006, '粥吧', 22, '女', '20170310', '13243255555'),
              (31007, '九妹', 22, '女', '20170310', '13243255555')]

    my_table = MyTable(list_1)
    my_table.show()
    sys.exit(app.exec_())













