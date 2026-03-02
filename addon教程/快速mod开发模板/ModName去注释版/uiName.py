# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
import config as DB
Client = clientApi.GetSystem(DB.ModName, 'ClientSystem')
ScreenNode = clientApi.GetScreenNodeCls()
CF = clientApi.GetEngineCompFactory()
PID = clientApi.GetLocalPlayerId()
class uiName(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)

    def Create(self):
        pass

    def Destroy(self):
        pass

    def Update(self):
        pass