# -*- coding: utf-8 -*-
from ..serverUtils import *
class ServerSystem(ServerBaseSystem):
    # def __init__(self, namespace, systemName):
        # super(ServerSystem, self).__init__(namespace, systemName)
    def ModName1PlayerUiInitFinished(self, args):
        print '服务端1 知道了客户端UI加载完成'
        self.CallClient(args['__id__'], 'OnServerSendData', 'アトリは、高性能ですから!')