# -*- encoding: utf-8 -*-

import client.extraClientApi as clientApi
from uidemoScripts.modCommon import modConfig
from uidemoScripts.modClient.ui.MenuScreens import SubScreen

ScreenNode = clientApi.GetScreenNodeCls()


class NormalWheelScreen(SubScreen):
	"""
	普通轮盘示例，对应 SelectionWheelScreen_1.json 和 SelectionWheelScreen_2.json 文件
	"""
	def __init__(self, namespace, name, param):
		super(NormalWheelScreen, self).__init__(namespace, name, param)

	def Create(self):
		self.registerCallbacks()

	def getSelectionWheel(self):
		node = self.GetBaseUIControl("/my_selection_wheel")
		if node:
			node = node.asSelectionWheel()
		return node

	def getExitButton(self):
		node = self.GetBaseUIControl("/ExitButton")
		if node:
			node = node.asButton()
		return node

	def registerCallbacks(self):
		wheel = self.getSelectionWheel()
		if wheel:
			# 注册回调
			wheel.SetHoverCallback(self.OnHoverSelectionWheel)
			wheel.SetTouchUpCallback(self.OnPressedSelectionWheel)
		exitButton = self.getExitButton()
		if exitButton:
			exitButton.AddTouchEventParams({"isSwallow": True})
			exitButton.SetButtonTouchUpCallback(self.backToMenu)

	def OnHoverSelectionWheel(self):
		# 打印当前选择的切片index
		currentIndex = self.getSelectionWheel().GetCurrentSliceIndex()
		print("hover: {}".format(currentIndex))

	def OnPressedSelectionWheel(self):
		# 打印当前选择的切片index
		currentIndex = self.getSelectionWheel().GetCurrentSliceIndex()
		print("pressed: {}".format(currentIndex))


