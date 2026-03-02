# -*- encoding: utf-8 -*-

import weakref
# 从客户端API中拿到我们需要的ViewBinder / ViewRequest / ScreenNode
import client.extraClientApi as clientApi

ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


# 富文本示例
class RichTextDemoScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.richTextPanel = "/richTextPanel"
        self.demoRichText_richTextItem = self.richTextPanel + "/richTextPanel"
        self.richTextItem = None
        self.clientSystem = weakref.proxy(param['clientSystem'])

    def Create(self):
        self.richTextPanelItem = self.GetBaseUIControl(self.richTextPanel)
        self.richTextItem = self.GetRichTextItem(self.demoRichText_richTextItem)
        self.richTextItem.registerLinkItemClickCallback(self.OnLinkItemClickCallback)
        self.richTextItem.registerButtonItemClickCallback(self.OnButtonItemClickCallback)
        self.richTextItem.registerRichTextFinishCallback(self.OnRichTextCreateFinishCallback)
        self.demoExitButton = self.richTextPanelItem.GetChildByName("ExitButton").asButton()

        self.demoExitButton.AddTouchEventParams({"isSwallow": True})
        self.demoExitButton.SetButtonTouchUpCallback(self.OnBackToWelcomeTouch)

    def InitRichText(self):
        self.richTextItem.readRichText(
            '[玩家]玩家一<button>{"press_texture" : "textures/ui/btn_pressed","hover_texture" : "textures/ui/btn_hover","default_texture" : "textures/ui/btn_light_default","x":20, "y":20}</button>:恭喜！<image>{"texture":"textures/ui/skin/ty_yuanshenghuli_0_0", "x":30, "y":30}</image>击杀了<link>{"text" : "末影人", "format_code":"§2"}</link><sfx>{"texture": "textures/ui/my_eating_apple","x":30, "y":30,"uv_x": 64,"uv_y": 64,"frame_count": 36,"fps": 10}</sfx>')

    def OnButtonItemClickCallback(self, data, touchX, touchY):
        print("---OnButtonItemClickCallback---", data, touchX, touchY)

    def OnLinkItemClickCallback(self, data, touchX, touchY):
        print("---OnLinkItemClickCallback---", data, touchX, touchY)

    def OnRichTextCreateFinishCallback(self):
        print("---OnRichTextCreateFinishCallback---")

    def OnBackToWelcomeTouch(self, args):
        self.SetScreenVisible(False)
        self.clientSystem.SetScreenVisible('UIDemo', True)
