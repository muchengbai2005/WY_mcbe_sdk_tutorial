# -*- coding: utf-8 -*-
import server.extraServerApi as serverApi
CF = serverApi.GetEngineCompFactory()
# 官方文档用的就是levelId，方便直接复制代码不用改
levelId = serverApi.GetLevelId()
CMD = CF.CreateCommand(levelId).SetCommand
eventList = []
def Listen(funcOrStr=None, EN=serverApi.GetEngineNamespace(), ESN=serverApi.GetEngineSystemName(), priority=0):
    def binder(func):
        eventList.append((EN, ESN, funcOrStr if isinstance(funcOrStr, str)else func.__name__, func, priority))
        return func
    return binder(funcOrStr)if callable(funcOrStr)else binder
# 这是经常用到的一个方法，所以写在Utils里简化调用
def GetTypeStr(entityId):
    return CF.CreateEngineType(entityId).GetEngineTypeStr()
class ServerBaseSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(ServerBaseSystem, self).__init__(namespace, systemName)
        self.ListenForEvent(namespace, 'ClientSystem', 'ClientEvent', self, self.OnGetClientEvent)
        for EN, ESN, eventName, callback, priority in eventList:
            self.ListenForEvent(EN, ESN, eventName, self, callback, priority)
        del eventList[:]
    def OnGetClientEvent(self, args):
        funcArgs = args.get('args', ({},))
        if len(funcArgs)==1 and isinstance(funcArgs[0], dict):
            funcArgs[0]['__id__'] = args['__id__']
        getattr(self, args['funcName'])(*funcArgs, **args.get('kwargs', {}))
    def CallClient(self, playerId, funcName, *args, **kwargs):
        data = {'funcName': funcName}
        if args:data['args'] = args
        if kwargs:data['kwargs'] = kwargs
        self.NotifyToClient(playerId, 'ServerEvent', data)
    def CallAllClient(self, funcName, *args, **kwargs):
        data = {'funcName': funcName}
        if args:data['args'] = args
        if kwargs:data['kwargs'] = kwargs
        self.BroadcastToAllClient('ServerEvent', data)