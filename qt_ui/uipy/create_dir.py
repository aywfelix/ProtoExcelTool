# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_dir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateDirForm(object):
    def setupUi(self, CreateDirForm):
        CreateDirForm.setObjectName("CreateDirForm")
        CreateDirForm.setWindowModality(QtCore.Qt.ApplicationModal)
        CreateDirForm.resize(352, 260)
        CreateDirForm.setAutoFillBackground(True)
        self.label = QtWidgets.QLabel(CreateDirForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.lEtProtoDirName = QtWidgets.QLineEdit(CreateDirForm)
        self.lEtProtoDirName.setGeometry(QtCore.QRect(90, 20, 241, 20))
        self.lEtProtoDirName.setObjectName("lEtProtoDirName")
        self.bTnCreateDir = QtWidgets.QPushButton(CreateDirForm)
        self.bTnCreateDir.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.bTnCreateDir.setObjectName("bTnCreateDir")
        self.tEtImport = QtWidgets.QTextEdit(CreateDirForm)
        self.tEtImport.setGeometry(QtCore.QRect(20, 80, 311, 141))
        self.tEtImport.setReadOnly(False)
        self.tEtImport.setObjectName("tEtImport")
        self.bTnClearImport = QtWidgets.QPushButton(CreateDirForm)
        self.bTnClearImport.setGeometry(QtCore.QRect(250, 50, 81, 23))
        self.bTnClearImport.setObjectName("bTnClearImport")
        self.label_2 = QtWidgets.QLabel(CreateDirForm)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(CreateDirForm)
        QtCore.QMetaObject.connectSlotsByName(CreateDirForm)

    def retranslateUi(self, CreateDirForm):
        _translate = QtCore.QCoreApplication.translate
        CreateDirForm.setWindowTitle(_translate("CreateDirForm", "创建目录"))
        self.label.setText(_translate("CreateDirForm", "目录名称："))
        self.bTnCreateDir.setText(_translate("CreateDirForm", "创建"))
        self.tEtImport.setHtml(_translate("CreateDirForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">import &quot;game.common&quot;;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">package user;</p></body></html>"))
        self.bTnClearImport.setText(_translate("CreateDirForm", "清除文本"))
        self.label_2.setText(_translate("CreateDirForm", "填写引入包及包名："))

