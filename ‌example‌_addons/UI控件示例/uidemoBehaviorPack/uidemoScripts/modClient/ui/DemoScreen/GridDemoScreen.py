# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 网格示例
class GridDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.gridPanel = "/gridPanel"
        self.demoGrid_grid = "/gridPanel/grid1"
        self.currentGridItemShowNum = -1
        self.maxGridItemShowNum = 0
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.gridPanelItem = self.GetBaseUIControl(self.gridPanel)
        self.demoGridAddButton = self.gridPanelItem.GetChildByName("addBtn").asButton()
        self.demoGridReduceButton = self.gridPanelItem.GetChildByName("reduceBtn").asButton()
        self.demoExitButton = self.gridPanelItem.GetChildByName("ExitButton").asButton()

        self.demoGridAddButton.AddTouchEventParams({"isSwallow": True})
        self.demoGridAddButton.SetButtonTouchUpCallback(self.OnDemoGridAddItemTouch)
        self.demoGridReduceButton.AddTouchEventParams({"isSwallow": True})
        self.demoGridReduceButton.SetButtonTouchUpCallback(self.OnDemoGridReduceItemTouch)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoGridAddItemTouch(self, args):
        gridItemsList = self.GetChildrenName(self.demoGrid_grid)
        if self.maxGridItemShowNum == 0:
            self.maxGridItemShowNum = len(gridItemsList)
        if self.currentGridItemShowNum == -1:
            self.currentGridItemShowNum = self.maxGridItemShowNum
        if self.currentGridItemShowNum < self.maxGridItemShowNum:
            self.currentGridItemShowNum += 1

    def OnDemoGridReduceItemTouch(self, args):
        gridItemsList = self.GetChildrenName(self.demoGrid_grid)
        if self.maxGridItemShowNum == 0:
            self.maxGridItemShowNum = len(gridItemsList)
        if self.currentGridItemShowNum == -1:
            self.currentGridItemShowNum = self.maxGridItemShowNum
        if self.currentGridItemShowNum > 0:
            self.currentGridItemShowNum -= 1

    @ViewBinder.binding_collection(ViewBinder.BF_BindBool, "gridDemo", "#GridDemo.visible")
    def GridItemVisible(self, index):
        gridItemsList = self.GetChildrenName(self.demoGrid_grid)
        if self.maxGridItemShowNum == 0:
            self.maxGridItemShowNum = len(gridItemsList)
        if self.currentGridItemShowNum == -1:
            self.currentGridItemShowNum = self.maxGridItemShowNum
        return index < self.currentGridItemShowNum

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
