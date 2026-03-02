# -*- coding: utf-8 -*-
#
import random

import mod.server.extraServerApi as serverApi

minecraftEnum = serverApi.GetMinecraftEnum()
compFactory = serverApi.GetEngineCompFactory()


class CustomBlocksServer(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, name):
        super(CustomBlocksServer, self).__init__(namespace, name)

        self.ListenEvent()
        self.levelId = serverApi.GetLevelId()


    def ListenEvent(self):
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'LoadServerAddonScriptsAfter',
                            self, self.LoadServerAddonScriptsAfter)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
                            self, self.OnServerChat)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerPlaceBlockEntityEvent',
                            self, self.ServerPlaceBlockEntityEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockEntityTickEvent",
                            self, self.OnBlockEntityTick)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerBlockUseEvent",
                            self, self.ServerBlockUseEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerPlayerTryDestroyBlockEvent",
                            self, self.ServerPlayerTryDestroyBlockEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "BlockStartFallingServerEvent",
                            self, self.BlockStartFallingServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "FallingBlockCauseDamageBeforeServerEvent",
                            self, self.FallingBlockCauseDamageBeforeServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "FallingBlockBreakServerEvent",
                            self, self.FallingBlockBreakServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "FallingBlockReturnHeavyBlockServerEvent",
                            self, self.FallingBlockReturnHeavyBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnBeforeFallOnBlockServerEvent",
                            self, self.OnBeforeFallOnBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnAfterFallOnBlockServerEvent",
                            self, self.OnAfterFallOnBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnStandOnBlockServerEvent",
                            self, self.OnStandOnBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "OnEntityInsideBlockServerEvent",
                            self, self.OnEntityInsideBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StepOnBlockServerEvent",
                            self, self.StepOnBlockServerEvent)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "StepOffBlockServerEvent",
                            self, self.StepOffBlockServerEvent)


    def LoadServerAddonScriptsAfter(self, args):
        self.RegisterBlockPattern()
        # 为原版方块注册OnStandOn、StepOn事件
        comp = serverApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        print "为原版粘液块注册服务端on_stand_on组件:", comp.RegisterOnStandOn("minecraft:slime", True)
        print "为原版粘液块注册服务端on_step_on组件:", comp.RegisterOnStepOn("minecraft:slime", True)


    def RegisterBlockPattern(self):
        levelId = serverApi.GetLevelId()
        # 方块组合
        comp = compFactory.CreateBlock(levelId)
        pattern = [
            ' # ',
            'XXX',
            ' X '
        ]
        defines = {
            '#': 'customblocks:customblocks_test_ore',
            'X': 'customblocks:customblocks_test0'
        }
        print 'RegisterBlockPatterns', comp.RegisterBlockPatterns(pattern, defines, 'minecraft:chicken')

    def OnServerChat(self, args):
        playerId = args["playerId"]
        if args["message"] == "overworld":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(0, pos)
        elif args["message"] == "dm5":
            comp = compFactory.CreatePos(playerId)
            pos = comp.GetPos()
            comp = compFactory.CreateDimension(playerId)
            comp.ChangePlayerDimension(5, pos)

    def ServerBlockUseEvent(self, args):
        blockName = args['blockName']
        blockPos = (args['x'], args['y'], args['z'])
        playerId = args['playerId']
        dimensionComp = compFactory.CreateDimension(playerId)
        dimension = dimensionComp.GetPlayerDimensionId()
        if blockName == 'customblocks:customblocks_test_block_entity':
            comp = compFactory.CreateBlockEntityData(self.levelId)
            blockEntityData = comp.GetBlockEntityData(dimension, blockPos)
            if blockEntityData:
                blockEntityData['key'] = [1, 2, 3]

    def OnBlockEntityTick(self, args):
        # 避免在Tick中频繁输出，易造成卡顿
        # print 'blockEntityTick ', args
        pass

    def ServerPlaceBlockEntityEvent(self, args):
        print 'ServerPlaceBlockEntityEvent  ', args
        dimension = args['dimension']
        blockPos = (args['posX'], args['posY'], args['posZ'])
        blockName = args['blockName']
        comp = compFactory.CreateBlockEntityData(self.levelId)
        blockEntityData = comp.GetBlockEntityData(dimension, blockPos)
        if blockEntityData:
            blockEntityData['abc'] = {"1": True, "2": None, "3": "123"}

    def ServerPlayerTryDestroyBlockEvent(self, args):
        pos = (args["x"], args["y"], args["z"])
        playerId = args['playerId']
        dimensionComp = compFactory.CreateDimension(playerId)
        dimension = dimensionComp.GetPlayerDimensionId()
        comp = compFactory.CreateBlockEntityData(self.levelId)
        blockEntityData = comp.GetBlockEntityData(dimension, pos)
        if blockEntityData:
            # 根据key获取方块实体中对应的value
            value1 = blockEntityData['key']
            value2 = blockEntityData['abc']
            print 'value of "key" is', value1
            print 'value of "abc" is', value2

