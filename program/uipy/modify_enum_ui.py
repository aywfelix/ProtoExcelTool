# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/modify_enum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyEnumForm(object):
    def setupUi(self, ModifyEnumForm):
        ModifyEnumForm.setObjectName("ModifyEnumForm")
        ModifyEnumForm.resize(529, 654)
        self.lEtEnumDesc = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumDesc.setGeometry(QtCore.QRect(80, 80, 431, 31))
        self.lEtEnumDesc.setObjectName("lEtEnumDesc")
        self.label_7 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lEtEnumName = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumName.setGeometry(QtCore.QRect(80, 40, 431, 31))
        self.lEtEnumName.setObjectName("lEtEnumName")
        self.label_8 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_8.setGeometry(QtCore.QRect(10, 80, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_10.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_10.setObjectName("label_10")
        self.bTnEnumModify = QtWidgets.QPushButton(ModifyEnumForm)
        self.bTnEnumModify.setGeometry(QtCore.QRect(250, 620, 75, 23))
        self.bTnEnumModify.setObjectName("bTnEnumModify")
        self.tBvEnum = QtWidgets.QTableWidget(ModifyEnumForm)
        self.tBvEnum.setGeometry(QtCore.QRect(80, 120, 431, 491))
        self.tBvEnum.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tBvEnum.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tBvEnum.setColumnCount(3)
        self.tBvEnum.setObjectName("tBvEnum")
        self.tBvEnum.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tBvEnum.setHorizontalHeaderItem(2, item)
        self.tBvEnum.verticalHeader().setVisible(False)
        self.tBvEnum.verticalHeader().setDefaultSectionSize(35)
        self.tBvEnum.verticalHeader().setMinimumSectionSize(30)
        self.tBvEnum.verticalHeader().setSortIndicatorShown(False)
        self.tBvEnum.verticalHeader().setStretchLastSection(False)
        self.rBtnCom = QtWidgets.QRadioButton(ModifyEnumForm)
        self.rBtnCom.setGeometry(QtCore.QRect(418, 10, 91, 21))
        self.rBtnCom.setObjectName("rBtnCom")
        self.rBtnServer = QtWidgets.QRadioButton(ModifyEnumForm)
        self.rBtnServer.setGeometry(QtCore.QRect(90, 10, 89, 21))
        self.rBtnServer.setObjectName("rBtnServer")
        self.label_9 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_9.setObjectName("label_9")
        self.rBtnClient = QtWidgets.QRadioButton(ModifyEnumForm)
        self.rBtnClient.setGeometry(QtCore.QRect(250, 10, 89, 21))
        self.rBtnClient.setObjectName("rBtnClient")

        self.retranslateUi(ModifyEnumForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyEnumForm)

    def retranslateUi(self, ModifyEnumForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyEnumForm.setWindowTitle(_translate("ModifyEnumForm", "修改枚举"))
        self.label_7.setText(_translate("ModifyEnumForm", "枚举名称："))
        self.label_8.setText(_translate("ModifyEnumForm", "枚举说明："))
        self.label_10.setText(_translate("ModifyEnumForm", "枚举字段："))
        self.bTnEnumModify.setText(_translate("ModifyEnumForm", "修改"))
        item = self.tBvEnum.horizontalHeaderItem(0)
        item.setText(_translate("ModifyEnumForm", "索引"))
        item = self.tBvEnum.horizontalHeaderItem(1)
        item.setText(_translate("ModifyEnumForm", "名称"))
        item = self.tBvEnum.horizontalHeaderItem(2)
        item.setText(_translate("ModifyEnumForm", "说明"))
        self.rBtnCom.setText(_translate("ModifyEnumForm", "共用"))
        self.rBtnServer.setText(_translate("ModifyEnumForm", "服务器"))
        self.label_9.setText(_translate("ModifyEnumForm", "枚举类型："))
        self.rBtnClient.setText(_translate("ModifyEnumForm", "客户端"))

