# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
from client.ui.viewBinder import ViewBinder
CustomUIScreenProxy = clientApi.GetUIScreenProxyCls()


class PauseScreenProxy(CustomUIScreenProxy):
	def __init__(self, screenName, screenNode):
		CustomUIScreenProxy.__init__(self, screenName, screenNode)

	def OnCreate(self):
		print("PauseScreenProxy Create")
		# 在pause.pause_screen被pushed的时候创建一个button以及一个toggle
		self.createCustomButtonAndToggle()

	def OnDestroy(self):
		print("PauseScreenProxy Destroy")

	def OnTick(self):
		pass

	def createCustomButtonAndToggle(self):
		screen = self.GetScreenNode()
		# 使用UI调试工具获取对应的路径，注意，随着版本更新，这个原生界面上的控件路径是可能会改变的。
		button_panel_path = "variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/pause_screen_main_panels/menu/the_rest_panel/pause_menu/menu_button_control/menu_background/button_panel"
		# 获取存放button的stack_panel
		button_panel = screen.GetBaseUIControl(button_panel_path)
		# 添加一小段垂直间隙，这里使用的都是pause命名空间的控件，
		# 当然可以用别的命名空间，为了和pause界面的控件样式一样，就用了这个"pause.vertical_padding"和"pause.pause_button_template"
		verticalPadding = screen.CreateChildControl("pause.vertical_padding", "myPadding", button_panel)
		# 创建Button
		myButton = screen.CreateChildControl("pause.pause_button_template", "myButton", button_panel).asButton()
		# Button的四个控件都需要修改文本
		button_states = ["default", "hover", "pressed", "locked"]
		for s in button_states:
			label_path = "/{}/button_content/common_buttons.new_ui_binding_button_label".format(s)
			label = myButton.GetChildByName(label_path).asLabel()
			label.SetText("我的按钮", True)
		# 添加注册回调，需要注意，如果这里获取的是原生界面中原来有的控件，那么注册回调将会将该控件原有的回调给清除（比如原生界面的逻辑）
		myButton.AddTouchEventParams({"isSwallow": True})
		myButton.SetButtonTouchDownCallback(self.onCustomButtonClicked)

		# 创建Toggle，并且本类支持binding，见本类方法 onToggleChanged
		toggle = screen.CreateChildControl("UIDemo.mytoggle", "myToggle", button_panel)

	def onCustomButtonClicked(self, args):
		print("onCustomButtonClicked: {}".format(args))

	@ViewBinder.binding(ViewBinder.BF_ToggleChanged, "#myMod.myToggle")
	def onToggleChanged(self, args):
		"""
		proxy也支持binding
		"""
		print("myToggle onToggleChanged: {}".format(args))