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
from qt_ui.uipy.modify_tmpl_ui import *


class ModifyTmplUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(str, str, int, str)

    def __init__(self, parent=None):
        super(ModifyTmplUI, self).__init__()
        self.ui = Ui_ModifyTmplForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        # 添加关联事件
        self.ui.bTnPublishDir.clicked.connect(self.setPublishPath)
        self.ui.bTnModify.clicked.connect(self.modifyTmplInfo)
        
        # 缓存之前的名字
        self.oldTmplName = None
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
        self.dialogSignal.emit(self.oldTmplName, name, lang, publish)
        self.close()
        
    def fillTmplData(self, name, lang, publish):
        self.oldTmplName = name
        self.ui.lEtTmplName.setText(name)
        self.ui.cBbxLang.setCurrentIndex(lang)
        self.ui.lEtPublishDir.setText(publish)
