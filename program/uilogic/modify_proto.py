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

        self.oldData = None

        self.ui.bTnProtoModify.clicked.connect(self.modifyProto)
        pass


    def getProtoType(self):
        if self.ui.rBtnReq.isChecked():
            return "1"
        if self.ui.rBtnAck.isChecked():
            return "2"
        if self.ui.rBtnNotify.isChecked():
            return "3"
        if self.ui.rBtnCom.isChecked():
            return "4"

    def modifyProto(self):
        protoId = self.ui.lEtProtoId.text()
        protoName = self.ui.lEtProtoName.text()
        protoDesc = self.ui.tEtProtoDesc.toPlainText()
        protoContent = self.ui.tEtProtoContent.toPlainText()

        protocols = self.proto_xml.protocols
        for _, protocolDict in protocols.items():
            for _, protoData in protocolDict.items():
                if self.oldData.id != protoId and protoData.id == protoId:
                    QMessageBox.warning(self, "警告", "此协议编号已经存在")
                    return
                if self.oldData.name != protoName and protoData.name == protoName:
                    QMessageBox.warning(self, "警告", "此协议名称已经存在")
                    return
            pass

        protoType = self.getProtoType() 
        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, protoType)
        self.proto_xml.delProtocolByUUID(self.oldData.uuid)
        self.dialogSignal.emit(protoData)
        self.close()

    def fillProtoData(self, data):
        self.oldData = data
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
        
