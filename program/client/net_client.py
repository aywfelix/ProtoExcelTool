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
from time import sleep
from client.session import *
from client.data_pack import *
from client.user import *
from proto_xml import *
from google.protobuf import json_format
import codecs
import requests
import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class NetClient(QMainWindow):
    # 显示请求返回的消息
    ShowMsgSignal = pyqtSignal(str, str)
    # 通知界面重新连接其他服务器
    ConnServerSignal = pyqtSignal(str, int)

    def __init__(self, parent=None):
        super(NetClient, self).__init__()
        self.protoXml = ToolProtoXml()

        self.dev_login_url = 'http://192.168.50.78:9999/sys/login'
        self.pro_login_url = ''

        self.user = User()
        self.session = Session()
        self.dataPack = DataPack()
        self.msgDefine = {}
        self.recordReq = {}
        self.req_history_file = "./config/request.json"
        self.loadReqHistory()
        pass

    def loadReqHistory(self):
        try:
            content = ""
            with codecs.open(self.req_history_file, 'r', encoding='GB2312') as f:
                content = f.read()
                pass

            self.recordReq = json.loads(content)
        except Exception as e:
            self.ShowMsgSignal.emit("", "load req history error:{0}".format(str(e)))
            print(e)
        pass

    def getReqHistory(self, msgID):
        if msgID in self.recordReq.keys():
            return self.recordReq[msgID]
        else:
            return None
    
    def connect(self, ip, port):
        if self.session.conn_server(ip, port):
            print("conn server({0}:{1}) ok".format(ip, port))
            self.startRespShowThrd()
            return True
        return False
        
    def disconnect(self):
        try:
            self.session.close()
            self.isDisconn = True
            self.showRespInfoThrd.join()
        except Exception as e:
            pass
        pass
    
    def sendMsg(self, msgID, msgClass, msgName, content):
        try:
            msgProto = self.dataPack.getMsgProto(msgClass, msgName)
            if not msgProto:
                return
            if not content:
                content = self.recordReq[msgID]
            
            request = json_format.Parse(content, msgProto)

            nMsgID = int(msgID)
            # 登录验证消息特殊处理
            # if nMsgID == 7056:
            #     if not self.webVerifyLogin():
            #         print("client login game error")
            #         return
            #     else:
            #         request.token = self.user.token
            # 打包发送消息
            msg = self.dataPack.dataPack2(nMsgID, request)
            if self.session.writeData(msg):
                print("send msg({0}) ok".format(msgID))
            else:
                print("send msg({0}) error".format(msgID))

            # 记录发送消息
            self.recordReq[msgID] = content
            #print('send msg:{0}, content:{1}'.format(msgID, content))
            pass
        except Exception as e:
            logStr = "send msg error: {0}".format(str(e))
            Logger.WriteLog(logStr)
            self.ShowMsgSignal.emit("", logStr)
    

    # 记录发送历史
    def saveSendHistory(self):
        try:
            with codecs.open(self.req_history_file, 'w+', encoding='GB2312') as f:
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

    def startRespShowThrd(self):
        # 开启一个线程用于显示服务器返回消息
        self.isDisconn = False   
        self.showRespInfoThrd = threading.Thread(target=self.startRespShow)
        self.showRespInfoThrd.start()            
        pass

    def startRespShow(self):
        # 从session的返回消息队列里拿出数据并显示到界面上
        while True:
            try:
                if self.isDisconn:
                    return
                msg = self.session.queue.get(timeout = 1) # 1秒以后没有就抛出异常
                if msg is not None:
                    self.ShowMsgSignal.emit(str(msg[0]), msg[1])
                    print("recv msgid:{0}".format(msg[0]))
                    # if str(msg[0]) == '7000':
                    #     msgDict = json.loads(msg[1])
                    #     ip = msgDict['gwHostname']
                    #     port = int(msgDict['gwPort'])
                    #     self.ConnServerSignal.emit(ip, port)
                    #     pass
                pass
            except Exception as e:
                pass
        pass



