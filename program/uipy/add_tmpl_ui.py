# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/add_tmpl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddTmplForm(object):
    def setupUi(self, AddTmplForm):
        AddTmplForm.setObjectName("AddTmplForm")
        AddTmplForm.resize(453, 167)
        self.label = QtWidgets.QLabel(AddTmplForm)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddTmplForm)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddTmplForm)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_3.setObjectName("label_3")
        self.bTnOk = QtWidgets.QPushButton(AddTmplForm)
        self.bTnOk.setGeometry(QtCore.QRect(170, 130, 75, 23))
        self.bTnOk.setObjectName("bTnOk")
        self.lEtTmplName = QtWidgets.QLineEdit(AddTmplForm)
        self.lEtTmplName.setGeometry(QtCore.QRect(80, 40, 281, 20))
        self.lEtTmplName.setObjectName("lEtTmplName")
        self.cBbxLang = QtWidgets.QComboBox(AddTmplForm)
        self.cBbxLang.setGeometry(QtCore.QRect(80, 70, 111, 22))
        self.cBbxLang.setObjectName("cBbxLang")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.lEtPublishDir = QtWidgets.QLineEdit(AddTmplForm)
        self.lEtPublishDir.setGeometry(QtCore.QRect(80, 100, 281, 21))
        self.lEtPublishDir.setReadOnly(False)
        self.lEtPublishDir.setObjectName("lEtPublishDir")
        self.bTnPublishDir = QtWidgets.QPushButton(AddTmplForm)
        self.bTnPublishDir.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.bTnPublishDir.setObjectName("bTnPublishDir")
        self.rBtnServer = QtWidgets.QRadioButton(AddTmplForm)
        self.rBtnServer.setGeometry(QtCore.QRect(80, 10, 89, 16))
        self.rBtnServer.setObjectName("rBtnServer")
        self.rBtnClient = QtWidgets.QRadioButton(AddTmplForm)
        self.rBtnClient.setGeometry(QtCore.QRect(250, 10, 89, 16))
        self.rBtnClient.setObjectName("rBtnClient")
        self.label_4 = QtWidgets.QLabel(AddTmplForm)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AddTmplForm)
        QtCore.QMetaObject.connectSlotsByName(AddTmplForm)

    def retranslateUi(self, AddTmplForm):
        _translate = QtCore.QCoreApplication.translate
        AddTmplForm.setWindowTitle(_translate("AddTmplForm", "添加模板"))
        self.label.setText(_translate("AddTmplForm", "模板名称："))
        self.label_2.setText(_translate("AddTmplForm", "模板语言："))
        self.label_3.setText(_translate("AddTmplForm", "发布目录："))
        self.bTnOk.setText(_translate("AddTmplForm", "确定"))
        self.cBbxLang.setItemText(0, _translate("AddTmplForm", "cpp"))
        self.cBbxLang.setItemText(1, _translate("AddTmplForm", "lua"))
        self.cBbxLang.setItemText(2, _translate("AddTmplForm", "golang"))
        self.cBbxLang.setItemText(3, _translate("AddTmplForm", "csharp"))
        self.cBbxLang.setItemText(4, _translate("AddTmplForm", "python"))
        self.bTnPublishDir.setText(_translate("AddTmplForm", "选择"))
        self.rBtnServer.setText(_translate("AddTmplForm", "服务器"))
        self.rBtnClient.setText(_translate("AddTmplForm", "客户端"))
        self.label_4.setText(_translate("AddTmplForm", "模板类型："))

