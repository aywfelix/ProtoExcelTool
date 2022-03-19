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
enum_item = '''
    // %(enum_desc)s
    enum Em%(enum_name)s{
        %(enum_fields)s
    };
'''
enum_field = '''
%(enum_field)s // %(field_desc)s
'''
enum_tmpl = '''
#pragma once

namespace Enums{
    %(enum_items)s
}
'''
#############################################################
