# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
CF = clientApi.GetEngineCompFactory()
PID = clientApi.GetLocalPlayerId()
# 官方文档用的就是levelId，方便直接复制代码不用改
levelId = clientApi.GetLevelId()
ScreenNode = clientApi.GetScreenNodeCls()
ViewBinder = clientApi.GetViewBinderCls()
# 当UI继承common.base_screen后，路径需要加上这个
BP = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/'
GetToggleOption = CF.CreatePlayerView(levelId).GetToggleOption
# 一个装饰器，适用于PushScreen出来的UI的按钮绑定。
# 使得鼠标模式下，按下就触发callBack，而触屏模式弹起才触发。
def ButtonBinder(funcOrStr=None):
    def binder(func):
        @ViewBinder.binding(ViewBinder.BF_ButtonClick, funcOrStr if isinstance(funcOrStr, str)else None)
        def wrapper(self, args):
            mode, event = GetToggleOption('INPUT_MODE'), args['TouchEvent']
            if(mode==1 and event==0)or(mode!=1 and event==1):
                return func(self, args)
        wrapper.__name__ = func.__name__
        return wrapper
    return binder(funcOrStr)if callable(funcOrStr)else binder
eventList = []
def Listen(funcOrStr=None, EN=clientApi.GetEngineNamespace(), ESN=clientApi.GetEngineSystemName(), priority=0):
    def binder(func):
        eventList.append((EN, ESN, funcOrStr if isinstance(funcOrStr, str)else func.__name__, func, priority))
        return func
    return binder(funcOrStr)if callable(funcOrStr)else binder
# 这是经常用到的一个方法，所以写在Utils里简化调用
def GetTypeStr(entityId):
    return CF.CreateEngineType(entityId).GetEngineTypeStr()
class ClientBaseSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(ClientBaseSystem, self).__init__(namespace, systemName)
        self.ListenForEvent(namespace, 'ServerSystem', 'ServerEvent', self, self.OnGetServerEvent)
        for EN, ESN, eventName, callback, priority in eventList:
            self.ListenForEvent(EN, ESN, eventName, self, callback, priority)
        del eventList[:]
    def OnGetServerEvent(self, args):
        getattr(self, args['funcName'])(*args.get('args', ()), **args.get('kwargs', {}))
    def CallServer(self, funcName, *args, **kwargs):
        data = {'funcName': funcName}
        if args:data['args'] = args
        if kwargs:data['kwargs'] = kwargs
        self.NotifyToServer('ClientEvent', data)
    def CallClient(self, playerId, funcName, *args, **kwargs):
        if playerId==PID:return getattr(self, funcName)(*args, **kwargs)
        self.CallServer('CallClient', playerId, funcName, *args, **kwargs)
    def CallAllClient(self, funcName, *args, **kwargs):
        self.CallServer('CallAllClient', funcName, *args, **kwargs)