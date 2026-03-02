# -*- coding: utf-8 -*-
#
import mod.server.extraServerApi as serverApi
from mod_log import logger
compFactory = serverApi.GetEngineCompFactory()

class CustomPlayerServerSystem(serverApi.GetServerSystemCls()):
	def __init__(self, namespace, name):
		super(CustomPlayerServerSystem, self).__init__(namespace, name)
		self.ListenEvent()

	def ListenEvent(self):
		self.ListenForEvent('CustomPlayerMaterialMod', 'CustomPlayerMaterialClient', "ShowMsgEvent",
		                    self, self.OnShowMsgEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ClientLoadAddonsFinishServerEvent",
							self, self.OnAddServerPlayerEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerChatEvent",
							self, self.OnServerChatEvent)
		self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), "ServerItemUseOnEvent",
							self, self.OnServerItemUseOnEvent)

	def OnAddServerPlayerEvent(self, args):
		# 玩家进入世界时发放对应物品
		playerId = args['playerId']
		comp = compFactory.CreateItem(playerId)
		itemDict = {
			'itemName': 'minecraft:apple',
			'count': 1,
			'auxValue': 0,
			'customTips': '§c 改变本地玩家的渲染材质 §r',
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, 0)
		itemDict = {
			'itemName': 'minecraft:diamond',
			'count': 1,
			'auxValue': 0,
			'customTips': '§c 改变本地玩家的渲染几何体 §r',
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, 1)
		itemDict = {
			'itemName': 'minecraft:egg',
			'count': 1,
			'auxValue': 0,
			'customTips': '§c 改变玩家的动画控制流程move.legs §r',
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, 2)
		itemDict = {
			'itemName': 'minecraft:snowball',
			'count': 1,
			'auxValue': 0,
			'customTips': '§c 改变玩家的动画控制流程move.arms §r',
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, 3)

		itemDict = {
			'itemName': 'minecraft:stick',
			'count': 1,
			'auxValue': 0,
			'customTips': '§c 改变move.arms动作的幅度 §r',
		}
		comp.SpawnItemToPlayerInv(itemDict, playerId, 4)

	def OnServerChatEvent(self, args):
		# 聊天框输入change改变玩家材质，再次输入change恢复原来的材质
		if args['message'] == 'change':
			playerId = args['playerId']
			self.BroadcastToAllClient("ChangeMaterial", {"entityId": playerId})

	# 使用对应物品改变玩家的表现
	def OnServerItemUseOnEvent(self, args):
		if args["itemName"] in ["minecraft:apple", "minecraft:egg", "minecraft:snowball", "minecraft:diamond",
								"minecraft:stick"]:
			args["ret"] = True

	def OnShowMsgEvent(self, args):
		comp = compFactory.CreateMsg(args["playerId"])
		comp.NotifyOneMessage(args["playerId"], args["msg"])