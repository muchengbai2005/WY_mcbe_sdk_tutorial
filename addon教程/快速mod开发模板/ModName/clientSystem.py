# -*- coding: utf-8 -*-
# 此文件有注释和多余的测试函数，正式开发推荐使用“ModName去注释版”或者“单modMain版”。
import client.extraClientApi as clientApi
import config as DB
CF = clientApi.GetEngineCompFactory()
PID = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
eventList = []
# 一个装饰器，让某个客户端类的函数变成回调函数。
# funcOrStr：既可以是函数，也可以是事件名称，用法见下方。
# EN：EngineNamespace的缩写，不传则默认监听游戏本体事件。
# ESN：EngineSystemName的缩写，不传则默认监听游戏本体事件。
# 本模板封装了更方便的通信接口，所以EN，ESN这两个参数大部分情况下都无需使用。
def Listen(funcOrStr=None, EN=clientApi.GetEngineNamespace(), ESN=clientApi.GetEngineSystemName(), priority=0):
    def binder(func):
        eventList.append((EN, ESN, funcOrStr if isinstance(funcOrStr, str)else func.__name__, func, priority))
        return func
    return binder(funcOrStr)if callable(funcOrStr)else binder

class ClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(ClientSystem, self).__init__(namespace, systemName)
        for EN, ESN, eventName, callback, priority in eventList:
            self.ListenForEvent(EN, ESN, eventName, self, callback, priority)
        # 无需在此处监听引擎事件，请使用@Listen，用法见下方。
        # 无需监听服务端自定义事件，请在服务端使用CallClient或CallAllClient。

    # @Listen可以让被装饰的函数变成回调函数，这时函数名需要与事件名相同。
    # 这里监听了UiInitFinished事件。
    # @Listen的另一种用法见服务端32行。
    @Listen
    def UiInitFinished(self, args):
        print 'UI框架初始化完成'
        # 这里演示了CallServer的用法，到时候服务端的这三个函数会被调用。
        self.CallServer('ServerTest1')
        self.CallServer('ServerTest2', {'456': (7, 8, 9)})
        self.CallServer('ServerTest3', PID, 123, {'456': (7, 8, 9)}, arg3=10)
        
    # 如果要监听其他模组事件，就需要使用EN，ESN参数。
    # 模组内双端通信用CallServer就行了。
    @Listen('ServerEvent', DB.ModName, 'ServerSystem')
    def OnGetServerEvent(self, args):
        getattr(self, args['funcName'])(*args.get('args', ()), **args.get('kwargs', {}))

    # 调用服务端函数，并发送数据。
    # funcName：str，服务端函数名称。
    # *args, **kwargs：要发送的参数。
    # 示例见上方UiInitFinished函数。
    # (兼容旧版)当无参数，或只发送一个字典时，服务端也会收到args，其中自带'__id__'表示客户端玩家id。
    def CallServer(self, funcName, *args, **kwargs):
        self.NotifyToServer('ClientEvent', DB.CreateEventData(funcName, args, kwargs))

    # 客户端调用其他玩家客户端函数，传入对方的playerId，实际由服务端转发。
    # 如果playerId和自己相同，则直接调用并返回，而不经过服务端。
    def CallClient(self, playerId, funcName, *args, **kwargs):
        if playerId==PID:return getattr(self, funcName)(*args, **kwargs)
        self.CallServer('CallClient', playerId, funcName, *args, **kwargs)

    # 客户端调用所有玩家客户端函数，传入对方的playerId，由服务端再NotifyToAllClient。
    # 如果playerId和本地玩家相同，也会被服务端转发后自己才能收到。
    def CallAllClient(self, funcName, *args, **kwargs):
        self.CallServer('CallAllClient', funcName, *args, **kwargs)

    # 这两个测试函数会被服务端调用。
    def ClientTest1(self):
        print 'ClientTest1'
    def ClientTest2(self, arg1, arg2, arg3):
        print 'ClientTest2', arg1, arg2, arg3