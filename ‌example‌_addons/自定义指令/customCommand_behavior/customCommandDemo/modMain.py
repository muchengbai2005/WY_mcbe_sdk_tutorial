# -*- coding: utf-8 -*-
from common.mod import Mod
import server.extraServerApi as serverApi
import client.extraClientApi as clientApi
ModName = 'customCommandDemo'
@Mod.Binding(name = ModName, version = '0.0.1')
class Main(object):
    @Mod.InitServer()
    def ServerInit(self):
        serverApi.RegisterSystem(ModName, 'ServerSystem', ModName+'.serverSystem.ServerSystem')
    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass