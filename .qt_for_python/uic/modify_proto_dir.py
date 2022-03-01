# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\达瓦未来\ProtocolAndExcelTool\qt_ui\ui\modify_proto_dir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ModifyDirForm(object):
    def setupUi(self, ModifyDirForm):
        ModifyDirForm.setObjectName("ModifyDirForm")
        ModifyDirForm.resize(352, 78)
        self.label = QtWidgets.QLabel(ModifyDirForm)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.label.setObjectName("label")
        self.bTnModifyDir = QtWidgets.QPushButton(ModifyDirForm)
        self.bTnModifyDir.setGeometry(QtCore.QRect(140, 50, 75, 23))
        self.bTnModifyDir.setObjectName("bTnModifyDir")
        self.lEtProtoDirName = QtWidgets.QLineEdit(ModifyDirForm)
        self.lEtProtoDirName.setGeometry(QtCore.QRect(90, 20, 241, 20))
        self.lEtProtoDirName.setObjectName("lEtProtoDirName")

        self.retranslateUi(ModifyDirForm)
        QtCore.QMetaObject.connectSlotsByName(ModifyDirForm)

    def retranslateUi(self, ModifyDirForm):
        _translate = QtCore.QCoreApplication.translate
        ModifyDirForm.setWindowTitle(_translate("ModifyDirForm", "修改目录"))
        self.label.setText(_translate("ModifyDirForm", "目录名称："))
        self.bTnModifyDir.setText(_translate("ModifyDirForm", "修改"))

