#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QApplication)
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.col = QColor(0, 0, 0)

        intb = QPushButton('INTERVAL', self)
        intb.setCheckable(True)
        intb.move(10, 10)

        intb.clicked[bool].connect(self.setColor)

        pointb = QPushButton('POINT', self)
        pointb.setCheckable(True)
        pointb.move(10, 60)

        pointb.clicked[bool].connect(self.setColor)

        lineb = QPushButton('LINE', self)
        lineb.setCheckable(True)
        lineb.move(10, 110)

        lineb.clicked[bool].connect(self.setColor)



        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 900,550)
        self.square.setStyleSheet("QWidget { background-color: %s }" %
                                  self.col.name())

        self.setGeometry(30, 30, 1100, 600)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame { background-color: %s }" %
                                  self.col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())