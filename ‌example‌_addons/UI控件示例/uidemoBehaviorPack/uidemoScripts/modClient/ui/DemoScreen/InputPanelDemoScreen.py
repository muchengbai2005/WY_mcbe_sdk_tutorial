# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# InputPanel示例
class InputPanelDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.inputPanelPanel = "/inputPanelPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.inputPanelPanelItem = self.GetBaseUIControl(self.inputPanelPanel)
        self.demoInputPanelOpenButton = self.inputPanelPanelItem.GetChildByName("inputPanelOpenBtn").asButton()
        self.demoInputPanelPanel = self.inputPanelPanelItem.GetChildByName("inputPanel")
        self.demoInputPanelCloseButton = self.demoInputPanelPanel.GetChildByName("inputPanelCloseBtn").asButton()
        self.demoExitButton = self.inputPanelPanelItem.GetChildByName("ExitButton").asButton()

        self.demoInputPanelOpenButton.AddTouchEventParams({"isSwallow": True})
        self.demoInputPanelOpenButton.SetButtonTouchUpCallback(self.OnDemoInputPanelOpenBtn)
        self.demoInputPanelCloseButton.AddTouchEventParams({"isSwallow": True})
        self.demoInputPanelCloseButton.SetButtonTouchUpCallback(self.OnDemoInputPanelCloseBtn)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoInputPanelOpenBtn(self, args):
        self.demoInputPanelPanel.SetVisible(True)

    def OnDemoInputPanelCloseBtn(self, args):
        self.demoInputPanelPanel.SetVisible(False)

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
