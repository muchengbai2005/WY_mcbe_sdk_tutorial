# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = 'CustomPlayerMaterialMod', version = "1.0")
class MyMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initServer(self):
		serverApi.RegisterSystem('CustomPlayerMaterialMod', 'CustomPlayerMaterialServer', "CustomPlayerMaterialScripts.customPlayerMaterialServer.CustomPlayerServerSystem")

	@Mod.InitClient()
	def initClient(self):
		clientApi.RegisterSystem('CustomPlayerMaterialMod', 'CustomPlayerMaterialClient', "CustomPlayerMaterialScripts.customPlayerMaterialClient.CustomPlayerClientSystem")