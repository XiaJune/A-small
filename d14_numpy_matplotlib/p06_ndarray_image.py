# 显示图像
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import numpy as np
import cv2

# 1，创建一个窗体应用
# 1.1 定义窗体
class NDArrayWidget(QWidget):
    def __init__(self):
        super().__init__()
        win_w = 800
        win_h = 600
        self.resize(win_w, win_h)
        # 创建标签框架显示
        lbl_w = 800
        lbl_h = 600
        self.lbl_img = QLabel(self)
        self.lbl_img.setGeometry(
            (win_w - lbl_w)/2,
            (win_h - lbl_h)/2,
            lbl_w, lbl_h)
        # 加载两个图像
        self.img1 = cv2.imread('cute1.jpg')
        self.img2 = cv2.imread('cute2.jpg')
        self.img1 = cv2.cvtColor(self.img1, cv2.COLOR_BGR2RGB)
        # self.img1 = ~self.img1      # 颜色取反 简称底片
        # print(self.img1)

        self.handle_image_show()
        # print(type(self.img1))
        # print(self.img1.shape)

    def handle_image_show(self):
        # 1. 转换成QImage
        q_img = QImage(
            self.img1,
            self.img1.shape[1],
            self.img1.shape[0],
            self.img1.shape[1] * self.img1.shape[2],
            QImage.Format_RGB888
        )
        pass
        # 2. 转换成像素图QPixmap
        pix_img = QPixmap(q_img)
        # 3. 标签显示
        self.lbl_img.setPixmap(pix_img)
        self.lbl_img.setScaledContents(True)





# 1.2 利用窗体创建应用
app = QApplication([])

nd = NDArrayWidget()
nd.show()
app.exec()





























