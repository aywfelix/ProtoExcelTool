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
from transtable.trans_cpp import *
from transtable.trans_csharp import *

@Singleton
class TransTable:
    def __init__(self):
        self.excel_dir = "../extra/excels/"
        self.json_dir = "../extra/tablejson/"
        pass

    def loadExcels(self):
        files = os.listdir(self.excel_dir)
        excels = [file for file in files if os.path.splitext(file)[
            1] == ".xlsx" and '~' not in file]
        classes_name = []
        for file in excels:
            tmp_name = os.path.splitext(file)[0]
            classes_name.append(tmp_name.split('_')[0])
        print(excels, classes_name)
        return excels, classes_name

    def get_all_rows(self, sheet, fields_type, fields_export, is_server):
        rows = 5
        rowe = sheet.nrows
        if rowe <= rows:
            return
        all_rows = {}
        while rows < rowe:
            row_dict = self.fix_row_dict(sheet.row_values(rows), fields_type, fields_export, is_server)
            all_rows[row_dict["id"]] = row_dict
            rows = rows+1  

        return all_rows      
        pass

    def fix_row_dict(self, row_values, fields_type, fields_export, is_server):
        row_dict = {}
        for i in range(len(fields_type)):  # i 代表列
            # 过滤导出字段
            if fields_export[i][1] == '':
                continue
            if is_server and fields_export[i][1].find('s') == 0:
                continue
            if not is_server and fields_export[i][1].find('c') == 0:
                continue

            if row_values[i] is None:
                row_values[i] = ""

            data_type = fields_type[i]
            field_type = data_type[0]
            field_id = data_type[1]
            #print("row_values====", row_values[i], type(row_values[i]), field_id)
            if "INT" == field_type:
                row_dict[field_id] = int(row_values[i])
            if "FLOAT" == field_type:
                row_dict[field_id] = float(row_values[i])
            if "DOUBLE" == field_type:
                row_dict[field_id] = float(row_values[i])
            if "STRING" == field_type:
                row_dict[field_id] = str(row_values[i])
            if field_type in("LI", "LF", "LD", "LS"):
                if row_values[i] == "":
                    row_dict[field_id] = []
                    continue
                else:
                    if '|' not in str(row_values[i]): # 默认读取的表格数据都是float类型
                        row_dict[field_id] = [int(row_values[i])]
                        continue
                    pass
            if "LI" == field_type:
                row_dict[field_id] = list(
                    map(int, row_values[i].split('|')))
            if "LD" == field_type:
                row_dict[field_id] = list(
                    map(float, row_values[i].split('|')))
            if "LF" == field_type:
                row_dict[field_id] = list(
                    map(float, row_values[i].split('|')))
            if "LS" == field_type:
                row_dict[field_id] = list(
                    map(str, row_values[i].split('|')))

        #print("=============", row_dict)
        return row_dict

    def write_json(self, table_name, all_rows):
        # 写入json
        json_file = os.path.join(self.json_dir, table_name+'.json')
        with open(json_file, 'w+') as f:
            jsonStr = json.dumps(
                all_rows, indent=4, sort_keys=False, ensure_ascii=False)
            f.write(jsonStr + '\n')        

    def transExcels(self, excel_name, table_name):
        try:
            excelFile = xlrd.open_workbook(os.path.join(self.excel_dir, excel_name))
            excelSheetNames = excelFile.sheet_names()
            sheet = excelFile.sheet_by_name(excelSheetNames[0])
            if not sheet:
                return

            # 字段注释
            data_desc1 = sheet.row_values(0)
            data_desc2 = sheet.row_values(1)
            data_desc = [a+" "+b for a, b in zip(data_desc1, data_desc2)]

            # 字段类型与字段名称--[(INT,id), (STRING,comment), ...)]
            data_type = []
            for x in sheet.row_values(3): # 字段类型
                data_type.append(x)
            fields_type = list(zip(data_type, sheet.row_values(2)))   # 字段名称
            # print(fields_type)
            # 字段导出与字段名称--[(id,cs), (comment,''), (name,s),..)]
            export_type = []
            for x in sheet.row_values(4):
                export_type.append(x)
            fields_export = list(zip(sheet.row_values(2),export_type))

            all_rows = self.get_all_rows(sheet, fields_type, fields_export, True)
            # print(all_rows)
            self.write_json(table_name, all_rows)
            # 导出json文件
            # trans_json = TransJson(sheet, table_name, fields_type, fields_export, True)
            # trans_json.convertJson()
            # trans_cpp = TransCpp(sheet, json_dir, cpp_dir)
            # trans_csharp = TransCsharp(sheet, csharp_dir)

            # 生成cpp 文件及json文件
            # trans_cpp.transport_json(table_name)
            # trans_cpp.gen_cpp(table_name, data_desc)
            # trans_csharp.gen_csharp(table_name, data_desc)

            # print("transport table ok!", excel_name)
        except Exception as e:
            print('str(Exception):\t', str(e))
            print('traceback.print_exc():', traceback.print_exc())
        pass


    def transTables(self):
        excels, _ = self.loadExcels()
        if not excels:
            return

        # pool = multiprocessing.Pool(processes=5)
        # for excel in excels:
        #     class_name = excel.split('_')[0]
        #     pool.apply_async(self.transExcels, (excel, class_name))
        # # gc pool
        # pool.close()
        # pool.join()
        for excel in excels:
            class_name = excel.split('_')[0]
            self.transExcels(excel, class_name)
    pass

if __name__ == '__main__':
    trans = TransTable()
    trans.transTables()

    pass
