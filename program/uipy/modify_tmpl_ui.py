# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/modify_tmpl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyTmplForm(object):
    def setupUi(self, ModifyTmplForm):
        ModifyTmplForm.setObjectName("ModifyTmplForm")
        ModifyTmplForm.resize(453, 168)
        self.label = QtWidgets.QLabel(ModifyTmplForm)
        self.label.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ModifyTmplForm)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ModifyTmplForm)
        self.label_3.setGeometry(QtCore.QRect(10, 100, 61, 16))
        self.label_3.setObjectName("label_3")
        self.bTnModify = QtWidgets.QPushButton(ModifyTmplForm)
        self.bTnModify.setGeometry(QtCore.QRect(180, 130, 75, 23))
        self.bTnModify.setObjectName("bTnModify")
        self.lEtTmplName = QtWidgets.QLineEdit(ModifyTmplForm)
        self.lEtTmplName.setGeometry(QtCore.QRect(80, 40, 281, 20))
        self.lEtTmplName.setObjectName("lEtTmplName")
        self.cBbxLang = QtWidgets.QComboBox(ModifyTmplForm)
        self.cBbxLang.setGeometry(QtCore.QRect(80, 70, 111, 22))
        self.cBbxLang.setObjectName("cBbxLang")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.cBbxLang.addItem("")
        self.lEtPublishDir = QtWidgets.QLineEdit(ModifyTmplForm)
        self.lEtPublishDir.setGeometry(QtCore.QRect(80, 100, 281, 20))
        self.lEtPublishDir.setReadOnly(False)
        self.lEtPublishDir.setObjectName("lEtPublishDir")
        self.bTnPublishDir = QtWidgets.QPushButton(ModifyTmplForm)
        self.bTnPublishDir.setGeometry(QtCore.QRect(370, 100, 75, 23))
        self.bTnPublishDir.setObjectName("bTnPublishDir")
        self.rBtnClient = QtWidgets.QRadioButton(ModifyTmplForm)
        self.rBtnClient.setGeometry(QtCore.QRect(250, 10, 89, 16))
        self.rBtnClient.setObjectName("rBtnClient")
        self.label_4 = QtWidgets.QLabel(ModifyTmplForm)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label_4.setObjectName("label_4")
        self.rBtnServer = QtWidgets.QRadioButton(ModifyTmplForm)
        self.rBtnServer.setGeometry(QtCore.QRect(80, 10, 89, 16))
        self.rBtnServer.setObjectName("rBtnServer")

        self.retranslateUi(ModifyTmplForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyTmplForm)

    def retranslateUi(self, ModifyTmplForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyTmplForm.setWindowTitle(_translate("ModifyTmplForm", "修改模板"))
        self.label.setText(_translate("ModifyTmplForm", "模板名称："))
        self.label_2.setText(_translate("ModifyTmplForm", "模板语言："))
        self.label_3.setText(_translate("ModifyTmplForm", "发布目录："))
        self.bTnModify.setText(_translate("ModifyTmplForm", "修改"))
        self.cBbxLang.setItemText(0, _translate("ModifyTmplForm", "cpp"))
        self.cBbxLang.setItemText(1, _translate("ModifyTmplForm", "lua"))
        self.cBbxLang.setItemText(2, _translate("ModifyTmplForm", "golang"))
        self.cBbxLang.setItemText(3, _translate("ModifyTmplForm", "csharp"))
        self.cBbxLang.setItemText(4, _translate("ModifyTmplForm", "python"))
        self.bTnPublishDir.setText(_translate("ModifyTmplForm", "选择"))
        self.rBtnClient.setText(_translate("ModifyTmplForm", "客户端"))
        self.label_4.setText(_translate("ModifyTmplForm", "模板类型："))
        self.rBtnServer.setText(_translate("ModifyTmplForm", "服务器"))

