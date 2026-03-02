# -*- coding: utf-8 -*-
# 这个文件保存了MOD中使用的一些变量，这样做的好处很多，建议参考

# Mod Version
ModName = "HugoUIDemoMod"
ModVersion = "0.0.1"

# Server System
ServerSystemName = "UIDemoServerSystem"
ServerSystemClsPath = "uidemoScripts.modServer.serverSystem.uidemoServerSystem.UIDemoServerSystem"

# Client System
ClientSystemName = "UIDemoClientSystem"
ClientSystemClsPath = "uidemoScripts.modClient.clientSystem.uidemoClientSystem.UIDemoClientSystem"

# Engine
Minecraft = "Minecraft"

# Server Component
## Engine
EngineTypeComponent = "engineType"
ScriptTypeCompServer = "type"
PosComponent = "pos"
RotComponent = "rot"
ModelCompServer = "model"

# Client Component
## Engine
CameraComponent = "camera"
ModelCompClient = "model"
AudioComponent = "customAudio"
ScriptTypeCompClient = "type"
PathComponent = "path"
FrameAniBindComponent = "frameAniEntityBind"
FrameAniTransComponent = "frameAniTrans"
FrameAniCtrlComponent = "frameAniControl"
ParticleTransComponent = "particleTrans"
ParticleControlComponent = "particleControl"
ParticleBindComponent = "particleEntityBind"
## Custom
CreateItemEvent = "CreateItemEvent"

# Server Event
## Engine
ServerChatEvent = "ServerChatEvent"
ScriptTickServerEvent = "OnScriptTickServer"
AddServerPlayerEvent = "AddServerPlayerEvent"
ProjectileDoHitEffectEvent = "ProjectileDoHitEffectEvent"
##Custom
# Client Event
## Engine
UiInitFinishedEvent = "UiInitFinished"
ScriptTickClientEvent = "OnScriptTickClient"
## Custom


# UI
UIDemoUIName = "UIDemo"
UIDemoUIPyClsPath = "uidemoScripts.modClient.ui.UIDemoScreen.UIDemoScreen"
UIDemoUIScreenDef = "UIDemo.main"

MainScreenUIName = "MainScreen"
MainScreenPyClsPath = "uidemoScripts.modClient.ui.MainScreen.MainScreen"
MainScreenScreenDef = "MainScreen.main"

PushScreenDemoUIName = "PushScreenDemo"
PushScreenPyClsPath = "uidemoScripts.modClient.ui.PushScreenDemo.PushScreenDemo"
PushScreenScreenDef = "PushScreenDemo.main"

UIAnimationDemoUIName = "UIAnimationScreen"
UIAnimationPyClsPath = "uidemoScripts.modClient.ui.UIAnimationScreen.UIAnimationScreen"
UIAnimationScreenDef = "UIAnimationScreen.main"

# 二级界面
LabelTextUIName = "LabelTextDemo"
LabelTextPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.LabelTextDemoScreen.LabelTextDemoScreen"
LabelTextScreenDef = "LabelTextDemo.main"

ImageUIName = "ImageDemo"
ImagePyClsPath = "uidemoScripts.modClient.ui.DemoScreen.ImageDemoScreen.ImageDemoScreen"
ImageScreenDef = "ImageDemo.main"

DollUIName = "DollDemo"
DollPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.DollDemoScreen.DollDemoScreen"
DollScreenDef = "DollDemo.main"

ScrollViewUIName = "ScrollViewDemo"
ScrollViewPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.ScrollViewDemoScreen.ScrollViewDemoScreen"
ScrollViewScreenDef = "ScrollViewDemo.main"

ProgressBarUIName = "ProgressBarDemo"
ProgressBarPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.ProgressBarDemoScreen.ProgressBarDemoScreen"
ProgressBarScreenDef = "ProgressBarDemo.main"

ToggleUIName = "ToggleDemo"
TogglePyClsPath = "uidemoScripts.modClient.ui.DemoScreen.ToggleDemoScreen.ToggleDemoScreen"
ToggleScreenDef = "ToggleDemo.main"

GridUIName = "GridDemo"
GridPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.GridDemoScreen.GridDemoScreen"
GridScreenDef = "GridDemo.main"

ItemRendererUIName = "ItemRendererDemo"
ItemRendererPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.ItemRendererDemoScreen.ItemRendererDemoScreen"
ItemRendererScreenDef = "ItemRendererDemo.main"

InputPanelUIName = "InputPanelDemo"
InputPanelPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.InputPanelDemoScreen.InputPanelDemoScreen"
InputPanelScreenDef = "InputPanelDemo.main"

RichTextUIName = "RichTextDemo"
RichTextPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.RichTextDemoScreen.RichTextDemoScreen"
RichTextScreenDef = "RichTextDemo.main"

SliderUIName = "SliderDemo"
SliderPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.SliderDemoScreen.SliderDemoScreen"
SliderScreenDef = "SliderDemo.main"

NeteaseComboBoxUIName = "NeteaseComboBoxDemo"
NeteaseComboBoxPyClsPath = "uidemoScripts.modClient.ui.DemoScreen.NeteaseComboBoxDemoScreen.NeteaseComboBoxDemoScreen"
NeteaseComboBoxScreenDef = "NeteaseComboBoxDemo.main"


SelectionWheelUIs = [
	["SelectionWheelScreen_menu", "SelectionWheelScreen_menu.main", "uidemoScripts.modClient.ui.MenuScreens.SelectionWheelMenuScreen"],
	["SelectionWheelScreen_1", "SelectionWheelScreen_1.main", "uidemoScripts.modClient.ui.DemoScreen.SelectionWheelScreen.NormalWheelScreen"],
	["SelectionWheelScreen_2", "SelectionWheelScreen_2.main", "uidemoScripts.modClient.ui.DemoScreen.SelectionWheelScreen.NormalWheelScreen"],
	["SelectionWheelScreen_3", "SelectionWheelScreen_3.main", "uidemoScripts.modClient.ui.DemoScreen.SelectionWheelScreen.ComplexWheelScreen"],
]

ImageRotateUIs = [
	["ImageRotateUI_menu", "ImageRotate.MenuScreen", "uidemoScripts.modClient.ui.MenuScreens.ImageRotationMenuScreen"],
	["RotateDemo", "ImageRotate.SubScreen", "uidemoScripts.modClient.ui.DemoScreen.ImageRotateDemoScreen.RotateDemo"],
	["RotateAroundDemo", "ImageRotate.SubScreen", "uidemoScripts.modClient.ui.DemoScreen.ImageRotateDemoScreen.RotateAroundDemo"],
	["RotateAllDemo", "ImageRotate.SubScreen", "uidemoScripts.modClient.ui.DemoScreen.ImageRotateDemoScreen.RotateAllDemo"],
	["RotateWithAnimationDemo", "ImageRotate.SubScreen", "uidemoScripts.modClient.ui.DemoScreen.ImageRotateDemoScreen.RotateWithAnimationDemo"],
]


# Client param

# Server param
