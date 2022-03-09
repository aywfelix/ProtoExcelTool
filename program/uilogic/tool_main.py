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
from email.charset import QP
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

# treeview右键菜单操作
class TVMenuOpType(object):
    DirCreate = 1
    DirModify = 2
    DirDelete = 3
    ProtoCreate = 4
    ProtoModify = 5
    ProtoDelete = 6

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
        self.ui.tRvProtocol.customContextMenuRequested.connect(self.showTreeViewMenu)
        self.contextMenu = QMenu(self.ui.tRvProtocol)
        self.actionA = self.contextMenu.addAction(u'创建协议')
        self.actionB = self.contextMenu.addAction(u'修改协议')
        self.actionC = self.contextMenu.addAction(u'删除协议')
        self.actionD = self.contextMenu.addAction(u'创建目录')
        self.actionE = self.contextMenu.addAction(u'修改目录')
        self.actionF = self.contextMenu.addAction(u'删除目录')
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
        
        # 当前选中item
        self.currentItem = None

        # 客户端测试协议
        self.client = NetClient()
        # 初始化ToolProtoXml对象(TODO: 优化)
        self.protoXml = ToolProtoXml()
        self.protoXml.setProtoConfig("./config/protocols.config")

        # 初始化settingXml 对象
        self.exportPb = ExportPb()
        # TODO:缓存协议编号
        # load protocol xml 初始化treeViewItems
        self.loadProtocols()

    
    def loadProtocols(self):
        protocols = self.protoXml.readProtocolXml()
        if protocols is None or not protocols:
            print("warn:load protocol xml file, protocol==None")
            return

        self.ui.tRvProtocol.clear()
        # 根据配置信息创建item 节点
        for module in protocols:
            dirData = module["module"]
            protoDataList = module["protocol"]
            dirItem = self.createDirItem(dirData)

            self.ui.tRvProtocol.addTopLevelItem(dirItem)
            for protoData in protoDataList:
                protoNode = self.createProto(protoData.id, protoData.name, protoData.desc, protoData.content, protoData.onlyServer)
                dirItem.addChild(protoNode)
        pass
        

    def showTreeViewMenu(self, pos):
            self.actionD.setEnabled(True)
            self.contextMenu.exec_(QCursor.pos())
    
    def treeViewActionHandler(self, op):
        if op == TVMenuOpType.ProtoCreate:
            self.createProtoUI = CreateProtoUI()
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
                parent.removeChild(self.currentItem)
                self.currentItem = None
            pass
        if op == TVMenuOpType.DirCreate:
            self.createDirUI = CreateProtoDirUI()
            self.createDirUI.show()
            self.createDirUI.dialogSignal.connect(self.createDir_emit)
            pass
        if op == TVMenuOpType.DirModify:
            if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
                return
            self.modifyDirUI = ModifyProtoDirUI()
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
                self.currentItem = None
                self.saveToXml()
            pass
        pass

    def createDirItem(self, dirData):
        root=QTreeWidgetItem(TVItemType.ItemDir)
        root.setText(0,dirData.dirName)
        root.setIcon(0,QIcon('../designer/icons/folder.ico'))
        root.setData(0, Qt.UserRole, dirData)
        return root
        
    def checkCreateDir(self, dirName):
        topItemCount = self.ui.tRvProtocol.topLevelItemCount()
        for i in range(0, topItemCount):
            topItem = self.ui.tRvProtocol.topLevelItem(i)
            if topItem.text(0) == dirName:
                return False

        return True

    def createDir_emit(self, dirName, package):
        if not self.checkCreateDir(dirName):
            return

        dirData = TVItemDirData(dirName, package)
        root = self.createDirItem(dirData)
        self.ui.tRvProtocol.addTopLevelItem(root)

    def modifyDir_emit(self, dirName, package):
        self.currentItem.setText(0, dirName)
        dirData = TVItemDirData(dirName, package)
        self.currentItem.setData(0, Qt.UserRole, dirData)
        pass

    # TODO:临时解决方案
    def checkCreateProto(self, protoId, protoName):
        topItemCount = self.ui.tRvProtocol.topLevelItemCount()
        for i in range(0, topItemCount):
            topItem = self.ui.tRvProtocol.topLevelItem(i)
            # 遍历topItem 下所有子节点
            childItemCount = topItem.childCount()
            for j in range(0, childItemCount):
                childItem = topItem.child(j)
                protoData = childItem.data(0, Qt.UserRole)
                if protoData.id == protoId or protoName == protoData.name:
                    return False

        return True

    def createProto(self, protoId, protoName, protoDesc, protoContent, onlyServer=False):
        # 添加子节点
        item = QTreeWidgetItem(TVItemType.ItemProto)
        item.setText(0, protoId+"#"+protoName)
        item.setIcon(0, QIcon('../designer/icons/TextFile.ico'))
        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, onlyServer)
        item.setData(0, Qt.UserRole, protoData)
        return item

    def createProto_emit(self, protoId, protoName, protoDesc, protoContent, onlyServer):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemDir:
            return
        # 检测协议编号是否已经存在，如果存在弹出警告
        if not self.checkCreateProto(protoId, protoName):
            QMessageBox.critical(self, "错误", "协议编号已经被使用!!!")
            return

        item = self.createProto(protoId, protoName, protoDesc, protoContent, onlyServer)
        self.currentItem.addChild(item)
        # 如果是创建请求类型协议，则自动生成返回协议
        if 'Req' in protoName:
            protoId = str(int(protoId)+1)
            protoName = protoName[0:-3]+"Resp"
            item = self.createProto(protoId, protoName, "", "", False)
            self.currentItem.addChild(item)
            pass

    def modifyProto_emit(self, protoId, protoName, protoDesc, protoContent, onlyServer):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return
        self.currentItem.setText(0, protoId+"#"+protoName)
        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, onlyServer)
        self.currentItem.setData(0, Qt.UserRole, protoData)
        newData = self.currentItem.data(0, Qt.UserRole)
        # 更新界面显示
        self.ui.lEtProtoId.setText(protoId)
        self.ui.lEtProtoName.setText(protoName)
        self.ui.tEtProtoDesc.setText(protoDesc)
        self.ui.tEtProtoContent.setText(protoContent)
        # 保存更新信息
        self.saveToXml()
        print(newData)

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

    def saveToXml(self):
        # 保存proto信息
        # 获取treeview 所有节点data
        protocols = []
        topItemCount = self.ui.tRvProtocol.topLevelItemCount()
        for i in range(0, topItemCount):
            moduleDict = {}
            topItem = self.ui.tRvProtocol.topLevelItem(i)
            dirData = topItem.data(0, Qt.UserRole)
            moduleDict["module"] = dirData
            protocolList = []
            # 遍历topItem 下所有子节点
            childItemCount = topItem.childCount()
            for j in range(0, childItemCount):
                childItem = topItem.child(j)
                protoData = childItem.data(0, Qt.UserRole)
                protocolList.append(protoData)

            moduleDict["protocol"] = protocolList
            protocols.append(moduleDict)

        self.protoXml.writeProtocolXml(protocols)
        # 保存enum信息
        # 保存配置信息
        pass

    def showModifyProtoWindow(self):
        if self.currentItem == None or self.currentItem.type() != TVItemType.ItemProto:
            return          
        self.modifyProtoUI = ModifyProtoUI()
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
        
def ShowWindow():
    app = QApplication(sys.argv)
    mainWindow = ProtoMainUI()
    mainWindow.show()

    app.setStyle(QStyleFactory.create("Fusion"))
    app.setAttribute(QtCore.Qt.AA_NativeWindows)
    app.setAttribute(QtCore.Qt.AA_MSWindowsUseDirect3DByDefault)

    multiprocessing.freeze_support()
    sys.exit(app.exec_())
