﻿#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   export_pb.py
@Time    :   2022/03/02 17:49:58
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   导出不同语言的pb文件
'''

# here put the import lib
import subprocess
import os
from tool_define import *
from setting_xml import *
from proto_xml import *
from logger import *

#############################################################################
proto_header = 'syntax = "proto3";'

proto_enum_tmpl = '''
enum %(DirName)sMsgId {
    %(DirName)s_MSG_ID = 0;    
%(enum_fields)s
}
'''
#############################################################################

@Singleton
class ExportPb(object):
    def __init__(self):
        self.settingXml = ToolSettingXml()
        self.protoXml = ToolProtoXml()
        pass

    # 导出最新proto文件
    def exportProtoFile(self):
        try:
            self.protoXml.readProtocolXml()
            # 根据xml信息生产proto文件
            modules = self.protoXml.getModules()
            protocols = self.protoXml.getProtocols()
            for dirName, dirData in modules.items():
                # 添加引用
                protoMsgs = proto_header+"\n"
                protoMsgs += dirData.package +"\n"

                protocolDict = protocols[dirName]
                # 添加消息枚举
                enum_fields = ""
                dir_name = dirName.split(" ")[1]
                for _, protoData in protocolDict.items():
                    if not protoData.id: continue
                    if protoData.type == ProtocolType.REQ: 
                        enum_field = dir_name.upper()+"_"+(protoData.name)[:-3].upper()
                        enum_field += "_REQ"
                    if protoData.type == ProtocolType.ACK: 
                        enum_field = dir_name.upper()+"_"+(protoData.name)[:-3].upper()
                        enum_field += "_ACK"
                    if protoData.type == ProtocolType.NOTIFY: 
                        enum_field = dir_name.upper()+"_"+(protoData.name)[:-6].upper()
                        enum_field += "_NOTIFY"
                    if protoData.type == ProtocolType.COMMON: 
                        enum_field = dir_name.upper()+"_"+protoData.name.upper()
                        enum_field += "_COM"

                    enum_field += " = " + str(protoData.id) + ";"
                    if enum_fields == "":
                        enum_fields += "    "+enum_field
                    else:
                        enum_fields += "\n    "+enum_field
                    pass

                # protoMsgs += proto_enum_tmpl % {
                #     "DirName": dir_name.capitalize(), "enum_fields": enum_fields
                # }

                protoMsgs += proto_enum_tmpl % {
                    "DirName": dir_name.capitalize(), "enum_fields": enum_fields
                }
                
                # if not protocolDict: continue
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
                toolConfig = settingXml.getTool()
                #print("save proto path=", toolConfig['proto'])
                protoFilePath = toolConfig['proto'] +"/"+moduleName+".proto"
                #print("export proto file=", protoFilePath)
                with codecs.open(protoFilePath, "w", 'utf-8', errors='ignore') as f:
                    f.write(protoMsgs)
                    pass   
                             
            return True
        except Exception as e:
            Logger.WriteLog(e)
            return False


    def exportProtobuf(self):
        try:
            if not self.exportProtoFile():
                return "export pb failed"
                
            # 根据配置选项导出不同pb
            tmpls = self.settingXml.getTmplsByType(TmplType.PROTO)
            if not tmpls:
                return
            toolConfig = self.settingXml.getTool()
            protocPath = toolConfig['protoc']
            if not protocPath.endswith("/"):
                protocPath = protocPath +"/"
            
            protocExeFile = protocPath+"protoc.exe"
            protocGenGoFile = protocPath+"protoc-gen-go.exe"

            protoDir = toolConfig['proto']  
            if not protoDir: return  
            for config in tmpls:
                for proto in os.listdir(protoDir):
                    if not proto.endswith(".proto"):
                        continue
                    if not config.publish: continue        
                    gen_pb_cmd = ""
                    if config.lang == ProgramLangType.CPP: # cpp
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --cpp_out='+config.publish + " "+proto
                        pass
                    if config.lang == ProgramLangType.LUA: # lua
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' -o '+config.publish+"/"+proto[:-6]+".pb" + " "+proto
                        pass
                    if config.lang == ProgramLangType.GO: # go
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --plugin=protoc-gen-go='+ protocGenGoFile + ' --go_out='+config.publish + " "+proto                           
                        pass
                    if config.lang == ProgramLangType.CSHARP: # csharp
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --csharp_out='+config.publish + " "+proto
                        pass
                    if config.lang == ProgramLangType.PYTHON: #python
                        gen_pb_cmd = protocExeFile + ' --proto_path=' + \
                            protoDir + ' --python_out='+config.publish + " "+proto

                    p = subprocess.Popen(gen_pb_cmd, shell=True, cwd=os.getcwd(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    outlines = ""
                    while p.poll() is None:
                        line = p.stdout.readline().decode("utf-8")
                        if not line: continue
                        outlines = outlines + line
                    if outlines:
                        Logger.WriteLog(outlines)
                        return outlines

            return None    
        except Exception as e:
            logStr = "export pb err, {0}".format(e)
            Logger.WriteLog(logStr)
            return logStr

   

