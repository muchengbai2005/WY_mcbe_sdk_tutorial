# -*- coding: utf-8 -*-

from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi

@Mod.Binding(name="NeteasePaperDollScript", version="0.0.1")
class Script_NeteaseModwqNvPTuI(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def NeteasePaperDollScriptServerInit(self):
        pass

    @Mod.DestroyServer()
    def NeteasePaperDollScriptServerDestroy(self):
        pass

    @Mod.InitClient()
    def NeteasePaperDollScriptClientInit(self):
        print "===== init NeteasePaperDollDemo client ====="
        clientApi.RegisterSystem("NeteasePaperDollDemo", "NeteasePaperDollClientSystem", "NeteasePaperDollScript.neteasePaperDollClientSystem.NeteasePaperDollClientSystem")

    @Mod.DestroyClient()
    def NeteasePaperDollScriptClientDestroy(self):
        pass
