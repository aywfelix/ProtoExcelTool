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
from client.user import *
from proto_xml import *

from google.protobuf import json_format
import codecs
import requests
import json

class NetClient(object):
    def __init__(self, parent=None):
        self.protoXml = ToolProtoXml()

        self.dev_login_url = 'http://192.168.50.78:9999/sys/login'
        self.pro_login_url = ''

        self.user = User()

        self.reactor = selectors.DefaultSelector()
        self.session = Session()
        self.dataPack = DataPack()
        self.msgDefine = {}
        # self.iniMsgDefine()
        self.recordReq = {}
        self.reqHistoryPath = "../extra/tmp/request.json"
        self.loadReqHistory()
        pass

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
    
    def sendMsg(self, msgID, msgClass, msgType, content):
        msgProto = self.dataPack.getMsgProto(msgClass, msgType)
        if not msgProto:
            return
        if not content:
            content = self.recordReq[msgID]
        
        request = json_format.Parse(content, msgProto)

        nMsgID = int(msgID)
        # 登录验证消息特殊处理
        if nMsgID == 7056:
            request.token = self.user.token
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

    # 请求web端进行登录验证
    def webVerifyLogin(self):
        try:
            postdata = {
                'username': self.user.username,
                'password': self.user.password,
                'type': 'game',
            }

            headers = {
                'Content-Type': 'application/json; charset=UTF-8',
                'tenant-id':'d59de7b24a9f11eca01000163e144cbe,ff51a4b4f7f167fedb7e51f451270f99',
            }   

            resp = requests.post(self.dev_login_url, json=postdata, headers=headers)

            if resp.status_code == 200:
                respDict = resp.json()
                result = respDict['result']
                self.user.userInfo = result['userInfo']
                self.user.token = result['token']
                self.user.inviteCode = result['InvitationCodeStatus']
                self.user.wallets = result['wallets']
            else:
                print("http post error, code=", resp.status_code)
                return False

            return True
        except Exception as e:
            print(e)

        return False



