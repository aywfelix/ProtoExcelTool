# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/create_proto.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateProtoForm(object):
    def setupUi(self, CreateProtoForm):
        CreateProtoForm.setObjectName("CreateProtoForm")
        CreateProtoForm.resize(504, 544)
        self.tEtProtoDesc = QtWidgets.QTextEdit(CreateProtoForm)
        self.tEtProtoDesc.setGeometry(QtCore.QRect(80, 120, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tEtProtoDesc.setFont(font)
        self.tEtProtoDesc.setObjectName("tEtProtoDesc")
        self.tEtProtoContent = QtWidgets.QTextEdit(CreateProtoForm)
        self.tEtProtoContent.setGeometry(QtCore.QRect(10, 190, 481, 311))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tEtProtoContent.setFont(font)
        self.tEtProtoContent.setObjectName("tEtProtoContent")
        self.lEtProtoId = QtWidgets.QLineEdit(CreateProtoForm)
        self.lEtProtoId.setGeometry(QtCore.QRect(80, 39, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lEtProtoId.setFont(font)
        self.lEtProtoId.setObjectName("lEtProtoId")
        self.label_5 = QtWidgets.QLabel(CreateProtoForm)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_5.setObjectName("label_5")
        self.bTnProtoCreate = QtWidgets.QPushButton(CreateProtoForm)
        self.bTnProtoCreate.setGeometry(QtCore.QRect(200, 510, 75, 23))
        self.bTnProtoCreate.setObjectName("bTnProtoCreate")
        self.label_3 = QtWidgets.QLabel(CreateProtoForm)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CreateProtoForm)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(CreateProtoForm)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lEtProtoName = QtWidgets.QLineEdit(CreateProtoForm)
        self.lEtProtoName.setGeometry(QtCore.QRect(80, 79, 411, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lEtProtoName.setFont(font)
        self.lEtProtoName.setObjectName("lEtProtoName")
        self.rBtnReq = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnReq.setGeometry(QtCore.QRect(90, 10, 89, 16))
        self.rBtnReq.setObjectName("rBtnReq")
        self.rBtnNotify = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnNotify.setGeometry(QtCore.QRect(310, 10, 89, 16))
        self.rBtnNotify.setObjectName("rBtnNotify")
        self.label = QtWidgets.QLabel(CreateProtoForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")
        self.rBtnCom = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnCom.setGeometry(QtCore.QRect(410, 10, 89, 16))
        self.rBtnCom.setObjectName("rBtnCom")
        self.rBtnAck = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnAck.setGeometry(QtCore.QRect(200, 10, 89, 16))
        self.rBtnAck.setObjectName("rBtnAck")

        self.retranslateUi(CreateProtoForm)
        QtCore.QMetaObject.connectSlotsByName(CreateProtoForm)

    def retranslateUi(self, CreateProtoForm):
        _translate = QtCore.QCoreApplication.translate
        CreateProtoForm.setWindowTitle(_translate("CreateProtoForm", "创建协议"))
        self.label_5.setText(_translate("CreateProtoForm", "协议说明："))
        self.bTnProtoCreate.setText(_translate("CreateProtoForm", "创建"))
        self.label_3.setText(_translate("CreateProtoForm", "协议编号："))
        self.label_4.setText(_translate("CreateProtoForm", "协议名称："))
        self.label_6.setText(_translate("CreateProtoForm", "协议内容："))
        self.rBtnReq.setText(_translate("CreateProtoForm", "请求消息"))
        self.rBtnNotify.setText(_translate("CreateProtoForm", "广播消息"))
        self.label.setText(_translate("CreateProtoForm", "协议类型："))
        self.rBtnCom.setText(_translate("CreateProtoForm", "共用消息"))
        self.rBtnAck.setText(_translate("CreateProtoForm", "请求确认消息"))

