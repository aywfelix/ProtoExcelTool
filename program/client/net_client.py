#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py
@Time    :   2022/03/08 22:05:10
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   协议测试客户端
'''

# here put the import lib
import selectors
from client.session import *
from client.data_pack import *

class NetClient(object):
    def __init__(self, parent=None):
        self.reactor = selectors.DefaultSelector()
        self.session = Session()
        self.dataPack = DataPack()
        pass
    
    def connect(self, ip, port):
        self.session.close()
        self.session.conn_server(ip, port)
        self.reactor.register(
            self.session.sock, selectors.EVENT_READ, self.session.readData)
        
    def disconnect(self):
        self.session.close()
        print(self.session)
        pass
    
    def jsonToPb(self, msg):
    # json_obj='{"a1":1,"a2":2}'
    # # json to pb
    # request = json_format.Parse(json_obj,test_pb2.test())
    # #pb to json  
    # json_result = json_format.MessageToJson(request)
        pass
    
    def sendMsg(self, data):
        self.session.writeData(data)
        pass
    
    # 发送登录消息
    def sendLoginReq(self, data):
        
        pass

    

