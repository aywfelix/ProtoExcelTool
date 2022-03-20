# _*_coding:utf-8 _*_
import os
import codecs
from transtable.trans_define import *


class TransCsharp:
    def __init__(self, csharp_dir, field_types, field_descs):
        self.csharp_dir = csharp_dir
        self.field_types = field_types
        self.field_descs = field_descs

    def gen_row_fields(self):
        row_fields = "\t"
        tmp_field = ""
        for i in range(len(self.field_types)):
            field_type = self.field_types[i]
            tmp_field = data_type_cs[field_type[0]]+" " + field_type[1] + ";"
            strlen = 50
            self.field_descs[i] = self.field_descs[i].replace("\n", " ")
            row_fields += (tmp_field + " " *
                           (strlen-len(tmp_field)) + "// "+self.field_descs[i])
            row_fields += "\n\t"
        return row_fields

    def gen(self, table_name):
        row_fields = self.gen_row_fields()
        s = ""
        tmpl_file = "./transtable/table_csharp.tmpl"
        with codecs.open(tmpl_file, "r", "utf-8") as f:
            s = f.read()
        if not s:
            return
        s = s % {"class_name": table_name, "row_fields": row_fields}

        cs_file = os.path.join(self.csharp_dir, table_name+'.cs')
        with codecs.open(cs_file, "w", "GB2312") as f:
            f.write(s)
            f.flush()
            pass
