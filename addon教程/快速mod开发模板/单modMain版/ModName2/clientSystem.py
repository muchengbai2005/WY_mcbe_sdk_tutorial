# -*- coding: utf-8 -*-
from ..clientUtils import *
import config as DB
class ClientSystem(ClientBaseSystem):
    @Listen
    def UiInitFinished(self, args):
        print '客户端2 UI框架初始化完成'
        # uiName = 'uiName'
        # clientApi.RegisterUI(DB.ModName, uiName, DB.ModName+'.'+uiName+'.'+uiName, uiName+'.main')
        # self.uiNode = clientApi.CreateUI(DB.ModName, uiName, {'isHud': 1})
        # self.uiNode.xxxxx()