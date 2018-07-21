#coding:utf-8
#QtWidgets所有控制模块包
#引入PyQt5模块中MainWindow模块
#QApplication应用程序包
from PyQt5.QtWidgets import QMainWindow,QApplication
#PyQt5.QtWidgets相当于文件夹，QMainWindow,QApplication相当于类，她们中有很多函数，可以通过类，创建对象，由对象调用。
# 引入sys库
import sys
#sys.argv获取当前文件名称，并用列表返回
# 创建应用程序对象，把当前文件名称作为参数传递
app = QApplication(sys.argv)
# 创建window窗口
window = QMainWindow()# 设置当前窗口的大小
window.resize(600,400)
# 移动窗口，不过不设置移动，则默认在屏幕中间显示
# x,y轴坐标：x越往右越大，y越往下越大
window.move(100,100)
# 设置当前窗口的名称
window.setWindowTitle('我的第一个pyqt程序')
# 引入QIcon模块
from PyQt5.QtGui import *
# 创建icon图标对象
icon = QIcon('1.png')
# 设置当前窗口的图标
window.setWindowIcon(icon)
# 创建QPalette调色板对象
palette =  QPalette()
# 设置调色板颜色
# 1.要设置的对象的某个颜色属性
# 2.QColor要设置的颜色值 RGB(红绿蓝) 0~255
 palette.setColor(window.backgroundRole(),QColor(0,0,0))
# 设置背景图片
palette.setBrush(window.backgroundRole(),QBrush(QPixmap('icon.png')))
# 设置当前窗口的背景颜色
window.setPalette(palette)
# 展示窗口
window.show()
# 执行应用程序
app.exec_()
# 当程序退出时，结束该程序进程
sys.exit(app.exec_())
