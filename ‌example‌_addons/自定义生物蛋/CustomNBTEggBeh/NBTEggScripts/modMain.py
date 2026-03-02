# -*- coding: UTF-8 -*-

from mod.common.mod import Mod
import mod.server.extraServerApi as serverApi


@Mod.Binding(name="NBTEgg", version="0.1")
class NBTEggScript(object):

    def __init__(self):
        pass

    @Mod.InitClient()
    def init_client(self):
        pass

    @Mod.InitServer()
    def init_server(self):
        serverApi.RegisterSystem("NBTEgg", "NBTEggServer",
                                 "NBTEggScripts.server.NBTEggMgr.Main")

    @Mod.DestroyClient()
    def destroy_client(self):
        pass

    @Mod.DestroyServer()
    def destroy_server(self):
        pass
