# _*_coding:utf-8 _*_
import os
import codecs
from tool_define import *
from transtable.trans_define import *


class TransLua:
    def __init__(self, lua_dir):
        self.lua_dir = lua_dir

    def gen(self, table_name):
        s = ""
        tmpl_file = "./transtable/table_lua.tmpl"
        with codecs.open(tmpl_file, "r", "utf-8") as f:
            s = f.read()
        if not s:
            return
        s = s % {"class_name": table_name}

        lua_file = os.path.join(self.lua_dir, table_name+'.lua')
        with codecs.open(lua_file, "w", "utf-8", errors='ignore') as f:
            f.write(s)
            f.flush()
            pass
