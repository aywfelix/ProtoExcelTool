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
from tool_define import *

@Singleton
class ToolSettingXml(object):
    def __init__(self):
        self.xmlSettingPath = "./config/setting.config"
 
        self.initSettingConfig()      
        pass

    def initSettingConfig(self):
        # 初始化配置文件
        try:
            if os.path.exists(self.xmlSettingPath):
                return
            # 创建默认配置文件
            with open(self.xmlSettingPath, "w+", encoding="gbk") as f:
                # 文件不存在创建节点
                domTree = xmlDom.Document()
                settingNode = domTree.createElement("setting")
                # 创建tool 节点
                toolNode = domTree.createElement("tool")
                settingNode.appendChild(toolNode)
                # 创建protoc path 节点
                protocNode = domTree.createElement("protoc")
                toolNode.appendChild(protocNode)
                protocNode.setAttribute("path", "")
                # 创建proto path 节点
                protoNode = domTree.createElement("proto")
                toolNode.appendChild(protoNode)
                protoNode.setAttribute("path", "")
                # 创建table path 节点
                tableNode = domTree.createElement("excel")
                toolNode.appendChild(tableNode)
                tableNode.setAttribute("path", "")          

                domTree.appendChild(settingNode)
                with open(self.xmlSettingPath, 'w', encoding="gbk") as f:
                    f.write(self.toPrettyXml(domTree.toxml()))
        except Exception as e:
                print(e)

    def readTmplsConfig(self):
        try:
            tmplsDict = {}
            protoList = []
            enumList = []
            tableList = []
            tmplsDict[TmplType.PROTO] = protoList
            tmplsDict[TmplType.ENUM] = enumList
            tmplsDict[TmplType.TABLE] = tableList
            
            dataResource = ""
            with open(self.xmlSettingPath, "r", encoding="gbk") as f:
                dataResource = f.read()
            # 获取节点信息
            domTree = xmlDom.parseString(dataResource)
            if domTree == None:
                print("parse xml err")
                return None
            
            rootNode = domTree.documentElement
            protocolNodes = rootNode.getElementsByTagName("protocol")
            for protocolNode in protocolNodes:
               tmplNodes = protocolNode.getElementsByTagName("tmpl")
               if tmplNodes is None:
                   continue
               for node in tmplNodes:
                   name = node.getAttribute("name")
                   lang = node.getAttribute("lang")
                   publish = node.getAttribute("publish")
                   tmplData = TmplItemData(name, int(lang), publish)
                   protoList.append(tmplData)
           
            enumNodes = rootNode.getElementsByTagName("enum")
            for enumNode in enumNodes:
                tmplNodes = enumNode.getElementsByTagName("tmpl")
                if tmplNodes is None:
                    continue
                for node in tmplNodes:
                   name = node.getAttribute("name")
                   lang = node.getAttribute("lang")
                   publish = node.getAttribute("publish")
                   tmplData = TmplItemData(name, int(lang), publish)
                   enumList.append(tmplData)
                
            tableNodes = rootNode.getElementsByTagName("table")
            for tableNode in tableNodes:
                tmplNodes = tableNode.getElementsByTagName("tmpl")
                for node in tmplNodes:
                   name = node.getAttribute("name")
                   lang = node.getAttribute("lang")
                   publish = node.getAttribute("publish")
                   tmplData = TmplItemData(name, int(lang), publish)
                   tableList.append(tmplData)
                   
            # 返回配置信息
            return tmplsDict
        except Exception as e:
            print(e)
        pass

    def saveTmplsConfig(self, tmplsDict):
        try:
            if not tmplsDict:
                return
            dataResource = ""
            with open(self.xmlSettingPath, "r", encoding="gbk") as f:
                dataResource = f.read()
                f.close()
            # 获取节点信息
            domTree = xmlDom.parseString(dataResource)
            if domTree == None:
                print("parse xml err")
                return
            
            rootNode = domTree.documentElement
            # 删除原来的节点
            protocolNodes = rootNode.getElementsByTagName("protocol")
            if protocolNodes:
                for protocolNode in protocolNodes:
                    rootNode.removeChild(protocolNode)

            enumNodes = rootNode.getElementsByTagName("enum")
            if enumNodes:
                for enumNode in enumNodes:
                    rootNode.removeChild(enumNode)
                    
            tableNodes = rootNode.getElementsByTagName("table")
            if tableNodes:
                for tableNode in tableNodes:
                    rootNode.removeChild(tableNode)
                    
            # 重新创建配置节点
            protocolNode = domTree.createElement("protocol")
            rootNode.appendChild(protocolNode)
            enumNode = domTree.createElement("enum")
            rootNode.appendChild(enumNode)
            tableNode = domTree.createElement("table")
            rootNode.appendChild(tableNode)
            
            for tmplData in tmplsDict[TmplType.PROTO]:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                protocolNode.appendChild(tmplNode)            

            for tmplData in tmplsDict[TmplType.ENUM]:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                enumNode.appendChild(tmplNode)
            
            for tmplData in tmplsDict[TmplType.TABLE]:
                tmplNode = domTree.createElement("tmpl")
                tmplNode.setAttribute("name", tmplData.name)
                tmplNode.setAttribute("lang", str(tmplData.lang))
                tmplNode.setAttribute("publish", tmplData.publish)
                tableNode.appendChild(tmplNode)            
                                        
            with open(self.xmlSettingPath, 'w', encoding="gbk") as f:
                f.write(self.toPrettyXml(domTree.toxml()))
        except Exception as e:
            print(e)
        pass
    
    # 读取工具配置
    def readToolConfig(self):
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
            protocNode = rootNode.getElementsByTagName("protoc")[0]
            protoNode = rootNode.getElementsByTagName("proto")[0]
            tableNode = rootNode.getElementsByTagName("excel")[0]

            protocPath = protocNode.getAttribute("path")
            protoPath = protoNode.getAttribute("path")
            tablePath = tableNode.getAttribute("path")
            
            # print(protocPath, protoPath, tablePath)
            return protocPath, protoPath, tablePath
        except Exception as e:
            print(e)        
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
            protocNode = rootNode.getElementsByTagName("protoc")[0]
            protocNode.setAttribute("path", protocPath)

            protoNode = rootNode.getElementsByTagName("proto")[0]
            protoNode.setAttribute("path", protoPath)

            tableNode = rootNode.getElementsByTagName("excel")[0]
            tableNode.setAttribute("path", tablePath)
            
            with open(self.xmlSettingPath, 'w', encoding="gbk") as f:
                f.write(self.toPrettyXml(domTree.toxml()))
                
        except Exception as e:
            print(e)
        
        pass
    
    def toPrettyXml(self, data):
        return '\n'.join([line for line in xmlDom.parseString(
    data).toprettyxml(indent=' '*2).split('\n') if line.strip()])

    

