# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi


class CustomBlocksClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomBlocksClient, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = clientApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'LoadClientAddonScriptsAfter',
                            self, self.LoadClientAddonScriptsAfter)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "FallingBlockCauseDamageBeforeClientEvent",
                            self, self.FallingBlockCauseDamageBeforeClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnAfterFallOnBlockClientEvent",
                            self, self.OnAfterFallOnBlockClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnStandOnBlockClientEvent",
                            self, self.OnStandOnBlockClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "OnEntityInsideBlockClientEvent",
                            self, self.OnEntityInsideBlockClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "StepOnBlockClientEvent",
                            self, self.StepOnBlockClientEvent)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "StepOffBlockClientEvent",
                            self, self.StepOffBlockClientEvent)

    def LoadClientAddonScriptsAfter(self, args):
        # 为原版方块注册OnStandOn、StepOn事件
        comp = clientApi.GetEngineCompFactory().CreateBlockInfo(self.levelId)
        print "为原版粘液块注册客户端on_stand_on组件:", comp.RegisterOnStandOn("minecraft:slime", True)
        print "为原版粘液块注册客户端on_step_on组件:", comp.RegisterOnStepOn("minecraft:slime", True)

# region 毒花（模型花的逻辑拓展展示）事件
    def OnEntityInsideBlockClientEvent(self, args):
        # 不是所有的方块都会触发，只有json中配置了netease:on_entity_inside组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnEntityInside接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_flower_extend":
            args["slowdownMultiX"] = 0.25
            args["slowdownMultiY"] = 0.05
            args["slowdownMultiZ"] = 0.25
# endregion

# region 重力方块相关
    def FallingBlockCauseDamageBeforeClientEvent(self, args):
        # 不是所有重力方块都会触发，只有json中配置了netease:fall组件且send_python_event为true才会触发
        print "FallingBlockCauseDamageBeforeClientEvent", args
# endregion

# region 仿制粘液块事件
    def OnAfterFallOnBlockClientEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_after_fall_on组件且send_python_event为true才会触发
        if args["blockName"] == "customblocks:customblocks_slime":
            is_snakeing = False
            if clientApi.GetLocalPlayerId() == args["entityId"]:
                if clientApi.GetEngineCompFactory().CreatePlayer(args["entityId"]).isSneaking():
                    is_snakeing = True
            if args["motionY"] < 0.0 and not is_snakeing:  # 如果是下落并且不在潜行状态则反弹
                args["motionY"] *= -1
                args["calculate"] = True


    def OnStandOnBlockClientEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_stand_on组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStandOn接口为原版方块注册
        # 仿制粘液块
        if args["blockName"] == "customblocks:customblocks_slime":
            if abs(args["motionY"]) < 0.1:  # 根据“浮空”算普通移动缓速
                scale = 0.4 + abs(args["motionY"]) * 0.2
                scale *= 0.1 # 原版在除该事件外还有其他计算，因此将该值改为0也不能将其固定
                args["motionX"] *= scale
                args["motionZ"] *= scale
        # 原版粘液块
        elif args["blockName"] == "minecraft:slime":
            # 微软原版里客户端是不跑OnStandOn逻辑的
            # 在我们为原版粘液块添加了该组件后会使原版粘液块多跑一部分客户端计算，导致力的计算上有区别
            # 我们可以在客户端把多余的原版力计算给cancel掉，达到和原本一样手感的效果
            args["cancel"] = True

    def StepOnBlockClientEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_step_on组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStepOn接口为原版方块注册
        # 仿制粘液块
        if args["blockName"] == "customblocks:customblocks_slime":
            print "进入仿制粘液块客户端事件", args
        # 原版粘液块
        elif args["blockName"] == "minecraft:slime":
            print "进入原版粘液块客户端事件", args

    def StepOffBlockClientEvent(self, args):
        # 不是所有方块都会触发，只有json中配置了netease:on_step_off组件且send_python_event为true才会触发
        # 原版方块想触发该事件可以通过RegisterOnStepOff接口为原版方块注册
        if args["blockName"] == "customblocks:customblocks_slime":
            print "离开仿制粘液块客户端事件", args
# endregion
