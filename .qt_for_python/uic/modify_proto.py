# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\达瓦未来\ProtocolAndExcelTool\qt_ui\ui\modify_proto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyProtoForm(object):
    def setupUi(self, ModifyProtoForm):
        ModifyProtoForm.setObjectName("ModifyProtoForm")
        ModifyProtoForm.resize(504, 544)
        self.tEtProtoDesc = QtWidgets.QTextEdit(ModifyProtoForm)
        self.tEtProtoDesc.setGeometry(QtCore.QRect(80, 90, 411, 41))
        self.tEtProtoDesc.setObjectName("tEtProtoDesc")
        self.tEtProtoContent = QtWidgets.QTextEdit(ModifyProtoForm)
        self.tEtProtoContent.setGeometry(QtCore.QRect(80, 150, 411, 351))
        self.tEtProtoContent.setObjectName("tEtProtoContent")
        self.lEtProtoNum = QtWidgets.QLineEdit(ModifyProtoForm)
        self.lEtProtoNum.setGeometry(QtCore.QRect(80, 10, 411, 20))
        self.lEtProtoNum.setObjectName("lEtProtoNum")
        self.label_5 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_5.setObjectName("label_5")
        self.bTnProtoUpdate = QtWidgets.QPushButton(ModifyProtoForm)
        self.bTnProtoUpdate.setGeometry(QtCore.QRect(280, 510, 75, 23))
        self.bTnProtoUpdate.setObjectName("bTnProtoUpdate")
        self.label_3 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lEtProtoName = QtWidgets.QLineEdit(ModifyProtoForm)
        self.lEtProtoName.setGeometry(QtCore.QRect(80, 50, 411, 20))
        self.lEtProtoName.setObjectName("lEtProtoName")
        self.cBxProtocol = QtWidgets.QCheckBox(ModifyProtoForm)
        self.cBxProtocol.setGeometry(QtCore.QRect(80, 510, 121, 16))
        self.cBxProtocol.setObjectName("cBxProtocol")

        self.retranslateUi(ModifyProtoForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyProtoForm)

    def retranslateUi(self, ModifyProtoForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyProtoForm.setWindowTitle(_translate("ModifyProtoForm", "修改协议"))
        self.label_5.setText(_translate("ModifyProtoForm", "协议说明："))
        self.bTnProtoUpdate.setText(_translate("ModifyProtoForm", "修改"))
        self.label_3.setText(_translate("ModifyProtoForm", "协议编号："))
        self.label_4.setText(_translate("ModifyProtoForm", "协议名称："))
        self.label_6.setText(_translate("ModifyProtoForm", "协议内容："))
        self.cBxProtocol.setText(_translate("ModifyProtoForm", "仅导出服务器"))

