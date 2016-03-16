# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'giris.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import time
from PyQt5.QtWidgets import *
import images_rc
psw = '123'
path = '/home/furkan'
class Ui_Giris(object):
    def setupUi(self, Giris):
        Giris.setObjectName("Giris")
        Giris.setWindowModality(QtCore.Qt.WindowModal)
        Giris.setEnabled(True)
        Giris.resize(310, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Giris.sizePolicy().hasHeightForWidth())
        Giris.setSizePolicy(sizePolicy)
        Giris.setMaximumSize(QtCore.QSize(310, 180))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/img/lock-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Giris.setWindowIcon(icon)
        Giris.setAccessibleName("")
        Giris.setStyleSheet(" #titleLabel {\n"
"background: white;\n"
"color: blue;\n"
"font-size: 20px;\n"
"border: none;\n"
"border-bottom:  1px solid black;\n"
"padding: 5px;\n"
"}\n"
"\n"
"#mainFrame {\n"
"border: none;\n"
"background: transparent;\n"
"}\n"
"\n"
"#loginFrame {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgb(0, 255, 0), stop: 1 rgb(255, 180, 130));\n"
"border: 1px solid gray;\n"
"padding: 10px;\n"
"border-radius: 25px;\n"
"}\n"
"\n"
"#btn {\n"
"    border-radius: 100;\n"
"    border-width: 2;\n"
"    border-color : white;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"#btn:hover{\n"
"     background-color: rgb(0, 255, 255);\n"
"}\n"
" \n"
"#btn:pressed, #btn:default:hover:pressed\n"
"{\n"
"    border-radius: 100;\n"
"    border-width: 2;\n"
"    border-color : white;\n"
"    background-color: transparent;\n"
"}\n"
" \n"
"#btn:focused\n"
"{\n"
"    border-radius: 100;\n"
"    border-width: 2;\n"
"    border-color : white;\n"
"    background-color: transparent;\n"
"}\n"
"\n"
" #sonuc {\n"
"color: red;\n"
"}")
        Giris.setAnimated(True)
        Giris.setDockNestingEnabled(False)
        self.centralWidget = QtWidgets.QWidget(Giris)
        self.centralWidget.setObjectName("centralWidget")
        self.mainFrame = QtWidgets.QFrame(self.centralWidget)
        self.mainFrame.setGeometry(QtCore.QRect(0, -1, 310, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainFrame.setObjectName("mainFrame")
        self.loginFrame = QtWidgets.QFrame(self.mainFrame)
        self.loginFrame.setGeometry(QtCore.QRect(5, 15, 300, 131))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginFrame.sizePolicy().hasHeightForWidth())
        self.loginFrame.setSizePolicy(sizePolicy)
        self.loginFrame.setMinimumSize(QtCore.QSize(300, 0))
        self.loginFrame.setLocale(QtCore.QLocale(QtCore.QLocale.Turkish, QtCore.QLocale.Turkey))
        self.loginFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loginFrame.setObjectName("loginFrame")
        self.layoutWidget = QtWidgets.QWidget(self.loginFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 281, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
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
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
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
        self.btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/img/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn.setIcon(icon1)
        self.btn.setIconSize(QtCore.QSize(45, 40))
        self.btn.setObjectName("btn")
        self.horizontalLayout.addWidget(self.btn)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.sonuc = QtWidgets.QLabel(self.mainFrame)
        self.sonuc.setEnabled(True)
        self.sonuc.setGeometry(QtCore.QRect(0, 155, 310, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.sonuc.setFont(font)
        self.sonuc.setAlignment(QtCore.Qt.AlignCenter)
        self.sonuc.setObjectName("sonuc")
        Giris.setCentralWidget(self.centralWidget)

        self.btn.clicked.connect(self.girisYap)


        self.retranslateUi(Giris)
        QtCore.QMetaObject.connectSlotsByName(Giris)

    def retranslateUi(self, Giris):
        _translate = QtCore.QCoreApplication.translate
        Giris.setWindowTitle(_translate("Giris", "Şifreyi Giriniz"))
        self.label.setText(_translate("Giris", "Dosya Şifreli Lütfen Şifreyi Giriniz"))
        self.sifre.setPlaceholderText(_translate("Giris", "Şifreniz..."))
        self.sonuc.setText(_translate("Giris", "Sonuç"))

    def girisYap(self):
            if(self.sifre.text()==psw):
                    subprocess.check_call(['xdg-open', path])
                    time.sleep(0.1)
                    quit()
            else:
                    self.sonuc.setText("Sonuc Yanlış")

class MyMainWindow(QtWidgets.QMainWindow, Ui_Giris):
        def __init__(self):
            super(MyMainWindow, self).__init__()
            self.setupUi(self)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = MyMainWindow()
    ui.show()
    sys.exit(app.exec_())

