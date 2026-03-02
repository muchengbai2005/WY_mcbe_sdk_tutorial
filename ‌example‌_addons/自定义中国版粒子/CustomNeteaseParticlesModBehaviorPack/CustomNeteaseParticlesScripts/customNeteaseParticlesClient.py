# -*- coding: utf-8 -*-
#
from mod_log import logger
import mod.client.extraClientApi as clientApi
compFactory = clientApi.GetEngineCompFactory()

class CustomNeteaseParticlesClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomNeteaseParticlesClient, self).__init__(namespace, name)
        self.ListenEvent()
        self.levelId = clientApi.GetLevelId()
        self.mBaseUINode = None

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished',
                            self, self.OnUIInitFinished)
        self.ListenForEvent('CustomNeteaseParticlesMod', 'CustomNeteaseParticlesServer', "CreateNeteaseEffect",
                            self, self.OnCreateNeteaseEffect)
        self.ListenForEvent('CustomNeteaseParticlesMod', 'CustomNeteaseParticlesServer', "CreateCustomMaterialParticleEffect",
                            self, self.OnCreateCustomMaterialNeteaseEffect)

    def OnUIInitFinished(self, args):
        clientApi.RegisterUI("CustomNeteaseParticlesMod", "instruction",
                             "CustomNeteaseParticlesScripts.ui.MainScreen.MainScreen",
                             "instruction.main")
        clientApi.CreateUI("CustomNeteaseParticlesMod", "instruction", {"isHud": 1})
        self.mBaseUINode = clientApi.GetUI("CustomNeteaseParticlesMod", "instruction")

    def OnCreateNeteaseEffect(self, args):
        comp = clientApi.GetEngineCompFactory().CreatePos(clientApi.GetLocalPlayerId())
        # 获取位置
        entityPos = comp.GetPos()
        # 在玩家的当前位置创建粒子特效
        particleEntityId = self.CreateEngineParticle("effects/test_yanwu.json", (entityPos[0]+1, entityPos[1],entityPos[2]))
        particleControlComp = compFactory.CreateParticleControl(particleEntityId)
        particleControlComp.Play()
        # 在玩家当前位置创建序列帧特效
        frameEntityId = self.CreateEngineSfxFromEditor("effects/test_baoshan.json")
        frameAniTransComp = compFactory.CreateFrameAniTrans(frameEntityId)
        frameAniTransComp.SetPos((entityPos[0]-1, entityPos[1],entityPos[2]))
        frameAniControlComp = compFactory.CreateFrameAniControl(frameEntityId)
        frameAniControlComp.Play()

    def OnCreateCustomMaterialNeteaseEffect(self, args):
        comp = clientApi.GetEngineCompFactory().CreatePos(clientApi.GetLocalPlayerId())
        # 获取位置
        entityPos = comp.GetPos()
        # 在玩家的当前位置创建自定义材质的粒子特效
        particleEntityId = self.CreateEngineParticle("effects/test_yanwu_change.json",
                                                     (entityPos[0], entityPos[1]+1, entityPos[2]))
        particleControlComp = compFactory.CreateParticleControl(particleEntityId)
        particleControlComp.Play()