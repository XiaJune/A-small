# coding = utf-8
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from uis.ui_webchatmain import Ui_Form

class WidChatMain(QWidget):
    def __init__(self, chat_):
        super().__init__()
        self.chat = chat_
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # 处理chat发送过来的信号
        self.chat.sign_coming_msg.connect(self.show_msg)

        # 添加模式
        self.model = QStandardItemModel()   # 构建一个模式
        self.ui.listView.setModel(self.model)

        #绑定信号处理
        self.ui.listView.clicked.connect(self.select_user)
        # 点击信息
        self.ui.pushButton.clicked.connect(self.send_msg)

    def send_msg(self):
        # 获取文本信息
        msg = self.ui.lineEdit.text()       # 得到文本
        # 发送 需要使用辅助类
        self.chat.send_msg(self.current_user, msg)  # 其实要判断下用户是否选择


    def select_user(self, index):
        # 获取当前用户
        row = index.row()
        self.current_user = self.model.item(row).data() # 绑定在模型中不显示的数据

    def show_msg(self, msg):
        self.window()


    def show_user_list(self):
        #调用辅助类 获取用户列表
        lst_users = self.chat.get_friends()
        # 显示用户列表到别表框
        for user_ in lst_users:
            user_name = user_['UserName']    # 发送时使用的用户ID
            nick_name = user_['NickName']   # 显示这个类
            icon_head = QIcon('imgs/user.jpg')
            item_ = QStandardItem(icon_head, nick_name) # 得到数据项
            item_.setData(user_name)
            self.model.appendRow(item_) # 添加到模型里面