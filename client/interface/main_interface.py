from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from time import sleep
from PyQt5.QtGui import QIcon, QColor, QPainter
from interface import Ui_MainWindow
from lobby import Ui_Form

class Form(QtWidgets.QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.add_1)
        self.lobby = Form()
        self.pix = QtGui.QPixmap()  # создать экземпляр объекта QPixmap
        self.lastPoint = QtCore.QPoint()  # начальная точка
        self.endPoint = QtCore.QPoint()  # конечная точка
        self.init_UI()


    def init_UI(self):
        self.ui.lineEdit.setPlaceholderText("Your name")
        # Размер окна установлен 600 * 500
        self.resize(1440, 900)
        # Размер холста 400 * 400, фон белый
        self.pix = QtGui.QPixmap(1440, 900)
        self.pix.fill(QtCore.Qt.red)

    def paintEvent(self, event):
        pp = QPainter(self.pix)
        # Нарисуйте прямую линию в соответствии с двумя положениями до и после указателя мыши
        pp.drawLine(self.lastPoint, self.endPoint)
        # Сделать предыдущее значение координаты равным следующему значению координаты,
        # Таким образом можно нарисовать непрерывную линию
        self.lastPoint = self.endPoint
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix)  # Рисуем на холсте


    # Мышь пресс-мероприятие
    def mousePressEvent(self, event):
        # Нажмите левую кнопку мыши
        if event.button() == QtCore.Qt.LeftButton:
            self.lastPoint = event.pos()
            self.endPoint = self.lastPoint


    # Событие движения мыши
    def mouseMoveEvent(self, event):
        # Перемещайте мышь, удерживая нажатой левую кнопку мыши
        if event.buttons() and QtCore.Qt.LeftButton:
            self.endPoint = event.pos()
            # Сделать перекраску
            self.update()


    # Событие отпускания мыши
    def mouseReleaseEvent(self, event):
        # Отпустить левую кнопку мыши
        if event.button() == QtCore.Qt.LeftButton:
            self.endPoint = event.pos()
            # Сделать перекраску
            self.update()

    def add_1(self):
        self.lobby.showFullScreen()
        self.close()


    def print_name(self):
        name = self.ui.lineEdit.text()
        print(name)








if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application_1 = MainWindow()
    application_1.showFullScreen()

    sys.exit(app.exec())
