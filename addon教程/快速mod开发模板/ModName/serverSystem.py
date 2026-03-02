# -*- coding: utf-8 -*-
# 此文件有注释和多余的测试函数，正式开发推荐使用“ModName去注释版”或者“单modMain版”。
import server.extraServerApi as serverApi
import config as DB
CF = serverApi.GetEngineCompFactory()
levelId = serverApi.GetLevelId()
CMD = CF.CreateCommand(levelId).SetCommand
eventList = []
# 一个装饰器，让某个服务端类的函数变成回调函数。
# funcOrStr：既可以是函数，也可以是事件名称，用法见下方。
# EN：EngineNamespace的缩写，不传则默认监听游戏本体事件。
# ESN：EngineSystemName的缩写，不传则默认监听游戏本体事件。
# 本模板封装了更方便的通信接口，所以EN，ESN这两个参数大部分情况下都无需使用。
def Listen(funcOrStr=None, EN=serverApi.GetEngineNamespace(), ESN=serverApi.GetEngineSystemName(), priority=0):
    def binder(func):
        eventList.append((EN, ESN, funcOrStr if isinstance(funcOrStr, str)else func.__name__, func, priority))
        return func
    return binder(funcOrStr)if callable(funcOrStr)else binder

class ServerSystem(serverApi.GetServerSystemCls()):
    def __init__(self, namespace, systemName):
        super(ServerSystem, self).__init__(namespace, systemName)
        for EN, ESN, eventName, callback, priority in eventList:
            self.ListenForEvent(EN, ESN, eventName, self, callback, priority)
        # 无需在此处监听引擎事件，请使用@Listen，用法见下方。
        # 无需监听客户端自定义事件，请在客户端使用CallServer。

    # @Listen可以让被装饰的函数变成回调函数。
    # 这里监听了ClientLoadAddonsFinishServerEvent事件。
    # @Listen后面可以传入事件名，这样函数就可以自己起名了。
    # @Listen的更简用法见客户端31行。
    @Listen('ClientLoadAddonsFinishServerEvent')
    def CustomFuncName(self, args):
        print '客户端mod初始化完成，给客户端发送数据'
        # 这里演示了CallClient的用法，到时候客户端的这两个函数会被调用。
        self.CallClient(args['playerId'], 'ClientTest1')
        self.CallClient(args['playerId'], 'ClientTest2', 123, {'456': (7, 8, 9)}, arg3=10)

    # 如果要监听其他模组事件，就需要使用EN，ESN参数。
    # 模组内双端通信用CallClient就行了。
    @Listen('ClientEvent', DB.ModName, 'ClientSystem')
    def OnGetClientEvent(self, args):
        funcArgs = args.get('args', ({},))
        if len(funcArgs)==1 and isinstance(funcArgs[0], dict):
            funcArgs[0]['__id__'] = args['__id__']
        getattr(self, args['funcName'])(*funcArgs, **args.get('kwargs', {}))

    # 调用客户端函数，并发送数据。
    # funcName：str，客户端函数名称。
    # *args, **kwargs：要发送的参数。
    # 示例见上方CustomFuncName函数。
    def CallClient(self, playerId, funcName, *args, **kwargs):
        self.NotifyToClient(playerId, 'ServerEvent', DB.CreateEventData(funcName, args, kwargs))

    # 调用所有玩家客户端函数。
    def CallAllClient(self, funcName, *args, **kwargs):
        self.BroadcastToAllClient('ServerEvent', DB.CreateEventData(funcName, args, kwargs))

    # 这三个测试函数会被客户端调用。
    def ServerTest1(self, args):
        print 'ServerTest1', args
    def ServerTest2(self, args):
        print 'ServerTest2', args
    def ServerTest3(self, playerId, arg1, arg2, arg3):
        print 'ServerTest3', playerId, arg1, arg2, arg3