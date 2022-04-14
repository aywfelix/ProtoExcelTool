#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   reload.py
@Time    :   2022/03/09 23:18:35
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   遍历某个文件夹，动态加载代码
'''

# here put the import lib
import os
import sys

import importlib
from setting_xml import *

class ReLoadFiles(object):
    def __init__(self, parent=None):
        self.moduleList = {}
        pass

    def getPythonPbPath(self):
        setting_xml = ToolSettingXml()
        tmpls = setting_xml.getTmplsByType(TmplType.PROTO)
        if not tmpls:
            return None
        for config in tmpls:
            if config.lang == ProgramLangType.PYTHON: #python
                return config.publish
        return None 
        pass
    
    def readLoadModule(self):
        try:
            reload_path = self.getPythonPbPath()
            if not reload_path: return
            
            sys.path.append(reload_path)
            for pbfile in os.listdir(reload_path):
                if not pbfile.endswith(".py"):
                    continue
                shortFile = os.path.splitext(pbfile)[0]
                module = importlib.import_module(shortFile)
                # print(shortFile, module)
                self.moduleList[shortFile] = module
        except Exception as e:
            Logger.WriteLog("readLoadModule error, {0}".format(str(e)))
            print(e)
        pass


    def getModule(self, name):
        if name not in self.moduleList.keys():
            return None
        return self.moduleList[name]
        pass

if __name__ == "__main__":
    reload = ReLoadFiles()
    reload.readLoadModule()
    pass

#https://blog.csdn.net/mijichui2153/article/details/111665192
