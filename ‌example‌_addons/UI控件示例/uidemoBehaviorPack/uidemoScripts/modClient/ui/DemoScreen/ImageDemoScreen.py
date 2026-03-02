# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 图片-按钮示例
class ImageDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.imageButtonPanel = "/imageButtonPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.imageButtonPanelItem = self.GetBaseUIControl(self.imageButtonPanel)
        self.imageButton0Item = self.imageButtonPanelItem.GetChildByName("button0").asButton()
        self.imageButton1Item = self.imageButtonPanelItem.GetChildByName("button1").asButton()
        self.demoExitButton = self.imageButtonPanelItem.GetChildByName("ExitButton").asButton()

        self.imageButton0Item.AddTouchEventParams({"isSwallow": True})
        self.imageButton0Item.SetButtonTouchUpCallback(self.OnDemoImageButtonFirstImageTouch)
        self.imageButton1Item.AddTouchEventParams({"isSwallow": True})
        self.imageButton1Item.SetButtonTouchUpCallback(self.OnDemoImageButtonSecondImageTouch)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoImageButtonFirstImageTouch(self, args):
        imageItem = self.imageButtonPanelItem.GetChildByName("image0").asImage()
        if imageItem:
            imageItem.SetSprite("textures/ui/aim")

    def OnDemoImageButtonSecondImageTouch(self, args):
        imageItem = self.imageButtonPanelItem.GetChildByName("image0").asImage()
        if imageItem:
            imageItem.SetSprite("textures/ui/my_cross_hair")

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
