# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 文本-文本输入框示例
class LabelTextDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.labelTextPanel = "/labelTextPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])
        self.demoText = ""

    def Create(self):
        self.labelTextPanelItem = self.GetBaseUIControl(self.labelTextPanel)
        self.demoExitButton = self.labelTextPanelItem.GetChildByName("ExitButton").asButton()

        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    @ViewBinder.binding(ViewBinder.BF_EditChanged | ViewBinder.BF_EditFinished)
    def OnDemoLabelTextOnTextEditCallback(self, args):
        self.demoText = args["Text"]
        labelItem = self.labelTextPanelItem.GetChildByName("label0").asLabel()
        if labelItem:
            labelItem.SetText(self.demoText)
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_BindString)
    def ReturnTextString(self):
        return self.demoText

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)