class ComplexWheelScreen(SubScreen):
	"""
	复杂轮盘示例，对应 SelectionWheelScreen_3.json 文件
	"""
	def __init__(self, namespace, name, param):
		super(ComplexWheelScreen, self).__init__(namespace, name, param)
		self.isExiting = False
		self.items = [
			{
				"itemName": "minecraft:apple",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取苹果",
			},
			{
				"itemName": "minecraft:iron_shovel",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取铁锹",
			},
			{
				"itemName": "minecraft:iron_axe",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取铁斧",
			},
			{
				"itemName": "minecraft:bow",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取弓",
			},
			{
				"itemName": "minecraft:arrow",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取箭",
			},
			{
				"itemName": "minecraft:diamond",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取钻石",
			},
			{
				"itemName": "minecraft:coal",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取煤炭",
			},
			{
				"itemName": "minecraft:iron_shovel",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取铁锹",
			},
			{
				"itemName": "minecraft:iron_sword",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取铁剑",
			},
			{
				"itemName": "minecraft:gunpowder",
				"auxValue": 0,
				"isEnchanted": False,
				"count": 1,
				"tips": "获取火药",
			},
		]

	def Create(self):
		self.initViewData()
		self.initViewState()
		self.registerCallbacks()

	def initViewData(self):
		# 初始化物品界面
		for idx, data in enumerate(self.items):
			hoverTip = self.getHoverTip(idx)
			if hoverTip:
				hoverTip.SetText(data.get("tips", ""))
			item = self.getItemRenderer(idx)
			if item:
				item.SetUiItem(data.get("itemName", "minecraft:apple"),
					data.get("auxValue", 0), data.get("isEnchanted", False))

	def initViewState(self):
		# 初始化界面状态
		self.setCenterLabel("请选择物品")
		self.isExiting = False
		wheel = self.getSelectionWheel()
		if wheel:
			# 恢复至默认状态
			wheel.SetCurrentSliceIndex(-1)

	def getHoverTip(self, idx):
		path = "/my_selection_wheel/content/changed_controls/state_{}/hover_tip".format(idx)
		node = self.GetBaseUIControl(path)
		if node:
			node = node.asLabel()
		return node

	def getItemRenderer(self, idx):
		path = "/my_selection_wheel/content/unchanged_controls/state_content_{}/item".format(idx)
		node = self.GetBaseUIControl(path)
		if node:
			node = node.asItemRenderer()
		return node

	def getSelectionWheel(self):
		node = self.GetBaseUIControl("/my_selection_wheel")
		if node:
			node = node.asSelectionWheel()
		return node

	def getButton(self, buttonPath):
		node = self.GetBaseUIControl(buttonPath)
		if node:
			node = node.asButton()
		return node

	def setCenterLabel(self, text):
		# 获取中间的Label控件
		node = self.GetBaseUIControl("/my_selection_wheel/content/unchanged_controls/center_label")
		if node:
			node = node.asLabel()
		if node:
			node.SetText(text)

	def registerCallbacks(self):
		wheel = self.getSelectionWheel()
		if wheel:
			# 轮盘注册回调
			wheel.SetHoverCallback(self.OnHoverSelectionWheel)
			wheel.SetTouchUpCallback(self.OnPressedSelectionWheel)
		exitButton = self.getButton("/ExitButton")
		if exitButton:
			exitButton.AddTouchEventParams({"isSwallow": True})
			exitButton.SetButtonTouchUpCallback(self.backToMenu)
		selectButton = self.getButton("/SelectButton")
		if selectButton:
			selectButton.AddTouchEventParams({"isSwallow": True})
			selectButton.SetButtonTouchUpCallback(self.selectWheel)

	def OnHoverSelectionWheel(self):
		if self.isExiting:
			return
		currentIndex = self.getSelectionWheel().GetCurrentSliceIndex()
		if currentIndex == -1:
			# 当前无选择切片的话，就提示 "请选择物品"
			self.setCenterLabel("请选择物品")
			return
		if currentIndex >= len(self.items) or currentIndex < 0:
			return
		# 当前有选择的切片，则提示对应的文本
		self.setCenterLabel(self.items[currentIndex].get("tips", ""))

	def OnPressedSelectionWheel(self):
		if self.isExiting:
			return
		currentIndex = self.getSelectionWheel().GetCurrentSliceIndex()
		if 0 <= currentIndex < len(self.items):
			# 一旦点击选择后，则将会生成对应的物品到玩家背包中
			self.setCenterLabel("正在生成物品{}，生成后将退出界面...".format(self.items[currentIndex].get("itemName", "")))
			comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
			# 这里模拟服务器响应，一段时间后退出当前界面
			comp.AddTimer(2, self.delayBackToMenu)
			# 在退出之前，部分操作将会被屏蔽
			self.isExiting = True
			# 向服务端发起请求，请求生成对应的物品
			if self.clientSystem:
				self.clientSystem.CreateItem(self.items[currentIndex])

	def SetScreenVisible(self, visible):
		# 重写该函数，当界面显示的时候，重新刷新下界面
		super(ComplexWheelScreen, self).SetScreenVisible(visible)
		if visible:
			self.initViewState()

	def delayBackToMenu(self):
		self.isExiting = False
		self.backToMenu()

	def backToMenu(self, args=None):
		if self.isExiting:
			return
		super(ComplexWheelScreen, self).backToMenu(args)

	def selectWheel(self, args):
		# 切换轮盘的选择
		wheel = self.getSelectionWheel()
		count = wheel.GetSliceCount()
		currentIdx = (wheel.GetCurrentSliceIndex() + 1) % count

		def callback():
			wheel.SetCurrentSliceIndex(currentIdx)
			# 模拟hover的效果
			self.OnHoverSelectionWheel()

		comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())
		# 因为点击按钮弹起的事件会影响到轮盘控件，导致轮盘控件切换成默认状态，所以需要延迟一小段事件后设置轮盘才生效
		comp.AddTimer(0.1, callback)
