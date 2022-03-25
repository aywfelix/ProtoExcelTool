#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   modify_tmpl.py
@Time    :   2022/03/05 12:39:44
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   显示修改配置模板窗口
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.modify_tmpl_ui import *
from tool_define import *


class ModifyTmplUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(TmplItemData, TmplItemData)

    def __init__(self, parent):
        super(ModifyTmplUI, self).__init__()
        self.ui = Ui_ModifyTmplForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        self.parent = parent
        # 添加关联事件
        self.ui.bTnPublishDir.clicked.connect(self.setPublishPath)
        self.ui.bTnModify.clicked.connect(self.modifyTmplInfo)
        
        # 缓存之前的名字
        self.oldTmplData = None
        pass

    def setPublishPath(self):
        dirPath = QFileDialog.getExistingDirectory(
            self, '选择目录', './')
        if not dirPath:
            return
        self.ui.lEtPublishDir.setText(dirPath)

        pass

    def modifyTmplInfo(self):
        name = self.ui.lEtTmplName.text()
        lang = self.ui.cBbxLang.currentIndex()
        publish = self.ui.lEtPublishDir.text()
        if self.ui.rBtnServer.isChecked():
            ttype = '1'
        if self.ui.rBtnClient.isChecked():
            ttype = '2'
        tmplData = TmplItemData(name, lang, publish, ttype)
        self.dialogSignal.emit(self.oldTmplData, tmplData)
        self.close()
        
    def fillTmplData(self, tmplData):
        self.oldTmplData = tmplData
        self.ui.lEtTmplName.setText(tmplData.name)
        self.ui.cBbxLang.setCurrentIndex(tmplData.lang)
        self.ui.lEtPublishDir.setText(tmplData.publish)
        if tmplData.ttype == '1':
            self.ui.rBtnServer.setChecked(True)
        else:
            self.ui.rBtnClient.setChecked(True)
        