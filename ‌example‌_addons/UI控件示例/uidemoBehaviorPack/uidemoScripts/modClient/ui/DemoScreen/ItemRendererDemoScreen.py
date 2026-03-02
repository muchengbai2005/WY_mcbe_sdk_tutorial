# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 道具渲染示例
class ItemRendererDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.itemRendererPanel = "/itemRendererPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.itemRendererPanelItem = self.GetBaseUIControl(self.itemRendererPanel)
        self.demoItemRendererUIControl = self.itemRendererPanelItem.GetChildByName("itemRendererWidget").asItemRenderer()
        self.demoItemRendererWoolButton = self.itemRendererPanelItem.GetChildByName("woolRender").asButton()
        self.demoItemRendererWoodButton = self.itemRendererPanelItem.GetChildByName("woodRender").asButton()
        self.demoExitButton = self.itemRendererPanelItem.GetChildByName("ExitButton").asButton()

        self.demoItemRendererWoolButton.AddTouchEventParams({"isSwallow": True})
        self.demoItemRendererWoolButton.SetButtonTouchUpCallback(self.OnDemoItemRendererWoolTouch)
        self.demoItemRendererWoodButton.AddTouchEventParams({"isSwallow": True})
        self.demoItemRendererWoodButton.SetButtonTouchUpCallback(self.OnDemoItemRendererWoodTouch)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoItemRendererWoolTouch(self, args):
        self.demoItemRendererUIControl.SetUiItem('minecraft:wool', 0)

    def OnDemoItemRendererWoodTouch(self, args):
        self.demoItemRendererUIControl.SetUiItem('minecraft:wood', 0)

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
