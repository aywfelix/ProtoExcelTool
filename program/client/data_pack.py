#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   data_pack.py
@Time    :   2022/03/08 22:18:18
@Author  :   felix 
@Version :   1.0
@Contact :   laijia2008@126.com
@License :   (C)Copyright 2021-2025, felix&lai
@Desc    :   用于数据封包解包
'''

# here put the import lib
import struct
from tool_define import *

@Singleton
class DataPack(object):
    def __init__(self, parent=None):
        pass
    
    @staticmethod
    def dataPack(self, msg_id, msg_proto):
        msg_pack = None
        msg_content = msg_proto.SerializeToString()
        msg_len = 8 + len(msg_content)
        msg_pack = struct.pack('i', msg_len)
        msg_pack = msg_pack + struct.pack('i', msg_id)
        msg_pack = msg_pack+msg_content
        pass
    
    @staticmethod
    def dataUnpack(self, recv_data):
        msg_len = struct.unpack('i', recv_data[:4])[0]
        msg_id = struct.unpack('i', recv_data[4:8])[0]
        msg_proto = self.getMsgProto()
        msg_content = msg_proto.ParseFromString(recv_data[8:])
        return msg_id, msg_content
        pass
    
    @staticmethod
    def dataLen(self, recv_data):
        msg_len = struct.unpack('i', recv_data[:4])[0]
        return msg_len
        pass
    
    def getMsgProto(self, msg_id):
        return None
        pass
    
# protobuffer 反射实现 https://blog.csdn.net/JMW1407/article/details/107223287
