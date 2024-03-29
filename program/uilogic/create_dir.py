﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示创建目录窗口
'''

# here put the import lib
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.create_dir_ui import *
from proto_xml import *

class CreateProtoDirUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(TVItemDirData)

    def __init__(self, parent=None):
        super(CreateProtoDirUI, self).__init__()
        self.ui = Ui_CreateDirForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.parent = parent
        self.protoXml = ToolProtoXml()
        # 添加关联事件
        self.ui.bTnCreateDir.clicked.connect(self.inputDirName)
        self.ui.bTnClearImport.clicked.connect(self.clearEditText)
        pass

    def checkDirName(self, dirName):
        if len(dirName) == 0 or len(dirName)>20:
            QMessageBox.critical(self, "错误", "目录名不能为空且长度不能超过20")
            self.ui.lEtProtoDirName.setText("")
            return False
            pass
        if not re.search(r'\d{1,4}\s+[a-z]+', dirName):
            QMessageBox.critical(self, "错误", "目录名格为1-4数字+空格+字母名")
            self.ui.lEtProtoDirName.setText("")
            return False
         # 直接判断目录名是否重复
        if self.protoXml.getDirData(dirName):
            QMessageBox.critical(self, "错误", "目录名已存在")
            self.ui.lEtProtoDirName.setText("") 
            return False

        return True
    
    def inputDirName(self):
        dirName = self.ui.lEtProtoDirName.text().strip()
        package = self.ui.tEtImport.toPlainText()
        if not self.checkDirName(dirName):
            self.close()
            return

        dirData = TVItemDirData(dirName, package)
        self.dialogSignal.emit(dirData)
        self.close()

    def clearEditText(self):
        self.ui.tEtImport.setText("")
        
