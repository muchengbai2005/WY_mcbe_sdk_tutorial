# -*- coding: utf-8 -*-
#
import json

import mod.server.extraServerApi as serverApi

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()


class CustomItemsServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomItemsServer, self).__init__(namespace, name)
        print 'CustomItemsServer init'
        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.ServerChatEvent)

    def ServerChatEvent(self, args):
        if args['message'] == 'up':
            playerId = args['playerId']
            import mod.server.extraServerApi as serverApi
            comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
            itemDict = comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.CARRIED, 0, True)
            if itemDict:
                extraId = itemDict['extraId']
                if extraId:
                    extraId = json.loads(extraId)
                else:
                    extraId = {}
                level = extraId.get('level', 0) + 1
                if level > 4:
                    compFactory.CreateMsg(playerId).NotifyOneMessage(playerId, '已经升到最高级')
                    return
                extraId['level'] = level
                itemDict['extraId'] = json.dumps(extraId)
                comp.SetItemLayer(itemDict, 1, 'customitems:top_layer_%d' % level)
                comp.SetItemLayer(itemDict, -1, 'customitems:bottom_layer_%d' % level)
                comp.SpawnItemToPlayerCarried(itemDict, playerId)
                compFactory.CreateMsg(playerId).NotifyOneMessage(playerId, '升级成功')
