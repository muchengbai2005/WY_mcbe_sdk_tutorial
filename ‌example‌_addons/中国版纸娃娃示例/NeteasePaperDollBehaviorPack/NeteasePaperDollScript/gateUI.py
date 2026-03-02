# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ScreenNode = clientApi.GetScreenNodeCls()

class GateUI(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.gateButton = "/button"

    def Create(self):
        GoodBtnCtl = self.GetBaseUIControl(self.gateButton).asButton()
        GoodBtnCtl.AddTouchEventParams({"isSwallow": True})
        GoodBtnCtl.SetButtonTouchUpCallback(self._onGateClick)

    def _onGateClick(self, args):
        clientApi.PushScreen("NeteasePaperDollDemo", "mainWindow")

