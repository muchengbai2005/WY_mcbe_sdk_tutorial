# -*- coding: utf-8 -*-

import server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
from uidemoScripts.modCommon import modConfig
# 规范地打印log
from mod_log import logger
from uidemoScripts.modCommon import modConfig
# 用来执行一些延迟函数
from uidemoScripts.modServer.serverManager.coroutineMgrGas import CoroutineMgr


class UIDemoServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        logger.info("===== Server Listen =====")
        self.ListenEvent()

    # 在类初始化的时候开始监听
    def ListenEvent(self):
        # 在自定义的ServerSystem中监听引擎的事件ServerChatEvent，回调函数为OnServerChat
        self.ListenForEvent(modConfig.ModName, modConfig.ClientSystemName, modConfig.CreateItemEvent, self, self.OnCreateItemEvent)

    # 在Destroy中调用反注册一些事件
    def UnListenEvent(self):
        pass

    # ServerChatEvent的回调函数（响应函数）
    def OnServerChat(self, args):
        pass

    # ScriptTickServerEvent的回调函数，会在引擎tick的时候调用，1秒30帧（被调用30次）
    def OnTickServer(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    # 这个Update函数是基类的方法，同样会在引擎tick的时候被调用，1秒30帧（被调用30次）
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== UIDemo Server System Destroy =====")
        self.UnListenEvent()

    # 监听CreateItemEvent的回调函数
    def OnCreateItemEvent(self, args):
        print("OnCreateItemEvent")
        # 生成掉落物品
        playerId = args["playerId"]
        item = args["item"]
        # 获取组件工厂，用来创建组件
        compFactory = serverApi.GetEngineCompFactory()
        comp = compFactory.CreateItem(playerId)
        # 调用SpawnItemToPlayerInv接口生成物品到玩家背包，参数参考《MODSDK文档》
        comp.SpawnItemToPlayerInv(item, playerId)
