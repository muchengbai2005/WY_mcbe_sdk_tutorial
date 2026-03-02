# -*- coding: utf-8 -*-

# 获取客户端引擎API模块
import mod.client.extraClientApi as clientApi
from common.minecraftEnum import NativeScreenDataType
# 获取客户端system的基类ClientSystem
ClientSystem = clientApi.GetClientSystemCls()
NativeScreenManager = clientApi.GetNativeScreenManagerCls()


class Config:
    ModName = "UITutorialMod"
    # UI
    UIDemoUIName = "UIDemo"
    UIDemoUIPyClsPath = "tutorialScripts.screens.UIDemoScreen.UIDemoScreen"
    UIDemoUIScreenDef = "UIDemo.main"


# 在modMain中注册的Client System类
class TutorialClientSystem(ClientSystem):

    # 客户端System的初始化函数
    def __init__(self, namespace, systemName):
        # 首先初始化TutorialClientSystem的基类ClientSystem
        super(TutorialClientSystem, self).__init__(namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(),
            clientApi.GetEngineSystemName(), "UiInitFinished", self, self.OnUIInitFinished)

    # 函数名为Destroy才会被调用，在这个System被引擎回收的时候会调这个函数来销毁一些内容
    def Destroy(self):
        pass

    # 监听引擎初始化完成事件，在这个事件后创建我们的UI
    def OnUIInitFinished(self, args):
        # 代理暂停界面
        NativeScreenManager.instance().RegisterScreenProxy(
            "pause.pause_screen", "tutorialScripts.proxys.PauseScreenProxy.PauseScreenProxy"
        )