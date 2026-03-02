# -*- coding: utf-8 -*-
#

import mod.client.extraClientApi as clientApi

compFactory = clientApi.GetEngineCompFactory()


class CustomItemsClient(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, name):
        super(CustomItemsClient, self).__init__(namespace, name)
        print 'CustomItemsClient init'
        self.ListenEvent()
        self.levelId = clientApi.GetLevelId()

    def ListenEvent(self):
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.UiInitFinished)

    def UiInitFinished(self, args):
        compFactory.CreateTextNotifyClient(self.levelId).SetLeftCornerNotify("聊天栏输入up来升级手持物品~ 最多升级4次")
