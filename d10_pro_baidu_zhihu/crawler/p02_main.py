"""
    功能：启动百度翻译应用模块
    作者：Miller
    日期：2019-04-10
"""
import baidu.baiduapp
from PyQt5.QtWidgets import QApplication
import sys

qt = QApplication(sys.argv)
app = baidu.baiduapp.BaiduApp()
app.start()
sys.exit(qt.exec())

