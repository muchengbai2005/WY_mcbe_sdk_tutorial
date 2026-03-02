# -*- coding: utf-8 -*-
from ..clientUtils import *
class ClientSystem(ClientBaseSystem):
    # def __init__(self, namespace, systemName):
        # super(ClientSystem, self).__init__(namespace, systemName)
    @Listen
    def UiInitFinished(self, args):
        print '客户端1 UI框架初始化完成'
        self.CallServer('ModName1PlayerUiInitFinished')
    def OnServerSendData(self, text):
        print text