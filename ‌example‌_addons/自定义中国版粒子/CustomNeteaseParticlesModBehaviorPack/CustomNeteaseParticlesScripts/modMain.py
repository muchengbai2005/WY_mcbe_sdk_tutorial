# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name="CustomNeteaseParticlesMod", version="0.0.1")
class CustomPostprocessMod(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def CustomNeteaseParticlesModServerInit(self):
        serverApi.RegisterSystem("CustomNeteaseParticlesMod", "CustomNeteaseParticlesServer", "CustomNeteaseParticlesScripts.customNeteaseParticlesServer.CustomNeteaseParticlesServer")

    @Mod.DestroyServer()
    def CustomNeteaseParticlesModServerDestroy(self):
        pass

    @Mod.InitClient()
    def CustomNeteaseParticlesModClientInit(self):
        clientApi.RegisterSystem("CustomNeteaseParticlesMod", "CustomNeteaseParticlesClient", "CustomNeteaseParticlesScripts.customNeteaseParticlesClient.CustomNeteaseParticlesClient")

    @Mod.DestroyClient()
    def CustomNeteaseParticlesModClientDestroy(self):
        pass
