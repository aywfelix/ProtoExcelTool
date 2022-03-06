#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   add_tmpl.py
@Time    :   2022/03/04 16:55:32
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   显示添加模板窗口
'''

# here put the import lib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from uipy.add_tmpl_ui import *

class AddTmplUI(QMainWindow):
    # 窗体间通信
    dialogSignal = pyqtSignal(str, int, str)   

    def __init__(self, parent=None):
        super(AddTmplUI, self).__init__()
        self.ui = Ui_AddTmplForm()
        self.ui.setupUi(self)
        self.setWindowOpacity(0.96)
        self.setFixedSize(self.width(), self.height())

        # 添加关联事件
        self.ui.bTnPublishDir.clicked.connect(self.setPublishPath)
        self.ui.bTnOk.clicked.connect(self.addTmplInfo)
        pass

    def setPublishPath(self):
        dirPath = QFileDialog.getExistingDirectory(
            self, '选择目录', './')
        if not dirPath:
            return
        self.ui.lEtPublishDir.setText(dirPath)

        pass

    def addTmplInfo(self):
        tmplName = self.ui.lEtTmplName.text()
        lang = self.ui.cBbxLang.currentIndex()
        publish = self.ui.lEtPublishDir.text()
        self.dialogSignal.emit(tmplName, lang, publish)
        self.close()        

