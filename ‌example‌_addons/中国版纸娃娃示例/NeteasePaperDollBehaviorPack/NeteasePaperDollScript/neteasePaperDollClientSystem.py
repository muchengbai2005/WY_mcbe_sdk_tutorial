# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()


class NeteasePaperDollClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self._onUIInitFinished)

    def _onUIInitFinished(self, args):
        clientApi.RegisterUI("NeteasePaperDollDemo", "gate", "NeteasePaperDollScript.gateUI.GateUI", "Gate.main")
        clientApi.RegisterUI("NeteasePaperDollDemo", "mainWindow", "NeteasePaperDollScript.mainWindow.MainWindow", "NeteasePaperDoll.main")
        clientApi.CreateUI("NeteasePaperDollDemo", "gate", {"isHud": 1})

    def Destroy(self):
        self.UnListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), "UiInitFinished", self, self._onUIInitFinished)