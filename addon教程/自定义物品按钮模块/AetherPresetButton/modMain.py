# -*- coding: utf-8 -*-
from common.mod import Mod
import client.extraClientApi as clientApi
ModName = __file__.rsplit('/'if'/'in __file__ else'.', 2)[-2]
@Mod.Binding(name = ModName, version = '0.0.1')
class Main(object):
    @Mod.InitClient()
    def ClientInit(self):
        if clientApi.GetSystem(ModName, 'ClientSystem'):
            return
        clientApi.RegisterSystem(ModName, 'ClientSystem', ModName+'.ClientSystem'*2)
    @Mod.DestroyClient()
    def ClientDestroy(self):
        pass