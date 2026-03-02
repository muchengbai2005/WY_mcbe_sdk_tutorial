# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 下拉框示例
class NeteaseComboBoxDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.neteaseComboBoxPanel = "/neteaseComboBoxPanel"
        self.autoIncre = 0
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.neteaseComboBoxPanelItem = self.GetBaseUIControl(self.neteaseComboBoxPanel)
        self.demoComboBox = self.neteaseComboBoxPanelItem.GetChildByPath("/comboBoxPanel").asNeteaseComboBox()
        self.demoComboBoxAddBtn = self.neteaseComboBoxPanelItem.GetChildByPath("/addComboBtn").asButton()
        self.demoComboBoxReduceBtn = self.neteaseComboBoxPanelItem.GetChildByPath("/reduceComboBtn").asButton()
        self.demoComboBoxSelectLabel = self.neteaseComboBoxPanelItem.GetChildByPath("/ComboSelectLabel").asLabel()
        self.demoExitButton = self.neteaseComboBoxPanelItem.GetChildByName("ExitButton").asButton()

        self.demoComboBoxAddBtn.AddTouchEventParams({"isSwallow": True})
        self.demoComboBoxAddBtn.SetButtonTouchUpCallback(self.OnDemoComboBoxAdd)
        self.demoComboBoxReduceBtn.AddTouchEventParams({"isSwallow": True})
        self.demoComboBoxReduceBtn.SetButtonTouchUpCallback(self.OnDemoComboBoxReduce)
        self.demoComboBox.RegisterOpenComboBoxCallback(self.onComboBoxOpen)
        self.demoComboBox.RegisterCloseComboBoxCallback(self.onComboBoxClose)
        self.demoComboBox.RegisterSelectItemCallback(self.onComboBoxSelect)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoComboBoxAdd(self, args):
        self.autoIncre += 1
        self.demoComboBox.AddOption("测试项" + str(self.autoIncre))

    def OnDemoComboBoxReduce(self, args):
        self.demoComboBox.RemoveOptionByIndex(0)

    def onComboBoxOpen(self):
        print("---onComboBoxOpen---")

    def onComboBoxClose(self):
        print("---onComboBoxClose---")

    def onComboBoxSelect(self, index, showName, userData):
        if index > -1 and showName:
            self.demoComboBoxSelectLabel.SetText("Select ComboBox, index:" + str(index) + "   showName: " + showName)
        else:
            self.demoComboBoxSelectLabel.SetText("未选中内容")

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
