#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum_lua.py
@Time    :   2022/03/25 17:41:44
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   自动生成lua枚举文件
'''

# here put the import lib
#################################################################################
enum_field_tmpl = '%(item_name)s.%(enum_field)s = %(field_index)s  -- %(field_desc)s'

enum_item_tmpl = '''
-- %(item_desc)s
EnumTable.%(item_name)s = EnumTable.%(item_name)s or {}
local %(item_name)s = EnumTable.%(item_name)s
%(enum_fields)s
'''

enum_tmpl = '''
EnumTable = EnumTable or {}
local EnumTable = EnumTable
%(enum_items)s

--------------------------------------------------------------
return EnumTable
'''
#################################################################################

from tool_define import *
import os
import codecs

@Singleton
class ExportEnumLua(object):
    def __init__(self, lua_dir, enum_datas):
        self.lua_dir = lua_dir
        self.enum_datas = enum_datas
        pass

    def gen(self):
        gen_str = ''
        enum_items = ''
        for enum_name, enum_data in self.enum_datas.items():
            enum_fields = ''
            enum_item = ''
            for field in enum_data.fields:
                field_str = enum_field_tmpl % {"item_name":enum_name, "enum_name":enum_name, "enum_field": field.name, "field_index": int(field.index), "field_desc":field.desc}
                enum_fields += field_str + '\n'
                pass
            enum_item = enum_item_tmpl % {"item_desc":enum_data.desc, "item_name":enum_name, "enum_fields":enum_fields}
            enum_items += enum_item
        
        gen_str = enum_tmpl % {"enum_items": enum_items}

        # 将生成内容写入文件中
        lua_file = os.path.join(self.lua_dir, 'Enums.lua')
        with codecs.open(lua_file, "w", "GB2312") as f:
            f.write(gen_str)
            f.flush()
            pass

        pass