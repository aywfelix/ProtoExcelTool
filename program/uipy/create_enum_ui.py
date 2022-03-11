# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../designer/ui/create_enum.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CreateEnumForm(object):
    def setupUi(self, CreateEnumForm):
        CreateEnumForm.setObjectName("CreateEnumForm")
        CreateEnumForm.resize(529, 642)
        self.lEtEnumDesc = QtWidgets.QLineEdit(CreateEnumForm)
        self.lEtEnumDesc.setGeometry(QtCore.QRect(80, 50, 431, 20))
        self.lEtEnumDesc.setObjectName("lEtEnumDesc")
        self.cBxEnum = QtWidgets.QCheckBox(CreateEnumForm)
        self.cBxEnum.setGeometry(QtCore.QRect(80, 610, 121, 16))
        self.cBxEnum.setObjectName("cBxEnum")
        self.label_7 = QtWidgets.QLabel(CreateEnumForm)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.label_7.setObjectName("label_7")
        self.lEtEnumName = QtWidgets.QLineEdit(CreateEnumForm)
        self.lEtEnumName.setGeometry(QtCore.QRect(80, 10, 431, 20))
        self.lEtEnumName.setObjectName("lEtEnumName")
        self.label_8 = QtWidgets.QLabel(CreateEnumForm)
        self.label_8.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(CreateEnumForm)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 71, 21))
        self.label_10.setObjectName("label_10")
        self.bTnEnumCreate = QtWidgets.QPushButton(CreateEnumForm)
        self.bTnEnumCreate.setGeometry(QtCore.QRect(280, 610, 75, 23))
        self.bTnEnumCreate.setObjectName("bTnEnumCreate")
        self.tBvEnum = QtWidgets.QTableWidget(CreateEnumForm)
        self.tBvEnum.setGeometry(QtCore.QRect(80, 90, 431, 491))
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
        self.tBvEnum.verticalHeader().setDefaultSectionSize(35)
        self.tBvEnum.verticalHeader().setMinimumSectionSize(30)
        self.tBvEnum.verticalHeader().setSortIndicatorShown(False)
        self.tBvEnum.verticalHeader().setStretchLastSection(False)

        self.retranslateUi(CreateEnumForm)
        QtCore.QMetaObject.connectSlotsByName(CreateEnumForm)

    def retranslateUi(self, CreateEnumForm):
        _translate = QtCore.QCoreApplication.translate
        CreateEnumForm.setWindowTitle(_translate("CreateEnumForm", "创建枚举"))
        self.cBxEnum.setText(_translate("CreateEnumForm", "仅导出服务器"))
        self.label_7.setText(_translate("CreateEnumForm", "枚举名称："))
        self.label_8.setText(_translate("CreateEnumForm", "枚举说明："))
        self.label_10.setText(_translate("CreateEnumForm", "枚举字段："))
        self.bTnEnumCreate.setText(_translate("CreateEnumForm", "创建"))
        item = self.tBvEnum.horizontalHeaderItem(0)
        item.setText(_translate("CreateEnumForm", "索引"))
        item = self.tBvEnum.horizontalHeaderItem(1)
        item.setText(_translate("CreateEnumForm", "名称"))
        item = self.tBvEnum.horizontalHeaderItem(2)
        item.setText(_translate("CreateEnumForm", "说明"))

