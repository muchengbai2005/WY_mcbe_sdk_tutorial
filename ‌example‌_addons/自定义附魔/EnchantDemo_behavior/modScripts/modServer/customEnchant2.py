# -*- coding: utf-8 -*-

import mod.server.extraServerApi as serverApi

from enchantEffectBase import EnchantEffectBase

#雷电下落相对于玩家的偏移列表
AROND_POS = [[-5, 0], [5, 0], [0, -5], [0, 5]]
#不同级别雷落的间隔时间，等于越高，时间越短
LEVEL_TIME_MAP = [5, 4, 3]

#雷鸣四方附魔效果实现函数
class CustomEnchant2(EnchantEffectBase):
    def __init__(self, system, playerId, enchantData):
        super(CustomEnchant2, self).__init__(system, playerId, enchantData)
        level = self.enchantData[1]
        #雷落间隔时间
        self.intervalTime = LEVEL_TIME_MAP[level - 1]
        self.tickCnt = 1

    def tick(self):
        self.tickCnt += 1
        #如果间隔时间不足，直接返回，不执行逻辑
        if self.tickCnt < self.intervalTime:
            return

        self.tickCnt = 1
        compCommon = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        compPos = serverApi.GetEngineCompFactory().CreatePos(self.playerId)
        #使用SetCommand接口，在玩家周围落雷
        for offsetPos in AROND_POS:
            compCommon.SetCommand("/summon lightning_bolt %d ~ %d" % (offsetPos[0] + compPos.GetPos()[0], offsetPos[1]  + compPos.GetPos()[2]))

    #是否为穿戴型附魔
    def isArmorEnchant(self):
        return True