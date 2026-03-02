# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()


class CustomPostprocessServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomPostprocessServer, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()
        # 自定义后处理名称，与resource_pack/graphics_settings/post_process.json中定义的自定义后处理名称一致
        self.postprocessList = ["oldtvDemo", "scanmapDemo"]

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(),
                            serverApi.GetEngineSystemName(),
                            "ServerChatEvent",
                            self, self.OnServerChat)

    def OnServerChat(self, args):
        # 聊天框输入对应后处理名称("oldtvDemo"或者"scanmapDemo")开启对应自定义后处理
        if args["message"] in self.postprocessList:
            self.BroadcastToAllClient("ChangePostprocess", {"name": args["message"]})

