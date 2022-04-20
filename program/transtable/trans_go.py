#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   trans_go.py
@Time    :   2022/03/31 14:33:36
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   None
'''

# here put the import lib
import os
import codecs
from tool_define import *
from transtable.trans_define import *


class TransGo:
    def __init__(self, go_dir, field_types, field_descs):
        self.go_dir = go_dir
        self.field_types = field_types
        self.field_descs = field_descs

    def gen_row_fields(self):
        row_fields = "\t"
        tmp_field = ""
        for i in range(len(self.field_types)):
            field_type = self.field_types[i]
            field_name = field_type[1]
            if '_' in field_name:
                names = field_name.split('_')
                tmp_field = names[0].capitalize()+names[1].capitalize() + " " + data_type_go[field_type[0]]
            else:
                tmp_field = field_name.capitalize() + " " + data_type_go[field_type[0]]
            strlen = 50
            self.field_descs[i] = self.field_descs[i].replace("\n", " ")
            row_fields += (tmp_field + " " *
                                (strlen-len(tmp_field)) + " // "+self.field_descs[i])
            row_fields += "\n\t"
        return row_fields


    def gen(self, table_name):
        row_fields = self.gen_row_fields()
        s = ""
        tmpl_file = "./transtable/table_go.tmpl"
        with codecs.open(tmpl_file, "r", "utf-8") as f:
            s = f.read()
        if not s:
            return
        s = s % {"class_name": table_name,
                 "low_class_name": table_name[0].lower()+table_name[1:],
                 "high_class_name":table_name.capitalize(),
                 "row_fields": row_fields}

        go_file = os.path.join(self.go_dir, table_name+'.go')
        with codecs.open(go_file, "w", "utf-8", errors='ignore') as f:
            f.write(s)
            f.flush()
            pass
