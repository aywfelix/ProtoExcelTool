# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/modify_proto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyProtoForm(object):
    def setupUi(self, ModifyProtoForm):
        ModifyProtoForm.setObjectName("ModifyProtoForm")
        ModifyProtoForm.resize(504, 550)
        self.tEtProtoDesc = QtWidgets.QTextEdit(ModifyProtoForm)
        self.tEtProtoDesc.setGeometry(QtCore.QRect(80, 121, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tEtProtoDesc.setFont(font)
        self.tEtProtoDesc.setObjectName("tEtProtoDesc")
        self.tEtProtoContent = QtWidgets.QTextEdit(ModifyProtoForm)
        self.tEtProtoContent.setGeometry(QtCore.QRect(10, 190, 481, 321))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tEtProtoContent.setFont(font)
        self.tEtProtoContent.setObjectName("tEtProtoContent")
        self.lEtProtoId = QtWidgets.QLineEdit(ModifyProtoForm)
        self.lEtProtoId.setGeometry(QtCore.QRect(80, 40, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lEtProtoId.setFont(font)
        self.lEtProtoId.setReadOnly(False)
        self.lEtProtoId.setObjectName("lEtProtoId")
        self.label_5 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_5.setGeometry(QtCore.QRect(10, 121, 71, 21))
        self.label_5.setObjectName("label_5")
        self.bTnProtoModify = QtWidgets.QPushButton(ModifyProtoForm)
        self.bTnProtoModify.setGeometry(QtCore.QRect(200, 520, 75, 23))
        self.bTnProtoModify.setObjectName("bTnProtoModify")
        self.label_3 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_3.setGeometry(QtCore.QRect(10, 41, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_4.setGeometry(QtCore.QRect(10, 81, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(ModifyProtoForm)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lEtProtoName = QtWidgets.QLineEdit(ModifyProtoForm)
        self.lEtProtoName.setGeometry(QtCore.QRect(80, 80, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lEtProtoName.setFont(font)
        self.lEtProtoName.setObjectName("lEtProtoName")
        self.label = QtWidgets.QLabel(ModifyProtoForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.rBtnReq = QtWidgets.QRadioButton(ModifyProtoForm)
        self.rBtnReq.setGeometry(QtCore.QRect(90, 10, 89, 16))
        self.rBtnReq.setObjectName("rBtnReq")
        self.rBtnCom = QtWidgets.QRadioButton(ModifyProtoForm)
        self.rBtnCom.setGeometry(QtCore.QRect(400, 10, 89, 16))
        self.rBtnCom.setObjectName("rBtnCom")
        self.rBtnNotify = QtWidgets.QRadioButton(ModifyProtoForm)
        self.rBtnNotify.setGeometry(QtCore.QRect(300, 10, 89, 16))
        self.rBtnNotify.setObjectName("rBtnNotify")
        self.rBtnAck = QtWidgets.QRadioButton(ModifyProtoForm)
        self.rBtnAck.setGeometry(QtCore.QRect(190, 10, 89, 16))
        self.rBtnAck.setObjectName("rBtnAck")

        self.retranslateUi(ModifyProtoForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyProtoForm)

    def retranslateUi(self, ModifyProtoForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyProtoForm.setWindowTitle(_translate("ModifyProtoForm", "修改协议"))
        self.label_5.setText(_translate("ModifyProtoForm", "协议说明："))
        self.bTnProtoModify.setText(_translate("ModifyProtoForm", "修改"))
        self.label_3.setText(_translate("ModifyProtoForm", "协议编号："))
        self.label_4.setText(_translate("ModifyProtoForm", "协议名称："))
        self.label_6.setText(_translate("ModifyProtoForm", "协议内容："))
        self.label.setText(_translate("ModifyProtoForm", "协议类型："))
        self.rBtnReq.setText(_translate("ModifyProtoForm", "请求消息"))
        self.rBtnCom.setText(_translate("ModifyProtoForm", "共用消息"))
        self.rBtnNotify.setText(_translate("ModifyProtoForm", "广播消息"))
        self.rBtnAck.setText(_translate("ModifyProtoForm", "请求确认消息"))

