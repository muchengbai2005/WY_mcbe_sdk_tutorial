# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

from enchantEffectBase import EnchantEffectBase

#战利品附魔效果实现函数
class CustomEnchant3(EnchantEffectBase):
    def __init__(self, system, playerId, enchantData):
        super(CustomEnchant3, self).__init__(system, playerId, enchantData)

    def onEnter(self):
        #监听实体受伤事件
        self.mSystem.ListenForEvent(serverApi.GetEngineNamespace(),serverApi.GetEngineSystemName(), "ActuallyHurtServerEvent", self, self.hurtHandler)

    def onExit(self):
        #反监听实体受伤事件
        self.mSystem.UnListenForEvent(serverApi.GetEngineNamespace(),serverApi.GetEngineSystemName(), "ActuallyHurtServerEvent", self, self.hurtHandler)

    def hurtHandler(self, args):
        srcId = args["srcId"]
        dstId = args["entityId"]
        #排除其他实体互相攻击情况，只有玩家冲击可产生掉落物 苹果
        if srcId != self.playerId:
            return

        #苹果的itemDict
        itemDict = {
            'itemName': 'minecraft:apple',
            'count': 1,
            'enchantData': [],
            'auxValue': 0
        }
        compItem = serverApi.GetEngineCompFactory().CreateItem(serverApi.GetLevelId())
        compPos = serverApi.GetEngineCompFactory().CreatePos(dstId)
        spawnPos = compPos.GetPos()
        #在世界中创建苹果
        compItem.SpawnItemToLevel(itemDict, 0, (spawnPos[0], spawnPos[1], spawnPos[2]))