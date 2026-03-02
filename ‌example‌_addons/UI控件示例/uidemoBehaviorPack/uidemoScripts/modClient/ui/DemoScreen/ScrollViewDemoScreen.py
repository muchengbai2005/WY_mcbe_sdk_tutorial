# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 滚动列表示例
class ScrollViewDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.scrollViewPanel = "/scrollViewPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.scrollViewPanelItem = self.GetBaseUIControl(self.scrollViewPanel)
        self.demoExitButton = self.scrollViewPanelItem.GetChildByName("ExitButton").asButton()

        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def InitGridLabel(self):
        comp = clientApi.CreateComponent(clientApi.GetLevelId(), "Minecraft", "game")
        comp.AddTimer(1.0, self.reInitGridLabel)

    def reInitGridLabel(self):
        scrollviewItem = self.scrollViewPanelItem.GetChildByName("scroll_view0").asScrollView()
        data = ["data0", "data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10"]
        for index, item in enumerate(self.GetAllChildrenPath(scrollviewItem.GetScrollViewContentPath())):
            index = item[item.rfind('/')+1+10:]
            labelUIControl = self.GetBaseUIControl(item).asLabel()
            labelUIControl.SetText(data[int(index)])

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)

