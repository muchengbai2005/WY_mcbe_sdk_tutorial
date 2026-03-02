# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi

ClientSystem = clientApi.GetClientSystemCls()
from uidemoScripts.modCommon import modConfig
# 规范地打印log
from mod_log import logger
# 用来执行一些延迟函数，yield 负数为帧数，正数为秒数
from uidemoScripts.modClient.clientManager.coroutineMgrGac import CoroutineMgr


class UIDemoClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        logger.info("===== Client Listen =====")
        self.ListenEvent()
        # 保存ui界面节点
        self.mUIDemoNode = None

        # 二级界面Node字典
        self.mScreenNodeDict = {}

    # 监听引擎和服务端脚本的事件
    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "GridComponentSizeChangedClientEvent", self, self.reInitGridLabel)

    def reInitGridLabel(self, args):
        self.mScreenNodeDict['ScrollView'].reInitGridLabel()

    # 取消监听引擎和服务端脚本事件
    def UnListenEvent(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.UiInitFinishedEvent, self, self.OnUIInitFinished)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), modConfig.ScriptTickClientEvent, self, self.OnTickClient)
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "GridComponentSizeChangedClientEvent", self,
                              self.reInitGridLabel)

    # 设置界面显示
    def SetScreenVisible(self, screenNodeName, flag):
        if screenNodeName in self.mScreenNodeDict and self.mScreenNodeDict[screenNodeName]:
            self.mScreenNodeDict[screenNodeName].SetScreenVisible(flag)

            if screenNodeName == 'UIDemo' and flag:
                self.AllScreenInvisible()
                self.mScreenNodeDict['UIDemo'].SetScreenVisible(True)

            if screenNodeName == 'ScrollView' and flag:
                self.mScreenNodeDict['ScrollView'].InitGridLabel()

            if screenNodeName == 'ProgressBar' and flag:
                self.mScreenNodeDict['ProgressBar'].SetCurrentProgress()

            if screenNodeName == 'Doll' and flag:
                self.mScreenNodeDict['Doll'].SetDollVisible(True)
                self.mScreenNodeDict['Doll'].SetToggleRadioVisible(False)
                self.mScreenNodeDict['Doll'].SetModal(True)

            if screenNodeName == 'RichText' and flag:
                self.mScreenNodeDict['RichText'].InitRichText()

            if screenNodeName == 'ToggleRadio' and flag:
                self.mScreenNodeDict['Doll'].SetDollVisible(False)
                self.mScreenNodeDict['Doll'].SetToggleRadioVisible(True)
                self.mScreenNodeDict['Doll'].SetModal(True)

            if screenNodeName == 'Slider' and flag:
                self.mScreenNodeDict['Slider'].InitSlider()

    # 隐藏所有界面
    def AllScreenInvisible(self):
        for k in self.mScreenNodeDict:
            self.SetScreenVisible(k, False)

    # 创建二级界面UI
    def CreateSecondaryUI(self, uiName, dictName):
        uiNode = clientApi.CreateUI(modConfig.ModName, uiName, {"isHud": 1, 'clientSystem': self})
        self.mScreenNodeDict[dictName] = uiNode

    # 监听引擎初始化完成事件，在这个事件后创建我们的战斗UI
    def OnUIInitFinished(self, args):
        logger.info("OnUIInitFinished : %s", args)
        # 注册UI 详细解释参照《UI API》
        clientApi.RegisterUI(modConfig.ModName, modConfig.UIDemoUIName, modConfig.UIDemoUIPyClsPath, modConfig.UIDemoUIScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.UIAnimationDemoUIName, modConfig.UIAnimationPyClsPath, modConfig.UIAnimationScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.LabelTextUIName, modConfig.LabelTextPyClsPath, modConfig.LabelTextScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.ImageUIName, modConfig.ImagePyClsPath, modConfig.ImageScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.DollUIName, modConfig.DollPyClsPath, modConfig.DollScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.ScrollViewUIName, modConfig.ScrollViewPyClsPath, modConfig.ScrollViewScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.ProgressBarUIName, modConfig.ProgressBarPyClsPath, modConfig.ProgressBarScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.ToggleUIName, modConfig.TogglePyClsPath, modConfig.ToggleScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.GridUIName, modConfig.GridPyClsPath, modConfig.GridScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.ItemRendererUIName, modConfig.ItemRendererPyClsPath, modConfig.ItemRendererScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.InputPanelUIName, modConfig.InputPanelPyClsPath, modConfig.InputPanelScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.RichTextUIName, modConfig.RichTextPyClsPath, modConfig.RichTextScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.SliderUIName, modConfig.SliderPyClsPath, modConfig.SliderScreenDef)
        clientApi.RegisterUI(modConfig.ModName, modConfig.NeteaseComboBoxUIName, modConfig.NeteaseComboBoxPyClsPath, modConfig.NeteaseComboBoxScreenDef)

        for [name, screen_def, pyCls] in modConfig.SelectionWheelUIs:
            clientApi.RegisterUI(modConfig.ModName, name, pyCls, screen_def)

        for [name, screen_def, pyCls] in modConfig.ImageRotateUIs:
            clientApi.RegisterUI(modConfig.ModName, name, pyCls, screen_def)

        # 创建UI 详细解释参照《UI API》，下面是两种获得 uiNode 的方式
        self.mUIDemoNode = clientApi.CreateUI(modConfig.ModName, modConfig.UIDemoUIName, {"isHud": 1, 'clientSystem': self})
        self.mUIDemoNode = clientApi.GetUI(modConfig.ModName, modConfig.UIDemoUIName)
        self.mScreenNodeDict['UIDemo'] = self.mUIDemoNode

        # 创建二级界面UI
        self.CreateSecondaryUI(modConfig.LabelTextUIName, 'LabelText')
        self.CreateSecondaryUI(modConfig.ImageUIName, 'Image')
        self.CreateSecondaryUI(modConfig.DollUIName, 'Doll')
        self.CreateSecondaryUI(modConfig.ScrollViewUIName, 'ScrollView')
        self.CreateSecondaryUI(modConfig.ProgressBarUIName, 'ProgressBar')
        self.CreateSecondaryUI(modConfig.ToggleUIName, 'Toggle')
        self.CreateSecondaryUI(modConfig.GridUIName, 'Grid')
        self.CreateSecondaryUI(modConfig.ItemRendererUIName, 'ItemRenderer')
        self.CreateSecondaryUI(modConfig.InputPanelUIName, 'InputPanel')
        self.CreateSecondaryUI(modConfig.RichTextUIName, 'RichText')
        self.CreateSecondaryUI(modConfig.SliderUIName, 'Slider')
        self.CreateSecondaryUI(modConfig.NeteaseComboBoxUIName, 'NeteaseComboBox')
        self.CreateSecondaryUI(modConfig.SelectionWheelUIs[0][0], 'SelectionWheelMenu')
        self.CreateSecondaryUI(modConfig.ImageRotateUIs[0][0], 'ImageRotateMenu')

        self.mScreenNodeDict['ToggleRadio'] = self.mScreenNodeDict['Doll']

        self.AllScreenInvisible()

        if self.mUIDemoNode:
            def fun():
                self.mUIDemoNode.Init()

            comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
            ret = comp.AddTimer(1, fun)
        else:
            logger.error("create ui %s failed!" % modConfig.UIDemoUIScreenDef)

    # 监听引擎ScriptTickClientEvent事件，引擎会执行该tick回调，1秒钟30帧
    def OnTickClient(self):
        """
        Driven by event, One tick way
        """
        CoroutineMgr.Tick()

    # 被引擎直接执行的父类的重写函数，引擎会执行该Update回调，1秒钟30帧
    def Update(self):
        """
        Driven by system manager, Two tick way
        """
        pass

    # 在清楚该system的时候调用取消监听事件
    def Destroy(self):
        logger.info("===== UIDemo Client System Destroy =====")
        self.UnListenEvent()

    # 向服务端请求生成物品
    def CreateItem(self, item):
        print("CreateItem")
        self.NotifyToServer(modConfig.CreateItemEvent, {"item": item, "playerId": clientApi.GetLocalPlayerId()})