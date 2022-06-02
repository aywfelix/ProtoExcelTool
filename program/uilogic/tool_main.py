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
import enum
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
from export.export_pb import *
from export.export_enum import *
from client.net_client import *
from uilogic.create_enum import *
from uilogic.modify_enum import *
from transtable.trans_table import *

class ProtoMainUI(QMainWindow):
    def __init__(self, parent=None):
        super(ProtoMainUI, self).__init__()
        self.ui = Ui_GameToolWindow()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setWindowIcon(QtGui.QIcon('./images/program.ico'))
        self.setFixedSize(self.width(), self.height())

        #tabWidget 
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.tabWidget.currentChanged['int'].connect(self.tabWidgetChanged)
        # treeView 设置
        self.ui.tRvProtocol.setStyle(QStyleFactory.create('windows'))
        self.ui.tRvProtocol.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tRvProtocol.clicked.connect(self.protoTreeViewClicked)
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
        self.actionA.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.ProtoCreate))
        self.actionB.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.ProtoModify))
        self.actionC.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.ProtoDelete))
        self.actionD.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.DirCreate))
        self.actionE.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.DirModify))
        self.actionF.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.DirDelete))
        self.setTVMenuUnEnabled()
        # 协议修改按钮绑定事件
        self.ui.bTnProtoModify.clicked.connect(self.modifyProtoClicked)
        # 枚举修改按钮绑定事件
        self.ui.bTnEnumModify.clicked.connect(self.modifyEnumClicked)
        # 主界面几个常用按钮绑定事件
        self.ui.btnExportPb.clicked.connect(self.exportPbClicked)
        self.ui.btnExportEnum.clicked.connect(self.exportEnumClicked)
        self.ui.btnExportTable.clicked.connect(self.exportTableClicked)
        self.ui.btnSetting.clicked.connect(self.openSettingClicked)
        # 协议测试
        self.ui.bTnConn.clicked.connect(self.connServerClicked)
        self.ui.bTnDisconn.clicked.connect(self.disConnectClicked)
        # 协议测试发送消息按钮
        self.ui.bTnSendMsg.clicked.connect(self.sendProtoMsgClicked)
        # 枚举tableWidget设置
        self.ui.tRvEnum.setStyle(QStyleFactory.create('windows'))
        self.ui.tRvEnum.clicked.connect(self.enumTreeViewClicked)
        self.ui.tBvEnum.setColumnCount(3)
        self.ui.tBvEnum.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tBvEnum.horizontalHeader().setSectionsClickable(False)
        self.ui.tRvEnum.setSelectionMode(QAbstractItemView.SingleSelection)
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
        self.actionAA.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.EnumCreate))
        self.actionBB.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.EnumModify))
        self.actionCC.triggered.connect(
            lambda: self.treeViewActionHandler(TVMenuOpType.EnumDelete))

        # 协议搜索框
        self.ui.lEtProtoSearch.textChanged.connect(self.showSearchProtoItem)
        # 枚举搜索框
        self.ui.lEtEnumSearch.textChanged.connect(self.showSearchEnumItem)
        # proto当前选中item
        self.protoCurItem = None
        # enum当前选中item
        self.enumCurItem = None        
        # 客户端测试协议
        self.client = NetClient()
        # 初始化ToolProtoXml对象(TODO: 优化)
        self.protoXml = ToolProtoXml()
        # 初始化ToolEnumXml对象
        self.enumXml = ToolEnumXml()
        # 初始化settingXml 对象
        self.settingXml = ToolSettingXml()

        # 初始化导出配置表对象
        self.exportPb = ExportPb()
        self.transTable = TransTable()

        # load protocol xml 初始化treeViewItems
        self.loadProtocols()
        # 刷新协议测试
        self.refreshProtoComboBox()
        self.client.ShowMsgSignal.connect(self.showRespMsg_emit)
        self.client.ConnServerSignal.connect(self.reConnectServer_emit)
        # load enum xml
        self.loadEnums()

        # 设置协议测试界面
        self.ui.cbBxMsgClass.currentIndexChanged[str].connect(self.cbBxMsgClassChanged)
        self.ui.cBbxProto.currentIndexChanged[str].connect(self.cBbxProtoChange)
        self.showProtoTest()

    def tabWidgetChanged(self, index):
        if index == 2:
            self.refreshConnHosts()
            self.refreshProtoComboBox()
    
    def setProtoTestReqData(self):
        curText = self.ui.cBbxProto.currentText()
        if not curText:
            return
        _, msgID = curText.strip().split(':')
        reqData = self.client.getReqHistory(msgID)
        if reqData:
            self.ui.tEtReq.setText(reqData)
        else:
            self.ui.tEtReq.setText('')
        pass

    def showProtoTest(self):
        self.setProtoTestReqData()
        pass

    def cBbxProtoChange(self):
        self.setProtoTestReqData()
        pass

    def cbBxProtoRefresh(self):
        curText = self.ui.cbBxMsgClass.currentText()
        if not curText:
            return        
        self.ui.cBbxProto.clear()
        protocols = self.protoXml.getModuleProtos(curText)
        for _, protoData in protocols.items():
            if protoData.type != '1': continue
            msgName = protoData.name
            msgId = protoData.id
            self.ui.cBbxProto.addItem("{0}:{1}".format(msgName, msgId))
        pass

    def cbBxMsgClassChanged(self):
        self.cbBxProtoRefresh()

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

    def refreshConnHosts(self):
        self.ui.cBbxServAddr.clear()
        ipList = self.settingXml.getTool()['hosts']
        for ip in ipList:
            self.ui.cBbxServAddr.addItem(ip)   
        pass

    def refreshProtoComboBox(self):
        self.ui.cbBxMsgClass.clear()
        self.ui.cBbxProto.clear()

        protocols = self.protoXml.getProtocols()
        for msgClass, _ in protocols.items():
            self.ui.cbBxMsgClass.addItem(msgClass)
        self.cbBxProtoRefresh()
        pass


    def loadEnums(self):
        self.enumXml.readEnumXml()
        enumDatas = self.enumXml.getDatas()
        if not enumDatas:
            return
        self.ui.tRvEnum.clear()
        for enumName, _ in enumDatas.items():
            self.createEnumItem(enumName)
            pass
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
            if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemProto:
                return
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除协议?')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                parent = self.protoCurItem.parent()
                protoData = self.protoCurItem.data(0, Qt.UserRole)
                parent.removeChild(self.protoCurItem)
                self.protoCurItem = None
                self.protoXml.delProtocol(parent.text(0), protoData.uuid)
                self.saveProtoXml()
            pass
        if op == TVMenuOpType.DirCreate:
            self.createDirUI = CreateProtoDirUI(self)
            self.createDirUI.show()
            self.createDirUI.dialogSignal.connect(self.createDir_emit)
            pass
        if op == TVMenuOpType.DirModify:
            if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemDir:
                return
            self.modifyDirUI = ModifyProtoDirUI(self)
            dirData = self.protoCurItem.data(0, Qt.UserRole)
            self.modifyDirUI.fillDirData(dirData)
            self.modifyDirUI.show()
            self.modifyDirUI.dialogSignal.connect(self.modifyDir_emit)
            pass
        if op == TVMenuOpType.DirDelete:
            if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemDir:
                return
            msgBox = QMessageBox(QMessageBox.Warning, u'提示',
                                 u'确认删除协议目录? (此操作会删除目录下所有协议)')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                index = self.ui.tRvProtocol.indexOfTopLevelItem(
                    self.protoCurItem)
                self.ui.tRvProtocol.takeTopLevelItem(index)
                dirName = self.protoCurItem.text(0)
                self.protoCurItem = None
                self.protoXml.delDir(dirName)
                result = self.protoXml.writeProtocolXml()
                if result is not None:
                    self.ui.statusbar.showMessage(result)
            pass

        if op == TVMenuOpType.EnumCreate:
            self.createEnumUI = CreateEnumUI(self)
            self.createEnumUI.show()
            self.createEnumUI.dialogSignal.connect(self.createEnum_emit)
            pass
        if op == TVMenuOpType.EnumModify:
            self.showModifyEnumWindow()
            pass
        if op == TVMenuOpType.EnumDelete:
            if self.enumCurItem == None:
                return
            msgBox = QMessageBox(QMessageBox.Warning, u'提示', u'确认删除枚举目录?')
            yes = msgBox.addButton(u'确定', QMessageBox.YesRole)
            no = msgBox.addButton(u'取消', QMessageBox.NoRole)
            msgBox.exec_()
            if msgBox.clickedButton() == yes:
                index = self.ui.tRvEnum.indexOfTopLevelItem(self.enumCurItem)
                self.ui.tRvEnum.takeTopLevelItem(index)
                enumName = self.enumCurItem.text(0)
                self.enumCurItem = None
                self.enumXml.delData(enumName)
            pass
        pass

    def createDirItem(self, dirData):
        topItem = QTreeWidgetItem(TVItemType.ItemDir)
        topItem.setText(0, dirData.dirName)
        topItem.setIcon(0, QIcon('./images/folder.ico'))
        topItem.setData(0, Qt.UserRole, dirData)

        self.ui.tRvProtocol.addTopLevelItem(topItem)
        return topItem

    def createDir_emit(self, dirData):
        if not dirData:
            return
        self.createDirItem(dirData)
        self.protoXml.addDir(dirData)
        self.saveToXml()

    def modifyDir_emit(self, dirData):
        self.protoCurItem.setText(0, dirData.dirName)
        self.protoCurItem.setData(0, Qt.UserRole, dirData)
        self.protoXml.modDir(dirData)
        self.saveToXml()
        pass

    def createProto(self, protoData, dirName=None):
        item = QTreeWidgetItem(TVItemType.ItemProto)
        item.setText(0, protoData.id+"#"+protoData.name)
        item.setIcon(0, QIcon('./images/file.ico'))
        item.setData(0, Qt.UserRole, protoData)
        return item
        pass

    def createProto_emit(self, protoData):
        if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemDir:
            return
        dirName = self.protoCurItem.text(0)
        item = self.createProto(protoData, dirName)
        self.protoCurItem.addChild(item)

        self.protoXml.addProtocol(self.protoCurItem.text(0), protoData)
        # 如果是创建请求类型协议，则自动生成返回协议
        protoName = protoData.name
        protoId = protoData.id

        if 'Req' in protoName:
            protoId = str(int(protoId)+1)
            protoName = protoName[0:-3]+"Ack"
            protoData = TVItemProtoData(protoId, protoName, "", "", ProtocolType.ACK)
            item = self.createProto(protoData, dirName)
            self.protoCurItem.addChild(item)

            self.protoXml.addProtocol(self.protoCurItem.text(0), protoData)
            pass
        # 保存更新信息
        self.saveProtoXml()

    def modifyProto_emit(self, protoData):
        if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemProto:
            return
        self.protoCurItem.setText(0, protoData.id+"#"+protoData.name)
        self.protoCurItem.setData(0, Qt.UserRole, protoData)
        # 更新界面显示
        self.ui.lEtProtoId.setText(protoData.id)
        self.ui.lEtProtoName.setText(protoData.name)
        self.ui.tEtProtoDesc.setText(protoData.desc)
        self.ui.tEtProtoContent.setText(protoData.content)

        parent = self.protoCurItem.parent()

        self.protoXml.addProtocol(parent.text(0), protoData)
        # 保存更新信息
        self.saveProtoXml()
        
    def modifyEnum_emit(self, enumData):
        self.enumCurItem.setText(0, enumData.name)
        # 更新界面显示
        self.rightShowEnumInfo(enumData)
        pass

    def setTVMenuUnEnabled(self):
        self.actionA.setEnabled(False)
        self.actionB.setEnabled(False)
        self.actionC.setEnabled(False)
        self.actionD.setEnabled(False)
        self.actionE.setEnabled(False)
        self.actionF.setEnabled(False)

    def protoTreeViewClicked(self):
        self.setTVMenuUnEnabled()
        self.protoCurItem = self.ui.tRvProtocol.currentItem()
        if self.protoCurItem == None:
            self.actionD.setEnabled(True)
            return

        if self.protoCurItem.type() == TVItemType.ItemDir:
            # 选中根节点
            self.actionA.setEnabled(True)

            self.actionD.setEnabled(True)
            self.actionE.setEnabled(True)
            self.actionF.setEnabled(True)

        if self.protoCurItem.type() == TVItemType.ItemProto:
            # 选中子节点
            self.actionB.setEnabled(True)
            self.actionC.setEnabled(True)

            # 进行界面赋值
            protoData = self.protoCurItem.data(0, Qt.UserRole)
            self.ui.lEtProtoId.setText(protoData.id)
            self.ui.lEtProtoName.setText(protoData.name)
            self.ui.tEtProtoDesc.setText(protoData.desc)
            self.ui.tEtProtoContent.setText(protoData.content)
        pass

    # tableWidget显示数据
    def fillEnumTableWidgetData(self, enumData):
        # 删除所有的Items
        rowCount = self.ui.tBvEnum.rowCount()
        for row in range(0, rowCount)[::-1]:
            self.ui.tBvEnum.removeRow(row)
        row = 0
        for field in enumData.fields:
            self.ui.tBvEnum.insertRow(row)
            # 索引
            indexItem = QTableWidgetItem()
            indexItem.setText(field.index)
            self.ui.tBvEnum.setItem(row, 0, indexItem)    
            nameItem = QTableWidgetItem()
            nameItem.setText(field.name)
            self.ui.tBvEnum.setItem(row, 1, nameItem)    
            descItem = QTableWidgetItem()
            descItem.setText(field.desc)
            self.ui.tBvEnum.setItem(row, 2, descItem)    
            row = row+1 
            pass
        pass

    def enumTreeViewClicked(self):
        self.enumCurItem = self.ui.tRvEnum.currentItem()
        if self.enumCurItem == None:
            self.actionAA.setEnabled(True)
            return
        
        # 进行界面赋值
        enumName = self.enumCurItem.text(0)
        if enumName == self.ui.lEtEnumName.text():
            return      
        enumData = self.enumXml.getData(enumName)
        self.rightShowEnumInfo(enumData)
        pass
    
    # 主界面右侧显示枚举信息
    def rightShowEnumInfo(self, enumData):
        if not enumData:
            return
        self.ui.lEtEnumName.setText(enumData.name)
        self.ui.lEtEnumDesc.setText(enumData.desc)
        if enumData.type == '1':
            self.ui.rBtnServer.setChecked(True)
        if enumData.type == '2':
            self.ui.rBtnClient.setChecked(True)
        if enumData.type == '3':
            self.ui.rBtnCom.setChecked(True)            
        self.fillEnumTableWidgetData(enumData)
        pass

    def saveProtoXml(self):
        result = self.protoXml.writeProtocolXml()
        if result is not None:
            self.ui.statusbar.showMessage(result)

    def saveToXml(self):
        # 保存protocol信息
        self.saveProtoXml()
        # 保存enum信息
        self.saveEnumXml()
        pass

    def showModifyProtoWindow(self):
        if self.protoCurItem == None or self.protoCurItem.type() != TVItemType.ItemProto:
            return
        self.modifyProtoUI = ModifyProtoUI(self)
        protoData = self.protoCurItem.data(0, Qt.UserRole)
        self.modifyProtoUI.fillProtoData(protoData)
        self.modifyProtoUI.show()
        self.modifyProtoUI.dialogSignal.connect(self.modifyProto_emit)

    # 点击协议修改按钮
    def modifyProtoClicked(self):
        self.showModifyProtoWindow()
        pass

    def showModifyEnumWindow(self):
        if self.enumCurItem == None:
            return
        self.modifyEnumUI = ModifyEnumUI(self)
        enumName = self.enumCurItem.text(0)
        self.modifyEnumUI.fillEnumData(enumName)
        self.modifyEnumUI.show()
        self.modifyEnumUI.dialogSignal.connect(self.modifyEnum_emit)
            
    # 点击枚举修改按钮
    def modifyEnumClicked(self):
        self.showModifyEnumWindow()
        pass


    # 程序界面退出
    def closeEvent(self, event):
        # 程序退出保存信息
        self.saveToXml()
        # 保存测试历史
        self.client.saveSendHistory()
        #关闭网络客户端
        self.disConnectClicked()
        print("program exit")

    # 协议测试处理逻辑
    def connServer(self, ip, port):
        result = self.client.connect(ip, port)
        if not result:
            QMessageBox.information(self, "信息", "连接服务器失败")
            return

        palette = self.ui.bTnConn.palette()
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.green)
        self.ui.bTnConn.setPalette(palette)
        self.ui.bTnConn.setAutoFillBackground(True)
        pass

    def connServerClicked(self):
        connHost = self.ui.cBbxServAddr.currentText()
        addr = connHost.split(':')
        self.connServer(addr[0], int(addr[1]))

    def disConnectClicked(self):
        self.client.disconnect()

        palette = self.ui.bTnConn.palette()
        palette.setColor(QtGui.QPalette.ButtonText, QtCore.Qt.black)
        self.ui.bTnConn.setPalette(palette)
        self.ui.bTnConn.setAutoFillBackground(True)

        self.ui.tEtResp.setText('')
        pass

    def showSearchProtoItem(self, filter):
        filter = filter.lower()
        if filter != "":
            for i in range(self.ui.tRvProtocol.topLevelItemCount()):
                topItem = self.ui.tRvProtocol.topLevelItem(i)
                isHidden = True
                if topItem.text(0).lower().find(filter) >= 0:
                    topItem.setExpanded(True)
                    topItem.setHidden(False)
                    isHidden = False
                for j in range(topItem.childCount()):
                    childItem = topItem.child(j)
                    if childItem.text(0).lower().find(filter) >= 0:
                        topItem.setExpanded(True)
                        topItem.setHidden(False)
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
            iter = QTreeWidgetItemIterator(self.ui.tRvEnum)
            while iter.value():
                item = iter.value()
                if item.text(0).lower().find(filter) >= 0:
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
            iter = QTreeWidgetItemIterator(self.ui.tRvEnum)
            while iter.value():
                item = iter.value()
                item.setHidden(False)
                item.setExpanded(False)
                iter.__iadd__(1)
            pass

    def createEnumItem(self, enumName):
        # 创建treewidget item
        topItem = QTreeWidgetItem()
        topItem.setText(0, enumName)
        topItem.setIcon(0, QIcon('./images/file.ico'))
        self.ui.tRvEnum.addTopLevelItem(topItem)
        pass            

    def createEnum_emit(self, enumData):
        # 创建treewidget item
        topItem = QTreeWidgetItem()
        topItem.setText(0, enumData.name)
        topItem.setIcon(0, QIcon('./images/file.ico'))
        self.ui.tRvEnum.addTopLevelItem(topItem)
        pass
    
    def saveEnumXml(self):
        self.enumXml.writeEnumXml()
        pass

    # 导出协议
    def exportPbClicked(self):
        self.ui.statusbar.showMessage('正在导出最新协议...')
        self.saveProtoXml()
        export_pb = ExportPb()
        result = export_pb.exportProtobuf()
        if result == None:
            self.ui.statusbar.showMessage('完成导出协议...')
        else:
            self.ui.statusbar.showMessage(result)

    # 导出枚举
    def exportEnumClicked(self):
        self.ui.statusbar.showMessage('正在导出最新枚举...')
        self.saveEnumXml()
        exprotEnum = ExportEnum()
        exprotEnum.export_enum()

        self.ui.statusbar.showMessage('完成导出枚举...')        
        pass

    # 导出配置表
    def exportTableClicked(self):
        self.ui.statusbar.showMessage('正在导出配置表...')
        transTable = TransTable()
        transTable.transTables()
        self.ui.statusbar.showMessage('完成导出配置表...')
        pass

    
    def openSettingClicked(self):
        self.toolSettingUI = ToolSettingUI()
        self.toolSettingUI.show()
        pass

    def sendProtoMsgClicked(self):
        # 获取当前消息ID
        curText = self.ui.cbBxMsgClass.currentText().strip()
        _, msgClass = curText.split(' ')
        msgName, msgID = self.ui.cBbxProto.currentText().strip().split(':')
        # 获取发送消息内容
        sendContent = self.ui.tEtReq.toPlainText().strip()
        # 调用client 发送消息
        self.client.sendMsg(msgID, msgClass, msgName, sendContent)
        pass

    def showRespMsg_emit(self, msgID, msgContent):
        if "error" in msgContent:
            self.ui.tEtResp.setText(msgContent+"\n\n")
            return

        msgText = self.ui.tEtResp.toPlainText()
        if msgText == "":
            msgText = "消息ID: " + msgID + "\n"
            msgText = msgText + "消息内容:\n" + msgContent + "\n"
        else:
            msgText += "===============================================================================\n"
            msgText = msgText + "消息ID: " + msgID + "\n"
            msgText = msgText + "消息内容:\n" + msgContent + "\n"
        self.ui.tEtResp.setText(msgText)
        pass

    def reConnectServer_emit(self, ip, port):
        self.disConnectClicked()
        self.connServer(ip, port)
        print("conn server={0}:{1}".format(ip, port))
        pass

########################################################################################


def ShowWindow():
    app = QApplication(sys.argv)
    mainWindow = ProtoMainUI()
    mainWindow.show()

    app.setStyle(QStyleFactory.create("Fusion"))
    app.setAttribute(QtCore.Qt.AA_NativeWindows)
    app.setAttribute(QtCore.Qt.AA_MSWindowsUseDirect3DByDefault)

    multiprocessing.freeze_support()
    sys.exit(app.exec_())
