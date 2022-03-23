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
from client.reload import *
from google.protobuf import reflection

@Singleton
class DataPack(object):
    def __init__(self, parent=None):
        self.reload = ReLoadFiles()
        pass
    

    def dataPack(self, msg_id, msg_proto):
        msg_pack = None
        msg_content = msg_proto.SerializeToString()
        msg_len = 4 + len(msg_content)
        msg_pack = struct.pack('i', msg_len)
        msg_pack = msg_pack + struct.pack('i', msg_id)
        msg_pack = msg_pack+msg_content
        return msg_pack
        pass

    def dataUnpack(self, recv_data):
        msg_len = struct.unpack('i', recv_data[:4])[0]
        msg_id = struct.unpack('i', recv_data[4:8])[0]
        msg_proto = self.getMsgProto(msg_id)
        msg_content = msg_proto.ParseFromString(recv_data[8:])
        return msg_id, msg_content
        pass


    def dataPack2(self, msg_id, msg_proto):
        msg_pack = None
        msg_content = msg_proto.SerializeToString()
        msg_len = 4 + len(msg_content)
        msg_pack = struct.pack('i', msg_len)
        msg_pack = msg_pack + struct.pack('HH', msg_id, 0)
        msg_pack = msg_pack + msg_content
        return msg_pack
        pass    
    
    def dataUnpack2(self, recv_data):
        msg_len = struct.unpack('i', recv_data[:4])[0]  # msg_len=len(msg_id)+len(msg_content)
        msg_id, _ = struct.unpack('HH', recv_data[4:8])
        msg_proto = self.getMsgProto(msg_id)
        msg_content = msg_proto.ParseFromString(recv_data[8:])
        return msg_id, msg_content
        pass 
    

    def dataLen(self, recv_data):
        msg_len = struct.unpack('i', recv_data[:4])[0]
        return msg_len
        pass


    def getMsgProto(self, msgClass, msgType):
        self.reload.readLoadModule()
        module = self.reload.getModule(msgClass+"_pb2")
        if not module: return None
        descriptor = module.DESCRIPTOR.message_types_by_name[msgType]
        protoMsgType = reflection.MakeClass(descriptor)
        msgProto = protoMsgType()

        if not msgProto:
            return None

        return msgProto
        pass
    
