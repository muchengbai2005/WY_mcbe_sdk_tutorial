# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi
from uidemoScripts.modCommon import modConfig

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 纸娃娃示例
class DollDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.dollPanel = "/dollPanel"
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.dollInputPanel = self.GetBaseUIControl(self.dollPanel).asInputPanel()
        self.SetModal(False)

        self.dollPanelItem = self.GetBaseUIControl(self.dollPanel)
        self.demoDollUIControl = self.dollPanelItem.GetChildByName("paper_doll0").asNeteasePaperDoll()
        self.demoDollButton0Item = self.dollPanelItem.GetChildByName("button2").asButton()
        self.demoDollButton1Item = self.dollPanelItem.GetChildByName("button3").asButton()
        self.demoExitButton = self.dollPanelItem.GetChildByName("ExitButton").asButton()

        self.toggleRadioPanel = self.GetBaseUIControl(self.dollPanel + "/toggleRadioPanel")
        self.button2 = self.GetBaseUIControl(self.dollPanel + "/button2")
        self.button3 = self.GetBaseUIControl(self.dollPanel + "/button3")
        self.paper_doll0 = self.GetBaseUIControl(self.dollPanel + "/paper_doll0")
        self.dollButtonExplain = self.GetBaseUIControl(self.dollPanel + "/dollButtonExplain")

        self.demoDollButton0Item.AddTouchEventParams({"isSwallow": True})
        self.demoDollButton0Item.SetButtonTouchUpCallback(self.OnDemoDollFirstDollTouch)
        self.demoDollButton1Item.AddTouchEventParams({"isSwallow": True})
        self.demoDollButton1Item.SetButtonTouchUpCallback(self.OnDemoDollSecondDollTouch)
        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def OnDemoDollFirstDollTouch(self, args):
        param = {
            "scale": 1.0,
            "entity_identifier": "minecraft:cat",  # 渲染猫的原版模型
            "init_rot_y": 60,
            "molang_dict": {"variable.state": 2, "variable.liedownamount": 1}  # 通过molang变量来调整渲染效果（坐下的猫）
        }
        self.demoDollUIControl.RenderSkeletonModel(param)

    def OnDemoDollSecondDollTouch(self, args):
        param = {
            "scale": 1.0,
            "entity_identifier": "minecraft:cow",  # 渲染牛的原版模型
            "init_rot_y": 60,
            "molang_dict": {"variable.state": 2, "variable.liedownamount": 1}  # 通过molang变量来调整渲染效果（坐下的猫）
        }
        self.demoDollUIControl.RenderSkeletonModel(param)

    # toggle radio panel 单选分页示例
    @ViewBinder.binding(ViewBinder.BF_ToggleChanged, "#toggle_radio_tab")
    def OnToggleChecked(self, args):
        toggleIndex = args["index"]
        if toggleIndex == 0:
            self.clientSystem.SetScreenVisible('LabelText', True)
            self.clientSystem.SetScreenVisible('Image', False)
            self.SetModal(False)
            self.SetDollVisible(False)
        elif toggleIndex == 1:
            self.clientSystem.SetScreenVisible('LabelText', False)
            self.clientSystem.SetScreenVisible('Image', True)
            self.SetModal(False)
            self.SetDollVisible(False)
        elif toggleIndex == 2:
            self.clientSystem.SetScreenVisible('LabelText', False)
            self.clientSystem.SetScreenVisible('Image', False)
            self.SetDollVisible(True)
            self.SetModal(True)

    def SetModal(self, flag):
        self.dollInputPanel.SetIsModal(flag)

    def SetToggleRadioVisible(self, flag):
        self.toggleRadioPanel.SetVisible(flag)

    def SetDollVisible(self, flag):
        self.button2.SetVisible(flag)
        self.button3.SetVisible(flag)
        self.paper_doll0.SetVisible(flag)
        self.dollButtonExplain.SetVisible(flag)

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.SetModal(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
