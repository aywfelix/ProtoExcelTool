# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\达瓦未来\ProtocolAndExcelTool\qt_ui\ui\create_proto_dir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateDirForm(object):
    def setupUi(self, CreateDirForm):
        CreateDirForm.setObjectName("CreateDirForm")
        CreateDirForm.resize(349, 76)
        self.label = QtWidgets.QLabel(CreateDirForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.lEtProtoDirName = QtWidgets.QLineEdit(CreateDirForm)
        self.lEtProtoDirName.setGeometry(QtCore.QRect(90, 20, 241, 20))
        self.lEtProtoDirName.setObjectName("lEtProtoDirName")
        self.bTnCreateDir = QtWidgets.QPushButton(CreateDirForm)
        self.bTnCreateDir.setGeometry(QtCore.QRect(140, 50, 75, 23))
        self.bTnCreateDir.setObjectName("bTnCreateDir")

        self.retranslateUi(CreateDirForm)
        QtCore.QMetaObject.connectSlotsByName(CreateDirForm)

    def retranslateUi(self, CreateDirForm):
        _translate = QtCore.QCoreApplication.translate
        CreateDirForm.setWindowTitle(_translate("CreateDirForm", "创建目录"))
        self.label.setText(_translate("CreateDirForm", "目录名称："))
        self.bTnCreateDir.setText(_translate("CreateDirForm", "创建"))

