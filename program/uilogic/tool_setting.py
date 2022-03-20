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
from setting_xml import *
from uipy.setting_ui import *
from uilogic.add_tmpl import *
from uilogic.modify_tmpl import *
from tool_define import *

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
        self.settingXml.readSettingXml()
        self.showSettingInfo() 
        pass

    def showSettingInfo(self):
        # tab1--工具常用配置
        toolInfos = self.settingXml.getTool()
        if not toolInfos:
            return
        if not toolInfos['protoc']:
            self.ui.lEtProtocPath.setText(toolInfos['protoc'])
        if not toolInfos['proto']:
            self.ui.lEtProtoPath.setText(toolInfos['proto'])
        if not toolInfos['excel']:    
            self.ui.lEtTablePath.setText(toolInfos['excel'])
        
        # 读取配置显示所有配置模板信息
        protocolTmpls, enumTmpls, tableTmpls = self.settingXml.getTmpls()
        if protocolTmpls: self.initTmplInfo(protocolTmpls, TmplType.PROTO)
        if enumTmpls: self.initTmplInfo(enumTmpls, TmplType.ENUM)
        if tableTmpls: self.initTmplInfo(tableTmpls, TmplType.TABLE)

    def initTmplInfo(self, tmplList, tmplType):
        for tmpl in tmplList:
            self.addTmplInfo(tmpl, tmplType)
        pass

    # 配置窗口关闭保存所有配置信息    
    def closeEvent(self, event):
        protocPath = self.ui.lEtProtocPath.text().strip()
        protoPath = self.ui.lEtProtoPath.text().strip()
        excelPath = self.ui.lEtTablePath.text().strip()
        serverHosts = self.ui.tEtIPList.toPlainText()
        toolConfigData = ToolConfigData(protocPath, protoPath, excelPath, serverHosts)
        self.settingXml.updateTool(toolConfigData)
        self.settingXml.writeSettingXml()        

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
        self.addTmplUI = AddTmplUI(self)
        self.addTmplUI.show()
        self.addTmplUI.dialogSignal.connect(self.appendTmplInfo)
        pass

    def addTmplInfo(self, tmplData, tmplType):
        # 生成界面显示组件-QListWidget
        hBoxLayout = QtWidgets.QHBoxLayout()
        # 根据传值生成控件
        lEtTemplName = QLineEdit()
        lEtTemplName.setText(tmplData.name)
        lEtTemplName.setReadOnly(True)
        lEtTemplName.setFixedWidth(150)
        lEtTmplLang = QLineEdit()
        lEtTmplLang.setText(self.tmplLang.getLang(tmplData.lang))
        lEtTmplLang.setReadOnly(True)
        lEtTmplLang.setFixedWidth(60)

        bTnModify = QPushButton()
        bTnModify.setText("修改")
        bTnModify.clicked.connect(
            lambda: self.showModifyTmpl(tmplData, hBoxLayout))
        bTnModify.setFixedWidth(80)
        bTnDelete = QPushButton()
        bTnDelete.setText("删除")
        bTnDelete.clicked.connect(lambda: self.deleteTmpl(tmplData, hBoxLayout))
        bTnDelete.setFixedWidth(80)

        hBoxLayout.addWidget(lEtTemplName)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(lEtTmplLang)
        hBoxLayout.addStretch(2)
        hBoxLayout.addWidget(bTnModify)
        hBoxLayout.addStretch(1)
        hBoxLayout.addWidget(bTnDelete)
        
        if tmplType == TmplType.PROTO:
            self.protoFormLayout.addRow(hBoxLayout)
        if tmplType == TmplType.ENUM:
            self.enumFormLayout.addRow(hBoxLayout)
        if tmplType == TmplType.TABLE:
            self.tableFormLayout.addRow(hBoxLayout)

    # 追加模板信息
    def appendTmplInfo(self, tmplData):
        self.addTmplInfo(tmplData, self.tmplType)
        self.settingXml.addTmpls(tmplData, self.tmplType)
    
    def showModifyTmpl(self, tmplData, hBoxLayout):
        # 弹出更改窗口
        self.hBoxLayout = hBoxLayout
        self.modifyTmplUI = ModifyTmplUI(self)
        self.modifyTmplUI.show()
        self.modifyTmplUI.fillTmplData(tmplData)
        self.modifyTmplUI.dialogSignal.connect(self.modifyTmpl)
        pass
    
    def deleteTmpl(self, tmplData, layout):
        tmplList = self.settingXml.getTmplsByType(self.tmplType)
        
        if self.tmplType == TmplType.PROTO:
            self.protoFormLayout.removeRow(layout)
        if self.tmplType == TmplType.ENUM:
            self.enumFormLayout.removeRow(layout)
        if self.tmplType == TmplType.TABLE:
            self.tableFormLayout.removeRow(layout)

        tmplList.remove(tmplData)        
        # for index, tmpl in enumerate(tmplList):
        #     if tmpl.name == name:
        #         tmplList.pop(index)
        #     pass        
        # pass
    
    def modifyTmpl(self, oldTmplData, tmplData):
        # 更新缓存模板信息
        tmplList = self.settingXml.getTmplsByType(self.tmplType)
        tmplList.remove(oldTmplData)
        tmplList.append(tmplData)
        # 刷新界面控件
        qLetName = self.hBoxLayout.itemAt(0).widget()
        qLetName.setText(tmplData.name)
        qLetLang = self.hBoxLayout.itemAt(2).widget()
        qLetLang.setText(self.tmplLang.getLang(tmplData.lang))
        pass

