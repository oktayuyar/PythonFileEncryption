#!/usr/bin/python3
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from mainwindow import Ui_MainWindow
#import QtLocation 5.3

app = QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
