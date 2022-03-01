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
        self.actionB.setEnabled(False)
        self.actionC.setEnabled(False)
        

    def showTreeViewMenu(self, pos):
            self.contextMenu.exec_(QCursor.pos())
    
    def treeViewActionHandler(self, op):
        if op == "create_proto":
            pass
        if op == "modify_proto":
            pass
        if op == "delete_proto":
            pass
        if op == "create_dir":
            # 弹出添加目录名称窗口
            self.createDirUI = CreateProtoDirUI()
            self.createDirUI.show()
            # root=QTreeWidgetItem(self.ui.tRvProtocol)
            # root.setText(0,'Root')
            # root.setIcon(0,QIcon('../../qt_ui/icons/folder.ico'))
            # self.ui.tRvProtocol.addTopLevelItem(root)

            # child=QTreeWidgetItem()
            # child.setText(0,'Child')
            # root.addChild(child)
            pass
        if op == "modify_dir":
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
        
        
def ShowWindow():
    app = QApplication(sys.argv)
    mainWindow = ProtoMainUI()
    mainWindow.show()

    app.setStyle(QStyleFactory.create("Fusion"))
    app.setAttribute(QtCore.Qt.AA_NativeWindows)
    app.setAttribute(QtCore.Qt.AA_MSWindowsUseDirect3DByDefault)
    
    multiprocessing.freeze_support()
    sys.exit(app.exec_())
