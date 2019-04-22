# coding = utf-8
"""
作用：组合界面，业务封装，形成独立的应用逻辑
"""
from PyQt5.QtCore import *
from uis.dlgqrlogin import DlgQRLogin
from uis.widchatmain import WidChatMain
from helpers.webchathelper import WebChatHelper

class WebChatApp(QObject):
    """
    负责组合登录页面，聊天界面，微信访问模块，形成微信聊天的功能
    """
    def __init__(self):
        super().__init__()

        # 调用辅助类实现登录
        self.chat = WebChatHelper()

        self.ui_login = DlgQRLogin(self.chat)    # 调用窗体构成 传给ui_login
        self.ui_login.show()                     # show  显示窗体
        self.ui_main = WidChatMain(self.chat)
        # self.ui_main.show()

        self.chat.sign_login_ok.connect(self.show_chat_main)
        self.chat.start()   # 启动多线程 辅助类开始工作


    def show_chat_main(self):
        # 隐藏登录
        self.ui_login.hide()    # 隐藏登录界面
        # 释放登录
        self.ui_login.destroy() #  释放登录窗口
        # 加载用户列表
        self.ui_main.show_user_list()
        # #  加载聊天室
        # self.ui_main.show_userd_list()
        # 登录成功 显示主窗体
        self.ui_main.show()     # 显示聊天窗口




