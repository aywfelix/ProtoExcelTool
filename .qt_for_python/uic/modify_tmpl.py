# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\达瓦未来\ProtocolAndExcelTool\qt_ui\ui\modify_tmpl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyTmplForm(object):
    def setupUi(self, ModifyTmplForm):
        ModifyTmplForm.setObjectName("ModifyTmplForm")
        ModifyTmplForm.resize(453, 152)
        self.label = QtWidgets.QLabel(ModifyTmplForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ModifyTmplForm)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(ModifyTmplForm)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_3.setObjectName("label_3")
        self.cBxTmpl = QtWidgets.QCheckBox(ModifyTmplForm)
        self.cBxTmpl.setGeometry(QtCore.QRect(30, 120, 121, 16))
        self.cBxTmpl.setObjectName("cBxTmpl")
        self.bTnModify = QtWidgets.QPushButton(ModifyTmplForm)
        self.bTnModify.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.bTnModify.setObjectName("bTnModify")
        self.lEtTmpName = QtWidgets.QLineEdit(ModifyTmplForm)
        self.lEtTmpName.setGeometry(QtCore.QRect(80, 10, 281, 20))
        self.lEtTmpName.setObjectName("lEtTmpName")
        self.cBxLanguage = QtWidgets.QComboBox(ModifyTmplForm)
        self.cBxLanguage.setGeometry(QtCore.QRect(80, 40, 281, 22))
        self.cBxLanguage.setObjectName("cBxLanguage")
        self.cBxLanguage.addItem("")
        self.cBxLanguage.addItem("")
        self.cBxLanguage.addItem("")
        self.cBxLanguage.addItem("")
        self.lEtPublishDir = QtWidgets.QLineEdit(ModifyTmplForm)
        self.lEtPublishDir.setGeometry(QtCore.QRect(80, 70, 281, 20))
        self.lEtPublishDir.setObjectName("lEtPublishDir")
        self.bTnPublishDirChoose = QtWidgets.QPushButton(ModifyTmplForm)
        self.bTnPublishDirChoose.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.bTnPublishDirChoose.setObjectName("bTnPublishDirChoose")

        self.retranslateUi(ModifyTmplForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyTmplForm)

    def retranslateUi(self, ModifyTmplForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyTmplForm.setWindowTitle(_translate("ModifyTmplForm", "修改模板"))
        self.label.setText(_translate("ModifyTmplForm", "模板名称："))
        self.label_2.setText(_translate("ModifyTmplForm", "模板语言："))
        self.label_3.setText(_translate("ModifyTmplForm", "发布目录："))
        self.cBxTmpl.setText(_translate("ModifyTmplForm", "仅导出服务器"))
        self.bTnModify.setText(_translate("ModifyTmplForm", "修改"))
        self.cBxLanguage.setItemText(0, _translate("ModifyTmplForm", "c++"))
        self.cBxLanguage.setItemText(1, _translate("ModifyTmplForm", "golang"))
        self.cBxLanguage.setItemText(2, _translate("ModifyTmplForm", "csharp"))
        self.cBxLanguage.setItemText(3, _translate("ModifyTmplForm", "lua"))
        self.bTnPublishDirChoose.setText(_translate("ModifyTmplForm", "选择"))

