# -*- coding: utf-8 -*-
'/Users/sliwmen/Downloads/main_window-2.png'
# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/sliwmen/Downloads/main_window-2.png"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(540, 280, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Chalkboard SE")
        font.setPointSize(36)
        self.lineEdit.setFont(font)
        self.lineEdit.setMouseTracking(True)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setStyleSheet("border: 3px solid #000000;\n"
"border-radius: 30;\n"
"background-color: #ffffff;\n"
"color: black;\n"
"\n"
"\n"
"")
        self.lineEdit.setFrame(True)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(620, 610, 251, 60))
        font = QtGui.QFont()
        font.setFamily("Chalkboard SE")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setStyleSheet("QPushButton { \n"
"    border: 3px solid #000000;\n"
"    border-radius: 30;\n"
"    background-color: #ffffff;\n"
"    color: black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color: #d7d7d7;\n"
"}")
        self.pushButton.setIconSize(QtCore.QSize(20, 20))
        self.pushButton.setCheckable(False)
        self.pushButton.setChecked(False)
        self.pushButton.setAutoRepeat(False)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoRepeatDelay(400)
        self.pushButton.setAutoRepeatInterval(230)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Let\'s play!"))
        self.pushButton.setProperty("Alignment", _translate("MainWindow", "asdasd"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
