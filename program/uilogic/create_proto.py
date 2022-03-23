#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_proto_dir.py
@Time    :   2022/03/01 14:23:59
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示创建协议窗口
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.create_proto_ui import *
from proto_xml import *

class CreateProtoUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(TVItemProtoData)

    def __init__(self, parent=None):
        super(CreateProtoUI, self).__init__()
        self.ui = Ui_CreateProtoForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())
        self.parent = parent
        self.protoXml = ToolProtoXml()

        self.ui.bTnProtoCreate.clicked.connect(self.createProto)
        self.ui.rBtnReq.setChecked(True)
        self.ui.lEtProtoId.editingFinished.connect(self.checkProtoId)
        self.ui.lEtProtoName.editingFinished.connect(self.changeProtoName)
        self.ui.rBtnReq.toggled.connect(self.changeRadioButton)
        pass

    def createProto(self):
        protoId = self.ui.lEtProtoId.text().strip()
        protoName = self.ui.lEtProtoName.text().strip()
        protoDesc = self.ui.tEtProtoDesc.toPlainText()
        protoContent = self.ui.tEtProtoContent.toPlainText()
        onlyServer = self.ui.cBxProtocol.isChecked()

        protocols = self.protoXml.protocols
        for _, protocolDict in protocols.items():
            for _, protoData in protocolDict.items():
                if protoData.id == protoId:
                    QMessageBox.warning(self, "警告", "此协议编号已经存在")
                    return
                if protoData.name == protoName:
                    QMessageBox.warning(self, "警告", "此协议名称已经存在")
                    return
            pass        

        protoData = TVItemProtoData(protoId, protoName, protoDesc, protoContent, onlyServer)

        self.dialogSignal.emit(protoData)
        self.close()

    def checkProtoId(self):
        protoId = self.ui.lEtProtoId.text().strip()
        if not protoId.isdigit():
            # 弹出警告
            QMessageBox.critical(self, "错误", "协议编号默认为整数数字")
            pass
        pass

    def changeProtoName(self):
        # protoName = self.ui.lEtProtoName.text()
        # if self.ui.rBtnReq.isChecked():
        #     protoName += "Req"
        # elif self.ui.rBtnNotify.isChecked():
        #     protoName += "Notify"
        # self.ui.lEtProtoName.setText(protoName)
        pass

    def changeRadioButton(self):
        # protoName = self.ui.lEtProtoName.text().strip()
        # if self.ui.rBtnReq.isChecked():
        #     protoName = protoName[0:-6]
        #     protoName += "Req"
        # else:
        #     protoName = protoName[0:-3]
        #     protoName += "Notify"
        
        # self.ui.lEtProtoName.setText(protoName)        
        pass
        
