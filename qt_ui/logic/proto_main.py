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

        #treeView item
        self.tRvItem = None
        

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
            self.modifyProtoUI = ModifyProtoUI()
            self.modifyProtoUI.show()
            self.modifyProtoUI.dialogSinal.connect(self.modifyProto_emit)
            pass
        if op == "delete_proto":
            pass
        if op == "create_dir":
            # 弹出添加目录名称窗口
            self.createDirUI = CreateProtoDirUI()
            self.createDirUI.show()
            self.createDirUI.dialogSinal.connect(self.createDir_emit)
            pass
        if op == "modify_dir":
            self.modifyDirUI = ModifyProtoDirUI()
            self.modifyDirUI.show()
            self.modifyDirUI.dialogSinal.connect(self.modifyDir_emit)            
            pass
        if op == "delete_dir":
            # 提示删除协议目录
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议目录? (此操作会删除目录下所有协议)')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                print("aaaaaaaaaaa")
            else:
                print("bbbbbbbbbbbb")
            pass
        pass

    def createDir_emit(self, str):
        root=QTreeWidgetItem(self.ui.tRvProtocol)
        root.setText(0,str)
        root.setIcon(0,QIcon('../../qt_ui/icons/folder.ico'))
        self.ui.tRvProtocol.addTopLevelItem(root)
        # TODO: 将目录写入xml文件

    def modifyDir_emit(self, str):
        # 遍历目录修改节点text
        self.tRvItem.setText(0,str)
        # TODO: 更新xml文件     
        pass 

    def createProto_emit(self, protoNum, protoName, protoDesc, protoContent):
        #print(protoNum, protoName, protoDesc, protoContent)

        if self.tRvItem != None:
            # 添加子节点
            item = QTreeWidgetItem()
            item.setText(0, str(protoNum)+" "+protoName)
            item.setIcon(0,QIcon('../../qt_ui/icons/TextFile.ico'))
            self.tRvItem.addChild(item)
            pass
        pass

    def modifyProto_emit(self, protoNum, protoName, protoDesc, protoContent):
        if self.tRvItem != None:
            self.tRvItem.setText(0, str(protoNum)+" "+protoName)
            # TODO: 修改xml文件内容
            pass
        pass

    def treeViewClicked(self, modelIndex):
        #print(modelIndex.data(), modelIndex.row(), modelIndex.column())
        self.tRvItem = self.ui.tRvProtocol.currentItem()
        parent = self.tRvItem.parent()
        if parent == None:
            # 选中根节点
            self.actionA.setEnabled(True)
            self.actionB.setEnabled(False)
            self.actionC.setEnabled(False)

            self.actionD.setEnabled(True)
            self.actionE.setEnabled(True)
            self.actionF.setEnabled(True)              
        else:
            # 选中子节点
            self.actionB.setEnabled(True)
            self.actionC.setEnabled(True)

            self.actionD.setEnabled(False)
            self.actionE.setEnabled(False)
            self.actionF.setEnabled(False)
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
