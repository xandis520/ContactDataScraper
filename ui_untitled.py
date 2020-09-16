# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledGqPCPE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(340, 340)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 320, 320))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setEnabled(True)
        self.frame_2.setGeometry(QRect(10, 10, 300, 300))
        self.frame_2.setStyleSheet(u"QFrame{\n"
            "	border-radius: 150px;\n"
            "	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.749 rgba(69, 64, 93, 0), stop:0.750 rgba(255, 106, 80, 255));\n"
            "}")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setEnabled(True)
        self.frame_3.setGeometry(QRect(10, 10, 300, 300))
        self.frame_3.setStyleSheet(u"QFrame {\n"
            "	border-radius: 150px;\n"
            "	background-color: rgba(85, 85, 127, 100);\n"
            "}")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(30, 30, 260, 260))
        self.frame_4.setStyleSheet(u"QFrame{\n"
            "	border-radius: 130px;\n"
            "	background-color: rgb(77, 77, 127);\n"
            "}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 40, 193, 181))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.labelTitle = QLabel(self.widget)
        self.labelTitle.setObjectName(u"labelTitle")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.labelTitle.setFont(font)
        self.labelTitle.setStyleSheet(u"background-color:none;")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle, 0, 0, 1, 1)

        self.labelPercentage = QLabel(self.widget)
        self.labelPercentage.setObjectName(u"labelPercentage")
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Light")
        font1.setPointSize(40)
        self.labelPercentage.setFont(font1)
        self.labelPercentage.setStyleSheet(u"background-color:none;")
        self.labelPercentage.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelPercentage, 1, 0, 1, 1)

        self.labelTitle_2 = QLabel(self.widget)
        self.labelTitle_2.setObjectName(u"labelTitle_2")
        self.labelTitle_2.setMinimumSize(QSize(0, 20))
        self.labelTitle_2.setMaximumSize(QSize(16777215, 20))
        self.labelTitle_2.setFont(font)
        self.labelTitle_2.setStyleSheet(u"QLabel{\n"
            "	border-radius: 10px;\n"
            "	background-color: rgb(120, 120, 179);\n"
            "	color: #FFFFFF;\n"
            "	margin-left: 30px;\n"
            "	margin-right: 30px;\n"
            "}")
        self.labelTitle_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle_2, 2, 0, 1, 1)

        self.labelTitle_3 = QLabel(self.widget)
        self.labelTitle_3.setObjectName(u"labelTitle_3")
        self.labelTitle_3.setFont(font)
        self.labelTitle_3.setStyleSheet(u"QLabel{\n"
            "	color: #FFFFFF;\n"
            "	background-color: none;\n"
            "}")
        self.labelTitle_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.labelTitle_3, 3, 0, 1, 1)

        self.frame_3.raise_()
        self.frame_2.raise_()
        self.frame_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.labelTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600; color:#abb1d3;\">CONTACT</span> DATA SCRAPER</p></body></html>", None))
        self.labelPercentage.setText(QCoreApplication.translate("MainWindow", u"<p><span style=\" font-size:42pt; color:#ffffff;\">0</span><span style=\" font-size:30pt; color:#ffffff; vertical-align:super;\">%</span></p>", None))
        self.labelTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Loading...</span></p></body></html>", None))
        self.labelTitle_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>by Adrian W</p></body></html>", None))
        # retranslateUi

