# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 开关示例
class ToggleDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.togglePanel = "/togglePanel"
        self.currentToggleShow = True
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.togglePanelItem = self.GetBaseUIControl(self.togglePanel)
        self.demoToggleLabelItem = self.togglePanelItem.GetChildByPath("/label1")
        self.demoExitButton = self.togglePanelItem.GetChildByName("ExitButton").asButton()

        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    @ViewBinder.binding(ViewBinder.BF_ToggleChanged)
    def OnDemoToggleChangeCallback(self, args):
        self.currentToggleShow = args["state"]
        self.demoToggleLabelItem.SetVisible(self.currentToggleShow)
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_BindBool)
    def ReturnToggleState(self):
        return self.currentToggleShow

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
