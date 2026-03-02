# ModAPI 接口-世界

## 目录

- [地图](#地图)
- [天气](#天气)
- [实体管理](#实体管理)
- [指令](#指令)
- [方块管理](#方块管理)
- [方块组合](#方块组合)
- [时间](#时间)
- [消息](#消息)
- [渲染](#渲染)
- [游戏规则](#游戏规则)
- [生物生成](#生物生成)
- [自定义数据](#自定义数据)
- [配方](#配方)

---

## 地图

# 地图

## CanSee

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    判断起始对象是否可看见目标对象,基于对象的Head位置判断

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromId | str | 起始对象ID |
    | targetId | str | 目标对象ID |
    | viewRange | float | 视野距离,默认值8.0 |
    | onlySolid | bool | 只判断固体方块遮挡,默认True; False则液体方块也会遮挡 |
    | angleX | float | 视野X轴角度,默认值180.0度 |
    | angleY | float | 视野Y轴角度,默认值180.0度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否可见 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
comp.CanSee(entityId,targetId,20.0,True,180.0,180.0)
```



## CheckBlockToPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    判断位置之间是否有方块

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromPos | tuple(float,float,float) | 起始位置 |
    | toPos | tuple(float,float,float) | 终止位置 |
    | dimensionId | int | 位置所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | result -1：获取失败  0：没有方块  1：有方块 |

- 备注
    - 支持判断对应维度的常加载区块内位置之间是否有方块
    - 返回-1通常是由于传入维度不存在、传入错误参数、传入位置所在区块并未加载等

- 示例

```python
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
if comp.CheckBlockToPos((0, 0, 0), (1, 1, 1), 0):
    logger.info("(0, 0, 0)与(1, 1, 1)之间有方块")
```



## CheckChunkState

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    判断指定位置的chunk是否加载完成

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | chunk所在维度 |
    | pos | tuple(int,int,int) | 指定位置的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 加载是否完成 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
comp.CheckChunkState(0, (0, 0, 0))
```



## CreateDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    创建新的dimension

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度，0/1/2维度是不需要创建的。创建大于20的维度，需要在dimension_config.json中注册，注意，维度21是不可用的 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否创建成功 |

- 备注
    - 建议在mod初始化时统一调用
    - 与维度相关的接口(SetUseLocalTime,SetDimensionUseLocalWeather等)会影响出生点的生成，如果要用主世界地形生成出生点，需要在mod初始化的时候优先调用一次CreateDimension(0)

- 示例

```python
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.CreateDimension(3)
```



## CreateExplosion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.explosionCompServer.ExplosionComponentServer

- 描述

    用于生成爆炸

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 爆炸位置 |
    | radius | int | 爆炸威力，具体含义可参考[wiki](https://minecraft-zh.gamepedia.com/%E7%88%86%E7%82%B8)对爆炸的解释 |
    | fire | bool | 是否带火 |
    | breaks | bool | 是否破坏方块 |
    | sourceId | str | 爆炸伤害源的实体id |
    | playerId | str | 爆炸创造的实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExplosion(levelId)
comp.CreateExplosion((50,50,50),10,True,True,sourceId,playerId)
```



## DeleteAllArea

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    删除所有常加载区域

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 删除的区域数目，错误时为None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
comp.DeleteAllArea()
```



## DeleteArea

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    删除一个常加载区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 常加载区域的名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
comp.DeleteArea('Area0')
```



## DetectStructure

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.portalCompServer.PortalComponentServer

- 描述

    检测自定义门的结构

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | None | 该参数未使用，直接传入None即可 |
    | pattern | list(str) | 传送门形状 |
    | defines | dict | 传送门定义 |
    | touchPos | list(tuple(int,int)) | 传送门可激活的位置（相对参数pattern中定义的位置） |
    | pos | tuple(int,int,int) | 使用物品坐标 |
    | dimensionId | int | 传送门所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(bool,tuple(int,int,int),tuple(int,int,int)) | 检测结果,传送门起始位置,方向 |

- 示例

```python
#传送门定义
defines = {
    '#': 'minecraft:glowstone',
    '*': 'minecraft:air'
}
#传送门形状
pattern = [
    '####',
    '#**#',
    '#**#',
    '####',
]
# 最下面中间的两个位置点击激活
touchPos =[(3,1),(3,2)]
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePortal(levelId)
ret = comp.DetectStructure(None, pattern, defines, touchPos, (12, 1, 5), 0)
if ret[0]:
    logger.info('自定义传送门构建成功')
else:
    logger.info('自定义传送门构建失败')
```



## GetAllAreaKeys

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取所有常加载区域名称列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 名称列表list |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
comp.GetAllAreaKeys()
```



## GetBiomeName

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.biomeCompServer.BiomeCompServer

- 描述

    获取某一位置所属的生物群系信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 指定位置 |
    | dimId | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 该位置所属生物群系name |

- 备注
    - 支持获取未加载区块的群系。但对于未加载的区块，将使用地形生成器来计算群系，而非存档内保存的群系。因此对于使用地图修改器修改过群系的地图，获取未加载区块的群系，结果可能与实际不符，建议确认区块加载完毕后再获取。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBiome(levelId)
biomeName = comp.GetBiomeName((0, 80, 0), 0)
```



## GetBlockLightLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取方块位置的光照等级

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 光照等级 |

- 备注
    - 仅能获取到已加载区块内方块位置的光照等级，支持获取对应维度的常加载区块内光照等级

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
lightlevel = comp.GetBlockLightLevel((x,y,z), 0)
```



## GetChunkEntites

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取指定位置的区块中，全部的实体和玩家的ID列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 指定位置的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或list(str) | 实体和玩家的ID的列表，当指定位置的区块不存在或尚未加载时，返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
entityList = comp.GetChunkEntites(0, (0, 0, 0))
print "GetChunkEntites entityList={}".format(entityList)
```



## GetChunkMaxPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取某区块最大点的坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或tuple(int,int,int) | 该区块最大点的坐标 |

- 备注
    - 当传入的chunkPos类型不是tuple或者长度不为2时，返回值为None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
maxPos = comp.GetChunkMaxPos((1, 3))
```



## GetChunkMinPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取某区块最小点的坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或tuple(int,int,int) | 该区块最小点的坐标 |

- 备注
    - 当传入的chunkPos类型不是tuple或者长度不为2时，返回值为None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
minPos = comp.GetChunkMinPos((1, 3))
```



## GetChunkMobNum

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取某区块中的生物数量（不包括玩家，但包括盔甲架）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 区块所在维度 |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 该区块中的生物数量 |

- 备注
    - 返回值为-1通常是由于该维度未加载、该区块未加载

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
mobNum = comp.GetChunkMobNum(0, (1, 3))
```



## GetChunkPosFromBlockPos

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    通过方块坐标获得该方块所在区块坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockPos | tuple(int,int,int) | 方块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或tuple(int,int) | 该方块所在区块的坐标 |

- 备注
    - 当传入的blockPos类型不是tuple或者长度不为3时，返回值为None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
chunkPos = comp.GetChunkPosFromBlockPos((90, 40, -4))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.chunkSourceCompClient.ChunkSourceCompClient

- 描述

    通过方块坐标获得该方块所在区块坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockPos | tuple(int,int,int) | 方块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或tuple(int,int) | 该方块所在区块的坐标 |

- 备注
    - 当传入的blockPos类型不是tuple或者长度不为3时，返回值为None

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateChunkSource(LevelId)
chunkPos = comp.GetChunkPosFromBlockPos((90, 40, -4))
```



## GetCurrentDimension

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    获取客户端当前维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id。客户端未登录完成或正在切维度时返回-1 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
dimId = comp.GetCurrentDimension()
```



## GetEntitiesAround

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取区域内的entity列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 某个entityId |
    | radius | int | 正方体区域半径 |
    | filters | dict | 过滤设置字典 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回entityId的list |

- 备注
    - 过滤器在对区域内的所有实体进行过滤时，会把每一个实体设置为other，同时把entityId对应的实体设置为self。关于过滤器的详细说明，用户可以查看基岩版wiki：https://bedrock.dev/zh/docs/stable/Entities#Filters
    - 过滤器中"subject"表示过滤判断的实体类型，"subject"="self"表示对每个实体设置的self进行过滤判断,"subject"="other"表示对每个实体设置的other进行过滤判断

- 示例

```python
#利用过滤器获取玩家身边的entity
#样例中的过滤器表示满足“是玩家”或者“没有头戴南瓜帽”的entity
filters = {
    "any_of": [
        {
            "subject" : "other",
            "test" :  "is_family",
            "value" :  "player"
        },
        {
            "test" :  "has_equipment",
            "domain": "head",
            "subject" : "other",
            "operator" : "not",
            "value" : "carved_pumpkin"
        }
    ]
}
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
comp.GetEntitiesAround(entityId, 100, filters)
```



## GetEntitiesAroundByType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取区域内的某类型的entity列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 区域中心的entityId,如某个玩家的entityid |
    | radius | int | 区域半径 |
    | entityType | int | [EntityType枚举](../../枚举值/EntityType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回entityId的list |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 获取身边10格内的掉落物
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.GetEntitiesAroundByType(entityId, 10, serverApi.GetMinecraftEnum().EntityType.ItemEntity)
```



## GetEntitiesInSquareArea

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取区域内的entity列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | None | 该参数已废弃 |
    | startPos | tuple(int,int,int) | 初始位置 |
    | endPos | tuple(int,int,int) | 结束位置 |
    | dimensionId | int | 区域所在维度，可获取对应维度的常加载区块内的实体列表 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回entityId的list |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.GetEntitiesInSquareArea(None, (0,0,0), (100,100,100), 0)
```



## GetEntityInArea

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    返回区域内的实体，可获取到区域范围内已加载的实体列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或None | 实体Id |
    | pos_a | tuple(int,int,int) | 起点 |
    | pos_b | tuple(int,int,int) | 终点，终点应大于起点 |
    | exceptEntity | bool | 返回结果中是否除去entityId, 默认为False，传入entityId为None时exceptEntity无作用 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 区域范围内已加载的entityId列表 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
entities = comp.GetEntityInArea(entityId, (0,0,0), (1,2,3))
```



## GetLevelId

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 当前地图的levelId |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def ExtraDataTest(args):
        extraDataComp = serverApi.GetEngineCompFactory().CreateExtraData(serverApi.GetLevelId())
        extraDataComp.score = 100
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取levelId。某些组件需要levelId创建，可以用此接口获取levelId。其中level即为当前地图的游戏。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 当前地图的levelId |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def CameraCompTest(args):
        cameraComp = clientApi.GetComponent(clientApi.GetLevelId(), 'Minecraft', 'camera')
        cameraComp.fov = 60
```



## GetLoadedChunks

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取指定维度当前已经加载完毕的全部区块的坐标列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None或list(tuple(int,int)) | 区块坐标的列表（区块坐标为(x,z)），当指定维度不存在或尚未创建时，返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
result = comp.GetLoadedChunks(0)
print "dimension {} has chunk {}".format(0, result)
```



## GetSpawnDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取世界出生维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
spawnDimension = gameComp.GetSpawnDimension()
```



## GetSpawnPosition

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取世界出生点坐标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 出生点坐标 |

- 备注
    - 返回的坐标不一定是精确的出生点坐标，也不一定是安全的出生点，玩家出生时会在该坐标附近随机选取一个满足出生条件的坐标。
    - 未使用setworldspawn指令设置过出生点位置时，返回坐标的y轴是32767

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
spawnPos = gameComp.GetSpawnPosition()
```



## IsChunkGenerated

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取某个区块是否生成过。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 区块所在维度 |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 该区块是否生成过 |

- 备注
    - 玩家探索过（以玩家为中心，模拟距离（在游戏的设置页面内）为半径内的区块），或者使用SetAddArea设置常加载区块附近的区块，都是生成过的区块。这些区块会保存到存档里，再次探索时会从存档读取，不会重新生成。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
# 获取主世界(10000,0,10000)坐标所在的区块是否生成过
result = comp.IsChunkGenerated(0, comp.GetChunkPosFromBlockPos((10000, 0, 10000)))
```



## IsSlimeChunk

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    获取某个区块是否史莱姆区块。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 区块所在维度 |
    | chunkPos | tuple(int,int) | 指定区块的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 该区块是否史莱姆区块 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
result = comp.IsSlimeChunk(0, comp.GetChunkPosFromBlockPos((10000, 0, 10000)))
```



## LocateNeteaseFeatureRule

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.featureCompServer.FeatureCompServer

- 描述

    与[/locate指令](https://minecraft-zh.gamepedia.com/%E5%91%BD%E4%BB%A4/locate)相似，用于定位<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/4-自定义特征.html#特征规则（feature-rules）">网易自定义特征规则</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | ruleName | str | 特征规则名称，形式为namespace:featureRuleIdentifier，如custombiomes:overworld_pumpkins_feature_rule |
    | dimensionId | int | 查找维度，**要求该维度已加载** |
    | pos | tuple(int,int,int) | 以该位置为中心来查找满足网易自定义特征规则分布条件的坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float)或None | 最近的满足网易自定义特征规则分布条件的坐标，定位失败则返回None |

- 备注
    - 定位失败通常是由于传入维度不存在、维度未加载、没有满足该自定义特征规则分布条件的坐标、目标坐标距离传入位置过远（以该位置为中心，半径100个区块内无法找到）等
    - 若在feature rules中"conditions"内的"minecraft:biome_filter"中**填写了判断维度以外的过滤规则，将有概率无法定位到满足该自定义特征规则分布条件的坐标**。建议开发者在"distribution"的"iterations"中使用query.is_biome代替
    - 定位原理是根据网易自定义特征规则分布条件寻找可能的位置，因此**有可能会定位到在PlaceNeteaseStructureFeatureEvent事件中被取消生成的结构位置**。开发者应注意甄别，尽量避免对可能在PlaceNeteaseStructureFeatureEvent事件中被取消放置的结构对应特征规则文件调用定位函数

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
pos = comp.LocateNeteaseFeatureRule("custombiomes:overworld_pumpkins_feature_rule", 0, (0, 64, 0))
```



## LocateStructureFeature

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.featureCompServer.FeatureCompServer

- 描述

    与[/locate指令](https://minecraft-zh.gamepedia.com/%E5%91%BD%E4%BB%A4/locate)相似，用于定位原版的部分结构，如海底神殿、末地城等。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | featureType | int | 原版的结构类型，[StructureFeatureType](../../枚举值/StructureFeatureType.md)枚举 |
    | dimensionId | int | 结构所在维度，**要求该维度已加载** |
    | pos | tuple(int,int,int) | 以该位置为中心来查找最近的结构 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float)或None | 最近的结构所在区块位置(x坐标,z坐标)，y坐标不定，若定位失败则返回None |

- 备注
    - 定位失败通常是由于该维度不存在、该维度未加载、该维度中不存在该结构、该结构距离传入位置过远等
    - 该接口返回值为对应结构所在区块的坐标，与结构实际生成位置可能相距一定距离

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateFeature(levelId)
pos = comp.LocateStructureFeature(serverApi.GetMinecraftEnum().StructureFeatureType.Village, 0, (0, 64, 0))
```



## MayPlace

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    判断方块是否可以放置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 方块identifier，如minecraft:wheat |
    | blockPos | tuple(int,int,int) | 方块将要放置的坐标 |
    | facing | int | 朝向，详见[Facing枚举](../../枚举值/Facing.md) |
    | dimensionId | int | 维度，默认为主世界0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 方块是否可以放置 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
pos = (-1, 4, 34)
canPlace = comp.MayPlace("minecraft:wheat", pos, serverApi.GetMinecraftEnum().Facing.Up, 0)
```



## MayPlaceOn

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    判断物品是否可以放到指定的位置上

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 物品标识，如minecraft:dye |
    | auxValue | int | 物品的附加值 |
    | blockPos | tuple(int,int,int) | 位置坐标 |
    | facing | int | 朝向，详见[Facing枚举](../../枚举值/Facing.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否可以放置 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.MayPlaceOn("minecraft:dye", 3, (1,2,3), serverApi.GetMinecraftEnum().Facing.Up)
```



## MirrorDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    复制不同dimension的地形

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromId | int | 原dimensionId |
    | toId | int | 目标dimensionId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 仅复制源维度已经生成的区块信息到新的维度，对于未生成的源维度区块无法完全复制生成逻辑，可能采用部分新维度自己的信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.MirrorDimension(0, 1)
```



## PlaceStructure

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    放置结构

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | None | 该参数已废弃 |
    | pos | tuple(float,float,float) | 放置结构的位置 |
    | structureName | str | 结构名称 |
    | dimensionId | int | 希望放置结构的维度，可在对应维度的常加载区块放置结构，默认为-1 |
    | rotation | int | 放置结构的旋转角度，默认为0(只可旋转90，180，270度) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否放置成功，True为放置成功，False为放置失败 |

- 备注
    - 放置时需要确保所放置的区块都已加载，否则会放置失败或者部分缺失
    - 该接口是同步执行的，请勿在一帧内放置大量结构，会造成游戏卡顿

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.PlaceStructure(None, (100, 70, 100), "test:structureName", 0, 0)
```



## SetAddArea

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chunkSourceComp.ChunkSourceCompServer

- 描述

    设置区块的常加载

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 常加载区域的名称 |
    | dimensionId | int | 区块所在的维度 |
    | minPos | tuple(int,int,int) | 加载区域的最小坐标 |
    | maxPos | tuple(int,int,int) | 加载区域的最大坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - key必须唯一，若添加区域时key已存在将添加失败。
    - 该方式创建的常加载区域不会tick，即实体，方块实体，随机刻都不会进行更新。若需要区域被tick，请使用原版[tickingarea指令](https://minecraft-zh.gamepedia.com/%E5%91%BD%E4%BB%A4/tickingarea)。
    - 将当前未加载的区块设置为常加载区块时，不会从存档加载生物。但如果是当前已加载的区块，则玩家远离区块后，区块内的实体会一直保持加载。
    - 常加载区块内可以使用api创建实体、放置方块、放置结构、修改方块实体数据。
    - 由于区块加载算法的特性，不保证最小到最大坐标的区块完全加载并可用（即CheckChunkState接口返回True），建议将操作位置的四周外延80格的区域都设置为常加载，例如需要在(0,5,0)的位置生成生物/放置方块，需要将(-80,0,-80)到(80,0,80)的区域设置为常加载。
    - 通过本接口添加的区块不被tick时，无法使用fill指令在区块内填充方块

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChunkSource(levelId)
comp.SetAddArea('Area0', 0, (0,0,0), (60,0,60))
```



## SetMergeSpawnItemRadius

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置新生成的物品是否合堆

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | radius | int | 合堆检测半径，范围可设置为0到5，初始为0。若为0代表不合堆，若大于0，则地图中生成一个物品时，会检测这个半径内是否有相同物品，若有且未达到堆叠上限，则不生成新物品，而是使地图上该物品的数量增加。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 备注
    - 该接口主要应用于优化会一次性大量生成掉落物品的场景，使用此方式后生成结果就是一堆物品，不会先生成多个物品再进行合堆检测，可大大减少掉落物品实体数量，大幅提升性能。
    - 该接口不会影响游戏本身的每帧合堆检测逻辑，手中丢弃的物品不受上述合堆逻辑影响。

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
gameComp.SetMergeSpawnItemRadius(5)
```



## SetSpawnDimensionAndPosition

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置世界出生点维度与坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int或None | 维度id |
    | pos | tuple(int,int,int)或None | 出生点坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 同时设置dimensionId与pos时，出生点被设置在对应维度的对应坐标。
        只设置dimensionId，而pos为None时，出生点设置为对应维度，而坐标将通过[基岩版世界生成搜索](https://minecraft.fandom.com/zh/wiki/%E7%94%9F%E6%88%90#.E5.9F.BA.E5.B2.A9.E7.89.88.E4.B8.96.E7.95.8C.E7.94.9F.E6.88.90.E6.90.9C.E7.B4.A2)决定。
        只设置pos，而dimensionId为None，则出生点设置为当前出生维度的对应坐标，与setworldspawn指令相同。
    - 将pos的y轴设置为65535，表示出生到xz坐标轴的最高实心方块上。
    - 当出生维度的类型是地狱和末地时，不会像主世界一样寻找一个安全的位置出生。
    - 关于世界出生点与个人出生点的规则，详见[玩家的生成](https://minecraft.fandom.com/zh/wiki/%E7%94%9F%E6%88%90#.E7.8E.A9.E5.AE.B6.E7.9A.84.E7.94.9F.E6.88.90)

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
# 设置世界出生点到dm3维度的某个坐标
gameComp.SetSpawnDimensionAndPosition(3, (0, 60, 0))
```



## UpgradeMapDimensionVersion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    提升指定地图维度的版本号，版本号不符的维度，地图存档信息将被废弃。使用后存档的地图版本均会同步提升至最新版本，假如希望使用此接口清理指定维度的地图存档，需要在保证该维度区块都没有被加载时调用。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度的数字ID，0代表主世界 |
    | version | int | 维度地图的版本号，取值范围为1-999 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 备注
    - 对于本地游戏来说，由于引擎加载时机比mod早，因此可能出现区块加载比mod加载更早的情况，此时在初始化时使用该接口升级当前维度会出现失效的情况，建议本地游戏中先将玩家移出需要升级的维度，等区块卸载完成（可以使用CheckChunkState判断玩家离开前位置）后再升级该维度。
    - 对于网络服游戏来说，因为服务端加载mod总是比玩家登录要早，因此可以在mod初始化时调用该接口升级指定维度。

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
success = gameComp.UpgradeMapDimensionVersion(0, 10)
```

## 天气

# 天气

## GetDimensionLocalWeatherInfo

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    获取独立维度天气信息(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 独立维度天气信息(下雨强度，下雨时间，打雷强度，打雷时间，是否开启天气循环) |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.GetDimensionLocalWeatherInfo(0)
```



## GetDimensionUseLocalWeather

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    获取某个维度是否拥有自己的天气规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否使用了独立天气规则 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.GetDimensionUseLocalWeather(0)
```



## IsRaining

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    获取是否下雨

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否下雨 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.IsRaining()
```



## IsThunder

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    获取是否打雷

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否打雷 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.IsThunder()
```



## SetDimensionLocalDoWeatherCycle

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置某个维度是否开启天气循环(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否开启天气循环 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetDimensionLocalDoWeatherCycle(0, True)
```



## SetDimensionLocalRain

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置某个维度下雨(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | rainLevel | float | 下雨强度，范围0-1 |
    | rainTime | int | 下雨的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetDimensionLocalRain(0, 0.5, 180)
```



## SetDimensionLocalThunder

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置某个维度打雷(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | thunderLevel | float | 打雷强度，范围0-1 |
    | thunderTime | int | 打雷的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetDimensionLocalThunder(0, 0.5, 180)
```



## SetDimensionUseLocalWeather

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置某个维度拥有自己的天气规则，开启后该维度可以拥有与其他维度不同的天气和天气更替的规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否开启独立天气 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 我们对主世界以及自定义维度新增了“局部天气”的概念。在此之前，所有的维度会共享一个“全局天气”，即设置天气或天气循环规则时，会对所有维度生效。
        现在，我们可以将某个维度使用局部天气规则，并且单独设置它的下雨强度，下雨时间，打雷强度，打雷时间，是否开启天气循环（见[SetDimensionLocalRain](#setdimensionlocalrain)、[SetDimensionLocalThunder](#setdimensionlocalthunder)、[SetDimensionLocalDoWeatherCycle](#setdimensionlocaldoweathercycle)）。
        在下文中，我们会将使用局部天气规则的维度称为“局部维度”，而使用全局天气的维度称为“全局维度”。默认情况下，维度都是全局维度。
        原版的weather指令，接口[SetRaining](#setraining)、[SetThunder](#setthunder)均不会对局部维度产生影响
    - 启用局部天气规则时，默认继承全局的天气强度和时间，局部维度天气循环默认开启
    - 天气规则对原版的下界与末地无效，这两个维度并没有天气系统
    - 建议统一在游戏启动时调用

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetDimensionUseLocalWeather(0, True)
```



## SetRaining

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置是否下雨

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | float | 下雨强度，范围为0-1 |
    | time | int | 天气的持续时间，单位为帧，一秒20帧。持续时间结束后会自动转换为相反的天气。注意，需要在游戏设置中开启天气更替后该参数才会生效。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetRaining(0.5,1000)
```



## SetThunder

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.weatherCompServer.WeatherComponentServer

- 描述

    设置是否打雷

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | level | float | 打雷强度，范围为0-1 |
    | time | int | 打雷持续时间，单位为帧，一秒20帧。注意，需要在游戏设置中开启天气更替后该参数才会生效。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateWeather(levelId)
comp.SetThunder(0.5,1000)set_lightning
```

## 实体管理

# 实体管理

## CreateEngineEntityByTypeStr

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    创建指定identifier的实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | engineTypeStr | str | 实体identifier，例如'minecraft:husk' |
    | pos | tuple(float,float,float) | 生成坐标 |
    | rot | tuple(float,float) | 生物面向 |
    | dimensionId | int | 生成的维度，默认值为0（0为主世界，1为地狱，2为末地） |
    | isNpc | bool | 是否为npc，默认值为False。npc不会移动、转向、存盘。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str或None | 实体Id或者None |

- 备注
    - 在未加载的chunk无法创建
        生成村民请使用"minecraft:villager_v2"

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class MyServerSystem(ServerSystem):
    def createMob(self):
        # 在主世界(0，5，0)的位置创建一个朝向为(0, 0)的尸壳
        entityId = self.CreateEngineEntityByTypeStr('minecraft:husk', (0, 5, 0), (0, 0), 0)
```



## CreateEngineItemEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    用于创建物品实体（即掉落物），返回物品实体的entityId

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | dimensionId | int | 设置dimension，默认为主世界 |
    | pos | tuple(float,float,float) | 生成坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str或None | 实体Id或者None |

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
    'userData': { 'color': { '__type__':8, '__value__':'gray'} },
}
itemEntityId = self.CreateEngineItemEntity(itemDict, 0, (0, 5, 0))
```



## CreateExperienceOrb

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    创建专属经验球

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | exp | int | 经验球经验 |
    | position | tuple(float,float,float) | 创建的位置 |
    | isSpecial | bool | 是否专属经验球 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 设置经验球经验，entityId是人的entityId。专属的经验球只有entityId的人才能拾取

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
comp.CreateExperienceOrb(25,(10,10,10),False)
```



## CreateProjectileEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.projectileCompServer.ProjectileComponentServer

- 描述

    创建抛射物（直接发射）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | spawnerId | str | 创建者Id |
    | entityIdentifier | str | 创建抛射物的identifier，如minecraft:snowball |
    | param | dict | 默认为None，详细说明请见备注 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 创建抛射物的Id，失败时为“-1” |

- 备注
    - param参数解释如下：
        | 参数              | 类型  | 解释                                                         |
        | ----------------- | ----- | ------------------------------------------------------------ |
        | position      | tuple(float,float,float) | 初始位置                                           |
        | direction     | tuple(float,float,float) | 初始朝向                                     |
        | power         | float   | 投掷的力量值            |
        | gravity       | float   | 抛射物重力因子，默认为json配置中的值 |
        | damage        | float   | 抛射物伤害值，默认为json配置中的值               |
        | targetId      | str     | 抛射物目标（指定了target之后，会和潜影贝生物发射的跟踪导弹的那个投掷物是一个效果），默认不指定                                |
        | isDamageOwner | bool    | 对创建者是否造成伤害，默认不造成伤害                                |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateProjectile(levelId)
param = {
    'position': (1,1,1),
    'direction': (1,1,1)
}
comp.CreateProjectileEntity(playerId, "minecraft:snowball", param)
```



## DestroyEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    销毁实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 销毁的实体ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def testDestroyEntity(self, entityId):
        self.DestroyEntity(entityId)
```



## GetDroppedItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取掉落物的物品信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemEntityId | str | 掉落物的entityId |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 信息 |

- 备注
    - 如果掉落物实体不存在，返回值为None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
comp.GetDroppedItem(entityId)
```



## GetEngineActor

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    获取所有实体（不包含玩家）。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 当前地图中的所有实体信息，key：实体id，value：实体dict |

- 备注
    - 实体信息字典 entityDict
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | dimensionId       | int | 维度id |
        | identifier  | str | 实体identifier |

- 示例

```python
import mod.server.extraServerApi as serverApi
entityDicts = serverApi.GetEngineActor()
```



## GetLocalPlayerId

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取本地玩家的id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 客户端玩家Id |

- 示例

```python
import mod.client.extraClientApi as clientApi
localId = clientApi.GetLocalPlayerId()
```



## GetPlayerList

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    获取level中所有玩家的id列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 返回玩家id列表 |

- 备注
    - 由于引擎中的玩家id是无序存储的，所以该接口返回列表的先后顺序没有实际意义，仅为在多平台下表现一致。

- 示例

```python
import mod.server.extraServerApi as serverApi
print serverApi.GetPlayerList()
```



## HasEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    判断 entity 是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0表示不存在，1表示存在 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
exist = comp.HasEntity(entityId)
```



## IsEntityAlive

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    判断生物实体是否存活或非生物实体是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | false表示生物实体已死亡或非生物实体已销毁，true表示生物实体存活或非生物实体存在 |

- 备注
    - 注意，如果检测的实体所在的区块被卸载，则该接口返回False。因此，需要注意实体所在的区块是否被加载。
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://minecraft-zh.gamepedia.com/%E5%8C%BA%E5%9D%97)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
alive = comp.IsEntityAlive(entityId)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    判断生物实体是否存活或非生物实体是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | false表示生物实体已死亡或非生物实体已销毁，true表示生物实体存活或非生物实体存在 |

- 备注
    - 注意，如果检测的实体所在的区块被卸载，则该接口返回False。因此，需要注意实体所在的区块是否被加载。
    - 区块卸载：游戏只会加载玩家周围的区块，玩家移动到别的区域时，原来所在区域的区块会被卸载，参考[区块介绍](https://minecraft-zh.gamepedia.com/%E5%8C%BA%E5%9D%97)

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
alive = comp.IsEntityAlive(entityId)
```



## KillEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    杀死某个Entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 要杀死的目标的entityId |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否杀死成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.KillEntity(entityId)
```



## SpawnItemToLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    生成物品掉落物，如果需要获取物品的entityId，可以调用服务端系统接口CreateEngineItemEntity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | dimensionId | int | 设置dimension |
    | pos | tuple(float,float,float) | 生成位置 |

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
    'userData': {},
}
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
comp.SpawnItemToLevel(itemDict, 0, (0,80,20))
# 当最大生成数量为 1 时，可以继续调用生成 2 个物品
comp.SpawnItemToLevel(itemDict, 0, (0,80,20))
```



## SpawnLootTable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorLootCompServer.ActorLootComponentServer

- 描述

    使用生物类型模拟一次随机掉落，生成的物品与json定义的概率有关

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 掉落位置 |
    | identifier | str | 实体identifier，如minecraft:guardian |
    | playerKillerId | str | 玩家杀手（只能是玩家），默认None |
    | damageCauseEntityId | str | 伤害来源实体Id（掉落与该实体手持物品的抢夺附魔等级有关），默认None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功生成掉落 |

- 备注
    - 需要在对应的player实体附近生成，否则会生成失败。对于某些特殊的生物，如minecraft:sheep，需要使用SpawnLootTableWithActor接口来模拟随机掉落。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateActorLoot(playerId)
result = comp.SpawnLootTable((1, 4, 5), 'minecraft:guardian')
```



## SpawnLootTableWithActor

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorLootCompServer.ActorLootComponentServer

- 描述

    使用生物实例模拟一次随机掉落，生成的物品与json定义的概率有关

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 掉落位置 |
    | entityId | str | 模拟生物的生物Id |
    | playerKillerId | str | 玩家杀手（只能是玩家），默认None |
    | damageCauseEntityId | str | 伤害来源实体Id（掉落与该实体手持物品的抢夺附魔等级有关），默认None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功生成掉落 |

- 备注
    - 需要在对应的player实体附近生成，否则会生成失败

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateActorLoot(playerId)
result = comp.SpawnLootTableWithActor((1, 4, 5), '-335007449086')
```



## SpawnResources

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    产生方块随机掉落（该方法不适用于实体方块）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 方块的identifier，如minecraft:wool |
    | pos | tuple(int,int,int) | 掉落位置 |
    | aux | int | 方块的附加值 |
    | probability | float | 掉落概率，范围为[0, 1]，0为不掉落，1为100%掉落 |
    | bonusLootLevel | int | [时运等级](https://minecraft-zh.gamepedia.com/时运)，默认为0 |
    | dimensionId | int | 掉落方块的维度，默认值为-1，传入非负值时用于获取产生方块掉落的维度；否则将随机挑选一个存在玩家的维度产生掉落 |
    | allowRandomness | bool | 是否允许随机采集，默认为True，如果为False，掉落概率probability无效 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 时运等级[bonusLootLevel]只对部分方块生效
        掉落概率[probability]对部分农作物树叶不生效
    - 可在对应维度的常加载区块产生掉落

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 金矿石掉落
result = comp.SpawnResources('minecraft:gold_ore', (1,1,1), 7, 1.0, 10)
# 指定维度产生掉落
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
result = comp.SpawnResources('minecraft:gold_ore', (1,1,1), 7, 1.0, 10, 0)
```



## SpawnResourcesSilkTouched

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    模拟方块精准采集掉落

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 方块的identifier，如minecraft:wool |
    | pos | tuple(int,int,int) | 掉落位置 |
    | aux | int | 方块的附加值 |
    | dimensionId | int | 掉落方块的维度，默认值为-1，传入非负值时用于获取产生方块掉落的维度；否则将随机挑选一个存在玩家的维度产生掉落 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 如果指定方块不属于精准采集方块，返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
result = comp.SpawnResourcesSilkTouched('minecraft:gold_ore', (1,1,1), 7)
```

## 指令

# 指令

## GetCommandPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.commandCompServer.CommandCompServer

- 描述

    返回设定使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 权限等级：1-OP可以绕过重生点保护；2-OP可以使用所有单人游戏作弊命令；3-OP可以使用大多数多人游戏中独有的命令；4-OP可以使用所有命令 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
opLevel = comp.GetCommandPermissionLevel()
print "GetCommandPermissionLevel oplevel={}".format(opLevel)
```



## GetDefaultPlayerPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.commandCompServer.CommandCompServer

- 描述

    返回新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 权限身份：0-Visitor；1-Member；2-Operator；3-自定义 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
opLevel = comp.GetDefaultPlayerPermissionLevel()
print "GetDefaultPlayerPermissionLevel oplevel={}".format(opLevel)
```



## SetCommand

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.commandCompServer.CommandCompServer

- 描述

    使用游戏内指令

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cmdStr | str | 指令 |
    | playerId | str | 玩家id:可选，如果playerId不设置，则随机选择玩家 |
    | showOutput | bool | 是否输出到聊天窗口：可选，默认False，如果为True的话，指令正确时，才会和聊天框输入原生指令一样输出返回信息。只有当该参数为True的时候会触发OnCommandOutputServerEvent与OnCommandOutputClientEvent |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
comp.SetCommand("/tp @p 100 5 100")#传送指令
```



## SetCommandPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.commandCompServer.CommandCompServer

- 描述

    设置当玩家使用/op命令时OP的权限等级（对应server.properties中的op-permission-level配置）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | opLevel | int | 权限等级：1-OP可以绕过重生点保护；2-OP可以使用所有单人游戏作弊命令；3-OP可以使用大多数多人游戏中独有的命令；4-OP可以使用所有命令 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 备注
    - 此API不会修改已经获取了op的玩家的权限等级，仅影响调用API之后才获取op的玩家，建议在游戏初始化时调用此API

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
opLevel = 4
suc = comp.SetCommandPermissionLevel(opLevel)
print "SetCommandPermissionLevel to {} suc={}".format(opLevel, suc)
```



## SetDefaultPlayerPermissionLevel

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.commandCompServer.CommandCompServer

- 描述

    设置新玩家加入时的权限身份（对应server.properties中的default-player-permission-level配置）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | opLevel | int | 权限身份：0-Visitor；1-Member；2-Operator；3-自定义 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 命令是否执行成功 |

- 备注
    - 此API不会修改已经加入过游戏的玩家的权限身份，仅影响调用API之后才新加入的玩家，建议在游戏初始化时调用此API

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCommand(levelId)
opLevel = 1
suc = comp.SetDefaultPlayerPermissionLevel(opLevel)
print "SetDefaultPlayerPermissionLevel to {} suc={}".format(opLevel, suc)
```

## 方块管理

# 方块管理

## GetBlock

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取某一位置的block

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(str,int) | 参数1:方块的名称，参数2:方块的附加值AuxValue |

- 备注
    - 已经加载的地形才设置、获取方块信息

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetBlock((x,y,z))
```



## GetBlockClip

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取某一位置方块当前<a href="../../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-aabb">clip的aabb</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度,不填时默认为-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块clip的aabb字典 |

- 备注
    - 已经加载的地形才能获取方块信息，支持获取对应维度的常加载区块内方块信息
    - 由于方块的碰撞盒可以随临近方块改变而改变，因此该接口返回的是调用时方块clip的aabb

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockDict = comp.GetBlockClip((0, 5, 0), 0)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取指定位置方块当前clip的aabb

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块aabb字典 |

- 备注
    - 由于方块的碰撞盒可以随临近方块改变而改变，因此该接口返回的是调用时方块clip的aabb

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetBlockClip((x,y,z))
```



## GetBlockCollision

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取某一位置方块当前collision的aabb

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度,不填时默认为-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块aabb字典 |

- 备注
    - 已经加载的地形才能获取方块信息，支持获取对应维度的常加载区块内方块信息
    - 由于方块的碰撞盒可以随临近方块改变而改变，因此该接口返回的是调用时方块collision的aabb

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockDict = comp.GetBlockCollision((0, 5, 0), 0)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取指定位置方块当前collision的aabb

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块aabb字典 |

- 备注
    - 由于方块的碰撞盒可以随临近方块改变而改变，因此该接口返回的是调用时方块collision的aabb

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetBlockCollision((x,y,z))
```



## GetBlockNew

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取某一位置的block

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块信息字典">方块信息字典</a> |

- 备注
    - 已经加载的地形才能获取方块信息，支持获取对应维度的常加载区块内方块信息
    - 对于有多种状态的方块，aux计算比较复杂，推荐使用GetBlockStates获取方块状态字典

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockDict = comp.GetBlockNew((0, 5, 0), 0)
```



## GetDestroyTotalTime

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取使用物品破坏方块需要的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，格式[namespace:name:auxvalue]，auxvalue默认为0 |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，默认为None（不使用物品） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 需要消耗的时间 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetDestroyTotalTime("minecraft:diamond_block", "minecraft:stone_pickaxe")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取使用物品破坏方块需要的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，格式[namespace:name:auxvalue]，auxvalue默认为0 |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，默认为None（不使用物品） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 需要消耗的时间 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetDestroyTotalTime("minecraft:diamond_block", "minecraft:stone_pickaxe")
```



## GetLiquidBlock

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取某个位置方块所含流体信息接口

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块信息字典">方块信息字典</a> |

- 备注
    - 已经加载的地形才能获取方块信息，支持获取对应维度的常加载区块内方块信息
    - 对于不含水或者不是流体的方块，则返回None。对于一个含水的方块，如含水的橡木栅栏，GetLiquidBlock会返回其含有的流体的信息(包括自定义流体)，GetBlockNew则会返回橡木栅栏的信息。而对于一般的水方块(包括自定义流体)，GetLiquidBlock和GetBlockNew则都会返回水的信息(包括自定义流体)。因此可以用GetLiquidBlock和GetBlockNew判断某个方块是否流体

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
liquidBlockDict = comp.GetLiquidBlock((0, 5, 0), 0)
```



## GetTopBlockHeight

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取某一位置最高的非空气方块的高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int) | x轴与z轴位置 |
    | dimension | int | 维度id，默认为0，可在获取常加载区块内最高非空气方块高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 高度。若区块未加载返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
height = comp.GetTopBlockHeight((5, 5), 0)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取当前维度某一位置最高的非空气方块的高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int) | x轴与z轴位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 高度。若区块未加载返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
height = comp.GetTopBlockHeight((5, 5))
```



## SetBlockNew

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置某一位置的方块

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | blockDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块信息字典">方块信息字典</a> |
    | oldBlockHandling | int | 0：替换，1：销毁，2：保留，默认为0 |
    | dimensionId | int | 方块所在维度，必需参数 |
    | isLegacy | bool | 是否设置为传统的aux，建议设置为True，即aux对应的state不随着版本迭代而变化。默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 已经加载的地形才能设置方块，支持在对应维度的常加载区块内设置方块
    - **若使用SetBlockNew接口替换含方块实体的方块，除自定义方块实体外，当替换前后方块实体类型相同时，其方块实体内数据不会发生改变。**
        例如在箱子中放置了物品，使用SetBlockNew接口将箱子方块替换为箱子方块后，新的箱子中依然保留旧箱子内的物品。<br>
        要避免这种情况，中间添加一次不同方块实体类型（或不含方块实体）的方块替换即可。比如先将箱子替换为空气，再将空气替换为箱子。
    - 随着版本更新，aux值对应的方块state会发生改变，对于有多种状态的方块，aux计算方式比较复杂，推荐先通过GetBlockAuxValueFromStates获取传统aux值再进行设置。

- 示例

```python
import mod.server.extraServerApi as serverApi

comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
# GetBlockAuxValueFromStates 只需要调用一次，得到的auxValue可以缓存以来以供后续使用
auxValue = comp.GetBlockAuxValueFromStates("minecraft:wool", { 'color': 'orange' })

blockDict = {
    'name': 'minecraft:wool',
    'aux': auxValue
}
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.SetBlockNew((0, 5, 0), blockDict, 0, 0, True)
```



## SetLiquidBlock

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置某一位置的方块的extraBlock，可在此设置方块含水等

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | blockDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块信息字典">方块信息字典</a> |
    | dimensionId | int | 方块所在维度，必需参数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 已经加载的地形才能设置方块，支持在对应维度的常加载区块内设置方块
    - dimensionId需要是playerId对应玩家所在的维度；如果dimensionId是-1则默认使用playerId对应玩家所在的维度

- 示例

```python
import mod.server.extraServerApi as serverApi
blockDict = {
    'name': 'minecraft:water',
    'aux': 5
}
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
comp.SetLiquidBlock((0, 5, 0), blockDict, 0)
```



## SetSnowBlock

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置某一位置的方块含雪

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块位置 |
    | dimensionId | int | 方块所在维度，必需参数 |
    | height | int | 雪块的高度，默认是1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 已经加载的地形才能设置方块，支持在对应维度的常加载区块内设置方块
    - dimensionId需要是playerId对应玩家所在的维度；如果dimensionId是-1则默认使用playerId对应玩家所在的维度

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
comp.SetSnowBlock((0, 5, 0), 0, 1)
```

## 方块组合

# 方块组合

## CreateMicroBlockResStr

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    生成微缩方块资源Json字符串

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 微缩方块唯一标识 |
    | start | tuple(int,int,int) | 微缩起始坐标 |
    | end | tuple(int,int,int) | 微缩结束坐标 |
    | colorMap | dict | 默认为None，微缩方块颜色对应表 |
    | isMerge | bool | 默认为False，是否合并同类型方块 |
    | icon | str | 默认为空字符串，微缩方块图标，需要定义在 terrain_texture.json 中 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生成的微缩方块的资源字符串 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
result = comp.CreateMicroBlockResStr("x", (12, 60, 12), (26, 76, 26), colorMap={'minecraft:grass': [12, 22, 123, 255]}, isMerge=True, icon="micro_block_datiangou")
with open("micro_block_x.json", "w+") as f:
    f.write(result)
#该例子中，方块将以 (12 60 12) 为起点，以 (26 76 26) 为终点进行微缩，最终微缩方块里所有草方块的颜色为 rgba(12,22,123,255)，实际显示颜色会依据环境光照微调，物品栏里的图标为 terrain_texture.json 里 micro_block_datiangou 对应的图片。
```



## GetBlankBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    获取一个空白的方块调色板。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如获取失败则返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
blankPalette = comp.GetBlankBlockPalette()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockCompClient.BlockCompClient

- 描述

    获取一个空白的方块调色板。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如获取失败则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
blankPalette = comp.GetBlankBlockPalette()
```



## GetBlockPaletteBetweenPos

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    根据输入的两个方块位置创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 方块所在维度 |
    | startBlockPos | tuple(int,int,int) | 起始方块位置 |
    | endBlockPos | tuple(int,int,int) | 终点方块位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 对于床方块，方块调色板获取床方块时，只会添加床头的方块，床尾方块会进行忽略。对于门方块，则只会添加门的下半部分的方块，门的上半部分会进行忽略。

- 示例

```python
import mod.server.extraServerApi as serverApi
# playerId可以为None，也可以传入玩家的id。当传入的dimensionId为0或正值时，依赖dimensionId来获取区域；当传入的dimensionId为负值时，依赖传入的playerId来获取区域。
comp = serverApi.GetEngineCompFactory().CreateBlock(entityId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockCompClient.BlockCompClient

- 描述

    根据输入的两个位置创建并获取一个方块调色板，该接口会搜索这两个位置之间的所有方块创建方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。这个方块调色板包含了这两个位置之间的所有方块及其相对位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | startPos | tuple(int,int,int) | 起始位置 |
    | endPos | tuple(int,int,int) | 终点位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 对于床方块，方块调色板获取床方块时，只会添加床头的方块，床尾方块会进行忽略。对于门方块，则只会添加门的下半部分的方块，门的上半部分会进行忽略。
    - 需要等区域内的方块完全加载才能正确获取调色板

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
```



## GetBlockPaletteFromPosList

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 方块所在维度 |
    | posList | list(tuple(int,int,int)) | 方块位置列表 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 对于床方块，方块调色板获取床方块时，只会添加床头的方块，床尾方块会进行忽略。对于门方块，则只会添加门的下半部分的方块，门的上半部分会进行忽略。

- 示例

```python
import mod.server.extraServerApi as serverApi
# playerId可以为None，也可以传入玩家的id。当传入的dimensionId为0或正值时，依赖dimensionId来获取区域；当传入的dimensionId为负值时，依赖传入的playerId来获取区域。
comp = serverApi.GetEngineCompFactory().CreateBlock(entityId)
palette = comp.GetBlockPaletteFromPosList(0,
[(200,64,200),
(201,64,200)
(202,64,200)
])
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.blockCompClient.BlockCompClient

- 描述

    根据输入的方块位置列表创建并获取一个方块调色板，方块调色板用于描述和记录世界中的多个方块的组合。创建的方块调色板包含了这个位置列表中的所有方块及其相对位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posList | list(tuple(int,int,int)) | 方块位置列表 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 对于床方块，方块调色板获取床方块时，只会添加床头的方块，床尾方块会进行忽略。对于门方块，则只会添加门的下半部分的方块，门的上半部分会进行忽略。
    - 需要等列表内的方块完全加载才能正确获取调色板

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteFromPosList([
(200,64,200),
(201,64,200)
(202,64,200)
])
```



## RegisterBlockPatterns

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    注册特殊方块组合

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pattern | list(str) | 方块组合位置 |
    | defines | dict | 方块组合类型 |
    | result_actor_name | str | 合成结果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该pattern不限定方向，只要能在任一平面上组合成功就能合成对应的实体。
    - 如示例代码所示，不需要放方块的位置需要显式定义为空气方块
    - 当引擎中已注册过相同的pattern和defines时，该接口不会更新result_actor_name，并返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
pattern = [
    'A#A',
    'XXX',
    'AXA'
    ]
defines ={
    '#': 'minecraft:gold_block',
    'X': 'minecraft:iron_block',
    'A': 'minecraft:air',
}
comp.RegisterBlockPatterns(pattern,defines,'minecraft:chicken')
#该例子左中右下放铁块，上面放金块，会生成一只鸡
```



## SetBlockByBlockPalette

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockCompServer.BlockCompServer

- 描述

    根据输入的方块调色板内容，将调色板内记录的所有方块设置为实际的方块。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockPalette | BlockPaletteComponent | 方块调色板，由GetBlockPaletteBetweenPos以及GetBlockPaletteFromPosList接口获取 |
    | dimensionId | int | 方块所在维度。如果输入的数值小于0，则使用entityId获取设置方块的区块。 |
    | pos | tuple(int,int,int) | 设置方块的原点位置，将以这个位置作为原点设置方块 |
    | rotation | int | 方块组合体的旋转，旋转方向为绕设置方块的原点位置所在的y轴进行旋转，旋转角度仅支持-270,-180,-90,0,90,180,270。如果传入的不是这些值，将取其中最接近输入值的数值。 |
    | conflictMode | int | 冲突模式枚举，可选参数，默认为0。在生成过程中，遇到生成的位置有其他方块的情况时，那么将会根据冲突模式来进行处理。可以输入的值为:0,1,2, 分别代表: 0: 替换地图中的方块，1: 跳过这个方块，2: 放弃之后的生成过程。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 生成过程是否成功，无法完成整个生成过程返回False，完成整个生成过程则返回True。如果冲突模式为2时，遇到冲突方块时放弃之后的生成过程，这时候接口也会返回False。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(entityId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
# 将方块以(205,64,200)为原点设置palette中的方块，旋转90度，冲突模式为0，即替代地图中的方块
comp.SetBlockByBlockPalette(palette, 0, (205,64,200),90,0)
```

## 时间

# 时间

## GetLocalDoDayNightCycle

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    获取维度是否打开昼夜更替

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否打开昼夜更替 |

- 备注
    - 维度使用局部时间规则时，返回维度自身的昼夜更替规则；没有使用时返回全局的昼夜更替规则
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.GetLocalDoDayNightCycle(3)
```



## GetLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    获取维度的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 备注
    - 维度使用局部时间规则时，返回局部时间；没有使用时返回全局时间
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
# 从游戏开始经过的总帧数
passedTime = comp.GetLocalTime(3)
# 当前游戏天内的帧数
timeOfDay = passedTime % 24000
# 从游戏开始经过的游戏天数
day = passedTime / 24000
```



## GetTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.timeCompServer.TimeComponentServer

- 描述

    获取当前世界时间

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 当前时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
# 从游戏开始经过的总帧数
passedTime = comp.GetTime()
# 当前游戏天内的帧数
timeOfDay = passedTime % 24000
# 从游戏开始经过的游戏天数
day = passedTime / 24000
```



## GetUseLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    获取某个维度是否设置了使用局部时间规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否使用局部时间规则 |

- 备注
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.GetUseLocalTime(3)
```



## SetLocalDoDayNightCycle

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    设置使用局部时间规则的维度是否打开昼夜更替

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否打开昼夜更替 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 只有使用局部时间规则维度才能设置
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)
    - 在pc开发包下，可以在聊天栏键入`dmtime cycle on`或`dmtime cycle off`来测试开启与关闭当前维度的昼夜更替

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.SetLocalDoDayNightCycle(3, False)
```



## SetLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    设置使用局部时间规则维度的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | time | int | 时间，单位为帧数。表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 游戏有天数的概念，使用时需要进行考虑。您也可以直接使用[SetLocalTimeOfDay](#setlocaltimeofday)设置一天内所在的时间而不用计算天数。
    - 只有使用局部时间规则维度才能设置
    - 关于“局部时间规则”，见[SetUseLocalTime](#setuselocaltime)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
# 获取当前的时间
passedTime = comp.GetLocalTime(3)
# 获取当前的天数
day = passedTime / 24000
# 设置为当天的正午
comp.SetLocalTime(3, day * 24000 + 6000)
# 设置为次日的日出
comp.SetLocalTime(3, (day + 1) * 24000 + 0)
```



## SetLocalTimeOfDay

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    设置使用局部时间规则维度在一天内所在的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | timeOfDay | int | 时间，单位为帧数，表示游戏天内的时间，范围为0到24000。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 具体的逻辑与time指令相同，若timeOfDay比当前时间晚，则设置到当天的timeOfDay；若timeOfDay比当前时间早，则设置到次日的timeOfDay
    - 在pc开发包下，可以在聊天栏键入`dmtime time <int:帧数>`来测试设置当前维度的局部时间

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
# 设置为正午
comp.SetLocalTimeOfDay(3, 6000)
```



## SetTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.timeCompServer.TimeComponentServer

- 描述

    设置当前世界时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | time | int | 时间，单位为帧数，表示该存档从新建起经过的时间，而非当前游戏天内的时间。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 游戏有天数的概念，使用时需要进行考虑。您也可以直接使用[SetTimeOfDay](#settimeofday)设置一天内所在的时间而不用计算天数。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
# 获取当前的时间
passedTime = comp.GetTime()
# 获取当前的天数
day = passedTime / 24000
# 设置为当天的正午
comp.SetTime(day * 24000 + 6000)
# 设置为次日的日出
comp.SetTime((day + 1) * 24000 + 0)
```



## SetTimeOfDay

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.timeCompServer.TimeComponentServer

- 描述

    设置当前世界在一天内所在的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timeOfDay | int | 时间，单位为帧数，表示游戏天内的时间，范围为0到24000。mc中一个游戏天相当于现实的20分钟，即24000帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 具体的逻辑与time指令相同，若timeOfDay比当前时间晚，则设置到当天的timeOfDay；若timeOfDay比当前时间早，则设置到次日的timeOfDay

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTime(levelId)
# 设置为正午
comp.SetTimeOfDay(6000)
```



## SetUseLocalTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度id |
    | value | bool | 是否开启局部时间规则 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 我们对主世界以及自定义维度新增了“局部时间规则”的概念。在此之前，所有的维度会共享一个“全局时间”，即设置时间或dodaynightcycle规则时，会对所有维度生效。
        现在，我们可以将某个维度使用局部时间规则，并且单独设置他的时间（见[SetLocalTime](#setlocaltime)）与dodaynightcycle规则（见[SetLocalDoDayNightCycle](#setlocaldodaynightcycle)）。
        在下文中，我们会将使用局部时间规则的维度称为“局部维度”，而使用全局时间的维度称为“全局维度”。默认情况下，维度都是全局维度。
        原版的time指令，gamerule dodaylightcycle指令与开启昼夜更替的设置，daylock指令与终为白日的设置，均不会对局部维度生效。
        当世界上同时存在局部维度与全局维度时，只有以下两种情况可以睡觉来跳过黑夜：
        1. 所有玩家都在全局维度睡觉。这时会将全局时间跳到第二天早上。
        2. 所有玩家都在同一个局部维度睡觉。这时会将该局部维度的时间跳到第二天早上。
    - 启用局部时间规则时，默认继承全局的时间与昼夜更替规则
    - 时间规则对原版的下界与末地无效，这两个维度永远为黑夜且没有昼夜更替
    - 建议统一在游戏启动时调用
    - 在pc开发包下，可以在聊天栏键入`dmtime on`或`dmtime off`来测试开启与关闭当前维度的局部时间

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(levelId)
comp.SetUseLocalTime(3, True)
```

## 消息

# 消息

## NotifyOneMessage

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.msgCompServer.MsgComponentServer

- 描述

    给指定玩家发送聊天框消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 指定玩家id |
    | msg | str | 消息内容 |
    | color | str | 颜色样式代码字符串，可参考wiki[样式代码](https://minecraft-zh.gamepedia.com/%E6%A0%B7%E5%BC%8F%E4%BB%A3%E7%A0%81)，默认为白色 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateMsg(entityId)
comp.NotifyOneMessage(playerId, "test", "§c")
```



## SendMsg

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.msgCompServer.MsgComponentServer

- 描述

    模拟玩家给所有人发送聊天栏消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 发送者玩家的名字 |
    | msg | str | 消息内容 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - name参数需要设置玩家的名字(可通过name组件获取)，如果设置的玩家名字不存在，则随机找一个玩家发出该消息

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateMsg(entityId)
comp.SendMsg("playerName","test")
```



## SendMsgToPlayer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.msgCompServer.MsgComponentServer

- 描述

    模拟玩家给另一个玩家发送聊天栏消息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fromEntityId | str | 发送者玩家ID |
    | toEntityId | str | 接受者玩家ID |
    | msg | str | 消息内容 |

- 返回值

    无

- 示例

```python
comp = serverApi.GetEngineCompFactory().CreateMsg(entityId)
comp.SendMsgToPlayer(fromEntityId, toEntityId, "test")
```



## SetLeftCornerNotify

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textNotifyCompClient.TextNotifyComponet

- 描述

    客户端设置左上角通知信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | textMsg | str | 通知内容 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextNotifyClient(levelId)
comp.SetLeftCornerNotify("做好准备")
```



## SetNotifyMsg

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置消息通知

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | msg | str | 消息内容 |
    | color | str | 使用GenerateColor接口获取的颜色，默认为白色 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetNotifyMsg("消息通知", serverApi.GenerateColor('BLUE'))
```



## SetOnePopupNotice

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    在具体某个玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方，此功能更建议客户端使用game组件的对应接口SetPopupNotice

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 具体玩家Id |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |
    | subtitle | str | 消息子标题内容,效果同message，也可设置颜色，位置位于message上方 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
# playerId 变量改为具体的玩家Id
comp.SetOnePopupNotice(playerId, serverApi.GenerateColor("RED") + "消息通知", "消息子标题")
```



## SetOneTipMessage

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    在具体某个玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方，此功能更建议在客户端使用game组件的对应接口SetTipMessage

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 具体玩家Id |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
# playerId 变量改为具体的玩家Id
comp.SetOneTipMessage(playerId, serverApi.GenerateColor("RED") + "tip提示")
```



## SetPopupNotice

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    在所有玩家物品栏上方弹出popup类型通知，位置位于tip类型消息下方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |
    | subtitle | str | 消息子标题内容,效果同message，也可设置颜色，位置位于message上方 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetPopupNotice(serverApi.GenerateColor("RED") + "消息通知", "消息子标题")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    在本地玩家的物品栏上方弹出popup类型通知，位置位于tip类型消息下方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraClientApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |
    | subtitle | str | 消息子标题内容,效果同message，也可设置颜色，位置位于message上方 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(entityId)
comp.SetPopupNotice(clientApi.GenerateColor("RED") + "消息通知", "消息子标题")
```



## SetTipMessage

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    在所有玩家物品栏上方弹出tip类型通知，位置位于popup类型通知上方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraServerApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetTipMessage(serverApi.GenerateColor("RED") + "tip提示")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    在本地玩家的物品栏上方弹出tip类型通知，位置位于popup类型通知上方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | message | str | 消息内容,可以在消息前增加extraClientApi.GenerateColor("RED")字符来设置颜色，具体参考样例 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(entityId)
comp.SetTipMessage(clientApi.GenerateColor("RED") + "tip提示")
```

## 渲染

# 渲染

## GetAmbientBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取环境光亮度，影响天空亮度，不影响实体与方块光照

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 范围0到1之间 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
ambineBrightness = comp.GetAmbientBrightness()
```



## GetFogColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    获取当前雾效颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float,float) | 颜色rgba |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
# 获取雾效颜色
fogColor = comp.GetFogColor()
```



## GetFogLength

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    获取雾效范围

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 雾效起始值与终点值 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
start,end = comp.GetFogLength()
```



## GetMoonRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取月亮角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 第一个float表示南北偏移，第二个float表示月亮的自旋角度，第三个float表示月升月落。单位为角度 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
rot = comp.GetMoonRot()
```



## GetSkyColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取天空颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float,float) | 颜色RGBA，0到1之间，目前a值暂时没用 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
color = comp.GetSkyColor()
```



## GetSkyTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取当前维度天空盒贴图，天空盒共6张贴图

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str)或None | 天空盒贴图列表，该值可能为None |

- 示例

```python
# 贴图列表按顺序分别对应世界坐标的 负Z轴方向， 正X轴方向，正Z轴方向，负X轴方向，正Y轴方向，负Y轴方向。 其中正Y轴即为上方（采用右手坐标系）。
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
textureList = comp.GetSkyTextures()
```



## GetStarBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取星星亮度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 范围0到1之间 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
starBrightness = comp.GetStarBrightness()
```



## GetSunRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    获取太阳角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 第一个float表示南北偏移，第二个float表示太阳的自旋角度，第三个float表示日升日落。单位为角度 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
rot = comp.GetSunRot()
```



## GetUseAmbientBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    判断是否在mod设置了环境光亮度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
useAmbientBrightness = comp.GetUseAmbientBrightness()
```



## GetUseFogColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    判断当前是否开启设置雾效颜色，该值默认为False，使用mod传入的颜色值后为True

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
# 获取是否开启设置雾效颜色
useFogColor = comp.GetUseFogColor()
```



## GetUseFogLength

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    判断当前是否开启设置雾效范围,该值默认为False，使用mod传入的范围值后为True

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
# 获取是否开启设置雾效范围
useFogLength = comp.GetUseFogLength()
```



## GetUseMoonRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    判断是否在mod设置了月亮角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
useMoonRot = comp.GetUseMoonRot()
```



## GetUseSkyColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    判断是否在mod设置了天空颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
useSkyColor = comp.GetUseSkyColor()
```



## GetUseStarBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    判断是否在mod设置了星星亮度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
useStarBrightness = comp.GetUseStarBrightness()
```



## GetUseSunRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    判断是否在mod设置了太阳角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
useSunRot = comp.GetUseSunRot()
```



## HideNameTag

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    隐藏场景内所有名字显示，包括玩家名字，生物的自定义名称，物品展示框与命令方块的悬浮文本等

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isHide | bool | 是否隐藏，True为隐藏，False为显示 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.HideNameTag(True)
```



## ResetAmbientBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置环境光亮度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetAmbientBrightness()
```



## ResetFogColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    重置雾效颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
comp.ResetFogColor()
```



## ResetFogLength

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    重置雾效范围

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
comp.ResetFogLength()
```



## ResetMoonRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置月亮角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetMoonRot()
```



## ResetSkyColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置天空颜色

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetSkyColor()
```



## ResetSkyTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置当前维度天空盒贴图。如果有使用addon配置贴图则会使用配置的贴图，否则为游戏内默认无贴图的情况

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetSkyTextures()
```



## ResetStarBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置星星亮度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetStarBrightness()
```



## ResetSunRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    重置太阳角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.ResetSunRot()
```



## SetAmbientBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置环境光亮度，影响天空亮度，不影响实体与方块光照

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | brightness | float | 范围0到1之间 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetAmbientBrightness(0.1)
```



## SetFogColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    设置雾效颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float,float) | 颜色RGBA，范围0到1之间，a值主要用于水下效果 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
# 雾效设置为全白色
comp.SetFogColor((1.0,1.0,1.0,1.0))
```



## SetFogLength

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.fogCompClient.FogCompClient

- 描述

    设置雾效范围

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | start | float | 雾效起始距离 |
    | end | float | 雾效终点范围 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFog(levelId)
comp.SetFogLength(10, 50)
```



## SetMoonRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置月亮所在角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float,float) | 第一个float表示南北偏移，第二个float表示月亮的自旋角度，第三个float表示月升月落。单位为角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetMoonRot((10, 0, 10))
```



## SetSkyColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置天空颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float,float) | 颜色RGBA，0到1之间，目前a值暂时没用 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetSkyColor((0.5, 0.5, 0.8, 1.0))
```



## SetSkyTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置当前维度天空盒贴图，天空盒需要6张贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | textureList | list(str) | 需要为6张贴图的路径，路径为从textures目录开始的绝对路径，如果天空盒某个方向不需要设置，则传空字符串 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 游戏内切dimension的时候会重设天空盒贴图，因此开发者需要监听对应的切换维度完成事件(DimensionChangeFinishClientEvent)进行贴图的处理。

- 示例

```python
# 贴图列表按顺序分别对应世界坐标的 负Z轴方向， 正X轴方向，正Z轴方向，负X轴方向，正Y轴方向，负Y轴方向。 其中正Y轴即为上方（采用右手坐标系）。
textureList = ['', 'textures/environment/positiveX','textures/environment/positiveZ', '', 'textures/environment/positiveY', '']
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetSkyTextures(textureList)
```



## SetStarBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置星星亮度，白天也可以显示星星

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | brightness | float | 范围0到1之间 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetStarBrightness(0.1)
```



## SetSunRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    设置太阳所在角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float,float) | 第一个float表示南北偏移，第二个float表示太阳的自旋角度，第三个float表示日升日落。单位为角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateSkyRender(levelId)
comp.SetSunRot((10, 0, 10))
```



## SkyTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.skyRenderCompClient.SkyRenderCompClient

- 描述

    修改太阳、月亮、云层分布、天空盒的贴图。使用addon配置，非python接口。

- 参数

    无

- 返回值

    无

- 备注
    - 游戏提供了重载贴图的方式来修改太阳、月亮、云层分布、天空盒的贴图。
        **末地和下界没有太阳月亮和云层，另外末地的天空是用一张贴图end_sky.png而不是天空盒贴图，end_sky.png要结合雾效颜色使用。下界暂不支持此功能**。
        具体路径为：
        | 贴图         | 路径                                                         |
        | ------------ | ------------------------------------------------------------ |
        | 太阳贴图     | modResource目录/textures/environment/{dimName}_sun.png       |
        | 月亮贴图     | modResource目录/textures/environment/{dimName}_moon_phases.png |
        | 云层分布贴图 | modResource目录/textures/environment/{dimName}_clouds.png    |
        | 天空盒贴图   | modResource目录/textures/environment/{dimName}_cubemap/cubemap_0.png |
        
        其中：天空盒贴图需要放6张图，即最后需要包含```cubemap_0.png```到```cubemap_5.png```，而```{dimName}```表示dimension的名称，各个dimension名称如下：
        | dimension                   | 名称            |
        | --------------------------- | --------------- |
        | 末地                        | theend          |
        | 下界                        | nether          |
        | 上界                        | overworld       |
        | 其他复制出来的dimension镜像 | 从3到20的数字id |
        
        示例：
        ```json
        modResource/textures/environment/4_sun.png
        modResource/textures/environment/overworld_moon_phases.png
        modResource/textures/environment/3_clouds.png
        modResource/textures/environment/overworld_cubemap/cubemap_0.png # -z方向
        modResource/textures/environment/overworld_cubemap/cubemap_1.png #  x方向
        modResource/textures/environment/overworld_cubemap/cubemap_2.png #  z方向
        modResource/textures/environment/overworld_cubemap/cubemap_3.png # -x方向
        modResource/textures/environment/overworld_cubemap/cubemap_4.png #  y方向
        modResource/textures/environment/overworld_cubemap/cubemap_5.png # -y方向
        modResource/textures/environment/end_sky.png #末地天空渲染贴图
        ```

## 游戏规则

# 游戏规则

## AddBannedItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemBannedCompServer.ItemBannedCompServer

- 描述

    增加禁用物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。例如：minecraft:egg（也可以通过填写配置文件config/banned_items.json进行启动禁用） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否增加成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
comp.AddBannedItem("minecraft:egg")
```



## AddBlockProtectField

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置一个方块无法被玩家/实体破坏的区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 不可破坏区域所在维度 |
    | startPos | tuple(int,int,int) | 初始位置，不可破坏区域AABB包围盒的最小点 |
    | endPos | tuple(int,int,int) | 结束位置，不可破坏区域AABB包围盒的最大点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 成功时返回区域的唯一ID，可用于取消不可破坏区域，失败时返回-1 |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
field = gameComp.AddBlockProtectField(0, (-20, 0, -20), (20, 255, 20))
if field > 0:
    print "AddBlockProtectField success field={}".format(field)
else:
    print "AddBlockProtectField fail"
```



## CleanBlockProtectField

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    取消全部已设置的方块无法被玩家/实体破坏的区域

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为取消成功，False为取消失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
suc = gameComp.CleanBlockProtectField()
print "CleanBlockProtectField suc={}".format(suc)
```



## ClearBannedItems

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemBannedCompServer.ItemBannedCompServer

- 描述

    清空禁用物品

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否清空成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
comp.ClearBannedItems()
```



## DisableVineBlockSpread

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置是否禁用藤曼蔓延生长

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | disable | bool | True:禁用 False:非禁用 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.DisableBineBlockSpread(disable)
```



## ForbidLiquidFlow

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    禁止/允许地图中的流体流动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | forbid | bool | True为禁止流体流动 False为允许流体流动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 备注
    - 禁止流动后的流体，在重新允许流动之后，不会立刻向四周流动，直到受到方块更新（如相邻的方块发生改变）

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
success = gameComp.ForbidLiquidFlow(True)
```



## GetBannedItemList

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemBannedCompServer.ItemBannedCompServer

- 描述

    获取禁用物品列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str)或None | 禁用物品列表或者None(异常情况),list元素为物品标识符,格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
comp.GetBannedItemList()
```



## GetGameDiffculty

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取游戏难度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | GetMinecraftEnum().GameDiffculty.*:Peaceful，Easy，Normal，Hard分别为0~3 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
diffculty = comp.GetGameDiffculty()
```



## GetGameRulesInfoServer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取游戏规则

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 游戏规则字典 |

- 备注
    - 游戏规则字典 gameRule见代码注释

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
type = comp.GetGameRulesInfoServer()
#返回值如下
{
'option_info': {
    'pvp': bool,
    'show_coordinates': bool,
    'fire_spreads': bool,
    'tnt_explodes': bool,
    'mob_loot': bool,
    'natural_regeneration': bool,
    'tile_drops': bool,
    'experimental_gameplay': bool,
    },
'cheat_info': {
    'enable': bool,
    'always_day': bool,
    'mob_griefing': bool,
    'keep_inventory': bool,
    'weather_cycle': bool,
    'mob_spawn': bool,
    'entities_drop_loot': bool,
    'daylight_cycle': bool,
    'command_blocks_enabled': bool,
    'random_tick_speed': int,
    }
}
```



## GetGameType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取默认游戏模式

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | GetMinecraftEnum().GameType.*:Survival，Creative，Adventure分别为0~2 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
type = comp.GetGameType()
```



## GetLevelGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取重力因子

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 重力因子 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.GetLevelGravity()
```



## GetSeed

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取存档种子

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 存档种子 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
seed = comp.GetSeed()
```



## IsDisableCommandMinecart

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取当前是否允许运行命令方块矿车内置逻辑指令，当前仅Apollo网络服可用

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True：当前禁止运行命令方块矿车内置逻辑指令；False：当前允许运行命令方块矿车内置逻辑指令 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
isDisable = comp.IsDisableCommandMinecart()
```



## IsLockDifficulty

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取当前世界的游戏难度是否被锁定

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | isLock True为已锁定，False为未锁定 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
isLock = comp.IsLockDifficulty()
```



## LockDifficulty

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    锁定当前世界游戏难度（仅本次游戏有效），锁定后任何玩家在游戏内都无法通过指令或暂停菜单修改游戏难度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | lock | bool | True:锁定 False:解锁 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | result是否操作成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.LockDifficulty(True)
```



## OpenCityProtect

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    开启城市保护，包括禁止破坏方块，禁止对方块使用物品，禁止怪物攻击玩家，禁止玩家之间互相攻击，禁止日夜切换，禁止天气变化，禁止怪物群落刷新

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
success = gameComp.OpenCityProtect()
```



## RemoveBannedItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemBannedCompServer.ItemBannedCompServer

- 描述

    移除禁用物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemName | str | 物品标识符，格式[namespace:name:auxvalue]，auxvalue默认为0，auxvalue为*时候匹配任意auxvalue值。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否移除成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItemBanned(levelId)
comp.RemoveBannedItem("minecraft:stained_glass:2")
```



## RemoveBlockProtectField

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    取消一个方块无法被玩家/实体破坏的区域

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | field | int | 不可破坏区域的唯一ID，AddBlockProtectField的返回值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为取消成功，False为取消失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
field = gameComp.AddBlockProtectField(0, (-20, 0, -20), (20, 255, 20))
if field > 0:
    print "AddBlockProtectField success field={}".format(field)
    suc = gameComp.RemoveBlockProtectField(field)
    print "RemoveBlockProtectField field={} suc={}".format(field, suc)
```



## SetCanActorSetOnFireByLightning

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    禁止/允许闪电点燃实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | True为允许闪电点燃实体 False为禁止闪电点燃实体 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
success = gameComp.SetCanActorSetOnFireByLightning(False)
```



## SetCanBlockSetOnFireByLightning

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    禁止/允许闪电点燃方块

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | True为允许闪电点燃方块 False为禁止闪电点燃方块 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | success True为设置成功，False为设置失败 |

- 备注
    - 只有当游戏难度为普通及以上，并且开启了火焰蔓延，闪电才会点燃方块

- 示例

```python
import mod.server.extraServerApi as serverApi
gameComp = serverApi.GetEngineCompFactory().CreateGame(levelId)
success = gameComp.SetCanBlockSetOnFireByLightning(False)
```



## SetDefaultGameType

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置默认游戏模式

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
comp = serverApi.GetEngineCompFactory().CreateGame(playerId)
# 设置创造模式为默认游戏模式
comp.SetDefaultGameType(1)
```



## SetDisableCommandMinecart

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置停止/开启运行命令方块矿车内置逻辑指令，当前仅Apollo网络服可用

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | True：停止运行命令方块矿车内置逻辑指令；False：开启运行命令方块矿车内置逻辑指令 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
suc = comp.SetDisableCommandMinecart(True)
```



## SetDisableContainers

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    禁止所有容器界面的打开，包括玩家背包，各种包含背包界面的容器方块如工作台与箱子，以及包含背包界面的实体交互如马背包与村民交易

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | 是否禁止容器界面 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
comp.SetDisableContainers(True)
```



## SetDisableDropItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置禁止丢弃物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | 是否禁止丢弃物品 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
# 1、开启开关后，玩家死亡会所有物品消失；如需保证物品不掉落，可以配合/gamerule keepInventory true 使用
# 2、创造模式下物品依然能丢弃。
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
comp.SetDisableDropItem(True)
```



## SetDisableGravityInLiquid

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    是否屏蔽所有实体在液体（水、岩浆）中的重力

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | True:屏蔽 False:取消屏蔽 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 设置屏蔽实体在液体中的重力后，实体将不能上浮也不能下潜。**对玩家而言，当水/岩浆淹没腰部及以上时（约在水面/岩浆表面0.7格及以下），将无法上岸。**

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetDisableGravityInLiquid(True)
```



## SetDisableHunger

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置是否屏蔽饥饿度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isDisable | bool | 是否屏蔽饥饿度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如需隐藏饥饿度请使用extraClientApi的HideHungerGui

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(entityId)
comp.SetDisableHunger(True)
```



## SetGameDifficulty

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置游戏难度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | difficulty | int | GetMinecraftEnum().GameDiffculty.*:Peaceful，Easy，Normal，Hard分别为0~3 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功，True为成功，False为失败 |

- 备注
    - 若已经锁定了游戏难度，除非调用解锁游戏难度，否则将无法成功修改游戏难度

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
result = comp.SetGameDifficulty(0)
```



## SetGameRulesInfoServer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置游戏规则。所有参数均可选。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | gameRuleDict | dict | 游戏规则字典 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 其中游戏规则字典中每一项都为可选参数,但是设置option_info或者cheat_info其中一项子项后，必须加上option_info或者cheat_info

- 示例

```python
###游戏规则字典说明
gameRuleDict ={
'option_info': {
    'pvp': bool, #玩家伤害
    'show_coordinates': bool, #显示坐标
    'fire_spreads': bool, #火焰蔓延
    'tnt_explodes': bool, #tnt爆炸
    'mob_loot': bool, #生物战利品
    'natural_regeneration': bool, #自然生命恢复
    'tile_drops': bool, #方块掉落
    'immediate_respawn':bool #立即重生
    },
'cheat_info': {
    'enable': bool, #是否开启作弊
    'always_day': bool, #终为白日
    'mob_griefing': bool, #生物破坏方块
    'keep_inventory': bool, #保留物品栏
    'weather_cycle': bool, #天气更替
    'mob_spawn': bool, #生物生成
    'entities_drop_loot': bool, #实体掉落
    'daylight_cycle': bool, #开启昼夜交替
    'command_blocks_enabled': bool, #启用方块命令
    'random_tick_speed': int,#随机方块tick速度
    }
}
###
ruleDict ={
    'cheat_info': {
        'enable': True,
        'always_day': True,

    }
}
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetGameRulesInfoServer(ruleDict)
```



## SetHurtCD

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置伤害CD

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | cdTime | int | 单位帧数 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetHurtCD(1)
```



## SetLevelGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    设置重力因子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | float | 重力因子 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
#生物可单独设置重力因子，当生物的重力因子非0时则该生物单独有自己的重力因子，具体参见实体重力组件
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.SetLevelGravity(-0.08)
```

## 生物生成

# 生物生成

## GetEntityLimit

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    获取世界最大可生成实体数量上限。可生成实体的含义见[SetEntityLimit](#setentitylimit)

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 最大可生成实体数量上限 |

- 示例

```python
import mod.server.extraServerApi as serverApi
print serverApi.GetEntityLimit()
```



## SetEntityLimit

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    设置世界最大可生成实体数量上限。可生成实体指具有spawnrule的实体。当前世界上被加载的可生成实体数量超过这个上限时，生物就不会再通过spawnrule刷出。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | num | int | 最大可生成实体数量上限 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 备注
    - 该上限与生物json文件中配置的种群密度共同作用，比如上限是200，但种群密度是10，那么该生物随机生成不会超过10个。此外生物上限还和适合生成的区块容量相关，设置上限过高的话可能因其他限制条件而不能达到该高度。

- 示例

```python
import mod.server.extraServerApi as serverApi
print serverApi.SetEntityLimit(300)
```



## SpawnCustomModule

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.mobSpawnCompServer.MobSpawnComponentServer

- 描述

    设置自定义刷怪

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | biomeType | int | [BiomeType枚举](../../枚举值/BiomeType.md) |
    | change | int | [Change枚举](../../枚举值/Change.md) |
    | entityType | int | [EntityType枚举](../../枚举值/EntityType.md) |
    | probability | int | 生成的权重[1, 10] |
    | minCount | int | 最小生成数量[0, 10] |
    | maxCount | int | 最大生成数量[0, 10] |
    | environment | int | 1:生成在表面；2:生成在水里 |
    | minBrightness | int | 生成该生物时的最小光照[1, 15]，不设置时使用默认值 |
    | maxBrightness | int | 生成该生物时的最大光照[1, 15]，不设置时使用默认值 |
    | minHeight | int | 生成该生物时最小的海拔高度[0, 256]，不设置时使用默认值 |
    | maxHeight | int | 生成该生物时最大的海拔高度[0, 256]，不设置时使用默认值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateMobSpawn(levelId)
comp.SpawnCustomModule(BiomeType.river,Change.Add,EntityType.Dolphin,10,1,10,2)
```

## 自定义数据

# 自定义数据

## CleanExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.exDataCompServer.ExDataCompServer

- 描述

    清除实体的自定义数据或者世界的自定义数据，清除实体数据时使用对应实体id创建组件，清除世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 清除实体数据
entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
suc = entitycomp.CleanExtraData("nickname")
print "CleanExtraData entity=%s suc=%s" % (entityId, suc)
# 清除全局数据
levelcomp = serverApi.GetEngineCompFactory().CreateExtraData(levelId)
suc = levelcomp.CleanExtraData("globalMsg")
print "CleanExtraData for level suc=%s" % suc
```



## GetExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.exDataCompServer.ExDataCompServer

- 描述

    获取实体的自定义数据或者世界的自定义数据，某个键所对应的值。获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | key对应的值 |

- 示例

```python
# 获取全局数据
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExtraData(levelId)
levelExData = comp.GetExtraData("globalMsg")
# 获取
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
nickName = comp.GetExtraData("nickName")
```



## GetWholeExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.exDataCompServer.ExDataCompServer

- 描述

    获取完整的实体的自定义数据或者世界的自定义数据，获取实体数据时使用对应实体id创建组件，获取世界数据时使用levelId创建组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict或None | 获取指定实体或者全局的额外存储数据字典，假如没有任何额外存储数据，那么返回None或者空字典 |

- 示例

```python
#获取实体数据字典
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
dataDict = comp.GetWholeExtraData()
if dataDict:
    for key, value in dataDict.iteritems():
        print "key=%s value=%s" % (key, str(value))
#获取全局数据字典
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExtraData(levelId)
dataDict = comp.GetWholeExtraData()
if dataDict:
    for key, value in dataDict.iteritems():
        print "key=%s value=%s" % (key, str(value))
```



## SaveExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.exDataCompServer.ExDataCompServer

- 描述

    用于保存实体的自定义数据或者世界的自定义数据

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 保存结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 设置实体的自定义数据
entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
entitycomp.SetExtraData("nickname", "steve", False)
entitycomp.SetExtraData("score", 256, False)
# more data to set
entitycomp.SaveExtraData()
```



## SetExtraData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.exDataCompServer.ExDataCompServer

- 描述

    用于设置实体的自定义数据或者世界的自定义数据，数据以键值对的形式保存。设置实体数据时使用对应实体id创建组件，设置世界数据时使用levelId创建组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 自定义key |
    | value | any | key对应的值，支持python基本数据类型 |
    | autoSave | bool | 默认自动保存，默认为True，如果批量设置数据，请将该参数设置为False，同时在设置数据完毕时调用SaveExtraData接口 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 设置实体的自定义数据
entitycomp = serverApi.GetEngineCompFactory().CreateExtraData(entityId)
entitycomp.SetExtraData("nickname","steve")
entitycomp.SetExtraData("score",256)
# 设置世界的自定义数据
levelcomp = serverApi.GetEngineCompFactory().CreateExtraData(levelId)
levelcomp.SetExtraData("globalMsg","helloWorld")
```

## 配方

# 配方

## AddBrewingRecipes

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.recipeCompServer.RecipeCompServer

- 描述

    添加酿造台配方的接口

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | brewType | str | recipe_brewing_mix或者recipe_brewing_container，recipe_brewing_mix代表混合酿造配方，recipe_brewing_container代表换容酿造配方 |
    | inputName | str | 该配方接受的物品 |
    | reagentName | str | 酿造所需要的额外物品 |
    | outputName | str | 该配方输出的物品 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 输出的物品无法和原来的物品堆叠一起
    - 对于已有的配方会返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRecipe(serverApi.GetLevelId())
print(comp.AddBrewingRecipes("recipe_brewing_container", "minecraft:potion", "minecraft:gunpowder", "minecraft:splash_potion"))
```



## GetRecipeResult

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.recipeCompServer.RecipeCompServer

- 描述

    根据配方id获取配方结果。仅支持合成配方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | recipeId | str | 配方id,对应配方json文件中的identifier字段 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | list的元素resultDict字典见备注 |

- 备注
    - resultDict字典内容如下
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | itemName  | str | 物品名称id |
        |auxValue| int | 物品附加值 |
        |num| int | 物品数目 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRecipe(serverApi.GetLevelId())
comp.GetRecipeResult(recipe1)
comp.GetRecipeResult(recipe2)
```



## GetRecipesByInput

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.recipeCompServer.RecipeCompServer

- 描述

    通过输入物品查询配方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | inputIdentifier | str | 输入物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 获取熔炉配方时，若输出物品数量为1时，output使用字符串表示物品identifier及附加值；若输出物品数量大于1时，output为一个dict
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。
    - 需要遍历较多数据，不建议频繁调用

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRecipe(serverApi.GetLevelId())
print(comp.GetRecipesByInput("minecraft:log", "crafting_table", 0, -1))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.recipeCompClient.RecipeCompClient

- 描述

    通过输入物品查询配方

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | inputIdentifier | str | 输入物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 获取熔炉配方时，若输出物品数量为1时，output使用字符串表示物品identifier及附加值；若输出物品数量大于1时，output为一个dict
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。
    - 需要遍历较多数据，不建议频繁调用

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRecipe(clientApi.GetLevelId())
print(comp.GetRecipesByInput("minecraft:log", "crafting_table", 0, -1))
```



## GetRecipesByResult

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.recipeCompServer.RecipeCompServer

- 描述

    通过输出物品查询配方所需要的输入材料

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resultIdentifier | str | 输出物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 获取熔炉配方时，若输出物品数量为1时，output使用字符串表示物品identifier及附加值；若输出物品数量大于1时，output为一个dict
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRecipe(serverApi.GetLevelId())
print(comp.GetRecipesByResult("minecraft:boat", "crafting_table", 4, -1))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.recipeCompClient.RecipeCompClient

- 描述

    通过输出物品查询配方所需要的输入材料

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | resultIdentifier | str | 输出物品的标识符 |
    | tag | str | 对应配方json中的tags字段里面的值 |
    | aux | int | 输出物品的附加值, 不传参的话默认为0 |
    | maxResultNum | int | 最大输出条目数，若大于等于0时，结果超过maxResultNum，则只返回maxResultNum条。默认-1，表示返回全部 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 返回符合条件的配方列表 |

- 备注
    - 获取熔炉配方时，若输出物品数量为1时，output使用字符串表示物品identifier及附加值；若输出物品数量大于1时，output为一个dict
    - 在获取酿造台配方时，不匹配tag标签与aux值，药水的identifier需要输入全称，例如：minecraft:potion_type:long_turtle_master，否则无法获取正确的配方。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRecipe(clientApi.GetLevelId())
print(comp.GetRecipesByResult("minecraft:boat", "crafting_table", 4, -1))
```

