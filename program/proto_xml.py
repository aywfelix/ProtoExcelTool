#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   tool_xml.py
@Time    :   2022/03/02 11:14:44
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   工具协议配置文件处理
'''

# here put the import lib
import codecs
from xml.dom import Node
import xml.dom.minidom as xmlDom

from sympy import N
from tool_define import *
from setting_xml import *


@Singleton
class ToolProtoXml(object):
    def __init__(self):
        # self.modules = {['dirname']=data, ...}
        # self.protocols = {['dirname']={['uuid']=data, ...}, ...}
        self.xmlProtoPath = "./config/protocols.config"
        self.modules = {}
        self.protocols = {}
        #用于动态生成消息
        self.dynamicMsg = {}
        pass

    def getModules(self):
        return self.modules
    
    def getProtocols(self):
        return self.protocols

    def getModuleProtos(self, dirname):
        if not dirname in self.protocols.keys():
            return None
        return self.protocols[dirname]

    
    def getDirData(self, dirName):
        if not self.modules:
            return None
        if dirName not in self.modules.keys():
            return None
        return self.modules[dirName]
    
    def addProtocol(self, dirName, protoData):
        if dirName not in self.protocols.keys():
            self.protocols[dirName] = {}
        
        self.protocols[dirName][protoData.uuid] = protoData
        pass

    def delProtocol(self, dirName, uuid):
        if dirName not in self.protocols.keys():
            return
        if not uuid in self.protocols[dirName].keys():
            return
        self.protocols[dirName].pop(uuid)
    
    def delProtocolByUUID(self, uuid):
        for dirName, protocol in self.protocols.items():
            for proto_uuid, _ in protocol.items():
                if proto_uuid == uuid:
                    self.protocols[dirName].pop(uuid)
                    break
        pass
    
    def addDir(self, dirData):
        if dirData.dirName in self.modules.keys():
            return
        self.modules[dirData.dirName] = dirData
        self.protocols[dirData.dirName] = {}
        pass

    def delDir(self, dirName):
        if dirName not in self.modules.keys():
            return
        self.modules.pop(dirName)
        self.protocols.pop(dirName)

    def writeProtocolXml(self):
        try:
            # 根元素
            domTree = xmlDom.Document()
            # 创建protocols 节点
            protocolsNode = domTree.createElement("protocols")
            domTree.appendChild(protocolsNode)
            for dirName, dirData in self.modules.items():
                # 创建module节点
                moduleNode = domTree.createElement("module")
                protocolsNode.appendChild(moduleNode)
                # 设置属性
                moduleNode.setAttribute("name", dirData.dirName)
                dirPackage = dirData.package.replace("\r", "&#xD;").replace("\n", "&#xA;")
                moduleNode.setAttribute("package", dirPackage)
                # 创建module子节点 protocol节点
                protoDict = self.protocols[dirName]
                for _, protoData in protoDict.items():
                    # 创建protocol 节点
                    protocolNode = domTree.createElement("protocol")
                    moduleNode.appendChild(protocolNode)
                    # 设置属性
                    protocolNode.setAttribute("type", protoData.type)
                    protocolNode.setAttribute("id", protoData.id)
                    protocolNode.setAttribute("name", protoData.name)
                    protoDesc = protoData.desc.replace("\r", "&#xD;").replace("\n", "&#xA;")
                    protocolNode.setAttribute("desc", protoDesc)
                    protoContent = protoData.content.replace("\r", "&#xD;").replace("\n", "&#xA;")
                    protocolNode.setAttribute("content", protoContent)
                    pass
                pass
            # 写入protocol配置文件
            with open(self.xmlProtoPath, "w", encoding="GB2312") as f:
                domTree.writexml(f, indent=' ', addindent='\t',
                                 newl='\n', encoding="GB2312")
        except Exception as e:
            print(e)


    def readProtocolXml(self):
        try:
            self.modules = {}
            self.protocols = {}            
            dataResource = ""
            with open(self.xmlProtoPath, "r", encoding="GB2312", errors='ignore') as f:
                dataResource = f.read()
            if not dataResource:
                return

            dom = xmlDom.parseString(dataResource)
            if dom == None:
                print("parse xml err, xml file not exist")
                return
            # 根元素
            domTree = dom.documentElement

            moduleNodes = domTree.getElementsByTagName("module")
            for moduleNode in moduleNodes:
                dirName = moduleNode.getAttribute("name")
                package = moduleNode.getAttribute("package")
                package = package.replace("&#xD;", "\r").replace("&#xA;", "\n")
                dirData = TVItemDirData(dirName, package)
                self.modules[dirName] = dirData

                protocolDict = {}
                # 获取protocol
                for protocolNode in moduleNode.childNodes:
                    if protocolNode.nodeType == Node.TEXT_NODE:
                        continue
                    type =  protocolNode.getAttribute("type")
                    id = protocolNode.getAttribute("id")
                    name = protocolNode.getAttribute("name")
                    desc = protocolNode.getAttribute("desc")
                    desc = desc.replace("&#xD;", "\r").replace("&#xA;", "\n")
                    content = protocolNode.getAttribute("content")
                    content = content.replace("&#xD;", "\r").replace("&#xA;", "\n")              
                    protoData = TVItemProtoData(id, name, desc, content, type)
                    proto_uuid = protoData.uuid
                    protocolDict[proto_uuid] = protoData
                    print(proto_uuid)
                    #print('-------', protoData.name)
                    pass
                
                self.protocols[dirName] = protocolDict
                
                # # 动态消息生成
                self.dynamicMsg = {}
                for dirName, protoDatas in self.protocols.items():
                    msgClass = dirName.split(' ')[1]
                    for protoId, protoData in protoDatas.items():
                        msgName = protoData.name
                        msgType = protoData.type
                        self.dynamicMsg[protoId] = DynamicMsgData(protoId, msgClass, msgName, msgType)
                    pass                
        except Exception as e:
            print(e)

    def getDynamicMsgs(self):
        return self.dynamicMsg

    def getDynamicMsg(self, protoId):
        if protoId not in self.dynamicMsg.keys():
            return None

        return self.dynamicMsg[protoId]   

