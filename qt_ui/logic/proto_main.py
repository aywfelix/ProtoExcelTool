#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   proto_ui.py
@Time    :   2022/02/28 00:37:44
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   None
'''

# here put the import lib
import os
import sys
import multiprocessing
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from qt_ui.uipy.proto_tool_ui import *
from qt_ui.logic.create_proto_dir import *
from qt_ui.logic.modify_proto_dir import *
from qt_ui.logic.create_proto import *
from qt_ui.logic.modify_proto import *
from qt_ui.logic.tool_define import *
from qt_ui.logic.tool_xml import *


class ProtoMainUI(QMainWindow):
    def __init__(self, parent=None):
        super(ProtoMainUI, self).__init__()
        self.ui = Ui_ProtoWindow()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setWindowIcon(QtGui.QIcon('../../qt_ui/icons/Icon_.ico'))
        self.setFixedSize(self.width(), self.height())
        # treeView 设置
        self.ui.tRvProtocol.setStyle(QStyleFactory.create('windows'))
        self.ui.tRvProtocol.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tRvProtocol.clicked.connect(self.treeViewClicked)
        # 右键treeView显示菜单
        self.ui.tRvProtocol.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.tRvProtocol.customContextMenuRequested.connect(self.showTreeViewMenu)
        self.contextMenu = QMenu(self.ui.tRvProtocol)
        self.actionA = self.contextMenu.addAction(u'创建协议')
        self.actionB = self.contextMenu.addAction(u'修改协议')
        self.actionC = self.contextMenu.addAction(u'删除协议')
        self.actionD = self.contextMenu.addAction(u'创建目录')
        self.actionE = self.contextMenu.addAction(u'修改目录')
        self.actionF = self.contextMenu.addAction(u'删除目录')
        self.actionA.triggered.connect(lambda: self.treeViewActionHandler("create_proto"))
        self.actionB.triggered.connect(lambda: self.treeViewActionHandler("modify_proto"))
        self.actionC.triggered.connect(lambda: self.treeViewActionHandler("delete_proto"))
        self.actionD.triggered.connect(lambda: self.treeViewActionHandler("create_dir"))
        self.actionE.triggered.connect(lambda: self.treeViewActionHandler("modify_dir"))
        self.actionF.triggered.connect(lambda: self.treeViewActionHandler("delete_dir"))
        self.actionA.setEnabled(False)
        self.actionB.setEnabled(False)
        self.actionC.setEnabled(False)

        # 修改按钮绑定事件
        self.ui.bTnProtoModify.clicked.connect(self.modifyProtoClicked)
        # 菜单事件处理逻辑
        self.ui.menuSave.triggered.connect(self.menuSaveClicked)
        self.ui.menuExit.triggered.connect(self.menuExitClicked)
        self.ui.menuExportProto.triggered.connect(self.menuExportProtoClicked)
        self.ui.menuExportServerPb.triggered.connect(self.menuExportServerPbClicked)

        # 当前选中item
        self.currentItem = None

        # 初始化ToolProtoXml对象(TODO: 优化)
        self.protoXml = ToolProtoXml()
        self.protoXml.setProtoConfig("../../config/protocols.config")
        self.protoXml.exportProtoPath("../../proto_tool/protos")
        # load protocol xml 初始化treeViewItems
        self.loadProtocols()

    
    def loadProtocols(self):
        protocolDict = self.protoXml.readProtocolXml()
        if protocolDict is None:
            print("load protocol xml file err")
            return

        self.ui.tRvProtocol.clear()
        # 根据配置信息创建item 节点
        for dirName, protocolList in protocolDict.items():
            dirNode = self.createDir(dirName)
            for protocol in protocolList:
                protoNode = self.createProto(protocol.id, protocol.name, protocol.desc, protocol.content, protocol.onlyServer)
                dirNode.addChild(protoNode)
            self.ui.tRvProtocol.addTopLevelItem(dirNode)
        pass
        

    def showTreeViewMenu(self, pos):
            self.contextMenu.exec_(QCursor.pos())
    
    def treeViewActionHandler(self, op):
        if op == "create_proto":
            # 弹出创建协议窗口
            self.createProtoUI = CreateProtoUI()
            self.createProtoUI.show()
            self.createProtoUI.dialogSinal.connect(self.createProto_emit)
            pass
        if op == "modify_proto":
            self.showModifyProtoWindow()
            pass
        if op == "delete_proto":
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
                return 
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议?')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                parent = self.currentItem.parent()
                parent.removeChild(self.currentItem)
                self.currentItem = None
            pass
        if op == "create_dir":
            # 弹出添加目录名称窗口
            self.createDirUI = CreateProtoDirUI()
            self.createDirUI.show()
            self.createDirUI.dialogSinal.connect(self.createDir_emit)
            pass
        if op == "modify_dir":
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
                return
            self.modifyDirUI = ModifyProtoDirUI()
            self.modifyDirUI.show()
            self.modifyDirUI.dialogSinal.connect(self.modifyDir_emit)            
            pass
        if op == "delete_dir":
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
                return
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议目录? (此操作会删除目录下所有协议)')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                index = self.ui.tRvProtocol.indexOfTopLevelItem(self.currentItem)
                self.ui.tRvProtocol.takeTopLevelItem(index)
                self.currentItem = None
            pass
        pass

    def createDir(self, dirName):
        root=QTreeWidgetItem(TVItemType.ItemDir)
        root.setText(0,dirName)
        root.setIcon(0,QIcon('../../qt_ui/icons/folder.ico'))
        return root
        

    def createDir_emit(self, dirName):
        root = self.createDir(dirName)
        self.ui.tRvProtocol.addTopLevelItem(root)

    def modifyDir_emit(self, str):
        # 遍历目录修改节点text
        self.currentItem.setText(0,str)
        # TODO: 更新xml文件     
        pass

    def createProto(self, protoId, protoName, protoDesc, protoContent, onlyServer=False):
        # 添加子节点
        item = QTreeWidgetItem(TVItemType.ItemProto)
        item.setText(0, protoId+" "+protoName)
        item.setIcon(0, QIcon('../../qt_ui/icons/TextFile.ico'))
        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, onlyServer)
        item.setData(0, Qt.ItemDataRole.UserRole, protoData)
        return item

    def createProto_emit(self, protoId, protoName, protoDesc, protoContent, onlyServer):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
            return
        item = self.createProto(protoId, protoName, protoDesc, protoContent, onlyServer)
        self.currentItem.addChild(item)

    def modifyProto_emit(self, protoId, protoName, protoDesc, protoContent, onlyServer):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return
        self.currentItem.setText(0, protoId+" "+protoName)
        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, onlyServer)
        self.currentItem.setData(0, Qt.ItemDataRole.UserRole, protoData)
        newData = self.currentItem.data(0, Qt.ItemDataRole.UserRole)
        print(newData)

    def treeViewClicked(self):
        self.currentItem = self.ui.tRvProtocol.currentItem()
        if self.currentItem == None:
            self.actionA.setEnabled(False)
            self.actionD.setEnabled(True)
            return

        if self.currentItem.type() == TVItemType.ItemDir:
            # 选中根节点
            self.actionA.setEnabled(True)
            self.actionB.setEnabled(False)
            self.actionC.setEnabled(False)

            self.actionD.setEnabled(True)
            self.actionE.setEnabled(True)
            self.actionF.setEnabled(True)

        if self.currentItem.type() == TVItemType.ItemProto:
            # 选中子节点
            self.actionA.setEnabled(False)
            self.actionB.setEnabled(True)
            self.actionC.setEnabled(True)

            self.actionD.setEnabled(True)
            self.actionE.setEnabled(False)
            self.actionF.setEnabled(False)

            # 进行界面赋值
            protoData = self.currentItem.data(0, Qt.ItemDataRole.UserRole)
            self.ui.lEtProtoId.setText(protoData.id)
            self.ui.lEtProtoName.setText(protoData.name)
            self.ui.tEtProtoDesc.setText(protoData.desc)
            self.ui.tEtProtoContent.setText(protoData.content)
            self.ui.cBxProtocol.setChecked(bool(protoData))
                 
        pass  

    def saveToXml(self):
        # 保存proto信息
        # 获取treeview 所有节点data
        protocolsDict = {}
        topItemCount = self.ui.tRvProtocol.topLevelItemCount()
        for i in range(0, topItemCount):
            topItem = self.ui.tRvProtocol.topLevelItem(i)
            protocolList = []
            print(topItem.text(0))
            # 遍历topItem 下所有子节点
            childItemCount = topItem.childCount()
            for j in range(0, childItemCount):
                childItem = topItem.child(j)
                protoData = childItem.data(0, Qt.ItemDataRole.UserRole)
                protocolList.append(protoData)
                print(protoData)

            protocolsDict[topItem.text(0)] = protocolList

        self.protoXml.writeProtocolXml(protocolsDict)
        # 保存enum信息
        # 保存配置信息
        pass

    def showModifyProtoWindow(self):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return          
        self.modifyProtoUI = ModifyProtoUI()
        protoData = self.currentItem.data(0, Qt.ItemDataRole.UserRole)
        self.modifyProtoUI.fillProtoData(protoData)
        self.modifyProtoUI.show()
        self.modifyProtoUI.dialogSinal.connect(self.modifyProto_emit)

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
        # 根据xml文件导出proto文件
        self.protoXml.exportProtoFile()
        pass

    def menuExportServerPbClicked(self):
        self.protoXml.exportProtoPb()
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
