# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainHuwQgi.ui'
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
        MainWindow.resize(1069, 783)
        MainWindow.setStyleSheet(u"background-color: rgb(32, 34, 37);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1000, 500))
        self.centralwidget.setLocale(QLocale(QLocale.Polish, QLocale.Poland))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_window = QFrame(self.centralwidget)
        self.frame_main_window.setObjectName(u"frame_main_window")
        self.frame_main_window.setMinimumSize(QSize(0, 100))
        self.frame_main_window.setFrameShape(QFrame.NoFrame)
        self.frame_main_window.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_main_window)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Top_Bar = QFrame(self.frame_main_window)
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
        self.frame_top_moving = QFrame(self.frame)
        self.frame_top_moving.setObjectName(u"frame_top_moving")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_top_moving.sizePolicy().hasHeightForWidth())
        self.frame_top_moving.setSizePolicy(sizePolicy1)
        self.frame_top_moving.setFrameShape(QFrame.NoFrame)
        self.frame_top_moving.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_top_moving)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_top_moving)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
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

        self.horizontalLayout_25.addWidget(self.pushButton_4)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(185, 187, 190);\n"
"")

        self.horizontalLayout_25.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.frame_3, 0, Qt.AlignLeft)


        self.horizontalLayout_3.addWidget(self.frame_top_moving)

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


        self.verticalLayout_28.addWidget(self.Top_Bar)

        self.Content = QFrame(self.frame_main_window)
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
"	background-image: url(:/24x24/icons/24x24/cil-home.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_home)

        self.button_menu_files = QPushButton(self.frame_left_top_menu)
        self.button_menu_files.setObjectName(u"button_menu_files")
        self.button_menu_files.setMinimumSize(QSize(0, 70))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Black")
        font2.setBold(False)
        font2.setWeight(50)
        self.button_menu_files.setFont(font2)
        self.button_menu_files.setStyleSheet(u"QPushButton{\n"
"	margin-top:10px;\n"
"	margin-bottom:10px;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	color: rgb(185, 187, 190);\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 25px;\n"
"	border: 0px solid;\n"
"	background-image: url(:/24x24/icons/24x24/cil-camera-roll.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_files)

        self.button_menu_home_3 = QPushButton(self.frame_left_top_menu)
        self.button_menu_home_3.setObjectName(u"button_menu_home_3")
        self.button_menu_home_3.setMinimumSize(QSize(0, 70))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Black")
        self.button_menu_home_3.setFont(font3)
        self.button_menu_home_3.setStyleSheet(u"QPushButton{\n"
"	margin-top:10px;\n"
"	margin-bottom:10px;\n"
"	margin-left:10px;\n"
"	margin-right:10px;\n"
"	color: rgb(185, 187, 190);\n"
"	background-color: rgb(54, 57, 63);\n"
"	border-radius: 25px;\n"
"	border: 0px solid;\n"
"	background-image: url(:/24x24/icons/24x24/cil-justify-center.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(54, 57, 63);\n"
"	background-color: rgb(185, 187, 190);\n"
"	border-radius: 7px;\n"
"}")

        self.verticalLayout_4.addWidget(self.button_menu_home_3)


        self.verticalLayout_3.addWidget(self.frame_left_top_menu)

        self.frame_left_bottom = QFrame(self.frame_left_menu)
        self.frame_left_bottom.setObjectName(u"frame_left_bottom")
        self.frame_left_bottom.setMinimumSize(QSize(70, 90))
        self.frame_left_bottom.setStyleSheet(u"QFrame{\n"
"	margin-bottom: 20px;\n"
"}")
        self.frame_left_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_left_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_left_bottom)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_settings = QFrame(self.frame_left_bottom)
        self.frame_settings.setObjectName(u"frame_settings")
        self.frame_settings.setStyleSheet(u"margin: 0px;")
        self.frame_settings.setFrameShape(QFrame.NoFrame)
        self.frame_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_settings)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.button_settings = QPushButton(self.frame_settings)
        self.button_settings.setObjectName(u"button_settings")
        sizePolicy.setHeightForWidth(self.button_settings.sizePolicy().hasHeightForWidth())
        self.button_settings.setSizePolicy(sizePolicy)
        self.button_settings.setMinimumSize(QSize(50, 50))
        self.button_settings.setMaximumSize(QSize(16777215, 16777215))
        self.button_settings.setStyleSheet(u"QPushButton{\n"
"	background-image: url(:/24x24/icons/24x24/cil-settings.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: 0px solid;\n"
"	margin-bottom: 0px;\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(54, 57, 63);\n"
"}")

        self.verticalLayout_25.addWidget(self.button_settings)


        self.verticalLayout_8.addWidget(self.frame_settings, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.frame_left_bottom, 0, Qt.AlignBottom)


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
        self.verticalLayout_6.setContentsMargins(15, -1, -1, -1)
        self.pages_widget = QStackedWidget(self.frame_pages)
        self.pages_widget.setObjectName(u"pages_widget")
        self.pages_widget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_22 = QVBoxLayout(self.page_home)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.frame_home = QFrame(self.page_home)
        self.frame_home.setObjectName(u"frame_home")
        self.frame_home.setFrameShape(QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_home)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.frame_search = QFrame(self.frame_home)
        self.frame_search.setObjectName(u"frame_search")
        sizePolicy.setHeightForWidth(self.frame_search.sizePolicy().hasHeightForWidth())
        self.frame_search.setSizePolicy(sizePolicy)
        self.frame_search.setMinimumSize(QSize(400, 0))
        self.frame_search.setMaximumSize(QSize(16777215, 16777215))
        self.frame_search.setLayoutDirection(Qt.LeftToRight)
        self.frame_search.setFrameShape(QFrame.NoFrame)
        self.frame_search.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_search)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.text_search = QTextEdit(self.frame_search)
        self.text_search.setObjectName(u"text_search")
        sizePolicy.setHeightForWidth(self.text_search.sizePolicy().hasHeightForWidth())
        self.text_search.setSizePolicy(sizePolicy)
        self.text_search.setMinimumSize(QSize(0, 0))
        self.text_search.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setPointSize(16)
        self.text_search.setFont(font4)
        self.text_search.setStyleSheet(u"background-color: rgb(185, 187, 190);\n"
"border-radius: 5px;")
        self.text_search.setFrameShape(QFrame.NoFrame)
        self.text_search.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_26.addWidget(self.text_search, 0, Qt.AlignVCenter)


        self.verticalLayout_24.addWidget(self.frame_search, 0, Qt.AlignVCenter)

        self.frame_run = QFrame(self.frame_home)
        self.frame_run.setObjectName(u"frame_run")
        self.frame_run.setFrameShape(QFrame.StyledPanel)
        self.frame_run.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_run)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.button_run = QPushButton(self.frame_run)
        self.button_run.setObjectName(u"button_run")
        self.button_run.setMinimumSize(QSize(200, 200))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(40)
        self.button_run.setFont(font5)
        self.button_run.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(32, 34, 37);\n"
