#!/usr/bin/python3

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import (QFont, QIcon, QPaintDevice)
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
        self.ui.pushButton_4.setIcon(QIcon('icone.png'))




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    t = Test()
    t.show()
    sys.exit(app.exec())