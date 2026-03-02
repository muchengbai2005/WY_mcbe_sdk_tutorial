# ModAPI 接口-玩家

## 目录

- [动画](#动画)
- [导航](#导航)
- [属性](#属性)
- [摄像机](#摄像机)
- [权限](#权限)
- [渲染](#渲染)
- [游戏模式](#游戏模式)
- [背包](#背包)
- [行为](#行为)

---

## 动画

# 动画

## PlayTpAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerAnimCompClient.PlayerAnimCompClient

- 描述

    第三人称视角播放玩家通用动作

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | anim | str | 动作名称，如sneaking |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 支持的动作包括：sneaking、sneaking_inverted、swim、sleeping、holding_left、holding_right、crossbow_hold、crossbow_equipped、bow_equipped、upside_down、tp_attack

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayerAnim(playerId)
comp.PlayTpAnimation("sneaking")
```



## StopAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerAnimCompClient.PlayerAnimCompClient

- 描述

    停止播放玩家通用动作

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | anim | str | 动作名称，如sneaking |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayerAnim(playerId)
comp.StopAnimation("sneaking")
```

## 导航

# 导航

## GetNavPath

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取本地玩家到目标点的寻路路径，开发者可以通过该接口定制自定义的导航系统。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 目标点的坐标 |
    | maxTrimNode | int | 对搜索路径进行平滑时的最大尝试格数。设置的太大会影响寻路性能。默认值16 |
    | maxIteration | int | A星寻路的最大迭代次数。默认值800 |
    | isSwimmer | bool | 目标点是否在水中。默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或list(tuple(float,float,float)) | 返回1：参数错误<br>返回2：玩家所在chunk未加载完毕<br>返回3：终点为实心方块，无法寻路<br>返回list(tuple(float,float,float),)：从起点到终点的坐标点列表。注意该list可能为空，表示本地玩家离地太远，或者被堵住无法行动。 |

- 备注
    - 寻路算法迭代一定次数后（即maxIteration的数值），如果未寻到目标点，接口会返回**局部最优解**，即当前搜索到的点的集合中，离设置目标点最近的点的路径，但是这条路径可能是不准确或错误的（例如往终点的方向是死胡同的情况）。<br>出现这种可能的情况包括：目标点无法抵达（被围住等），目标点所在chunk未加载，目标点较远（但是仍在区块加载范围内）或地形较复杂（例如与终点间有很长一面墙）。
    - 上述情况中，目标点较远或地形较复杂的情况可以通过增大maxIteration的数值避免，但是这样同时也会增加客户端的卡顿。
    - 如果终点在水里需要将isSwimmer参数设为True，但如果只是路途中会经过水域是不需要的。但需要注意在水中的寻路性能非常低下，其他参数不变时，单次寻路计算出的最大路径长度会小很多。



## StartNavTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    我们提供了一个基于GetNavPath的导航系统实现，做法是在路径上生成序列帧以引导玩家通向目标点，并且当玩家偏离路径会重新进行导航。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 目标点的坐标 |
    | sfxPath | str | 构成导航路径的序列帧素材路径。样式可以参考指向上的箭头 |
    | callback | function | 玩家抵达终点时会调用的**回调函数**。该函数需要接受一个bool参数。 |
    | sfxIntl | float | 相邻两个序列帧之间的间隔。默认值2 |
    | sfxMaxNum | int | 同时存在的序列帧的最大个数。默认值16 |
    | sfxScale | tuple(float,float) | 序列帧的宽度及高度的缩放。默认为（0.5，0.5） |
    | maxIteration | int | A星寻路的最大迭代次数。默认值800 |
    | isSwimmer | bool | 目标点是否在水中。默认为False |
    | fps | int | 序列帧帧率，默认为20，不建议超过30 |
    | playIntl | int | 一轮中相邻序列帧开始播放的间隔，默认为8帧，不得小于0，否则将使用默认值 |
    | duration | int | 单个序列帧持续播放帧数，默认为60帧，不小于10，否则将使用默认值 |
    | oneTurnDuration | int | 两轮序列帧之间的播放间隔(帧)，默认值为90帧，至少为duration的1.5倍，否则将以1.5 * duration进行计算 |
    | sfxDepthTest | bool | 序列帧是否开启深度检测，默认为False，设为True时序列帧会被场景遮挡 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回0：导航正常开始<br>返回-1：本地玩家离地太远，或者被堵住无法行动<br>返回1：参数错误<br>返回2：玩家所在chunk未加载完毕<br>返回3：终点为实心方块，无法寻路 |

- 备注
    - 寻路算法迭代一定次数后（即maxIteration的数值），如果未寻到目标点，接口会返回**局部最优解**，即当前搜索到的点的集合中，离设置目标点最近的点的路径，但是这条路径可能是不准确或错误的（例如往终点的方向是死胡同的情况）。<br>出现这种可能的情况包括：目标点无法抵达（被围住等），目标点所在chunk未加载，目标点较远（但是仍在区块加载范围内）或地形较复杂（例如与终点间有很长一面墙）。
    - 上述情况中，目标点较远或地形较复杂的情况可以通过增大maxIteration的数值避免，但是这样同时也会增加客户端的卡顿。
    - 如果终点在水里需要将isSwimmer参数设为True，但如果只是路途中会经过水域是不需要的。但需要注意在水中的寻路性能非常低下，其他参数不变时，单次寻路计算出的最大路径长度会小很多。
    - callback函数接受一个bool参数。当参数为True时，表示玩家到达目标点附近，但不代表导航结束，如果玩家又离开目标点，导航系统会再次尝试导航，开发者需要在某个时机手动调用停止导航（参考[StopNav接口](导航.md#StopNav)）。当参数为False时，表示玩家偏离航线并到了某个无法到达目标点的状态（即返回值不为0的那些情况），这种情况导航会自动终止。
        ```python
        # 一个到达终点时停止导航的callback函数示例
        from mod_log import logger as logger
        def myCallback(result):
            if result:
                extraClientApi.StopNav()
            else:
                logger.info('something happened in navigation')
        # 若目标点很远，需要进行分段导航的callback函数示例
        def myCallback2(result):
            if result:
                if GetDistence(localplayerPos, destinationPos) < sfxIntl*2:
                    extraClientApi.StopNav()
                else:
                    extraClientApi.StartNavTo(destinationPos, ...)
            else:
                logger.info('something happened in navigation')
        ```
    - 如果上一次导航没结束时再次调用会覆盖之前的导航
    - 使用默认参数的导航效果示例：<br>![avatar](../../picture/startNavTo.png)



## StopNav

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    终止当前的导航

- 参数

    无

- 返回值

    无

## 属性

# 属性

## AddPlayerExperience

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    增加玩家经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | exp | int | 玩家经验值，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如果设置的exp值为负数，且超过当前等级已有的经验值，调用接口后，该玩家等级不会下降但是经验值会置为最小值

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
comp.AddPlayerExperience(25)
```



## AddPlayerLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.levelCompServer.LevelComponentServer

- 描述

    修改玩家等级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | int | 玩家等级，可设置负数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
comp.AddPlayerLevel(2)
```



## CollectOnlineClientData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    收集在线玩家客户端数据，用于判断玩家是否作弊

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | collectTypes | list(str) | 数据类型，不同类型收集到不同数据，具体说明参见备注。 |
    | callback | function | 回调函数，用于分析数据并判断玩家是否作弊，包含两个参数，第一个参数是playerId，类型str；第二个参数表示收集到的数据，dict类型，内容由collectTypes决定的，具体参见备注，若数据收集失败则为None（比如玩家不在线） |
    | extraArgs | dict | 默认为None，根据collectTypes传入不同参数，具体说明参见备注。 |

- 返回值

    无

- 备注
    - collectTypes中类型解释如下
        game类型收集到的数据字典解释如下：
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | gameType | int | 游戏模式，含义：-1：获取失败，0：生存模式，1：创造模式，2：冒险模式，3：旁观者模式|
        | levelGravity | float | 世界的重力因子|
        
        player类型收集到的数据字典解释如下：
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | playerHealth | int | 玩家生命值|
        
        world类型收集到的数据字典解释如下：
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | blockName | str | 某一位置方块的名称，要求extraArgs参数包含pos参数|
        | blockAuxValue | int | 某一位置方块的附加值AuxValue，要求extraArgs参数字典中包含"pos"，若缺少则没有数据|
        
        entity类型收集到的数据字典解释如下：
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | entityPos | tuple(float,float,float) | 实体位置，具体参见客户端GetPos接口说明，要求extraArgs参数字典中包含"entityId"，若缺少则没有数据|
        | entityGravity | float | 获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子，要求extraArgs参数字典中包含"entityId"，若缺少则没有数据|

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
def ProcessData(playerId, data):
    #正常返回实例：ProcessData 123 {'blockAuxValue': 0, 'blockName': 'minecraft:air', 'blockBoxSize': (-1.0, -1.0), 'gameType': 1, 'entityPos': (123,456,789), 'levelGravity': -0.08, 'playerHealth': 20, 'entityGravity': 0.0}
    #失败返回实例：ProcessData 123 None
    print minecraft'ProcessData', playerId, data
comp.CollectOnlineClientData(['player', 'world', 'entity', 'game'], ProcessData, {'entityId' :'123', 'pos' : (123,456,789))})
```



## GetPlayerExp

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    获取玩家当前等级下的经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPercent | bool | 是否为百分比 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家经验值 |

- 备注
    - 如果设置返回百分比为False，则返回玩家当前等级下经验的绝对值（非当前玩家总经验值）。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
print(comp.GetPlayerExp(False))
```



## GetPlayerHealthLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为18

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 健康临界值，-1表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.GetPlayerHealthLevel())
```



## GetPlayerHealthTick

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认值为80刻（即每4秒）恢复1点血量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 自然恢复速度，-1表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.GetPlayerHealthTick())
```



## GetPlayerHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家饥饿度，展示在UI饥饿度进度条上，初始值为20，即每一个鸡腿代表2个饥饿度。 **饱和度(saturation)** ：玩家当前饱和度，初始值为5，最大值始终为玩家当前饥饿度(hunger)，该值直接影响玩家**饥饿度(hunger)**。<br>1）增加方法：吃食物。<br>2）减少方法：每触发一次**消耗事件**，该值减少1，如果该值不大于0，直接把玩家 **饥饿度(hunger)** 减少1。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家饥饿度 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.GetPlayerHunger()
```



## GetPlayerLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.levelCompServer.LevelComponentServer

- 描述

    获取玩家等级

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 玩家等级 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateLv(playerId)
comp.GetPlayerLevel()
```



## GetPlayerMaxExhaustionValue

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家foodExhaustionLevel的归零值，常量值，默认为4。**消耗度（exhaustion）**是指玩家当前消耗度水平，初始值为0，该值会随着玩家一系列动作（如跳跃）的影响而增加，当该值大于最大消耗度（maxExhaustion）后归零，并且把饱和度（saturation）减少1（为了说明饥饿度机制，我们将此定义为**消耗事件**）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 玩家foodExhaustionLevel的归零值 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.GetPlayerMaxExhaustionValue()
```



## GetPlayerStarveLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 饥饿临界值 -1表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.GetPlayerStarveLevel())
```



## GetPlayerStarveTick

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为80刻（即每4秒）扣除1点血量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 饥饿掉血速度，-1表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.GetPlayerStarveTick())
```



## GetPlayerTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    获取玩家的总经验值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 总经验值，正整数。获取失败的情况下返回-1。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
print(comp.GetPlayerTotalExp())
```



## IsPlayerNaturalRegen

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效。原版默认开启

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示开启，False表示关闭，None表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.IsPlayerNaturalRegen())
```



## IsPlayerNaturalStarve

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动恢复血量，开启饥饿值且开启饥饿掉血时有效。原版默认开启

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示开启，False表示关闭，None表示获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
print(comp.IsPlayerNaturalStarve())
```



## SetPlayerHealthLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家健康临界值，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为18

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | healthLevel | int | 健康临界值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：健康临界值始终大于等于饥饿临界值。如果设置的健康临界值小于饥饿临界值，饥饿临界值将被设置为当前的健康临界值

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerHealthLevel(16) # 饥饿值大于等于16就会进入自然恢复状态，默认每隔4秒恢复1点血量
```



## SetPlayerHealthTick

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家自然恢复速度，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认值为80刻（即每4秒）恢复1点血量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | healthTick | int | 自然恢复速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：最小值为1，即每秒恢复20点血量

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerHealthTick(40) # 自然恢复状态下每隔2（40/20）秒恢复1点血量
```



## SetPlayerHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家饥饿度。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | 饥饿度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerHunger(10)
```



## SetPlayerMaxExhaustionValue

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家**最大消耗度(maxExhaustion)**，通过调整 **最大消耗度(maxExhaustion)** 的大小，就可以调整 **饥饿度(hunger)** 的消耗速度，当 **最大消耗度(maxExhaustion)** 很大时，饥饿度可以看似一直不下降

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | float | **最大消耗度(maxExhaustion)** |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 例如：当**最大消耗度(maxExhaustion)**为4时，玩家的饥饿消耗速度是**最大消耗度(maxExhaustion)**为8时的两倍

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerMaxExhaustionValue(10.0)
```



## SetPlayerNaturalRegen

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置是否开启玩家自然恢复，当饥饿值大于等于健康临界值时会自动恢复血量，开启饥饿值且开启自然恢复时有效.原版默认开启

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | bool | True开启，False关闭 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerNaturalRegen(False) # 关闭自然恢复，即使饥饿值大于健康临界值时也不会恢复血量
```



## SetPlayerNaturalStarve

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置是否开启玩家饥饿掉血，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认开启

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | value | bool | True开启，False关闭 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerNaturalStarve(False) # 关闭饥饿掉血，即使饥饿值小于饥饿临界值时也不会扣除血量
```



## SetPlayerPrefixAndSuffixName

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.nameCompServer.NameComponentServer

- 描述

    设置玩家前缀和后缀名字

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | prefix | str | 前缀内容 |
    | prefixColor | str | 前缀内容颜色描述，可以使用GenerateColor接口传入参数 |
    | suffix | str | 后缀内容 |
    | suffixColor | str | 后缀内容颜色描述，可以使用GenerateColor接口传入参数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateName(playerId)
comp.SetPlayerPrefixAndSuffixName("红队",serverApi.GenerateColor('RED'),'肉盾',serverApi.GenerateColor('RED'))
```



## SetPlayerStarveLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家饥饿临界值，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效。原版默认值为1

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | starveLevel | int | 饥饿临界值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：健康临界值始终大于等于饥饿临界值。如果设置的饥饿临界值大于健康临界值，将被设置为当前的健康临界值

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerStarveLevel(2) # 饥饿值小于等于2就会进入饥饿掉血状态，默认每隔4秒掉1点血量
```



## SetPlayerStarveTick

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家饥饿掉血速度，当饥饿值小于饥饿临界值时会自动扣除血量，开启饥饿值且开启饥饿掉血时有效.原版默认值为80刻（即每4秒）扣除1点血量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | starveTick | int | 饥饿掉血速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注：最小值为1，即每秒扣20点血量

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.SetPlayerStarveTick(40) # 饥饿掉血状态下每隔2（40/20）秒扣除1点血量
```



## SetPlayerTotalExp

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    设置玩家的总经验值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | exp | int | 总经验值，正整数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 根据总经验值会重新计算等级，该接口可引起等级的变化
    - 内部运算采用浮点数，数值较大时会出现误差

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
comp.SetPlayerTotalExp(25)
```



## Swing

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    本地玩家播放原版攻击动作

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayer(clientApi.GetLevelId())
comp.Swing()
```



## getUid

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    获取本地玩家的uid

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | long或None | 玩家uid |

- 备注
    - 不是客户端线程或者没有经过登录认证获取的uid为None。在当前机器上调用该接口获取的值为固定值，不依赖创建的player
    - getUid接口不能在加载mod过程中使用，推荐开发者在OnLocalPlayerStopLoading事件触发之后再使用

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
uid = comp.getUid()
```

## 摄像机

# 摄像机

## DepartCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    分离玩家与摄像机

- 参数

    无

- 返回值

    无

- 备注
    - 分离之后，可以看到玩家四周，旋转镜头时玩家面向的方向不再跟随镜头旋转而变化。注意，分离镜头后乘船时，船的组件minecraft:rideable中的lock_rider_rotation字段将失去效果。另外，在骑乘马或者其他生物的情况下，分离镜头后由于玩家的方向不再跟随镜头旋转，因此骑乘时无法进行转向，请注意这一点。

- 示例

```python
import mod.client.extraClientApi as clientApi
# 第三人称锁定视角例子
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.DepartCamera()
comp.LockModCameraYaw(1) # 锁定左右视角
comp.LockModCameraPitch(1) # 锁定上下视角
comp.SetCameraOffset((0, 0, 15))
comp.SetCameraRot((45.0, 0.0))
```



## GetCameraAnchor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取相机锚点

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 锚点偏移量 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.GetCameraAnchor()
```



## GetCameraOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取摄像机偏移量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 偏移量 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.GetCameraOffset()
```



## GetCameraPitchLimit

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取摄像机上下角度限制值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 上下角度限制值 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.GetCameraPitchLimit()
```



## GetCameraRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取相机转向

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 转向 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
rot = comp.GetCameraRot()
```



## GetForward

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    返回相机向前的方向

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 向前的方向 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.GetForward()
```



## GetFov

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取视野大小

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 即视频设置中的视野，单位为角度 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
fov = comp.GetFov()
```



## GetFpHeight

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    获取本地玩家当前状态下，第一人称视角时的摄像机高度偏移量。游泳时，滑翔时以及普通状态下会有所不同

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 高度偏移量 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
heightOffset = comp.GetFpHeight()
```



## GetPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerViewCompClient.PlayerViewCompClient

- 描述

    获取当前的视角模式

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayerView(entityId)
persp = comp.GetPerspective()
```



## GetPosition

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    返回相机中心

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 相机中心位置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.GetPosition()
```



## IsModCameraLockPitch

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    是否锁定摄像机上下角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否锁定 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.IsModCameraLockPitch()
```



## IsModCameraLockYaw

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    是否锁定摄像机左右角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否锁定 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.IsModCameraLockYaw()
```



## LockCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    锁定摄像机

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | lockPos | tuple(float,float,float) | 世界坐标 |
    | lockRot | tuple(float,float) | 摄像机的角度（俯仰角及偏航角） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 锁定摄像机时只是锁定画面视角，玩家仍然可以移动

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
# 把摄像机固定在(0, 6, 0)，并且30度俯视，朝向世界z轴正方向
comp.LockCamera((0, 6, 0), (30, 0))
```



## LockModCameraPitch

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    锁定摄像机上下角度（第三人称下生效，锁定后不能上下调整视角）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | int | 1:锁定 0:解锁 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.LockModCameraPitch(1)
```



## LockModCameraYaw

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    锁定摄像机左右角度（第三人称下生效，锁定后不能通过鼠标左右调整视角）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | int | 1:锁定 0:解锁 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.LockModCameraYaw(1)
```



## LockPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerViewCompClient.PlayerViewCompClient

- 描述

    锁定玩家的视角模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | lock | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 其他值：解除锁定 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否锁定成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayerView(entityId)
comp.LockPerspective(1)
```



## ResetCameraBindActorId

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    将摄像机重新绑定回主角身上

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.ResetCameraBindActorId()
```



## SetCameraAnchor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设置相机锚点,暂时只支持高度,其他维度无效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset | tuple(float,float,float) | 锚点偏移量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 与SetCameraOffset不同的是，该接口改变的是相机的轨道的圆心位置。对第一人称和第三人称模式均生效。
    - 注意，设置后的效果不会存档

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetCameraAnchor((0,1,0))
```



## SetCameraBindActorId

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    将摄像机绑定到目标实体身上（调用者与目标必须在同一个dimension，同时需要在加载范围之内，若绑定后目标离开了范围或者死亡，则会自动解除绑定）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 目标实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetCameraBindActorId('1234')
```



## SetCameraOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设置摄像机偏移量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | offset | tuple(float,float,float) | 偏移量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意，该接口仅改变第三人称的相机（包括前视第三人称和后视第三人称）的偏移量，对第一人称模式下的相机无效。
    - 与SetCameraAnchor不同的是，该接口改变的是相机的位置偏移值，不会对相机轨道的圆心位置进行改变。
    - 注意，设置后的效果不会存档

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetCameraOffset((1, 1, 1))
```



## SetCameraPitchLimit

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设置摄像机上下角度限制值，默认是（-90，90）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | limit | tuple(float,float) | 上下角度限制值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 注意，设置后的效果不会存档

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.DepartCamera()
comp.SetCameraPitchLimit((-30, 30))
```



## SetCameraPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设置相机中心的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意，设置后的效果不会存档

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetCameraPos((1, 1, 1))
```



## SetCameraRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设定相机转向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | 转向 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetCameraRot((1, 1))
```



## SetFov

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    设置视野大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fov | float | 单位为角度, 范围为[30, 110]，若fov小于30则设置为30，，若fov大于110，则设置为110. |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetFov(60)
```



## SetPerspective

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerViewCompClient.PlayerViewCompClient

- 描述

    设置视角模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | persp | int | 0：第一人称视角；1：第三人称视角；2：前视第三人称视角 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePlayerView(entityId)
comp.SetPerspective(1)
```



## SetSpeedFovLock

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    是否锁定相机视野fov，锁定后不随速度变化而变化

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isLocked | bool | 是否锁定 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.SetSpeedFovLock(True)
```



## UnDepartCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    绑定玩家与摄像机

- 参数

    无

- 返回值

    无

- 备注
    - 绑定之后，只能看到玩家背部

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.UnDepartCamera()
```



## UnLockCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.cameraCompClient.CameraComponentClient

- 描述

    解除摄像机锁定

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.UnLockCamera()
```

## 权限

# 权限

## GetPlayerAbilities

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家具体权限

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 具体权限，详见备注 |

- 备注
    - 具体权限说明
        | 权限字段 | 数据类型 | 说明 |
        | --------| ---- |------|
        | build | bool | 放置方块 |
        | mine | bool | 采集方块 |
        | doorsandswitches | bool | 使用门和开关 |
        | opencontainers | bool | 打开容器 |
        | attackplayers | bool | 攻击玩家 |
        | attackmobs | bool | 攻击生物 |
        | op | bool | 操作员命令 |
        | teleport | bool | 使用传送 |
    - 返回值示例
        ```python
        {'teleport': True, 'opencontainers': True, 'mine': True, 'build': True, 'op': True, 'attackmobs': True, 'doorsandswitches': True, 'attackplayers': True}
        ```

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
operation = comp.GetPlayerAbilities()
```



## GetPlayerOperation

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家权限类型信息

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 权限类型，Visitor为0，Member为1，Operator为2，Custom为3 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
operation = comp.GetPlayerOperation()
```

## 渲染

# 渲染

## AddPlayerAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家渲染动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationKey | str | 动画键 |
    | animationName | str | 动画名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerAnimation("move.arms", "animation.player.move.arms_custom")
```



## AddPlayerAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllerKey | str | 动画控制器键 |
    | animationControllerName | str | 动画控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerAnimationController("root", "controller.animation.player.root_custom")
```



## AddPlayerAnimationIntoState

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    在玩家的动画控制器中的状态添加动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllerName | str | 动画控制器名称，如root（controller.animation.player.root） |
    | stateName | str | 动画状态名称，如first_person |
    | animationName | str | 添加的动画名称或动画控制器名称，如first_person_attack_controller_new |
    | condition | str | 动画控制表达式，默认为空，如query.mod.index > 0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerAnimationIntoState("root", "first_person", "first_person_attack_controller_new", "query.mod.index > 0")
```



## AddPlayerGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家渲染几何体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryKey | str | 渲染几何体键，如玩家默认几何体default |
    | geometryName | str | 渲染几何体名称，如玩家默认几何体geometry.humanoid.custom |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效
        动画和贴图都是与几何体密切相关的，改变几何体也需要改变动画与贴图

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerGeometry("default", "geometry.player.custom")
```



## AddPlayerParticleEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家特效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectKey | str | 特效资源Key，如bee.entity.json中的nectar_dripping |
    | effectName | str | 特效资源名称，如minecraft:nectar_drip_particle |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerParticleEffect("nectar_dripping", "minecraft:nectar_drip_particle")
```



## AddPlayerRenderController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | renderControllerName | str | 渲染控制器名称 |
    | condition | str | 渲染控制器条件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerRenderController('custom_render_controller_name', 'query.mod.condition')
```



## AddPlayerRenderMaterial

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家渲染需要的<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质">材质</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | materialKey | str | 材质key |
    | materialName | str | 材质名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerRenderMaterial('custom_material_key', 'custom_material_name')
```



## AddPlayerSoundEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家音效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | soundKey | str | 音效资源Key |
    | soundName | str | 音效资源名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 音效在RP/entities/player.entity.json # minecraft:client_entity / description中的定义如下：
        "sound_effects": {
            "sound_thunder": "ambient.weather.thunder" # ambient.weather.thunder是sound_definitions中定义
        }
        如果在动作中同步播放音频，可以在RP/animations/player.animation_controllers.json # animation_controllers / controller.animation.player.root中定义如下：
        "dripping": {
            "sound_effects": [
                {
                    "effect": "sound_thunder"
                }
            ],
            "transitions": [
                {
                    "third_person": "!query.mod.is_powered"
                }
            ]
        },

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerSoundEffect("sound_thunder", "ambient.weather.thunder")
```



## AddPlayerTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加玩家渲染贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryKey | str | 贴图键 |
    | geometryName | str | 贴图路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddPlayerTexture("default", "textures/misc/missing_texture")
```



## RebuildPlayerRender

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    重建玩家的数据渲染器

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 重建是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.RebuildPlayerRender()
```



## RemovePlayerAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    移除玩家渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | animationControllKey | str | 动画控制器键 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.RemovePlayerAnimationController("root")
```



## RemovePlayerGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除玩家渲染几何体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryKey | str | 渲染几何体名称键，如玩家默认几何体default |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效
        动画和贴图都是与几何体密切相关的，改变几何体也需要改变动画与贴图

- 示例

```python
import mod.client.extraClientApi as clientApi
# geometry definition in player.entity.json
"geometry": {
    "default": "geometry.humanoid.custom",
    "cape": "geometry.cape"
}
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.RemovePlayerGeometry("default")
```



## RemovePlayerRenderController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除玩家<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器">渲染控制器</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | renderControllerName | str | 渲染控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功 |

- 备注
    - 调用该接口后需要调用RebuildPlayerRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.RemovePlayerRenderController('custom_render_controller_name')
```



## SetPlayerItemInHandVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置是否隐藏玩家的手持物品模型显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | visible | bool | 设置是否显示或隐藏，True表示显示，False表示隐藏 |
    | mode | int | 设置隐藏手持物品在哪一个视角模式生效。mode=0时，表示第一人称和第三人称下均隐藏手持物品；mode=1时表示仅隐藏第三人称下的手持物品；mode=2时表示仅隐藏第一人称下的手持物品。默认值为0。填入0,1,2以外的数值会被强制设置为0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
# 隐藏指定玩家的手持物品模型显示
print actorRenderComp.SetPlayerItemInHandVisible(False, 0)
```



## SetSkin

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.modelCompClient.ModelComponentClient

- 描述

    更换原版自定义皮肤

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | skin | str | 贴图路径，以textures\models为当前路径的相对路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 会覆盖原有皮肤（包括4d皮肤）。但会被骨骼模型覆盖

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
comp.SetSkin("kagura")
```

## 游戏模式

# 游戏模式

## GetPlayerGameType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取指定玩家的游戏模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | [GameType枚举](../../枚举值/GameType.md) |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
gameType = comp.GetPlayerGameType(playerId)
```



## SetPlayerGameType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家个人游戏模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | gameType | int | GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别为0~2 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerGameType(serverApi.GetMinecraftEnum().GameType.Survival)
```

## 背包

# 背包

## AddEnchantToInvItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    给物品栏的物品添加附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |
    | enchantType | int | 附魔类型，可以查看枚举值文档 |
    | level | int | 附魔等级 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.AddEnchantToInvItem(0, serverApi.GetMinecraftEnum().EnchantType.BowDamage, 2)
```



## AddModEnchantToInvItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    给物品栏中物品添加自定义附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |
    | modEnchantId | str | 自定义附魔identifier |
    | level | int | 自定义附魔等级 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.AddModEnchantToInvItem(0, "customenchant", 2)
```



## ChangePlayerItemTipsAndExtraId

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    修改玩家物品的自定义tips和自定义标识符

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | [ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | slotPos | int | 物品栏槽位 |
    | customTips | str | 物品的自定义tips |
    | extraId | str | 物品的自定义标识符 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.ChangePlayerItemTipsAndExtraId(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, 0, "自定义tips", "自定义标识符")
```



## ChangeSelectSlot

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家当前选中快捷栏物品的index

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slot | int | 快捷栏物品的index，从0开始，最大为8 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
success = comp.ChangeSelectSlot(0)
```



## GetCarriedItem

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.itemCompClient.ItemCompClient

- 描述

    获取右手物品的信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | getUserData | bool | 是否获取物品的userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateItem(entityId)
carriedData = comp.GetCarriedItem()
```



## GetInvItemEnchantData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取物品栏的物品附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(int,int)) | list中每个tuple由附魔类型([EnchantType枚举](../../枚举值/EnchantType.md))和附魔等级组成。没有附魔则为空list |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetInvItemEnchantData(0)
```



## GetInvItemModEnchantData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取物品栏的物品自定义附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(str,int)) | list中每个tuple由自定义附魔id和附魔等级组成，没有自定义附魔则为空list |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetInvItemModEnchantData(0)
```



## GetOffhandItem

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.itemCompClient.ItemCompClient

- 描述

    获取左手物品的信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | getUserData | bool | 是否获取物品的userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateItem(entityId)
offhandData = comp.GetOffhandItem()
```



## GetPlayerAllItems

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取玩家指定的槽位的批量物品信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | [ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>的数组，没有物品的位置为None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetPlayerAllItems(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY)
```



## GetPlayerItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取玩家物品，支持获取背包，盔甲栏，副手以及主手物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | [ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | slotPos | int | 槽位，获取INVENTORY及ARMOR时需要设置，其他情况写0即可 |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 备注
    - 左右手及装备可以替代GetEntityItem接口获取生物的物品，但背包不行。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetPlayerItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, 0)
```



## GetSelectSlotId

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取玩家当前选中槽位

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前槽位，错误时返回-1 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetSelectSlotId()
```



## GetSlotId

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.itemCompClient.ItemCompClient

- 描述

    获取当前手持的快捷栏的槽id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0到8 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateItem(entityId)
slotId = comp.GetSlotId()
```



## RemoveEnchantToInvItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    给物品栏的物品移除附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |
    | enchantType | int | 附魔类型，可以查看枚举值文档 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 移除结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.RemoveEnchantToInvItem(0, serverApi.GetMinecraftEnum().EnchantType.BowDamage)
```



## RemoveModEnchantToInvItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    给物品栏中物品移除自定义附魔信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |
    | modEnchantId | str | 自定义附魔identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 移除结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.RemoveModEnchantToInvItem(0, "customenchant")
```



## SetInvItemExchange

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    交换玩家背包物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos1 | int | 物品位置 |
    | pos2 | int | 物品位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.SetInvItemExchange(0, 2)
```



## SetInvItemNum

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    设置玩家背包物品数目

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | 物品栏槽位 |
    | num | int | 物品数目，可以通过设置数量为0来达到清除背包物品的效果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.SetInvItemNum(0, 10)
```



## SetPlayerAllItems

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    添加批量物品信息到指定槽位

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemsDictMap | dict | 需要添加的物品的字典，字典的key是tuple([ItemPosType](../../枚举值/ItemPosType.md), slotPos)，value是需要添加的<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 设置结果，字典的key是tuple(ItemPosType, slot)，value为bool代表该槽位设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
itemsDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
itemsDictMap = {}
for i in xrange(36):
    if i % 3 == 0:
        itemsDictMap[(minecraftEnum.ItemPosType.INVENTORY, i)] = itemsDict
itemsDictMap[(minecraftEnum.ItemPosType.CARRIED, 0)] = itemsDict
itemsDictMap[(minecraftEnum.ItemPosType.OFFHAND, 0)] = itemsDict
comp.SetPlayerAllItems(itemsDictMap)
```



## SpawnItemToPlayerCarried

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    生成物品到玩家右手

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | playerId | str | 玩家id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.SpawnItemToPlayerCarried(itemDict, playerId)
```



## SpawnItemToPlayerInv

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    生成物品到玩家背包

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | playerId | str | 玩家id |
    | slotPos | int | 背包槽位(可选) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 当slotPos不设置时，当设置的数量超过单个槽位堆叠的上限时，会将多余的物品设置到另外的空闲槽位.如果生成的物品与背包中有的槽位的物品种类一致，该接口也会将物品增加到这些槽位中。注意：如果背包中剩余的物品数目和增加的物品数目之和大于64，则会生成物品数目到64，但是接口返回失败。

- 示例

```python
import mod.server.extraServerApi as serverApi
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.SpawnItemToPlayerInv(itemDict, playerId, 0)
```

## 行为

# 行为

## AddPlayerAroundEntityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给玩家添加对实体环绕运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eID | str | 要环绕的某个实体的ID |
    | angularVelocity | float | 圆周运动的角速度（弧度/秒） |
    | axis | tuple(float,float,float) | 圆周运动的轴，决定了在哪个平面上做圆周运动，默认为(0, 1, 0) |
    | lockDir | bool | 是否在运动器生效时锁定实体的朝向，不锁定则实体的朝向会随着运动而改变，默认为False。 |
    | stopRad | float | 停止该运动器所需要的弧度，当stopRad为0时，该运动器会一直运行，默认为0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽玩家控制的移动以及重力作用，当有玩家控制发生时，最终的表现结果可能与预期有差异。由于玩家的头部与相机控制相关，若需要使运动器控制玩家的头部，请使用[DepartCamera](./摄像机.md#DepartCamera)分离玩家与摄像机。
    - 环绕运动器可叠加多个，且可与速度运动器互相叠加。
    - 由于引擎中有加载的区块限制，建议将玩家的运动范围控制在当前位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
axis=(-1, 1, 1)
mID = motionComp.AddPlayerAroundEntityMotion(eID, 1.0, axis, lockDir=False, stopRad=0)
```



## AddPlayerAroundPointMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给玩家添加对点环绕运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | center | tuple(float,float,float) | 要环绕的圆心点坐标 |
    | angularVelocity | float | 圆周运动的角速度（弧度/秒） |
    | axis | tuple(float,float,float) | 圆周运动的轴，决定了在哪个平面上做圆周运动，默认为(0, 1, 0) |
    | lockDir | bool | 是否在运动器生效时锁定实体的朝向，不锁定则玩家的朝向会随着运动而改变，默认为False。 |
    | stopRad | float | 停止该运动器所需要的弧度，当stopRad为0时，该运动器会一直运行，默认为0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽玩家控制的移动以及重力作用，当有玩家控制发生时，最终的表现结果可能与预期有差异。由于玩家的头部与相机控制相关，若需要使运动器控制玩家的头部，请使用[DepartCamera](./摄像机.md#DepartCamera)分离玩家与摄像机。
    - 环绕运动器可叠加多个，且可与速度运动器互相叠加。
    - 由于引擎中有加载的区块限制，建议将玩家的运动范围控制在当前位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
center = (0, 8, 0)
axis=(-1, 1, 1)
mID = motionComp.AddPlayerAroundPointMotion(center, 1.0, axis, lockDir=False, stopRad=0)
```



## AddPlayerTrackMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给玩家添加轨迹运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 轨迹终点 |
    | duraTime | float | 到达终点所需要的时间 |
    | startPos | tuple(float,float,float) | 轨迹起点，默认为None，表示以调用[StartPlayerMotion](#StartPlayerMotion)的位置作为起点。 |
    | relativeCoord | bool | 是否使用相对坐标设置起点和终点，默认为False。 |
    | isLoop | bool | 是否循环，若设为True，则玩家会在起点和终点之间往复运动。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽玩家控制的移动，当有玩家控制发生时，最终的表现结果可能与预期有差异。
    - 轨迹运动器不可叠加，仅能添加一个。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
target = (5, 0, 0)
mID = motionComp.AddPlayerTrackMotion(target, 3.0, startPos=None, relativeCoord=True, isLoop=False)
```



## AddPlayerVelocityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给玩家添加速度运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | velocity | tuple(float,float,float) | 速度，包含大小、方向 |
    | accelerate | tuple(float,float,float) | 加速度，包含大小、方向，默认为None，表示没有加速度 |
    | useVelocityDir | bool | 是否使用当前速度的方向作为此刻实体的朝向，默认为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽玩家控制的移动以及重力作用，当有玩家控制发生时，最终的表现结果可能与预期有差异。由于玩家的头部与相机控制相关，若需要使运动器控制玩家的头部，请使用[DepartCamera](./摄像机.md#DepartCamera)分离玩家与摄像机。
    - 速度运动器可叠加多个，且可与环绕运动器互相叠加。
    - 由于引擎中有加载的区块限制，建议将玩家的运动范围控制在当前位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
velocity = (0, 0, 1)
accelerate = (0, 0, -1)
mID = motionComp.AddPlayerVelocityMotion(velocity, accelerate, useVelocityDir=True)
```



## BeginSprinting

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorMotionCompClient.ActorMotionComponentClient

- 描述

    使本地玩家进入并保持向前冲刺状态

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorMotion(localPlayerId)
comp.BeginSprinting()
```



## ChangePlayerDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    传送玩家

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度，0-overWorld; 1-nether; 2-theEnd |
    | pos | tuple(int,int,int) | 传送的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 该接口在成功切换维度时pos位置为玩家头的位置，即比设定位置低1.62

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(playerId)
comp.ChangePlayerDimension(0, (0,4,0))
```



## ChangePlayerFlyState

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.flyCompServer.FlyComponentServer

- 描述

    给予/取消飞行能力，并且进入飞行/非飞行状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isFly | bool | 飞行状态，True：飞行模式，False：正常行走模式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |

- 备注
    - 不建议在OnGroundClientEvent事件回调中NotifyToServer，然后服务端收到数据后，调用ChangePlayerFlyState接口。
        如果仍然需要这样调用，则建议在服务端收到数据后，用AddTimer延迟一帧后再调用ChangePlayerFlyState接口

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
comp.ChangePlayerFlyState(True)
```



## EnableKeepInventory

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家死亡不掉落物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启“保留物品栏” |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
succ = comp.EnableKeepInventory(True)
```



## EndSprinting

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorMotionCompClient.ActorMotionComponentClient

- 描述

    使本地玩家结束向前冲刺状态

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorMotion(localPlayerId)
comp.EndSprinting()
```



## GetEntityRider

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    获取玩家正在骑乘的实体的id。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 玩家直接骑乘对象的实体id，假如玩家没有骑乘则返回“-1” |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
riderId = comp.GetEntityRider()
```



## GetIsBlocking

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家激活盾牌状态

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 玩家盾牌状态是否激活 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.GetIsBlocking()
```



## GetPlayerExhaustionRatioByType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家某行为饥饿度消耗倍率

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | type | int |  行为枚举[PlayerExhauseRatioType枚举](../../枚举值/PlayerExhauseRatioType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 饥饿度消耗倍率值, -1为获取失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
jumpType = serverApi.GetMinecraftEnum().PlayerExhauseRatioType.JUMP
ratio = comp.GetPlayerExhaustionRatioByType(jumpType)
```



## GetPlayerMotions

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    获取玩家身上的所有运动器

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 运动器集合，key值代表运动器mID，value值代表运动器类型0：轨迹运动器、1：速度运动器、2：环绕运动器 |

- 备注
    - 运动器非人为停止后会被移除。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
motions = motionComp.GetPlayerMotions()
# motions = {
#   0:1,
#   1:2
# }
```



## GetPlayerRespawnPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家复活点

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 复活点信息，包括维度和坐标 |

- 备注
    - 使用spawnpoint指令设置玩家的出生点后，该接口可以获取到设置后的出生点
    - 未使用setworldspawn指令设置过出生点位置时，返回坐标的y轴是32767

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
print comp.GetPlayerRespawnPos()
#结果示例 {'dimensionId': 0, 'pos': (44, 32767, 4)}
```



## GetRelevantPlayer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取附近玩家id列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | list(str) | exceptList | 排除的玩家id列表,默认值为None,不排除其他玩家及自身 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 附近玩家id列表 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.GetRelevantPlayer(exceptId)
```



## IsEntityRiding

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    检查玩家是否骑乘。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否骑乘 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
isRiding = comp.IsEntityRiding()
```



## IsPlayerFlying

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.flyCompServer.FlyComponentServer

- 描述

    获取玩家是否在飞行

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:是 False:否 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFly(playerId)
comp.IsPlayerFlying()
```



## PickUpItemEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    某个Player拾取物品ItemEntity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerEntityId | str | 拾取者的playerEntityId |
    | itemEntityId | str |  要拾取的物品itemEntityId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否拾取成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.PickUpItemEntity(playerEntityId, itemEntityId)
```



## PlayerDestoryBlock

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    使用手上工具破坏方块

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | particle | int | 是否开启破坏粒子效果，默认为开 |
    | sendInv | bool | 是否同步服务端背包信息，默认为不同步。因为破坏方块可能会造成手持物品耐久度降低等信息改变，不同步信息可能会造成后续一些逻辑异常，若大批量破坏方块，每次同步会有性能问题，建议前面的调用可令sendInv为False，在最后一次调用此函数时传入sendInv为True。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 手上工具的附魔效果会生效，同时扣除耐久度
    - 会触发ServerPlayerTryDestroyBlockEvent事件，并且可以被这个事件cancel

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)  # 此处playerId为block的破坏者
comp.PlayerDestoryBlock((0, 5, 0), 1, False)
comp.PlayerDestoryBlock((0, 6, 0), 1, True)

# 关闭破坏粒子效果
comp.PlayerDestoryBlock((0, 6, 0),0)
```



## PlayerUseItemToEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    玩家使用手上物品对某个生物使用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物entityId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 1.会触发PlayerInteractServerEvent事件，并且可以被这个事件cancel；2.此接口无视距离，但无法跨维度使用，同时需要目标区域已加载

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)  # 此处playerId为使用物品的玩家
suc = comp.PlayerUseItemToEntity("-123456")
```



## PlayerUseItemToPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    玩家对某个坐标使用物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 坐标 |
    | posType | int | 物品所在的地方[ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | slotPos | int | 槽位，获取INVENTORY及ARMOR时需要设置，其他情况写0即可 |
    | facing | int | 朝向，详见[Facing枚举](../../枚举值/Facing.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 当使用抛射物时，只有在非创造模式下才会返回True;如果要对"盔甲架"等实体使用物品，请使用PlayerUseItemToEntity接口;只能对玩家周边200格以内的坐标使用

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)  # 此处playerId为使用物品的玩家
comp.PlayerUseItemToPos((0, 5, 0), serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, 0, 1)
```



## RemovePlayerMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    移除玩家身上的运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 要移除的某个运动器的ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功移除 |

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
motionComp.RemovePlayerMotion(mID)
```



## SetPickUpArea

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家的拾取物品范围，设置后该玩家的拾取物品范围会在原版拾取范围的基础上进行改变。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | area | tuple(float,float,float) | 拾取物品范围，传入(0, 0, 0)时视作取消设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
# 玩家拾取物品范围在X轴正负方向各增加5格，在Z轴正负方向各增加3格，在Y轴保持不变
succ = comp.SetPickUpArea((5, 0, 3))
```



## SetPlayerAttackSpeedAmplifier

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家攻击速度倍数，1.0表示正常水平，1.2表示速度减益20%，0.8表示速度增益20%

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | amplifier | float | 攻击速度倍数，范围[0.5,2.0] |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 该接口影响接口[SetHurtCD](../世界/游戏规则.md#sethurtcd)设置的全局攻击cd

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerAttackSpeedAmplifier(1.1)
```



## SetPlayerExhaustionRatioByType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家某行为饥饿度消耗倍率

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | type | int |  行为枚举[PlayerExhauseRatioType枚举](../../枚举值/PlayerExhauseRatioType.md) |
    | ratio | float |  倍率 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
jumpType = serverApi.GetMinecraftEnum().PlayerExhauseRatioType.JUMP
ratio = comp.SetPlayerExhaustionRatioByType(jumpType, 20)
```



## SetPlayerJumpable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家是否可跳跃

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isJumpable | bool | 是否可跳跃,True允许跳跃，False禁止跳跃 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerJumpable(False)
```



## SetPlayerMovable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家是否可移动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isMovable | bool | 是否可移动,True允许移动，False禁止移动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
comp.SetPlayerMovable(False)
```



## SetPlayerRespawnPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    设置玩家复活的位置与维度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 复活点的位置坐标 |
    | dimensionId | int | 复活点的维度，默认值为0（主世界），注意1：维度21是不可用的；注意2：不能在玩家死亡（PlayerDieEvent）之后设置复活点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
suc = comp.SetPlayerRespawnPos((0, 4, 0), 0)
```



## SetPlayerRideEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    设置玩家骑乘生物（或者船与矿车）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | rideEntityId | str | 被骑乘生物id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 通常需要配合SetEntityRide、SetControl一起使用
        当被控制的entity有多个位置时且开发者想要添加多个玩家时，第一个被添加的玩家会被引擎默认设置为控制者

- 示例

```python
# 骑上坐骑
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetPlayerRideEntity(playerId,rideEntityId)
```



## StartPlayerMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    启动玩家身上的某个运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 要启动的某个运动器的ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功启动 |

- 备注
    - 由于玩家的运动器需要在客户端与服务端之间同步，所以请以[EntityMotionStartServerEvent](../../事件/实体.md#EntityMotionStartServerEvent)事件的触发作为真正的开始时机。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
motionComp.StartPlayerMotion(mID)
```



## StopEntityRiding

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    强制玩家下坐骑。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 当玩家当前正在骑乘并成功下坐骑返回True，否则返回False |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
success = comp.StopEntityRiding()
```



## StopPlayerMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    停止玩家身上的某个运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 要停止的某个运动器的ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功停止 |

- 备注
    - 调用该接口不会触发事件[EntityMotionStopServerEvent](../../事件/实体.md#EntityMotionStopServerEvent)。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(playerId)
motionComp.StopPlayerMotion(mID)
```



## isGliding

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否鞘翅飞行

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否鞘翅飞行 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isGliding()
```



## isInWater

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否在水中

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在水中 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isInWater()
```



## isMoving

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否在行走

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在行走 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isMoving()
```



## isRiding

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否骑乘

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否骑乘 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isRiding()
```



## isSneaking

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家是否处于潜行状态

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 当前玩家是否处于潜行状态 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
is_sneaking = comp.isSneaking()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否潜行

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否潜行 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isSneaking()
```



## isSprinting

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否在疾跑

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在疾跑 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isSprinting()
```



## isSwimming

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.playerCompServer.PlayerCompServer

- 描述

    获取玩家是否处于游泳状态。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 当前玩家是否处于游泳状态 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
is_swiming = comp.isSwimming()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    是否游泳

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否游泳 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.isSwimming()
```



## setMoving

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    设置是否行走，只能设置本地玩家（只适用于移动端）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.setMoving()
```



## setSneaking

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    设置是否潜行，只能设置本地玩家（只适用于移动端）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.setSneaking()
```



## setSprinting

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    设置是否疾跑，只能设置本地玩家（只适用于移动端）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.setSprinting()
```



## setUsingShield

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.playerCompClient.PlayerCompClient

- 描述

    激活盾牌状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | flag | bool | True使用盾牌，False取消使用盾牌 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 1设置成功，0设置失败，-1玩家未持盾 |

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreatePlayer(entityId)
comp.setUsingShield(True)
```

