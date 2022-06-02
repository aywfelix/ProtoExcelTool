#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示更改协议窗口
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.modify_proto_ui import *
from proto_xml import *

class ModifyProtoUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(TVItemProtoData)

    def __init__(self, parent=None):
        super(ModifyProtoUI, self).__init__()
        self.ui = Ui_ModifyProtoForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())
        self.parent = parent
        self.proto_xml = ToolProtoXml()

        self.protoData = None

        self.ui.bTnProtoModify.clicked.connect(self.modifyProto)
        self.ui.lEtProtoName.editingFinished.connect(self.changeProtoName)
        self.ui.rBtnReq.toggled.connect(self.changeRadioButton)
        pass


    def getProtoType(self):
        if self.ui.rBtnReq.isChecked():
            return ProtocolType.REQ
        if self.ui.rBtnAck.isChecked():
            return ProtocolType.ACK
        if self.ui.rBtnNotify.isChecked():
            return ProtocolType.NOTIFY
        if self.ui.rBtnCom.isChecked():
            return ProtocolType.COMMON

    def modifyProto(self):
        protoId = self.ui.lEtProtoId.text()
        protoName = self.ui.lEtProtoName.text()
        protoDesc = self.ui.tEtProtoDesc.toPlainText()
        protoContent = self.ui.tEtProtoContent.toPlainText()

        protocols = self.proto_xml.protocols
        for _, protocolDict in protocols.items():
            for _, protoData in protocolDict.items():
                if protoData.id !='' and self.protoData.id != protoId and protoData.id == protoId:
                    QMessageBox.warning(self, "警告", "此协议编号已经存在")
                    return
                if self.protoData.name != protoName and protoData.name == protoName:
                    QMessageBox.warning(self, "警告", "此协议名称已经存在")
                    return
            pass


        self.protoData.id = protoId
        self.protoData.name = protoName
        self.protoData.desc = protoDesc
        self.protoData.content = protoContent

        self.dialogSignal.emit(self.protoData)
        self.close()

    def fillProtoData(self, data):
        self.protoData = data
        self.ui.lEtProtoId.setText(data.id)
        self.ui.lEtProtoName.setText(data.name)
        self.ui.tEtProtoDesc.setText(data.desc)
        self.ui.tEtProtoContent.setText(data.content)

        if data.type == '1':
            self.ui.rBtnReq.setChecked(True)
        if data.type == '2':
            self.ui.rBtnAck.setChecked(True)
        if data.type == '3':
            self.ui.rBtnNotify.setChecked(True)
        if data.type == '4':
            self.ui.rBtnCom.setChecked(True)
        pass


    def getOriginProtoName(self):
        protoName = self.ui.lEtProtoName.text().strip()
        if 'Req' in protoName:
            return protoName[:-3]
        if 'Ack' in protoName:
            return protoName[:-3]
        if 'Notify' in protoName:
            return protoName[:-6]
        return protoName

    def fixProtoName(self):
        protoName = self.getOriginProtoName()
        if self.ui.rBtnReq.isChecked():
            protoName += "Req"
        if self.ui.rBtnNotify.isChecked():
            protoName += "Notify"
        if self.ui.rBtnAck.isChecked():
            protoName += "Ack"

        self.ui.lEtProtoName.setText(protoName)


    def changeProtoName(self):
        self.fixProtoName()
        pass

    def changeRadioButton(self):
        self.fixProtoName()   
        pass

        
