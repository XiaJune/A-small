from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

"""
负责翻译器的界面
    |- 聚合翻译类一起工作
"""
class UiTranslator(QWidget):
    def __init__(self, tr): #  tr 翻译器
        super().__init__()
        self.translator = tr
        # 窗体大小 窗体的属性
        self.setWindowTitle('Miller爆炸器')    # 窗体标题
        self.setGeometry(600, 400, 400, 300)      # 窗体所在的位置 大小
        # 文本输入框（输入需要翻译的单词）
        self.edt_keyword = QLineEdit(self)  # 创建文本框
        self.edt_keyword.setGeometry(10, 10, 250, 30)      #  文本输入框大小 位置
        # 按钮（事件提交）
        self.btn_translate = QPushButton(self)  # 创建按钮
        self.btn_translate.setText('按下就爆炸！！')
        self.btn_translate.setGeometry(260, 10, 110, 30)    # 按钮位置 大小
        # 标签框（显示结果）
        self.lbl_info = QLabel(self)
        self.lbl_info.setText('<p style="color:yellow;background-color:bleak;font-size:50px">爆炸范围</p>')
        self.lbl_info.setGeometry(10, 50, 380, 250)     # 标签库位置大小 离左 上边的距离  框的大小
        self.lbl_info.setAlignment(Qt.AlignTop)

        # 处理事件
        self.btn_translate.clicked.connect(self.b_translate)

    def b_translate(self):
        # 获取文本
        str_keyword = self.edt_keyword.text()
        # 调用翻译器
        print(1123)
        result = self.translator.translatedd(str_keyword)
        # 显示结果(处理显示结果)
        self.lbl_info.setText(result)







