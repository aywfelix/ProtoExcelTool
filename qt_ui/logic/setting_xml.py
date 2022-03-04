#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tool_setting.py
@Time    :   2022/03/04 10:11:53
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   保存更新工具配置
'''

# here put the import lib
import codecs
import os
import xml.dom.minidom as xmlDom

from sympy import root
from qt_ui.logic.tool_define import *

class ToolSettingXml(object):
    def __init__(self):
        self.xmlSettingPath = "./setting.config"
 
        self.initSettingXml()      
        pass

    def initSettingXml(self):
        # 初始化配置文件
        try:
            if os.path.exists(self.xmlSettingPath):
                print("文件已存在")
                return
            # 创建默认配置文件
            with open(self.xmlSettingPath, "w+", encoding="gbk") as f:
                # 文件不存在创建节点
                domTree = xmlDom.Document()
                settingNode = domTree.createElement("setting")
                # 创建tool 节点
                toolNode = domTree.createElement("tool")
                settingNode.appendChild(toolNode)
                # 创建protocpath 节点
                protocPathNode = domTree.createElement("protocPath")
                toolNode.appendChild(protocPathNode)
                protocTextNode = domTree.createTextNode("./")
                protocPathNode.appendChild(protocTextNode)
                # 创建protopath 节点
                protoPathNode = domTree.createElement("protoPath")
                toolNode.appendChild(protoPathNode)
                protoTextNode = domTree.createTextNode("./")
                protoPathNode.appendChild(protoTextNode)
                # 创建tablepath 节点
                tablePathNode = domTree.createElement("tablePath")
                toolNode.appendChild(tablePathNode)
                tableTextNode = domTree.createTextNode("./")
                tablePathNode.appendChild(tableTextNode)            

                domTree.appendChild(settingNode)
                domTree.writexml(f, indent=' ', addindent='\t', newl='\n', encoding="gbk")   
        except Exception as e:
                print(e)

    def readToolConfig(self):
        try:
            dataResource = ""
            with open(self.xmlSettingPath, "r", encoding="gbk") as f:
                dataResource = f.read()
            # 获取节点信息
            dom = xmlDom.parseString(dataResource)
            if dom == None:
                print("parse xml err")
                return 
            rootNode = dom.documentElement
            toolNode = rootNode.getElementsByTagName("tool")[0]
            protocNode = toolNode.getElementsByTagName("protocPath")[0]
            protoNode = toolNode.getElementsByTagName("protoPath")[0]
            tableNode = toolNode.getElementsByTagName("tablePath")[0]
            protocPath, protoPath, tablePath = "", "", ""
            if protocNode.childNodes:
                protocPath = protocNode.childNodes[0].data
            if protoNode.childNodes:
                protoPath = protoNode.childNodes[0].data
            if tableNode.childNodes:
                tablePath = tableNode.childNodes[0].data      
            return protocPath, protoPath, tablePath
        except Exception as e:
            print(e)        
        pass

    def readProtoConfig(self):
        pass

    def readEnumConfig(self):
        pass

    def readTableConfig(self):
        pass

    def saveProtoSetting(self):
        pass
    def saveEnumSetting(self):
        pass
    def saveTableSetting(self):
        pass

    def saveToolSetting(self, protocPath, protoPath, tablePath):
        try:
            dataResource = ""
            with open(self.xmlSettingPath, "r", encoding="gbk") as f:
                dataResource = f.read()
            # 获取节点信息
            domTree = xmlDom.parseString(dataResource)
            if domTree == None:
                print("parse xml err")
                return            

            rootNode = domTree.documentElement
            # 更新节点值
            protocNode = rootNode.getElementsByTagName("protocPath")[0]
            protocNode.childNodes[0].data = protocPath

            protocNode = rootNode.getElementsByTagName("protoPath")[0]
            protocNode.childNodes[0].data = protoPath

            protocNode = rootNode.getElementsByTagName("tablePath")[0]
            protocNode.childNodes[0].data = tablePath            

            # 写入protocol配置文件
            with open(self.xmlSettingPath, "w", encoding="gbk") as f:
                domTree.writexml(f, indent=' ', encoding="gbk")
                
        except Exception as e:
            print(e)
        
        pass