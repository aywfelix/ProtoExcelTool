# _*_coding:utf-8 _*_

import xlrd
from xlrd import xldate_as_tuple
import multiprocessing
import json
import os
import codecs
import datetime
import traceback


# 数据类型字典
data_type_dic = {
    "INT": "int",
    "FLOAT": "float",
    "DOUBLE": "double",
    "STRING": "string",
    "LI": "List<int>",
    "LD": "List<double>",
    "LF": "List<float>",
    "LS": "List<string>"
}


class TransCsharp:
    def __init__(self, sheet, csharp_dir):
        self.sheet = sheet
        self.csharp_dir = csharp_dir

        self.data_row_type = self.join_field_type()

    def join_field_type(self):
        data_type = []
        for x in self.sheet.row_values(0):
            data_type.append(data_type_dic[x])
        
        return list(zip(data_type, self.sheet.row_values(2)))      

    def gen_row_fields(self, data_desc):
        row_fields = "\t"
        tmp_field = ""
        for i in range(len(self.data_row_type)):
            x = self.data_row_type[i]
            tmp_field = x[0]+" " + x[1] + ";"
            strlen = 50
            data_desc[i] = data_desc[i].replace("\n", " ")
            row_fields += (tmp_field + " " *
                                (strlen-len(tmp_field)) + "// "+data_desc[i])
            row_fields += "\n\t"
        return row_fields

    def gen_csharp(self, table_name, data_desc):
        row_fields = self.gen_row_fields(data_desc)
        s = ""
        tmpl_file = "./transtable/table_csharp.tmpl"
        with codecs.open(tmpl_file, "r", "utf-8") as f:
            s = f.read()
        if not s:
            return
        s = s % {"class_name": table_name, "row_fields": row_fields}

        cpp_file = os.path.join(self.csharp_dir, table_name+'.cs')
        with codecs.open(cpp_file, "w", "GB2312") as f:
            f.write(s)
            f.flush()
            pass


