#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   proto_ui.py
@Time    :   2022/02/28 00:37:44
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   显示文件主界面
'''

# here put the import lib
import os
import sys
import multiprocessing
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.proto_tool_ui import *
from uilogic.create_dir import *
from uilogic.modify_dir import *
from uilogic.create_proto import *
from uilogic.modify_proto import *
from tool_define import *
from proto_xml import *
from uilogic.tool_setting import *
from export_pb import *
from client.net_client import *
from uilogic.create_enum import *
from uilogic.modify_enum import *


class ProtoMainUI(QMainWindow):
    def __init__(self, parent=None):
        super(ProtoMainUI, self).__init__()
        self.ui = Ui_ProtoWindow()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setWindowIcon(QtGui.QIcon('../designer/icons/Icon_.ico'))
        self.setFixedSize(self.width(), self.height())

        self.ui.tabWidget.setCurrentIndex(0)
        # treeView 设置
        self.ui.tRvProtocol.setStyle(QStyleFactory.create('windows'))
        self.ui.tRvProtocol.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tRvProtocol.clicked.connect(self.treeViewClicked)
        # 右键treeView显示菜单
        self.ui.tRvProtocol.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tRvProtocol.customContextMenuRequested.connect(self.showProtoMenu)
        self.protoMenu = QMenu(self.ui.tRvProtocol)
        self.actionA = self.protoMenu.addAction(u'创建协议')
        self.actionB = self.protoMenu.addAction(u'修改协议')
        self.actionC = self.protoMenu.addAction(u'删除协议')
        self.actionD = self.protoMenu.addAction(u'创建目录')
        self.actionE = self.protoMenu.addAction(u'修改目录')
        self.actionF = self.protoMenu.addAction(u'删除目录')
        self.actionA.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.ProtoCreate))
        self.actionB.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.ProtoModify))
        self.actionC.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.ProtoDelete))
        self.actionD.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.DirCreate))
        self.actionE.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.DirModify))
        self.actionF.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.DirDelete))
        self.setTVMenuUnEnabled()
        # 修改按钮绑定事件
        self.ui.bTnProtoModify.clicked.connect(self.modifyProtoClicked)
        # 菜单事件处理逻辑
        self.ui.menuSave.triggered.connect(self.menuSaveClicked)
        self.ui.menuExit.triggered.connect(self.menuExitClicked)
        self.ui.menuExportProto.triggered.connect(self.menuExportProtoClicked)
        self.ui.menuExportServerPb.triggered.connect(self.menuExportServerPbClicked)
        self.ui.menuOpenSetting.triggered.connect(self.menuOpenSettingClicked)
        # 协议测试
        self.ui.bTnConn.clicked.connect(self.connServer)
        self.ui.bTnDisconn.clicked.connect(self.disConnect)
        self.ui.bTnSendMsg.clicked.connect(self.sendReqMsg)
        self.ui.bTnClearResp.clicked.connect(self.clearRespTextEdit)
        # 枚举tableWidget设置
        self.ui.tBvEnum.setColumnCount(3)
        self.ui.tBvEnum.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)    
        self.ui.tBvEnum.horizontalHeader().setSectionsClickable(False)
        self.ui.tBvEnum.horizontalHeader().resizeSection(0, 80)
        self.ui.tBvEnum.horizontalHeader().resizeSection(1, 173)
        self.ui.tBvEnum.horizontalHeader().resizeSection(2, 175)
        self.ui.tBvEnum.setShowGrid(True)
        # 枚举右键菜单
        self.ui.tRvEnum.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tRvEnum.customContextMenuRequested.connect(self.showEnumMenu)        
        self.enumMenu = QMenu(self.ui.tRvEnum)
        self.actionAA = self.enumMenu.addAction(u'创建枚举')
        self.actionBB = self.enumMenu.addAction(u'修改枚举')
        self.actionCC = self.enumMenu.addAction(u'删除枚举')
        self.actionAA.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.EnumCreate))
        self.actionBB.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.EnumModify))
        self.actionCC.triggered.connect(lambda: self.treeViewActionHandler(TVMenuOpType.EnumDelete))

        # 协议搜索框
        self.ui.lEtProtoSearch.textChanged.connect(self.showSearchProtoItem)
        # 枚举搜索框
        self.ui.lEtEnumSearch.textChanged.connect(self.showSearchEnumItem)
        # 当前选中item
        self.currentItem = None

        # 客户端测试协议
        self.client = NetClient()
        # 初始化ToolProtoXml对象(TODO: 优化)
        self.protoXml = ToolProtoXml()

        # 初始化settingXml 对象
        self.exportPb = ExportPb()

        # load protocol xml 初始化treeViewItems
        self.loadProtocols()

    
    def loadProtocols(self):
        self.protoXml.readProtocolXml()
        modules = self.protoXml.getModules()
        protocols = self.protoXml.getProtocols()
        if not modules:
            print("warn:load protocol xml file, protocol==None")
            return

        self.ui.tRvProtocol.clear()
        # 根据配置信息创建item 节点
        for dirName, dirData in modules.items():
            dirItem = self.createDirItem(dirData)
            for _, protoData in protocols[dirName].items():
                protoNode = self.createProto(protoData)
                dirItem.addChild(protoNode)

        pass
        

    def showProtoMenu(self, pos):
            self.actionD.setEnabled(True)
            self.protoMenu.exec_(QCursor.pos())

    def showEnumMenu(self, pos):
            self.enumMenu.exec_(QCursor.pos())

    def treeViewActionHandler(self, op):
        if op == TVMenuOpType.ProtoCreate:
            self.createProtoUI = CreateProtoUI(self)
            self.createProtoUI.show()
            self.createProtoUI.dialogSignal.connect(self.createProto_emit)
            pass
        if op == TVMenuOpType.ProtoModify:
            self.showModifyProtoWindow()
            pass
        if op == TVMenuOpType.ProtoDelete:
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
                return 
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议?')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                parent = self.currentItem.parent()
                protoData = self.currentItem.data(0, Qt.UserRole)
                parent.removeChild(self.currentItem)
                self.currentItem = None
                self.protoXml.delProtocol(parent.text(0), protoData.id)
                self.saveProtoXml()
            pass
        if op == TVMenuOpType.DirCreate:
            self.createDirUI = CreateProtoDirUI(self)
            self.createDirUI.show()
            self.createDirUI.dialogSignal.connect(self.createDir_emit)
            pass
        if op == TVMenuOpType.DirModify:
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
                return
            self.modifyDirUI = ModifyProtoDirUI(self)
            dirData = self.currentItem.data(0, Qt.UserRole)
            self.modifyDirUI.fillDirData(dirData)
            self.modifyDirUI.show()
            self.modifyDirUI.dialogSignal.connect(self.modifyDir_emit)            
            pass
        if op == TVMenuOpType.DirDelete:
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
                return
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议目录? (此操作会删除目录下所有协议)')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                index = self.ui.tRvProtocol.indexOfTopLevelItem(self.currentItem)
                self.ui.tRvProtocol.takeTopLevelItem(index)
                dirName = self.currentItem.text(0)
                self.currentItem = None
                self.protoXml.delDir(dirName)
                self.saveProtoXml()
            pass

        if op == TVMenuOpType.EnumCreate:
            self.createEnumUI = CreateEnumUI(self)
            self.createEnumUI.show()   
            pass
        if op == TVMenuOpType.EnumModify:
            self.modifyEnumUI = ModifyEnumUI(self)
            self.modifyEnumUI.show() 
            pass
        if op == TVMenuOpType.EnumDelete:
            pass
        pass

    def createDirItem(self, dirData):
        root=QTreeWidgetItem(TVItemType.ItemDir)
        root.setText(0, dirData.dirName)
        root.setIcon(0, QIcon('../designer/icons/folder.ico'))
        root.setData(0, Qt.UserRole, dirData)

        self.ui.tRvProtocol.addTopLevelItem(root)
        return root

    def createDir_emit(self, dirData):
        if not dirData:
            return
        self.createDirItem(dirData)
        self.protoXml.addDir(dirData)
        self.saveToXml()

    def modifyDir_emit(self, dirData):
        self.currentItem.setText(0, dirData.dirName)
        self.currentItem.setData(0, Qt.UserRole, dirData)
        self.saveToXml()
        pass


    def createProto(self, protoData, dirName = None):
        item = QTreeWidgetItem(TVItemType.ItemProto)
        item.setText(0, protoData.id+"#"+protoData.name)
        item.setIcon(0, QIcon('../designer/icons/TextFile.ico'))
        item.setData(0, Qt.UserRole, protoData)
        return item    
        pass

    def createProto_emit(self, protoData):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
            return
        dirName = self.currentItem.text(0)
        item = self.createProto(protoData, dirName)
        self.currentItem.addChild(item)

        self.protoXml.addProtocol(self.currentItem.text(0), protoData)
        # 如果是创建请求类型协议，则自动生成返回协议
        protoName = protoData.name
        protoId = protoData.id
        if 'Req' in protoName:
            protoId = str(int(protoId)+1)
            protoName = protoName[0:-3]+"Ack"
            protoData = TVItemProtoData(protoId, protoName, "", "", protoData.onlyServer)
            item = self.createProto(protoData, dirName)
            self.currentItem.addChild(item)

            self.protoXml.addProtocol(self.currentItem.text(0), protoData)
            pass
        if protoData.onlyServer:
            self.ui.cBxProtocol.setChecked(True)
        else:
            self.ui.cBxProtocol.setChecked(False)
        # 保存更新信息
        self.saveProtoXml()           

    def modifyProto_emit(self, protoData):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return
        self.currentItem.setText(0, protoData.id+"#"+protoData.name)
        self.currentItem.setData(0, Qt.UserRole, protoData)
        # 更新界面显示
        self.ui.lEtProtoId.setText(protoData.id)
        self.ui.lEtProtoName.setText(protoData.name)
        self.ui.tEtProtoDesc.setText(protoData.desc)
        self.ui.tEtProtoContent.setText(protoData.content)
        if protoData.onlyServer:
            self.ui.cBxProtocol.setChecked(True)
        else:
            self.ui.cBxProtocol.setChecked(False)
        parent = self.currentItem.parent()

        self.protoXml.addProtocol(parent.text(0), protoData)
        # 保存更新信息
        self.saveProtoXml()

    def setTVMenuUnEnabled(self):
        self.actionA.setEnabled(False)
        self.actionB.setEnabled(False)
        self.actionC.setEnabled(False)
        self.actionD.setEnabled(False)
        self.actionE.setEnabled(False)
        self.actionF.setEnabled(False)

    def treeViewClicked(self):
        self.setTVMenuUnEnabled()
        self.currentItem = self.ui.tRvProtocol.currentItem()
        if self.currentItem == None:
            self.actionD.setEnabled(True)
            return

        if self.currentItem.type() == TVItemType.ItemDir:
            # 选中根节点
            self.actionA.setEnabled(True)

            self.actionD.setEnabled(True)
            self.actionE.setEnabled(True)
            self.actionF.setEnabled(True)

        if self.currentItem.type() == TVItemType.ItemProto:
            # 选中子节点
            self.actionB.setEnabled(True)
            self.actionC.setEnabled(True)

            # 进行界面赋值
            protoData = self.currentItem.data(0, Qt.UserRole)
            self.ui.lEtProtoId.setText(protoData.id)
            self.ui.lEtProtoName.setText(protoData.name)
            self.ui.tEtProtoDesc.setText(protoData.desc)
            self.ui.tEtProtoContent.setText(protoData.content)
            self.ui.cBxProtocol.setChecked(bool(protoData))
        pass  

    def saveProtoXml(self):
        self.protoXml.writeProtocolXml()

    def saveToXml(self):
        # 保存protocol信息
        self.saveProtoXml()
        # 保存enum信息
        # 保存配置信息        
        pass

    def showModifyProtoWindow(self):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return          
        self.modifyProtoUI = ModifyProtoUI(self)
        protoData = self.currentItem.data(0, Qt.UserRole)
        self.modifyProtoUI.fillProtoData(protoData)
        self.modifyProtoUI.show()
        self.modifyProtoUI.dialogSignal.connect(self.modifyProto_emit)

    # 菜单点击触发功能
    def modifyProtoClicked(self):
        self.showModifyProtoWindow()  
        pass

    def menuSaveClicked(self):
        self.saveToXml()
        pass

    def menuExitClicked(self):
        self.saveToXml()
        self.close()
        pass

    def menuExportProtoClicked(self):
        self.protoXml.exportProtoFile()
        pass

    # 导出serverPb
    def menuExportServerPbClicked(self):
        self.exportPb.exportPb()
        
    def menuExportServerProtoClicked(self):

        pass

    def menuOpenSettingClicked(self):
        self.toolSettingUI = ToolSettingUI()
        self.toolSettingUI.show()    
        pass

    # 程序界面退出    
    def closeEvent(self, event):
        # 程序退出保存信息
        self.saveToXml()
        print("program exit")

    # 协议测试处理逻辑
    def connServer(self):
        ip = self.ui.cBbxServAddr.currentText()
        port = self.ui.sBxPort.value()
        result = self.client.connServer(ip, port)
        if not result:
            QMessageBox.information(self, "信息", "连接服务器失败")
            return

        palette = self.ui.bTnConn.palette()
        palette.setColor(QtGui.QPalette.ButtonText , QtCore.Qt.green)
        self.ui.bTnConn.setPalette(palette)
        self.ui.bTnConn.setAutoFillBackground(True)
        pass

    def disConnect(self):
        self.client.disConnect()

        palette = self.ui.bTnConn.palette()
        palette.setColor(QtGui.QPalette.ButtonText , QtCore.Qt.black)
        self.ui.bTnConn.setPalette(palette)
        self.ui.bTnConn.setAutoFillBackground(True)        
        pass

    def sendReqMsg(self):
        # 获取填写请求数据 json
        # 将json转换成pb
        # 将消息发送给服务器
        pass

    def clearRespTextEdit(self):
        self.ui.tEtResp.setText("")
        pass
    
    def showSearchProtoItem(self, filter):
        filter = filter.lower()
        if filter != "":
            for i in range(self.ui.tRvProtocol.topLevelItemCount()):
                topItem = self.ui.tRvProtocol.topLevelItem(i)
                isHidden = True
                if topItem.text(0).lower().find(filter) > 0:
                    topItem.setExpanded(True)
                    topItem.setHidden(False)
                    isHidden = False
                for j in range(topItem.childCount()):
                    childItem = topItem.child(j)
                    if childItem.text(0).lower().find(filter) > 0:
                        childItem.setHidden(False)
                        isHidden = False
                    else:
                        childItem.setHidden(True)
                if isHidden:
                    topItem.setHidden(isHidden)
            pass            
        else:
            for i in range(self.ui.tRvProtocol.topLevelItemCount()):
                topItem = self.ui.tRvProtocol.topLevelItem(i)
                topItem.setHidden(False)
                for j in range(topItem.childCount()):
                    childItem = topItem.child(j)
                    childItem.setHidden(False)
            pass
        pass

    def showSearchEnumItem(self, filter):
        filter = filter.lower()
        if filter != "":
            iter = QTreeWidgetItemIterator(self.ui.tRvProtocol)
            while iter.value():
                item = iter.value()
                if item.text(0).lower().find(filter) > 0:
                    item.setExpanded(True)
                    item.setHidden(False)
                    if item.parent():
                        item.parent().setHidden(False)
                        item.parent().setExpanded(True)
                        item = item.parent()
                        pass
                    pass
                else:
                    item.setHidden(True)
                iter.__iadd__(1)
                pass
            pass
        else:
            iter = QTreeWidgetItemIterator(self.ui.tRvProtocol)
            while iter.value():
                item = iter.value()
                item.setHidden(False)
                item.setExpanded(False)
                iter.__iadd__(1)
            pass

def ShowWindow():
    app = QApplication(sys.argv)
    mainWindow = ProtoMainUI()
    mainWindow.show()

    app.setStyle(QStyleFactory.create("Fusion"))
    app.setAttribute(QtCore.Qt.AA_NativeWindows)
    app.setAttribute(QtCore.Qt.AA_MSWindowsUseDirect3DByDefault)

    multiprocessing.freeze_support()
    sys.exit(app.exec_())
