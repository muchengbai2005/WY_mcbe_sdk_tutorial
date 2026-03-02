# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()


class ChangeSkeletonModelMaterialServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(ChangeSkeletonModelMaterialServer, self).__init__(namespace, name)

        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(),
                            serverApi.GetEngineSystemName(),
                            "ServerChatEvent",
                            self, self.OnServerChat)

    def OnServerChat(self, args):
        # 聊天框输入change改变骨骼模型材质
        playerId = args["playerId"]
        if args["message"] == "change":
            self.BroadcastToAllClient("ChangeMaterial", {"entityId": playerId})

