"""
# File       : main.py
# Encoding   : utf-8
# Date       ：2023/12/11
# Author     ：LiFZ
# Email      ：lifzcn@gmail.com
# Description：
"""

import sys
import time

import numpy as np
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget

from client import Ui_Form


class mainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super(mainWindow, self).__init__(parent)
        self.setupUi(self)
        self.slots()
        self.items()
        self.image()

    def items(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.time)
        self.timer.start(100)

    def slots(self):
        self.pushButton_1.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.exit)

    def calculate(self):
        # 光速
        c = 299792458

        # 介质的介电常数
        epsilon_r = float(self.lineEdit_1.text())

        # 天线的中心工作频率
        f = float(self.lineEdit_2.text()) * np.power(10.0, 9)

        # 介质基片的厚度
        H = float(self.lineEdit_3.text()) * np.power(10.0, -3)

        # 高效率辐射贴片的宽度
        W = c / 2.0 / f * np.power((epsilon_r + 1.0) / 2.0, -1 / 2)

        # 有效介电常数
        epsilon_e = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 * np.power(1.0 + 12.0 * H / W, -1 / 2)

        # 等效辐射缝隙长度
        Delta_L = 0.412 * H * (epsilon_e + 0.3) * (W / H + 0.264) / (epsilon_e - 0.258) / (W / H + 0.8)

        # 介质内的导波波长
        lambda_e = c / f / np.sqrt(epsilon_e)

        # 实际辐射单元长度
        L = c / 2.0 / f / np.sqrt(epsilon_e) - 2.0 * Delta_L

        xi_re = (epsilon_r + 1.0) / 2.0 + (epsilon_r - 1.0) / 2.0 * np.power(1.0 + 12.0 * H / L, -1 / 2)

        # 馈电点位置
        X_Feed = L / 2.0 * 1.0 / np.sqrt(xi_re)

        # 贴片长度显示
        self.lineEdit_4.setText(str(round(L * np.power(10.0, 3), 3)))

        # 贴片宽度显示
        self.lineEdit_5.setText(str(round(W * np.power(10.0, 3), 3)))

    def exit(self):
        sys.exit(app.exec())

    def time(self):
        self.label_7.setText(time.strftime("%H:%M:%S", time.localtime()))

    def image(self):
        image = QImage("antenna.png")
        pixmap = QPixmap.fromImage(image)
        self.label_8.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = mainWindow()
    myWin.show()
    sys.exit(app.exec())
