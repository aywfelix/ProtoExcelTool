#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tool_xml.py
@Time    :   2022/03/02 11:14:44
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   None
'''

# here put the import lib

import os
import sys
import xml.dom.minidom as xmlDom
from qt_ui.logic.tool_define import *

class ToolXml(object):
    def __init__(self, xmlPath=None, ):
        self.xmlPath = xmlPath
        pass

    def writeProtocolXml(self, protocolDict): #protocolDict={目录名：list[]}
        if protocolDict is None or not protocolDict:
            return
        try:
            # 根元素
            domTree = xmlDom.Document()
            # 创建protocols 节点
            protocolsNode = domTree.createElement("protocols")
            # 根据protocolDict 创建package 节点
            # 遍历protocolDict
            for dirName, protocolList in protocolDict.items():
                packageNode = domTree.createElement("package")
                packageNode.setAttribute("name", dirName)
                protocolsNode.appendChild(packageNode)
                for protocol in protocolList:
                    protoNode = domTree.createElement("protocol")
                    protoNode.setAttribute("id", protocol.id)
                    protoNode.setAttribute("name", protocol.name)
                    protoNode.setAttribute("desc", protocol.desc)
                    protoNode.setAttribute("content", protocol.content)
                    protoNode.setAttribute("onlyServer", str(protocol.onlyServer))
                    packageNode.appendChild(protoNode)
                    pass
                pass
            domTree.appendChild(protocolsNode)

            # 写入protocol配置文件
            with open('protocols.config', 'w') as f:
                domTree.writexml(f, indent=' ', addindent='\t', newl='\n', encoding='UTF-8')
                
        except Exception as e:
            print(e)

    def readProtocolXml(self):
        protocolDict = {}
        try:
            dom = xmlDom.parse(self.xmlPath)
            if dom == None:
                print("parse xml err, xml file not exist")
                return
            # 根元素
            domTree = dom.documentElement
            packages = domTree.getElementsByTagName("package")
            for package in packages:
                protocolList = []
                dirName = package.getAttribute("name")
                protocols = package.getElementsByTagName("protocol")
                
                for protocol in protocols:
                    id = protocol.getAttribute("id")
                    name = protocol.getAttribute("name")
                    desc = protocol.getAttribute("desc")
                    content = protocol.getAttribute("content")
                    onlyServer = protocol.getAttribute("onlyServer")

                    protoData = TVItemProtoData(id, name, desc, content, onlyServer)
                    protocolList.append(protoData)

                protocolDict[dirName] = protocolList
        except Exception as e:
            print(e)

        return protocolDict



# if __name__ == "__main__":
#     xml = ToolXml("protocols.config")
#     protoList = []
    
#     data = TVItemProtoData(1101, "sds", "sdgsa", "sdrga", True)
#     protoList.append(data)
#     data = TVItemProtoData(1102, "aa", "bb", "cc", True)
#     protoList.append(data)

#     protocolsDict = {}
#     protocolsDict["10 Test"] = protoList
#     xml.writeProtocolXml(protocolsDict)

#     xml.readProtocolXml()
