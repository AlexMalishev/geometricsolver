# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon,QPalette,QColor
from PyQt5.QtCore import  Qt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(950, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(165, 30, 770, 580))
        self.graph.setObjectName("graph")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 161, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 50, 141, 101))
        self.groupBox.setObjectName("groupBox")

        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButtonDel_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDel_2.setGeometry(QtCore.QRect(73, 20, 51, 31))
        self.pushButtonDel_2.setObjectName("pushButton_2")

        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 51, 31))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setObjectName("pushButton")

        self.pushButtonDel = QtWidgets.QPushButton(self.groupBox)
        self.pushButtonDel.setGeometry(QtCore.QRect(73, 60, 51, 31))
        self.pushButtonDel.setMouseTracking(False)
        self.pushButtonDel.setObjectName("pushButton")



        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 200, 141, 241))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 80, 41, 41))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 20, 41, 41))
        self.pushButton_4.setText("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 20, 41, 41))
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 80, 41, 41))
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 140, 41, 41))
        self.pushButton_7.setText("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 140, 41, 41))
        self.pushButton_8.setText("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 190, 41, 41))
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_10.setGeometry(QtCore.QRect(80, 190, 41, 41))
        self.pushButton_10.setText("")
        self.pushButton_10.setObjectName("pushButton_10")
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menufh = QtWidgets.QMenu(self.menubar)
        self.menufh.setObjectName("menufh")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.menufh.addSeparator()
        self.menufh.addSeparator()
        self.menufh.addAction(self.action_3)
        self.menufh.addAction(self.action_4)
        self.menufh.addAction(self.action_5)
        self.menubar.addAction(self.menufh.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())


        self.pushButton_3.setIcon(QIcon('./pict/horiz.png'))
        self.pushButton_4.setIcon(QIcon('./pict/para.png'))
        self.pushButton_5.setIcon(QIcon('./pict/orto.png'))
        self.pushButton_6.setIcon(QIcon('./pict/vert.png'))
        self.pushButton_7.setIcon(QIcon('./pict/pl.png'))
        self.pushButton_8.setIcon(QIcon('./pict/pp.png'))
        self.pushButton_9.setIcon(QIcon('./pict/angle.png'))
        self.pushButton_10.setIcon(QIcon('./pict/lenght.png'))
        self.style="""
            QPushButton:hover { background-color: red }
            QPushButton:!hover { background-color: white }

            QPushButton:pressed { background-color: rgb(0, 255, 0); }
        """

        self.pushButton_3.setStyleSheet(self.style)
        self.pushButton_4.setStyleSheet(self.style)
        self.pushButton_5.setStyleSheet(self.style)
        self.pushButton_6.setStyleSheet(self.style)
        self.pushButton_7.setStyleSheet(self.style)
        self.pushButton_8.setStyleSheet(self.style)
        self.pushButton_9.setStyleSheet(self.style)
        self.pushButton_10.setStyleSheet(self.style)


        self.graph.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.graph.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GeoSolve"))
        self.groupBox.setTitle(_translate("MainWindow", "Примитивы"))
        self.pushButton_2.setText(_translate("MainWindow", "Отрезок"))
        self.pushButton.setText(_translate("MainWindow", "Точка"))
        self.pushButtonDel_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButtonDel.setText(_translate("MainWindow", "Удалить"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Ограничения"))
        self.menufh.setTitle(_translate("MainWindow", "Файл"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.action_3.setText(_translate("MainWindow", "Открыть"))
        self.action_4.setText(_translate("MainWindow", "Сохранить"))
        self.action_5.setText(_translate("MainWindow", "Выход"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

