#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   None
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_ui.uipy.create_proto_ui import *

class CreateProtoUI(QMainWindow):
    # 窗体间通信
    dialogSinal = pyqtSignal(str, str, str, str, bool)

    def __init__(self, parent=None):
        super(CreateProtoUI, self).__init__()
        self.ui = Ui_CreateProtoForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.ui.bTnProtoCreate.clicked.connect(self.createProto)

        pass

    def createProto(self):
        protoId = self.ui.lEtProtoId.text()
        protoName = self.ui.lEtProtoName.text()
        protoDesc = self.ui.tEtProtoDesc.toPlainText()
        protoContent = self.ui.tEtProtoContent.toPlainText()

        self.dialogSinal.emit(protoId, protoName, protoDesc, protoContent, False)
        self.close()
        
