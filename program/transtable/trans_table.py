# _*_coding:utf-8 _*_

from operator import is_
from attr import field
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
from transtable.trans_lua import *
from transtable.trans_go import *
from setting_xml import *


@Singleton
class TransTable:
    def __init__(self):
        self.settingXml = ToolSettingXml()
        toolConfig = self.settingXml.getTool()
        self.excel_dir = toolConfig['excel']
        self.json_dir = toolConfig['tbjson']
        if not self.excel_dir: 
            self.excel_dir = "../extra/excels/"
        if not self.json_dir: 
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

    def get_all_rows(self, sheet, field_types):
        rows = 5
        rowe = sheet.nrows
        if rowe <= rows:
            return
        all_rows = {}
        while rows < rowe:
            row_dict = self.fix_row_dict(sheet.row_values(rows), field_types)
            all_rows[row_dict["id"]] = row_dict
            rows = rows+1  

        return all_rows      
        pass

    def fix_row_dict(self, row_values, field_types):
        row_dict = {}
        for data_type in field_types:  # i 代表列
            field_type = data_type[0]
            field_id = data_type[1]
            i = data_type[2]
            if row_values[i] is None:
                row_values[i] = ""
            #print("row_values====", row_values[j], type(row_values[j]), field_id)
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

    def write_json(self, table_name, all_rows, is_server):
        # 写入json
        if is_server:
            json_file = os.path.join(self.json_dir, table_name+'S.json')
        else:
            json_file = os.path.join(self.json_dir, table_name+'C.json')
        with codecs.open(json_file, 'w+', encoding='utf-8') as f:
            jsonStr = json.dumps(
                all_rows, indent=4, sort_keys=False, ensure_ascii=False)
            f.write(jsonStr + '\n')

    def filter_field_types(self, field_types, field_exports, is_server):
        new_field_types = []
        for i in range(len(field_types)):
            field_type = field_types[i]
            field_export = field_exports[i]

            if field_export[1] == '': continue
            if is_server and field_export[1].find("s") == -1: continue
            if not is_server and field_export[1].find("c") == -1: continue

            field_type = field_type + (i,)
            new_field_types.append(field_type)
                    
        return new_field_types
        pass      

    def transExcels(self, excel_name, table_name):
        try:
            excelFile = xlrd.open_workbook(os.path.join(self.excel_dir, excel_name))
            excelSheetNames = excelFile.sheet_names()
            sheet = excelFile.sheet_by_name(excelSheetNames[0])
            if not sheet:
                return

            # 字段注释
            field_desc1 = sheet.row_values(0)
            field_desc2 = sheet.row_values(1)
            field_descs = [a+" "+b for a, b in zip(field_desc1, field_desc2)]

            # 字段类型与字段名称--[(INT,id), (STRING,comment), ...)]
            data_type = []
            for x in sheet.row_values(3): # 字段类型
                data_type.append(x)
            field_types = list(zip(data_type, sheet.row_values(2)))   # 字段名称
            # print(fields_type)
            # 字段导出与字段名称--[(id,cs), (comment,''), (name,s),..)]
            export_type = []
            for x in sheet.row_values(4):
                export_type.append(x)
            field_exports = list(zip(sheet.row_values(2),export_type))

            # 如果配置了导出cpp
            exportTmpls = self.settingXml.getTmplsByType(TmplType.TABLE)
            if not exportTmpls:
                return
            for tmpl in exportTmpls:
                if tmpl.ttype == '1': 
                    is_server = True 
                else: 
                    is_server = False
                filter_types = self.filter_field_types(field_types, field_exports, is_server) #(int, id, 0)已经加上列索引
                all_rows = self.get_all_rows(sheet, filter_types)
                # 导出json文件
                self.write_json(table_name, all_rows, is_server)

                if tmpl.lang == ProgramLangType.CPP:
                    trans_cpp = TransCpp(tmpl.publish, field_types, field_descs)
                    trans_cpp.gen(table_name)

                if tmpl.lang == ProgramLangType.CSHARP:
                    trans_csharp = TransCsharp(tmpl.publish, field_types, field_descs)
                    trans_csharp.gen(table_name)

                if tmpl.lang == ProgramLangType.LUA:
                    trans_lua = TransLua(tmpl.publish)
                    trans_lua.gen(table_name)
                
                if tmpl.lang == ProgramLangType.GO:
                    trans_go = TransGo(tmpl.publish, field_types, field_descs)
                    trans_go.gen(table_name)
                    
            print("transport table ", excel_name, " succ")
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
