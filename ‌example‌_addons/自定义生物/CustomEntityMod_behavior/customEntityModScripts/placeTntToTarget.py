# -*- coding: utf-8 -*-
#

import mod.server.extraServerApi as serverApi
CustomGoalCls = serverApi.GetCustomGoalCls()
class PlaceTntToTarget(CustomGoalCls):
    def __init__(self, entityId, argsJson):
        CustomGoalCls.__init__(self, entityId, argsJson)
        self.mFrameCnt = 0
        self.mSummonTntTime = 0

    def _HasTarget(self):
        #是否有仇恨目标
        comp = serverApi.GetEngineCompFactory().CreateAction(self.mEntityId)
        targetId = comp.GetAttackTarget()
        hasTarget = targetId != "-1"
        return hasTarget

    def _IsTargetAlive(self):
        comp = serverApi.GetEngineCompFactory().CreateAction(self.mEntityId)
        targetId = comp.GetAttackTarget()
        comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())
        alive = comp.IsEntityAlive(targetId)
        return alive

    def _MoveToTarget(self):
        # 向目标移动
        comp = serverApi.GetEngineCompFactory().CreateAction(self.mEntityId)
        targetId = comp.GetAttackTarget()
        comp = serverApi.GetEngineCompFactory().CreatePos(targetId)
        targetFootPos = comp.GetFootPos()

        comp = serverApi.GetEngineCompFactory().CreateMoveTo(self.mEntityId)
        comp.SetMoveSetting(targetFootPos, 0.5, 1000)

    def _IsReachTarget(self):
        # 是否接近目标
        comp = serverApi.GetEngineCompFactory().CreateAction(self.mEntityId)
        targetId = comp.GetAttackTarget()
        comp = serverApi.GetEngineCompFactory().CreatePos(targetId)
        targetFootPos = comp.GetFootPos()

        comp = serverApi.GetEngineCompFactory().CreatePos(self.mEntityId)
        selfFootPos = comp.GetFootPos()
        dx = targetFootPos[0] - selfFootPos[0]
        dy = targetFootPos[1] - selfFootPos[1]
        dz = targetFootPos[2] - selfFootPos[2]
        if dx * dx + dy * dy + dz * dz < 4:
            return True
        return False

    def _SummonTnt(self):
        # 向目标放置tnt
        comp = serverApi.GetEngineCompFactory().CreatePos(self.mEntityId)
        selfFootPos = comp.GetFootPos()
        comp = serverApi.GetEngineCompFactory().CreateCommand(serverApi.GetLevelId())
        comp.SetCommand("/summon tnt %s %s %s"%(selfFootPos[0]+1, selfFootPos[1], selfFootPos[2]))  # 传送指令

    def CanUse(self):
        if self._HasTarget() and self._IsTargetAlive():
            return True
        return False

    def CanContinueToUse(self):
        if not self._HasTarget() or not self._IsTargetAlive():
            # 目标已经不合法
            return False
        if self.mSummonTntTime > 0:
            # 已经放置了tnt，不用继续执行了
            return False
        return True

    def CanBeInterrupted(self):
        # print "PlaceTntToTarget CanBeInterrupted", self.mEntityId
        return True

    def Start(self):
        print "PlaceTntToTarget Start", self.mEntityId
        # 重置放置次数
        self.mSummonTntTime = 0
        # 向目标移动
        self._MoveToTarget()

    def Stop(self):
        print "PlaceTntToTarget Stop", self.mEntityId

    def Tick(self):
        if self._IsReachTarget():
            # 若已经接近目标，放置tnt
            self._SummonTnt()
            self.mSummonTntTime += 1
            return
        self.mFrameCnt += 1
        if self.mFrameCnt % 20 == 0:
            self._MoveToTarget()

