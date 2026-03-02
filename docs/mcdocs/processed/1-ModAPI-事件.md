# ModAPI 事件

## 目录

- [UI](#ui)
- [世界](#世界)
- [实体](#实体)
- [控制](#控制)
- [方块](#方块)
- [模型](#模型)
- [物品](#物品)
- [玩家](#玩家)
- [联机大厅](#联机大厅)
- [音效](#音效)

---

## UI

# UI

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ClientChestCloseEvent](UI.md#clientchestcloseevent) | <span style="display:inline;color:#7575f9">客户端</span> | 关闭箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子 |
| [ClientChestOpenEvent](UI.md#clientchestopenevent) | <span style="display:inline;color:#7575f9">客户端</span> | 打开箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子 |
| [ClientPlayerInventoryCloseEvent](UI.md#clientplayerinventorycloseevent) | <span style="display:inline;color:#7575f9">客户端</span> | 关闭物品背包界面时触发 |
| [ClientPlayerInventoryOpenEvent](UI.md#clientplayerinventoryopenevent) | <span style="display:inline;color:#7575f9">客户端</span> | 打开物品背包界面时触发 |
| [GridComponentSizeChangedClientEvent](UI.md#gridcomponentsizechangedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：UI grid组件里格子数目发生变化时触发 |
| [OnItemSlotButtonClickedEvent](UI.md#onitemslotbuttonclickedevent) | <span style="display:inline;color:#7575f9">客户端</span> | 点击快捷栏和背包栏的物品槽时触发 |
| [PlayerChatButtonClickClientEvent](UI.md#playerchatbuttonclickclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件 |
| [PlayerInventoryOpenScriptServerEvent](UI.md#playerinventoryopenscriptserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 某个客户端打开物品背包界面时触发 |
| [PopScreenEvent](UI.md#popscreenevent) | <span style="display:inline;color:#7575f9">客户端</span> | screen移除触发 |
| [PushScreenEvent](UI.md#pushscreenevent) | <span style="display:inline;color:#7575f9">客户端</span> | screen创建触发 |
| [UiInitFinished](UI.md#uiinitfinished) | <span style="display:inline;color:#7575f9">客户端</span> | UI初始化框架完成,此时可以创建UI |
| [UrgeShipEvent](UI.md#urgeshipevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家点击商城催促发货按钮时触发该事件 |
# UI

## ClientChestCloseEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    关闭箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子

- 参数

    无

- 返回值

    无



## ClientChestOpenEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    打开箱子界面时触发，包括小箱子，合并后大箱子和末影龙箱子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | x | int | 箱子位置x值 |
    | y | int | 箱子位置y值 |
    | z | int | 箱子位置z值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ClientPlayerInventoryCloseEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    关闭物品背包界面时触发

- 参数

    无

- 返回值

    无



## ClientPlayerInventoryOpenEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    打开物品背包界面时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isCreative | bool | 是否是创造模式背包界面 |
    | cancel | bool | 取消打开物品背包界面 |

- 返回值

    无



## GridComponentSizeChangedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：UI grid组件里格子数目发生变化时触发

- 参数

    无

- 返回值

    无



## OnItemSlotButtonClickedEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    点击快捷栏和背包栏的物品槽时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotIndex | int | 点击的物品槽的编号 |

- 返回值

    无



## PlayerChatButtonClickClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件

- 参数

    无

- 返回值

    无



## PlayerInventoryOpenScriptServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    某个客户端打开物品背包界面时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 客户端对应的玩家entity的唯一ID |
    | isCreative | bool | 是否是创造模式背包界面 |

- 返回值

    无

- 备注
    - 可以监听此事件判定客户端是否打开了创造背包

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PopScreenEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    screen移除触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | screenName | str | UI名字 |

- 返回值

    无



## PushScreenEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    screen创建触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | screenName | str | UI名字 |

- 返回值

    无



## UiInitFinished

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    UI初始化框架完成,此时可以创建UI

- 参数

    无

- 返回值

    无

- 备注
    - 切换维度后会重新初始化UI并触发该事件



## UrgeShipEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家点击商城催促发货按钮时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>

## 世界

# 世界

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AchievementCompleteEvent](世界.md#achievementcompleteevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家完成自定义成就时触发该事件 |
| [AddEntityClientEvent](世界.md#addentityclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端侧创建新实体时触发 |
| [AddEntityServerEvent](世界.md#addentityserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端侧创建新实体，或实体从存档加载时触发 |
| [AddPlayerAOIClientEvent](世界.md#addplayeraoiclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家加入游戏或者其余玩家进入当前玩家所在的区块时触发的AOI事件，替换AddPlayerEvent |
| [AddPlayerCreatedClientEvent](世界.md#addplayercreatedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家进入当前玩家所在的区块AOI后，玩家皮肤数据异步加载完成后触发的事件 |
| [AddServerPlayerEvent](世界.md#addserverplayerevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家加入时触发该事件。 |
| [ChunkAcquireDiscardedClientEvent](世界.md#chunkacquirediscardedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：客户端区块即将被卸载时 |
| [ChunkAcquireDiscardedServerEvent](世界.md#chunkacquirediscardedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端区块即将被卸载时触发 |
| [ChunkGeneratedServerEvent](世界.md#chunkgeneratedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：区块创建完成时触发 |
| [ChunkLoadedClientEvent](世界.md#chunkloadedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：客户端区块加载完成时 |
| [ChunkLoadedServerEvent](世界.md#chunkloadedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：服务端区块加载完成时 |
| [ClientLoadAddonsFinishServerEvent](世界.md#clientloadaddonsfinishserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：客户端mod加载完成时，服务端触发此事件。服务器可以使用此事件，往客户端发送数据给其初始化。 |
| [CommandEvent](世界.md#commandevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家请求执行指令时触发 |
| [DelServerPlayerEvent](世界.md#delserverplayerevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：删除玩家时触发该事件。 |
| [EntityRemoveEvent](世界.md#entityremoveevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体被删除时触发 |
| [ExplosionServerEvent](世界.md#explosionserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当发生爆炸时触发。 |
| [LoadClientAddonScriptsAfter](世界.md#loadclientaddonscriptsafter) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端加载mod完成事件 |
| [LoadServerAddonScriptsAfter](世界.md#loadserveraddonscriptsafter) | <span style="display:inline;color:#ff5555">服务端</span> | 服务器加载完mod时触发 |
| [NewOnEntityAreaEvent](世界.md#newonentityareaevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件。 |
| [OnCommandOutputClientEvent](世界.md#oncommandoutputclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 当command命令有成功消息输出时触发 |
| [OnCommandOutputServerEvent](世界.md#oncommandoutputserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | Command命令执行成功事件 |
| [OnContainerFillLoottableServerEvent](世界.md#oncontainerfillloottableserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：随机奖励箱第一次打开根据loottable生成物品时 |
| [OnLightningLevelChangeServerEvent](世界.md#onlightninglevelchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 打雷强度发生改变 |
| [OnLocalLightningLevelChangeServerEvent](世界.md#onlocallightninglevelchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 独立维度天气打雷强度发生改变时触发 |
| [OnLocalPlayerStopLoading](世界.md#onlocalplayerstoploading) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家进入存档，出生点地形加载完成时触发。该事件触发时可以进行切换维度的操作。 |
| [OnLocalRainLevelChangeServerEvent](世界.md#onlocalrainlevelchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 独立维度天气下雨强度发生改变时触发 |
| [OnRainLevelChangeServerEvent](世界.md#onrainlevelchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 下雨强度发生改变 |
| [OnScriptTickClient](世界.md#onscripttickclient) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端tick事件,1秒30次 |
| [OnScriptTickServer](世界.md#onscripttickserver) | <span style="display:inline;color:#ff5555">服务端</span> | 服务器tick时触发,1秒有30个tick |
| [PlaceNeteaseStructureFeatureEvent](世界.md#placeneteasestructurefeatureevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：首次生成地形时，结构特征即将生成时服务端抛出该事件。 |
| [PlayerIntendLeaveServerEvent](世界.md#playerintendleaveserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：即将删除玩家时触发该事件，此时可以通过各种API获取玩家的当前状态。 |
| [PlayerJoinMessageEvent](世界.md#playerjoinmessageevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件。 |
| [PlayerLeftMessageServerEvent](世界.md#playerleftmessageserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件。 |
| [RemoveEntityClientEvent](世界.md#removeentityclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端侧实体被移除时触发 |
| [RemovePlayerAOIClientEvent](世界.md#removeplayeraoiclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家离开当前玩家同一个区块时触发AOI事件 |
| [ServerChatEvent](世界.md#serverchatevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家发送聊天信息时触发 |
| [ServerPostBlockPatternEvent](世界.md#serverpostblockpatternevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：用方块组合生成生物，生成生物之后触发该事件。 |
| [ServerPreBlockPatternEvent](世界.md#serverpreblockpatternevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：用方块组合生成生物，在放置最后一个组成方块时触发该事件。 |
| [ServerSpawnMobEvent](世界.md#serverspawnmobevent) | <span style="display:inline;color:#ff5555">服务端</span> | 游戏内自动生成生物，以及使用api生成生物时触发 |
| [UnLoadClientAddonScriptsBefore](世界.md#unloadclientaddonscriptsbefore) | <span style="display:inline;color:#7575f9">客户端</span> | 客户端卸载mod之前触发 |
# 世界

## AchievementCompleteEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家完成自定义成就时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | rootNodeId | str | 所属的页面的根节点成就id |
    | achievementId | str | 达成的成就id |
    | title | str | 成就标题 |
    | description | str | 成就描述 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddEntityClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    客户端侧创建新实体时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |
    | posX | float | 位置x |
    | posY | float | 位置y |
    | posZ | float | 位置z |
    | dimensionId | int | 实体维度 |
    | isBaby | bool | 是否为幼儿 |
    | engineTypeStr | str | 实体类型 |
    | itemName | str | 物品identifier（仅当物品实体时存在该字段） |
    | auxValue | int | 物品附加值（仅当物品实体时存在该字段） |

- 返回值

    无

- 备注
    - 创建玩家时不会触发该事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddEntityServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    服务端侧创建新实体，或实体从存档加载时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |
    | posX | float | 位置x |
    | posY | float | 位置y |
    | posZ | float | 位置z |
    | dimensionId | int | 实体维度 |
    | isBaby | bool | 是否为幼儿 |
    | engineTypeStr | str | 实体类型，即实体identifier |
    | itemName | str | 物品identifier（仅当物品实体时存在该字段） |
    | auxValue | int | 物品附加值（仅当物品实体时存在该字段） |

- 返回值

    无

- 备注
    - 创建玩家时不会触发该事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddPlayerAOIClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家加入游戏或者其余玩家进入当前玩家所在的区块时触发的AOI事件，替换AddPlayerEvent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

- 备注
    - 该事件触发只表明在服务端数据中接收到了新玩家，并不能代表此时玩家在客户端中可见，若想在玩家进入AOI后立马调用玩家渲染相关接口，建议使用[AddPlayerCreatedClientEvent](#addplayercreatedclientevent)。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddPlayerCreatedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家进入当前玩家所在的区块AOI后，玩家皮肤数据异步加载完成后触发的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

- 备注
    - 由于玩家皮肤是异步加载的原因，该事件触发时机比[AddPlayerAOIClientEvent](#addplayeraoiclientevent)晚，触发该事件后可以对该玩家调用相关[玩家渲染接口](../接口/玩家/渲染.md)。
    - 当前客户端每加载好一个玩家的皮肤，就会触发一次该事件，比如刚进入世界时，localPlayer加载好会触发一次，周围的所有玩家加载好后也会分别触发一次。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddServerPlayerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家加入时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |
    | isTransfer | bool | 是否是切服时进入服务器，仅用于Apollo。如果是True，则表示切服时加入服务器，若是False，则表示登录进入网络游戏 |
    | isReconnect | bool | 是否是断线重连，仅用于Apollo。如果是True，则表示本次登录是断线重连，若是False，则表示本次是正常登录或者转服 |
    | isPeUser | bool | 是否从手机端登录，仅用于Apollo。如果是True，则表示本次登录是从手机端登录，若是False，则表示本次登录是从PC端登录 |
    | transferParam | str | 切服传入参数，仅用于Apollo。调用【TransferToOtherServer】或【TransferToOtherServerById】传入的切服参数 |
    | uid | int/long | 仅用于Apollo，玩家的netease uid，玩家的唯一标识 |
    | proxyId | int | 仅用于Apollo，当前客户端连接的proxy服务器id |

- 返回值

    无

- 备注
    - 触发此事件时，客户端mod未加载完毕，因此响应本事件时不能客户端发送事件。若需要在玩家进入世界时，服务器往客户端发送事件，请使用ClientLoadAddonsFinishServerEvent
    - 触发此事件时，玩家的实体还未加载完毕，请勿在这时切换维度。请在客户端监听OnLocalPlayerStopLoading事件并发送事件到server端再进行维度切换。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ChunkAcquireDiscardedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：客户端区块即将被卸载时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPosX | int | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
    | chunkPosZ | int | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |

- 返回值

    无

- 备注
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://minecraft-zh.gamepedia.com/%E5%8C%BA%E5%9D%97)



## ChunkAcquireDiscardedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    服务端区块即将被卸载时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPosX | int | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
    | chunkPosZ | int | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |
    | entities | list(str) | 随区块卸载而从世界移除的实体id的列表。注意事件触发时已经无法获取到这些实体的信息，仅供脚本资源回收用。 |
    | blockEntities | list(dict) | 随区块卸载而从世界移除的自定义方块实体的坐标的列表，列表元素dict包含posX，posY，posZ三个int表示自定义方块实体的坐标。注意事件触发时已经无法获取到这些方块实体的信息，仅供脚本资源回收用。 |

- 返回值

    无

- 备注
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://minecraft-zh.gamepedia.com/%E5%8C%BA%E5%9D%97)



## ChunkGeneratedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：区块创建完成时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 该区块所在的维度 |
    | blockEntityData | [{"blockName":str,"posX":int,"posY":int,"posZ":int}...]/None | 该区块中的自定义方块实体列表，通常是由自定义特征生成的自定义方块，没有自定义方块实体时该值为None |

- 返回值

    无



## ChunkLoadedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：客户端区块加载完成时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPosX | int | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
    | chunkPosZ | int | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |

- 返回值

    无



## ChunkLoadedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：服务端区块加载完成时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPosX | int | 区块的x坐标，对应方块X坐标区间为[x * 16, x * 16 + 15] |
    | chunkPosZ | int | 区块的z坐标，对应方块Z坐标区间为[z * 16, z * 16 + 15] |

- 返回值

    无



## ClientLoadAddonsFinishServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：客户端mod加载完成时，服务端触发此事件。服务器可以使用此事件，往客户端发送数据给其初始化。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## CommandEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家请求执行指令时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家ID |
    | command | str | 指令字符串 |
    | cancel | bool | 是否取消 |

- 返回值

    无

- 备注
    - 该事件是玩家请求执行指令时触发的Hook，该事件不响应命令方块的指令和通过modSDK调用的指令，阻止玩家的该条指令只需要将cancel设置为True

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DelServerPlayerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：删除玩家时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |
    | isTransfer | bool | 是否是切服时退出服务器，仅用于Apollo。如果是True，则表示切服时退出服务器；若是False，则表示退出网络游戏 |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityRemoveEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体被删除时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 触发情景：实体从场景中被删除，例如：生物死亡，生物被[清除](https://minecraft.fandom.com/zh/wiki/%E7%94%9F%E6%88%90#.E6.B8.85.E9.99.A4)，玩家退出游戏，船/盔甲架被破坏，掉落物/经验球被捡起或清除
    - 当生物随区块卸载时，不会触发该事件，而是ChunkAcquireDiscardedServerEvent事件
    - 关于生物的清除：当生物离玩家大于wiki所说的距离，并且还在玩家的模拟距离内时，会被清除。也就是说，如果玩家瞬间传送到远处，原处的生物马上离开了模拟距离，并不会被清除
    - 玩家退出游戏时，EntityRemoveEvent，DelServerPlayerEvent按顺序依次触发

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ExplosionServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当发生爆炸时触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blocks | list[[x,y,z,cancel],...] | 爆炸涉及到的方块坐标(x,y,z)，cancel是一个bool值 |
    | victims | list/None | 受伤实体id列表，当该爆炸创建者id为None时，victims也为None |
    | sourceId | str/None | 爆炸创建者id |
    | explodePos | list | 爆炸位置[x,y,z] |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 通过设置blocks中cancel的bool值为True可以将该方块的爆炸取消，例如(x,y,z,True)
    - 某些情况下爆炸创建者id为None，此时受伤实体id列表也为None，比如爬行者所造成的爆炸。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## LoadClientAddonScriptsAfter

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    客户端加载mod完成事件

- 参数

    无

- 返回值

    无



## LoadServerAddonScriptsAfter

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    服务器加载完mod时触发

- 参数

    无

- 返回值

    无



## NewOnEntityAreaEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：通过RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 注册感应区域名称 |
    | enteredEntities | list[str] | 进入该感应区域的实体id列表 |
    | leftEntities | list[str] | 离开该感应区域的实体id列表 |

- 返回值

    无

- 备注
    - 本事件代替原有的OnEntityAreaEvent事件

- 示例

```python
# ServerSystem
import mod.server.extraServerApi as serverApi
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "NewOnEntityAreaEvent",
                    self, self.NewOnEntityAreaEvent)
def NewOnEntityAreaEvent(self, args):
    name = args['name']
```



### 相关接口

<span id="RegisterEntityAOIEvent"></span>
### RegisterEntityAOIEvent

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    注册感应区域，有实体进入时和离开时会有消息通知

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | name | str | 注册的感应区域名 |
    | aabb | tuple(float,float,float,float,float,float) | 感应区域的坐标范围，依次为minX, minY, minZ, maxX, maxY, maxZ |
    | ignoredEntities | list(str) | 忽略的实体id列表 |
    | entityType | int | 期望响应的实体类型，不传则响应所有的实体类型[EntityType枚举](../枚举值/EntityType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 注册完感应区域后，需通过监听OnEntityAreaEvent或NewOnEntityAreaEvent事件来获取感应事件
    - 不支持长或宽大于2000格的区域。对于大范围区域，建议在脚本中每隔一段时间获取实体坐标判断来实现。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.RegisterEntityAOIEvent(0, "test", (0, 0, 0, 1, 1, 1), None)
```



<span id="UnRegisterEntityAOIEvent"></span>
### UnRegisterEntityAOIEvent

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    反注册感应区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | name | str | 需要反注册的感应区域名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.UnRegisterEntityAOIEvent(0, "test")
```



## OnCommandOutputClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    当command命令有成功消息输出时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | command | str | 命令名称 |
    | message | str | 命令返回的消息 |

- 返回值

    无

- 备注
    - 部分命令在返回的时候没有命令名称，命令组件需要showOutput参数为True时才会有返回



## OnCommandOutputServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    Command命令执行成功事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | command | str | 命令名称 |
    | message | str | 命令返回的消息 |

- 返回值

    无

- 备注
    - 部分命令在返回的时候没有命令名称，命令组件需要showOutput参数为True时才会有返回



## OnContainerFillLoottableServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：随机奖励箱第一次打开根据loottable生成物品时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | loottable | str | 奖励箱子所读取的loottable的json路径 |
    | playerId | str | 打开奖励箱子的玩家的playerId |
    | itemList | list | 掉落物品列表，每个元素为一个itemDict，格式可参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | dirty | bool | 默认为False，如果需要修改掉落列表需将该值设为True |

- 返回值

    无

- 备注
    - 只有当dirty为True时才会重新读取item列表并生成对应的掉落物，如果不需要修改掉落结果的话请勿随意修改dirty值

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnLightningLevelChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    打雷强度发生改变

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldLevel | float | 改变前的打雷强度 |
    | newLevel | float | 改变后的打雷强度 |

- 返回值

    无



## OnLocalLightningLevelChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    独立维度天气打雷强度发生改变时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldLevel | float | 改变前的打雷强度 |
    | newLevel | float | 改变后的打雷强度 |
    | dimensionId | int | 独立天气维度id |

- 返回值

    无



## OnLocalPlayerStopLoading

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家进入存档，出生点地形加载完成时触发。该事件触发时可以进行切换维度的操作。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 加载完成的玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnLocalRainLevelChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    独立维度天气下雨强度发生改变时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldLevel | float | 改变前的下雨强度 |
    | newLevel | float | 改变后的下雨强度 |
    | dimensionId | int | 独立天气维度id |

- 返回值

    无



## OnRainLevelChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    下雨强度发生改变

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldLevel | float | 改变前的下雨强度 |
    | newLevel | float | 改变后的下雨强度 |

- 返回值

    无



## OnScriptTickClient

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    客户端tick事件,1秒30次

- 参数

    无

- 返回值

    无



## OnScriptTickServer

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    服务器tick时触发,1秒有30个tick

- 参数

    无

- 返回值

    无



## PlaceNeteaseStructureFeatureEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：首次生成地形时，结构特征即将生成时服务端抛出该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | structureName | str | 结构名称 |
    | x | int | 结构坐标最小方块所在的x坐标 |
    | y | int | 结构坐标最小方块所在的y坐标 |
    | z | int | 结构坐标最小方块所在的z坐标 |
    | biomeType | int | 该feature所放置区块的生物群系类型 |
    | biomeName | str | 该feature所放置区块的生物群系名称 |
    | dimensionId | int | 维度id |
    | cancel | bool | 设置为True时可阻止该结构的放置 |

- 返回值

    无

- 备注
    - **需要配合AddNeteaseFeatureWhiteList接口一同使用**
        若在本监听事件中调用其他mod SDK接口将无法生效，强烈建议本事件仅用于设置结构放置与否



### 相关接口

<span id="AddNeteaseFeatureWhiteList"></span>
### AddNeteaseFeatureWhiteList

method in mod.server.component.featureCompServer.FeatureCompServer

- 描述

    添加结构对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | structureName | str | 结构的identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
# 注意structureName格式为floderName:structureName
comp.AddNeteaseFeatureWhiteList("test:pumpkins")
```



<span id="RemoveNeteaseFeatureWhiteList"></span>
### RemoveNeteaseFeatureWhiteList

method in mod.server.component.featureCompServer.FeatureCompServer

- 描述

    移除structureName对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | structureName | str | 结构名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
# 注意structureName格式为floderName:structureName
comp.RemoveNeteaseFeatureWhiteList("test:pumpkins")
```



<span id="ClearAllNeteaseFeatureWhiteList"></span>
### ClearAllNeteaseFeatureWhiteList

method in mod.server.component.featureCompServer.FeatureCompServer

- 描述

    清空所有已添加Netease Structure Feature对PlaceNeteaseStructureFeatureEvent事件的脚本层监听

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
comp.ClearAllNeteaseFeatureWhiteList()
```



## PlayerIntendLeaveServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：即将删除玩家时触发该事件，此时可以通过各种API获取玩家的当前状态。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

- 备注
    - 与【DelServerPlayerEvent】事件不同，此时可以通过各种API获取玩家的当前状态。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerJoinMessageEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：准备显示“xxx加入游戏”的玩家登录提示文字时服务端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家实体id |
    | name | str | 玩家昵称 |
    | cancel | bool | 是否显示提示文字，允许修改。True：不显示提示 |
    | message | str | 玩家加入游戏的提示文字，允许修改 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerLeftMessageServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：准备显示“xxx离开游戏”的玩家离开提示文字时服务端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家实体id |
    | name | str | 玩家昵称 |
    | cancel | bool | 是否显示提示文字，允许修改。True：不显示提示 |
    | message | str | 玩家离开游戏的提示文字，允许修改 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## RemoveEntityClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    客户端侧实体被移除时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 移除的实体id |

- 返回值

    无

- 备注
    - 客户端接收服务端AOI事件时触发，原事件名 RemoveEntityPacketEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## RemovePlayerAOIClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家离开当前玩家同一个区块时触发AOI事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerChatEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家发送聊天信息时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | username | str | 玩家名称 |
    | playerId | str | 玩家id |
    | message | str | 玩家发送的聊天消息内容 |
    | cancel | bool | 是否取消这个聊天事件，若取消可以设置为True |
    | bChatById | bool | 是否把聊天消息发送给指定在线玩家，而不是广播给所有在线玩家，若只发送某些玩家可以设置为True |
    | bForbid | bool | 是否禁言，仅apollo可用。true：被禁言，玩家聊天会提示“你已被管理员禁言”。 |
    | toPlayerIds | list(str) | 接收聊天消息的玩家id列表，bChatById为True时生效 |

- 返回值

    无

- 示例

```python
# ServerSystem
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
# 监听引擎的事件 ：self指ServerSystem类的实例  ServerChatEvent是系统事件
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "ServerChatEvent",
                    self, self.OnServerChat)
def OnServerChat(self, args):
    #可以设置username或者message的样式代码 详见mc维基 样式代码
    args["username"] = "§rl"+args[username]+"§r"
    args["message"] = "test"
    logger.info("ServerChatEvent %s" % args)
```

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerPostBlockPatternEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：用方块组合生成生物，生成生物之后触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生成生物的id |
    | entityGenerated | str | 生成生物的名字，如"minecraft:pig" |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | dimensionId | int | 维度id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerPreBlockPatternEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：用方块组合生成生物，在放置最后一个组成方块时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否允许继续生成。若设为False，可阻止生成生物 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | dimensionId | int | 维度id |
    | entityWillBeGenerated | str | 即将生成生物的名字，如"minecraft:pig" |

- 返回值

    无



## ServerSpawnMobEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    游戏内自动生成生物，以及使用api生成生物时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | identifier | str | 生成实体的命名空间 |
    | type | int | 生成实体的类型，参考[EntityType](../枚举值/EntityType.md) |
    | baby | bool | 生成怪物是否是幼年怪 |
    | x | float | 生成实体坐标x |
    | y | float | 生成实体坐标y |
    | z | float | 生成实体坐标z |
    | dimensionId | int | 生成实体的维度，默认值为0（0为主世界，1为地狱，2为末地） |
    | realIdentifier | str | 生成实体的命名空间，通过MOD API生成的生物在这个参数也能获取到真正的命名空间，而不是以custom开头的 |
    | cancel | bool | 是否取消生成该实体 |

- 返回值

    无

- 备注
    - 如果通过MOD API生成，identifier命名空间为custom。如果需要屏蔽原版的生物生成，可以判断identifier命名空间不为custom时设置cancel为True

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## UnLoadClientAddonScriptsBefore

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    客户端卸载mod之前触发

- 参数

    无

- 返回值

    无

## 实体

# 实体

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ActorHurtServerEvent](实体.md#actorhurtserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：生物（包括玩家）受伤时触发 |
| [ActuallyHurtServerEvent](实体.md#actuallyhurtserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体实际受到伤害时触发，相比于DamageEvent，该伤害为经过护甲及buff计算后，实际的扣血量 |
| [AddEffectServerEvent](实体.md#addeffectserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体获得状态效果时 |
| [ApproachEntityClientEvent](实体.md#approachentityclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家靠近生物时触发 |
| [ChangeSwimStateServerEvent](实体.md#changeswimstateserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体开始或者结束游泳时 |
| [DamageEvent](实体.md#damageevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体受到伤害时触发 |
| [EntityChangeDimensionServerEvent](实体.md#entitychangedimensionserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体维度改变时服务端抛出 |
| [EntityDefinitionsEventServerEvent](实体.md#entitydefinitionseventserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件 |
| [EntityDieLoottableServerEvent](实体.md#entitydieloottableserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：生物死亡掉落物品时 |
| [EntityDroppedItemServerEvent](实体.md#entitydroppeditemserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：生物扔出物品时触发 |
| [EntityEffectDamageServerEvent](实体.md#entityeffectdamageserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 生物受到状态伤害/回复事件。 |
| [EntityLoadScriptEvent](实体.md#entityloadscriptevent) | <span style="display:inline;color:#ff5555">服务端</span> | 数据库加载实体自定义数据时触发 |
| [EntityModelChangedClientEvent](实体.md#entitymodelchangedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：实体模型切换时触发 |
| [EntityMotionStartServerEvent](实体.md#entitymotionstartserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体运动器开始事件。实体（包含玩家）添加运动器后，运动器开始运行时触发 |
| [EntityMotionStopServerEvent](实体.md#entitymotionstopserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体运动器停止事件。实体（包含玩家）添加运动器并开始运行后，运动器自动停止时触发 |
| [EntityPickupItemServerEvent](实体.md#entitypickupitemserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件，例如村民拾取面包、猪灵拾取金锭 |
| [EntityStartRidingEvent](实体.md#entitystartridingevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当实体骑乘上另一个实体时触发 |
| [EntityStopRidingEvent](实体.md#entitystopridingevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当实体停止骑乘时 |
| [EntityStopRidingEvent](实体.md#entitystopridingevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：当实体停止骑乘时 |
| [EntityTickServerEvent](实体.md#entitytickserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体tick时触发。该事件为20帧每秒。需要使用AddEntityTickEventWhiteList添加触发该事件的实体类型白名单。 |
| [HealthChangeBeforeServerEvent](实体.md#healthchangebeforeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 生物生命值发生变化之前触发 |
| [HealthChangeClientEvent](实体.md#healthchangeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 生物生命值发生变化时触发 |
| [HealthChangeServerEvent](实体.md#healthchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 生物生命值发生变化时触发 |
| [LeaveEntityClientEvent](实体.md#leaveentityclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家远离生物时触发 |
| [MobDieEvent](实体.md#mobdieevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体被玩家杀死时触发 |
| [MobGriefingBlockServerEvent](实体.md#mobgriefingblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 环境生物改变方块时触发，触发的时机与mobgriefing游戏规则影响的行为相同 |
| [OnFireHurtEvent](实体.md#onfirehurtevent) | <span style="display:inline;color:#ff5555">服务端</span> | 生物受到火焰伤害时触发 |
| [OnGroundClientEvent](实体.md#ongroundclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 实体着地事件。玩家，沙子，铁砧，掉落的物品，点燃的TNT掉落地面时触发，其余实体着地不触发。 |
| [OnGroundServerEvent](实体.md#ongroundserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体着地事件。实体，掉落的物品，点燃的TNT掉落地面时触发 |
| [OnKnockBackServerEvent](实体.md#onknockbackserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体被击退时触发 |
| [OnMobHitBlockServerEvent](实体.md#onmobhitblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：通过OpenMobHitBlockDetection打开方块碰撞检测后，当生物（不包括玩家）碰撞到方块时触发该事件。 |
| [OnMobHitMobClientEvent](实体.md#onmobhitmobclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。 |
| [OnMobHitMobServerEvent](实体.md#onmobhitmobserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。 |
| [ProjectileCritHitEvent](实体.md#projectilecrithitevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当抛射物与头部碰撞时触发该事件。注：需调用OpenPlayerCritBox开启玩家爆头后才能触发。 |
| [ProjectileDoHitEffectEvent](实体.md#projectiledohiteffectevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当抛射物碰撞时触发该事件 |
| [RefreshEffectServerEvent](实体.md#refresheffectserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体身上状态效果更新时触发，更新条件1、新增状态等级较高，更新状态等级及时间；2、新增状态等级不变，时间较长，更新状态持续时间 |
| [RemoveEffectServerEvent](实体.md#removeeffectserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体身上状态效果被移除时 |
| [SpawnProjectileServerEvent](实体.md#spawnprojectileserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：抛射物生成时触发 |
| [StartRidingClientEvent](实体.md#startridingclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：一个实体即将骑乘另外一个实体 |
| [StartRidingServerEvent](实体.md#startridingserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：一个实体即将骑乘另外一个实体 |
| [WillAddEffectServerEvent](实体.md#willaddeffectserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体即将获得状态效果前 |
| [WillTeleportToServerEvent](实体.md#willteleporttoserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 实体即将传送或切换维度 |
# 实体

## ActorHurtServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：生物（包括玩家）受伤时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物Id |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md) |
    | damage | int | 伤害值（被伤害吸收后的值），不可修改 |
    | absorbedDamage | int | 被伤害吸收效果吸收的伤害值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ActuallyHurtServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体实际受到伤害时触发，相比于DamageEvent，该伤害为经过护甲及buff计算后，实际的扣血量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | srcId | str | 伤害源id |
    | projectileId | str | 投射物id |
    | entityId | str | 被伤害id |
    | damage | int | 伤害值（被伤害吸收后的值），允许修改，设置为0则此次造成的伤害为0 |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md) |

- 返回值

    无

- 备注
    - 药水与状态效果造成的伤害不触发，可以使用ActorHurtServerEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddEffectServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体获得状态效果时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | effectName | str | 实体获得状态效果的名字 |
    | effectDuration | int | 状态效果的持续时间，单位秒 |
    | effectAmplifier | int | 状态效果的放大倍数 |
    | damage | int | 状态造成的伤害值（真实扣除生命值的量）。只有持续时间为0时有用 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ApproachEntityClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家靠近生物时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | entityId | str | 靠近的生物实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ChangeSwimStateServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体开始或者结束游泳时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体的唯一ID |
    | formState | bool | 事件触发前，实体是否在游泳状态 |
    | toState | bool | 事件触发后，实体是否在游泳状态 |

- 返回值

    无

- 备注
    - 当实体的状态没有变化时，不会触发此事件，即formState和toState必定一真一假

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DamageEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体受到伤害时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | srcId | str | 伤害源id |
    | projectileId | str | 投射物id |
    | entityId | str | 被伤害id |
    | damage | int | 伤害值（被伤害吸收前的值），允许修改，设置为0则此次造成的伤害为0 |
    | absorption | int | 伤害吸收生命值，详见[AttrType枚举](../枚举值/AttrType.md)的ABSORPTION |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause](../枚举值/ActorDamageCause.md) |
    | knock | bool | 是否击退被攻击者，允许修改，设置该值为False则不产生击退 |
    | ignite | bool | 是否点燃被伤害者，允许修改，设置该值为True产生点燃效果，反之亦然 |

- 返回值

    无

- 备注
    - damage值会被护甲和absorption等吸收，不一定是最终扣血量。通过设置这个伤害值可以取消伤害，但不会取消由击退效果或者点燃效果带来的伤害
    - 该事件在实体受伤之前触发，由于部分伤害是在tick中处理，因此持续触发受伤时（如站在火中）会每帧触发事件（可以使用ActorHurtServerEvent来避免）。
    - 这里的damage是伤害源具有的攻击伤害值，并非实体真实的扣血量，如果需要获取真实伤害，可以使用ActuallyHurtServerEvent事件。
    - 当目标无法被击退时，knock值无效
    - 药水与状态效果造成的伤害不触发，可以使用ActorHurtServerEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityChangeDimensionServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体维度改变时服务端抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | fromDimensionId | int | 维度改变前的维度 |
    | toDimensionId | int | 维度改变后的维度 |
    | fromX | float | 改变前的位置x |
    | fromY | float | 改变前的位置Y |
    | fromZ | float | 改变前的位置Z |
    | toX | float | 改变后的位置x |
    | toY | float | 改变后的位置Y |
    | toZ | float | 改变后的位置Z |

- 返回值

    无

- 备注
    - 实体转移维度时，如果对应维度的对应位置的区块尚未加载，实体会缓存在维度自身的缓冲区中，直到对应区块被加载时才会创建对应的实体，此事件的抛出只代表实体从原维度消失，不代表必定会在对应维度出现
    - 注意，玩家维度改变时不触发该事件，而是会触发DimensionChangeServerEvent事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityDefinitionsEventServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：生物定义json文件中设置的event触发时同时触发。生物行为变更事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物id |
    | eventName | str | 触发的事件名称 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityDieLoottableServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：生物死亡掉落物品时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dieEntityId | str | 死亡实体的entityId |
    | attacker | str | 伤害来源的entityId |
    | itemList | list(dict) | 掉落物品列表，每个元素为一个itemDict，格式可参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | dirty | bool | 默认为False，如果需要修改掉落列表需将该值设为True |

- 返回值

    无

- 备注
    - 只有当dirty为True时才会重新读取item列表并生成对应的掉落物，如果不需要修改掉落结果的话请勿随意修改dirty值

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityDroppedItemServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：生物扔出物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物Id |
    | itemDict | dict | 扔出的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | itemEntityId | str | 物品实体Id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityEffectDamageServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    生物受到状态伤害/回复事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | damage | int | 伤害值（伤害吸收后实际扣血量），负数表示生命回复量 |
    | attributeBuffType | int | 状态类型，参考[AttributeBuffType](../枚举值/AttributeBuffType.md) |
    | duration | float | 状态持续时间，单位秒（s） |
    | lifeTimer | float | 状态生命时间，单位秒（s） |
    | isInstantaneous | bool | 是否为立即生效状态 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityLoadScriptEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    数据库加载实体自定义数据时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | args | list | 该事件的参数为长度为2的list，而非dict，其中list的第一个元素为实体id |

- 返回值

    无

- 备注
    - 只有使用过extraData组件的实体才有此事件，触发时可以通过extraData组件获取该实体的自定义数据



## EntityModelChangedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：实体模型切换时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | newModel | str | 新的模型名字 |
    | oldModel | str | 原来的模型名字 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityMotionStartServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体运动器开始事件。实体（包含玩家）添加运动器后，运动器开始运行时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 运动器id |
    | entityId | str | 实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityMotionStopServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体运动器停止事件。实体（包含玩家）添加运动器并开始运行后，运动器自动停止时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 运动器id |
    | entityId | str | 实体id |
    | remove | bool | 是否移除该运动器，设置为False则保留，默认为True，即运动器停止后自动移除，该参数设置只对非玩家实体有效 |

- 返回值

    无

- 备注
    - 注意：该事件触发表示运动器播放顺利完成，手动调用的[StopEntityMotion](../接口/实体/行为.md#StopEntityMotion)、[RemoveEntityMotion](../接口/实体/行为.md#RemoveEntityMotion)以及实体被销毁导致的运动器停止不会触发该事件。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityPickupItemServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    有minecraft:behavior.pickup_items行为的生物拾取物品时触发该事件，例如村民拾取面包、猪灵拾取金锭

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物Id |
    | itemDict | dict | 拾取的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | secondaryActor | str | 物品给予者id（一般是玩家），如果不存在给予者的话，这里为空字符串 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityStartRidingEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当实体骑乘上另一个实体时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 乘骑者实体id |
    | rideId | str | 被乘骑者实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityStopRidingEvent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

<span id="server"></span>
### 服务端事件

- 描述

    触发时机：当实体停止骑乘时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |
    | rideId | str | 坐骑id |
    | exitFromRider | bool | 是否下坐骑 |
    | entityIsBeingDestroyed | bool | 坐骑是否将要销毁 |
    | switchingRides | bool | 是否换乘坐骑 |
    | cancel | bool | 设置为True可以取消（需要与客户端事件一同取消） |

- 返回值

    无

- 备注
    - 以下情况不允许取消
        1. ride组件StopEntityRiding接口
        2. 玩家传送时
        3. 坐骑死亡时
        4. 玩家睡觉时
        5. 玩家死亡时
        6. 未驯服的马
        7. 怕水的生物坐骑进入水里
        8. 切换维度

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


<span id="client"></span>
### 客户端事件

- 描述

    触发时机：当实体停止骑乘时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |
    | rideId | str | 坐骑id |
    | exitFromRider | bool | 是否下坐骑 |
    | entityIsBeingDestroyed | bool | 坐骑是否将要销毁 |
    | switchingRides | bool | 是否换乘坐骑 |
    | cancel | bool | 设置为True可以取消（需要与服务端事件一同取消） |

- 返回值

    无

- 备注
    - 以下情况不允许取消
        1. ride组件StopEntityRiding接口
        2. 玩家传送时
        3. 坐骑死亡时
        4. 玩家睡觉时
        5. 玩家死亡时
        6. 未驯服的马
        7. 怕水的生物坐骑进入水里
        8. 切换维度

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## EntityTickServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体tick时触发。该事件为20帧每秒。需要使用AddEntityTickEventWhiteList添加触发该事件的实体类型白名单。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | identifier | str | 实体identifier |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="AddEntityTickEventWhiteList"></span>
### AddEntityTickEventWhiteList

method in mod.server.extraServerApi

- 描述

    添加实体类型到EntityTickServerEvent事件的触发白名单。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 实体的类型名，原版的实体需要加上minecraft命名空间 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 让牛触发EntityTickServerEvent事件
serverApi.AddEntityTickEventWhiteList('minecraft:cow')
```



## HealthChangeBeforeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    生物生命值发生变化之前触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | from | float | 变化前的生命值 |
    | to | float | 将要变化到的生命值，cancel设置为True时可以取消该变化，但是此参数不变 |
    | byScript | bool | 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化 |
    | cancel | bool | 是否取消该变化 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## HealthChangeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    生物生命值发生变化时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | from | float | 变化前的生命值 |
    | to | float | 变化后的生命值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## HealthChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    生物生命值发生变化时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | from | float | 变化前的生命值 |
    | to | float | 变化后的生命值 |
    | byScript | bool | 是否通过SetAttrValue或SetAttrMaxValue调用产生的变化 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## LeaveEntityClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家远离生物时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | entityId | str | 远离的生物实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## MobDieEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体被玩家杀死时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |
    | attacker | str | 伤害来源id |

- 返回值

    无

- 备注
    - 注意：不能在该事件回调中对此玩家手持物品进行修改，如[SpawnItemToPlayerCarried](../接口/玩家/背包.md#spawnitemtoplayercarried)、[ChangePlayerItemTipsAndExtraId](../接口/玩家/背包.md#changeplayeritemtipsandextraId)等接口

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## MobGriefingBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    环境生物改变方块时触发，触发的时机与mobgriefing游戏规则影响的行为相同

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件 |
    | blockX | int | 方块x坐标 |
    | blockY | int | 方块y坐标 |
    | blockZ | int | 方块z坐标 |
    | entityId | str | 触发的entity的唯一ID |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 触发的时机包括：生物踩踏耕地、破坏单个方块、破门、火矢点燃方块、凋灵boss破坏方块、末影龙破坏方块、末影人捡起方块、蠹虫破坏被虫蚀的方块、蠹虫把方块变成被虫蚀的方块、凋零杀死生物生成凋零玫瑰、生物踩坏海龟蛋。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnFireHurtEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    生物受到火焰伤害时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | victim | str | 受伤实体id |
    | src | str | 火焰创建者id |
    | fireTime | float | 着火时间，单位秒 |
    | cancel | bool | 是否取消此处火焰伤害 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnGroundClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    实体着地事件。玩家，沙子，铁砧，掉落的物品，点燃的TNT掉落地面时触发，其余实体着地不触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnGroundServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体着地事件。实体，掉落的物品，点燃的TNT掉落地面时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnKnockBackServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体被击退时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnMobHitBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：通过OpenMobHitBlockDetection打开方块碰撞检测后，当生物（不包括玩家）碰撞到方块时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 碰撞到方块的生物Id |
    | posX | int | 碰撞方块x坐标 |
    | posY | int | 碰撞方块y坐标 |
    | posZ | int | 碰撞方块z坐标 |
    | blockId | str | 碰撞方块的identifier |
    | auxValue | int | 碰撞方块的附加值 |
    | dimensionId | int | 维度id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="OpenMobHitBlockDetection"></span>
### OpenMobHitBlockDetection

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    开启碰撞方块的检测，开启后，生物（不包括玩家）碰撞到方块时会触发OnMobHitBlockServerEvent事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物的实体Id |
    | precision | float | 碰撞检测精度，参数需要在区间[0, 1) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.OpenMobHitBlockDetection("-123456",0.0001)
```



<span id="CloseMobHitBlockDetection"></span>
### CloseMobHitBlockDetection

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    关闭碰撞方块的检测，关闭后，生物（不包括玩家）碰撞到方块时将不会触发OnMobHitBlockServerEvent事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物的实体Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.CloseMobHitBlockDetection("-123456")
```



## OnMobHitMobClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | mobId | str | 当前生物的id |
    | hittedMobList | list[str] | 当前生物碰撞到的其他所有生物id的list |

- 返回值

    无

- 备注
    - 本事件代替原有的OnPlayerHitMobClientEvent事件

- 示例

```python
# ClientSystem
import mod.client.extraClientApi as clientApi
self.ListenForEvent(clientApi.GetEngineNamespace(),
                    clientApi.GetEngineSystemName(),
                    "OnMobHitMobClientEvent",
                    self, self.OnMobHitMobClientEvent)
def OnMobHitMobClientEvent(self, args):
    mobId = args.get('mobId', '')
    hittedMobs = args.get('hittedMobList', [])
```



### 相关接口

<span id="OpenPlayerHitMobDetection"></span>
### OpenPlayerHitMobDetection

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    开启对其他生物的碰撞检测，开启后和生物间发生碰撞时会触发OnMobHitMobClientEvent事件。（该接口对生物同样有效）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否开启成功 |

- 备注
    - 该接口对生物同样有效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.OpenPlayerHitMobDetection()
```



<span id="ClosePlayerHitMobDetection"></span>
### ClosePlayerHitMobDetection

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    关闭碰撞生物的检测，关闭后将不会触发OnMobHitMobClientEvent事件。（该接口对生物同样有效）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否关闭成功 |

- 备注
    - 该接口对生物同样有效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.ClosePlayerHitMobDetection()
```



## OnMobHitMobServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：通过OpenPlayerHitMobDetection打开生物碰撞检测后，当生物间（包含玩家）碰撞时触发该事件。注：客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | mobId | str | 当前生物的id |
    | hittedMobList | list[str] | 当前生物碰撞到的其他所有生物id的list |

- 返回值

    无

- 备注
    - 本事件代替原有的OnPlayerHitMobServerEvent事件

- 示例

```python
# ServerSystem
import mod.server.extraServerApi as serverApi
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "OnMobHitMobServerEvent",
                    self, self.OnMobHitMobServerEvent)
def OnMobHitMobServerEvent(self, args):
    mobId = args.get('mobId', '')
    hittedMobs = args.get('hittedMobList', [])
```



### 相关接口

<span id="OpenPlayerHitMobDetection"></span>
### OpenPlayerHitMobDetection

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    开启对其他生物的碰撞检测，开启后和生物间发生碰撞时会触发OnMobHitMobServerEvent事件。（该接口对生物同样有效）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否开启成功 |

- 备注
    - 该接口对生物同样有效

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.OpenPlayerHitMobDetection()
```



<span id="ClosePlayerHitMobDetection"></span>
### ClosePlayerHitMobDetection

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    关闭碰撞生物的检测，关闭后将不会触发OnMobHitMobServerEvent事件。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否关闭成功 |

- 备注
    - 该接口对生物同样有效

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.ClosePlayerHitMobDetection()
```



## ProjectileCritHitEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当抛射物与头部碰撞时触发该事件。注：需调用OpenPlayerCritBox开启玩家爆头后才能触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 子弹id |
    | targetId | str | 碰撞目标id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="OpenPlayerCritBox"></span>
### OpenPlayerCritBox

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    开启玩家爆头，开启后该玩家头部被击中后会触发ProjectileCritHitEvent事件。

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.OpenPlayerCritBox()
```



<span id="ClosePlayerCritBox"></span>
### ClosePlayerCritBox

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    关闭玩家爆头，关闭后将无法触发ProjectileCritHitEvent事件。

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.ClosePlayerCritBox()
```



## ProjectileDoHitEffectEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当抛射物碰撞时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 子弹id |
    | hitTargetType | str | 碰撞目标类型,'ENTITY'或是'BLOCK' |
    | targetId | str | 碰撞目标id |
    | hitFace | int | 撞击在方块上的面id，参考[Facing枚举](../枚举值/Facing.md) |
    | x | float | 碰撞x坐标 |
    | y | float | 碰撞y坐标 |
    | z | float | 碰撞z坐标 |
    | blockPosX | int | 碰撞是方块时，方块x坐标 |
    | blockPosY | int | 碰撞是方块时，方块y坐标 |
    | blockPosZ | int | 碰撞是方块时，方块z坐标 |
    | srcId | str | 创建者id |
    | cancel | bool | 是否取消这个碰撞事件，若取消可以设置为True |

- 返回值

    无

- 示例

```python
# ServerSystem
import mod.server.extraServerApi as serverApi
# 监听引擎的事件 ：self指ServerSystem类的实例  ProjectileDoHitEffectEvent是系统事件
self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(),
                    "ProjectileDoHitEffectEvent", self, self.OnProjectileDoHitEffectEvent)
def OnProjectileDoHitEffectEvent(self, args):
    # 设为True后，将取消这次的抛射物碰撞事件
    args["cancel"] = True
```

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## RefreshEffectServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体身上状态效果更新时触发，更新条件1、新增状态等级较高，更新状态等级及时间；2、新增状态等级不变，时间较长，更新状态持续时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | effectName | str | 更新状态效果的名字 |
    | effectDuration | int | 更新后状态效果剩余持续时间，单位秒 |
    | effectAmplifier | int | 更新后的状态效果放大倍数 |
    | damage | int | 状态造成的伤害值，如药水 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## RemoveEffectServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体身上状态效果被移除时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | effectName | str | 被移除状态效果的名字 |
    | effectDuration | int | 被移除状态效果的剩余持续时间，单位秒 |
    | effectAmplifier | int | 被移除状态效果的放大倍数 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## SpawnProjectileServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：抛射物生成时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | projectileId | str | 抛射物的实体id |
    | projectileIdentifier | str | 抛射物的identifier |
    | spawnerId | str | 发射者的实体id，没有发射者时为-1 |

- 返回值

    无

- 备注
    - 该事件里无法获取弹射物实体的auxvalue。如有需要可以延迟一帧获取，或者在ProjectileDoHitEffectEvent获取

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StartRidingClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：一个实体即将骑乘另外一个实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorId | str | 骑乘者的唯一ID |
    | victimId | str | 被骑乘实体的唯一ID |

- 返回值

    无

- 备注
    - 如果需要修改cancel，请通过服务端事件StartRidingServerEvent同步修改，客户端触发该事件时，实体已经骑乘成功。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StartRidingServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：一个实体即将骑乘另外一个实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续的实体交互事件 |
    | actorId | str | 骑乘者的唯一ID |
    | victimId | str | 被骑乘实体的唯一ID |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WillAddEffectServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体即将获得状态效果前

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | effectName | str | 实体获得状态效果的名字 |
    | effectDuration | int | 状态效果的持续时间，单位秒 |
    | effectAmplifier | int | 状态效果的放大倍数 |
    | cancel | bool | 设置为True可以取消 |
    | damage | int | 状态将会造成的伤害值，如药水；需要注意，该值不一定是最终的伤害值，例如被伤害吸收效果扣除。只有持续时间为0时有用 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WillTeleportToServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    实体即将传送或切换维度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续的传送 |
    | entityId | str | 实体的唯一ID |
    | fromDimensionId | int | 传送前所在的维度 |
    | toDimensionId | int | 传送后的目标维度 |
    | fromX | int | 传送前所在的x坐标 |
    | fromY | int | 传送前所在的y坐标 |
    | fromZ | int | 传送前所在的z坐标 |
    | toX | int | 传送目标地点的x坐标 |
    | toY | int | 传送目标地点的y坐标 |
    | toZ | int | 传送目标地点的z坐标 |
    | cause | str | 传送理由，详情见MinecraftEnum.EntityTeleportCause |

- 返回值

    无

- 备注
    - 假如目标维度尚未在内存中创建（即服务器启动之后，到传送之前，没有玩家进入过这个维度），那么此时事件中返回的目标地点坐标是算法生成的，不能保证正确。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>

## 控制

# 控制

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ClientJumpButtonPressDownEvent](控制.md#clientjumpbuttonpressdownevent) | <span style="display:inline;color:#7575f9">客户端</span> | 跳跃按钮按下事件，返回值设置参数只对当次按下事件起作用 |
| [ClientJumpButtonReleaseEvent](控制.md#clientjumpbuttonreleaseevent) | <span style="display:inline;color:#7575f9">客户端</span> | 跳跃按钮按下释放事件 |
| [GetEntityByCoordEvent](控制.md#getentitybycoordevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击屏幕时触发，多个手指点在屏幕上时，只有第一个会触发。 |
| [GetEntityByCoordReleaseClientEvent](控制.md#getentitybycoordreleaseclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击屏幕后松开时触发，多个手指点在屏幕上时，只有最后一个手指松开时触发。 |
| [HoldBeforeClientEvent](控制.md#holdbeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家长按屏幕，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用RightClickBeforeClientEvent事件监听鼠标右键 |
| [LeftClickBeforeClientEvent](控制.md#leftclickbeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家按下鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。 |
| [LeftClickReleaseClientEvent](控制.md#leftclickreleaseclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家松开鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。 |
| [OnBackButtonReleaseClientEvent](控制.md#onbackbuttonreleaseclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 返回按钮（目前特指安卓系统导航中的返回按钮）松开时触发 |
| [OnClientPlayerStartMove](控制.md#onclientplayerstartmove) | <span style="display:inline;color:#7575f9">客户端</span> | 移动按钮按下触发事件，在按住一个方向键的同时，去按另外一个方向键，不会触发第二次 |
| [OnClientPlayerStopMove](控制.md#onclientplayerstopmove) | <span style="display:inline;color:#7575f9">客户端</span> | 移动按钮按下释放时触发事件，同时按下多个方向键，需要释放所有的方向键才会触发事件 |
| [OnKeyPressInGame](控制.md#onkeypressingame) | <span style="display:inline;color:#7575f9">客户端</span> | 按键按下或按键释放时触发 |
| [RightClickBeforeClientEvent](控制.md#rightclickbeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家按下鼠标右键时触发。仅在pc下触发（普通控制模式及F11模式都会触发）。 |
| [RightClickReleaseClientEvent](控制.md#rightclickreleaseclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家松开鼠标右键时触发。仅在pc的普通控制模式（即非F11模式）下触发。在F11下右键，按下会触发RightClickBeforeClientEvent，松开时会触发TapOrHoldReleaseClientEvent |
| [TapBeforeClientEvent](控制.md#tapbeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击屏幕并松手，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickBeforeClientEvent事件监听鼠标左键 |
| [TapOrHoldReleaseClientEvent](控制.md#taporholdreleaseclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击屏幕后松手时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickReleaseClientEvent与RightClickReleaseClientEvent事件监听鼠标松开 |
# 控制

## ClientJumpButtonPressDownEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    跳跃按钮按下事件，返回值设置参数只对当次按下事件起作用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | continueJump | bool | 设置是否执行跳跃逻辑 |

- 返回值

    无



## ClientJumpButtonReleaseEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    跳跃按钮按下释放事件

- 参数

    无

- 返回值

    无



## GetEntityByCoordEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击屏幕时触发，多个手指点在屏幕上时，只有第一个会触发。

- 参数

    无

- 返回值

    无



## GetEntityByCoordReleaseClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击屏幕后松开时触发，多个手指点在屏幕上时，只有最后一个手指松开时触发。

- 参数

    无

- 返回值

    无



## HoldBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家长按屏幕，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用RightClickBeforeClientEvent事件监听鼠标右键

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 设置为True可拦截原版的挖方块/使用物品/与实体交互响应 |

- 返回值

    无

- 备注
    - 玩家长按屏幕的处理顺序为：
        1. 玩家点击屏幕，在长按判定时间内（默认为400毫秒，可通过SetHoldTimeThreshold接口修改）一直没有进行拖动或松手
        2. 触发该事件
        3. 若事件没有cancel，则根据主手上的物品，准心处的物体类型以及与玩家的距离，进行挖方块/使用物品/与实体交互等操作
        即该事件只会在到达长按判定时间的瞬间触发一次，后面一直按住不会连续触发，可以使用TapOrHoldReleaseClientEvent监听长按后松手
    - 与TapBeforeClientEvent事件类似，被ui层捕获，没有穿透到世界的点击不会触发该事件



## LeftClickBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家按下鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 设置为True可拦截原版的挖方块或攻击响应 |

- 返回值

    无



## LeftClickReleaseClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家松开鼠标左键时触发。仅在pc的普通控制模式（即非F11模式）下触发。

- 参数

    无

- 返回值

    无



## OnBackButtonReleaseClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    返回按钮（目前特指安卓系统导航中的返回按钮）松开时触发

- 参数

    无

- 返回值

    无

- 备注
    - 目前仅安卓平台可用



## OnClientPlayerStartMove

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    移动按钮按下触发事件，在按住一个方向键的同时，去按另外一个方向键，不会触发第二次

- 参数

    无

- 返回值

    无



## OnClientPlayerStopMove

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    移动按钮按下释放时触发事件，同时按下多个方向键，需要释放所有的方向键才会触发事件

- 参数

    无

- 返回值

    无



## OnKeyPressInGame

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    按键按下或按键释放时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | screenName | str | 当前screenName |
    | key | str | 键码（注：这里的int型被转成了str型，比如"1"对应的就是枚举值文档中的1），详见[KeyBoardType枚举](../枚举值/KeyBoardType.md)| |
    | isDown | str | 是否按下，按下为1，弹起为0 |

- 返回值

    无



## RightClickBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家按下鼠标右键时触发。仅在pc下触发（普通控制模式及F11模式都会触发）。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 设置为True可拦截原版的物品使用/实体交互响应 |

- 返回值

    无



## RightClickReleaseClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家松开鼠标右键时触发。仅在pc的普通控制模式（即非F11模式）下触发。在F11下右键，按下会触发RightClickBeforeClientEvent，松开时会触发TapOrHoldReleaseClientEvent

- 参数

    无

- 返回值

    无

- 备注
    - pc的普通控制模式下的鼠标点击流程见[TapOrHoldReleaseClientEvent](#taporholdreleaseclientevent)备注中的配图



## TapBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击屏幕并松手，即将响应到游戏内时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickBeforeClientEvent事件监听鼠标左键

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 设置为True可拦截原版的攻击或放置响应 |

- 返回值

    无

- 备注
    - 玩家点击屏幕的处理顺序为：
        1. 玩家点击屏幕，没有进行拖动，并在短按判定时间（250毫秒）内松手
        2. 触发该事件
        3. 若事件没有cancel，则根据准心处的物体类型以及与玩家的距离，进行攻击或放置等操作
    - 与GetEntityByCoordEvent事件不同的是，被ui层捕获，没有穿透到世界的点击不会触发该事件，例如：
        1. 点击原版的移动/跳跃等按钮，
        2. 通过SetIsHud(0)屏蔽了游戏操作
        3. 对按钮使用AddTouchEventHandler接口时isSwallow参数设置为True



## TapOrHoldReleaseClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击屏幕后松手时触发。仅在移动端或pc的F11模式下触发。pc的非F11模式可以使用LeftClickReleaseClientEvent与RightClickReleaseClientEvent事件监听鼠标松开

- 参数

    无

- 返回值

    无

- 备注
    - 短按及长按后松手都会触发该事件
    - 移动端及pc的F11模式下点触流程见下图
        ![点触说明](../picture/pe_touch_event.png)

## 方块

# 方块

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [BlockDestroyByLiquidServerEvent](方块.md#blockdestroybyliquidserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：方块被水流破坏的事件 |
| [BlockLiquidStateChangeAfterServerEvent](方块.md#blockliquidstatechangeafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：方块转为含水或者脱离含水(流体)后触发 |
| [BlockLiquidStateChangeServerEvent](方块.md#blockliquidstatechangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：方块转为含水或者脱离含水(流体)前触发 |
| [BlockNeighborChangedServerEvent](方块.md#blockneighborchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：自定义方块周围的方块发生变化时，需要配置netease:neighborchanged_sendto_script，详情请查阅《自定义农作物》文档 |
| [BlockRandomTickServerEvent](方块.md#blockrandomtickserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：自定义方块配置<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-random-tick">netease:random_tick</a>随机tick时 |
| [BlockRemoveServerEvent](方块.md#blockremoveserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：监听该事件的方块在销毁时触发，可以通过[ListenOnBlockRemoveEvent](#listenonblockremoveevent)方法进行监听，或者通过json组件<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-listen-block-remove">netease:listen_block_remove</a>进行配置 |
| [BlockSnowStateChangeAfterServerEvent](方块.md#blocksnowstatechangeafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：方块转为含雪或者脱离含雪后触发 |
| [BlockSnowStateChangeServerEvent](方块.md#blocksnowstatechangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：方块转为含雪或者脱离含雪前触发 |
| [BlockStrengthChangedServerEvent](方块.md#blockstrengthchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：自定义机械元件方块红石信号量发生变化时触发 |
| [ChestBlockTryPairWithServerEvent](方块.md#chestblocktrypairwithserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：两个并排的小箱子方块准备组合为一个大箱子方块时 |
| [ClientBlockUseEvent](方块.md#clientblockuseevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时客户端抛出该事件（该事件tick执行，需要注意效率问题）。 |
| [CommandBlockContainerOpenEvent](方块.md#commandblockcontaineropenevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家点击命令方块，尝试打开命令方块的设置界面 |
| [CommandBlockUpdateEvent](方块.md#commandblockupdateevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家尝试修改命令方块的内置命令时 |
| [DestroyBlockEvent](方块.md#destroyblockevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当方块已经被玩家破坏时触发该事件。 |
| [DirtBlockToGrassBlockServerEvent](方块.md#dirtblocktograssblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：泥土方块变成草方块时触发 |
| [EntityPlaceBlockAfterServerEvent](方块.md#entityplaceblockafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当生物成功放置方块后触发 |
| [FallingBlockBreakServerEvent](方块.md#fallingblockbreakserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当下落的方块实体被破坏时，服务端触发该事件 |
| [FallingBlockCauseDamageBeforeClientEvent](方块.md#fallingblockcausedamagebeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件 |
| [FallingBlockCauseDamageBeforeServerEvent](方块.md#fallingblockcausedamagebeforeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当下落的方块开始计算砸到实体的伤害时，服务端触发该事件 |
| [FallingBlockReturnHeavyBlockServerEvent](方块.md#fallingblockreturnheavyblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当下落的方块实体变回普通重力方块时，服务端触发该事件 |
| [FarmBlockToDirtBlockServerEvent](方块.md#farmblocktodirtblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：耕地退化为泥土时触发 |
| [GrassBlockToDirtBlockServerEvent](方块.md#grassblocktodirtblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：草方块变成泥土方块时触发 |
| [HeavyBlockStartFallingServerEvent](方块.md#heavyblockstartfallingserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当重力方块变为下落的方块实体后，服务端触发该事件 |
| [HopperTryPullInServerEvent](方块.md#hoppertrypullinserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次 |
| [HopperTryPullOutServerEvent](方块.md#hoppertrypulloutserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次 |
| [OnAfterFallOnBlockClientEvent](方块.md#onafterfallonblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：当实体降落到方块后客户端触发，主要用于力的计算 |
| [OnAfterFallOnBlockServerEvent](方块.md#onafterfallonblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当实体降落到方块后服务端触发，主要用于力的计算 |
| [OnBeforeFallOnBlockServerEvent](方块.md#onbeforefallonblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当实体刚降落到方块上时服务端触发，主要用于伤害计算 |
| [OnEntityInsideBlockClientEvent](方块.md#onentityinsideblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：当实体碰撞盒所在区域有方块时，客户端持续触发 |
| [OnEntityInsideBlockServerEvent](方块.md#onentityinsideblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当实体碰撞盒所在区域有方块时，服务端持续触发 |
| [OnModBlockNeteaseEffectCreatedClientEvent](方块.md#onmodblockneteaseeffectcreatedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 自定义方块实体绑定的特效创建成功事件，在自定义方块实体中绑定的特效创建成功时触发以及使用接口CreateFrameEffectForBlockEntity或CreateParticleEffectForBlockEntity为自定义方块实体添加特效成功时触发。 |
| [OnStandOnBlockClientEvent](方块.md#onstandonblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：当实体站立到方块上时客户端持续触发 |
| [OnStandOnBlockServerEvent](方块.md#onstandonblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当实体站立到方块上时服务端持续触发 |
| [PistonActionServerEvent](方块.md#pistonactionserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：活塞或者粘性活塞推送/缩回影响附近方块时 |
| [PlayerTryDestroyBlockClientEvent](方块.md#playertrydestroyblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 当玩家即将破坏方块时，客户端线程触发该事件。主要用于床，旗帜，箱子这些根据方块实体数据进行渲染的方块，一般情况下请使用ServerPlayerTryDestroyBlockEvent |
| [ServerBlockEntityTickEvent](方块.md#serverblockentitytickevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：自定义方块配置了netease:block_entity组件并设tick为true，方块在玩家的模拟距离（新建存档时可以设置，默认为4个区块）内，或者在tickingarea内的时候触发 |
| [ServerBlockUseEvent](方块.md#serverblockuseevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时服务端抛出该事件（该事件tick执行，需要注意效率问题）。 |
| [ServerEntityTryPlaceBlockEvent](方块.md#serverentitytryplaceblockevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当生物试图放置方块时触发该事件。 |
| [ServerPlaceBlockEntityEvent](方块.md#serverplaceblockentityevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：手动放置或通过接口创建含自定义方块实体的方块时触发，此时可向该方块实体中存放数据 |
| [ServerPlayerTryDestroyBlockEvent](方块.md#serverplayertrydestroyblockevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当玩家即将破坏方块时，服务端线程触发该事件。 |
| [ShearsDestoryBlockBeforeClientEvent](方块.md#shearsdestoryblockbeforeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在客户端线程触发该事件 |
| [ShearsDestoryBlockBeforeServerEvent](方块.md#shearsdestoryblockbeforeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程触发该事件 |
| [StartDestroyBlockClientEvent](方块.md#startdestroyblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家开始挖方块时触发。创造模式下不触发。 |
| [StartDestroyBlockServerEvent](方块.md#startdestroyblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家开始挖方块时触发。创造模式下不触发。 |
| [StepOffBlockClientEvent](方块.md#stepoffblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：实体移动离开一个实心方块时触发 |
| [StepOffBlockServerEvent](方块.md#stepoffblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体移动离开一个实心方块时触发 |
| [StepOnBlockClientEvent](方块.md#steponblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：实体刚移动至一个新实心方块时触发。 |
| [StepOnBlockServerEvent](方块.md#steponblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体刚移动至一个新实心方块时触发。 |
# 方块

## BlockDestroyByLiquidServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：方块被水流破坏的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | liquidName | str | 流体方块id |
    | blockName | str | 方块id |
    | auxValue | int | 方块附加值 |

- 返回值

    无

- 备注
    - 指令或者接口的设置不会触发该事件



## BlockLiquidStateChangeAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：方块转为含水或者脱离含水(流体)后触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块附加值 |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | turnLiquid | bool | 是否转为含水，true则转为含水，false则脱离含水 |

- 返回值

    无



## BlockLiquidStateChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：方块转为含水或者脱离含水(流体)前触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块附加值 |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | turnLiquid | bool | 是否转为含水，true则转为含水，false则脱离含水 |

- 返回值

    无



## BlockNeighborChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：自定义方块周围的方块发生变化时，需要配置netease:neighborchanged_sendto_script，详情请查阅《自定义农作物》文档

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度 |
    | posX | int | 方块x坐标 |
    | posY | int | 方块y坐标 |
    | posZ | int | 方块z坐标 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块附加值 |
    | neighborPosX | int | 变化方块x坐标 |
    | neighborPosY | int | 变化方块y坐标 |
    | neighborPosZ | int | 变化方块z坐标 |
    | fromBlockName | str | 方块变化前的identifier，包含命名空间及名称 |
    | fromBlockAuxValue | int | 方块变化前附加值 |
    | toBlockName | str | 方块变化后的identifier，包含命名空间及名称 |
    | toAuxValue | int | 方块变化后附加值 |

- 返回值

    无



## BlockRandomTickServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：自定义方块配置<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-random-tick">netease:random_tick</a>随机tick时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posX | int | 方块x坐标 |
    | posY | int | 方块y坐标 |
    | posZ | int | 方块z坐标 |
    | blockName | str | 方块名称 |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块附加值 |
    | dimensionId | int | 实体维度 |

- 返回值

    无



## BlockRemoveServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：监听该事件的方块在销毁时触发，可以通过[ListenOnBlockRemoveEvent](#listenonblockremoveevent)方法进行监听，或者通过json组件<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-listen-block-remove">netease:listen_block_remove</a>进行配置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块位置x |
    | y | int | 方块位置y |
    | z | int | 方块位置z |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块的附加值 |
    | dimension | int | 该方块所在的维度 |

- 返回值

    无



### 相关接口

<span id="ListenOnBlockRemoveEvent"></span>
### ListenOnBlockRemoveEvent

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    是否监听方块BlockRemoveServerEvent事件，可以动态修改json组件<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-listen-block-remove">netease:listen_block_remove</a>的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 方块identifier，如minecraft:wheat |
    | listen | bool | 是否监听 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 对于一些特殊的方块，注意要使用对应的方块Id参数（如砖块楼梯，监听的方块Id应该为minecraft:brick_block）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.ListenOnBlockRemoveEvent("minecraft:wheat", True)
```



## BlockSnowStateChangeAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：方块转为含雪或者脱离含雪后触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | turnSnow | bool | 是否转为含雪，true则转为含雪，false则脱离含雪 |
    | setBlockType | int | 方块进入脱离含雪的原因，参考[SetBlockType](../枚举值/SetBlockType.md) |

- 返回值

    无



## BlockSnowStateChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：方块转为含雪或者脱离含雪前触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | turnSnow | bool | 是否转为含雪，true则转为含雪，false则脱离含雪 |
    | setBlockType | int | 方块进入脱离含雪的原因，参考[SetBlockType](../枚举值/SetBlockType.md) |

- 返回值

    无



## BlockStrengthChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：自定义机械元件方块红石信号量发生变化时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posX | int | 方块x坐标 |
    | posY | int | 方块y坐标 |
    | posZ | int | 方块z坐标 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块附加值 |
    | newStrength | int | 变化后的红石信号量 |
    | dimensionId | int | 维度 |

- 返回值

    无



## ChestBlockTryPairWithServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：两个并排的小箱子方块准备组合为一个大箱子方块时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止小箱子组合成为一个大箱子 |
    | blockX | int | 小箱子方块x坐标 |
    | blockY | int | 小箱子方块y坐标 |
    | blockZ | int | 小箱子方块z坐标 |
    | otherBlockX | int | 将要与之组合的另外一个小箱子方块x坐标 |
    | otherBlockY | int | 将要与之组合的另外一个小箱子方块y坐标 |
    | otherBlockZ | int | 将要与之组合的另外一个小箱子方块z坐标 |
    | dimensionId | int | 维度id |

- 返回值

    无



## ClientBlockUseEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时客户端抛出该事件（该事件tick执行，需要注意效率问题）。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | aux | int | 方块附加值 |
    | cancel | bool | 设置为True可拦截与方块交互的逻辑。 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |

- 返回值

    无

- 备注
    - 有的方块是在ServerBlockUseEvent中设置cancel生效，但是有部分方块是在ClientBlockUseEvent中设置cancel才生效，如有需求建议在两个事件中同时设置cancel以保证生效。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="AddBlockItemListenForUseEvent"></span>
### AddBlockItemListenForUseEvent

method in mod.client.component.blockUseEventWhiteListCompClient.BlockUseEventWhiteListComponentClient

- 描述

    增加blockName方块对ClientBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(clientApi.GetLevelId())
comp.AddBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://minecraft-zh.gamepedia.com/楼梯 中的‘方块数据值’
```



<span id="RemoveBlockItemListenForUseEvent"></span>
### RemoveBlockItemListenForUseEvent

method in mod.client.component.blockUseEventWhiteListCompClient.BlockUseEventWhiteListComponentClient

- 描述

    移除blockName方块对ClientBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(clientApi.GetLevelId())
comp.RemoveBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://minecraft-zh.gamepedia.com/楼梯 中的‘方块数据值’
```



<span id="ClearAllListenForBlockUseEventItems"></span>
### ClearAllListenForBlockUseEventItems

method in mod.client.component.blockUseEventWhiteListCompClient.BlockUseEventWhiteListComponentClient

- 描述

    清空所有已添加方块对ClientBlockUseEvent事件的脚本层监听

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(clientApi.GetLevelId())
comp.ClearAllListenForBlockUseEventItems()
```



## CommandBlockContainerOpenEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家点击命令方块，尝试打开命令方块的设置界面

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | isBlock | bool | 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义 |
    | blockX | int | 命令方块位置x，当isBlock为True时有效 |
    | blockY | int | 命令方块位置y，当isBlock为True时有效 |
    | blockZ | int | 命令方块位置z，当isBlock为True时有效 |
    | victimId | str | 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效 |
    | cancel | bool | 修改为True时，可以阻止玩家打开命令方块的设置界面 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## CommandBlockUpdateEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家尝试修改命令方块的内置命令时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | playerUid | int/long | 玩家的uid |
    | command | str | 企图修改的命令方块中的命令内容字符串 |
    | isBlock | bool | 是否以方块坐标的形式定位命令方块，当为True时下述的blockX/blockY/blockZ有意义，当为False时，下述的victimId有意义 |
    | blockX | int | 命令方块位置x，当isBlock为True时有效 |
    | blockY | int | 命令方块位置y，当isBlock为True时有效 |
    | blockZ | int | 命令方块位置z，当isBlock为True时有效 |
    | victimId | str | 命令方块对应的逻辑实体的唯一id，当isBlock为False时有效 |
    | cancel | bool | 修改为True时，可以阻止玩家修改命令方块的内置命令 |

- 返回值

    无

- 备注
    - 当修改的目标为命令方块矿车时（此时isBlock为False），设置cancel为True，依旧可以阻止修改命令方块矿车的内部指令，但是从客户端能够看到命令方块矿车的内部指令变化了，不过这仅仅是假象，重新登录或者其他客户端打开命令方块矿车的设置界面，就会发现其实内部指令没有变化

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DestroyBlockEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当方块已经被玩家破坏时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | face | int | 方块被敲击的面向id，参考[Facing枚举](../枚举值/Facing.md) |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | playerId | str | 破坏方块的玩家ID |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 在生存模式或创造模式下都会触发

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DirtBlockToGrassBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：泥土方块变成草方块时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |

- 返回值

    无

- 备注
    - 指令或者接口的设置不会触发该事件



## EntityPlaceBlockAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当生物成功放置方块后触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | entityId | str | 试图放置方块的生物ID |
    | dimensionId | int | 维度id |
    | face | int | 点击方块的面，参考[Facing枚举](../枚举值/Facing.md) |

- 返回值

    无

- 备注
    - 部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、花盆、红石中继器、船、炼药锅、头部模型、蛋糕、酿造台、盔甲架等。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## FallingBlockBreakServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当下落的方块实体被破坏时，服务端触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fallingBlockId | str | 下落的方块实体id |
    | fallingBlockX | float | 下落的方块实体位置x |
    | fallingBlockY | float | 下落的方块实体位置y |
    | fallingBlockZ | float | 下落的方块实体位置z |
    | blockName | str | 重力方块的identifier，包含命名空间及名称 |
    | fallTickAmount | int | 下落的方块实体持续下落了多少tick |
    | dimensionId | int | 下落的方块实体维度id |
    | cancelDrop | bool | 是否取消方块物品掉落，可以在脚本层中设置 |

- 返回值

    无

- 备注
    - 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html">自定义重力方块</a>）



## FallingBlockCauseDamageBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：当下落的方块开始计算砸到实体的伤害时，客户端触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fallingBlockId | int | 下落的方块实体id |
    | fallingBlockX | float | 下落的方块实体位置x |
    | fallingBlockY | float | 下落的方块实体位置y |
    | fallingBlockZ | float | 下落的方块实体位置z |
    | blockName | str | 重力方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 下落的方块实体维度id |
    | collidingEntitys | list(str) | 当前碰撞到的实体列表id（客户端只能获取到玩家），如果没有的话是None |
    | fallTickAmount | int | 下落的方块实体持续下落了多少tick |
    | fallDistance | float | 下落的方块实体持续下落了多少距离 |
    | isHarmful | bool | 客户端始终为false，因为客户端不会计算伤害值 |
    | fallDamage | int | 对实体的伤害 |

- 返回值

    无

- 备注
    - 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html">自定义重力方块</a>）
    - 当该事件的参数数据（fallTickAmount，fallDistance，collidingEntitys，fallDamage）与服务端事件FallingBlockCauseDamageBeforeServerEvent数据有差异时，请以服务端事件数据为准。



## FallingBlockCauseDamageBeforeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当下落的方块开始计算砸到实体的伤害时，服务端触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fallingBlockId | str | 下落的方块实体id |
    | fallingBlockX | float | 下落的方块实体位置x |
    | fallingBlockY | float | 下落的方块实体位置y |
    | fallingBlockZ | float | 下落的方块实体位置z |
    | blockName | str | 重力方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 下落的方块实体维度id |
    | collidingEntitys | list(str) | 当前碰撞到的实体列表id，如果没有的话是None |
    | fallTickAmount | int | 下落的方块实体持续下落了多少tick |
    | fallDistance | float | 下落的方块实体持续下落了多少距离 |
    | isHarmful | bool | 是否计算对实体的伤害，引擎传来的值由json配置和伤害是否大于0决定，可在脚本层修改传回引擎 |
    | fallDamage | int | 对实体的伤害，引擎传来的值距离和json配置决定，可在脚本层修改传回引擎 |

- 返回值

    无

- 备注
    - 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html">自定义重力方块</a>）
    - 服务端通常触发在客户端之后，而且有时会相差一个tick，这就意味着可能发生以下现象:服务端fallTickAmount比配置强制破坏时间多1tick，下落的距离、下落的伤害计算出来比客户端时间多1tick的误差。



## FallingBlockReturnHeavyBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当下落的方块实体变回普通重力方块时，服务端触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fallingBlockId | int | 下落的方块实体id |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | heavyBlockName | str | 重力方块的identifier，包含命名空间及名称 |
    | prevHereBlockName | str | 变回重力方块时，原本方块位置的identifier，包含命名空间及名称 |
    | dimensionId | int | 下落的方块实体维度id |
    | fallTickAmount | int | 下落的方块实体持续下落了多少tick |

- 返回值

    无

- 备注
    - 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html">自定义重力方块</a>）



## FarmBlockToDirtBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：耕地退化为泥土时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | setBlockType | int | 耕地退化为泥土的原因，参考[SetBlockType](../枚举值/SetBlockType.md) |

- 返回值

    无

- 备注
    - 指令或者接口的设置不会触发该事件



## GrassBlockToDirtBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：草方块变成泥土方块时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 方块维度 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |

- 返回值

    无

- 备注
    - 指令或者接口的设置不会触发该事件



## HeavyBlockStartFallingServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当重力方块变为下落的方块实体后，服务端触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fallingBlockId | str | 下落的方块实体id |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 重力方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 下落的方块实体维度id |

- 返回值

    无

- 备注
    - 不是所有下落的方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html">自定义重力方块</a>）



## HopperTryPullInServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 漏斗位置x |
    | y | int | 漏斗位置y |
    | z | int | 漏斗位置z |
    | abovePosX | int | 交互的容器位置x |
    | abovePosY | int | 交互的容器位置y |
    | abovePosZ | int | 交互的容器位置z |
    | dimensionId | int | 维度id |
    | canHopper | bool | 是否允许容器往漏斗加东西(要关闭此交互，需先监听此事件再放置容器) |

- 返回值

    无



## HopperTryPullOutServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 漏斗位置x |
    | y | int | 漏斗位置y |
    | z | int | 漏斗位置z |
    | attachedPosX | int | 交互的容器位置x |
    | attachedPosY | int | 交互的容器位置y |
    | attachedPosZ | int | 交互的容器位置z |
    | dimensionId | int | 维度id |
    | canHopper | bool | 是否允许漏斗往容器加东西(要关闭此交互，需先监听此事件再放置容器) |

- 返回值

    无



## OnAfterFallOnBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：当实体降落到方块后客户端触发，主要用于力的计算

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | posX | float | 实体位置x |
    | posY | float | 实体位置y |
    | posZ | float | 实体位置z |
    | motionX | float | 瞬时移动X方向的力 |
    | motionY | float | 瞬时移动Y方向的力 |
    | motionZ | float | 瞬时移动Z方向的力 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | calculate | bool | 是否按脚本层传值计算力 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
    - 如果要在脚本层修改motion，回传的需要是浮点型，例如需要赋值0.0而不是0
    - 如果需要修改实体的力，最好配合服务端事件同步修改，避免产生非预期现象
    - 因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
    - 引擎在落地之后OnAfterFallOnBlockClientEvent会一直触发，因此请在脚本层中做对应的逻辑判断

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnAfterFallOnBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当实体降落到方块后服务端触发，主要用于力的计算

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | posX | float | 实体位置x |
    | posY | float | 实体位置y |
    | posZ | float | 实体位置z |
    | motionX | float | 瞬时移动X方向的力 |
    | motionY | float | 瞬时移动Y方向的力 |
    | motionZ | float | 瞬时移动Z方向的力 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | calculate | bool | 是否按脚本层传值计算力 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
    - 如果要在脚本层修改motion，回传的需要是浮点型，例如需要赋值0.0而不是0
    - 如果需要修改实体的力，最好配合客户端事件同步修改，避免产生非预期现象
    - 因为引擎最后一定会按照原版方块规则计算力（普通方块置0，床、粘液块等反弹），所以脚本层如果想直接修改当前力需要将calculate设为true取消原版计算，按照传回值计算
    - 引擎在落地之后，OnAfterFallOnBlockServerEvent会一直触发，因此请在脚本层中做对应的逻辑判断

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnBeforeFallOnBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当实体刚降落到方块上时服务端触发，主要用于伤害计算

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | fallDistance | float | 实体下降距离，可在脚本层传给引擎 |
    | cancel | bool | 是否取消引擎对实体下降伤害的计算 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
    - 如果要在脚本层修改fallDistance，回传的一定要是浮点型，例如需要赋值0.0而不是0
    - 可能会因为轻微的反弹触发多次，可在脚本层针对fallDistance的值进行判断

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnEntityInsideBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：当实体碰撞盒所在区域有方块时，客户端持续触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | dimensionId | int | 实体所在维度id |
    | slowdownMultiX | float | 实体移速X方向的减速比例 |
    | slowdownMultiY | float | 实体移速Y方向的减速比例 |
    | slowdownMultiZ | float | 实体移速Z方向的减速比例 |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | cancel | bool | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
        ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
    - 如果需要修改slowdownMulti/cancel，强烈建议与服务端事件同步修改，避免出现被服务端矫正等非预期现象。
    - 如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
    - 有任意slowdownMulti参数被传回非0值时生效减速比例
    - slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnEntityInside"></span>
### RegisterOnEntityInside

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态注册与修改netease:on_entity_inside组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_entity_inside组件
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnEntityInside接口

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnEntityInside("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnEntityInside"></span>
### UnRegisterOnEntityInside

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态删除netease:on_entity_inside组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_entity_inside组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnEntityInside("minecraft:redstone_ore")
```



## OnEntityInsideBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当实体碰撞盒所在区域有方块时，服务端持续触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | slowdownMultiX | float | 实体移速X方向的减速比例，可在脚本层被修改 |
    | slowdownMultiY | float | 实体移速Y方向的减速比例，可在脚本层被修改 |
    | slowdownMultiZ | float | 实体移速Z方向的减速比例，可在脚本层被修改 |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | cancel | bool | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
        ，原版方块需要先通过RegisterOnEntityInside接口注册才能触发
    - 如果需要修改slowdownMulti/cancel，强烈建议与客户端事件同步修改，避免出现客户端表现不一致等非预期现象。
    - 如果要在脚本层修改slowdownMulti，回传的一定要是浮点型，例如需要赋值1.0而不是1
    - 有任意slowdownMulti参数被传回非0值时生效减速比例
    - slowdownMulti参数更像是一个Buff，例如并不是立刻计算，而是先保存在实体属性里延后计算、在已经有slowdownMulti属性的情况下会取最低的值、免疫掉落伤害等，与原版蜘蛛网逻辑基本一致。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnEntityInside"></span>
### RegisterOnEntityInside

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态注册与修改netease:on_entity_inside组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_entity_inside组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnEntityInside接口

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnEntityInside("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnEntityInside"></span>
### UnRegisterOnEntityInside

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态删除netease:on_entity_inside组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_entity_inside组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnEntityInside("minecraft:redstone_ore")
```



## OnModBlockNeteaseEffectCreatedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    自定义方块实体绑定的特效创建成功事件，在自定义方块实体中绑定的特效创建成功时触发以及使用接口CreateFrameEffectForBlockEntity或CreateParticleEffectForBlockEntity为自定义方块实体添加特效成功时触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectName | str | 创建成功的特效的自定义键值名称 |
    | id | int | 该特效的id |
    | effectType | int | 该特效的类型，0为粒子特效，1为序列帧特效 |
    | blockPos | tuple(float,float,float) | 该特效绑定的自定义方块实体的世界坐标 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnStandOnBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：当实体站立到方块上时客户端持续触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | dimensionId | int | 实体所在维度id |
    | posX | float | 实体位置x |
    | posY | float | 实体位置y |
    | posZ | float | 实体位置z |
    | motionX | float | 瞬时移动X方向的力 |
    | motionY | float | 瞬时移动Y方向的力 |
    | motionZ | float | 瞬时移动Z方向的力 |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | cancel | bool | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
        ，原版方块需要先通过RegisterOnStandOn接口注册才能触发
    - 如果要在脚本层修改motion/cancel，强烈建议配合OnStandOnBlockServerEvent服务端事件同步修改，避免出现被服务端矫正等非预期现象
    - 如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStandOn"></span>
### RegisterOnStandOn

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态注册与修改netease:on_stand_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_stand_on组件
    - 游戏原版逻辑是不会跑方块客户端OnStandOn相关逻辑，使用接口给原版方块添加客户端组件的话，无论是否发送python事件，都会使原版方块多跑客户端相关逻辑，
        例如粘液块这种会有一定物理计算的方块，在客户端多跑一次计算之后，会有手感上的差别。
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnStandOn接口

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStandOn("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStandOn"></span>
### UnRegisterOnStandOn

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态删除netease:on_stand_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_stand_on组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStandOn("minecraft:redstone_ore")
```



## OnStandOnBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当实体站立到方块上时服务端持续触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |
    | dimensionId | int | 实体所在维度id |
    | posX | float | 实体位置x |
    | posY | float | 实体位置y |
    | posZ | float | 实体位置z |
    | motionX | float | 瞬时移动X方向的力 |
    | motionY | float | 瞬时移动Y方向的力 |
    | motionZ | float | 瞬时移动Z方向的力 |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | cancel | bool | 可由脚本层回传True给引擎，阻止触发后续原版逻辑 |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>）
        ，原版方块需要先通过RegisterOnStandOn接口注册才能触发
    - 如果需要修改motion/cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等现象
    - 如果要在脚本层修改motion，回传的一定要是浮点型，例如需要赋值0.0而不是0

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStandOn"></span>
### RegisterOnStandOn

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态注册与修改netease:on_stand_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_stand_on组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件
    - 游戏原版逻辑是不会跑方块客户端OnStandOn相关逻辑，使用接口给原版方块添加客户端组件的话，无论是否发送python事件，都会使原版方块多跑客户端相关逻辑，
        例如粘液块这种会有一定物理计算的方块，在客户端多跑一次计算之后，会有手感上的差别。
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnStandOn接口

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStandOn("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStandOn"></span>
### UnRegisterOnStandOn

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态删除netease:on_stand_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_stand_on组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStandOn("minecraft:redstone_ore")
```



## PistonActionServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：活塞或者粘性活塞推送/缩回影响附近方块时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续的事件 |
    | action | str | 推送时=expanding；缩回时=retracting |
    | pistonFacing | int | 活塞的朝向，参考[Facing枚举](../枚举值/Facing.md) |
    | pistonMoveFacing | int | 活塞的运动方向，参考[Facing枚举](../枚举值/Facing.md) |
    | dimensionId | int | 活塞方块所在的维度 |
    | pistonX | int | 活塞方块的x坐标 |
    | pistonY | int | 活塞方块的y坐标 |
    | pistonZ | int | 活塞方块的z坐标 |
    | blockList | list[(x,y,z),...] | 活塞运动影响到产生被移动效果的方块坐标(x,y,z)，均为int类型 |
    | breakBlockList | list[(x,y,z),...] | 活塞运动影响到产生被破坏效果的方块坐标(x,y,z)，均为int类型 |
    | entityList | list[string,...] | 活塞运动影响到产生被移动或被破坏效果的实体的ID列表 |

- 返回值

    无



## PlayerTryDestroyBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    当玩家即将破坏方块时，客户端线程触发该事件。主要用于床，旗帜，箱子这些根据方块实体数据进行渲染的方块，一般情况下请使用ServerPlayerTryDestroyBlockEvent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | face | int | 方块被敲击的面向id，参考[Facing枚举](../枚举值/Facing.md) |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | playerId | str | 试图破坏方块的玩家ID |
    | cancel | bool | 默认为False，在脚本层设置为True就能取消该方块的破坏 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerBlockEntityTickEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：自定义方块配置了netease:block_entity组件并设tick为true，方块在玩家的模拟距离（新建存档时可以设置，默认为4个区块）内，或者在tickingarea内的时候触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 该方块名称 |
    | dimension | int | 该方块所在的维度 |
    | posX | int | 该方块的x坐标 |
    | posY | int | 该方块的y坐标 |
    | posZ | int | 该方块的z坐标 |

- 返回值

    无

- 备注
    - **方块实体的tick事件频率为每秒钟20次**
    - 触发本事件时，若正在退出游戏，将无法获取到抛出本事件的方块实体数据（GetBlockEntityData函数返回None），也无法对其进行操作



## ServerBlockUseEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家右键点击新版自定义方块（或者通过接口AddBlockItemListenForUseEvent增加监听的MC原生游戏方块）时服务端抛出该事件（该事件tick执行，需要注意效率问题）。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | aux | int | 方块附加值 |
    | cancel | bool | 设置为True可拦截与方块交互的逻辑。 |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 当对原生方块进行使用时，如堆肥桶等类似有 使用 功能的方块使用物品时，会触发该事件，而ServerItemUseOnEvent则不会被触发。当需要获取触发时使用的物品时，可以通过item组件获取手上有的物品。对应的客户端事件同理。
    - 有的方块是在ServerBlockUseEvent中设置cancel生效，但是有部分方块是在ClientBlockUseEvent中设置cancel才生效，如有需求建议在两个事件中同时设置cancel以保证生效。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="AddBlockItemListenForUseEvent"></span>
### AddBlockItemListenForUseEvent

method in mod.server.component.blockUseEventWhiteListCompServer.BlockUseEventWhiteListComponentServer

- 描述

    增加blockName方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(levelId)
comp.AddBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://minecraft-zh.gamepedia.com/楼梯 中的‘方块数据值’
```



<span id="RemoveBlockItemListenForUseEvent"></span>
### RemoveBlockItemListenForUseEvent

method in mod.server.component.blockUseEventWhiteListCompServer.BlockUseEventWhiteListComponentServer

- 描述

    移除blockName方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称，格式：namespace:name:auxvalue，其中namespace:name:*匹配所有的auxvalue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(levelId)
comp.RemoveBlockItemListenForUseEvent("minecraft:nether_brick_stairs:2")
# 注意blockName格式为namespace:name:auxvalue，如果不填auxvalue，则默认为0
# auxValue详细值详见官方wiki，如https://minecraft-zh.gamepedia.com/楼梯 中的‘方块数据值’
```



<span id="ClearAllListenForBlockUseEventItems"></span>
### ClearAllListenForBlockUseEventItems

method in mod.server.component.blockUseEventWhiteListCompServer.BlockUseEventWhiteListComponentServer

- 描述

    清空所有已添加方块对ServerBlockUseEvent事件的脚本层监听

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockUseEventWhiteList(levelId)
comp.ClearAllListenForBlockUseEventItems()
```



## ServerEntityTryPlaceBlockEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当生物试图放置方块时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | entityId | str | 试图放置方块的生物ID |
    | dimensionId | int | 维度id |
    | face | int | 点击方块的面，参考[Facing枚举](../枚举值/Facing.md) |
    | cancel | bool | 默认为False，在脚本层设置为True就能取消该方块的放置 |

- 返回值

    无

- 备注
    - 部分放置后会产生实体的方块、可操作的方块、带有特殊逻辑的方块，不会触发该事件，包括但不限于床、门、告示牌、花盆、红石中继器、船、炼药锅、头部模型、蛋糕、酿造台、盔甲架等。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerPlaceBlockEntityEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：手动放置或通过接口创建含自定义方块实体的方块时触发，此时可向该方块实体中存放数据

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 该方块名称 |
    | dimension | int | 该方块所在的维度 |
    | posX | int | 该方块的x坐标 |
    | posY | int | 该方块的y坐标 |
    | posZ | int | 该方块的z坐标 |

- 返回值

    无



## ServerPlayerTryDestroyBlockEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当玩家即将破坏方块时，服务端线程触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | x | int | 方块x坐标 |
    | y | int | 方块y坐标 |
    | z | int | 方块z坐标 |
    | face | int | 方块被敲击的面向id，参考[Facing枚举](../枚举值/Facing.md) |
    | fullName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | playerId | str | 试图破坏方块的玩家ID |
    | dimensionId | int | 维度id |
    | cancel | bool | 默认为False，在脚本层设置为True就能取消该方块的破坏 |
    | spawnResources | bool | 是否生成掉落物，默认为True，在脚本层设置为False就能取消生成掉落物 |

- 返回值

    无

- 备注
    - 若需要禁止某些特殊方块的破坏，需要配合PlayerTryDestroyBlockClientEvent一起使用，例如床，旗帜，箱子这些根据方块实体数据进行渲染的方块

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ShearsDestoryBlockBeforeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在客户端线程触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | dropName | str | 触发剪刀效果的掉落物identifier，包含命名空间及名称 |
    | dropCount | int | 触发剪刀效果的掉落物数量 |
    | playerId | str | 触发剪刀效果的玩家id |
    | dimensionId | int | 玩家触发时的维度id |
    | cancelShears | bool | 是否取消剪刀效果 |

- 返回值

    无

- 备注
    - 目前仅绊线会触发，需要取消剪刀效果得配合ShearsDestoryBlockBeforeServerEvent同时使用

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ShearsDestoryBlockBeforeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家手持剪刀破坏方块时，有剪刀特殊效果的方块会在服务端线程触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | dropName | str | 触发剪刀效果的掉落物identifier，包含命名空间及名称 |
    | dropCount | int | 触发剪刀效果的掉落物数量 |
    | playerId | str | 触发剪刀效果的玩家id |
    | dimensionId | int | 玩家触发时的维度id |
    | cancelShears | bool | 是否取消剪刀效果 |

- 返回值

    无

- 备注
    - 该事件触发在ServerPlayerTryDestroyBlockEvent之后，如果在ServerPlayerTryDestroyBlockEvent事件中设置了取消Destory或取消掉落物会导致该事件不触发
    - 取消剪刀效果后不掉落任何东西的方块类型：蜘蛛网、枯萎的灌木、草丛、下界苗、树叶、海草、藤蔓
    - 绊线取消剪刀效果需要配合ShearsDestoryBlockBeforeClientEvent同时使用，否则在表现上可能展现出来的还是剪刀剪断后的效果。绊线取消剪刀效果后依然会掉落成线。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StartDestroyBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家开始挖方块时触发。创造模式下不触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块的坐标 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块的附加值 |
    | playerId | str | 玩家id |
    | cancel | bool | 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockServerEvent一起修改。 |

- 返回值

    无

- 备注
    - 如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireClientEvent使用

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StartDestroyBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家开始挖方块时触发。创造模式下不触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块的坐标 |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxValue | int | 方块的附加值 |
    | playerId | str | 玩家id |
    | dimensionId | int | 维度id |
    | cancel | bool | 修改为True时，可阻止玩家进入挖方块的状态。需要与StartDestroyBlockClientEvent一起修改。 |

- 返回值

    无

- 备注
    - 如果是隔着火焰挖方块，即使将该事件cancel掉，火焰也会被扑灭。如果要阻止火焰扑灭，需要配合ExtinguishFireServerEvent使用

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StepOffBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：实体移动离开一个实心方块时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockX | int | 方块x坐标 |
    | blockY | int | 方块y坐标 |
    | blockZ | int | 方块z坐标 |
    | entityId | str | 触发的entity的唯一ID |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>），
        原版方块需要先通过RegisterOnStepOff接口注册才能触发
    - 压力板与绊线钩这种非实心方块不会触发

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStepOff"></span>
### RegisterOnStepOff

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态注册与修改netease:on_step_off组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_step_off组件
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnStepOff接口

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStepOff("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStepOff"></span>
### UnRegisterOnStepOff

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态删除netease:on_step_off组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_step_off组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStepOff("minecraft:redstone_ore")
```



## StepOffBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体移动离开一个实心方块时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockX | int | 方块x坐标 |
    | blockY | int | 方块y坐标 |
    | blockZ | int | 方块z坐标 |
    | entityId | str | 触发的entity的唯一ID |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>），
        原版方块需要先通过RegisterOnStepOff接口注册才能触发
    - 压力板与绊线钩这种非实心方块不会触发

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStepOff"></span>
### RegisterOnStepOff

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态注册与修改netease:on_step_off组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_step_off组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件
    - 可以多次调用修改原组件的值，删除组件请使用UnRegisterOnStepOff接口

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStepOff("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStepOff"></span>
### UnRegisterOnStepOff

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态删除netease:on_step_off组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_step_off组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStepOff("minecraft:redstone_ore")
```



## StepOnBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：实体刚移动至一个新实心方块时触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续原版逻辑 |
    | blockX | int | 方块x坐标 |
    | blockY | int | 方块y坐标 |
    | blockZ | int | 方块z坐标 |
    | entityId | str | 触发的entity的唯一ID |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 在合并微软更新之后，本事件触发时机与微软molang实验性玩法组件"minecraft:on_step_on"一致
    - 压力板与绊线钩在过去的版本的事件是可以触发的，但在更新后这种非实心方块并不会触发，有需要的可以使用OnEntityInsideBlockClientEvent事件。
    - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>），
        原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
    - 如果需要修改cancel，强烈建议配合服务端事件同步修改，避免出现被服务端矫正等非预期现象。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStepOn"></span>
### RegisterOnStepOn

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态注册与修改netease:on_step_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_step_on组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStepOn("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStepOn"></span>
### UnRegisterOnStepOn

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    可以动态删除netease:on_step_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_step_on组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStepOn("minecraft:redstone_ore")
```



## StepOnBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体刚移动至一个新实心方块时触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否允许触发，默认为False，若设为True，可阻止触发后续物理交互事件 |
    | blockX | int | 方块x坐标 |
    | blockY | int | 方块y坐标 |
    | blockZ | int | 方块z坐标 |
    | entityId | str | 触发的entity的唯一ID |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 在合并微软更新之后，本事件触发时机与微软molang实验性玩法组件"minecraft:on_step_on"一致
    - 压力板与绊线钩在过去的版本的事件是可以触发的，但在更新后这种非实心方块并不会触发，有需要的可以使用OnEntityInsideBlockServerEvent事件。
    - 不是所有方块都会触发该事件，自定义方块需要在json中先配置触发开关（详情参考：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html">自定义方块JSON组件</a>），
        原版方块需要先通过RegisterOnStepOn接口注册才能触发。原版的红石矿默认注册了，但深层红石矿没有默认注册。
    - 如果需要修改cancel，强烈建议配合客户端事件同步修改，避免出现客户端表现不一致等非预期现象。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="RegisterOnStepOn"></span>
### RegisterOnStepOn

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态注册与修改netease:on_step_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |
    | sendPythonEvent | bool | 是否发送python事件，为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否注册成功 |

- 备注
    - 目前仅能动态添加与修改原版方块的netease:on_step_on组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.RegisterOnStepOn("minecraft:redstone_ore", True)
```



<span id="UnRegisterOnStepOn"></span>
### UnRegisterOnStepOn

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    可以动态删除netease:on_step_on组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，包含命名空间，如minecraft:grass |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 备注
    - 目前仅能动态删除原版方块的netease:on_step_on组件
    - （非租赁服联机）使用服务端接口注册会影响到房主客户端组件

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.UnRegisterOnStepOn("minecraft:redstone_ore")
```

## 模型

# 模型

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AttackAnimBeginClientEvent](模型.md#attackanimbeginclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 攻击动作开始时触发 |
| [AttackAnimBeginServerEvent](模型.md#attackanimbeginserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当攻击动作开始时触发 |
| [AttackAnimEndClientEvent](模型.md#attackanimendclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 攻击动作结束时触发 |
| [AttackAnimEndServerEvent](模型.md#attackanimendserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当攻击动作结束时触发 |
| [JumpAnimBeginServerEvent](模型.md#jumpanimbeginserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当跳跃动作开始时触发 |
| [WalkAnimBeginClientEvent](模型.md#walkanimbeginclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 走路动作开始时触发 |
| [WalkAnimBeginServerEvent](模型.md#walkanimbeginserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当走路动作开始时触发 |
| [WalkAnimEndClientEvent](模型.md#walkanimendclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 走路动作结束时触发 |
| [WalkAnimEndServerEvent](模型.md#walkanimendserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 当走路动作结束时触发 |
# 模型

## AttackAnimBeginClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    攻击动作开始时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AttackAnimBeginServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当攻击动作开始时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AttackAnimEndClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    攻击动作结束时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AttackAnimEndServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当攻击动作结束时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## JumpAnimBeginServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当跳跃动作开始时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WalkAnimBeginClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    走路动作开始时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WalkAnimBeginServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当走路动作开始时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WalkAnimEndClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    走路动作结束时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## WalkAnimEndServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    当走路动作结束时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 实体id |

- 返回值

    无

- 备注
    - 使用SetModel替换骨骼模型后，该事件才生效

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>

## 物品

# 物品

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [ActorAcquiredItemClientEvent](物品.md#actoracquireditemclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家获得物品时客户端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。） |
| [ActorAcquiredItemServerEvent](物品.md#actoracquireditemserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家获得物品时服务端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。） |
| [ActorUseItemClientEvent](物品.md#actoruseitemclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家使用物品时客户端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲） |
| [ActorUseItemServerEvent](物品.md#actoruseitemserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家使用物品生效之前服务端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲） |
| [AnvilCreateResultItemAfterClientEvent](物品.md#anvilcreateresultitemafterclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击铁砧合成得到的物品时抛出的事件。 |
| [ClientItemTryUseEvent](物品.md#clientitemtryuseevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击右键尝试使用物品时客户端抛出的事件，可以通过设置cancel为True取消使用物品。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。 |
| [ClientItemUseOnEvent](物品.md#clientitemuseonevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家在对方块使用物品时客户端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。 |
| [ClientShapedRecipeTriggeredEvent](物品.md#clientshapedrecipetriggeredevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家合成物品时触发 |
| [ContainerItemChangedServerEvent](物品.md#containeritemchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 容器物品变化事件 |
| [CraftItemOutputChangeServerEvent](物品.md#craftitemoutputchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家从容器拿出生成物品时触发 |
| [FurnaceBurnFinishedServerEvent](物品.md#furnaceburnfinishedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 服务端熔炉烧制触发事件。熔炉, 高炉，烟熏炉烧出物品时触发 |
| [GrindStoneRemovedEnchantClientEvent](物品.md#grindstoneremovedenchantclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家点击砂轮合成得到的物品时抛出的事件 |
| [InventoryItemChangedClientEvent](物品.md#inventoryitemchangedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家背包物品变化时客户端抛出的事件。 |
| [InventoryItemChangedServerEvent](物品.md#inventoryitemchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家背包物品变化时服务端抛出的事件。 |
| [ItemReleaseUsingClientEvent](物品.md#itemreleaseusingclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：释放正在使用的物品 |
| [ItemReleaseUsingServerEvent](物品.md#itemreleaseusingserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：释放正在使用的物品时 |
| [ItemUseAfterServerEvent](物品.md#itemuseafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家在使用物品之后服务端抛出的事件。 |
| [ItemUseOnAfterServerEvent](物品.md#itemuseonafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家在对方块使用物品之后服务端抛出的事件。 |
| [OnCarriedNewItemChangedClientEvent](物品.md#oncarriednewitemchangedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 手持物品发生变化时，触发该事件；数量改变不会通知 |
| [OnCarriedNewItemChangedServerEvent](物品.md#oncarriednewitemchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家切换主手物品时触发该事件 |
| [OnItemPutInEnchantingModelServerEvent](物品.md#onitemputinenchantingmodelserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家将可附魔物品放到附魔台上时 |
| [OnNewArmorExchangeServerEvent](物品.md#onnewarmorexchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家切换盔甲时触发该事件 |
| [OnOffhandItemChangedServerEvent](物品.md#onoffhanditemchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家切换副手物品时触发该事件 |
| [OnPlayerActiveShieldServerEvent](物品.md#onplayeractiveshieldserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家激活/取消激活盾牌触发的事件。包括玩家持盾进入潜行状态，以及在潜行状态切换盾牌（切换耐久度不同的相同盾牌不会触发） |
| [OnPlayerBlockedByShieldAfterServerEvent](物品.md#onplayerblockedbyshieldafterserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家使用盾牌抵挡伤害之后触发 |
| [OnPlayerBlockedByShieldBeforeServerEvent](物品.md#onplayerblockedbyshieldbeforeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家使用盾牌抵挡伤害之前触发 |
| [PlayerDropItemServerEvent](物品.md#playerdropitemserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家丢弃物品时触发 |
| [PlayerTryDropItemClientEvent](物品.md#playertrydropitemclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：玩家丢弃物品时触发 |
| [ServerItemTryUseEvent](物品.md#serveritemtryuseevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家点击右键尝试使用物品时服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。 |
| [ServerItemUseOnEvent](物品.md#serveritemuseonevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家在对方块使用物品之前服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。 |
| [ServerPlayerTryTouchEvent](物品.md#serverplayertrytouchevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家即将捡起物品时触发 |
| [ShearsUseToBlockBeforeServerEvent](物品.md#shearsusetoblockbeforeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：实体手持剪刀对方块使用时，有剪刀特殊效果的方块会在服务端线程触发该事件 |
| [StartUsingItemClientEvent](物品.md#startusingitemclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出 |
| [StopUsingItemClientEvent](物品.md#stopusingitemclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家停止使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出 |
| [UIContainerItemChangedServerEvent](物品.md#uicontaineritemchangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 合成容器物品发生变化时触发 |
# 物品

## ActorAcquiredItemClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家获得物品时客户端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actor | str | 获得物品玩家实体id |
    | secondaryActor | str | 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串 |
    | itemDict | dict | 获取到的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | acquireMethod | int | 获得物品的方法，详见[ItemAcquisitionMethod](../枚举值/ItemAcquisitionMethod.md) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ActorAcquiredItemServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家获得物品时服务端抛出的事件（有些获取物品方式只会触发客户端事件，有些获取物品方式只会触发服务端事件，在使用时注意一点。）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actor | str | 获得物品玩家实体id |
    | secondaryActor | str | 物品给予者玩家实体id，如果不存在给予者的话，这里为空字符串 |
    | itemDict | dict | 获得的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | acquireMethod | int | 获得物品的方法，详见[ItemAcquisitionMethod枚举](../枚举值/ItemAcquisitionMethod.md) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ActorUseItemClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家使用物品时客户端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | useMethod | int | 使用物品的方法，详见[ItemUseMethodEnum枚举](../枚举值/ItemUseMethodEnum.md) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ActorUseItemServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家使用物品生效之前服务端抛出的事件（比较特殊不走该事件的例子：1）喝牛奶；2）染料对有水的炼药锅使用；3）盔甲架装备盔甲）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | useMethod | int | 使用物品的方法，详见[ItemUseMethodEnum枚举](../枚举值/ItemUseMethodEnum.md) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AnvilCreateResultItemAfterClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击铁砧合成得到的物品时抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemShowName | str | 合成后的物品显示名称 |
    | itemDict | dict | 合成后的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | oldItemDict | dict | 合成前的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（铁砧内第一个物品） |
    | materialItemDict | dict | 合成所使用材料的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（铁砧内第二个物品） |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ClientItemTryUseEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击右键尝试使用物品时客户端抛出的事件，可以通过设置cancel为True取消使用物品。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | cancel | bool | 取消使用物品 |

- 返回值

    无

- 备注
    - ServerItemTryUseEvent/ClientItemTryUseEvent不能取消对方块使用物品的行为，如使用生物蛋，使用桶倒出/收集，使用打火石点燃草等；如果想要取消这种行为，请使用ClientItemUseOnEvent和ServerItemUseOnEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ClientItemUseOnEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家在对方块使用物品时客户端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | x | int | 方块 x 坐标值 |
    | y | int | 方块 y 坐标值 |
    | z | int | 方块 z 坐标值 |
    | blockName | str | 方块的identifier |
    | blockAuxValue | int | 方块的附加值 |
    | face | int | 点击方块的面，参考[Facing枚举](../枚举值/Facing.md) |
    | clickX | float | 点击点的x比例位置 |
    | clickY | float | 点击点的y比例位置 |
    | clickZ | float | 点击点的z比例位置 |
    | ret | bool | 设为True可取消物品的使用 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ClientShapedRecipeTriggeredEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家合成物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recipeId | str | 配方id，对应配方json文件中的identifier字段 |

- 返回值

    无



## ContainerItemChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    容器物品变化事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int)/None | 容器坐标 |
    | containerType | int | 容器类型，类型含义见：[容器类型枚举](../枚举值/ContainerType.md) |
    | slot | int | 容器槽位 |
    | dimensionId | int | 维度id |
    | oldItemDict | dict | 旧物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | newItemDict | dict | 新物品物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

- 备注
    - 储物容器(箱子，潜影箱)，熔炉，酿造台，发射器，投掷器，漏斗，炼药锅，唱片机，高炉，烟熏炉中物品发生变化会触发此事件
    - 工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台为合成容器，不会触发此事件，此类容器可通过UIContainerItemChangedServerEvent监听具体生成容器物品变化
    - 炼药锅只在使用染料时触发本事件，且slot为2
    - 唱片机只在从漏斗放入唱片触发此事件

- 示例

```python
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
# 监听引擎的事件
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "ContainerItemChangedServerEvent",
                    self, self.OnContainerItemChangedServerEvent)

def OnContainerItemChangedServerEvent(self, args):
    playerId = args['playerId']
    logger.info("OnContainerItemChangedServerEvent args:%s", args)
    if args['containerType'] == serverApi.GetMinecraftEnum().ContainerType.SMOKER:
        print '烟熏炉发生变化'
```



## CraftItemOutputChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家从容器拿出生成物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemDict | dict | 生成的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | screenContainerType | int | 当前界面类型,类型含义见：[容器类型枚举](../枚举值/ContainerType.md) |
    | cancel | bool | 是否取消生成物品 |

- 返回值

    无

- 备注
    - 支持工作台，铁砧，砂轮等工作方块
    - screenContainerType = serverApi.GetMinecraftEnum().ContainerType.INVENTORY时，表示从创造模式物品栏中拿出物品，或者从合成栏中拿出合成物品
    - 通过cancel参数取消生成物品，可用于禁止外挂刷物品
    - cancel=True时无法从创造模式物品栏拿物品
    - cancel=True时铁砧无法修复或重命名物品，但仍会扣除经验值

- 示例

```python
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
# 监听引擎的事件
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "CraftItemOutputChangeServerEvent",
                    self, self.OnCraftItemOutputChangeServerEvent)

def OnCraftItemOutputChangeServerEvent(self, args):
    playerId = args['playerId']
    comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
    logger.info("OnCraftItemOutputChangeServerEvent args:%s", args)

    # 铁砧触发
    if args['screenContainerType'] == serverApi.GetMinecraftEnum().ContainerType.ANVIL:
        anvilInputItem = comp.GetOpenContainerItem(playerId,serverApi.GetMinecraftEnum().OpenContainerId.AnvilInputContainer,True)
        if anvilInputItem != None:
            # 铁砧输入位有物品，该事件为拿出铁砧生成物触发的
            if anvilInputItem['itenName'] != args['itemDict']['itemName']:
                # 输入物品和生成物品不是同一类型，可能是作弊，取消物品生成
                args['cancel'] = True

```

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## FurnaceBurnFinishedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    服务端熔炉烧制触发事件。熔炉, 高炉，烟熏炉烧出物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度id |
    | posX | float | 位置x |
    | posY | float | 位置y |
    | posZ | float | 位置z |
    | itemDict | dict | 物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None |

- 返回值

    无



## GrindStoneRemovedEnchantClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家点击砂轮合成得到的物品时抛出的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | oldItemDict | dict | 合成前的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（砂轮内第一个物品） |
    | additionalItemDict | dict | 作为合成材料的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>（砂轮内第二个物品） |
    | newItemDict | dict | 合成后的物品<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | exp | int | 本次合成返还的经验 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## InventoryItemChangedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家背包物品变化时客户端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | slot | int | 背包槽位 |
    | oldItemDict | dict | 变化前槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | newItemDict | dict | 变化后槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

- 备注
    - 如果槽位变空，变化后槽位中物品为空气
    - 触发时槽位物品仍为变化前物品
    - 背包内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## InventoryItemChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家背包物品变化时服务端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | slot | int | 背包槽位 |
    | oldItemDict | dict | 变化前槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | newItemDict | dict | 变化后槽位中的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

- 备注
    - 如果槽位变空，变化后槽位中物品为空气
    - 触发时槽位物品仍为变化前物品
    - 玩家进入游戏时，身上的物品会触发该事件
    - 背包内物品移动，合堆，分堆的操作会分多次事件触发并且顺序不定，编写逻辑时请勿依赖事件触发顺序

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ItemReleaseUsingClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：释放正在使用的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | durationLeft | float | 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数) |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | maxUseDuration | int | 最大蓄力时长 |
    | cancel | bool | 设置为True可以取消，需要同时取消服务端事件[ItemReleaseUsingServerEvent](#itemreleaseusingserverevent) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ItemReleaseUsingServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：释放正在使用的物品时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | durationLeft | float | 蓄力剩余时间(当物品缺少"minecraft:maxduration"组件时,蓄力剩余时间为负数) |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | maxUseDuration | int | 最大蓄力时长 |
    | cancel | bool | 设置为True可以取消，需要同时取消客户端事件[ItemReleaseUsingClientEvent](#itemreleaseusingclientevent) |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ItemUseAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家在使用物品之后服务端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

- 备注
    - 做出使用物品这个动作之后触发，一些需要蓄力的物品使用事件(ActorUseItemServerEvent)会在之后触发。如投掷三叉戟，先触发本事件，投出去之后再触发ActorUseItemServerEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ItemUseOnAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家在对方块使用物品之后服务端抛出的事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | x | int | 方块 x 坐标值 |
    | y | int | 方块 y 坐标值 |
    | z | int | 方块 z 坐标值 |
    | face | int | 点击方块的面，参考[Facing枚举](../枚举值/Facing.md) |
    | clickX | float | 点击点的x比例位置 |
    | clickY | float | 点击点的y比例位置 |
    | clickZ | float | 点击点的z比例位置 |
    | blockName | str | 方块的identifier |
    | blockAuxValue | int | 方块的附加值 |
    | dimensionId | int | 维度id |

- 返回值

    无

- 备注
    - 在ServerItemUseOnEvent和原版物品使用事件之后触发

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnCarriedNewItemChangedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    手持物品发生变化时，触发该事件；数量改变不会通知

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | 切换后物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无



## OnCarriedNewItemChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家切换主手物品时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldItemDict | dict/None | 旧物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None |
    | newItemDict | dict/None | 新物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None |
    | playerId | str | 玩家 entityId |

- 返回值

    无

- 备注
    - 切换耐久度不同的相同物品，不会触发该事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnItemPutInEnchantingModelServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家将可附魔物品放到附魔台上时

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id，参数类型为str |
    | slotType | int | 玩家放入物品的EnchantSlotType |
    | options | list | 附魔台选项 |
    | change | bool | 传入True时，附魔台选项会被新传入的options覆盖 |

- 返回值

    无

- 备注
    - options为包含三个dict的list，单个dict的格式形如{'cost': 1, 'enchantData': [(1,1)], 'modEnchantData': [('custom_enchant, 1')]}，cost为解锁该选项所需的玩家等级，enchantData为该附魔选项包含的原版附魔数据，modEnchantData为该选项包含的自定义附魔数据

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnNewArmorExchangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家切换盔甲时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slot | int | 槽位id |
    | oldArmorDict | dict/None | 旧装备的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None |
    | newArmorDict | dict/None | 新装备的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None |
    | playerId | str | 玩家 entityId |

- 返回值

    无

- 备注
    - 当玩家登录时，每个盔甲槽位会触发两次该事件，第一次为None切换到身上的装备，第二次的old和new都为身上装备。如果槽位为空，则是触发两次从None切换到None的事件。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnOffhandItemChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家切换副手物品时触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | oldItemDict | dict/None | 旧物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当旧物品为空时，此项属性为None |
    | newItemDict | dict/None | 新物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，当新物品为空时，此项属性为None |
    | playerId | str | 玩家 entityId |

- 返回值

    无

- 备注
    - 当原有的物品槽内容为空时，`oldItemName`值为'minecraft:air'，且`oldItem`其余字段不存在<br>当切换原有物品，且新物品为空时，参数值同理

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnPlayerActiveShieldServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家激活/取消激活盾牌触发的事件。包括玩家持盾进入潜行状态，以及在潜行状态切换盾牌（切换耐久度不同的相同盾牌不会触发）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | isActive | bool | True:尝试激活,False:尝试取消激活 |
    | itemDict | dict | 盾牌物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | cancelable | bool | 是否可以取消。如果玩家在潜行状态切换盾牌，则无法取消 |
    | cancel | bool | 是否取消这次激活 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnPlayerBlockedByShieldAfterServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家使用盾牌抵挡伤害之后触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | sourceId | str | 伤害来源实体Id，没有实体返回"-1" |
    | itemDict | dict | 盾牌物品字典<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | damage | float | 抵挡的伤害数值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnPlayerBlockedByShieldBeforeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家使用盾牌抵挡伤害之前触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | sourceId | str | 伤害来源实体Id，没有实体返回"-1" |
    | itemDict | dict | 盾牌物品字典<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | damage | float | 抵挡的伤害数值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerDropItemServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家丢弃物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | itemEntityId | str | 物品entityId |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerTryDropItemClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：玩家丢弃物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | itemDict | dict | 物品dict |
    | cancel | bool | 是否取消此次操作 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerItemTryUseEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家点击右键尝试使用物品时服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemTryUseEvent和ServerItemTryUseEvent中将cancel设置为True才能正确取消。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | cancel | bool | 设为True可取消物品的使用 |

- 返回值

    无

- 备注
    - ServerItemTryUseEvent/ClientItemTryUseEvent不能取消对方块使用物品的行为，如使用生物蛋，使用桶倒出/收集，使用打火石点燃草等；如果想要取消这种行为，请使用ClientItemUseOnEvent和ServerItemUseOnEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerItemUseOnEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家在对方块使用物品之前服务端抛出的事件。注：如果需要取消物品的使用需要同时在ClientItemUseOnEvent和ServerItemUseOnEvent中将ret设置为True才能正确取消。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | x | int | 方块 x 坐标值 |
    | y | int | 方块 y 坐标值 |
    | z | int | 方块 z 坐标值 |
    | blockName | str | 方块的identifier |
    | blockAuxValue | int | 方块的附加值 |
    | face | int | 点击方块的面，参考[Facing枚举](../枚举值/Facing.md) |
    | dimensionId | int | 维度id |
    | clickX | float | 点击点的x比例位置 |
    | clickY | float | 点击点的y比例位置 |
    | clickZ | float | 点击点的z比例位置 |
    | ret | bool | 设为True可取消物品的使用 |

- 返回值

    无

- 备注
    - 当对原生方块进行使用时，如堆肥桶等类似有 使用 功能的方块使用物品时，不会触发该事件。而当原生方块加入监听后，ServerBlockUseEvent会触发。当需要获取触发时使用的物品时，可以通过item组件获取手中持有的物品，对应的客户端事件同理。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerPlayerTryTouchEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家即将捡起物品时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | entityId | str | 物品实体的Id |
    | itemDict | dict | 触碰的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | cancel | bool | 设置为True时将取消本次拾取 |
    | pickupDelay | int | 取消拾取后重新设置该物品的拾取cd，小于15帧将视作15帧，大于等于97813帧将视作无法拾取 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ShearsUseToBlockBeforeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：实体手持剪刀对方块使用时，有剪刀特殊效果的方块会在服务端线程触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockX | int | 方块位置x |
    | blockY | int | 方块位置y |
    | blockZ | int | 方块位置z |
    | blockName | str | 方块的identifier，包含命名空间及名称 |
    | auxData | int | 方块附加值 |
    | dropName | str | 触发剪刀效果的掉落物identifier，包含命名空间及名称 |
    | dropCount | int | 触发剪刀效果的掉落物数量 |
    | entityId | str | 触发剪刀效果的实体id，目前仅玩家会触发 |
    | dimensionId | int | 玩家触发时的维度id |
    | cancelShears | bool | 是否取消剪刀效果 |

- 返回值

    无

- 备注
    - 目前会触发该事件的方块：南瓜、蜂巢
    - 该事件触发在ServerItemUseOnEvent之后，如果ServerItemUseOnEvent中取消了物品使用，该事件无法被触发
    - 和ServerItemUseOnEvent一样该事件判定在tick执行，意味着如果取消剪刀效果该事件可能会多次触发（取决于玩家按下使用键时长）

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StartUsingItemClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StopUsingItemClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家停止使用物品（目前仅支持Bucket、Trident、RangedWeapon、Medicine、Food、Potion、Crossbow、ChemistryStick）时抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | itemDict | dict | 使用的物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## UIContainerItemChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    合成容器物品发生变化时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | slot | int | 容器槽位，含义见：[容器类型枚举](../枚举值/PlayerUISlot.md) |
    | oldItemDict | dict | 旧物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | newItemDict | dict | 生成的物品，格式参考<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    无

- 备注
    - 合成容器包括工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台，输入物品发生变化时会触发本事件
    - 可通过容器槽位区分不同的生成容器类型
    - 合成容器的生成槽位生成物品时不触发本事件，生成物品可通过CraftItemOutputChangeServerEvent监听
    - 储物容器(箱子，潜影箱)，熔炉，酿造台，发射器，投掷器，漏斗，炼药锅，唱片机，高炉，烟熏炉中物品发生变化不会触发此事件，此类容器可通过ContainerItemChangedServerEvent监听

- 示例

```python
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
# 监听引擎的事件
self.ListenForEvent(serverApi.GetEngineNamespace(),
                    serverApi.GetEngineSystemName(),
                    "UIContainerItemChangedServerEvent",
                    self, self.OnUIContainerItemChangedServerEvent)

def OnUIContainerItemChangedServerEvent(self, args):
    playerId = args['playerId']
    logger.info("OnUIContainerItemChangedServerEvent args:%s", args)
    if args['slot'] == serverApi.GetMinecraftEnum().PlayerUISlot.GrindstoneInput:
        print '砂轮输入位发生变化'
```

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>

## 玩家

# 玩家

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [AddExpEvent](玩家.md#addexpevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家增加经验时触发该事件。 |
| [AddLevelEvent](玩家.md#addlevelevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家升级时触发该事件。 |
| [ChangeLevelUpCostServerEvent](玩家.md#changelevelupcostserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次 |
| [DimensionChangeClientEvent](玩家.md#dimensionchangeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家维度改变时客户端抛出 |
| [DimensionChangeFinishClientEvent](玩家.md#dimensionchangefinishclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家维度改变完成后客户端抛出 |
| [DimensionChangeFinishServerEvent](玩家.md#dimensionchangefinishserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家维度改变完成后服务端抛出 |
| [DimensionChangeServerEvent](玩家.md#dimensionchangeserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家维度改变时服务端抛出 |
| [ExtinguishFireClientEvent](玩家.md#extinguishfireclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。 |
| [ExtinguishFireServerEvent](玩家.md#extinguishfireserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。 |
| [GameTypeChangedClientEvent](玩家.md#gametypechangedclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 个人游戏模式发生变化时客户端触发。 |
| [GameTypeChangedServerEvent](玩家.md#gametypechangedserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 个人游戏模式发生变化时服务端触发。 |
| [OnPlayerHitBlockClientEvent](玩家.md#onplayerhitblockclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。玩家着地时会触发OnGroundClientEvent，而不是该事件。客户端和服务端分别作碰撞检测，可能两个事件返回的结果略有差异。 |
| [OnPlayerHitBlockServerEvent](玩家.md#onplayerhitblockserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。监听玩家着地请使用客户端的OnGroundClientEvent。客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。 |
| [PerspChangeClientEvent](玩家.md#perspchangeclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 视角切换时会触发的事件 |
| [PlayerAttackEntityEvent](玩家.md#playerattackentityevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家攻击时触发该事件。 |
| [PlayerCheatSpinAttackServerEvent](玩家.md#playercheatspinattackserverevent) | <span style="display:inline;color:#ff5555">Apollo</span> | 触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备激流附魔的三叉戟、在水中或雨中，且未骑乘） |
| [PlayerDieEvent](玩家.md#playerdieevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家死亡时触发该事件。 |
| [PlayerDoInteractServerEvent](玩家.md#playerdointeractserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕 |
| [PlayerEatFoodServerEvent](玩家.md#playereatfoodserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家吃下食物时触发 |
| [PlayerHurtEvent](玩家.md#playerhurtevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家受伤害前触发该事件。 |
| [PlayerInteractServerEvent](玩家.md#playerinteractserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见[PlayerDoInteractServerEvent](#playerdointeractserverevent) |
| [PlayerRespawnEvent](玩家.md#playerrespawnevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家复活时触发该事件。 |
| [PlayerRespawnFinishServerEvent](玩家.md#playerrespawnfinishserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家复活完毕时触发 |
| [PlayerSleepServerEvent](玩家.md#playersleepserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家使用床睡觉成功 |
| [PlayerSpinAttackServerEvent](玩家.md#playerspinattackserverevent) | <span style="display:inline;color:#ff5555">Apollo</span> | 触发时机：玩家开始/结束快速旋转攻击时触发 |
| [PlayerStopSleepServerEvent](玩家.md#playerstopsleepserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家停止睡觉 |
| [PlayerTeleportEvent](玩家.md#playerteleportevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。 |
| [PlayerTrySleepServerEvent](玩家.md#playertrysleepserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家尝试使用床睡觉 |
| [ServerPlayerGetExperienceOrbEvent](玩家.md#serverplayergetexperienceorbevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机：玩家获取经验球时触发的事件 |
| [StoreBuySuccServerEvent](玩家.md#storebuysuccserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 触发时机:玩家游戏内购买商品时服务端抛出的事件 |
# 玩家

## AddExpEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家增加经验时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |
    | addExp | int | 增加的经验值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## AddLevelEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家升级时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |
    | addLevel | int | 增加的等级值 |
    | newLevel | int | 新的等级 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ChangeLevelUpCostServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：获取玩家下一个等级升级经验时，用于重载玩家的升级经验，每个等级在重置之前都只会触发一次

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | int | 玩家当前等级 |
    | levelUpCostExp | int | 当前等级升级到下个等级需要的经验值，当设置升级经验小于1时会被强制调整到1 |
    | changed | bool | 设置为True，重载玩家升级经验才会生效 |

- 返回值

    无



### 相关接口

<span id="ClearDefinedLevelUpCost"></span>
### ClearDefinedLevelUpCost

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    接口用于重置升级经验。使用ChangeLevelUpCostServerEvent事件设置升级经验后，升级经验无法调整。需要调整升级经验时，可使用该接口。使用步骤如下：1、使用ClearDefineLevelUpconst，2、在升级抛出ChangeLevelUpCostServerEvent事件后重新设置经验。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | int | 指定清理的等级，加入传入的数值小于0，则清理所有等级的升级经验值缓存 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清理成功。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
suc = comp.ClearDefinedLevelUpCost(1)
```



## DimensionChangeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家维度改变时客户端抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | fromDimensionId | int | 维度改变前的维度 |
    | toDimensionId | int | 维度改变后的维度 |
    | fromX | float | 改变前的位置x |
    | fromY | float | 改变前的位置Y |
    | fromZ | float | 改变前的位置Z |
    | toX | float | 改变后的位置x |
    | toY | float | 改变后的位置Y |
    | toZ | float | 改变后的位置Z |

- 返回值

    无

- 备注
    - 当通过传送门从末地回到主世界时，toY值为32767，其他情况一般会比设置值高1.62

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DimensionChangeFinishClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家维度改变完成后客户端抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | fromDimensionId | int | 维度改变前的维度 |
    | toDimensionId | int | 维度改变后的维度 |
    | toPos | tuple(float,float,float) |  改变后的位置x,y,z,其中y值为脚底加上角色的身高值 |

- 返回值

    无

- 备注
    - 当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DimensionChangeFinishServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家维度改变完成后服务端抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | fromDimensionId | int | 维度改变前的维度 |
    | toDimensionId | int | 维度改变后的维度 |
    | toPos | tuple(float,float,float) |  改变后的位置x,y,z,其中y值为脚底加上角色的身高值 |

- 返回值

    无

- 备注
    - 当通过传送门从末地回到主世界时，toPos的y值为32767，其他情况一般会比设置值高1.62

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## DimensionChangeServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家维度改变时服务端抛出

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家实体id |
    | fromDimensionId | int | 维度改变前的维度 |
    | toDimensionId | int | 维度改变后的维度 |
    | fromX | float | 改变前的位置x |
    | fromY | float | 改变前的位置Y |
    | fromZ | float | 改变前的位置Z |
    | toX | float | 改变后的位置x |
    | toY | float | 改变后的位置Y |
    | toZ | float | 改变后的位置Z |

- 返回值

    无

- 备注
    - 当通过传送门从末地回到主世界时，toY值为32767，其他情况一般会比设置值高1.62

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ExtinguishFireClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 火焰方块的坐标 |
    | playerId | str | 玩家id |
    | cancel | bool | 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireServerEvent一起修改。 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ExtinguishFireServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家扑灭火焰时触发。下雨，倒水等方式熄灭火焰不会触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 火焰方块的坐标 |
    | playerId | str | 玩家id |
    | cancel | bool | 修改为True时，可阻止玩家扑灭火焰。需要与ExtinguishFireClientEvent一起修改。 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## GameTypeChangedClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    个人游戏模式发生变化时客户端触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | oldGameType | int | 切换前的游戏模式 |
    | newGameType | int | 切换后的游戏模式 |

- 返回值

    无

- 备注
    - 游戏模式：GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别为0~2
        默认游戏模式发生变化时最后反映在个人游戏模式之上。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## GameTypeChangedServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    个人游戏模式发生变化时服务端触发。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id，[SetDefaultGameType](../接口/世界/游戏规则.md#SetDefaultGameType)接口改变游戏模式时该参数为空字符串 |
    | oldGameType | int | 切换前的游戏模式 |
    | newGameType | int | 切换后的游戏模式 |

- 返回值

    无

- 备注
    - 游戏模式：GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别为0~2
        默认游戏模式发生变化时最后反映在个人游戏模式之上。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## OnPlayerHitBlockClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。玩家着地时会触发OnGroundClientEvent，而不是该事件。客户端和服务端分别作碰撞检测，可能两个事件返回的结果略有差异。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 碰撞到方块的玩家Id |
    | posX | int | 碰撞方块x坐标 |
    | posY | int | 碰撞方块y坐标 |
    | posZ | int | 碰撞方块z坐标 |
    | blockId | str | 碰撞方块的identifier |
    | auxValue | int | 碰撞方块的附加值 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="OpenPlayerHitBlockDetection"></span>
### OpenPlayerHitBlockDetection

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    开启碰撞方块的检测，开启后碰撞时会触发OnPlayerHitBlockClientEvent事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | precision | float | 碰撞检测精度，参数需要在区间[0, 1) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.OpenPlayerHitBlockDetection(0.0001)
```



<span id="ClosePlayerHitBlockDetection"></span>
### ClosePlayerHitBlockDetection

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    关闭碰撞方块的检测，关闭后将不会触发OnPlayerHitBlockClientEvent事件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.ClosePlayerHitBlockDetection()
```



## OnPlayerHitBlockServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：通过OpenPlayerHitBlockDetection打开方块碰撞检测后，当玩家碰撞到方块时触发该事件。监听玩家着地请使用客户端的OnGroundClientEvent。客户端和服务端分别作碰撞检测，可能两个事件返回的略有差异。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 碰撞到方块的玩家Id |
    | posX | int | 碰撞方块x坐标 |
    | posY | int | 碰撞方块y坐标 |
    | posZ | int | 碰撞方块z坐标 |
    | blockId | str | 碰撞方块的identifier |
    | auxValue | int | 碰撞方块的附加值 |
    | dimensionId | int | 维度id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


### 相关接口

<span id="OpenPlayerHitBlockDetection"></span>
### OpenPlayerHitBlockDetection

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    开启碰撞方块的检测，开启后碰撞时会触发OnPlayerHitBlockServerEvent事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | precision | float | 碰撞检测精度，参数需要在区间[0, 1) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：该碰撞检测会屏蔽草、空气、火、高草四种方块

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.OpenPlayerHitBlockDetection(0.0001)
```



<span id="ClosePlayerHitBlockDetection"></span>
### ClosePlayerHitBlockDetection

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    关闭碰撞方块的检测，关闭后将不会触发OnPlayerHitBlockServerEvent事件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.ClosePlayerHitBlockDetection()
```



## PerspChangeClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    视角切换时会触发的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | from | int | 切换前的视角 |
    | to | int | 切换后的视角 |

- 返回值

    无

- 备注
    - 视角数字代表含义
        0: 第一人称
        1: 第三人称背面
        2: 第三人称正面



## PlayerAttackEntityEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家攻击时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | victimId | str | 受击者id |
    | damage | int | 伤害值：引擎传过来的值是0 允许脚本层修改为其他数 |
    | isValid | int | 脚本是否设置伤害值：1表示是；0 表示否 |
    | cancel | bool | 是否取消该次攻击，默认不取消 |
    | isKnockBack | bool | 是否支持击退效果，默认支持，当不支持时将屏蔽武器击退附魔效果 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerCheatSpinAttackServerEvent

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

- 描述

    触发时机：玩家开始/结束快速旋转攻击并且不符合发送快速旋转攻击条件时触发（装备激流附魔的三叉戟、在水中或雨中，且未骑乘）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家的entityId |
    | isStart | bool | True时代表开始快速旋转攻击；False时代表结束快速旋转攻击 |

- 返回值

    无

- 备注
    - 假如没有自定义类似三叉戟/激流附魔的物品，那么触发此事件说明此有很大可能此玩家使用了【杀戮光环】外挂

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerDieEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家死亡时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |
    | attacker | str | 伤害来源id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerDoInteractServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家与有minecraft:interact组件的生物交互时触发该事件，例如玩家手持空桶对牛挤奶、玩家手持打火石点燃苦力怕

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | itemDict | dict | 交互时使用物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | interactEntityId | str | 交互的生物entityId |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerEatFoodServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家吃下食物时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家Id |
    | itemDict | dict | 食物物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | hunger | int | 食物增加的饥饿值，可修改 |
    | nutrition | float | 食物的营养价值，回复饱和度 = 食物增加的饥饿值 * 食物的营养价值 * 2，饱和度最大不超过当前饥饿值，可修改 |

- 返回值

    无

- 备注
    - 吃蛋糕以及喝牛奶不触发该事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerHurtEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家受伤害前触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 受击玩家id |
    | attacker | str | 伤害来源实体id，若没有实体攻击，例如高空坠落，id为-1 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerInteractServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家可以与实体交互时。如果是鼠标控制模式，则当准心对着实体时触发。如果是触屏模式，则触发时机与屏幕下方的交互按钮显示的时机相同。玩家真正与实体发生交互的事件见[PlayerDoInteractServerEvent](#playerdointeractserverevent)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cancel | bool | 是否取消触发，默认为False，若设为True，可阻止触发后续的实体交互事件 |
    | playerId | str | 主动与实体互动的玩家的唯一ID |
    | itemDict | dict | 当前玩家手持物品的<a href="../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | victimId | str | 被动的实体的唯一ID |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerRespawnEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家复活时触发该事件。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |

- 返回值

    无

- 备注
    - 该事件为玩家点击重生按钮时触发，但是触发时玩家可能尚未完成复活，此时请勿对玩家进行切维度或设置生命值等操作
        一般情况下推荐使用PlayerRespawnFinishServerEvent

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerRespawnFinishServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家复活完毕时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

- 备注
    - 该事件触发时玩家已重生完毕，可以安全使用切维度等操作
    - 通过末地传送门回到主世界时也算重生，同样也会触发该事件

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerSleepServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家使用床睡觉成功

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerSpinAttackServerEvent

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

- 描述

    触发时机：玩家开始/结束快速旋转攻击时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家的entityId |
    | isInWaterOrRain | bool | 是否在水中或雨中 |
    | isRiding | bool | 是否骑乘状态 |
    | isStart | bool | True时代表开始快速旋转攻击；False时代表结束快速旋转攻击 |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerStopSleepServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家停止睡觉

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerTeleportEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：当玩家传送时触发该事件，如：玩家使用末影珍珠或tp指令时。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | id | str | 玩家id |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## PlayerTrySleepServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家尝试使用床睡觉

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | cancel | bool | 是否取消（开发者传入） |

- 返回值

    无

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## ServerPlayerGetExperienceOrbEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机：玩家获取经验球时触发的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | experienceValue | int | 经验球经验值 |
    | cancel | bool | 是否取消（开发者传入） |

- 返回值

    无

- 备注
    - `cancel`值设为True时，捡起的经验球不会增加经验值，但是经验球一样会消失。

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>


## StoreBuySuccServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    触发时机:玩家游戏内购买商品时服务端抛出的事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 购买商品的玩家实体id |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
self.ListenForEvent(serverApi.GetEngineNamespace(),serverApi.GetEngineSystemName(),
    "StoreBuySuccServerEvent",
    self, self.OnStoreBuySucc)
def OnStoreBuySucc(self, args):
    entityId = args['playerId']
    print 'Ship Item.EntityId:', playerId
```

在零件中直接声明一个同名函数，即可完成监听，详情参考<a href="../../../mcguide/20-玩法开发/14-预设玩法编程/2-深入理解零件/0-零件开发.html#零件事件">零件事件</a>

## 联机大厅

# 联机大厅

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [lobbyGoodBuySucServerEvent](联机大厅.md#lobbygoodbuysucserverevent) | <span style="display:inline;color:#ff5555">服务端</span> | 玩家登录联机大厅服务器，或者联机大厅游戏内购买商品时触发。如果是玩家登录，触发时玩家客户端已经触发了UiInitFinished事件 |
# 联机大厅

## lobbyGoodBuySucServerEvent

<span style="display:inline;color:#ff5555">服务端</span>

- 描述

    玩家登录联机大厅服务器，或者联机大厅游戏内购买商品时触发。如果是玩家登录，触发时玩家客户端已经触发了UiInitFinished事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eid | str | 购买商品的玩家实体id |
    | buyItem | bool | 玩家登录时为False，玩家购买了商品时为True |

- 返回值

    无

## 音效

# 音效

# 索引

| 事件 | <div style="width: 3em"></div> | 描述 |
| --- | --- | --- |
| [OnMusicStopClientEvent](音效.md#onmusicstopclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发该事件 |
| [PlayMusicClientEvent](音效.md#playmusicclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 播放背景音乐时触发 |
| [PlaySoundClientEvent](音效.md#playsoundclientevent) | <span style="display:inline;color:#7575f9">客户端</span> | 播放场景音效或UI音效时触发 |
# 音效

## OnMusicStopClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    音乐停止时，当玩家调用StopCustomMusic来停止自定义背景音乐时，会触发该事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | musicName | str | 音乐名称 |

- 返回值

    无



## PlayMusicClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    播放背景音乐时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 即资源包中sounds/music_definitions.json中的event_name，并且对应sounds/sound_definitions.json中的key |
    | cancel | bool | 设为True可屏蔽该次音效播放 |

- 返回值

    无



## PlaySoundClientEvent

<span style="display:inline;color:#7575f9">客户端</span>

- 描述

    播放场景音效或UI音效时触发

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 即资源包中sounds/sound_definitions.json中的key |
    | pos | tuple(float,float,float) | 音效播放的位置。UI音效为(0,0,0) |
    | volume | float | 音量，范围为0-1 |
    | pitch | float | 播放速度，正常速度为1 |
    | cancel | bool | 设为True可屏蔽该次音效播放 |

- 返回值

    无

