# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        Form.setMinimumSize(QtCore.QSize(640, 480))
        Form.setMaximumSize(QtCore.QSize(640, 480))
        self.groupBox_1 = QtWidgets.QGroupBox(Form)
        self.groupBox_1.setGeometry(QtCore.QRect(19, 9, 321, 171))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.groupBox_1.setFont(font)
        self.groupBox_1.setObjectName("groupBox_1")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 23, 281, 101))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_1 = QtWidgets.QLabel(self.layoutWidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_1)
        self.layoutWidget1.setGeometry(QtCore.QRect(20, 130, 281, 31))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_2.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(19, 180, 321, 291))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 120, 281, 161))
        self.groupBox_3.setObjectName("groupBox_3")
        self.tabWidget_1 = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget_1.setGeometry(QtCore.QRect(10, 20, 261, 131))
        self.tabWidget_1.setObjectName("tabWidget_1")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.layoutWidget_4 = QtWidgets.QWidget(self.tab_1)
        self.layoutWidget_4.setGeometry(QtCore.QRect(10, 10, 181, 81))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_4.addWidget(self.label_10, 1, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_4.addWidget(self.lineEdit_8, 2, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_1)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 30, 41, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget_1.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 181, 81))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_5.addWidget(self.lineEdit_9, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_13.setObjectName("label_13")
        self.gridLayout_5.addWidget(self.label_13, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_5.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.gridLayout_5.addWidget(self.label_14, 2, 0, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_5.addWidget(self.lineEdit_11, 2, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_4.setGeometry(QtCore.QRect(200, 30, 41, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget_1.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(10, 10, 181, 81))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_3)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_6.addWidget(self.lineEdit_12, 0, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 1, 0, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_6.addWidget(self.lineEdit_13, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget_3)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_6.addWidget(self.lineEdit_14, 2, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 30, 41, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_1.addTab(self.tab_3, "")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(21, 20, 281, 91))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 2, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(360, 19, 261, 411))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(10, 110, 241, 191))
        self.label_8.setObjectName("label_8")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(560, 437, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(497, 437, 61, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        self.tabWidget_1.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "天线计算工具 V2.0 By LiFZ"))
        self.groupBox_1.setTitle(_translate("Form", "参数设置"))
        self.label_1.setText(_translate("Form", "介电常数ε"))
        self.label_2.setText(_translate("Form", "工作频率(f:GHz)"))
        self.label_3.setText(_translate("Form", "基板厚度(H:mm)"))
        self.pushButton_1.setText(_translate("Form", "计算"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.groupBox_2.setTitle(_translate("Form", "计算结果"))
        self.groupBox_3.setTitle(_translate("Form", "同轴线馈点位置"))
        self.label_18.setText(_translate("Form", "r(mm)"))
        self.label_10.setText(_translate("Form", "R(mm)"))
        self.label_11.setText(_translate("Form", "Zo(ohm)"))
        self.pushButton_3.setText(_translate("Form", "->"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_1), _translate("Form", "r,R->Zo"))
        self.label_12.setText(_translate("Form", "r(mm)"))
        self.label_13.setText(_translate("Form", "Zo(ohm)"))
        self.label_14.setText(_translate("Form", "R(mm)"))
        self.pushButton_4.setText(_translate("Form", "->"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_2), _translate("Form", "r,Zo->R"))
        self.label_15.setText(_translate("Form", "R(mm)"))
        self.label_16.setText(_translate("Form", "Zo(ohm)"))
        self.label_17.setText(_translate("Form", "r(mm)"))
        self.pushButton_5.setText(_translate("Form", "->"))
        self.tabWidget_1.setTabText(self.tabWidget_1.indexOf(self.tab_3), _translate("Form", "R,Zo->r"))
        self.label_4.setText(_translate("Form", "贴片长度(L:mm)"))
        self.label_5.setText(_translate("Form", "贴片宽度(W:mm)"))
        self.label_9.setText(_translate("Form", "馈点位置(X:mm)"))
        self.groupBox_4.setTitle(_translate("Form", "同轴馈电微带贴片天线"))
        self.label_8.setText(_translate("Form", "图片"))
        self.label_7.setText(_translate("Form", "时间"))
        self.label_6.setText(_translate("Form", "当前时间："))
