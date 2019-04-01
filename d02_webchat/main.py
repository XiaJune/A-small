# coding = utf-8
"""
作者：Miller
作用：启动应用
"""
from apps.webchatapp import WebChatApp
from PyQt5.QtWidgets import QApplication
import sys

web_app = QApplication(sys.argv)    # 给个显示环境
chat_app = WebChatApp()
sys.exit(web_app.exec())