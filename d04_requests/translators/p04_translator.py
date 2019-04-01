from translators.transapp import TransApp
from PyQt5.QtWidgets import QApplication
import sys

"""
程序入口
"""
app = QApplication(sys.argv)    # 装了qt应用
trans_app = TransApp()  # 启动业务应用
sys.exit(app.exec())



