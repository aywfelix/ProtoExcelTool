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
from qt_ui.uipy.create_proto_dir import *

class CreateProtoDirUI(QMainWindow):
    # 窗体间通信
    dialogSinal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(CreateProtoDirUI, self).__init__()
        self.ui = Ui_CreateDirForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        # 添加关联事件
        self.ui.bTnCreateDir.clicked.connect(self.inputDirName)
        #self.ui.lEtProtoPackage.clicked.connect(self.clearEditText)
        pass

    def inputDirName(self):
        dirname = self.ui.lEtProtoDirName.text()
        self.dialogSinal.emit(dirname)
        self.close()

    def clearEditText(self):
        self.ui.lEtProtoPackage.setText("")
        
