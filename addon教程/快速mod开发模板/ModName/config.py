# -*- coding: utf-8 -*-
# 读取外层文件夹名称作为ModName。
ModName = __file__.rsplit('/'if'/'in __file__ else'.', 2)[-2]
# 框架自用函数，你无需使用。创建事件数据，不需要的键不添加，节约通信流量。
def CreateEventData(funcName, args, kwargs):
    data = {'funcName': funcName}
    if args:data['args'] = args
    if kwargs:data['kwargs'] = kwargs
    return data