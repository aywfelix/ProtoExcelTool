﻿#!/usr/bin/env python
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
from qt_ui.logic.add_tmpl import *
from qt_ui.logic.modify_tmpl import *

class SetPathType:
    PROTOC = 1
    PROTO = 2
    TABLE = 3

class TmplType:
    PROTO = 1
    ENUM = 2
    TABLE = 3

class ToolSettingUI(QMainWindow):
    def __init__(self, parent=None):
        super(ToolSettingUI, self).__init__()
        self.ui = Ui_SettingForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        # 设置默认为tab索引
        self.ui.tabWidget.setCurrentIndex(0)

        # 关联事件处理
        self.ui.bTnProtoc.clicked.connect(lambda: self.setDirPath(SetPathType.PROTOC))
        self.ui.bTnProto.clicked.connect(lambda: self.setDirPath(SetPathType.PROTO))
        self.ui.bTnTable.clicked.connect(lambda: self.setDirPath(SetPathType.TABLE))
        # 添加模板操作
        self.ui.bTnProtoAddTmpl.clicked.connect(lambda: self.showAddTmpl(TmplType.PROTO))
        self.ui.bTnEnumAddTmpl.clicked.connect(lambda: self.showAddTmpl(TmplType.ENUM))
        self.ui.bTnTableAddTmpl.clicked.connect(lambda: self.showAddTmpl(TmplType.TABLE))
        # 处理配置文件
        self.settingXml = ToolSettingXml()
        # 布局
        self.protoFormLayout = QtWidgets.QFormLayout()
        self.enumFormLayout = QtWidgets.QFormLayout()
        self.tableFormLayout = QtWidgets.QFormLayout()
        
        # 临时保存模板操作页
        self.tmplType = 1
        # 打开窗口初始化配置信息
        self.openWindow()    
        pass

        
    def openWindow(self):
        # tab1--工具常用配置
        protocPath, protoPath, tablePath = self.settingXml.readToolConfig()
        self.ui.lEtProtocPath.setText(protocPath)
        self.ui.lEtProtoPath.setText(protoPath)
        self.ui.lEtTablePath.setText(tablePath)
        # tab2--协议配置
        # tab3--枚举配置
        # tab4--配置表配置
        pass

    def closeEvent(self, event):
        # 保存filePath配置
        protocPath = self.ui.lEtProtocPath.text()
        protoPath = self.ui.lEtProtoPath.text()
        tablePath = self.ui.lEtTablePath.text()
        self.settingXml.saveToolSetting(protocPath, protoPath, tablePath)

    def setDirPath(self, openType):
        print("type===", openType)
        # 打开文件对话框
        dirPath = QFileDialog.getExistingDirectory(
            self, '选择目录', './')
        if not dirPath:
            return
        if openType == SetPathType.PROTOC:
            self.ui.lEtProtocPath.setText(dirPath)
        if openType == SetPathType.PROTO:
            self.ui.lEtProtoPath.setText(dirPath)
        if openType == SetPathType.TABLE:
            self.ui.lEtTablePath.setText(dirPath)
        pass

    def showAddTmpl(self, tmplType):
        self.tmplType = tmplType
        self.addTmplUI = AddTmplUI()
        self.addTmplUI.show()
        self.addTmplUI.dialogSignal.connect(self.appendTmplInfo)
        pass

    # 列出所有模板配置
    def showTmplList(self):
        # 读取配置显示所有配置模板信息
        pass

    # 追加模板信息
    def appendTmplInfo(self, tmplName, tmplLang):
        # 生成界面显示组件-QListWidget
        hBoxLayout = QtWidgets.QHBoxLayout()
        if self.tmplType == TmplType.PROTO:
            self.protoFormLayout.addRow(hBoxLayout)
            self.ui.lWProto.setLayout(self.protoFormLayout)
        if self.tmplType == TmplType.ENUM:
            self.enumFormLayout.addRow(hBoxLayout)
            self.ui.lWEnum.setLayout(self.enumFormLayout)
        if self.tmplType == TmplType.TABLE:
            self.tableFormLayout.addRow(hBoxLayout)
            self.ui.lWTable.setLayout(self.tableFormLayout)
        # 根据传值生成控件
        lEtTemplName = QLineEdit()
        lEtTemplName.setText(tmplName)
        lEtTemplName.setReadOnly(True)
        lEtTemplName.setFixedWidth(150)
        lEtTmplLang = QLineEdit()
        lEtTmplLang.setText(tmplLang)
        lEtTmplLang.setReadOnly(True)
        lEtTmplLang.setFixedWidth(60)

        bTnModify = QPushButton()
        bTnModify.setText("修改")
        bTnModify.clicked.connect(self.showModifyTmpl)
        bTnModify.setFixedWidth(80)
        bTnDelete = QPushButton()
        bTnDelete.setText("删除")
        bTnDelete.clicked.connect(lambda: self.deleteTmpl(hBoxLayout))
        bTnDelete.setFixedWidth(80)
        
        hBoxLayout.addWidget(lEtTemplName)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(lEtTmplLang)
        hBoxLayout.addStretch(2)
        hBoxLayout.addWidget(bTnModify)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(bTnDelete)
        pass
    
    def showModifyTmpl(self):
        # 弹出更改窗口
        self.modifyTmplUI = ModifyTmplUI()
        self.modifyTmplUI.show()
        self.modifyTmplUI.dialogSignal.connect(self.modifyTmpl)
        pass
    
    def deleteTmpl(self, layout):
        if self.tmplType == TmplType.PROTO:
            self.protoFormLayout.removeRow(layout)
        if self.tmplType == TmplType.ENUM:
            self.enumFormLayout.removeRow(layout)
        if self.tmplType == TmplType.TABLE:
            self.tableFormLayout.removeRow(layout)
        pass
    
    def modifyTmpl(self, tmplName, tmplLang, tmplPublish):
        print(tmplName, tmplLang, tmplPublish)


