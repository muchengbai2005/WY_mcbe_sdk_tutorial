# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 滑动条示例
class SliderDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.sliderPanel = "/sliderPanel"
        self.sliderValue = 0
        self.sliderAbsValue = 0.5
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.sliderPanelItem = self.GetBaseUIControl(self.sliderPanel)
        self.demoAbsSlider = self.sliderPanelItem.GetChildByPath("/slider0").asSlider()
        self.demoSlider = self.sliderPanelItem.GetChildByPath("/slider1").asSlider()
        self.demoSliderAbsLabelItem = self.sliderPanelItem.GetChildByPath("/slider_label0").asLabel()
        self.demoSliderLabelItem = self.sliderPanelItem.GetChildByPath("/slider_label1").asLabel()
        self.demoExitButton = self.sliderPanelItem.GetChildByName("ExitButton").asButton()

        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def InitSlider(self):
        self.sliderAbsValue = 5.0
        self.demoAbsSlider.SetSliderValue(self.sliderAbsValue)

    @ViewBinder.binding(ViewBinder.BF_SliderChanged | ViewBinder.BF_SliderFinished)
    def OnSliderChange(self, value, isFinish, _unused):
        self.sliderValue = value
        text = str(self.sliderValue)
        if isFinish:
            text += " Finish!"
        self.demoSliderLabelItem.SetText(text)
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_BindFloat)
    def ReturnSliderValue(self):
        return self.sliderValue

    @ViewBinder.binding(ViewBinder.BF_BindInt)
    def ReturnSliderStep(self):
        return 1

    @ViewBinder.binding(ViewBinder.BF_SliderChanged | ViewBinder.BF_SliderFinished)
    def OnAbsSliderChange(self, value, isFinish, _unused):
        self.sliderAbsValue = value
        text = str(self.sliderAbsValue)
        if isFinish:
            text += " Finish!"
        self.demoSliderAbsLabelItem.SetText(text)
        return ViewRequest.Refresh

    @ViewBinder.binding(ViewBinder.BF_BindFloat)
    def ReturnAbsSliderValue(self):
        return self.sliderAbsValue

    @ViewBinder.binding(ViewBinder.BF_BindInt)
    def ReturnAbsSliderStep(self):
        return 10

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
