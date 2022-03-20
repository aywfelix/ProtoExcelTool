#!/usr/bin/env python
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

@Singleton
class ExportPb(object):
    def __init__(self):
        self.settingXml = ToolSettingXml()
        self.pythonPbPath = "../extra/pb/python"
        pass

    def exportPb(self):
        try:
            # 导出最新proto文件
            protoXml = ToolProtoXml()
            protoXml.exportProtoFile()
            
            # 根据配置选项导出不同pb
            tmpls = self.settingXml.getTmplsByType(TmplType.PROTO)
            if not tmpls:
                return
            toolConfig = self.settingXml.getTool()
            protocPath = toolConfig['protoc']
            if protocPath.endswith("/"):
                protocPath = protocPath+"protoc.exe"
            else:
                protocPath = protocPath+"/protoc.exe"
            protoPath = toolConfig['proto']    
            for config in tmpls:
                for proto in os.listdir(protoPath):
                    if not proto.endswith(".proto"):
                        continue

                    cmdStr = ""
                    if config.lang == 0: # cpp
                        cmdStr = protocPath + ' --proto_path=' + \
                            protoPath + ' --cpp_out='+config.publish + " "+proto
                        pass
                    if config.lang == 1: # lua
                        pass
                    if config.lang == 2: # go
                        pass
                    if config.lang == 3: # csharp
                        pass
                    print(cmdStr)
                    subprocess.Popen(cmdStr)
                    # 默认导出 python pb，用于网络测试
                    cmdStr = protocPath + ' --proto_path=' + \
                        protoPath + ' --python_out=../extra/pb/python' + " "+proto                    
                    print(cmdStr)
                    subprocess.Popen(cmdStr)
        except Exception as e:
            print("export pb err, ", e)

   

