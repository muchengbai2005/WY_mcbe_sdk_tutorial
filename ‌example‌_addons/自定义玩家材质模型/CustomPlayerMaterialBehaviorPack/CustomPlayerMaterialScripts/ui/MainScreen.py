# -*- coding: utf-8 -*-

import client.extraClientApi as clientApi
from mod_log import logger

ScreenNode = clientApi.GetScreenNodeCls()


class MainScreen(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)

    def Create(self):
        logger.info("===== MainScreen Create =====")