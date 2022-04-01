#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   export_enum.py
@Time    :   2022/03/19 20:04:57
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   导出不同语言的文件
'''

# here put the import lib
from tool_define import *
from export.enum_cpp import *
from export.enum_lua import *
from export.enum_go import *
from enum_xml import *
from setting_xml import *

@Singleton
class ExportEnum(object):
    def __init__(self):
        self.enumXml = ToolEnumXml()
        self.settingXml = ToolSettingXml()
        pass
    
    def export_enum(self):
        try:
            # 读取最新枚举配置信息
            self.enumXml.readEnumXml()
            enumDatas = self.enumXml.getDatas()
            # 根据配置枚举语言导出不同枚举文件
            # 获取最新配置文件信息
            tmpls = self.settingXml.getTmplsByType(TmplType.ENUM)
            if not tmpls:
                return  
          
            for tmpl in tmpls:
                if not tmpl.publish: return
                if tmpl.lang == ProgramLangType.CPP:
                    # 读取cpp 枚举模板
                    enum_cpp = ExportEnumCpp(tmpl.publish, enumDatas)
                    enum_cpp.gen()
                    pass
                if tmpl.lang == ProgramLangType.CSHARP:
                    pass
                if tmpl.lang == ProgramLangType.LUA:
                    enum_lua = ExportEnumLua(tmpl.publish, enumDatas)
                    enum_lua.gen()
                    pass
                if tmpl.lang == ProgramLangType.GO:
                    enum_go = ExportEnumGo(tmpl.publish, enumDatas)
                    enum_go.gen()
                    pass
                pass
            pass
        except Exception as e:
            print(e)
        pass

