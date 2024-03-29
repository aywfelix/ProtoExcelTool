﻿#!/usr/bin/env python
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
from tool_define import *
from logger import *

@Singleton
class ToolSettingXml(object):
    def __init__(self):
        self.xmlSettingPath = "./config/setting.config"

        self.tools = {'protoc': '', 'proto': '', 'excel': '',
                      'serverjson': '', 'clientjson': '', 'hosts': []}
        self.protocols = []  # TmplItemData
        self.enums = []
        self.tables = []

        self.readSettingXml()
        pass

    def getTool(self):
        return self.tools

    def getTmpls(self):
        return self.protocols, self.enums, self.tables

    def getTmplsByType(self, tmplType):
        if tmplType == TmplType.PROTO:
            return self.protocols
        if tmplType == TmplType.ENUM:
            return self.enums
        if tmplType == TmplType.TABLE:
            return self.tables
        pass

    def addTmpls(self, tmplData, tmplType):
        if tmplType == TmplType.PROTO:
            self.protocols.append(tmplData)
        if tmplType == TmplType.ENUM:
            self.enums.append(tmplData)
        if tmplType == TmplType.TABLE:
            self.tables.append(tmplData)

    def updateTool(self, configData):
        self.tools['protoc'] = configData.protocPath
        self.tools['proto'] = configData.protoPath
        self.tools['excel'] = configData.excelPath
        self.tools['serverjson'] = configData.serverJsonPath
        self.tools['clientjson'] = configData.clientJsonPath
        self.tools['hosts'] = configData.serverHosts
        pass

    # 读取全部配置信息
    def readSettingXml(self):
        try:
            dataResource = ""
            with codecs.open(self.xmlSettingPath, "r", "GB2312") as f:
                dataResource = f.read()
            # 获取节点信息
            domTree = xmlDom.parseString(dataResource)
            if domTree == None:
                print("parse xml err")
                return
            rootNode = domTree.documentElement
            # 工具常用配置
            protocNode = rootNode.getElementsByTagName("protoc")[0]
            protoNode = rootNode.getElementsByTagName("proto")[0]
            excelNode = rootNode.getElementsByTagName("excel")[0]
            serverJsonNode = rootNode.getElementsByTagName("serverjson")[0]
            clientJsonNode = rootNode.getElementsByTagName("clientjson")[0]

            self.tools['protoc'] = protocNode.getAttribute("path")
            self.tools['proto'] = protoNode.getAttribute("path")
            self.tools['excel'] = excelNode.getAttribute("path")
            self.tools['serverjson'] = serverJsonNode.getAttribute("path")
            self.tools['clientjson'] = clientJsonNode.getAttribute("path")

            self.tools['hosts'] = []
            hostsNode = rootNode.getElementsByTagName("hosts")
            for hostNode in hostsNode:
                ipNodes = hostNode.getElementsByTagName("ip")
                if not ipNodes:
                    continue
                for hostNode in ipNodes:
                    host = hostNode.getAttribute("host")
                    self.tools['hosts'].append(host)
                    pass
                pass
            # 协议模板配置
            self.protocols = []
            protocolNodes = rootNode.getElementsByTagName("protocol")
            for protocolNode in protocolNodes:
                tmplNodes = protocolNode.getElementsByTagName("tmpl")
                if tmplNodes is None:
                    continue
                for node in tmplNodes:
                    name = node.getAttribute("name")
                    lang = node.getAttribute("lang")
                    publish = node.getAttribute("publish")
                    ttype = node.getAttribute("ttype")
                    tmplData = TmplItemData(name, int(lang), publish, ttype)
                    self.protocols.append(tmplData)

            # 枚举导出模板配置
            self.enums = []
            enumNodes = rootNode.getElementsByTagName("enum")
            for enumNode in enumNodes:
                tmplNodes = enumNode.getElementsByTagName("tmpl")
                if tmplNodes is None:
                    continue
                for node in tmplNodes:
                    name = node.getAttribute("name")
                    lang = node.getAttribute("lang")
                    publish = node.getAttribute("publish")
                    ttype = node.getAttribute("ttype")
                    tmplData = TmplItemData(name, int(lang), publish, ttype)
                    self.enums.append(tmplData)

            # 配置表导出模板配置
            self.tables = []
            tableNodes = rootNode.getElementsByTagName("table")
            for tableNode in tableNodes:
                tmplNodes = tableNode.getElementsByTagName("tmpl")
                for node in tmplNodes:
                    name = node.getAttribute("name")
                    lang = node.getAttribute("lang")
                    publish = node.getAttribute("publish")
                    ttype = node.getAttribute("ttype")
                    tmplData = TmplItemData(name, int(lang), publish, ttype)
                    self.tables.append(tmplData)

        except Exception as e:
            Logger.WriteLog("readSettingXml err, {0}".format(str(e)))
            print(e)
        pass

    # 保存全部配置信息
    def writeSettingXml(self):
        try:
            # 根元素
            domTree = xmlDom.Document()
            # 创建setting 节点
            settingNode = domTree.createElement("setting")
            domTree.appendChild(settingNode)
            # 创建tool节点
            toolNode = domTree.createElement("tool")
            settingNode.appendChild(toolNode)

            protocNode = domTree.createElement("protoc")
            protoNode = domTree.createElement("proto")
            excelNode = domTree.createElement("excel")
            serverJsonNode = domTree.createElement("serverjson")
            clientJsonNode = domTree.createElement("clientjson")

            hostsNode = domTree.createElement("hosts")
            protocNode.setAttribute("path", self.tools['protoc'])
            protoNode.setAttribute("path", self.tools['proto'])
            excelNode.setAttribute("path", self.tools['excel'])
            serverJsonNode.setAttribute("path", self.tools['serverjson'])
            clientJsonNode.setAttribute("path", self.tools['clientjson'])

            toolNode.appendChild(protocNode)
            toolNode.appendChild(protoNode)
            toolNode.appendChild(excelNode)
            toolNode.appendChild(serverJsonNode)
            toolNode.appendChild(clientJsonNode)
            toolNode.appendChild(hostsNode)
            # 创建ip节点
            for host in self.tools['hosts']:
                ipNode = domTree.createElement("ip")
                ipNode.setAttribute("host", host)
                hostsNode.appendChild(ipNode)

            # 创建protocol节点
            protocolNode = domTree.createElement("protocol")
            settingNode.appendChild(protocolNode)

            for tmplData in self.protocols:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                tmplNode.setAttribute("ttype", tmplData.ttype)
                protocolNode.appendChild(tmplNode)
                pass
            # 创建enum节点
            enumNode = domTree.createElement("enum")
            settingNode.appendChild(enumNode)
            for tmplData in self.enums:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                tmplNode.setAttribute("ttype", tmplData.ttype)
                enumNode.appendChild(tmplNode)
                pass
            # 创建table节点
            tableNode = domTree.createElement("table")
            settingNode.appendChild(tableNode)
            for tmplData in self.tables:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                tmplNode.setAttribute("ttype", tmplData.ttype)
                tableNode.appendChild(tmplNode)
                pass

            with open(self.xmlSettingPath, 'w+', encoding="GB2312") as f:
                f.write(self.toPrettyXml(domTree.toxml()))

        except Exception as e:
            Logger.WriteLog("writeSettingXml err, {0}".format(str(e)))
            print(e)
        pass

    # 防止保存xml插入多余空行

    def toPrettyXml(self, data):
        return '\n'.join([line for line in xmlDom.parseString(
            data).toprettyxml(indent=' '*2).split('\n') if line.strip()])
