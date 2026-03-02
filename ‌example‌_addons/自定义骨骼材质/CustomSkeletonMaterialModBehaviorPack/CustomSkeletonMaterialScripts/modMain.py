# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="CustomSkeletonModelMaterialMod", version="0.0.1")
class CustomSkeletonModelMaterialMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def CustomSkeletonModelMaterialModServerInit(self):
        serverApi.RegisterSystem("CustomSkeletonModelMaterialMod", "ChangeSkeletonModelMaterialServer", "CustomSkeletonMaterialScripts.changeSkeletonModelMaterialServer.ChangeSkeletonModelMaterialServer")

    @Mod.DestroyServer()
    def CustomSkeletonModelMaterialModServerDestroy(self):
        pass

    @Mod.InitClient()
    def CustomSkeletonModelMaterialModClientInit(self):
        clientApi.RegisterSystem("CustomSkeletonModelMaterialMod", "ChangeSkeletonModelMaterialClient", "CustomSkeletonMaterialScripts.changeSkeletonModelMaterialClient.ChangeSkeletonModelMaterialClient")

    @Mod.DestroyClient()
    def CustomSkeletonModelMaterialModClientDestroy(self):
        pass
