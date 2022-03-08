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
from session import *

class Client(object):
    def __init__(self, parent=None):
        self.reactor = selectors.DefaultSelector()
        self.session = Session()
        pass
    
    def connect(self, ip, port):
        self.session.close()
        self.session.conn_server(ip, port)
        self.reactor.register(
            self.session.sock, selectors.EVENT_READ, self.session.readData)
    
    
    