"color: rgb(185, 187, 190);\n"
"border-radius: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(41, 43, 47);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(32, 42, 47);\n"
"}")

        self.verticalLayout_27.addWidget(self.button_run, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_24.addWidget(self.frame_run)


        self.verticalLayout_22.addWidget(self.frame_home)

        self.pages_widget.addWidget(self.page_home)
        self.page_data = QWidget()
        self.page_data.setObjectName(u"page_data")
        self.pages_widget.addWidget(self.page_data)
        self.page_lists = QWidget()
        self.page_lists.setObjectName(u"page_lists")
        self.pages_widget.addWidget(self.page_lists)
        self.page_settings = QWidget()
        self.page_settings.setObjectName(u"page_settings")
        self.verticalLayout_9 = QVBoxLayout(self.page_settings)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_page_settings = QFrame(self.page_settings)
        self.frame_page_settings.setObjectName(u"frame_page_settings")
        self.frame_page_settings.setStyleSheet(u"QPushButton{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(171, 171, 172);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: rgb(111, 111, 111);\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(171, 171, 172);\n"
"}\n"
"\n"
"QCheckBox {\n"
"	color: rgb(171, 171, 172);\n"
"}")
        self.frame_page_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_page_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_page_settings)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_categories = QFrame(self.frame_page_settings)
        self.frame_categories.setObjectName(u"frame_categories")
        self.frame_categories.setMinimumSize(QSize(0, 40))
        self.frame_categories.setFrameShape(QFrame.StyledPanel)
        self.frame_categories.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_categories)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_categories_2 = QFrame(self.frame_categories)
        self.frame_categories_2.setObjectName(u"frame_categories_2")
        self.frame_categories_2.setFrameShape(QFrame.StyledPanel)
        self.frame_categories_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_categories_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_engines = QFrame(self.frame_categories_2)
        self.frame_engines.setObjectName(u"frame_engines")
        self.frame_engines.setFrameShape(QFrame.StyledPanel)
        self.frame_engines.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_engines)
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.button_google = QPushButton(self.frame_engines)
        self.button_google.setObjectName(u"button_google")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_google.sizePolicy().hasHeightForWidth())
        self.button_google.setSizePolicy(sizePolicy2)
        self.button_google.setMinimumSize(QSize(80, 40))
        self.button_google.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.button_google)

        self.button_categories = QPushButton(self.frame_engines)
        self.button_categories.setObjectName(u"button_categories")
        self.button_categories.setMinimumSize(QSize(80, 40))
        self.button_categories.setStyleSheet(u"")

        self.horizontalLayout_18.addWidget(self.button_categories)


        self.horizontalLayout_9.addWidget(self.frame_engines, 0, Qt.AlignLeft)

        self.frame_settings_load_save = QFrame(self.frame_categories_2)
        self.frame_settings_load_save.setObjectName(u"frame_settings_load_save")
        self.frame_settings_load_save.setFrameShape(QFrame.StyledPanel)
        self.frame_settings_load_save.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_settings_load_save)
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_settings_file = QLabel(self.frame_settings_load_save)
        self.label_settings_file.setObjectName(u"label_settings_file")
        self.label_settings_file.setMinimumSize(QSize(0, 40))
        self.label_settings_file.setStyleSheet(u"color: rgb(171, 171, 172);")

        self.horizontalLayout_26.addWidget(self.label_settings_file)

        self.button_settings_new = QPushButton(self.frame_settings_load_save)
        self.button_settings_new.setObjectName(u"button_settings_new")
        self.button_settings_new.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_26.addWidget(self.button_settings_new)

        self.button_settings_load = QPushButton(self.frame_settings_load_save)
        self.button_settings_load.setObjectName(u"button_settings_load")
        self.button_settings_load.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_26.addWidget(self.button_settings_load)

        self.button_settings_save = QPushButton(self.frame_settings_load_save)
        self.button_settings_save.setObjectName(u"button_settings_save")
        self.button_settings_save.setMinimumSize(QSize(80, 40))

        self.horizontalLayout_26.addWidget(self.button_settings_save)


        self.horizontalLayout_9.addWidget(self.frame_settings_load_save, 0, Qt.AlignRight)


        self.verticalLayout_11.addWidget(self.frame_categories_2)


        self.verticalLayout_10.addWidget(self.frame_categories)

        self.scrollArea = QScrollArea(self.frame_page_settings)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 975, 645))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_12.setSpacing(20)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 10, 10, 10)
        self.frame_google_engine = QFrame(self.scrollAreaWidgetContents)
        self.frame_google_engine.setObjectName(u"frame_google_engine")
        sizePolicy2.setHeightForWidth(self.frame_google_engine.sizePolicy().hasHeightForWidth())
        self.frame_google_engine.setSizePolicy(sizePolicy2)
        self.frame_google_engine.setMinimumSize(QSize(0, 0))
        self.frame_google_engine.setStyleSheet(u"QFrame{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(41, 43, 47);\n"
"}")
        self.frame_google_engine.setFrameShape(QFrame.NoFrame)
        self.frame_google_engine.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_google_engine)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_google_top_bar = QFrame(self.frame_google_engine)
        self.frame_google_top_bar.setObjectName(u"frame_google_top_bar")
        self.frame_google_top_bar.setMinimumSize(QSize(0, 20))
        self.frame_google_top_bar.setMaximumSize(QSize(16777215, 25))
        self.frame_google_top_bar.setStyleSheet(u"QFrame{\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-color: rgb(47, 49, 54);\n"
"}")
        self.frame_google_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_google_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_google_top_bar)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_google_top_bar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 0, 0, 0)
        self.label_google = QLabel(self.frame_5)
        self.label_google.setObjectName(u"label_google")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        self.label_google.setFont(font6)
        self.label_google.setStyleSheet(u"color: rgb(171, 171, 172);")
        self.label_google.setFrameShape(QFrame.Box)

        self.horizontalLayout_11.addWidget(self.label_google)


        self.horizontalLayout_10.addWidget(self.frame_5, 0, Qt.AlignLeft)


        self.verticalLayout_13.addWidget(self.frame_google_top_bar)

        self.frame_google_main = QFrame(self.frame_google_engine)
        self.frame_google_main.setObjectName(u"frame_google_main")
        self.frame_google_main.setStyleSheet(u"background-color: none;\n"
"border-radius: none;\n"
"color: rgb(171, 171, 172);")
        self.frame_google_main.setFrameShape(QFrame.StyledPanel)
        self.frame_google_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_google_main)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.frame_7 = QFrame(self.frame_google_main)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 40))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_google_how_many_pages = QLabel(self.frame_7)
        self.label_google_how_many_pages.setObjectName(u"label_google_how_many_pages")

        self.horizontalLayout_14.addWidget(self.label_google_how_many_pages)

        self.frame_how_many_pages = QFrame(self.frame_7)
        self.frame_how_many_pages.setObjectName(u"frame_how_many_pages")
        self.frame_how_many_pages.setFrameShape(QFrame.StyledPanel)
        self.frame_how_many_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_how_many_pages)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.spin_box_google_pages = QSpinBox(self.frame_how_many_pages)
        self.spin_box_google_pages.setObjectName(u"spin_box_google_pages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.spin_box_google_pages.sizePolicy().hasHeightForWidth())
        self.spin_box_google_pages.setSizePolicy(sizePolicy3)
        self.spin_box_google_pages.setMinimum(1)
        self.spin_box_google_pages.setMaximum(15)

        self.horizontalLayout_15.addWidget(self.spin_box_google_pages)


        self.horizontalLayout_14.addWidget(self.frame_how_many_pages, 0, Qt.AlignLeft)


        self.verticalLayout_15.addWidget(self.frame_7)

        self.frame_15 = QFrame(self.frame_google_main)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_user_agent = QLabel(self.frame_15)
        self.label_user_agent.setObjectName(u"label_user_agent")

        self.horizontalLayout_19.addWidget(self.label_user_agent)

        self.frame_16 = QFrame(self.frame_15)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_16)
        self.verticalLayout_17.setSpacing(8)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.radio_desktop = QRadioButton(self.frame_16)
        self.radio_desktop.setObjectName(u"radio_desktop")

        self.verticalLayout_17.addWidget(self.radio_desktop)

        self.radio_mobile = QRadioButton(self.frame_16)
        self.radio_mobile.setObjectName(u"radio_mobile")

        self.verticalLayout_17.addWidget(self.radio_mobile)


        self.horizontalLayout_19.addWidget(self.frame_16)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.frame_12 = QFrame(self.frame_google_main)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_8 = QLabel(self.frame_12)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_17.addWidget(self.label_8)

        self.check_google_pages = QCheckBox(self.frame_12)
        self.check_google_pages.setObjectName(u"check_google_pages")

        self.horizontalLayout_17.addWidget(self.check_google_pages)


        self.verticalLayout_15.addWidget(self.frame_12)

        self.frame_10 = QFrame(self.frame_google_main)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy4)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_16.addWidget(self.label_7)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setSpacing(8)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.radio_html = QRadioButton(self.frame_11)
        self.radio_html.setObjectName(u"radio_html")

        self.verticalLayout_16.addWidget(self.radio_html)

        self.radio_lxml = QRadioButton(self.frame_11)
        self.radio_lxml.setObjectName(u"radio_lxml")

        self.verticalLayout_16.addWidget(self.radio_lxml)


        self.horizontalLayout_16.addWidget(self.frame_11)


        self.verticalLayout_15.addWidget(self.frame_10)


        self.verticalLayout_13.addWidget(self.frame_google_main, 0, Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.frame_google_engine)

        self.frame_general_settings = QFrame(self.scrollAreaWidgetContents)
        self.frame_general_settings.setObjectName(u"frame_general_settings")
        self.frame_general_settings.setMinimumSize(QSize(0, 0))
        self.frame_general_settings.setMaximumSize(QSize(16777215, 400))
        self.frame_general_settings.setStyleSheet(u"QFrame{\n"
"	border-radius: 20px;\n"
"	background-color: rgb(41, 43, 47);\n"
"}")
        self.frame_general_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_general_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_general_settings)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_general_top_bar = QFrame(self.frame_general_settings)
        self.frame_general_top_bar.setObjectName(u"frame_general_top_bar")
        self.frame_general_top_bar.setMinimumSize(QSize(0, 25))
        self.frame_general_top_bar.setMaximumSize(QSize(16777215, 25))
        self.frame_general_top_bar.setStyleSheet(u"QFrame{\n"
"	border-bottom-left-radius: 0px;\n"
"	border-bottom-right-radius: 0px;\n"
"	background-color: rgb(47, 49, 54);\n"
"}")
        self.frame_general_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_general_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_general_top_bar)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_label_general = QFrame(self.frame_general_top_bar)
        self.frame_label_general.setObjectName(u"frame_label_general")
        self.frame_label_general.setFrameShape(QFrame.StyledPanel)
        self.frame_label_general.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_label_general)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 0, 0, 0)
        self.label_general = QLabel(self.frame_label_general)
        self.label_general.setObjectName(u"label_general")
        self.label_general.setFont(font6)
        self.label_general.setStyleSheet(u"color: rgb(171, 171, 172);")
        self.label_general.setFrameShape(QFrame.Box)

        self.horizontalLayout_12.addWidget(self.label_general)


        self.horizontalLayout_13.addWidget(self.frame_label_general, 0, Qt.AlignLeft)


        self.verticalLayout_14.addWidget(self.frame_general_top_bar)

        self.frame_general_main = QFrame(self.frame_general_settings)
        self.frame_general_main.setObjectName(u"frame_general_main")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_general_main.sizePolicy().hasHeightForWidth())
        self.frame_general_main.setSizePolicy(sizePolicy5)
        self.frame_general_main.setMinimumSize(QSize(0, 0))
        self.frame_general_main.setStyleSheet(u"")
        self.frame_general_main.setFrameShape(QFrame.NoFrame)
        self.frame_general_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_general_main)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_general_main_in = QFrame(self.frame_general_main)
        self.frame_general_main_in.setObjectName(u"frame_general_main_in")
        self.frame_general_main_in.setMinimumSize(QSize(0, 0))
        self.frame_general_main_in.setStyleSheet(u"")
        self.frame_general_main_in.setFrameShape(QFrame.NoFrame)
        self.frame_general_main_in.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_general_main_in)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_external_pages = QFrame(self.frame_general_main_in)
        self.label_external_pages.setObjectName(u"label_external_pages")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_external_pages.sizePolicy().hasHeightForWidth())
        self.label_external_pages.setSizePolicy(sizePolicy6)
        self.label_external_pages.setFrameShape(QFrame.NoFrame)
        self.label_external_pages.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.label_external_pages)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_external = QLabel(self.label_external_pages)
        self.label_external.setObjectName(u"label_external")

        self.horizontalLayout_20.addWidget(self.label_external)

        self.check_external = QCheckBox(self.label_external_pages)
        self.check_external.setObjectName(u"check_external")

        self.horizontalLayout_20.addWidget(self.check_external)


        self.verticalLayout_23.addWidget(self.label_external_pages, 0, Qt.AlignLeft)

        self.frame_black_list = QFrame(self.frame_general_main_in)
        self.frame_black_list.setObjectName(u"frame_black_list")
        sizePolicy6.setHeightForWidth(self.frame_black_list.sizePolicy().hasHeightForWidth())
        self.frame_black_list.setSizePolicy(sizePolicy6)
        self.frame_black_list.setFrameShape(QFrame.NoFrame)
        self.frame_black_list.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_black_list)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_black_list = QLabel(self.frame_black_list)
        self.label_black_list.setObjectName(u"label_black_list")

        self.horizontalLayout_22.addWidget(self.label_black_list)

        self.label_black_list_file = QLabel(self.frame_black_list)
        self.label_black_list_file.setObjectName(u"label_black_list_file")
        self.label_black_list_file.setMinimumSize(QSize(200, 0))
        self.label_black_list_file.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_22.addWidget(self.label_black_list_file, 0, Qt.AlignLeft)

        self.button_black_list_load = QPushButton(self.frame_black_list)
        self.button_black_list_load.setObjectName(u"button_black_list_load")
        self.button_black_list_load.setMinimumSize(QSize(80, 20))
        self.button_black_list_load.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.button_black_list_load)

        self.button_black_list_open = QPushButton(self.frame_black_list)
        self.button_black_list_open.setObjectName(u"button_black_list_open")
        self.button_black_list_open.setMinimumSize(QSize(80, 20))
        self.button_black_list_open.setStyleSheet(u"")

        self.horizontalLayout_22.addWidget(self.button_black_list_open)


        self.verticalLayout_23.addWidget(self.frame_black_list, 0, Qt.AlignLeft)

        self.frame_contact_data = QFrame(self.frame_general_main_in)
        self.frame_contact_data.setObjectName(u"frame_contact_data")
        sizePolicy6.setHeightForWidth(self.frame_contact_data.sizePolicy().hasHeightForWidth())
        self.frame_contact_data.setSizePolicy(sizePolicy6)
        self.frame_contact_data.setFrameShape(QFrame.NoFrame)
        self.frame_contact_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_contact_data)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_contact_data_1 = QFrame(self.frame_contact_data)
        self.frame_contact_data_1.setObjectName(u"frame_contact_data_1")
        sizePolicy6.setHeightForWidth(self.frame_contact_data_1.sizePolicy().hasHeightForWidth())
        self.frame_contact_data_1.setSizePolicy(sizePolicy6)
        self.frame_contact_data_1.setFrameShape(QFrame.NoFrame)
        self.frame_contact_data_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_contact_data_1)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label__contact_data = QLabel(self.frame_contact_data_1)
        self.label__contact_data.setObjectName(u"label__contact_data")

        self.horizontalLayout_23.addWidget(self.label__contact_data)

        self.check_contact_data = QCheckBox(self.frame_contact_data_1)
        self.check_contact_data.setObjectName(u"check_contact_data")

        self.horizontalLayout_23.addWidget(self.check_contact_data)


        self.verticalLayout_20.addWidget(self.frame_contact_data_1, 0, Qt.AlignLeft)

        self.frame_contact_data_2 = QFrame(self.frame_contact_data)
        self.frame_contact_data_2.setObjectName(u"frame_contact_data_2")
        self.frame_contact_data_2.setMinimumSize(QSize(0, 0))
        self.frame_contact_data_2.setFrameShape(QFrame.NoFrame)
        self.frame_contact_data_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_contact_data_2)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(30, 9, 9, 0)
        self.check_phone = QCheckBox(self.frame_contact_data_2)
        self.check_phone.setObjectName(u"check_phone")

        self.verticalLayout_19.addWidget(self.check_phone)

        self.check_email = QCheckBox(self.frame_contact_data_2)
        self.check_email.setObjectName(u"check_email")

        self.verticalLayout_19.addWidget(self.check_email)

        self.check_address = QCheckBox(self.frame_contact_data_2)
        self.check_address.setObjectName(u"check_address")

        self.verticalLayout_19.addWidget(self.check_address)

        self.check_city = QCheckBox(self.frame_contact_data_2)
        self.check_city.setObjectName(u"check_city")

        self.verticalLayout_19.addWidget(self.check_city)

        self.check_postal = QCheckBox(self.frame_contact_data_2)
        self.check_postal.setObjectName(u"check_postal")

        self.verticalLayout_19.addWidget(self.check_postal)

        self.check_nip = QCheckBox(self.frame_contact_data_2)
        self.check_nip.setObjectName(u"check_nip")

        self.verticalLayout_19.addWidget(self.check_nip)

        self.check_regon = QCheckBox(self.frame_contact_data_2)
        self.check_regon.setObjectName(u"check_regon")

        self.verticalLayout_19.addWidget(self.check_regon)


        self.verticalLayout_20.addWidget(self.frame_contact_data_2, 0, Qt.AlignLeft)


        self.verticalLayout_23.addWidget(self.frame_contact_data, 0, Qt.AlignLeft)

        self.frame_krs = QFrame(self.frame_general_main_in)
        self.frame_krs.setObjectName(u"frame_krs")
        sizePolicy6.setHeightForWidth(self.frame_krs.sizePolicy().hasHeightForWidth())
        self.frame_krs.setSizePolicy(sizePolicy6)
        self.frame_krs.setFrameShape(QFrame.NoFrame)
        self.frame_krs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_krs)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_krs1 = QFrame(self.frame_krs)
        self.frame_krs1.setObjectName(u"frame_krs1")
        sizePolicy6.setHeightForWidth(self.frame_krs1.sizePolicy().hasHeightForWidth())
        self.frame_krs1.setSizePolicy(sizePolicy6)
        self.frame_krs1.setFrameShape(QFrame.NoFrame)
        self.frame_krs1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_krs1)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label__krs = QLabel(self.frame_krs1)
        self.label__krs.setObjectName(u"label__krs")

        self.horizontalLayout_24.addWidget(self.label__krs)

        self.check_krs = QCheckBox(self.frame_krs1)
        self.check_krs.setObjectName(u"check_krs")

        self.horizontalLayout_24.addWidget(self.check_krs)


        self.verticalLayout_21.addWidget(self.frame_krs1, 0, Qt.AlignLeft)


        self.verticalLayout_23.addWidget(self.frame_krs, 0, Qt.AlignLeft)


        self.verticalLayout_18.addWidget(self.frame_general_main_in)


        self.verticalLayout_14.addWidget(self.frame_general_main)


        self.verticalLayout_12.addWidget(self.frame_general_settings)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.verticalLayout_9.addWidget(self.frame_page_settings)

        self.pages_widget.addWidget(self.page_settings)

        self.verticalLayout_6.addWidget(self.pages_widget)


        self.verticalLayout_5.addWidget(self.frame_pages)

        self.frame_bottom_bar = QFrame(self.frame_main_pages)
        self.frame_bottom_bar.setObjectName(u"frame_bottom_bar")
        self.frame_bottom_bar.setMinimumSize(QSize(0, 20))
        self.frame_bottom_bar.setMaximumSize(QSize(16777215, 20))
        self.frame_bottom_bar.setStyleSheet(u"QFrame{\n"
"background-color: rgb(41, 43, 47);\n"
"border-radius: 0px;\n"
"}")
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
        self.label_4.setFont(font6)
        self.label_4.setStyleSheet(u"QLabel{\n"
"	margin-left: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")

        self.horizontalLayout_8.addWidget(self.label_4)


        self.horizontalLayout_6.addWidget(self.frame_designed_by, 0, Qt.AlignLeft)

        self.frame_bottom_right = QFrame(self.frame_bottom_bar)
        self.frame_bottom_right.setObjectName(u"frame_bottom_right")
        self.frame_bottom_right.setMinimumSize(QSize(0, 0))
        self.frame_bottom_right.setFrameShape(QFrame.NoFrame)
        self.frame_bottom_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_bottom_right)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_version_01 = QLabel(self.frame_bottom_right)
        self.label_version_01.setObjectName(u"label_version_01")
        self.label_version_01.setStyleSheet(u"QLabel{\n"
"	margin-right: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")
        self.label_version_01.setMidLineWidth(0)
        self.label_version_01.setTextFormat(Qt.AutoText)

        self.horizontalLayout_7.addWidget(self.label_version_01)

        self.label_version_02 = QLabel(self.frame_bottom_right)
        self.label_version_02.setObjectName(u"label_version_02")
        self.label_version_02.setStyleSheet(u"QLabel{\n"
"	margin-right: 10px;\n"
"	color: rgb(185, 187, 190);\n"
"}")

        self.horizontalLayout_7.addWidget(self.label_version_02)

        self.frame_resize_window = QFrame(self.frame_bottom_right)
        self.frame_resize_window.setObjectName(u"frame_resize_window")
        sizePolicy.setHeightForWidth(self.frame_resize_window.sizePolicy().hasHeightForWidth())
        self.frame_resize_window.setSizePolicy(sizePolicy)
        self.frame_resize_window.setMinimumSize(QSize(20, 20))
        self.frame_resize_window.setMaximumSize(QSize(20, 20))
        self.frame_resize_window.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	background-color: rgb(41, 43, 47);\n"
