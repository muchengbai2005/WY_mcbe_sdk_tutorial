# -*- coding: utf-8 -*-

# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import weakref
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()
from functools import wraps


def touch_filter(touchType):
    def touchFilter(func):
        @wraps(func)
        def decorated(*args, **kwargs):
            touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
            touchEvent = args[1]["TouchEvent"]
            if touchType == "up":
                if touchEvent == touchEventEnum.TouchUp:
                    value = func(*args, **kwargs)
                    return value
            if touchType == "down":
                if touchEvent == touchEventEnum.TouchDown:
                    value = func(*args, **kwargs)
                    return value
            if touchType == "cancel":
                if touchEvent == touchEventEnum.TouchCancel:
                    value = func(*args, **kwargs)
                    return value
            if touchType == "move":
                if touchEvent == touchEventEnum.TouchMove:
                    value = func(*args, **kwargs)
                    return value

        return decorated

    return touchFilter


# 所有的UI类需要继承自引擎的ScreenNode类
class UIDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        # 欢迎面板
        self.welcomePanel = "/welcomePanel"
        # client system
        self.clientSystem = weakref.proxy(param['clientSystem'])

    # Create函数是继承自ScreenNode，会在UI创建完成后被调用
    def Create(self):
        print("===== UIDemoScreen Create =====")
        self.welcomePanelItem = self.GetBaseUIControl(self.welcomePanel)
        # 主界面按钮对象
        self.welcomeLabelItem = self.welcomePanelItem.GetChildByPath("/labelDemo").asButton()
        self.welcomeImageItem = self.welcomePanelItem.GetChildByPath("/imageDemo").asButton()
        self.welcomeButtonItem = self.welcomePanelItem.GetChildByPath("/buttonDemo").asButton()
        self.welcomeTextEditItem = self.welcomePanelItem.GetChildByPath("/textEditorDemo").asButton()
        self.welcomeDollItem = self.welcomePanelItem.GetChildByPath("/dollDemo").asButton()
        self.welcomeScrollViewItem = self.welcomePanelItem.GetChildByPath("/scrollViewDemo").asButton()
        self.welcomeProgressBarItem = self.welcomePanelItem.GetChildByPath("/progressBarDemo").asButton()
        self.welcomeToggleItem = self.welcomePanelItem.GetChildByPath("/toggleDemo").asButton()
        self.welcomeGridItem = self.welcomePanelItem.GetChildByPath("/gridDemo").asButton()
        self.welcomeItemRendererItem = self.welcomePanelItem.GetChildByPath("/itemRendererDemo").asButton()
        self.welcomeInputPanelItem = self.welcomePanelItem.GetChildByPath("/inputPanelDemo").asButton()
        self.welcomeRichTextItem = self.welcomePanelItem.GetChildByPath("/RichTextDemo").asButton()
        self.welcomePushScreenItem = self.welcomePanelItem.GetChildByPath("/pushScreenBtn").asButton()
        self.welcomeToggleRadioItem = self.welcomePanelItem.GetChildByPath("/toggleRadioBtn").asButton()
        self.welcomeSliderItem = self.welcomePanelItem.GetChildByPath("/sliderBtn").asButton()
        self.welcomeComboBoxItem = self.welcomePanelItem.GetChildByPath("/NeteaseComboBoxBtn").asButton()
        self.welcomeSelectionWheelItem = self.welcomePanelItem.GetChildByPath("/SelectionWheelBtn").asButton()
        self.welcomeImageRotateItem = self.welcomePanelItem.GetChildByPath("/ImageRotateBtn").asButton()
        self.welcomeUIAniItem = self.welcomePanelItem.GetChildByPath("/UIAnimationBtn").asButton()
        self.ExitBtnItem = self.welcomePanelItem.GetChildByPath("/ExitBtn").asButton()

        # 欢迎界面按钮注册
        self.welcomeLabelItem.AddTouchEventParams({"isSwallow": True, "myParams": 1})
        self.welcomeLabelItem.SetButtonTouchUpCallback(self.OnWelcomeLabelTouch)
        self.welcomeButtonItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeButtonItem.SetButtonTouchUpCallback(self.OnWelcomeButtonTouch)
        self.welcomeImageItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeImageItem.SetButtonTouchUpCallback(self.OnWelcomeImageTouch)
        self.welcomeTextEditItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeTextEditItem.SetButtonTouchUpCallback(self.OnWelcomeTextEditorTouch)
        self.welcomeDollItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeDollItem.SetButtonTouchUpCallback(self.OnWelcomeDollTouch)
        self.welcomeScrollViewItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeScrollViewItem.SetButtonTouchUpCallback(self.OnWelcomeScrollViewTouch)
        self.welcomeProgressBarItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeProgressBarItem.SetButtonTouchUpCallback(self.OnWelcomeProgressBarTouch)
        self.welcomeToggleItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeToggleItem.SetButtonTouchUpCallback(self.OnWelcomeToggleTouch)
        self.welcomeGridItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeGridItem.SetButtonTouchUpCallback(self.OnWelcomeGridTouch)
        self.welcomeItemRendererItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeItemRendererItem.SetButtonTouchUpCallback(self.OnWelcomeItemRendererTouch)
        self.welcomeInputPanelItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeInputPanelItem.SetButtonTouchUpCallback(self.OnWelcomeInputPanel)
        self.welcomeRichTextItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeRichTextItem.SetButtonTouchUpCallback(self.OnWelcomeRichText)
        self.welcomePushScreenItem.AddTouchEventParams({"isSwallow": True})
        self.welcomePushScreenItem.SetButtonTouchUpCallback(self.OnPushScreen)
        self.welcomeToggleRadioItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeToggleRadioItem.SetButtonTouchUpCallback(self.OnToggleRadioBtn)
        self.welcomeSliderItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeSliderItem.SetButtonTouchUpCallback(self.OnSliderBtn)
        self.welcomeComboBoxItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeComboBoxItem.SetButtonTouchUpCallback(self.OnNeteaseComboBox)
        self.welcomeSelectionWheelItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeSelectionWheelItem.SetButtonTouchUpCallback(self.OnSelectionWheel)
        self.welcomeImageRotateItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeImageRotateItem.SetButtonTouchUpCallback(self.OnImageRotate)
        self.welcomeUIAniItem.AddTouchEventParams({"isSwallow": True})
        self.welcomeUIAniItem.SetButtonTouchUpCallback(self.OnUIAnimation)
        self.ExitBtnItem.AddTouchEventParams({"isSwallow": True})
        self.ExitBtnItem.SetButtonTouchUpCallback(self.ExitScreen)

    def ExitScreen(self, args):
        clientApi.SetInputMode(0)
        clientApi.SetResponse(True)
        clientApi.HideSlotBarGui(False)
        self.SetScreenVisible(False)

    # 界面的一些初始化操作
    def Init(self):
        # 隐藏瞄准界面
        clientApi.SetInputMode(1)
        clientApi.SetResponse(False)
        clientApi.HideSlotBarGui(True)
        self.SetScreenVisible(True)
        self.welcomePanelItem.SetVisible(True)

    # 继承自ScreenNode的方法，会被引擎自动调用，1秒钟30帧
    def Update(self):
        """
        node tick function
        """
        pass

    def OnWelcomeLabelTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('LabelText', True)

    def OnWelcomeImageTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Image', True)

    def OnWelcomeButtonTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Image', True)

    def OnWelcomeTextEditorTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('LabelText', True)

    def OnWelcomeDollTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Doll', True)

    def OnWelcomeScrollViewTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('ScrollView', True)

    def OnWelcomeProgressBarTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('ProgressBar', True)

    def OnWelcomeToggleTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Toggle', True)

    def OnWelcomeGridTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Grid', True)

    def OnWelcomeItemRendererTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('ItemRenderer', True)

    def OnWelcomeInputPanel(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('InputPanel', True)

    def OnWelcomeRichText(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('RichText', True)

    def OnPushScreen(self, *args):
        from uidemoScripts.modCommon import modConfig
        clientApi.RegisterUI(modConfig.ModName, modConfig.MainScreenUIName, modConfig.MainScreenPyClsPath, modConfig.MainScreenScreenDef)
        clientApi.PushScreen(modConfig.ModName, modConfig.MainScreenUIName)

    def OnToggleRadioBtn(self, *args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('ToggleRadio', True)

    def OnSliderBtn(self, *args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('Slider', True)

    def OnNeteaseComboBox(self, *args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('NeteaseComboBox', True)

    def OnSelectionWheel(self, *args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('SelectionWheelMenu', True)

    def OnImageRotate(self, *args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('ImageRotateMenu', True)

    def OnUIAnimation(self, *args):
        from uidemoScripts.modCommon import modConfig
        clientApi.PushScreen(modConfig.ModName, modConfig.UIAnimationDemoUIName)
