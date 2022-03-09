#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2022/03/09 16:27:32
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   保存user信息
'''

# here put the import lib

class Role(object):
    def __init__(self):
        self.roleId = 0
        pass

class User(object):
    def __init__(self, parent=None):
        self.name = None
        self.passwd = None
        self.sceneId = 0
        self.lastSceneId = 0
        self.account = None
        self.roleList = {}
        pass
