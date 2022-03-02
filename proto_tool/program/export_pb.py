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
from subprocess import *
import os


class ExportPbType:
    CPP = 1
    CSHARP = 2
    PYTHON = 3
    LUA = 4
    GO = 5

class ExportPb(object):
    def __init__(self):
        pass

    def setExportPath(self, path):
        self.exportPath = path

    def setInputPath(self, path):
        self.inputPath = path

    def exportPb(self, exportType):
        # 获取导出文件列表
        for proto in os.listdir(self.inputPath):
            if not proto.endswith(".proto"):
                continue

            exportStr = ""
            if exportType == ExportPbType.CPP:
                exportStr = 'D:\work\ProtocolEditor\ProtoExcelTool\proto_tool\program\protoc.exe --proto_path='+ self.inputPath + ' --cpp_out='+self.exportPath + " "+proto
                pass
            if exportType == ExportPbType.CSHARP:
                pass
            if exportType == ExportPbType.PYTHON:
                pass
            if exportType == ExportPbType.LUA:
                pass
            if exportType == ExportPbType.GO:
                #exportStr = 'D:\work\ProtocolEditor\ProtoExcelTool\proto_tool\program\protoc.exe --proto_path='+ self.inputPath + ' --go_out='+self.exportPath + " "+proto
                pass

            run(exportStr, shell=True)
            print(exportStr)
        #os.system(exportStr)


if __name__ == "__main__":
    print(os.getcwd())
    export = ExportPb()
    export.setInputPath("proto_tool/protos/")
    export.setExportPath("./proto_tool/pb/go/")
    export.exportPb(ExportPbType.GO)
    pass

