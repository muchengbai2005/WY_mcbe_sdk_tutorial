# -*- encoding: utf-8 -*-

import client.extraClientApi as clientApi
from uidemoScripts.modCommon import modConfig
from uidemoScripts.modClient.ui.MenuScreens import SubScreen

ScreenNode = clientApi.GetScreenNodeCls()


class SubDemo(SubScreen):
	def __init__(self, namespace, name, param):
		super(SubDemo, self).__init__(namespace, name, param)
		self.desc = ""
		self.canvas = None
		self.sliders = []
		self.updateCalls = {}
		self.cacheData = {}

	def Create(self):
		# 创建返回按钮
		exitBtn = self.CreateChildControl("ImageRotate.ExitButton",
			"exitBtn", None, True).asButton()
		exitBtn.AddTouchEventParams({"isSwallow": True})
		exitBtn.SetButtonTouchUpCallback(self.backToMenu)
		pos = exitBtn.GetPosition()
		# 创建说明文档
		desLabel = self.CreateChildControl("ImageRotate.DescLabel",
			"desc", None, True).asLabel()
		desLabel.SetText("使用说明：\n" + self.desc)
		desLabel.SetPosition((pos[0], pos[1] - desLabel.GetSize()[1] - 10))
		# 创建画布
		self.canvas = self.CreateChildControl("ImageRotate.Canvas",
			"canvas", None, True)

	def Update(self):
		for name in self.updateCalls:
			self.updateCalls[name]()

	def registerUpdate(self, name, callback):
		self.updateCalls[name] = callback

	def createSlider(self, start, end, current, callback, text):
		# 创建slider，设置slider的最小值，最大值，以及当前的值，以及提示文本
		pos = [10, 10]
		if len(self.sliders) > 0:
			position = self.sliders[-1].GetPosition()
			size = self.sliders[-1].GetSize()
			pos[1] = position[1] + size[1] + 5
			pos[0] = position[0]
		name = "slider_{}".format(len(self.sliders))
		sliderPanel = self.CreateChildControl("ImageRotate.SliderWithValue",
			name, None, True)
		sideLabel = self.CreateChildControl("ImageRotate.FlexLabel",
			"label_{}".format(name), None, True).asLabel()
		sliderPanel.SetPosition(tuple(pos))
		sideLabel.SetPosition((pos[0] + sliderPanel.GetSize()[0] + 10, pos[1]))
		sideLabel.SetText(text)
		slider = sliderPanel.GetChildByPath("/slider").asSlider()
		slider.SetSliderValue((current - start) / float(end - start))
		start_label = sliderPanel.GetChildByPath("/panel/start").asLabel()
		end_label = sliderPanel.GetChildByPath("/panel/end").asLabel()
		center_label = sliderPanel.GetChildByPath("/panel/center").asLabel()
		start_label.SetText("{:.1f}".format(start))
		end_label.SetText("{:.1f}".format(end))
		self.cacheData[name] = 0

		# 注册回调函数，每帧检测slider的值是否发生改变，如果发生改变就调用回调
		def sliderWrapper():
			if callable(callback):
				sliderValue = slider.GetSliderValue()
				if self.cacheData[name] != sliderValue:
					value = start + sliderValue * float(end - start)
					callback(value)
					center_label.SetText("{:.1f}".format(value))
					self.cacheData[name] = sliderValue

		self.registerUpdate(name, sliderWrapper)
		self.sliders.append(sliderPanel)

	def createElement(self, defName, name):
		# 在画布上创建控件
		return self.CreateChildControl(defName, name, self.canvas, True)


class RotateDemo(SubDemo):
	"""
	局部旋转接口 Rotate 以及其参数 rotate_pivot 以及 rotate_angle 的理解
	"""
	def __init__(self, namespace, name, param):
		super(RotateDemo, self).__init__(namespace, name, param)
		self.desc = "拖动滑动条进行测试"
		self.pivot = None
		self.target = None
		self.targetSize = None
		self.targetPosition = None
		self.pivotSize = None
		self.currentPivotX = 0.5
		self.currentPivotY = 0.5

	def Create(self):
		super(RotateDemo, self).Create()
		self.createSlider(0, 1, 0.5, self.changePivotX, "调整锚点x")
		self.createSlider(0, 1, 0.5, self.changePivotY, "调整锚点y")
		self.createSlider(-180, 180, 0, self.changeAngle, "调整旋转角度")
		self.target = self.createElement("ImageRotate.image", "target").asImage()
		self.pivot = self.createElement("ImageRotate.Pivot", "pivot").asImage()
		self.pivotSize = self.pivot.GetSize()
		self.targetSize = self.target.GetSize()
		self.targetPosition = self.target.GetPosition()

	def changePivotX(self, value):
		# 修改显示出来的局部锚点控件
		pos = self.pivot.GetPosition()
		if not pos:
			return
		self.pivot.SetPosition((
			self.targetPosition[0] + self.targetSize[0] * value - self.pivotSize[0] / 2,
			pos[1]
		))
		self.currentPivotX = value
		self.updateRotatePivot()

	def changePivotY(self, value):
		# 修改显示出来的局部锚点控件
		pos = self.pivot.GetPosition()
		if not pos:
			return
		self.pivot.SetPosition((
			pos[0],
			self.targetPosition[1] + self.targetSize[1] * value - self.pivotSize[1] / 2
		))
		self.currentPivotY = value
		self.updateRotatePivot()

	def changeAngle(self, angle):
		# 更新局部旋转角度
		self.target.Rotate(angle)

	def updateRotatePivot(self):
		# 更新当前的局部旋转锚点
		self.target.SetRotatePivot((self.currentPivotX, self.currentPivotY))
		print "当前rotate_pivot: {}".format(self.target.GetRotatePivot())


