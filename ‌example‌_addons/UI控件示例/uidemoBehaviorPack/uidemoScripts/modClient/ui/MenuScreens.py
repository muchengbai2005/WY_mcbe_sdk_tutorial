# -*- coding: utf-8 -*-
import weakref
from functools import partial
import client.extraClientApi as clientApi
from uidemoScripts.modCommon import modConfig
ViewBinder = clientApi.GetViewBinderCls()
ViewRequest = clientApi.GetViewViewRequestCls()
ScreenNode = clientApi.GetScreenNodeCls()


class SubScreen(ScreenNode):
	"""
	作为 Menu 界面的子界面
	"""
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		self.clientSystem = clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName)

	def backToMenu(self, args=None):
		# 返回menu界面
		clientApi.PopScreen()


class MenuScreen(ScreenNode):
	def __init__(self, namespace, name, param):
		ScreenNode.__init__(self, namespace, name, param)
		# client system
		self.clientSystem = clientApi.GetSystem(modConfig.ModName, modConfig.ClientSystemName)
		self.subScreensData = {}
		self.createBtns = {}
		self.subScreens = {}
		self.currentSubScreenNode = None
		self.exitBtn = None

	def Create(self):
		print("MenuScreen Created")
		for subScreenName in self.subScreensData:
			data = self.subScreensData[subScreenName]
			btnPath = data["createBtn"]
			self.createBtns[subScreenName] = self.GetBaseUIControl(btnPath).asButton()
			self.createBtns[subScreenName].AddTouchEventParams()
			self.createBtns[subScreenName].SetButtonTouchUpCallback(partial(self.onShowSubScreen, subScreenName))

		self.exitBtn = self.GetBaseUIControl("/exitBtn").asButton()
		self.exitBtn.AddTouchEventParams()
		self.exitBtn.SetButtonTouchUpCallback(self.onExit)

	def onShowSubScreen(self, name, args):
		data = self.subScreensData[name]
		uiName = data["uiName"]
		self.currentSubScreenNode = clientApi.PushScreen(modConfig.ModName, uiName)

	def onExit(self, args):
		self.SetScreenVisible(False)
		self.clientSystem.SetScreenVisible('UIDemo', True)


class SelectionWheelMenuScreen(MenuScreen):
	def __init__(self, namespace, name, param):
		MenuScreen.__init__(self, namespace, name, param)
		self.subScreensData = {
			"wheel_1": {
				"uiName": modConfig.SelectionWheelUIs[1][0],
				"createBtn": "/wheel_1_btn"
			},
			"wheel_2": {
				"uiName": modConfig.SelectionWheelUIs[2][0],
				"createBtn": "/wheel_2_btn"
			},
			"wheel_3": {
				"uiName": modConfig.SelectionWheelUIs[3][0],
				"createBtn": "/wheel_3_btn"
			}
		}


class ImageRotationMenuScreen(MenuScreen):
	def __init__(self, namespace, name, param):
		MenuScreen.__init__(self, namespace, name, param)
		self.subScreensData = {
			"rotate_1": {
				"uiName": modConfig.ImageRotateUIs[1][0],
				"createBtn": "/stack_panel/rotate_1"
			},
			"rotate_2": {
				"uiName": modConfig.ImageRotateUIs[2][0],
				"createBtn": "/stack_panel/rotate_2"
			},
			"rotate_3": {
				"uiName": modConfig.ImageRotateUIs[3][0],
				"createBtn": "/stack_panel/rotate_3"
			},
			"rotate_4": {
				"uiName": modConfig.ImageRotateUIs[4][0],
				"createBtn": "/stack_panel/rotate_4"
			}
		}
