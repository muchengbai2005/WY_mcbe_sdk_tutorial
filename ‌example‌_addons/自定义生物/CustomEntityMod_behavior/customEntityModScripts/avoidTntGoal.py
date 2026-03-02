# -*- coding: utf-8 -*-
#

import mod.server.extraServerApi as serverApi
import math

CustomGoalCls = serverApi.GetCustomGoalCls()

class AvoidTntGoal(CustomGoalCls):
    def __init__(self, entityId, argsJson):
        CustomGoalCls.__init__(self, entityId, argsJson)
        self.mMinDistTntId = None
        self.mMinDistTntPos = None
        self.mFrameCnt = 0
        self.mMaxSpeedBackup = None
        self.mSpeedBackup = None

    def _GetFootPos(self, entityId):
        comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
        targetFootPos = comp.GetFootPos()
        return targetFootPos

    def _GetPos(self, entityId):
        comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
        return comp.GetPos()

    def _GetBlock(self, pos, dimensionId):
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
        blockDict = comp.GetBlockNew(pos, dimensionId)
        return blockDict

    def _FindNearestTnt(self):
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        entityIdList = comp.GetEntitiesAroundByType(self.mEntityId, 10, serverApi.GetMinecraftEnum().EntityType.PrimedTnt)
        selfPos = self._GetFootPos(self.mEntityId)
        minDist = 999999
        minPos = None
        minTntId = None
        for entityId in entityIdList:
            tntPos = self._GetPos(entityId)
            dx = selfPos[0] - tntPos[0]
            dy = selfPos[1] - tntPos[1]
            dz = selfPos[2] - tntPos[2]
            dist = dx * dx + dy * dy + dz * dz
            if dist < minDist * minDist:
                minDist = dist
                minTntId = entityId
                minPos = tntPos
        return minTntId, minPos

    def _IsEntityAlive(self, entityId):
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        alive = comp.IsEntityAlive(entityId)
        return alive

    def _IsFarawayTnt(self):
        if not self.mMinDistTntPos:
            return True
        selfPos = self._GetFootPos(self.mEntityId)
        dx = selfPos[0] - self.mMinDistTntPos[0]
        dy = selfPos[1] - self.mMinDistTntPos[1]
        dz = selfPos[2] - self.mMinDistTntPos[2]
        if dx * dx + dy * dy + dz * dz > 8 * 8:
            return True
        return False

    def _MoveFarawayTnt(self):
        selfPos = self._GetPos(self.mEntityId)
        # tnt 到 自己的方向
        dirX = selfPos[0] - self.mMinDistTntPos[0]
        dirZ = selfPos[2] - self.mMinDistTntPos[2]
        # 向量归一化
        len = math.sqrt(dirX * dirX + dirZ * dirZ)
        norX = dirX * 1.0 / len
        norZ = dirZ * 1.0 / len
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(serverApi.GetLevelId())
        # 找到远离tnt方向的一个目标点
        targetPosX = selfPos[0] + norX * 3
        targetPosZ = selfPos[2] + norZ * 3
        targetPosY = comp.GetTopBlockHeight((targetPosX, targetPosZ), 0)
        targetPos = (targetPosX, int(targetPosY + 1), targetPosZ)
        # 向目标点移动
        comp = serverApi.GetEngineCompFactory().CreateMoveTo(self.mEntityId)
        comp.SetMoveSetting(targetPos, 0.5, 3000)

    def CanUse(self):
        if self.mMinDistTntId is None:
            # 找到距离最近的tnt
            self.mMinDistTntId, self.mMinDistTntPos = self._FindNearestTnt()
        if self.mMinDistTntId is None:
            return False
        return True

    def CanContinueToUse(self):
        if not self.mMinDistTntId or not self._IsEntityAlive(self.mMinDistTntId):
            # tnt已经不合法
            self.mMinDistTntId = None
            return False
        if self._IsFarawayTnt():
            # 已经远离tnt
            return False
        return True

    def CanBeInterrupted(self):
        return True

    def Start(self):
        # 备份速度属性
        comp = serverApi.GetEngineCompFactory().CreateAttr(self.mEntityId)
        self.mMaxSpeedBackup = comp.GetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED)
        self.mSpeedBackup = comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.SPEED)
        # 加速
        comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.5)
        comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.SPEED, 0.5)
        # 远离tnt
        self._MoveFarawayTnt()

    def Stop(self):
        # 恢复速度属性
        comp = serverApi.GetEngineCompFactory().CreateAttr(self.mEntityId)
        comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED, self.mMaxSpeedBackup)
        comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.SPEED, self.mSpeedBackup)

    def Tick(self):
        self.mFrameCnt += 1
        if self.mFrameCnt % 20 == 0:
            self._MoveFarawayTnt()
