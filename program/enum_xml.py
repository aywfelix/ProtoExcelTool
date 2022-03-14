#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum_xml.py
@Time    :   2022/03/11 16:49:43
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   枚举读取保存xml
'''

# here put the import lib
import codecs
import os
import xml.dom.minidom as xmlDom
from tool_define import *

@Singleton
class ToolEnumXml(object):
    def __init__(self):
        self.xmlEnumPath = "./config/enum.config"
        self.enumItemDatas = {}
        pass
    
    def isExistEnumName(self, name):
        if name in self.enumItemDatas.keys():
            return True
        return False
    
    def readEnumXml(self):
        pass

    def writeEnumXml(self):
        pass
