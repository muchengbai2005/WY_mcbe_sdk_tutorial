# -*- coding: utf-8 -*-
import client.extraClientApi as clientApi
LVID = clientApi.GetLevelId()
CF = clientApi.GetEngineCompFactory()
ScreenNode = clientApi.GetScreenNodeCls()
GetToggleOption = CF.CreatePlayerView(LVID).GetToggleOption
GetCarriedItem = CF.CreateItem(clientApi.GetLocalPlayerId()).GetCarriedItem
BP = '/variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel/'
ModName = __file__.rsplit('/'if'/'in __file__ else'.', 2)[-2]
eventList = []
def Listen(funcOrStr=None, EN=clientApi.GetEngineNamespace(), ESN=clientApi.GetEngineSystemName(), priority=0):
    def binder(func):
        eventList.append((EN, ESN, funcOrStr if isinstance(funcOrStr, str)else func.__name__, func, priority))
        return func
    return binder(funcOrStr)if callable(funcOrStr)else binder

class PresetButtonUI(ScreenNode):
    def __init__(self, namespace, name, param):
        ScreenNode.__init__(self, namespace, name, param)
        self.client = clientApi.GetSystem(ModName, 'ClientSystem')
    def Create(self):
        self.AddTouchEventHandler(BP+'button', self.client.OnButtonTouch, {'isSwallow':True})
    def Destroy(self):
        self.client.uiNode = None

class ClientSystem(clientApi.GetClientSystemCls()):
    def __init__(self, namespace, systemName):
        super(ClientSystem, self).__init__(namespace, systemName)
        EN, ESN = clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName()
        for EN, ESN, eventName, callback, priority in eventList:
            self.ListenForEvent(EN, ESN, eventName, self, callback, priority)
        self.itemsButton = {}
        self.uiNode = None
        self.freshTimer = None

    def SetItemButton(self, itemName, callBack, buttonText='', pcTips='',
        default='textures/ui/button_borderless_light',
        hover='textures/ui/button_borderless_light',
        pressed='textures/ui/button_borderless_lightpressed',
        size=(30, 18), anchorFrom='bottom_middle', anchorTo='bottom_middle', offset=(0, -43)):
        
        self.itemsButton[itemName] = locals()
        if self.freshTimer:
            return
        self.freshTimer = CF.CreateGame(LVID).AddTimer(0, self.FreshUI)

    def FreshUI(self):
        self.OnCarriedNewItem({'itemDict': GetCarriedItem() or {'newItemName': 'minecraft:air'}})
        self.freshTimer = None
    @Listen
    def UiInitFinished(self, args):
        clientApi.RegisterUI(ModName, ModName+'UI', ModName+'.ClientSystem.PresetButtonUI', ModName+'UI.main')
        self.uiNode = clientApi.CreateUI(ModName, ModName+'UI', {'isHud': 1})
    @Listen
    def ClientItemTryUseEvent(self, args):
        itemName = args['itemDict']['newItemName']
        if itemName in self.itemsButton:
            self.itemsButton[itemName]['callBack']()

    def OnButtonTouch(self, args):
        if args['TouchEvent']!=0:
            return
        carried = GetCarriedItem()
        if carried and carried['newItemName']in self.itemsButton:
            self.itemsButton[carried['newItemName']]['callBack']()
    @Listen('OnCarriedNewItemChangedClientEvent')
    def OnCarriedNewItem(self, args):
        uiNode = self.uiNode
        if not uiNode:
            return
        info = self.itemsButton.get(args['itemDict']['newItemName'])
        if not info:
            uiNode.SetVisible(BP+'button', False)
            uiNode.SetText(BP+'tips', '')
            return
        if GetToggleOption('INPUT_MODE')!=1:
            uiNode.SetText(BP+'tips', info['pcTips'])
            return
        uiNode.SetSprite(BP+'button/default', info['default'])
        uiNode.SetSprite(BP+'button/hover', info['hover'])
        uiNode.SetSprite(BP+'button/pressed', info['pressed'])
        uiNode.SetText(BP+'button/button_label', info['buttonText'])
        button = uiNode.GetBaseUIControl(BP+'button')#.asButton()
        button.SetVisible(True)
        button.SetSize(info['size'], True)
        button.SetAnchorFrom(info['anchorFrom'])
        button.SetAnchorTo(info['anchorTo'])
        button.SetFullPosition('x', {'absoluteValue': info['offset'][0]})
        button.SetFullPosition('y', {'absoluteValue': info['offset'][1]})