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

@Singleton
class ExportPb(object):
    def __init__(self):
        self.settingXml = ToolSettingXml()
        self.pythonPbPath = "../extra/pb/python"
        pass

    def exportPb(self):
        # 根据配置选项导出不同pb
        tmplsDict = self.settingXml.readTmplsConfig()
        protoList = tmplsDict[TmplType.PROTO]
        if not protoList:
            return
        protocPath, protoPath, _ = self.settingXml.readToolConfig()
        if protocPath.endswith("/"):
            protocPath = protocPath+"protoc.exe"
        else:
            protocPath = protocPath+"/protoc.exe"
            
        for config in protoList:
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

                subprocess.Popen(cmdStr)
                # 默认导出 python pb，用于网络测试
                
                print(cmdStr)


# if __name__ == '__main__':
#     print(os.getcwd())
#     with open("../extra/pb/python/haha", "w") as f:
#         f.write("xxxxxxxxxxxxxxxxxxx")      

