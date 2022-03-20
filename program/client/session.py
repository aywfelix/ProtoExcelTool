#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   session.py
@Time    :   2022/03/08 21:58:12
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   用于协议测试连接会话
'''

# here put the import lib
import socket
import queue
from client.data_pack import *

class Session(object):
    def __init__(self, parent=None):
        self.sock = None
        self.recv_data = None
        self.queue = queue.Queue()
        pass
    
    def conn_server(self, ip, port):
        try:
            self.sock = socket.socket(socket.AF_INET)
            self.sock.connect((ip, port))
            self.sock.setblocking(True) 
            return True   
        except socket.error as e:
            print("connect server error:", e)
        return False
    
    def readData(self, fileobj, mask):
        recv_data = fileobj.recv(4*1024)
        if fileobj != self.sock:
            return
        if self.recv_data is None:
            self.recv_data = recv_data
        else:
            self.recv_data = self.recv_data + recv_data
        while True:
            try:
                if not self.recv_data:
                    break
                if len(self.recv_data) < 8:  # msg_len+msg_id = 8
                    break
                msg_len = DataPack.dataLen(self.recv_data)
                if len(self.recv_data) < msg_len:
                    break
                msg_id, msg_content = DataPack.dataUnpack(self.recv_data)
                self.queue.put((msg_id, msg_content))
                self.recv_data = self.recv_data[msg_len:]
                pass
            except Exception as e:
                print(e)
                break
            pass
        pass
    
    def writeData(self, data):
        self.sock.send(data)
        pass
    
    def close(self):
        self.sock.close()
        self.recv_data = None
        
    def __repr__(self):
        return self.socket.__repr__()
        pass
        
        
    