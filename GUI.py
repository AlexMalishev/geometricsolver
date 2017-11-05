#!/usr/bin/python3

import sys,my,time,math
from PyQt5.QtGui import (QFont, QIcon, QPaintDevice,QPen,QBrush, QColor, QPainter,QPalette)
from PyQt5.QtCore import (QEvent,QLine, QPoint, QRectF, Qt,pyqtSignal)
from PyQt5.QtWidgets import (QApplication,QWidget, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
class Point:
    def __init__(self,x=0,y=0):
        self.X=x
        self.Y=y
    def getX(self):
        return self.X
    def getY(self):
        return self.Y
    def setX(self,x):
        self.X=x
    def setY(self,y):
        self.Y=y

class Line(Point):

    def __init__(self):
        self.P1=None
        self.P2=None
    def setP1(self,P1):
        self.P1=P1
    def setP2(self,P2):
        self.P2=P2
    def x1(self):
        return self.P1.getX()
    def y1(self):
        return self.P1.getY()
    def x2(self):
        return self.P2.getX()
    def y2(self):
        return self.P2.getY()
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

        self.ui.pushButtonDel.clicked.connect(self.delP)
        self.ui.pushButtonDel_2.clicked.connect(self.delI)


        self.ui.pushButton_9.clicked.connect(self.angle)
        self.ui.pushButton_10.clicked.connect(self.lenght)

        self.scene=QGraphicsScene()
        self.ui.graph.setScene(self.scene)
        self.scene.setSceneRect(0, 0, self.ui.graph.width(),self.ui.graph.height())

        self.ui.graph.installEventFilter(self)
        self.grid(13)
        self.PointFlag=0
        self.points=list()
        self.lines=list()
        self.InteFlag=0
        self.delIflag=0
        self.delPflag=0
        self.Linepenpen=QPen(QColor('#000000'),2)
        self.pointpen = QPen(QColor('#ff0000'), 2)
        self.Linepenpen.style="DashLine"
        self.Linepenpen.cap="RoundCap"

    def angle(self):
        self.createmodal('Угол')
    def lenght(self):
        self.createmodal('Длина')

    def createmodal(self,t):
        modalWindow=QWidget(window,Qt.Window)
        modalWindow.setWindowTitle(t)
        modalWindow.resize(250,40)
        modalWindow.setWindowModality(Qt.WindowModal)
        modalWindow.setAttribute(Qt.WA_DeleteOnClose,True)
        modalWindow.move(window.geometry().center() - modalWindow.rect().center() -QPoint(4,30))
        modLab=QLabel(t)
        modBut=QPushButton('Применить')
        lineEdit=QLineEdit()
        hBox=QHBoxLayout()
        hBox.addWidget(modLab)
        hBox.addWidget(lineEdit)
        hBox.addWidget(modBut)
        modalWindow.setLayout(hBox)
        modBut.clicked.connect(modalWindow.close)
        modalWindow.show()



    def eventFilter(self, source, event):

        if (event.type() == QEvent.MouseButtonPress and
                    source is self.ui.graph):
            if self.PointFlag==1:

                pos = event.pos()
                print('add point: (%d, %d)' % (pos.x(), pos.y()))
                self.points.append(Point(pos.x(),pos.y()))
                self.PointFlag=0
                self.painter()


            if self.delPflag==1:
                pos = event.pos()
                poi=self.getpoint(event.pos())
                if poi != None:
                    allline=list()
                    for line in self.lines:
                        if line.P1==poi or line.P2==poi:
                            allline.append(line)
                    for line in allline:
                        self.lines.remove(line)
                    self.points.remove(poi)
                    self.delPflag=0
                    self.painter()


            if self.delIflag==1:
                pos = event.pos()
                lin = self.getline(event.pos())
                if lin != None:
                    self.lines.remove(lin)

                    self.delIflag=0
                    self.painter()
            if self.InteFlag>0:
                if self.InteFlag==2:

                    lin=Line()
                    if self.getpoint(event.pos())!=None:

                        lin.setP1(self.getpoint(event.pos()))
                        self.lines.append(lin)
                    else:
                        self.InteFlag+=1
                else:
                    if self.getpoint(event.pos()) != None:
                        self.lines[-1].setP2(self.getpoint(event.pos()))
                        print('add line()',self.lines[-1].x1(),self.lines[-1].y1(),self.lines[-1].x2(),self.lines[-1].y2())
                        self.painter()
                    else:
                        self.InteFlag+=1
                self.InteFlag-=1

        return QWidget.eventFilter(self, source, event)


    def painter(self):
        self.scene.clear()
        self.grid(13)
        for point in self.points:
            self.scene.addEllipse(point.X - 2.5, point.Y - 2.5, 5, 5, self.pointpen)
        for line in self.lines:
            self.scene.addLine(line.x1(), line.y1(), line.x2(), line.y2(),self.Linepenpen)
        self.scene.update()


    def getpoint(self,a):
        x=a.x()
        y=a.y()
        tolerance=10
        for point in self.points:
            if abs(point.getX()-x)<tolerance and abs(point.getY()-y)<tolerance:
                return point
        return None

    def getline(self,a):
        x = a.x()
        y = a.y()
        tolerance = 5
        for line in self.lines:
            t=abs(y-(line.y1()+((line.y2()-line.y1())*(x-line.x1())/(line.x2()-line.x1()))))
            print(t)
            if t<tolerance:
                return line
        return None


    def grid(self,dxy):
        pen=QPen()
        pen.setColor(QColor('#C0C0C0'))
        for i in range(0,int( self.ui.graph.height()/dxy)+1):
            self.scene.addLine(0,dxy*i,self.ui.graph.width(),dxy*i,pen)
        for i in range(0, int( self.ui.graph.width()/dxy)+1):
            self.scene.addLine( dxy*i,0, dxy*i, self.ui.graph.height(),pen)


    def delP(self):
        self.delPflag=1

        self.delIflag = 0
        self.PointFlag = 0
        self.InteFlag = 0


    def delI(self):
        self.delIflag = 1

        self.delPflag = 0
        self.PointFlag = 0
        self.InteFlag = 0

    def createP(self):
        self.PointFlag=1

        self.delPflag = 0
        self.delIflag = 0
        self.InteFlag = 0

    def createI(self):
        self.InteFlag=2

        self.delPflag = 0
        self.delIflag = 0
        self.PointFlag = 0

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window=MyWin()
    pal = window.palette()
    pal.setColor(QPalette.Normal, QPalette.Window, QColor("#7fffd4"))
    window.setPalette(pal)
    window.show()
    sys.exit(app.exec())