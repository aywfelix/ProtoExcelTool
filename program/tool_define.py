﻿#!/usr/bin/env python
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


import uuid
def create_uuid():
    return uuid.uuid1().hex
    pass   

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


class TVItemDirData:
    def __init__(self, dirName="", package=""):
        self.dirName = dirName
        self.package = package
        self.uuid = create_uuid()
        pass

    def __str__(self):
        return self.dirName+" "+self.package

class ProtocolType:
    REQ = "1"
    ACK = "2"
    NOTIFY = "3"
    COMMON = "4"

class TVItemProtoData:
    def __init__(self, protoId="", protoName="", protoDesc="", protoContent="", protoType=ProtocolType.REQ):
        self.id = protoId
        self.name = protoName
        self.desc = protoDesc
        self.content = protoContent
        self.type = protoType # 1请求消息 2回复消息 3广播消息 4共用消息

    def __str__(self):
        return self.id+" "+self.name+" "+self.desc+" "+self.content

class TmplType:
    PROTO = 1
    ENUM = 2
    TABLE = 3
 
    
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
    ServerJson = 4
    ClientJson = 5


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
    def __init__(self, protocPath, protoPath, excelPath, serverJsonPath, clientJsonPath, serverHosts=[]):
        self.protocPath = protocPath
        self.protoPath = protoPath
        self.excelPath = excelPath
        self.serverJsonPath = serverJsonPath
        self.clientJsonPath = clientJsonPath
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
        self.python = "python"

    def getLang(self, index):
        if index == 0:
            return self.cpp
        if index == 1:
            return self.lua
        if index == 2:
            return self.golang
        if index == 3:
            return self.csharp
        if index == 4:
            return self.python
        
    def getIndex(self, lang):
        if lang == self.cpp:
            return 0
        if lang == self.lua:
            return 1
        if lang == self.golang:
            return 2
        if lang == self.csharp:
            return 3
        if lang == self.python:
            return 4

def StrToBool(str):
    if not str: return False
    if str == "True": return True
    if str == "False": return False

import re
def VarifyHost(ip, port):
    if not ip: return False
    if not isinstance(ip, str): return False
    if not str.isdigit(port): return False
    if int(port) > 65535: return False
    ipre = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if ipre.match(ip):
        return True

    return False
