#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   enum_cpp.py
@Time    :   2022/03/19 20:24:05
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   导出cpp枚举文件
'''

# here put the import lib
#############################################################
enum_item_tmpl = '''
// %(item_desc)s
enum %(item_name)s{
%(enum_fields)s
};
'''
enum_field_tmpl = '%(enum_field)s = %(field_index)s, // %(field_desc)s'

enum_tmpl = '''
#pragma once

namespace Enums{
%(enum_items)s
}
'''
#############################################################
from tool_define import *
import os
import codecs

@Singleton
class ExportEnumCpp(object):
    def __init__(self, cpp_dir, enum_datas):
        self.cpp_dir = cpp_dir
        self.enum_datas = enum_datas
        pass

    def gen(self):
        gen_str = ''
        enum_items = ''
        for enum_name, enum_data in self.enum_datas.items():
            enum_fields = ''
            enum_item = ''
            for field in enum_data.fields:
                field_str = enum_field_tmpl % {"enum_field": field.name, "field_index": int(field.index), "field_desc":field.desc}
                enum_fields += " " * 4 + field_str + '\n'
                pass
            enum_item = enum_item_tmpl % {"item_desc": enum_data.desc, "item_name":enum_name, "enum_fields":enum_fields}
            enum_items += enum_item
        
        gen_str = enum_tmpl % {"enum_items": enum_items}

        # 将生成内容写入文件中
        cpp_file = os.path.join(self.cpp_dir, 'Enums.hpp')
        with codecs.open(cpp_file, "w", "GB2312") as f:
            f.write(gen_str)
            f.flush()
            pass

        pass