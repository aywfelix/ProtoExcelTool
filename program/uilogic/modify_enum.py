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
from uipy.modify_enum_ui import *
from enum_xml import *
from tool_define import *


class ModifyEnumUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(EnumItemData)

    def __init__(self, parent=None):
        super(ModifyEnumUI, self).__init__()
        self.ui = Ui_ModifyEnumForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.ui.tBvEnum.setColumnCount(3)
        self.ui.tBvEnum.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.ui.tBvEnum.horizontalHeader().setSectionsClickable(False)
        self.ui.tBvEnum.horizontalHeader().resizeSection(0, 80)
        self.ui.tBvEnum.horizontalHeader().resizeSection(1, 168)
        self.ui.tBvEnum.horizontalHeader().resizeSection(2, 170)
        self.ui.tBvEnum.setShowGrid(True)

        self.parent = parent
        self.enumXml = ToolEnumXml()
        self.enumName = None
        self.maxIndex = 0
        # 添加关联事件
        self.ui.bTnEnumModify.clicked.connect(self.modifyEnum)
        pass

    def modifyEnum(self):
        # 检查枚举名字是否重复
        enumName = self.ui.lEtEnumName.text().strip()
        if not enumName:
            return
        if enumName != self.enumName:
            if self.enumXml.isExistEnumName(enumName):
                QMessageBox.critical(self, "错误", "枚举名称已存在")
                return
        enumDesc = self.ui.lEtEnumDesc.text().strip()
        enumType = '1'
        if self.ui.rBtnServer.isChecked():
            enumType = '1'
        if self.ui.rBtnClient.isChecked():
            enumType = '2'
        if self.ui.rBtnCom.isChecked():
            enumType = '3'
        enumData = EnumItemData(enumName, enumDesc, enumType)
        rows = self.ui.tBvEnum.rowCount()
        for row in range(0, rows):
            indexItem = self.ui.tBvEnum.item(row, 0)
            nameItem = self.ui.tBvEnum.item(row, 1)
            descItem = self.ui.tBvEnum.item(row, 2)
            if not indexItem or not nameItem or not descItem:
                continue
            index = indexItem.text().strip()
            name = nameItem.text().strip()
            desc = descItem.text().strip()
            if not index or not name or not desc:
                continue
            enumField = EnumField(index, name, desc)
            enumData.fields.append(enumField)
        # 保存更新的枚举数据
        self.enumXml.addData(enumData)
        self.dialogSignal.emit(enumData)
        self.close()
        pass

    # 删除某行记录
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() == Qt.Key_Delete:
            selectRow = self.ui.tBvEnum.currentRow()
            self.ui.tBvEnum.removeRow(selectRow)
            pass
        rows = self.ui.tBvEnum.rowCount()
        if rows == 0:
            self.maxIndex = 0
            self.insertEmptyRow()
        pass

    # 编辑单元格触发
    def cellChanged(self, row, column):
        nameItem = self.ui.tBvEnum.item(row, 1)
        if not nameItem:
            return
        if nameItem.text().strip() == "":
            return
        rows = self.ui.tBvEnum.rowCount()
        if rows == row+1:
            self.insertEmptyRow()
        pass

    def fillEnumData(self, enumName):
        enumData = self.enumXml.getData(enumName)
        if not enumData:
            return
        self.enumName = enumName

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

    def fillEnumTableWidgetData(self, enumData):
        row = 0
        for field in enumData.fields:
            self.ui.tBvEnum.insertRow(row)
            # 索引
            indexItem = QTableWidgetItem()
            indexItem.setText(field.index)
            if int(field.index) > self.maxIndex:
                self.maxIndex = int(field.index)
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
        self.insertEmptyRow()
        # 插入空行
        self.ui.tBvEnum.cellChanged.connect(self.cellChanged)

    def insertEmptyRow(self):
        self.maxIndex = self.maxIndex + 1
        rows = self.ui.tBvEnum.rowCount()
        self.ui.tBvEnum.insertRow(rows)
        indexItem = QTableWidgetItem()
        indexItem.setText(str(self.maxIndex))
        self.ui.tBvEnum.setItem(rows, 0, indexItem)
        pass
