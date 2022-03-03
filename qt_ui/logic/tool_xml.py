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
import codecs
import xml.dom.minidom as xmlDom
from qt_ui.logic.tool_define import *

# class TVItemProtoData:
#     def __init__(self, protoId="", protoName="", protoDesc="", protoContent="", onlyServer=False):
#         self.id = protoId
#         self.name = protoName
#         self.desc = protoDesc
#         self.content = protoContent
#         self.onlyServer = onlyServer

#     def __str__(self):
#         return self.id+" "+self.name+" "+self.desc+" "+self.content

#############################################################################
proto_header = '''
syntax = "proto3";

'''
proto_message= '''
// %(protoDesc)s
message %(protoName)s{
    %(protoContent)s
}
'''
#############################################################################


class ToolProtoXml(object):
    def __init__(self):
        pass

    def setProtoConfig(self, protoConfig):
        self.xmlProtoPath = protoConfig

    def exportProtoPath(self, exportPath):
        self.protoPath = exportPath
        pass

    def writeProtocolXml(self, protocols): #protocols=[{["module"]=data, ["protocol"]=[protoData,]},...]
        if protocols is None or not protocols:
            return
        try:
            # 根元素
            domTree = xmlDom.Document()
            # 创建protocols 节点
            protocolsNode = domTree.createElement("protocols")
            for moduleDict in protocols:
                dirData = moduleDict["module"]
                protoDataList = moduleDict["protocol"]
                moduleNode = domTree.createElement("module")
                moduleNode.setAttribute("name", dirData.dirName)
                moduleNode.setAttribute("package", dirData.package)
                protocolsNode.appendChild(moduleNode)
                for protoData in protoDataList:
                    protocolNode = domTree.createElement("protocol")
                    protocolNode.setAttribute("id", protoData.id)
                    protocolNode.setAttribute("name", protoData.name)
                    protocolNode.setAttribute("desc", protoData.desc)
                    protocolNode.setAttribute("content", protoData.content)
                    protocolNode.setAttribute("onlyServer", str(protoData.onlyServer)) 
                    moduleNode.appendChild(protocolNode)                     
                    pass
                pass

            domTree.appendChild(protocolsNode)
            # 写入protocol配置文件
            with open(self.xmlProtoPath, "w") as f:
                domTree.writexml(f, indent=' ', addindent='\t', newl='\n', encoding="gbk")
                
        except Exception as e:
            print(e)

    def readProtocolXml(self):
        protocols = []
        try:
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
                moduleDict = {}
                dirName = moduleNode.getAttribute("name")
                package = moduleNode.getAttribute("package")
                dirData = TVItemDirData(dirName, package)
                moduleDict["module"] = dirData
                # 获取protocol data list
                protoDataList = []
                protocolNodes = moduleNode.getElementsByTagName("protocol")
                for protocolNode in protocolNodes:
                    id = protocolNode.getAttribute("id")
                    name = protocolNode.getAttribute("name")
                    desc = protocolNode.getAttribute("desc")
                    content = protocolNode.getAttribute("content")
                    onlyServer = protocolNode.getAttribute("onlyServer")
                    protoData = TVItemProtoData(id, name, desc, content, bool(onlyServer))
                    protoDataList.append(protoData)

                moduleDict["protocol"] = protoDataList
                protocols.append(moduleDict)
                
        except Exception as e:
            print(e)

        return protocols

    def exportProtoFile(self):
        # 根据配置文件生成proto file 文件
        try:
            protocolDict = self.readProtocolXml()
            if not protocolDict:
                return

            for dirName, protocolList in protocolDict.items():
                # 创建proto文件
                dirName = dirName.split(' ')[1]
                protoMsgs = proto_header
                for protocol in protocolList:
                    protoMessage = proto_message % {
                        "protoName": protocol.name,
                        "protoDesc": protocol.desc,
                        "protoContent": protocol.content
                    }
                    protoMsgs += "\n" + protoMessage
                    pass
                
                protoFilePath = self.protoPath+"/"+dirName+".proto"
                with codecs.open(protoFilePath, "w", 'utf-8') as f:
                    f.write(protoMsgs)
                    f.flush()
            pass            
        except Exception as e:
            print(e)

    def exportProtoPb(self):
        # 根据不同配置模板导出pb文件
        pass



# if __name__ == "__main__":
#     xml = ToolXml()
#     xml.setProtoConfig("./protocols.config")
#     xml.exportProtoPath("./")

#     protoList = []
    
#     data = TVItemProtoData("1101", "sds", "sdgsa", "sdrga", True)
#     protoList.append(data)
#     data = TVItemProtoData("1102", "aa", "bb", "cc", True)
#     protoList.append(data)

#     protocolsDict = {}
#     protocolsDict["10 Test"] = protoList
#     xml.writeProtocolXml(protocolsDict)
#     xml.exportProtoFile()

