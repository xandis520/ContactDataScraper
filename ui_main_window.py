# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainQNHcvV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 628)
        MainWindow.setStyleSheet(u"background-color: rgb(32, 34, 37);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 500))
        self.centralwidget.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.centralwidget)
        self.Top_Bar.setObjectName(u"Top_Bar")
        self.Top_Bar.setMaximumSize(QSize(16777215, 40))
        self.Top_Bar.setStyleSheet(u"")
        self.Top_Bar.setFrameShape(QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.Top_Bar)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 60))
        self.frame_toggle.setStyleSheet(u"")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.button_burger = QPushButton(self.frame_toggle)
        self.button_burger.setObjectName(u"button_burger")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_burger.sizePolicy().hasHeightForWidth())
        self.button_burger.setSizePolicy(sizePolicy)
        self.button_burger.setStyleSheet(u"background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"background-position: center;\n"
"background-repeat: no-reperat;\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;")

        self.verticalLayout_2.addWidget(self.button_burger)


        self.horizontalLayout.addWidget(self.frame_toggle)

        self.frame_top = QFrame(self.Top_Bar)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_top)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_top)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 40))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(40, 40))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/24x24/icons/24x24/cil-3d.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: 0px solid;	\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(185, 187, 190);\n"
"")

        self.horizontalLayout_5.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.frame_main_buttons = QFrame(self.frame)
        self.frame_main_buttons.setObjectName(u"frame_main_buttons")
        self.frame_main_buttons.setFrameShape(QFrame.NoFrame)
        self.frame_main_buttons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_main_buttons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_minimalize = QPushButton(self.frame_main_buttons)
        self.button_minimalize.setObjectName(u"button_minimalize")
        self.button_minimalize.setMinimumSize(QSize(40, 40))
        self.button_minimalize.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-image: url(:/24x24/icons/24x24/cil-window-minimize.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(47, 49, 54);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_minimalize)

        self.button_full_screen = QPushButton(self.frame_main_buttons)
        self.button_full_screen.setObjectName(u"button_full_screen")
        self.button_full_screen.setMinimumSize(QSize(40, 40))
        self.button_full_screen.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-image: url(:/24x24/icons/24x24/cil-window-restore.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(47, 49, 54);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_full_screen)

        self.button_exit = QPushButton(self.frame_main_buttons)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(40, 40))
        self.button_exit.setStyleSheet(u"QPushButton{\n"
"	border: 0px solid;\n"
"	background-image: url(:/24x24/icons/24x24/cil-x.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(77, 40, 40);\n"
"}")

        self.horizontalLayout_4.addWidget(self.button_exit)


        self.horizontalLayout_3.addWidget(self.frame_main_buttons, 0, Qt.AlignRight)


        self.verticalLayout_7.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.frame_top)


        self.verticalLayout.addWidget(self.Top_Bar)

        self.Content = QFrame(self.centralwidget)
        self.Content.setObjectName(u"Content")
        self.Content.setStyleSheet(u"")
        self.Content.setFrameShape(QFrame.NoFrame)
        self.Content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Content)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.Content)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet(u"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_left_top_menu = QFrame(self.frame_left_menu)
        self.frame_left_top_menu.setObjectName(u"frame_left_top_menu")
        self.frame_left_top_menu.setMaximumSize(QSize(16777215, 220))
        self.frame_left_top_menu.setStyleSheet(u"margin-top: 10px;")
        self.frame_left_top_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_top_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_left_top_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.button_menu_home = QPushButton(self.frame_left_top_menu)
        self.button_menu_home.setObjectName(u"button_menu_home")
        self.button_menu_home.setMinimumSize(QSize(0, 70))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Black")
        font1.setPointSize(8)
        self.button_menu_home.setFont(font1)
        self.button_menu_home.setStyleSheet(u"QPushButton{\n"
"	margin-top:10px;\n"
"	margin-bottom:10px;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	color: rgb(185, 187, 190);\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 25px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_home)

        self.button_menu_home_2 = QPushButton(self.frame_left_top_menu)
        self.button_menu_home_2.setObjectName(u"button_menu_home_2")
        self.button_menu_home_2.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        self.button_menu_home_2.setFont(font2)
        self.button_menu_home_2.setStyleSheet(u"QPushButton{\n"
"	margin-top:10px;\n"
"	margin-bottom:10px;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	color: rgb(185, 187, 190);\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 25px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_home_2)

        self.button_menu_home_3 = QPushButton(self.frame_left_top_menu)
        self.button_menu_home_3.setObjectName(u"button_menu_home_3")
        self.button_menu_home_3.setMinimumSize(QSize(0, 70))
        self.button_menu_home_3.setFont(font2)
        self.button_menu_home_3.setStyleSheet(u"QPushButton{\n"
"	margin-top:10px;\n"
"	margin-bottom:10px;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	color: rgb(185, 187, 190);\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 25px;\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-top-left-radius: 7px;\n"
"	border-bottom-right-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_home_3)


        self.verticalLayout_3.addWidget(self.frame_left_top_menu)

        self.frame_left_bottom_settings = QFrame(self.frame_left_menu)
        self.frame_left_bottom_settings.setObjectName(u"frame_left_bottom_settings")
        self.frame_left_bottom_settings.setMinimumSize(QSize(70, 90))
        self.frame_left_bottom_settings.setStyleSheet(u"QFrame{\n"
"	margin-bottom: 20px;\n"
"}")
        self.frame_left_bottom_settings.setFrameShape(QFrame.NoFrame)
        self.frame_left_bottom_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_left_bottom_settings)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.button_settings = QPushButton(self.frame_left_bottom_settings)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setMinimumSize(QSize(0, 0))
        self.button_settings.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/24x24/icons/24x24/cil-settings.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: 0px solid;\n"
"	margin-bottom: 0px;\n"
"}")

        self.verticalLayout_8.addWidget(self.button_settings)


        self.verticalLayout_3.addWidget(self.frame_left_bottom_settings, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_main_pages = QFrame(self.Content)
        self.frame_main_pages.setObjectName(u"frame_main_pages")
        self.frame_main_pages.setStyleSheet(u"QFrame{\n"
"	border-top-left-radius: 25px;\n"
"	background-color: rgb(54, 57, 63);\n"
"}")
        self.frame_main_pages.setFrameShape(QFrame.NoFrame)
        self.frame_main_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_main_pages)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_under_top_bar = QFrame(self.frame_main_pages)
        self.frame_under_top_bar.setObjectName(u"frame_under_top_bar")
        self.frame_under_top_bar.setMinimumSize(QSize(0, 20))
        self.frame_under_top_bar.setStyleSheet(u"border-top-left-radius: 20px;\n"
"background-color: rgb(47, 49, 54);")
        self.frame_under_top_bar.setFrameShape(QFrame.NoFrame)
        self.frame_under_top_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_under_top_bar)

        self.frame_pages = QFrame(self.frame_main_pages)
        self.frame_pages.setObjectName(u"frame_pages")
        self.frame_pages.setStyleSheet(u"")
        self.frame_pages.setFrameShape(QFrame.NoFrame)
        self.frame_pages.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_pages)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setStyleSheet(u"background: transparent;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pages_widget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pages_widget.addWidget(self.page_2)

        self.verticalLayout_6.addWidget(self.pages_widget)


        self.verticalLayout_5.addWidget(self.frame_pages)

        self.frame_bottom_bar = QFrame(self.frame_main_pages)
        self.frame_bottom_bar.setObjectName(u"frame_bottom_bar")
        self.frame_bottom_bar.setMinimumSize(QSize(0, 20))
        self.frame_bottom_bar.setMaximumSize(QSize(16777215, 20))
        self.frame_bottom_bar.setStyleSheet(u"background-color: rgb(41, 43, 47);")
        self.frame_bottom_bar.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_bottom_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_designed_by = QFrame(self.frame_bottom_bar)
        self.frame_designed_by.setObjectName(u"frame_designed_by")
        self.frame_designed_by.setFrameShape(QFrame.NoFrame)
        self.frame_designed_by.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_designed_by)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_designed_by)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_designed_by, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.frame_bottom_bar)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel{\n"
"	margin-right: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")
        self.label_2.setMidLineWidth(0)
        self.label_2.setTextFormat(Qt.AutoText)

        self.horizontalLayout_7.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"	margin-right: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_3)


        self.horizontalLayout_6.addWidget(self.frame_2, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_bottom_bar)


        self.horizontalLayout_2.addWidget(self.frame_main_pages)


        self.verticalLayout.addWidget(self.Content)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_burger.setText("")
        self.pushButton_4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Contact Data Scraper", None))
        self.button_minimalize.setText("")
        self.button_full_screen.setText("")
        self.button_exit.setText("")
        self.button_menu_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_menu_home_2.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_menu_home_3.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.button_settings.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Designed by Adrian W\u0142odarczyk", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

