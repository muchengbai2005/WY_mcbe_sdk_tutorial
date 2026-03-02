# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

from enchantEffectBase import EnchantEffectBase

#沉重附魔效果实现函数
class CustomEnchant4(EnchantEffectBase):
    def __init__(self, system, playerId, enchantData):
        super(CustomEnchant4, self).__init__(system, playerId, enchantData)

    #重写tick函数，每次tick给玩家添加2s等级为1的饥饿效果
    def tick(self):
        comp = serverApi.GetEngineCompFactory().CreateEffect(self.playerId)
        comp.AddEffectToEntity("hunger", 2, 1, True)