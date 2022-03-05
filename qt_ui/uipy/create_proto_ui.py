# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/create_proto.ui'
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
        self.tEtProtoDesc.setObjectName("tEtProtoDesc")
        self.tEtProtoContent = QtWidgets.QTextEdit(CreateProtoForm)
        self.tEtProtoContent.setGeometry(QtCore.QRect(80, 180, 411, 321))
        self.tEtProtoContent.setObjectName("tEtProtoContent")
        self.lEtProtoId = QtWidgets.QLineEdit(CreateProtoForm)
        self.lEtProtoId.setGeometry(QtCore.QRect(80, 40, 411, 20))
        self.lEtProtoId.setObjectName("lEtProtoId")
        self.label_5 = QtWidgets.QLabel(CreateProtoForm)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_5.setObjectName("label_5")
        self.bTnProtoCreate = QtWidgets.QPushButton(CreateProtoForm)
        self.bTnProtoCreate.setGeometry(QtCore.QRect(280, 510, 75, 23))
        self.bTnProtoCreate.setObjectName("bTnProtoCreate")
        self.label_3 = QtWidgets.QLabel(CreateProtoForm)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(CreateProtoForm)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(CreateProtoForm)
        self.label_6.setGeometry(QtCore.QRect(10, 170, 71, 21))
        self.label_6.setObjectName("label_6")
        self.lEtProtoName = QtWidgets.QLineEdit(CreateProtoForm)
        self.lEtProtoName.setGeometry(QtCore.QRect(80, 80, 411, 20))
        self.lEtProtoName.setObjectName("lEtProtoName")
        self.cBxProtocol = QtWidgets.QCheckBox(CreateProtoForm)
        self.cBxProtocol.setGeometry(QtCore.QRect(80, 510, 121, 16))
        self.cBxProtocol.setObjectName("cBxProtocol")
        self.rBtnReq = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnReq.setGeometry(QtCore.QRect(100, 10, 89, 16))
        self.rBtnReq.setObjectName("rBtnReq")
        self.rBtnNotify = QtWidgets.QRadioButton(CreateProtoForm)
        self.rBtnNotify.setGeometry(QtCore.QRect(220, 10, 89, 16))
        self.rBtnNotify.setObjectName("rBtnNotify")
        self.label = QtWidgets.QLabel(CreateProtoForm)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName("label")

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
        self.cBxProtocol.setText(_translate("CreateProtoForm", "仅导出服务器"))
        self.rBtnReq.setText(_translate("CreateProtoForm", "请求消息"))
        self.rBtnNotify.setText(_translate("CreateProtoForm", "广播消息"))
        self.label.setText(_translate("CreateProtoForm", "协议类型："))

