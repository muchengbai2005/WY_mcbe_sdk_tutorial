# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi
from mod_log import logger
minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()


class CustomNeteaseParticlesServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomNeteaseParticlesServer, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(),
                            serverApi.GetEngineSystemName(),
                            "ServerChatEvent",
                            self, self.OnServerChat)

    def OnServerChat(self, args):
        # 聊天框输入test创建粒子特效及序列帧特效
        if args["message"] == "test":
            self.BroadcastToAllClient("CreateNeteaseEffect", {})
        # 聊天框输入change创建使用自定义材质的粒子特效
        elif args["message"] == "change":
            self.BroadcastToAllClient("CreateCustomMaterialParticleEffect", {})

