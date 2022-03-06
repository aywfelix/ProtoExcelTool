#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示更改协议窗口
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.modify_proto_ui import *

class ModifyProtoUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(str, str, str, str, bool)

    def __init__(self, parent=None):
        super(ModifyProtoUI, self).__init__()
        self.ui = Ui_ModifyProtoForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.ui.bTnProtoModify.clicked.connect(self.modifyProto)
        self.ui.lEtProtoId.editingFinished.connect(self.checkProtoId)
        pass

    def checkProtoId(self):
        protoId = self.ui.lEtProtoId.text()
        if not protoId.isdigit():
            # 弹出警告
            QMessageBox.critical(self, "错误", "协议编号默认为整数数字!!!")
            pass
        pass

    def modifyProto(self):
        protoId = self.ui.lEtProtoId.text()
        protoName = self.ui.lEtProtoName.text()
        protoDesc = self.ui.tEtProtoDesc.toPlainText()
        protoContent = self.ui.tEtProtoContent.toPlainText()
        onlyServer = self.ui.cBxProtocol.isChecked()

        self.dialogSignal.emit(
            protoId, protoName, protoDesc, protoContent, onlyServer)
        self.close()

    def fillProtoData(self, data):
        self.ui.lEtProtoId.setText(data.id)
        self.ui.lEtProtoName.setText(data.name)
        self.ui.tEtProtoDesc.setText(data.desc)
        self.ui.tEtProtoContent.setText(data.content)
        self.ui.cBxProtocol.setChecked(bool(data.onlyServer))
        pass
        
