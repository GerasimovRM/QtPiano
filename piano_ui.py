# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'piano_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(418, 160)
        Form.setMaximumSize(QtCore.QSize(418, 160))
        self.C = QtWidgets.QPushButton(Form)
        self.C.setGeometry(QtCore.QRect(0, 0, 61, 161))
        self.C.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.C.setText("")
        self.C.setObjectName("C")
        self.D = QtWidgets.QPushButton(Form)
        self.D.setGeometry(QtCore.QRect(60, 0, 61, 161))
        self.D.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.D.setText("")
        self.D.setObjectName("D")
        self.E = QtWidgets.QPushButton(Form)
        self.E.setGeometry(QtCore.QRect(120, 0, 61, 161))
        self.E.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.E.setText("")
        self.E.setObjectName("E")
        self.F = QtWidgets.QPushButton(Form)
        self.F.setGeometry(QtCore.QRect(180, 0, 61, 161))
        self.F.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.F.setText("")
        self.F.setObjectName("F")
        self.G = QtWidgets.QPushButton(Form)
        self.G.setGeometry(QtCore.QRect(240, 0, 61, 161))
        self.G.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.G.setText("")
        self.G.setObjectName("G")
        self.A = QtWidgets.QPushButton(Form)
        self.A.setGeometry(QtCore.QRect(300, 0, 61, 161))
        self.A.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.A.setAutoFillBackground(False)
        self.A.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.A.setText("")
        self.A.setObjectName("A")
        self.C_sharp = QtWidgets.QPushButton(Form)
        self.C_sharp.setGeometry(QtCore.QRect(40, 0, 41, 91))
        self.C_sharp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.C_sharp.setObjectName("C_sharp")
        self.F_sharp = QtWidgets.QPushButton(Form)
        self.F_sharp.setGeometry(QtCore.QRect(220, 0, 41, 91))
        self.F_sharp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.F_sharp.setObjectName("F_sharp")
        self.G_sharp = QtWidgets.QPushButton(Form)
        self.G_sharp.setGeometry(QtCore.QRect(280, 0, 41, 91))
        self.G_sharp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.G_sharp.setObjectName("G_sharp")
        self.D_sharp = QtWidgets.QPushButton(Form)
        self.D_sharp.setGeometry(QtCore.QRect(100, 0, 41, 91))
        self.D_sharp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.D_sharp.setObjectName("D_sharp")
        self.B = QtWidgets.QPushButton(Form)
        self.B.setGeometry(QtCore.QRect(360, 0, 61, 161))
        self.B.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.B.setAutoFillBackground(False)
        self.B.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.B.setText("")
        self.B.setObjectName("B")
        self.A_sharp = QtWidgets.QPushButton(Form)
        self.A_sharp.setGeometry(QtCore.QRect(340, 0, 41, 91))
        self.A_sharp.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.A_sharp.setObjectName("A_sharp")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Пианино"))
        self.C_sharp.setText(_translate("Form", "D#"))
        self.F_sharp.setText(_translate("Form", "F#"))
        self.G_sharp.setText(_translate("Form", "G#"))
        self.D_sharp.setText(_translate("Form", "D#"))
        self.A_sharp.setText(_translate("Form", "G#"))
