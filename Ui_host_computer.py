# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jun/Documents/CAD/host_computer.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1417, 853)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1120, 190, 261, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.area_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.area_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.area_horizontalLayout.setObjectName("area_horizontalLayout")
        self.brick_label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(27)
        self.brick_label_2.setFont(font)
        self.brick_label_2.setMouseTracking(False)
        self.brick_label_2.setAutoFillBackground(False)
        self.brick_label_2.setObjectName("brick_label_2")
        self.area_horizontalLayout.addWidget(self.brick_label_2)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.area_horizontalLayout.addWidget(self.comboBox)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1110, 90, 281, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.brick_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.brick_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.brick_horizontalLayout.setObjectName("brick_horizontalLayout")
        self.h_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.h_label.setFont(font)
        self.h_label.setMouseTracking(False)
        self.h_label.setAutoFillBackground(False)
        self.h_label.setObjectName("h_label")
        self.brick_horizontalLayout.addWidget(self.h_label)
        self.h_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.h_textEdit.setObjectName("h_textEdit")
        self.brick_horizontalLayout.addWidget(self.h_textEdit)
        self.w_label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.w_label.setFont(font)
        self.w_label.setMouseTracking(False)
        self.w_label.setAutoFillBackground(False)
        self.w_label.setObjectName("w_label")
        self.brick_horizontalLayout.addWidget(self.w_label)
        self.w_textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.w_textEdit.setObjectName("w_textEdit")
        self.brick_horizontalLayout.addWidget(self.w_textEdit)
        self.h_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.h_label_3.setFont(font)
        self.h_label_3.setMouseTracking(False)
        self.h_label_3.setAutoFillBackground(False)
        self.h_label_3.setObjectName("h_label_3")
        self.brick_horizontalLayout.addWidget(self.h_label_3)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(1090, 330, 291, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.pattern_horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.pattern_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pattern_horizontalLayout.setObjectName("pattern_horizontalLayout")
        self.brick_label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.brick_label_3.setFont(font)
        self.brick_label_3.setMouseTracking(False)
        self.brick_label_3.setAutoFillBackground(False)
        self.brick_label_3.setObjectName("brick_label_3")
        self.pattern_horizontalLayout.addWidget(self.brick_label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_2 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.pattern_horizontalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.horizontalLayoutWidget_5)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.pattern_horizontalLayout.addLayout(self.horizontalLayout_3)
        self.choose_pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.choose_pushButton.setGeometry(QtCore.QRect(140, 740, 131, 31))
        self.choose_pushButton.setObjectName("choose_pushButton")
        self.cad_label = QtWidgets.QLabel(self.centralwidget)
        self.cad_label.setGeometry(QtCore.QRect(290, 740, 261, 31))
        self.cad_label.setAutoFillBackground(False)
        self.cad_label.setText("")
        self.cad_label.setObjectName("cad_label")
        self.brick_label = QtWidgets.QLabel(self.centralwidget)
        self.brick_label.setGeometry(QtCore.QRect(1060, 70, 36, 70))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.brick_label.setFont(font)
        self.brick_label.setMouseTracking(False)
        self.brick_label.setAutoFillBackground(False)
        self.brick_label.setObjectName("brick_label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1031, 711))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.image_label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.image_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.image_label.setObjectName("image_label")
        self.gridLayout.addWidget(self.image_label, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1417, 28))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.brick_label_2.setText(_translate("MainWindow", "区域"))
        self.h_label.setText(_translate("MainWindow", "长："))
        self.w_label.setText(_translate("MainWindow", "宽："))
        self.h_label_3.setText(_translate("MainWindow", "mm"))
        self.brick_label_3.setText(_translate("MainWindow", "摆放方式"))
        self.radioButton_2.setText(_translate("MainWindow", "上"))
        self.radioButton.setText(_translate("MainWindow", "下"))
        self.radioButton_3.setText(_translate("MainWindow", "左"))
        self.radioButton_4.setText(_translate("MainWindow", "右"))
        self.choose_pushButton.setText(_translate("MainWindow", "选择CAD文件"))
        self.brick_label.setText(_translate("MainWindow", "砖"))
        self.image_label.setText(_translate("MainWindow", "图片显示位置"))

