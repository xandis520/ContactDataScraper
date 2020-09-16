import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from ui_untitled import Ui_MainWindow

# GLOBALS
counter = 0


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # INITIAL PROGRESS BAR VALUE
        self.progressBarValue(0)


        # REMOVE STANDARD TITLE BAR
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Remove title bar
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # Set background transparent

        # APPLY DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 120))
        self.ui.frame_3.setGraphicsEffect(self.shadow)

        # QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(15)

        # Change progress bar value
        # self.progressBarValue(0)

        # Show main window
        self.show()

    def progress(self):
        global counter
        value = counter

        # HTML TEXT PERCENTAGE
        html_text = """<p><span style=" font-size:42pt; color:#ffffff;">{VALUE}</span><span style=" font-size:30pt; color:#ffffff; vertical-align:super;">%</span></p>"""

        # REPLACE VALUE IN HTML
        new_html_text = html_text.replace("{VALUE}", str(int(value)//10*10))

        # APPLY NEW PERCENTAGE TEXT
        self.ui.labelPercentage.setText(new_html_text)

        # SET VALUE TO PROGRESS BAR
        # fix max value error if > than 100
        if value > 100:
            value = 1.000
        self.progressBarValue(value)

        if counter > 100:
            self.timer.stop()
            # self.main = MainWindow()
            # self.main.show()
            self.close()

        counter += 0.5

    def progressBarValue(self, value):
        styleSheet = """
        QFrame{
        	border-radius: 150px;
	        background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(69, 64, 93, 0), stop:{STOP_2} rgba(255, 106, 80, 255));
        }
        """
        progress = (100 - value) / 100.0

        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        newStyleSheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2)

        self.ui.frame_2.setStyleSheet(newStyleSheet)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())