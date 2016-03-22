#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time

from mainwindow import Ui_MainWindow
from sifreG import Ui_Giris



class AltPen(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)

        
class AnaPen( QtWidgets.QMainWindow, Ui_Giris):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.altpen = AltPen()
        self.pushButton.clicked.connect(self.showw)
        
    def showw(self):
        self.altpen.show()
        time.sleep(0.1)
        ana.close()


        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ana = AnaPen()
    ana.show()
    sys.exit(app.exec_())