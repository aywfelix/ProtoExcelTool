#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum_xml.py
@Time    :   2022/03/11 16:49:43
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   枚举读取保存xml
'''

# here put the import lib
import codecs
import enum
import os
import xml.dom.minidom as xmlDom
from xml.dom import Node
from tool_define import *

@Singleton
class ToolEnumXml(object):
    def __init__(self):
        self.xmlEnumPath = "./config/enums.config"
        self.enumDatas = {}

        self.readEnumXml()
        pass
    
    def addData(self, data):
        self.enumDatas[data.name] = data
        pass
    
    def getData(self, name):
        if not name or name not in self.enumDatas.keys():
            return None
        return self.enumDatas[name]
        pass
    
    def delData(self, name):
        if not name or name not in self.enumDatas.keys():
            return
        self.enumDatas.pop(name)
        pass

    def getDatas(self):
        return self.enumDatas
        pass
    
    def isExistEnumName(self, name):
        if name in self.enumDatas.keys():
            return True
        return False
    
    def readEnumXml(self):
        try:
            self.enumDatas = {}      
            dataResource = ""
            with open(self.xmlEnumPath, "r", encoding="gbk") as f:
                dataResource = f.read()
            if not dataResource:
                return

            dom = xmlDom.parseString(dataResource)
            if dom == None:
                print("parse xml err, xml file not exist")
                return
            # 根元素
            domTree = dom.documentElement

            enumNodes = domTree.getElementsByTagName("Enum")
            for enumNode in enumNodes:
                enumName = enumNode.getAttribute("name")
                enumDesc = enumNode.getAttribute("desc")
                enumData = EnumItemData(enumName, enumDesc)
                self.enumDatas[enumName] = enumData

                for fieldNode in enumNode.childNodes:
                    if fieldNode.nodeType == Node.TEXT_NODE:
                        continue
                    index = fieldNode.getAttribute("index")
                    name = fieldNode.getAttribute("name")
                    desc = fieldNode.getAttribute("desc")
                    fieldData = EnumField(index, name, desc)
                    enumData.fields.append(fieldData)
        except Exception as e:
            print(e)
        pass

    def writeEnumXml(self):
        try:
            if not self.enumDatas:
                return
            # 根元素
            domTree = xmlDom.Document()
            # 创建Enums节点
            enumsNode = domTree.createElement("Enums")
            domTree.appendChild(enumsNode)
            for enumName, enumData in self.enumDatas.items():
                # 创建Enum节点
                enumNode = domTree.createElement("Enum")
                enumsNode.appendChild(enumNode)
                # 设置属性
                enumNode.setAttribute("name", enumData.name)
                enumNode.setAttribute("desc", enumData.desc)
                # 创建EnumNode子节点field节点
                enumFields = enumData.fields
                for field in enumFields:
                    # 创建field节点
                    fieldNode = domTree.createElement("field")
                    enumNode.appendChild(fieldNode)
                    # 设置属性
                    fieldNode.setAttribute("index", field.index)
                    fieldNode.setAttribute("name", field.name)
                    fieldNode.setAttribute("desc", field.desc)
                    pass
                pass
            # 写入protocol配置文件
            with open(self.xmlEnumPath, "w", encoding="gbk") as f:
                domTree.writexml(f, indent=' ', addindent='\t', newl='\n', encoding="gbk")            
        except Exception as e:
            print(e)

        pass
