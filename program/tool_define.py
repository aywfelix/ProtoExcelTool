#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tool_define.py
@Time    :   2022/03/02 13:41:28
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   定义辅助结构
'''

# here put the import lib

def Singleton(cls):
    _instance = {}

    def _Singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _Singleton

# 编程语言分类
class ProgramLangType:
    CPP = 0
    LUA = 1
    GO = 2
    CSHARP = 3
    PYTHON = 4

# treeview右键菜单操作
class TVMenuOpType(object):
    DirCreate = 1
    DirModify = 2
    DirDelete = 3
    ProtoCreate = 4
    ProtoModify = 5
    ProtoDelete = 6
    EnumCreate = 7
    EnumModify = 8
    EnumDelete = 9

class TVItemType:
    ItemDir = 1
    ItemProto = 2

class TVItemProtoData:
    def __init__(self, protoId="", protoName="", protoDesc="", protoContent="", protoType=1):
        self.id = protoId
        self.name = protoName
        self.desc = protoDesc
        self.content = protoContent
        self.type = protoType # 1请求消息 2广播消息 3共用消息

    def __str__(self):
        return self.id+" "+self.name+" "+self.desc+" "+self.content

class TVItemDirData:
    def __init__(self, dirName="", package=""):
        self.dirName = dirName
        self.package = package
        pass

    def __str__(self):
        return self.dirName+" "+self.package

class TmplType:
    PROTO = 1
    ENUM = 2
    TABLE = 3

import time, hashlib
def create_uuid():
    m = hashlib.md5(str(time.time()).encode('utf-8'))
    return m.hexdigest()
    pass    
    
class TmplItemData:
    def __init__(self, tmplName, lang, tmplPublish, ttype = '1'):
        self.name = tmplName
        self.lang = lang # 代码语言 combobox index
        self.publish = tmplPublish
        self.uuid = create_uuid()
        self.ttype = ttype
        pass


class SetPathType:
    PROTOC = 1
    PROTO = 2
    TABLE = 3


class EnumField:
    def __init__(self, index, name, desc):
        self.index = index
        self.name = name
        self.desc = desc
        pass

class EnumItemData:
    def __init__(self, name, desc, enumType=1):
        self.name = name
        self.desc = desc
        self.fields = []
        self.type = enumType
        pass


    
# 工具常用配置项
class ToolConfigData:
    def __init__(self, protocPath, protoPath, excelPath, serverHosts):
        self.protocPath = protocPath
        self.protoPath = protoPath
        self.excelPath = excelPath
        self.serverHosts = serverHosts


# 动态生成消息
class DynamicMsgData:
    def __init__(self, msgId, msgClass, msgName, msgType):
        self.msgId = msgId
        self.msgClass = msgClass
        self.msgName = msgName
        self.msgType = msgType


@Singleton
class TmplLang:
    def __init__(self):
        self.cpp = "cpp"
        self.lua = "lua"
        self.golang = "golang"
        self.csharp = "csharp"

    def getLang(self, index):
        if index == 0:
            return self.cpp
        if index == 1:
            return self.lua
        if index == 2:
            return self.golang
        if index == 3:
            return self.csharp
        
    def getIndex(self, lang):
        if lang == self.cpp:
            return 0
        if lang == self.lua:
            return 1
        if lang == self.golang:
            return 2
        if lang == self.csharp:
            return 3

def StrToBool(str):
    if not str: return False
    if str == "True": return True
    if str == "False": return False