# region 毒花（模型花的逻辑拓展展示）事件
    def OnEntityInsideBlockServerEvent(self, args):
        # 不是所有的方块都会触发，只有json中配置了netease:on_before_fall_on组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnEntityInside接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_flower_extend":
            args["slowdownMultiX"] = 0.25
            args["slowdownMultiY"] = 0.05
            args["slowdownMultiZ"] = 0.25
# endregion

# region 重力方块事件
# 不是所有重力方块都会触发，只有json中配置了netease:fall组件且send_python_event为true才会触发
    def BlockStartFallingServerEvent(self, args):
        print "BlockStartFallingServerEvent", args

    def FallingBlockCauseDamageBeforeServerEvent(self, args):
        # 如果需要修改部分参数，需配合客户端事件一起修改（详见MODSDK API官网）
        print "FallingBlockCauseDamageBeforeServerEvent", args

    def FallingBlockBreakServerEvent(self, args):
        print "FallingBlockBreakServerEvent", args

    def FallingBlockReturnHeavyBlockServerEvent(self, args):
        print "FallingBlockReturnHeavyBlockServerEvent", args
# endregion

# region 仿制粘液块事件
    def OnBeforeFallOnBlockServerEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_before_fall_on组件且send_python_event为true才会触发
        if args["blockName"] == "customblocks:customblocks_slime":
            if args["fallDistance"] > 0.1: # 此处只做范例，因为可能由于轻微反弹触发多次，因此可以对下落距离做判断触发不同逻辑
                args["fallDistance"] = 0.0  # 将下落距离置0以取消下落伤害，注意为了匹配数据类型得是0.0

    def OnAfterFallOnBlockServerEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_after_fall_on组件且send_python_event为true才会触发
        if args["blockName"] == "customblocks:customblocks_slime":
            is_snakeing = False
            etype = serverApi.GetEngineCompFactory().CreateEngineType(args["entityId"]).GetEngineType()
            if etype & serverApi.GetMinecraftEnum().EntityType.Player == serverApi.GetMinecraftEnum().EntityType.Player:
                if serverApi.GetEngineCompFactory().CreatePlayer(args["entityId"]).isSneaking():
                    is_snakeing = True
            if args["motionY"] < 0.0 and not is_snakeing:  # 如果是下落并且不在潜行状态则反弹
                args["motionY"] *= -1
                args["calculate"] = True

    def OnStandOnBlockServerEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_stand_on组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStandOn接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_slime":
            if abs(args["motionY"]) < 0.1:  # 根据“浮空”算普通移动缓速
                scale = 0.4 + abs(args["motionY"]) * 0.2
                scale *= 0.1 # 原版在除该事件外还有其他计算，因此将该值改为0也不能将其固定
                args["motionX"] *= scale
                args["motionZ"] *= scale
        # 原版粘液块
        elif args["blockName"] == "minecraft:slime":
            # 服务端不设置cancel，保持原版计算
            # # 避免频繁打印
            # print "站在原版粘液块持续触发事件", args 
            pass

    def StepOnBlockServerEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_step_on组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStepOn接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_slime":
            print "进入仿制粘液块服务端事件", args
        # 原版粘液块
        elif args["blockName"] == "minecraft:slime":
            print "进入原版粘液块服务端事件", args

    def StepOffBlockServerEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_step_off组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStepOff接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_slime":
            print "离开仿制粘液块服务端事件", args


# endregion
