# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 进度条示例
class ProgressBarDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.progressBarPanel = "/progressBarPanel"
        self.currentProgress = 0.0
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.progressBarPanelItem = self.GetBaseUIControl(self.progressBarPanel)
        self.demoProgressBarValueItem = self.progressBarPanelItem.GetChildByPath("/progress_bar0").asProgressBar("/filled_progress_bar")
        self.demoProgressBarButtonAddItem = self.progressBarPanelItem.GetChildByName("button5").asButton()
        self.demoProgressBarButtonReduceItem = self.progressBarPanelItem.GetChildByName("button4").asButton()
        self.demoExitButton = self.progressBarPanelItem.GetChildByName("ExitButton").asButton()

        self.demoProgressBarButtonAddItem.AddTouchEventParams({"isSwallow": True})
        self.demoProgressBarButtonAddItem.SetButtonTouchUpCallback(self.OnDemoProgressBarAddTouch)
        self.demoProgressBarButtonReduceItem.AddTouchEventParams({"isSwallow": True})
        self.demoProgressBarButtonReduceItem.SetButtonTouchUpCallback(self.OnDemoProgressBarReduceTouch)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def SetCurrentProgress(self):
        self.demoProgressBarValueItem.SetValue(self.currentProgress)

    def OnDemoProgressBarAddTouch(self, args):
        if self.currentProgress >= 1.0:
            return
        self.currentProgress += 0.1
        self.demoProgressBarValueItem.SetValue(self.currentProgress)

    def OnDemoProgressBarReduceTouch(self, args):
        if self.currentProgress <= 0.0:
            return
        self.currentProgress -= 0.1
        self.demoProgressBarValueItem.SetValue(self.currentProgress)

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
