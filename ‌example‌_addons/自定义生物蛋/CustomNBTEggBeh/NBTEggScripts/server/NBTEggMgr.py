# -*- coding: UTF-8 -*-
import mod.server.extraServerApi as serverApi

ServerSystem = serverApi.GetServerSystemCls()
CompFactory = serverApi.GetEngineCompFactory()


class Main(ServerSystem):

    def __init__(self, namespace, system_name):
        ServerSystem.__init__(self, namespace, system_name)
        namespace, system = serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName()
        self.ListenForEvent(namespace, system, "ServerItemUseOnEvent", self, self.onItemUseOn)
        self.ListenForEvent(namespace, system, "PlayerAttackEntityEvent", self, self.onPlayerAttackEntity)
        self.mEntitiesNBTList = []
        # 在ServerItemUseOnEvent获得自定义物品的UserData
        CompFactory.CreateItem(serverApi.GetLevelId()).GetUserDataInEvent("ServerItemUseOnEvent")

    def onItemUseOn(self, args):
        mItemDict =  args["itemDict"]
        # 判断是否是精灵蛋
        if mItemDict["newItemName"] == "design:nbt_egg":
            x = args["x"]
            y = args["y"]
            z = args["z"]
            # 修改NBT的坐标数据
            mItemDict["userData"]["Pos"][0]["__value__"] = x
            # 位置提高1格，避免生物窒息在方块内
            mItemDict["userData"]["Pos"][1]["__value__"] = y + 1
            mItemDict["userData"]["Pos"][2]["__value__"] = z
            # 创建带有NBT标签的实体
            self.CreateEngineEntityByNBT(mItemDict["userData"])
            # 清理掉缓存的NBT数据
            if mItemDict["userData"] in self.mEntitiesNBTList:
                self.mEntitiesNBTList.remove(mItemDict["userData"])
    
    def onPlayerAttackEntity(self, args):
        # 获取被攻击的生物ID
        mVictimId = args["victimId"]
        mDefinitionsComp = CompFactory.CreateEntityDefinitions(mVictimId)
        # 获取生物NBT标签
        mNBTTags = mDefinitionsComp.GetEntityNBTTags()
        mItemDict = {
            "newItemName": "design:nbt_egg",
            "newAuxValue": 0,
            "count": 1,
            "userData": mNBTTags
        }
        foot_pos = CompFactory.CreatePos(mVictimId).GetPos()
        mDimension = CompFactory.CreateDimension(mVictimId).GetEntityDimensionId()
        # 创建一个携带原有实体数据信息的精灵蛋
        self.CreateEngineItemEntity(
            mItemDict,
            mDimension,
            foot_pos
        )
        # 添加缓存
        self.mEntitiesNBTList.append(mNBTTags)