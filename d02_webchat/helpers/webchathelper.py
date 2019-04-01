# coding = utf-8
from PyQt5.QtCore import *
import itchat

class WebChatHelper(QThread):
    sign_qr = pyqtSignal(bytes)
    sign_login_ok = pyqtSignal()
    sign_coming_msg = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        print('开始登录')

        @itchat.msg_register(msgType=itchat.content.TEXT, isGroupChat=True)
        def recv_msg(msg):  # 嵌套函数 即是静态的  又可以使用self访问成员变量
            if msg['MsgType'] == 1:
                self.sign_coming_msg.emit(msg['Content'])
            # self.xxx.enit()

        #登录
        # itchat.auto_login()       # 时候手机端登录 不用重复登录
        itchat.login(
            qrCallback=self.qr_callback,
            loginCallback=self.login_callback)

        itchat.run()

    def qr_callback(self, uuid, status, qrcode):
        # if status == 0:
        self.sign_qr.emit(qrcode)      # emit 发出 信号

    def login_callback(self):
        print('登录成功')
        self.sign_login_ok.emit()       # 发出信号 给组合类

    def get_friends(self):
        lst_user = []
        # friends = itchat.get_chatrooms()    #获得聊天室
        friends = itchat.get_friends()    #获得好友

        for friend_ in friends:
            user = {}
            user['NickName'] = friend_['NickName']
            user['UserName'] = friend_['UserName']
            lst_user.append(user)

        return lst_user

    def send_msg(self, user_, msg_):
        itchat.send_msg(msg=msg_, toUserName=user_)








