# -*- coding: utf-8 -*-
from common.mod import Mod
import server.extraServerApi as serverApi
import client.extraClientApi as clientApi

clients = ('ModName1', 'ModName2')

servers = ('ModName1',)

folderName = __file__.rsplit('/'if'/'in __file__ else'.', 2)[-2]
@Mod.Binding(name = folderName, version = '0.0.1')
class Main(object):
    @Mod.InitServer()
    def ServerInit(self):
        for modName in servers:
            serverApi.RegisterSystem(modName, 'ServerSystem', folderName+'.'+modName+'.serverSystem.ServerSystem')
    @Mod.DestroyServer()
    def ServerDestroy(self):
        pass
    @Mod.InitClient()
    def ClientInit(self):
        for modName in clients:
            clientApi.RegisterSystem(modName, 'ClientSystem', folderName+'.'+modName+'.clientSystem.ClientSystem')
    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass