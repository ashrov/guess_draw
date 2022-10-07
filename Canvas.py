# import threading
# import socket
# import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QSlider
from PyQt5.QtCore import Qt

# CoLoRs = ['#141414', '#67615f', '#f0eeec', '#611732', '#ae2633', '#e86c18', '#f1bb3b', '#844239',
#           '#c47540', '#efb681', '#d4705c', '#206348', '#42ad37', '#b4e357', '#1a363f', '#20646c',
#           '#2bad96', '#a1e4a0', '#222664', '#264fa4', '#1f95e1', '#6de0e5', '#431c58', '#8d2f7c',
#           '#e4669b', '#f0b4ad']

CoLoRs = ['#000000', '#0e0e37', '#163854', '#137878', '#1ec663', '#9cff6a', '#fff678', '#ee7521',
          '#b62b38', '#670d3d', '#2a0426', '#501223', '#923737', '#ce8464', '#ffd7b0', '#ffffff',
          '#55fff1', '#2796db', '#243dab', '#1b1b5c', '#17072b', '#400b67', '#891393', '#da4fbc',
          '#ffaacf', '#b2cfcd', '#71888f', '#383e51']


class Canvas(QtWidgets.QLabel):
    def __init__(self, client):
        super().__init__()
        self.str1 = '0'
        pixmap = QtGui.QPixmap(750, 500)  # создание холста
        self.setPixmap(pixmap)
        self.last_x, self.last_y = None, None  # координаты дургого конца линии

        self.client = client

        self.pen_width = 4
        self.pen_color = '#000000'

    def set_pen_color(self, color):
        self.pen_color = color
        print('color set: ', color)

    def mouseMoveEvent(self, e):
        if self.last_x is None:
            self.last_x = e.x()
            self.last_y = e.y()

            return
        self.draw_point(self.last_x, self.last_y, e.x(), e.y(), self.pen_color, self.pen_width)
        self.str1 = str(self.last_x) + ' ' + str(self.last_y) + ' ' + str(e.x()) + ' ' + str(e.y()) + ' ' + str(
            self.pen_color) + ' ' + str(self.pen_width)

        self.client.send_message_to_server(self.str1)

        self.last_x = e.x()
        self.last_y = e.y()

    def draw_point(self, x1, y1, x2, y2, color=None, width=None):
        if not color:
            color = QtGui.QColor(self.pen_color)
        else:
            color = QtGui.QColor(color)
        if not width:
            width = self.pen_width

        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setWidth(width)
        p.setColor(color)
        painter.setPen(p)  # создание пера
        painter.drawLine(x1, y1, x2, y2)
        painter.end()
        self.update()

    def mouseReleaseEvent(self, e):
        self.last_x = None
        self.last_y = None


class ColorButton(QtWidgets.QPushButton):
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(25, 25))
        self.color = color
        self.setStyleSheet("background-color: %s;" % color)


class Paint(QMainWindow):
    def __init__(self, canv, client):
        super().__init__()
        self.canvas = canv(client)
        client.set_window(self)

        grid = QGridLayout()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(grid)
        l.addWidget(self.canvas)
        grid.addLayout(l, 1, 1)

        palette = QtWidgets.QHBoxLayout()

        self.make_pal(palette)
        l.addLayout(palette)

        sld = QSlider(Qt.Orientation.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)

        sld.setRange(1, 100)
        sld.valueChanged[int].connect(self.change_val)

        grid.addWidget(sld, 2, 1)
        self.setCentralWidget(w)

    def change_val(self, value):
        self.canvas.pen_width = value

    def make_pal(self, layout):
        for c in CoLoRs:
            b = ColorButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)

    def draw_point_on_canvas(self, x1, y1, x2, y2, color=None, width=None):
        self.canvas.draw_point(x1, y1, x2, y2, color, width)
