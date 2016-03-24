#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#directory encrypts

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtCore import Qt

from mainwindow import Ui_MainWindow
from sifreG import Ui_Giris

psw = '190323'


class AltPen(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.move(300,150)

class AnaPen( QtWidgets.QMainWindow, Ui_Giris):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.altpen = AltPen()
        self.move(500,180)
        self.btn.clicked.connect(self.girisYap)
        self.clos.clicked.connect(self.kapat)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def girisYap(self):
        if(self.sifre.text()==psw):
            self.btn.clicked.connect(self.goster)
        else:
            QtWidgets.QMessageBox.information(self,"Bilgi","Şifreyi Yanlış Girdiniz.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if(self.sifre.text()==psw):
                self.btn.clicked.connect(self.goster)
            else:
                QtWidgets.QMessageBox.information(self,"Bilgi","Şifreyi Yanlış Girdiniz.")
        if event.key() == Qt.Key_Escape:
            quit()

    def kapat(self):
            quit()

    def goster(self):
        self.altpen.show()
        ana.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ana = AnaPen()
    ana.show()
    sys.exit(app.exec_())
