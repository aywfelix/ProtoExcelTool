#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum_go.py
@Time    :   2022/04/01 11:09:17
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   导出golang 枚举文件
'''

# here put the import lib
######################################################################################
enum_field_tmpl = ' %(item_name)s_%(enum_field)s %(item_name)s = %(field_index)s // %(field_desc)s'
enum_tmpl = '''package enums
%(enum_items)s
'''
enum_item_tmpl = '''
// %(item_desc)s
type %(item_name)s int
const(
%(enum_fields)s    
)
'''
####################################################################################
from tool_define import *
import os
import codecs

@Singleton
class ExportEnumGo(object):
    def __init__(self, go_dir, enum_datas):
        self.go_dir = go_dir
        self.enum_datas = enum_datas
        pass

    def gen(self):
        gen_str = ''
        enum_items = ''
        for enum_name, enum_data in self.enum_datas.items():
            enum_fields = ''
            enum_item = ''
            for field in enum_data.fields:
                field_str = enum_field_tmpl % {
                    "item_name": enum_name,
                    "enum_field": field.name, 
                    "field_index": int(field.index), 
                    "field_desc":field.desc
                }
                enum_fields += " " * 4 + field_str + '\n'
                pass
            enum_item = enum_item_tmpl % {"item_desc": enum_data.desc, "item_name":enum_name, "enum_fields":enum_fields}
            enum_items += enum_item
        
        gen_str = enum_tmpl % {"enum_items": enum_items}

        # 将生成内容写入文件中
        go_file = os.path.join(self.go_dir, 'enums.go')
        with codecs.open(go_file, "w", "GB2312") as f:
            f.write(gen_str)
            f.flush()
            pass

        pass