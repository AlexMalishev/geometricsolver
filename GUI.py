#!/usr/bin/python3

import sys,my,time,math
from PyQt5.QtGui import (QFont, QIcon, QPaintDevice,QPen,QBrush, QColor, QPainter)
from PyQt5.QtCore import (QEvent,QLine, QPoint, QRectF, Qt,pyqtSignal)
from PyQt5.QtWidgets import (QApplication,QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)

class MyWin(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.ui = my.Ui_MainWindow()
        self.ui.setupUi(self)
        #self.ui.MainWindow.setFixedWidth(self.ui.geometry.width)
        self.setWindowIcon(QIcon('./pict/icone.png'))
        self.setWindowFlags(Qt.Window | Qt.MSWindowsFixedSizeDialogHint)

        self.ui.graph.setDisabled(True)

        self.ui.pushButton.clicked.connect(self.createP)
        self.ui.pushButton_2.clicked.connect(self.createI)



        self.scene=QGraphicsScene()
        self.ui.graph.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.ui.graph.width(),self.ui.graph.height())

        self.ui.graph.installEventFilter(self)
        self.grid(13)
        self.PointFlag=0
        self.points=list()
        self.lines=list()
        self.InteFlag=0
        self.Linepenpen=QPen(QColor('#000000'),2)
        self.pointpen = QPen(QColor('#ff0000'), 2)
        self.Linepenpen.style="DashLine"
        self.Linepenpen.cap="RoundCap"
    def eventFilter(self, source, event):

        if (event.type() == QEvent.MouseButtonPress and
                    source is self.ui.graph):
            if self.PointFlag==1:
                pos = event.pos()
                print('add point: (%d, %d)' % (pos.x(), pos.y()))
                self.points.append(QPoint(pos))
                self.PointFlag=0
                self.scene.addEllipse(pos.x()-2.5,pos.y()-2.5,5,5,self.pointpen)
                self.scene.update()
            if self.InteFlag>0:
                if self.InteFlag==2:

                    lin=QLine()
                    if self.getpoint(event.pos())!=None:
                        lin.setP1(self.getpoint(event.pos()))
                        self.lines.append(lin)
                    else:
                        self.InteFlag+=1
                else:
                    if self.getpoint(event.pos()) != None:
                        self.lines[-1].setP2(self.getpoint(event.pos()))
                        print('add line()',self.lines[-1].x1(),self.lines[-1].y1(),self.lines[-1].x2(),self.lines[-1].y2())
                        self.scene.addLine(self.lines[-1].x1(),self.lines[-1].y1(),self.lines[-1].x2(),self.lines[-1].y2(),self.Linepenpen)
                        self.scene.update()
                    else:
                        self.InteFlag+=1
                self.InteFlag-=1
        return QWidget.eventFilter(self, source, event)
    def getpoint(self,a):
        x=a.x()
        y=a.y()
        tolerance=15
        for point in self.points:
            if abs(point.x()-x)<tolerance and abs(point.y()-y)<tolerance:
                return point
        return None
    def grid(self,dxy):
        pen=QPen()
        pen.setColor(QColor('#C0C0C0'))
        for i in range(0,int( self.ui.graph.height()/dxy)+1):
            self.scene.addLine(0,dxy*i,self.ui.graph.width(),dxy*i,pen)
        for i in range(0, int( self.ui.graph.width()/dxy)+1):
            self.scene.addLine( dxy*i,0, dxy*i, self.ui.graph.height(),pen)


    def createP(self):
        self.PointFlag=1

    def createI(self):
        self.InteFlag=2

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window=MyWin()
    window.show()
    sys.exit(app.exec())