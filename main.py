import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_main_window import Ui_MainWindow

from ui_functions import *


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #######################################################################
        # WINDOW CONTENT (TITLE)
        #######################################################################
        self.setWindowTitle('Contact Data Scraper')

        #######################################################################
        # REMOVE STANDARD TITLE BAR
        #######################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background transparent

        #######################################################################
        # RESIZE WINDOW
        #######################################################################
        startSize = QSize(1000, 720)
        # Initial size
        self.resize(startSize)
        # Minimum size
        self.setMinimumSize(startSize)

        #######################################################################
        # TOOGLE/BURGER MENU FUNCTIONS
        #######################################################################
        self.ui.button_burger.clicked.connect(lambda: UIFunctions.toogle_menu(self, 250, True))

        #######################################################################
        # PAGES
        #######################################################################
        # Home page
        self.ui.button_menu_home.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_home))
        # Settings page
        self.ui.button_settings.clicked.connect(lambda: self.ui.pages_widget.setCurrentWidget(self.ui.page_settings))

        #######################################################################
        # MOVE WINDOW
        #######################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.return_status == 1:
                UIFunctions.maximize_restore()

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_top_moving.mouseMoveEvent = moveWindow

        #######################################################################
        # SHADOW EFFECTS
        #######################################################################
        UIFunctions.shadow_effects(self)

        #######################################################################
        # INTERFACE DEFINITIONS
        #######################################################################
        UIFunctions.ui_definitions(self)

        #######################################################################
        # CONFIG HANDLE
        #######################################################################
        # Initialize config from file to ui
        UIFunctions.config_initialize(self)
        # Update config
        self.ui.button_settings_save.clicked.connect(lambda: UIFunctions.config_update(self, 'config_settings.cfg'))
        # New file
        self.ui.button_settings_new.clicked.connect(lambda: UIFunctions.config_new(self, 'filename????'))
        # Load file
        self.ui.button_settings_load.clicked.connect(lambda: UIFunctions.config_load(self, 'filename?'))

        #######################################################################
        #  HOME PAGE DEFINITIONS
        #######################################################################
        self.ui.button_run.clicked.connect(lambda: UIFunctions.engine_run(self))

        #######################################################################
        # SHOW MAIN WINDOW
        #######################################################################
        self.show()

    #######################################################################
    # EVENT ==> MOUSE CLICK
    #######################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')


#######################################################################
# INITIALIZE APPLICATION
#######################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
