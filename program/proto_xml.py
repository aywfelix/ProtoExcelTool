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
#############################################################################
proto_header = 'syntax = "proto3";'
#############################################################################

@Singleton
class ToolProtoXml(object):
    def __init__(self):
        # self.modules = {['dirname']=data, ...}
        # self.protocols = {['dirname']={['protoId']=data, ...}, ...}
        self.xmlProtoPath = "./config/protocols.config"
        self.modules = {}
        self.protocols = {}
        pass
    
    def getProtocols(self):
        return self.protocols

    def getModules(self):
        return self.modules
    
    def getDirData(self, dirName):
        if not self.modules:
            return None
        if dirName not in self.modules.keys():
            return None
        return self.modules[dirName]

    def getProtoData(self, dirName, protoId):
        if dirName not in self.protocols.keys():
            return None
        if protoId not in self.protocols[dirName].keys():
            return None
        return self.protocols[dirName][protoId] 

    def addProtocol(self, dirName, protoData):
        if dirName not in self.protocols.keys():
            self.protocols[dirName] = {}
        
        self.protocols[dirName][protoData.id] = protoData
        pass

    def delProtocol(self, dirName, protoId):
        if dirName not in self.protocols.keys():
            return
        self.protocols[dirName].pop(protoId)
    
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
                    protocolNode.setAttribute("id", protoData.id)
                    protocolNode.setAttribute("name", protoData.name)
                    protoDesc = protoData.desc.replace("\r", "&#xD;").replace("\n", "&#xA;")
                    protocolNode.setAttribute("desc", protoDesc)
                    protoContent = protoData.content.replace("\r", "&#xD;").replace("\n", "&#xA;")
                    protocolNode.setAttribute("content", protoContent)
                    protocolNode.setAttribute("onlyServer", str(protoData.onlyServer))                     
                    pass
                pass
            # 写入protocol配置文件
            with open(self.xmlProtoPath, "w", encoding="gbk") as f:
                domTree.writexml(f, indent=' ', addindent='\t', newl='\n', encoding="gbk")            
        except Exception as e:
            print(e)


    def readProtocolXml(self):
        try:
            self.modules = {}
            self.protocols = {}            
            dataResource = ""
            with open(self.xmlProtoPath, "r", encoding="gbk") as f:
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
                    id = protocolNode.getAttribute("id")
                    name = protocolNode.getAttribute("name")
                    desc = protocolNode.getAttribute("desc")
                    desc = desc.replace("&#xD;", "\r").replace("&#xA;", "\n")
                    content = protocolNode.getAttribute("content")
                    content = content.replace("&#xD;", "\r").replace("&#xA;", "\n")              
                    onlyServer = protocolNode.getAttribute("onlyServer")
                    protoData = TVItemProtoData(id, name, desc, content, bool(onlyServer))
                    protocolDict[id] = protoData
                    pass
                self.protocols[dirName] = protocolDict
                
        except Exception as e:
            print(e)
        

    def exportProtoFile(self):
        try:
            if not self.modules:
                self.readProtocolXml()
                
            # 根据xml信息生产proto文件
            protoMsgs = proto_header+"\n"

            for dirName, dirData in self.modules.items():
                # 添加引用
                protoMsgs += dirData.package +"\n\n"
                protocolDict = self.protocols[dirName]
                for _, protoData in protocolDict.items():
                    # 注释
                    protoDesc = ""
                    descList = protoData.desc.split("\n")
                    for desc in descList:
                        protoDesc += "// "+desc+"\n"
                    protoMsgs += protoDesc
                    # 添加消息
                    protoMsgs += "message " + protoData.name + "{\n"

                    protoContent = ""
                    contentList = protoData.content.split("\n")
                    for content in contentList:
                        protoContent += "   " + content+"\n"
                    protoContent +="}\n\n"

                    protoMsgs += protoContent   
                    pass
                
                # 导出命名
                moduleName = dirData.dirName.split(" ")[1]
                # 获取导出proto路径
                settingXml = ToolSettingXml()
                _, protoPath, _ = settingXml.readToolConfig()
                protoFilePath = protoPath +"/"+moduleName+".proto"
                with codecs.open(protoFilePath, "w", 'utf-8') as f:
                    f.write(protoMsgs)
                    f.flush()
                    pass                
                pass
        except Exception as e:
            print(e)
