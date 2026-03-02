# -*- coding: utf-8 -*-
from ..clientUtils import *
import config as DB
# Client就是你的客户端，你可以用Client.xxx调用客户端函数。
Client = clientApi.GetSystem(DB.ModName, 'ClientSystem')
class uiName(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)

    def Create(self):
        pass

    def Destroy(self):
        pass

    def Update(self):
        pass