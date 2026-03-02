# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

from enchantEffectBase import EnchantEffectBase

#疾行附魔效果实现函数
class CustomEnchant1(EnchantEffectBase):
    def __init__(self, system, playerId, enchantData):
        super(CustomEnchant1, self).__init__(system, playerId, enchantData)

    def onEnter(self):
        level = self.enchantData[1]

        #通过获取自定义附魔等级，修改玩家速度属性
        comp = serverApi.GetEngineCompFactory().CreateAttr(self.playerId)
        comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.15 * level)
        comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.15 * level)

    def onExit(self):
        #附魔效果退出时，重新设置玩家速度属性
        comp = serverApi.GetEngineCompFactory().CreateAttr(self.playerId)
        comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.1)

    #是否为穿戴型附魔
    def isArmorEnchant(self):
        return True