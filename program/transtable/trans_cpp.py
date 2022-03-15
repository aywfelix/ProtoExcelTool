# _*_coding:utf-8 _*_

import xlrd
from xlrd import xldate_as_tuple
import multiprocessing
import json
import os
import codecs
import datetime
import traceback

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

class TransCpp:
    def __init__(self, sheet, json_dir, cpp_dir):
        self.sheet = sheet
        self.json_dir = json_dir
        self.cpp_dir = cpp_dir

        self.data_row_type = self.join_field_type()

    # 生成各自的类型核字段声明(int:id, string:comment...)
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

    def gen_json_logic(self):
        json_logic = ''
        for i in range(len(self.data_row_type)):
            x_tuple = self.data_row_type[i]
            if "vector" in x_tuple[0]:
                json_logic += (vector_tmpl) % {
                    "fields": x_tuple[1], "asType": data_type_trans[x_tuple[0]]}
            elif x_tuple[0] in ["int", "std::string", "float", "double"]:
                json_logic += (single_tmpl) % {
                    "fields": x_tuple[1], "asType": data_type_trans[x_tuple[0]]}
        return json_logic

    def fix_row_dict(self, row_values):
        row_dict = {}
        for i in range(len(self.data_row_type)):  # i 代表列
            if row_values[i] is None:
                row_values[i] = ""
            data_type = self.data_row_type[i]
            field_type = data_type[0]
            field_id = data_type[1]

            if "int" == field_type:
                row_dict[field_id] = int(row_values[i])
            if "float" == field_type:
                row_dict[field_id] = float(row_values[i])
            if "double" == field_type:
                row_dict[field_id] = float(row_values[i])
            if "std::string" == field_type:
                row_dict[field_id] = str(row_values[i])
            if "vector" in field_type and row_values[i] == "":
                row_dict[field_id] = []
                continue
            if "vector" in field_type and row_values[i] != "":
                if isinstance(row_values[i], float):
                    row_dict[field_id] = [int(row_values[i])]
                    continue
            if "std::vector<int>" == field_type:
                row_dict[field_id] = list(
                    map(int, row_values[i].split('|')))
            if "std::vector<double>" == field_type:
                row_dict[field_id] = list(
                    map(float, row_values[i].split('|')))
            if "std::vector<float>" == field_type:
                row_dict[field_id] = list(
                    map(float, row_values[i].split('|')))
            if "std::vector<std::string>" == field_type:
                row_dict[field_id] = list(
                    map(str, row_values[i].split('|')))
        # print("=============", row_dict)
        return row_dict


    def transport_json(self, table_name):
        rows = 5
        rowe = self.sheet.nrows
        if rowe <= rows:
            return
        all_rows = {}
        while rows < rowe:
            row_dict = self.fix_row_dict(self.sheet.row_values(rows))
            all_rows[row_dict["id"]] = row_dict
            rows = rows+1

        # 写入json
        json_file = os.path.join(self.json_dir, table_name+'.json')
        with open(json_file, 'w+') as f:
            jsonStr = json.dumps(
                all_rows, indent=4, sort_keys=False, ensure_ascii=False)
            f.write(jsonStr + '\n')

    def gen_cpp(self, table_name, data_desc):
        row_fields = self.gen_row_fields(data_desc)
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