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

class TVItemType:
    ItemDir = 1
    ItemProto = 2

class TVItemProtoData:
    def __init__(self, protoId="", protoName="", protoDesc="", protoContent="", onlyServer=False):
        self.id = protoId
        self.name = protoName
        self.desc = protoDesc
        self.content = protoContent
        self.onlyServer = onlyServer

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
    
class TmplItemData:
    def __init__(self, tmplName, lang, tmplPublish):
        self.name = tmplName
        self.lang = lang # 代码语言 combobox index
        self.publish = tmplPublish
        pass


class SetPathType:
    PROTOC = 1
    PROTO = 2
    TABLE = 3

def Singleton(cls):
    _instance = {}

    def _Singleton(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _Singleton


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
        if lang == "cpp":
            return 0
        if lang == "lua":
            return 1
        if lang == "golang":
            return 2
        if lang == "csharp":
            return 3
