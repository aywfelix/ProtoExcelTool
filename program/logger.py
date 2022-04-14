#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   logger.py
@Time    :   2022/04/14 10:44:45
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   记录一些日志
'''

# here put the import lib
import codecs
from tool_define import *
import os, time


class Logger(object):
    def __init__(self, parent=None):
        pass

    @staticmethod
    def WriteLog(logstr):
        timestr = time.strftime("[%Y-%m-%d %H:%M:%S] ")
        logstr = timestr + logstr + "\n"
        logDir = os.getcwd()+"\\log"
        if not os.path.exists(logDir):
            os.mkdir(logDir)
        now = time.strftime("%Y-%m-%d")
        logFile = os.path.join(logDir, now+".log")
        with open(logFile, 'a+', encoding='GB2312') as f:
            f.write(logstr)
            pass
        pass
        print(logstr)
    pass

# if __name__ == '__main__':
#     Logger.WriteLog("ccccc")
#     Logger.WriteLog("gggg")

