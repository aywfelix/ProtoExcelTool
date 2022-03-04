#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tool_setting.py
@Time    :   2022/03/04 10:17:03
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   用于显示setting界面
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_ui.logic.setting_xml import *
from qt_ui.uipy.setting_ui import *

class OpenFileType:
    PROTOC = 1
    PROTO = 2
    TABLE = 3

class ToolSettingUI(QMainWindow):
    def __init__(self, parent=None):
        super(ToolSettingUI, self).__init__()
        self.ui = Ui_SettingForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        # 关联事件处理
        self.ui.bTnProtoc.clicked.connect(lambda: self.openFilePath(OpenFileType.PROTOC))
        self.ui.bTnProto.clicked.connect(lambda: self.openFilePath(OpenFileType.PROTO))
        self.ui.bTnTable.clicked.connect(lambda: self.openFilePath(OpenFileType.TABLE))

        # 处理配置文件
        self.settingXml = ToolSettingXml()

        # 打开窗口初始化配置信息
        self.openWindow()    
        pass

    def openWindow(self):
        # filePath
        protocPath, protoPath, tablePath = self.settingXml.readToolConfig()
        self.ui.lEtProtocPath.setText(protocPath)
        self.ui.lEtProtoPath.setText(protoPath)
        self.ui.lEtTablePath.setText(tablePath)

        pass

    def closeEvent(self, event):
        # 保存filePath配置
        protocPath = self.ui.lEtProtocPath.text()
        protoPath = self.ui.lEtProtoPath.text()
        tablePath = self.ui.lEtTablePath.text()
        self.settingXml.saveToolSetting(protocPath, protoPath, tablePath)

    def openFilePath(self, openType):
        print("type===", openType)
        # 打开文件对话框
        filePath = QFileDialog.getExistingDirectory(
            self, '选择目录', './')
        if not filePath:
            return
        if openType == OpenFileType.PROTOC:
            self.ui.lEtProtocPath.setText(filePath)
        if openType == OpenFileType.PROTO:
            self.ui.lEtProtoPath.setText(filePath)
        if openType == OpenFileType.TABLE:
            self.ui.lEtTablePath.setText(filePath)
        pass


