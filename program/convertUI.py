#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   convertUI.py
@Time    :   2022/02/28 00:08:31
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   None
'''

# here put the import lib
import os
import sys


def ConvertUI():
    print(os.path.abspath(sys.argv[0]))
    path = os.path.split(os.path.abspath(sys.argv[0]))[0]
    os.system("cd "+path)
    print("-------------------------------------------------------")
    print(os.getcwd())

    os.system("pyuic5 -o ./uipy/add_tmpl_ui.py ../designer/ui/add_tmpl.ui")
    os.system("pyuic5 -o ./uipy/modify_enum_ui.py ../designer/ui/modify_enum.ui")
    os.system("pyuic5 -o ./uipy/modify_proto_ui.py ../designer/ui/modify_proto.ui")
    os.system("pyuic5 -o ./uipy/create_proto_ui.py ../designer/ui/create_proto.ui")
    os.system("pyuic5 -o ./uipy/modify_tmpl_ui.py ../designer/ui/modify_tmpl.ui")
    os.system("pyuic5 -o ./uipy/proto_tool_ui.py ../designer/ui/proto_tool.ui")
    os.system("pyuic5 -o ./uipy/setting_ui.py ../designer/ui/setting.ui")
    os.system("pyuic5 -o ./uipy/create_dir_ui.py ../designer/ui/create_dir.ui")
    os.system("pyuic5 -o ./uipy/modify_dir_ui.py ../designer/ui/modify_dir.ui")
    os.system("pyuic5 -o ./uipy/create_enum_ui.py ../designer/ui/create_enum.ui")
    os.system("pyuic5 -o ./uipy/modify_enum_ui.py ../designer/ui/modify_enum.ui")
    # os.system("pyrcc5 -o res_rc.py icons/res.qrc")

    print("transport ui to py ok...")
    print("-------------------------------------------------------")

if __name__ == "__main__":
    ConvertUI()
