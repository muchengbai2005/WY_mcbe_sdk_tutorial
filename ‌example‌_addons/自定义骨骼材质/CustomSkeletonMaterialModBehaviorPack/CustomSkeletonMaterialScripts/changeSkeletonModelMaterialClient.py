# -*- coding: utf-8 -*-
#
from mod_log import logger
import mod.client.extraClientApi as clientApi
compFactory = clientApi.GetEngineCompFactory()

class ChangeSkeletonModelMaterialClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(ChangeSkeletonModelMaterialClient, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = clientApi.GetLevelId()
        self.modelDict = {}
        self.modelMatDict = {}
        # 设置骨骼模型
        localId = clientApi.GetLocalPlayerId()
        comp = compFactory.CreateModel(localId)
        modelId = comp.SetModel("datiangou")
        self.modelDict[localId] = modelId

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished',
                            self, self.OnUIInitFinished)
        self.ListenForEvent('CustomSkeletonModelMaterialMod', 'ChangeSkeletonModelMaterialServer', "ChangeMaterial",
                            self, self.OnChangeMaterial)

    def OnUIInitFinished(self, args):
        clientApi.RegisterUI("CustomSkeletonModelMaterialMod", "instruction",
                             "CustomSkeletonMaterialScripts.ui.MainScreen.MainScreen",
                             "instruction.main")
        clientApi.CreateUI("CustomSkeletonModelMaterialMod", "instruction", {"isHud": 1})
        self.mBaseUINode = clientApi.GetUI("CustomSkeletonModelMaterialMod", "instruction")

    def OnChangeMaterial(self, args):
        entityId = args['entityId']
        comp = compFactory.CreateModel(entityId)
        modelId = self.modelDict.get(entityId, None)
        if modelId:
            if self.modelMatDict.get(entityId, None):
                success = comp.SetModelMaterial(modelId, "default_mat")
                logger.info("change mat : %s", success)
                self.modelMatDict.pop(entityId)
            else:
                # 对该骨骼模型设置自己所定义的材质。
                success = comp.SetModelMaterial(modelId, "mat_skeleton")
                logger.info("change mat : %s", success)
                currentMat = comp.GetModelMaterial(modelId)
                self.modelMatDict[entityId] = currentMat