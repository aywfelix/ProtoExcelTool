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

class CreateEnumUI(QMainWindow):
    # 窗体间通信
    #dialogSignal = pyqtSignal(str, str)

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
        # 添加关联事件
        self.ui.bTnEnumCreate.clicked.connect(self.createEnum)
        pass
    
    def createEnum(self):
        pass
