#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示更改目录窗口
'''

# here put the import lib
from posixpath import dirname
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_ui.uipy.modify_dir import *

class ModifyProtoDirUI(QMainWindow):
    # 窗体间通信
    dialogSinal = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(ModifyProtoDirUI, self).__init__()
        self.ui = Ui_ModifyDirForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.ui.bTnModifyDir.clicked.connect(self.inputDirName)
        # 清空输入框信息
        self.ui.tEtImport.installEventFilter(self)
        self.ui.bTnClearImport.clicked.connect(self.clearEditText)
        pass

    def fillDirData(self, dirData):
        self.ui.lEtProtoDirName.setText(dirData.dirName)
        self.ui.tEtImport.setText(dirData.package)
        pass

    def inputDirName(self):
        dirname = self.ui.lEtProtoDirName.text()
        package = self.ui.tEtImport.toPlainText()
        self.dialogSinal.emit(dirname, package)
        self.close()
        
    def clearEditText(self):
        self.ui.tEtImport.setText("")
            