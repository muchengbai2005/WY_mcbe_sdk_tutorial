# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="CustomPostprocessMod", version="0.0.1")
class CustomPostprocessMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def CustomPostprocessModServerInit(self):
        serverApi.RegisterSystem("CustomPostprocessMod", "CustomPostprocessServer", "CustomPostprocessScripts.customPostprocessServer.CustomPostprocessServer")

    @Mod.DestroyServer()
    def CustomPostprocessModServerDestroy(self):
        pass

    @Mod.InitClient()
    def CustomPostprocessModClientInit(self):
        clientApi.RegisterSystem("CustomPostprocessMod", "CustomPostprocessClient", "CustomPostprocessScripts.customPostprocessClient.CustomPostprocessClient")

    @Mod.DestroyClient()
    def CustomPostprocessModClientDestroy(self):
        pass
