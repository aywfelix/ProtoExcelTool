#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client_socket.py
@Time    :   2022/03/07 16:44:20
@Author  :   Felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, Felix&Lai
@Desc    :   作为客户端测试协议
'''

# here put the import lib
import os,sys
import socket
from tool_define import *
from google.protobuf import json_format

@Singleton
class ClientSocket(object):
    def __init__(self, parent=None):
        self.socket = None
        pass

    def connServer(self, ip, port):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            port = 11011
            print(ip, port)
            self.socket.connect((ip, port))
            print("connect server[{0}:{1}] ok".format(ip, port))
            return True
        except Exception as e:
            print(e)
            return False

    def disConnect(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        print("disconnect server ok")

    def jsonToPb(self, msg):
        # json_obj='{"a1":1,"a2":2}'
        # # json to pb
        # request = json_format.Parse(json_obj,test_pb2.test())
        # #pb to json  
        # json_result = json_format.MessageToJson(request)
        pass
    
    