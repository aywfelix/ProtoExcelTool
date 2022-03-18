# _*_coding:utf-8 _*_

import xlrd
from xlrd import xldate_as_tuple
import multiprocessing
import json
import os
import codecs
import datetime
import traceback
from tool_define import *
from trans_define import *

#############################################################################################
single_tmpl = '                row.%(fields)s = r["%(fields)s"].%(asType)s;\n'

vector_tmpl = '''
                auto end_%(fields)s = r["%(fields)s"].end();
				auto begin_%(fields)s = r["%(fields)s"].end();
				for (auto it = begin_%(fields)s; it != end_%(fields)s; ++it)
				{
					row.%(fields)s.emplace_back(it->%(asType)s);
				}
            '''
#############################################################################################

@Singleton
class TransCpp:
    def __init__(self, sheet, field_types, field_desc):
        self.json_dir = "../extra/tablejson"
        self.cpp_dir = "../extra/tables"
        self.sheet = sheet
        self.field_types = field_types
        self.field_desc = field_desc

    def gen_row_fields(self):
        row_fields = "\t"
        tmp_field = ""
        for i in range(len(self.field_types)):
            field_type = self.field_types[i]
            tmp_field = data_type_dic[field_type[0]]+" " + field_type[1] + ";"
            strlen = 50
            self.field_desc[i] = self.field_desc[i].replace("\n", " ")
            row_fields += (tmp_field + " " *
                                (strlen-len(tmp_field)) + "// "+self.field_desc[i])
            row_fields += "\n\t"
        return row_fields

    def gen_json_logic(self):
        json_logic = ''
        for field_type in self.field_types:
            real_type = data_type_dic[field_type[0]]
            logic_tmpl = ""
            if 'vector' in real_type:
                logic_tmpl = vector_tmpl
            else:
                logic_tmpl = single_tmpl    

            json_logic += logic_tmpl % {
                "fields": field_type[1],
                "asType": data_type_trans[field_type[0]]
            }
        return json_logic


    def gen(self, table_name):
        row_fields = self.gen_row_fields()
        json_logic = self.gen_json_logic()
        s = ""
        tmpl_file = "./transtable/table_cpp.tmpl"
        with codecs.open(tmpl_file, "r", "utf-8") as f:
            s = f.read()
        if not s:
            return
        s = s % {"class_name": table_name,
                 "row_fields": row_fields, "json_logic": json_logic}

        cpp_file = os.path.join(self.cpp_dir, table_name+'.hpp')
        with codecs.open(cpp_file, "w", "GB2312") as f:
            f.write(s)
            f.flush()
            pass
