# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/modify_dir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyDirForm(object):
    def setupUi(self, ModifyDirForm):
        ModifyDirForm.setObjectName("ModifyDirForm")
        ModifyDirForm.resize(352, 258)
        self.bTnModifyDir = QtWidgets.QPushButton(ModifyDirForm)
        self.bTnModifyDir.setGeometry(QtCore.QRect(140, 230, 75, 23))
        self.bTnModifyDir.setObjectName("bTnModifyDir")
        self.label = QtWidgets.QLabel(ModifyDirForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.lEtProtoDirName = QtWidgets.QLineEdit(ModifyDirForm)
        self.lEtProtoDirName.setGeometry(QtCore.QRect(90, 20, 241, 20))
        self.lEtProtoDirName.setObjectName("lEtProtoDirName")
        self.tEtImport = QtWidgets.QTextEdit(ModifyDirForm)
        self.tEtImport.setGeometry(QtCore.QRect(20, 80, 311, 141))
        self.tEtImport.setReadOnly(False)
        self.tEtImport.setObjectName("tEtImport")
        self.bTnClearImport = QtWidgets.QPushButton(ModifyDirForm)
        self.bTnClearImport.setGeometry(QtCore.QRect(250, 50, 81, 23))
        self.bTnClearImport.setObjectName("bTnClearImport")
        self.label_2 = QtWidgets.QLabel(ModifyDirForm)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 211, 16))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(ModifyDirForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyDirForm)

    def retranslateUi(self, ModifyDirForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyDirForm.setWindowTitle(_translate("ModifyDirForm", "修改目录"))
        self.bTnModifyDir.setText(_translate("ModifyDirForm", "修改"))
        self.label.setText(_translate("ModifyDirForm", "目录名称："))
        self.tEtImport.setHtml(_translate("ModifyDirForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">import &quot;game.common&quot;;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">package user;</p></body></html>"))
        self.bTnClearImport.setText(_translate("ModifyDirForm", "清除文本"))
        self.label_2.setText(_translate("ModifyDirForm", "填写引入包及包名："))

