#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   create_enum.py
@Time    :   2022/03/10 19:15:18
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   枚举创建窗口处理
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.create_enum_ui import *
from enum_xml import *
from tool_define import *

class CreateEnumUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(EnumItemData)

    def __init__(self, parent=None):
        super(CreateEnumUI, self).__init__()
        self.ui = Ui_CreateEnumForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.ui.tBvEnum.setColumnCount(3)
        self.ui.tBvEnum.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)    
        self.ui.tBvEnum.horizontalHeader().setSectionsClickable(False)
        self.ui.tBvEnum.horizontalHeader().resizeSection(0, 80)
        self.ui.tBvEnum.horizontalHeader().resizeSection(1, 173)
        self.ui.tBvEnum.horizontalHeader().resizeSection(2, 175)
        self.ui.tBvEnum.setShowGrid(True)
        
        self.parent = parent
        self.enumXml = ToolEnumXml()
        rows = self.ui.tBvEnum.rowCount()
        self.ui.tBvEnum.insertRow(rows)
        # 添加关联事件
        self.ui.bTnEnumCreate.clicked.connect(self.createEnum)

        pass
    
    def createEnum(self):
        # 检查枚举名字是否重复
        enumName = self.ui.lEtEnumName.text().strip()
        if not enumName:
            return
        if self.enumXml.isExistEnumName(enumName):
            QMessageBox.critical(self, "错误", "枚举名称已存在")
            return
        enumDesc = self.ui.lEtEnumDesc.text().strip()
        enumData = EnumItemData(enumName, enumDesc)
        rows = self.ui.tBvEnum.rowCount()
        for row in range(0, rows):
            index = self.ui.tBvEnum.item(row, 0).text()
            name = self.ui.tBvEnum.item(row, 1).text().strip()
            if not name:
                continue
            desc = self.ui.tBvEnum.item(row, 2).text().strip()
            enumField = EnumField(index, name, desc)
            enumData.fields.append(enumField)
        self.dialogSignal.emit(enumData)
        pass
    
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        row = self.ui.tBvEnum.currentRow()
        col = self.ui.tBvEnum.currentColumn()
        if event.key() == Qt.Key_Return and col == 2:
            # self.ui.tBvEnum.setCurrentCell(row, col)
            # self.ui.tBvEnum.edit(self.ui.tBvEnum.currentIndex())
            rows = self.ui.tBvEnum.rowCount()
            self.ui.tBvEnum.insertRow(rows)
        pass
    

        
