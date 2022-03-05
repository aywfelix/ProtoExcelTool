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
from turtle import pu
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
        # 用于语言索引转换
        self.tmplLang = TmplLang()
        # 布局
        self.protoFormLayout = QtWidgets.QFormLayout()
        self.enumFormLayout = QtWidgets.QFormLayout()
        self.tableFormLayout = QtWidgets.QFormLayout()
        self.ui.lWProto.setLayout(self.protoFormLayout)
        self.ui.lWEnum.setLayout(self.enumFormLayout)
        self.ui.lWTable.setLayout(self.tableFormLayout)
        # 临时保存模板操作页
        self.tmplType = 1
        # 缓存模板配置信息
        self.tmplsDict = None
        # 打开窗口初始化配置信息
        self.initToolSetting() 
        pass

    def initToolSetting(self):
        # tab1--工具常用配置
        protocPath, protoPath, tablePath = self.settingXml.readToolConfig()
        self.ui.lEtProtocPath.setText(protocPath)
        self.ui.lEtProtoPath.setText(protoPath)
        self.ui.lEtTablePath.setText(tablePath)
        
        # 读取配置显示所有配置模板信息
        self.tmplsDict = self.settingXml.readTmplsConfig()
        if self.tmplsDict is None or not self.tmplsDict:
            return
        protoList = self.tmplsDict[TmplType.PROTO]
        enumList = self.tmplsDict[TmplType.ENUM]
        tableList = self.tmplsDict[TmplType.TABLE]
        if protoList: self.initTmplInfo(protoList)
        if enumList: self.initTmplInfo(enumList)
        if tableList: self.initTmplInfo(tableList)

    def initTmplInfo(self, tmplList):
        for tmpl in tmplList:
            self.addTmplInfo(tmpl.name, tmpl.lang, tmpl.publish)
        pass

    def closeEvent(self, event):
        # 保存filePath配置
        protocPath = self.ui.lEtProtocPath.text()
        protoPath = self.ui.lEtProtoPath.text()
        tablePath = self.ui.lEtTablePath.text()
        self.settingXml.saveToolSetting(protocPath, protoPath, tablePath)

    def setDirPath(self, openType):
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

    def addTmplInfo(self, name, lang, publish):
        # 生成界面显示组件-QListWidget
        hBoxLayout = QtWidgets.QHBoxLayout()
        # 根据传值生成控件
        lEtTemplName = QLineEdit()
        lEtTemplName.setText(name)
        lEtTemplName.setReadOnly(True)
        lEtTemplName.setFixedWidth(150)
        lEtTmplLang = QLineEdit()
        lEtTmplLang.setText(self.tmplLang.getLang(lang))
        lEtTmplLang.setReadOnly(True)
        lEtTmplLang.setFixedWidth(60)

        bTnModify = QPushButton()
        bTnModify.setText("修改")
        bTnModify.clicked.connect(
            lambda: self.showModifyTmpl(name, lang, publish))
        bTnModify.setFixedWidth(80)
        bTnDelete = QPushButton()
        bTnDelete.setText("删除")
        bTnDelete.clicked.connect(lambda: self.deleteTmpl(name, hBoxLayout))
        bTnDelete.setFixedWidth(80)

        hBoxLayout.addWidget(lEtTemplName)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(lEtTmplLang)
        hBoxLayout.addStretch(2)
        hBoxLayout.addWidget(bTnModify)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(bTnDelete)
        
        if self.tmplType == TmplType.PROTO:
            self.protoFormLayout.addRow(hBoxLayout)
        if self.tmplType == TmplType.ENUM:
            self.enumFormLayout.addRow(hBoxLayout)
        if self.tmplType == TmplType.TABLE:
            self.tableFormLayout.addRow(hBoxLayout)

    # 追加模板信息
    def appendTmplInfo(self, name, lang, publish):
        self.addTmplInfo(name, lang, publish)
        if self.tmplType == TmplType.PROTO:
            # 添加缓存信息
            tmplList = self.tmplsDict[TmplType.PROTO]
            tmplList.append(TmplItemData(name, lang, publish))
        if self.tmplType == TmplType.ENUM:
            tmplList = self.tmplsDict[TmplType.ENUM]
            tmplList.append(TmplItemData(name, lang, publish))
        if self.tmplType == TmplType.TABLE:
            tmplList = self.tmplsDict[TmplType.TABLE]
            tmplList.append(TmplItemData(name, lang, publish))
            
        # 保存更新配置 
        print("=================================")  
        self.settingXml.saveTmplsConfig(self.tmplsDict)
        print("=================================")
    
    def showModifyTmpl(self, name, lang, publish):
        # 弹出更改窗口
        self.modifyTmplUI = ModifyTmplUI()
        self.modifyTmplUI.show()
        print("showModifyTmpl====>", name, lang, publish)
        self.modifyTmplUI.fillTmplData(name, lang, publish)
        self.modifyTmplUI.dialogSignal.connect(self.modifyTmpl)
        pass
    
    def deleteTmpl(self, name, layout):
        if self.tmplType == TmplType.PROTO:
            self.protoFormLayout.removeRow(layout)
            tmplList = self.tmplsDict[TmplType.PROTO]
            
        if self.tmplType == TmplType.ENUM:
            self.enumFormLayout.removeRow(layout)
            tmplList = self.tmplsDict[TmplType.ENUM]
        if self.tmplType == TmplType.TABLE:
            self.tableFormLayout.removeRow(layout)
            tmplList = self.tmplsDict[TmplType.TABLE]
        
        for index, tmpl in enumerate(tmplList):
            if tmpl.name == name:
                tmplList.pop(index)
            pass    
        # 保存更新配置
        self.settingXml.saveTmplsConfig(self.tmplsDict)            
        pass
    
    def modifyTmpl(self, oldName, name, lang, publish):
        if self.tmplType == TmplType.PROTO:
            tmplList = self.tmplsDict[TmplType.PROTO]
        if self.tmplType == TmplType.ENUM:
            tmplList = self.tmplsDict[TmplType.ENUM]
        if self.tmplType == TmplType.TABLE:
            tmplList = self.tmplsDict[TmplType.TABLE]
        
        for tmpl in tmplList:
            if tmpl.name == oldName:
                tmpl.name = name
                tmpl.lang = lang
                tmpl.publish = publish
        print("======================")        
        print(self.tmplsDict)
        print("======================")
        # TODO：更新界面显示
        
        # 保存更新配置
        self.settingXml.saveTmplsConfig(self.tmplsDict)
        pass
    


