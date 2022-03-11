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

        self.parent = parent
        # 添加关联事件

        pass
