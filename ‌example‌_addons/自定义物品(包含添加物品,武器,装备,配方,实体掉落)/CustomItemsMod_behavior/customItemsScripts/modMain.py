# -*- coding: utf-8 -*-
#
from mod.common.mod import Mod
import mod.client.extraClientApi as clientApi
import mod.server.extraServerApi as serverApi

@Mod.Binding(name = "CustomItemsMod", version = "1.0")
class CustomItemsMod(object):

	def __init__(self):
		pass

	@Mod.InitServer()
	def initMod(self):
		serverApi.RegisterSystem("CustomItems", "CustomItemsServer", "customItemsScripts.customItemsServer.CustomItemsServer")

	@Mod.InitClient()
	def init(self):
		clientApi.RegisterSystem("CustomItems", "CustomItemsClient", "customItemsScripts.customItemsClient.CustomItemsClient")