# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (Qt)
import subprocess
import time
import images_rc

psw = '123'
path = '/home/furkan'

class Ui_Giris(object):
    def setupUi(self, Giris):
        Giris.setObjectName("Giris")
        Giris.setWindowModality(QtCore.Qt.ApplicationModal)
        Giris.setEnabled(True)
        Giris.resize(300, 131)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Giris.sizePolicy().hasHeightForWidth())
        Giris.setSizePolicy(sizePolicy)
        Giris.setMaximumSize(QtCore.QSize(300, 131))
        Giris.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        Giris.setAcceptDrops(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/lock-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Giris.setWindowIcon(icon)
        Giris.setWindowOpacity(1.0)
        Giris.setAccessibleName("")
        Giris.setStyleSheet("#ana{\n"
"border: none;\n"
"padding: 10px;\n"
"border-radius: 30px;\n"
"}\n"
"#loginFrame {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(0, 0, 0), stop: 1 rgb(20, 20, 20));\n"
"border: 1px solid gray;\n"
"padding: 10px;\n"
"border-radius: 30px;\n"
"}\n"
"#btn,#clos {\n"
"    background-color: rgba( 0, 0, 0, 0% );\n"
"    border: 1px solid black;\n"
"}\n"
" \n"
"#btn:hover,#clos:hover{\n"
"    background-color: rgb(91, 91, 91)\n"
"}\n"
" \n"
"#btn:pressed, #btn:default:hover:pressed,#clos:pressed,#clos:default:hover:pressed\n"
"{\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"")
        Giris.setAnimated(True)
        Giris.setDocumentMode(False)
        Giris.setTabShape(QtWidgets.QTabWidget.Rounded)
        Giris.setDockNestingEnabled(False)
        Giris.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        Giris.setUnifiedTitleAndToolBarOnMac(False)
        self.ana = QtWidgets.QWidget(Giris)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ana.sizePolicy().hasHeightForWidth())
        self.ana.setSizePolicy(sizePolicy)
        self.ana.setMaximumSize(QtCore.QSize(300, 131))
        self.ana.setStyleSheet("")
        self.ana.setObjectName("ana")
        self.loginFrame = QtWidgets.QFrame(self.ana)
        self.loginFrame.setGeometry(QtCore.QRect(0, 0, 300, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginFrame.sizePolicy().hasHeightForWidth())
        self.loginFrame.setSizePolicy(sizePolicy)
        self.loginFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.loginFrame.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setObjectName("loginFrame")
        self.clos = QtWidgets.QPushButton(self.loginFrame)
        self.clos.setGeometry(QtCore.QRect(260, 10, 31, 27))
        self.clos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clos.setMouseTracking(True)
        self.clos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clos.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/img/coloredIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clos.setIcon(icon1)
        self.clos.setObjectName("clos")
        self.layoutWidget = QtWidgets.QWidget(self.loginFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 50, 281, 71))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sifre = QtWidgets.QLineEdit(self.layoutWidget)
        self.sifre.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sifre.sizePolicy().hasHeightForWidth())
        self.sifre.setSizePolicy(sizePolicy)
        self.sifre.setMinimumSize(QtCore.QSize(0, 0))
        self.sifre.setToolTip("")
        self.sifre.setAutoFillBackground(False)
        self.sifre.setInputMask("")
        self.sifre.setText("")
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sifre.setObjectName("sifre")
        self.horizontalLayout.addWidget(self.sifre)
        self.btn = QtWidgets.QPushButton(self.layoutWidget)
        self.btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn.sizePolicy().hasHeightForWidth())
        self.btn.setSizePolicy(sizePolicy)
        self.btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/img/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn.setIcon(icon2)
        self.btn.setIconSize(QtCore.QSize(45, 40))
        self.btn.setObjectName("btn")
        self.horizontalLayout.addWidget(self.btn)
        self.label = QtWidgets.QLabel(self.loginFrame)
        self.label.setGeometry(QtCore.QRect(10, 10, 251, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        self.label.setPalette(palette)
        self.label.setMouseTracking(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        Giris.setCentralWidget(self.ana)

        self.retranslateUi(Giris)
        QtCore.QMetaObject.connectSlotsByName(Giris)

    def retranslateUi(self, Giris):
        _translate = QtCore.QCoreApplication.translate
        Giris.setWindowTitle(_translate("Giris", "Şifreyi Giriniz"))
        self.sifre.setPlaceholderText(_translate("Giris", "Şifreniz..."))
        self.label.setText(_translate("Giris", "<html><head/><body><p><span style=\" color:#ffffff;\">Dosya Şifreli Lütfen Şifreyi Giriniz</span></p></body></html>"))

    def kapat(self):
            quit()

    def girisYap(self):
            if(self.sifre.text()==psw):
                    subprocess.check_call(['xdg-open', path])
                    time.sleep(0.1)
                    quit()
            else:
                     QtWidgets.QMessageBox.information(self,"Bilgi","Şifreyi Yanlış Girdiniz.")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if(self.sifre.text()==psw):
                    subprocess.check_call(['xdg-open', path])
                    time.sleep(0.1)
                    quit()
            else:
                    QtWidgets.QMessageBox.information(self,"Bilgi","Şifreyi Yanlış Girdiniz.")
        if event.key() == Qt.Key_Escape:
            quit()

class MyMainWindow(QtWidgets.QMainWindow, Ui_Giris):
        def __init__(self):

            super(MyMainWindow, self).__init__()
            self.setupUi(self)
            self.btn.clicked.connect(self.girisYap)
            self.clos.clicked.connect(self.kapat)
            self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())
