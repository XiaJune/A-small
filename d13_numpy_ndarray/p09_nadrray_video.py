from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2

# 1, QWidget(窗体)
class VideoWidget(QWidget):
    # 实现一个构造器，创建一个标签框，这个标签框用来显示视频
    def __init__(self):
        super().__init__()
        # 窗体大小（800*600）
        self.resize(800, 600)
        # 构造标签框
        self.lbl_img = QLabel(self, text='<font size=80>数据采集中。。。</font>')
        # 文本与图像居中
        self.lbl_img.setAlignment(Qt.AlignCenter)
        # 大小设置
        self.lbl_img.setGeometry((800-640)/2,(600-360)/2, 640, 360)
        # -------------------------------
        # 4.1 创建一个设备
        self.dev_video = cv2.VideoCapture(0)    # 驱动摄像头
        # -----------------------------
        # 3. 创建定时器
        self.timer = QTimer()
        # 3.1 定时器绑定的执行函数
        self.timer.timeout.connect(self.capture_video)
        #         # 3.2 启动定时器
        self.timer.start(100)

    def capture_video(self):
        # 4.2
        status, img = self.dev_video.read()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        if status:
            #-------图像显示
            q_img = QImage(
                img,    # 被显示的图像数据，是ndarray
                img.shape[1], # 图像的宽度
                img.shape[0], # 图像的高度
                img.shape[1] * 3, # 每个图像的宽度占几个长度（像素）
                QImage.Format_RGB888 # 颜色设置
            )
            q_pix = QPixmap(q_img)
            self.lbl_img.setPixmap(q_pix)
            self.lbl_img.setScaledContents(True)


# 2, QApplication
app = QApplication([])
widget = VideoWidget()
widget.show()
app.exec()


#






























