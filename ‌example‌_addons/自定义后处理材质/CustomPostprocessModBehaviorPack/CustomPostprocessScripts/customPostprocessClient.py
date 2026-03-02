# -*- coding: utf-8 -*-
#
from mod_log import logger
import mod.client.extraClientApi as clientApi
compFactory = clientApi.GetEngineCompFactory()

class CustomPostprocessClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomPostprocessClient, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = clientApi.GetLevelId()
        # 自定义后处理名称，与resource_pack/graphics_settings/post_process.json中定义的自定义后处理名称一致
        self.postprocessList = ["oldtvDemo", "scanmapDemo"]
        self.postComp = clientApi.GetEngineCompFactory().CreatePostProcess(self.levelId)

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished',
                            self, self.OnUIInitFinished)
        self.ListenForEvent('CustomPostprocessMod', 'CustomPostprocessServer', "ChangePostprocess",
                            self, self.OnChangePostprocess)

    def OnUIInitFinished(self, args):
        clientApi.RegisterUI("CustomPostprocessMod", "instruction",
                             "CustomPostprocessScripts.ui.MainScreen.MainScreen",
                             "instruction.main")
        clientApi.CreateUI("CustomPostprocessMod", "instruction", {"isHud": 1})
        self.mBaseUINode = clientApi.GetUI("CustomPostprocessMod", "instruction")

    def OnChangePostprocess(self, args):
        postprocessName = args["name"]
        # 为了看清单独一个后处理效果，先关闭其他后处理
        for name in self.postprocessList:
            if name != postprocessName:
                self.postComp.SetEnableByName(name, False)
        # 开启对应自定义后处理
        self.postComp.SetEnableByName(postprocessName, True)