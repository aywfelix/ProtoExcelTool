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
import client.login_pb2 as loginpb
import client.scene_pb2 as scenepb
from google.protobuf import reflection
from google.protobuf import json_format
import codecs
import json

class NetClient(object):
    def __init__(self, parent=None):
        self.reactor = selectors.DefaultSelector()
        self.session = Session()
        self.dataPack = DataPack()
        self.msgDefine = {}
        # self.iniMsgDefine()
        self.recordReq = {}
        self.reqHistoryPath = "../extra/tmp/request.json"
        self.loadReqHistory()
        pass

    # def iniMsgDefine(self):
    #     self.msgDefine[7056] = loginpb.C2SLoginMsg()
    #     self.msgDefine[7057] = loginpb.C2SRoleLoginReq()
    #     self.msgDefine[1050] = loginpb.S2CEnterScene()
    #     pass

    def loadReqHistory(self):
        try:
            content = ""
            with codecs.open(self.reqHistoryPath, 'r', encoding='GB2312') as f:
                content = f.read()
                pass

            self.recordReq = json.loads(content)
        except Exception as e:
            print(e)
        pass

    def getReqHistory(self, msgID):
        return self.recordReq[str(msgID)]
    
    def connect(self, ip, port):
        if self.session.conn_server(ip, port):
            self.reactor.register(
                self.session.sock, selectors.EVENT_READ, self.session.readData)
            return True
        return False
        
    def disconnect(self):
        self.session.close()
        pass
    
    def jsonToPb(self, msg):
    # json_obj='{"a1":1,"a2":2}'
    # # json to pb
    # request = json_format.Parse(json_obj,test_pb2.test())
    # #pb to json  
    # json_result = json_format.MessageToJson(request)
        pass
    
    def sendMsg(self, msgID, content):
        nMsgID = int(msgID)
        descriptor = loginpb.DESCRIPTOR.message_types_by_name['C2SLoginMsg']
        protoMsgType = reflection.MakeClass(descriptor)
        msgProto = protoMsgType()

        if not msgProto:
            return
        if not content:
            content = self.recordReq[msgID]
        
        request = json_format.Parse(content, msgProto)

        # 打包发送消息
        msg = self.dataPack.dataPack2(nMsgID, request)
        if self.session.writeData(msg):
            print("send msg({0}) ok".format(msgID))
        else:
            print("send msg({0}) error".format(msgID))

        # 记录发送消息
        self.recordReq[nMsgID] = content
        pass
    

    # 记录发送历史
    def saveSendHistory(self):
        try:
            with codecs.open(self.reqHistoryPath, 'w+', encoding='GB2312') as f:
                jsonStr = json.dumps(
                    self.recordReq, indent=4, sort_keys=False, ensure_ascii=False)
                f.write(jsonStr + '\n')  
            pass  
        except Exception as e:
            print(e)
            pass

    

