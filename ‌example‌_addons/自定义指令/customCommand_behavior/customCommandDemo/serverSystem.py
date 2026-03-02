# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()

class ServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(ServerSystem, self).__init__(namespace, systemName)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
        'CustomCommandTriggerServerEvent', self, self.OnCustomCommandTrigger)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
        'ClientLoadAddonsFinishServerEvent', self, self.OnClientLoadAddonsFinish)

    # 关闭新版聊天方便输指令（也可以在编辑器设置里关闭）
    def OnClientLoadAddonsFinish(self, args):
        CF.CreateChatExtension(args['playerId']).Disable()

    def OnCustomCommandTrigger(self, args):
        print '[debug]', args
        if args['command']=='explode':
            # 根据第一个参数确定爆炸位置
            arg0 = args['args'][0]['value']
            if arg0 is None:# 如果是None说明目标选择器未找到目标
                args['return_failed'] = True
                # 可直接填中文，或语言文件里的key
                args['return_msg_key'] = 'commands.generic.noTargetMatch'
                return
            if arg0=='アトリは、高性能ですから':# 如果第一个参数没传，则取origin中的整数位置
                positions = [tuple(x+0.5 for x in args['origin']['blockPos'])]
            # 如果是第一套参数变体，说明传入的首个参数是坐标。
            elif args['variant']==0:
                positions = [arg0]
            else:# 否则第一个参数是实体id列表，获取对应坐标
                positions = [CF.CreatePos(entityId).GetFootPos()for entityId in arg0]
            # 获取name和value的对应字典
            values = {arg['name']: arg['value']for arg in args['args']}
            # 根据玩家或命令方块发送的指令创建爆炸
            createExplosion = CF.CreateExplosion(levelId).CreateExplosion
            for position in positions:
                createExplosion(
                    position,
                    values['爆炸威力'],
                    values['是否产生火焰'],
                    values['是否破坏方块'],
                    # 对于命令方块发送的指令，origin中不包含entityId
                    args['origin'].get('entityId'),
                    args['origin'].get('entityId')
                )