class RotateAroundDemo(SubDemo):
	"""
	全局旋转转接口 RotateAround
	"""
	def __init__(self, namespace, name, param):
		super(RotateAroundDemo, self).__init__(namespace, name, param)
		self.desc = "直接拖动图片上的方块去修改图片围绕旋转的中心，并且可以拖动上面滑动条进行旋转角度的调整"
		self.target = None
		self.globalRotatePivot = None
		self.globalRotateAngle = 0
		self.globalPivotPos = None

	def Create(self):
		super(RotateAroundDemo, self).Create()
		self.createSlider(-180, 180, 0, self.changeAngle, "调整旋转角度")
		self.target = self.createElement("ImageRotate.image", "target").asImage()
		self.globalRotatePivot = self.createElement("ImageRotate.DraggablePivot", "aroundPivot").asButton()
		self.globalRotatePivot.AddTouchEventParams({"isSwallow": True})
		self.registerUpdate("checkPivotChanged", self.checkPivotChanged)
		self.globalPivotPos = self.globalRotatePivot.GetGlobalPosition()

	def changeAngle(self, angle):
		# 更新全局旋转角度
		self.globalRotateAngle = angle
		self.updateGlobalRotation()

	def checkPivotChanged(self):
		# 检测全局锚点位置是否发生改变
		pos = self.globalRotatePivot.GetGlobalPosition()
		if not pos:
			return
		if pos != self.globalPivotPos:
			self.globalPivotPos = pos
			self.updateGlobalRotation()

	def updateGlobalRotation(self):
		# 需要注意，RotateAround 接口传入的坐标是全局坐标而非局部坐标（用GetGlobalPosition，而不是GetPosition）
		print "current global pivot: {}".format(self.globalPivotPos)
		self.target.RotateAround(self.globalPivotPos, self.globalRotateAngle)


class RotateAllDemo(RotateAroundDemo):
	"""
	局部旋转以及全局旋转相结合
	"""
	def __init__(self, namespace, name, param):
		super(RotateAllDemo, self).__init__(namespace, name, param)
		self.localRotateAngle = 0
		self.localRotateSpeed = 0.5

	def Create(self):
		super(RotateAllDemo, self).Create()
		self.registerUpdate("localRotate", self.localRotate)
		# 可以在这里设置局部旋转的锚点
		# self.target.SetRotatePivot((0.5, 0.5))

	def localRotate(self):
		self.localRotateAngle += self.localRotateSpeed
		self.target.Rotate(self.localRotateAngle)


class RotateWithAnimationDemo(SubDemo):
	"""
	动画与旋转的结合
	"""
	def __init__(self, namespace, name, param):
		super(RotateWithAnimationDemo, self).__init__(namespace, name, param)
		self.desc = "拖动滑块查看效果"
		self.globalPivot = None
		self.itemCount = 10
		self.items = []

	def Create(self):
		# 创建足够多的可旋转图片
		super(RotateWithAnimationDemo, self).Create()
		self.createSlider(0, 360.0 / self.itemCount, 0, self.changeItemAngle, "调整旋转角度")
		imagesParent = self.createElement("ImageRotate.StretchObject", "stretch")
		for i in range(self.itemCount):
			name = "item_{}".format(i)
			item = self.CreateChildControl("ImageRotate.StretchItem", name, imagesParent, False)
			self.items.append(item.asImage())
		self.UpdateScreen(True)
		self.globalPivot = imagesParent.GetGlobalPosition()

	def changeItemAngle(self, value):
		for i in range(self.itemCount):
			item = self.items[i]
			# 图片的旋转变换永远是最后作用的，所以都是先进行动画再进行旋转，因此可以把动画看成局部变换
			item.RotateAround(self.globalPivot, value * i)



