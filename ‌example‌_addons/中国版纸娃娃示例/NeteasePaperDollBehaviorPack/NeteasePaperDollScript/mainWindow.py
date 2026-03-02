# -*- coding: utf-8 -*-

import mod.client.extraClientApi as clientApi
ScreenNode = clientApi.GetScreenNodeCls()

class MainWindow(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        panel = "/panel"
        self.mCloseButton = panel+ "/button"
        self.mEntityInputPanel = panel + "/entity_input_panel"
        self.mSkeletonInputPanel = panel + "/skeleton_input_panel"
        self.mBlockInputPanel = panel + "/block_input_panel"
        self.mEntityPaperDoll = self.mEntityInputPanel + "/entity_paper_doll"
        self.mSkeletonPaperDoll = self.mSkeletonInputPanel + "/skeleton_paper_doll"
        self.mBlockPaperDoll = self.mBlockInputPanel + "/block_paper_doll"

    def Create(self):
        GoodBtnCtl = self.GetBaseUIControl(self.mCloseButton).asButton()
        GoodBtnCtl.AddTouchEventParams({"isSwallow": True})
        GoodBtnCtl.SetButtonTouchUpCallback(self._onCloseClick)
        self._renderEntity()
        self._renderSkeleton()
        self._renderBlock()

    def _renderEntity(self):
        param = {
            "entity_id": clientApi.GetLocalPlayerId(),
            "scale": 0.5,
            "render_depth": -60,
            "init_rot_y": 120,
            "rotation_axis":(0,1,0), # 只绕y轴旋转
            "molang_dict": {"variable.liedownamount": 1}
        }
        doll = self.GetBaseUIControl(self.mEntityPaperDoll).asNeteasePaperDoll()
        doll.RenderEntity(param)

    def _renderSkeleton(self):
        param = {
            "skeleton_model_name": "ty_yuanshenghuli_0_0",
            "animation": "idle_stand",
            "scale": 0.5,
            "render_depth": -50,
            "rotation_axis":(0,1,1),# 绕y、Z轴旋转
            "init_rot_y": 60,
            "molang_dict": {"variable.liedownamount": 1},
            # 控制光照方向为从模型的正右边往左边打光，以及从模型的正前方往后打光
            "light_direction": (1.0, 0.0, 1.0)
        }
        doll = self.GetBaseUIControl( self.mSkeletonPaperDoll).asNeteasePaperDoll()
        doll.RenderSkeletonModel(param)

    def _renderBlock(self):
        blockComp = clientApi.GetEngineCompFactory().CreateBlock(clientApi.GetLevelId())
        comp = clientApi.GetEngineCompFactory().CreatePos(clientApi.GetLocalPlayerId())
        playerPos = comp.GetFootPos()
        palette = blockComp.GetBlockPaletteBetweenPos((playerPos[0]-10, playerPos[1]-10, playerPos[2]-10), (playerPos[0]+1, playerPos[1]-9, playerPos[2]-7))
        if not palette:
            return
        blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(clientApi.GetLevelId())
        blockGeometryComp.CombineBlockPaletteToGeometry(palette, "my_block_geometry")

        param = {
            "block_geometry_model_name": "my_block_geometry",
            "scale": 0.5,
            "rotation_axis": (1, 1, 1),# 绕三轴轴旋转
            "init_rot_y": 60,
            "molang_dict": {"variable.liedownamount": 1}
        }
        doll = self.GetBaseUIControl(self.mBlockPaperDoll).asNeteasePaperDoll()
        doll.RenderBlockGeometryModel(param)

    def _onCloseClick(self, args):
        clientApi.PopScreen()