"}")
        self.frame_resize_window.setFrameShape(QFrame.NoFrame)
        self.frame_resize_window.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_resize_window)


        self.horizontalLayout_6.addWidget(self.frame_bottom_right, 0, Qt.AlignRight)


        self.verticalLayout_5.addWidget(self.frame_bottom_bar)


        self.horizontalLayout_2.addWidget(self.frame_main_pages)


        self.verticalLayout_28.addWidget(self.Content)


        self.verticalLayout.addWidget(self.frame_main_window)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages_widget.setCurrentIndex(3)


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
        self.button_menu_home.setText("")
        self.button_menu_files.setText("")
        self.button_menu_home_3.setText("")
        self.button_settings.setText("")
        self.button_run.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.button_google.setText(QCoreApplication.translate("MainWindow", u"GoogleEngine", None))
        self.button_categories.setText(QCoreApplication.translate("MainWindow", u"Categories", None))
        self.label_settings_file.setText(QCoreApplication.translate("MainWindow", u"config.cfg", None))
        self.button_settings_new.setText(QCoreApplication.translate("MainWindow", u"New", None))
        self.button_settings_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.button_settings_save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_google.setText(QCoreApplication.translate("MainWindow", u"Google Engine", None))
        self.label_google_how_many_pages.setText(QCoreApplication.translate("MainWindow", u"How many pages to scrap? (1-15)", None))
        self.label_user_agent.setText(QCoreApplication.translate("MainWindow", u"User agent", None))
        self.radio_desktop.setText(QCoreApplication.translate("MainWindow", u"desktop", None))
        self.radio_mobile.setText(QCoreApplication.translate("MainWindow", u"mobile", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Save google pages links?", None))
        self.check_google_pages.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Parser", None))
        self.radio_html.setText(QCoreApplication.translate("MainWindow", u"html.parser", None))
        self.radio_lxml.setText(QCoreApplication.translate("MainWindow", u"lxml", None))
        self.label_general.setText(QCoreApplication.translate("MainWindow", u"General Settings", None))
        self.label_external.setText(QCoreApplication.translate("MainWindow", u"Search external pages?", None))
        self.check_external.setText("")
        self.label_black_list.setText(QCoreApplication.translate("MainWindow", u"Black list links file:", None))
        self.label_black_list_file.setText(QCoreApplication.translate("MainWindow", u"some_file.txt", None))
        self.button_black_list_load.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.button_black_list_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label__contact_data.setText(QCoreApplication.translate("MainWindow", u"Search contact data?", None))
        self.check_contact_data.setText("")
        self.check_phone.setText(QCoreApplication.translate("MainWindow", u"phone number", None))
        self.check_email.setText(QCoreApplication.translate("MainWindow", u"email", None))
        self.check_address.setText(QCoreApplication.translate("MainWindow", u"address (future release)", None))
        self.check_city.setText(QCoreApplication.translate("MainWindow", u"city (future release)", None))
        self.check_postal.setText(QCoreApplication.translate("MainWindow", u"postal code (future release)", None))
        self.check_nip.setText(QCoreApplication.translate("MainWindow", u"nip", None))
        self.check_regon.setText(QCoreApplication.translate("MainWindow", u"regon (future release)", None))
        self.label__krs.setText(QCoreApplication.translate("MainWindow", u"Search krs data? (future release)", None))
        self.check_krs.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Designed by Adrian W\u0142odarczyk", None))
        self.label_version_01.setText(QCoreApplication.translate("MainWindow", u"Alpha", None))
        self.label_version_02.setText(QCoreApplication.translate("MainWindow", u"v0.0.1", None))
    # retranslateUi

