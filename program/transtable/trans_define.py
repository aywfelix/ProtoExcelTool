#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trans_define.py
@Time    :   2022/03/15 11:29:35
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   转表常用定义
'''

# here put the import lib

# 数据类型字典
data_type_cpp = {
    "INT": "int",
    "FLOAT": "float",
    "DOUBLE": "double",
    "STRING": "std::string",
    "LI": "std::vector<int>",
    "LD": "std::vector<double>",
    "LF": "std::vector<float>",
    "LS": "std::vector<std::string>"
}

data_type_cs = {
    "INT": "int",
    "FLOAT": "float",
    "DOUBLE": "double",
    "STRING": "string",
    "LI": "List<int>",
    "LD": "List<double>",
    "LF": "List<float>",
    "LS": "List<string>"
}

data_type_go = {
    "INT": "int",
    "FLOAT": "float32",
    "DOUBLE": "float64",
    "STRING": "[]rune",
    "LI": "[]int",
    "LD": "[]float64",
    "LF": "[]float32",
    "LS": "[]byte"
}


data_type_trans = {
    "INT": "asInt()",
    "FLOAT": "asFloat()",
    "DOUBLE": "asFloat()",
    "STRING": "asString()",
    "LI": "asInt()",
    "LD": "asFloat()",
    "LF": "asFloat()",
    "LS": "asString()"
}
