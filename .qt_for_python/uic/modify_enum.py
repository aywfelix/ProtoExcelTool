# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\达瓦未来\ProtocolAndExcelTool\qt_ui\ui\modify_enum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyEnumForm(object):
    def setupUi(self, ModifyEnumForm):
        ModifyEnumForm.setObjectName("ModifyEnumForm")
        ModifyEnumForm.resize(504, 541)
        self.bTnEnumCancel = QtWidgets.QPushButton(ModifyEnumForm)
        self.bTnEnumCancel.setGeometry(QtCore.QRect(280, 510, 75, 23))
        self.bTnEnumCancel.setObjectName("bTnEnumCancel")
        self.lEtEnumDesc = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumDesc.setGeometry(QtCore.QRect(80, 50, 411, 20))
        self.lEtEnumDesc.setObjectName("lEtEnumDesc")
        self.label_7 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lEtEnumName = QtWidgets.QLineEdit(ModifyEnumForm)
        self.lEtEnumName.setGeometry(QtCore.QRect(80, 10, 411, 20))
        self.lEtEnumName.setObjectName("lEtEnumName")
        self.label_10 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_10.setObjectName("label_10")
        self.tBvEnum = QtWidgets.QTableView(ModifyEnumForm)
        self.tBvEnum.setGeometry(QtCore.QRect(80, 90, 411, 411))
        self.tBvEnum.setObjectName("tBvEnum")
        self.label_8 = QtWidgets.QLabel(ModifyEnumForm)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_8.setObjectName("label_8")
        self.cBxEnum = QtWidgets.QCheckBox(ModifyEnumForm)
        self.cBxEnum.setGeometry(QtCore.QRect(80, 510, 121, 16))
        self.cBxEnum.setObjectName("cBxEnum")
        self.bTnEnumUpdate = QtWidgets.QPushButton(ModifyEnumForm)
        self.bTnEnumUpdate.setGeometry(QtCore.QRect(410, 510, 75, 23))
        self.bTnEnumUpdate.setObjectName("bTnEnumUpdate")

        self.retranslateUi(ModifyEnumForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyEnumForm)

    def retranslateUi(self, ModifyEnumForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyEnumForm.setWindowTitle(_translate("ModifyEnumForm", "修改枚举"))
        self.bTnEnumCancel.setText(_translate("ModifyEnumForm", "取消修改"))
        self.label_7.setText(_translate("ModifyEnumForm", "枚举名称："))
        self.label_10.setText(_translate("ModifyEnumForm", "枚举字段："))
        self.label_8.setText(_translate("ModifyEnumForm", "枚举说明："))
        self.cBxEnum.setText(_translate("ModifyEnumForm", "仅导出服务器"))
        self.bTnEnumUpdate.setText(_translate("ModifyEnumForm", "修改"))

