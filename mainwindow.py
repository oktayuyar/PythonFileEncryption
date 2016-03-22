#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets

#import QtLocation 5.3

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(706, 431)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralWidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(680, 0, 20, 381))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(20, -20, 661, 401))
        self.listView.setObjectName("listView")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 10, 85, 26))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 60, 85, 26))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 110, 85, 26))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 160, 85, 26))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 210, 85, 26))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 471, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(50, 100, 471, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(50, 150, 471, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(50, 200, 471, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(50, 50, 471, 31))
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 706, 25))
        self.menuBar.setObjectName("menuBar")
        self.menuOktay = QtWidgets.QMenu(self.menuBar)
        self.menuOktay.setObjectName("menuOktay")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menuBar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuOktay.addAction("a")
        self.menuOktay.addAction("b")
        self.menuOktay.addAction("c")
        self.menuEdit.addSeparator()
        self.menuEdit.addSeparator()
        self.menuEdit.addSeparator()
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menuView.addSeparator()
        self.menuBar.addAction(self.menuOktay.menuAction())
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "oktayuyarr"))
        self.pushButton.setText(_translate("MainWindow", "Şifreyi Kaldır "))
        self.pushButton_2.setText(_translate("MainWindow", "Şifreyi Kaldır "))
        self.pushButton_3.setText(_translate("MainWindow", "Şifreyi Kaldır "))
        self.pushButton_4.setText(_translate("MainWindow", "Şifreyi Kaldır "))
        self.pushButton_5.setText(_translate("MainWindow", "Şifreyi Kaldır "))
        self.label.setText(_translate("MainWindow", "/home/oktay/PycharmProjects                                    Şifre: 1903"))
        self.label_2.setText(_translate("MainWindow", "/home/oktay/PycharmProjects                                    Şifre: 1903"))
        self.label_3.setText(_translate("MainWindow", "/home/oktay/PycharmProjects                                    Şifre: 1903"))
        self.label_4.setText(_translate("MainWindow", "/home/oktay/PycharmProjects                                    Şifre: 1903"))
        self.label_5.setText(_translate("MainWindow", "/home/oktay/PycharmProjects                                    Şifre: 1903"))
        self.menuOktay.setTitle(_translate("MainWindow", "Dosya"))
        self.menuEdit.setTitle(_translate("MainWindow", "Düzenle"))
        self.menuView.setTitle(_translate("MainWindow", "Görünüm"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
