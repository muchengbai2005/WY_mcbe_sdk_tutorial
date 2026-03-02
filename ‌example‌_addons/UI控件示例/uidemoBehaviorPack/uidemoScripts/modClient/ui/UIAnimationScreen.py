# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class UIAnimationScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.animationPathList = [
			"/alphaImg", "/clipImg", "/colorImg", "/flipbookImg", "/offsetImg", "/sizeImg", "/uvImg", "/normalImg"
		]
		self.animationUIControlList = []
		self.alphaBtn = None
		self.clipBtn = None
		self.colorBtn = None
		self.flipbookBtn = None
		self.offsetBtn = None
		self.sizeBtn = None
		self.uvBtn = None
		self.normalBtn = None
		self.closeBtn = None
		self.resetBtn = None
		self.resumeBtn = None
		self.pauseBtn = None
		self.setAnimationBtn = None
		self.removeAnimationBtn = None
		self.curShowIndex = 0

	def Create(self):
		self.alphaBtn = self.GetBaseUIControl("/alphaBtn").asButton()
		self.clipBtn = self.GetBaseUIControl("/clipBtn").asButton()
		self.colorBtn = self.GetBaseUIControl("/colorBtn").asButton()
		self.flipbookBtn = self.GetBaseUIControl("/flipbookBtn").asButton()
		self.offsetBtn = self.GetBaseUIControl("/offsetBtn").asButton()
		self.sizeBtn = self.GetBaseUIControl("/sizeBtn").asButton()
		self.uvBtn = self.GetBaseUIControl("/uvBtn").asButton()
		self.normalBtn = self.GetBaseUIControl("/normalBtn").asButton()
		self.closeBtn = self.GetBaseUIControl("/closeBtn").asButton()
		self.resetBtn = self.GetBaseUIControl("/resetBtn").asButton()
		self.resumeBtn = self.GetBaseUIControl("/resumeBtn").asButton()
		self.pauseBtn = self.GetBaseUIControl("/pauseBtn").asButton()
		self.setAnimationBtn = self.GetBaseUIControl("/setAnimationBtn").asButton()
		self.removeAnimationBtn = self.GetBaseUIControl("/removeAnimationBtn").asButton()
		self.alphaBtn.AddTouchEventParams()
		self.alphaBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(0, args))
		self.clipBtn.AddTouchEventParams()
		self.clipBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(1, args))
		self.colorBtn.AddTouchEventParams()
		self.colorBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(2, args))
		self.flipbookBtn.AddTouchEventParams()
		self.flipbookBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(3, args))
		self.offsetBtn.AddTouchEventParams()
		self.offsetBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(4, args))
		self.sizeBtn.AddTouchEventParams()
		self.sizeBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(5, args))
		self.uvBtn.AddTouchEventParams()
		self.uvBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(6, args))
		self.normalBtn.AddTouchEventParams()
		self.normalBtn.SetButtonTouchUpCallback( lambda args: self.OnItemClick(7, args))
		self.closeBtn.AddTouchEventParams()
		self.closeBtn.SetButtonTouchUpCallback(self.onCloseBtnClick)
		self.resetBtn.AddTouchEventParams()
		self.resetBtn.SetButtonTouchUpCallback(self.onResetBtnClick)
		self.resumeBtn.AddTouchEventParams()
		self.resumeBtn.SetButtonTouchUpCallback(self.onResumeBtnClick)
		self.pauseBtn.AddTouchEventParams()
		self.pauseBtn.SetButtonTouchUpCallback(self.onPauseBtnClick)
		self.setAnimationBtn.AddTouchEventParams()
		self.setAnimationBtn.SetButtonTouchUpCallback(self.onSetAnimationBtnClick)
		self.removeAnimationBtn.AddTouchEventParams()
		self.removeAnimationBtn.SetButtonTouchUpCallback(self.onRemoveAnimationBtnClick)
		for animationPath in self.animationPathList:
			self.animationUIControlList.append(self.GetBaseUIControl(animationPath))
		# 初始状态，执行第一个示例
		self.OnItemClick(0, {})

	def onCloseBtnClick(self, args):
		self.SetRemove()

	def onResetBtnClick(self, args):
		self.animationUIControlList[self.curShowIndex].resetAnimation()

	def onResumeBtnClick(self, args):
		self.animationUIControlList[self.curShowIndex].PlayAnimation()

	def onPauseBtnClick(self, args):
		self.animationUIControlList[self.curShowIndex].PauseAnimation()

	def onSetAnimationBtnClick(self, args):
		"""
		动画一定要包含命名空间，data的内容就类似 ui.json 中的定义一样（只不过从写进json改为通过代码注入的方式）
		"""
		# 注册两段动画，这两端动画共同构成一整段循环的动画，首段动画名称为 "color_animation_1"
		anim = {
			"namespace": "color_test",
			"color_animation_1": {
				"anim_type": "color",
				"duration": 1.5,
				"from": "red",
				"to": "green",
				"next": "@color_test.color_animation_2"
			},
			"color_animation_2": {
				"anim_type": "color",
				"duration": 1.5,
				"from": "green",
				"to": "red",
				"next": "@color_test.color_animation_1"
			}
		}
		clientApi.RegisterUIAnimations(anim)
		# 注册的动画是作用在颜色属性的，因此添加动画的时候要指定要颜色属性
		# 最后一个参数表示添加动画后自动播放
		self.animationUIControlList[self.curShowIndex].SetAnimation("color", "color_test", "color_animation_1", True)

	def onRemoveAnimationBtnClick(self, *args):
		self.animationUIControlList[self.curShowIndex].RemoveAnimation("color")

	def OnItemClick(self, index, args):
		self.curShowIndex = index
		for i, animationUIControl in enumerate(self.animationUIControlList):
			animationUIControl.SetVisible(i == self.curShowIndex, False)
		self.setAnimationBtn.SetVisible(self.curShowIndex == 7, False)
		self.removeAnimationBtn.SetVisible(self.curShowIndex == 7, False)
		self.UpdateScreen(True)
		self.onResetBtnClick({})
