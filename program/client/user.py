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

class Wallet(object):
    def __init__(self):
        self.id = None
        self.wallet = None
        self.userId = None
        pass

class User(object):
    def __init__(self, parent=None):
        self.id = None
        self.username = "boge88"
        self.password = "boge888"
        self.realname = None
        self.avatar = None
        self.sex = None
        self.email = None
        self.createTime = None
        self.updateTime = None
        self.inviteCode = 0
        self.wallets = []
        self.token = None
        self.roleList = {}

        self.userInfo = None
        pass
