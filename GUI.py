#!/usr/bin/python3

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import (QFont, QIcon, QPaintDevice,QPen)
from PyQt5.QtWidgets import (QApplication, QMainWindow)
from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)

class Test(QMainWindow):
    def __init__(self):
        super(Test, self).__init__()

#        self.ui = uic.loadUi("test-ok.ui", self)
        self.ui = uic.loadUi("myform.ui", self)
        self.setWindowIcon(QIcon('./pict/icone.png'))
        self.ui.pushButton_3.setIcon(QIcon('./pict/horiz.png'))
        self.ui.pushButton_4.setIcon(QIcon('./pict/para.png'))
        self.ui.pushButton_5.setIcon(QIcon('./pict/orto.png'))
        self.ui.pushButton_6.setIcon(QIcon('./pict/vert.png'))
        self.ui.pushButton_7.setIcon(QIcon('./pict/pl.png'))
        self.ui.pushButton_8.setIcon(QIcon('./pict/pp.png'))
        self.ui.pushButton_9.setIcon(QIcon('./pict/angle.png'))
        self.ui.pushButton_10.setIcon(QIcon('./pict/lenght.png'))

    def grid(self):
        pen=QPen()
        pen.setColor(QColor('#C0C0C0'))

        scene= QGraphicsScene()
        self.ui.graph.setScene(scene)
        scene.setSceneRect(0,0,500,400)
        for i in range(0,40):
            scene.addLine(0,10*i,500,10*i,pen)
        for i in range(0, 50):
            scene.addLine( 10*i,0, 10*i, 400,pen)
            #scene.addLine( 10 * i,-250,  10 * i,250)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = Test()
    t.grid()
    t.show()
    sys.exit(app.exec())