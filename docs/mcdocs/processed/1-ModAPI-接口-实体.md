# ModAPI 接口-实体

## 目录

- [molang](#molang)
- [官方伙伴](#官方伙伴)
- [实体类型](#实体类型)
- [属性](#属性)
- [抛射物](#抛射物)
- [标签](#标签)
- [渲染](#渲染)
- [状态效果](#状态效果)
- [经验球](#经验球)
- [背包](#背包)
- [自定义属性](#自定义属性)
- [自定义数据](#自定义数据)
- [行为](#行为)
- [附加值](#附加值)

---

## molang

# molang

## Get

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    获取某一个实体计算节点的值，如果不存在返回注册时的默认值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | variableName | str | 节点名称，必须以"query.mod."开头 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 节点的值 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
result = comp.Get('query.mod.state')
```



## GetMolangValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    获取实体molang变量的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | molangName | str | molang变量名称，如query.can_fly |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float或long | 节点的值，不存在返回None |

- 备注
    - 因为没有渲染上下文，某些molang无法通过该种方式获取到正确的值，如query.is_first_person、variable.is_first_person等。
    - 当molangName传入query.get_name或者query.owner_identifier等需要返回字符串的变量值时，返回其hash64，类型是个int，可以用于比较。query.get_name：返回生物的名字；query.owner_identifier：返回其owner的identifier

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
result = comp.GetMolangValue('query.can_fly')
```



## GetStringHash64

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    返回字符串变量的hash64

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | key | str | 需要计算的字符串变量,如“steve" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | long | 结果值，如果传入不是字符串则返回None |

- 备注
    - 可以配合GetMolangValue使用，可以获取query.get_name或者query.owner_identifier等返回hash64的是不是等于某个值

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
result = comp.GetStringHash64('steve')
```



## Register

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    注册实体计算节点

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | variableName | str | 节点名称，必须以"query.mod."开头 |
    | defalutValue | float | 默认值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注册是否成功 |

- 备注
    - 注意节点的值使用单精度浮点数存储，如果用来设置整数，那么值大于16777216（或小于-16777216）时就会有误差

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
result = comp.Register('query.mod.state', 0.0)
```



## Set

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    设置某一个实体计算节点的值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | variableName | str | 节点名称，必须以"query.mod."开头 |
    | value | float | 计算节点的值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 注意节点的值使用单精度浮点数存储，如果用来设置整数，那么值大于16777216（或小于-16777216）时就会有误差

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(entityId)
result = comp.Set('query.mod.state', 1.0)
```



## UnRegister

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.queryVariableCompClient.QueryVariableComponentClient

- 描述

    注销实体计算节点

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | variableName | str | 节点名称，必须以"query.mod."开头 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注销是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateQueryVariable(levelId)
result = comp.UnRegister('query.mod.state')
```

## 官方伙伴

# 官方伙伴

## Disable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.petCompServer.PetComponentServer

- 描述

    关闭官方伙伴功能，单人游戏以及本地联机不支持该接口

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 关闭结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePet(levelId)
comp.Disable()
```



## Enable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.petCompServer.PetComponentServer

- 描述

    启用官方伙伴功能，单人游戏以及本地联机不支持该接口

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 启用结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePet(levelId)
comp.Enable()
```

## 实体类型

# 实体类型

## GetEngineType

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.engineTypeCompServer.EngineTypeComponentServer

- 描述

    获取实体类型，主要用于判断实体是否属于某一类型的生物。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 详见[EntityType枚举](../../枚举值/EntityType.md) |

- 示例

```python
import mod.server.extraServerApi as serverApi
from mod_log import logger as logger
comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
entityType = comp.GetEngineType()
EntityTypeEnum = serverApi.GetMinecraftEnum().EntityType
# 判断是否是生物(Mob)
if entityType & EntityTypeEnum.Mob == EntityTypeEnum.Mob:
    logger.info("{} is Mob".format(comp.GetEngineTypeStr()))
# 判断是否是弹射物(Projectile)
if entityType & EntityTypeEnum.Projectile == EntityTypeEnum.Projectile:
    logger.info("{} is Projectile".format(comp.GetEngineTypeStr()))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.engineTypeCompClient.EngineTypeComponentClient

- 描述

    获取实体类型，主要用于判断实体是否属于某一类型的生物。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 详见[EntityType枚举](../../枚举值/EntityType.md) |

- 示例

```python
import mod.client.extraClientApi as clientApi
from mod_log import logger as logger
comp = clientApi.GetEngineCompFactory().CreateEngineType(entityId)
entityType = comp.GetEngineType()
EntityTypeEnum = clientApi.GetMinecraftEnum().EntityType
# 判断是否是生物(Mob)
if entityType & EntityTypeEnum.Mob == EntityTypeEnum.Mob:
    logger.info("{} is Mob".format(comp.GetEngineTypeStr()))
# 判断是否是弹射物(Projectile)
if entityType & EntityTypeEnum.Projectile == EntityTypeEnum.Projectile:
    logger.info("{} is Projectile".format(comp.GetEngineTypeStr()))
```



## GetEngineTypeStr

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.engineTypeCompServer.EngineTypeComponentServer

- 描述

    获取实体的类型名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体类型名称，如minecraft:husk |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateEngineType(entityId)
comp.GetEngineTypeStr()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.engineTypeCompClient.EngineTypeComponentClient

- 描述

    获取实体的类型名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体类型名称，如minecraft:husk |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateEngineType(entityId)
strType = comp.GetEngineTypeStr()
```

## 属性

# 属性

## ChangeEntityDimension

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    传送实体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimensionId | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |
    | pos | tuple(int,int,int) | 传送的坐标，假如输入None，那么就优先选择目标维度的传送门作为目的地，其次使用维度坐标映射逻辑确定目的地 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 该接口无法对玩家使用，玩家请使用ChangePlayerDimension
    - 该接口只能传送到另一个维度，如果实体已经在这个维度会返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
comp.ChangeEntityDimension(0, (0,4,0))
```



## GetAttrMaxValue

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    获取实体的引擎属性的最大值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | type | int | [AttrType枚举](../../枚举值/AttrType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性值结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.GetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.attrCompClient.AttrCompClient

- 描述

    获取属性最大值，包括生命值，饥饿度，移速等

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | type | int | [AttrType枚举](../../枚举值/AttrType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性值结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
comp.GetAttrMaxValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
```



## GetAttrValue

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    获取实体的引擎属性

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | attrType | int | [AttrType枚举](../../枚举值/AttrType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.GetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.attrCompClient.AttrCompClient

- 描述

    获取属性值，包括生命值，饥饿度，移速

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | attrType | int | [AttrType枚举](../../枚举值/AttrType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 属性结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
comp.GetAttrValue(clientApi.GetMinecraftEnum().AttrType.HEALTH)
```



## GetBodyRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.rotCompClient.RotComponentClient

- 描述

    获取实体的身体的角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 身体绕竖直方向的角度，单位是角度，如果没有身体，返回为0 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
y = comp.GetBodyRot()
```



## GetCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    生物当前氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 生物当前氧气储备值 |

- 备注
    - 注意：该值返回的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.GetCurrentAirSupply()
```



## GetEntityDimensionId

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.dimensionCompServer.DimensionCompServer

- 描述

    获取实体所在维度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 维度id，0-主世界; 1-下界; 2-末地; 或其他自定义维度 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateDimension(entityId)
comp.GetEntityDimensionId()
```



## GetEntityOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorOwnerCompServer.ActorOwnerComponentServer

- 描述

    获取实体的属主

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 实体属主id |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateActorOwner(entityId)
ownerId = comp.GetEntityOwner()
```



## GetFootPos

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.posCompServer.PosComponentServer

- 描述

    获取实体脚所在的位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |

- 备注
    - 获取实体脚底的位置（除了睡觉时）
    - 类似接口参见[获取实体位置](#getpos)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
entityFootPos = comp.GetFootPos()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.posCompClient.PosComponentClient

- 描述

    获取实体脚所在的位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |

- 备注
    - 获取实体脚底的位置（除了睡觉时）
    - 类似接口参见[获取实体位置](#getpos)

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePos(entityId)
#获取位置：
entityFootPos = comp.GetFootPos()
```



## GetGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gravityCompServer.GravityComponentServer

- 描述

    获取实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 重力因子 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
comp.GetGravity()
```



## GetMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    获取生物最大氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 最大氧气储备值 |

- 备注
    - 注意：该值返回的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.GetMaxAirSupply()
```



## GetName

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.nameCompServer.NameComponentServer

- 描述

    获取生物的自定义名称，即使用命名牌或者SetName接口设置的名称

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生物的自定义名称 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateName(entityId)
comp.GetName()
```



## GetPos

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.posCompServer.PosComponentServer

- 描述

    获取实体位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 位置信息 |

- 备注
    - 对于非玩家，获取到的是脚底部位的位置
    - 对于玩家，如果处于行走，站立，游泳，潜行，滑翔状态，获得的位置比脚底位置高1.62；如果处于睡觉状态，获得的位置比最低位置高0.2
    - 类似接口有[GetFootPos](#getfootpos)，对任何实体都是获取脚底部位的位置

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
comp.GetPos()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.posCompClient.PosComponentClient

- 描述

    获取实体位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 实体的坐标 |

- 备注
    - 对于非玩家，获取到的是脚底部位的位置
    - 对于玩家，如果处于行走，站立，游泳，潜行，滑翔状态，获得的位置比脚底位置高1.62，如果处于睡觉状态，获得的位置比最低位置高0.2
    - 类似接口有[GetFootPos](#getfootpos)，对任何实体都是获取脚底部位的位置

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePos(entityId)
#获取位置：
entityPos = comp.GetPos()
```



## GetRot

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.rotCompServer.RotComponentServer

- 描述

    获取实体头与水平方向的俯仰角度和竖直方向的旋转角度，获得角度后可用GetDirFromRot接口转换为朝向的单位向量 <a href="../../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a>

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
comp.GetRot()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.rotCompClient.RotComponentClient

- 描述

    获取实体头与水平方向的俯仰角度和竖直方向的旋转角度，获得角度后可用GetDirFromRot接口转换为朝向的单位向量 <a href="../../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a>

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 俯仰角度及绕竖直方向旋转的角度，单位是角度 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
x, y = comp.GetRot()
```



## GetSize

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.collisionBoxCompServer.CollisionBoxComponentServer

- 描述

    获取实体的包围盒

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 包围盒大小 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCollisionBox(entityId)
comp.GetSize()
```



## GetTypeFamily

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    获取生物行为包字段 type_family

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | type_family列表，例['cow', 'mob'] |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.GetTypeFamily()
```



## GetUnitBubbleAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    单位气泡数对应的氧气储备值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 单位气泡数对应的氧气储备值 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(levelId)
comp.GetUnitBubbleAirSupply()
```



## IsConsumingAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    获取生物当前是否在消耗氧气

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否消耗氧气 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.IsConsumingAirSupply()
```



## LockLocalPlayerRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.rotCompClient.RotComponentClient

- 描述

    在分离摄像机时，锁定本地玩家的头部角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | lock | bool | 传入True为锁定本地玩家头部角度<br>传入False为解锁本地玩家头部角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True：设置成功<br>False：设置失败 |

- 备注
    - 只能设置localplayer，即本地玩家自己
    - 玩家重生、切换维度时会重置头部角度
    - 锁定本地玩家头部角度时第一人称视角下可以旋转镜头，但玩家头部角度不会发生改变，下次切换到第一人称视角时镜头角度仍为锁定时的角度
    - 锁定本地玩家头部角度后，玩家划船时头部角度会尽量靠近锁定时的角度，若无法转到该角度，则会向左或向右看（视哪边距离目标角度更近而定）

- 示例

```python
import mod.client.extraClientApi as clientApi
# 分离摄像机
comp = clientApi.GetEngineCompFactory().CreateCamera(levelId)
comp.DepartCamera()
# 锁定本地玩家的头部角度
comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
comp.LockLocalPlayerRot(True)
```



## SetAttrMaxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    设置实体的引擎属性的最大值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | type | int | [AttrType枚举](../../枚举值/AttrType.md) |
    | value | float | 属性值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 设置接口暂不支持 ABSORPTION
    - 在设置属性的时候，需要注意判断是否超过原版的值范围，如果设置的数值超过原版值的范围，则返回False。
    - 设置的最大饱和度不能超过当前的饥饿值; 食用食物后，最大饱和度会被原版游戏机制修改

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.SPEED,0.2)
```



## SetAttrValue

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    设置实体的引擎属性

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | attrType | int | [AttrType枚举](../../枚举值/AttrType.md) |
    | value | float | 属性值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 设置接口暂不支持 ABSORPTION
    - 在设置属性的时候，需要注意判断是否超过原版的值范围或是当前属性的值范围，如果设置的数值超过原版值的范围，则返回False。
    - 如果超过当前属性的最大值，则需要先调用SetAttrMaxValue接口来扩充该属性的最大值，否则设置的值过大时会由于超过该属性的最大值而被截取成该最大值。如果设置的值低于当前属性的最小值，则会被设置成原版的最小值。
    - 关于基础属性的原版最大值或最小值限制，可查看[AttrType枚举](../../枚举值/AttrType.md)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
# 如果设置的值超过属性当前的最大值，需要先扩充该属性的最大值，否则不生效。
comp.SetAttrMaxValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, 30)
comp.SetAttrValue(serverApi.GetMinecraftEnum().AttrType.HEALTH, 30)
```



## SetCurrentAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    设置生物氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | int | 设置生物当前氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是当前氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.SetCurrentAirSupply(300)
```



## SetEntityLookAtPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rotCompServer.RotComponentServer

- 描述

    设置非玩家的实体看向某个位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 要看向的目标位置 |
    | minTime | float | 凝视行为最短维持时间，单位为秒 |
    | maxTime | float | 凝视行为最长维持时间，单位为秒，最大值为60<br>实际行为维持时间将在minTime和maxTime之间取随机值 |
    | reject | bool | 在进行凝视行为时，是否禁止触发其他行为<br>True为禁止其他行为<br>False为允许其他行为（此时凝视行为可能表现不明显） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功，True为成功，False为失败 |

- 备注
    - 调用本接口会打断该生物正在进行的行为，且该生物不会立刻看向目标位置，而是逐渐看向目标位置
    - 对部分不会转向的实体调用此接口，可能会返回失败或返回成功但实际无表现

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
# 设置该实体看向(0,78,0)这个位置，该凝视行为最少持续2秒，最多持续3秒，凝视过程中禁止触发其他行为
comp.SetEntityLookAtPos((0,78,0), 2, 3, True)
```



## SetEntityOwner

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorOwnerCompServer.ActorOwnerComponentServer

- 描述

    设置实体的属主

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 属主实体id，为None时设置实体的属主为空 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，True表示设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateActorOwner(entityId)
result = comp.SetEntityOwner(targetId)
```



## SetFootPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.posCompServer.PosComponentServer

- 描述

    设置实体脚底所在的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | footPos | tuple(float,float,float) | 实体脚所在的位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 行为与使用tp命令一致，实体会瞬移到目标点
    - 在床上时调用该接口会返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
comp.SetFootPos((0, 4, 0))
```



## SetGravity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gravityCompServer.GravityComponentServer

- 描述

    设置实体的重力因子，当生物重力因子为0时则应用世界的重力因子

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | gravity | float | 负数，表示每帧向下的速度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
comp.SetGravity(-0.08)
```



## SetMaxAirSupply

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    设置生物最大氧气储备值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | data | int | 设置生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 注意：该值设置的是最大氧气储备的支持的逻辑帧数 = 氧气储备值 * 逻辑帧数（每秒20帧数）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.SetMaxAirSupply(400)
```



## SetName

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.nameCompServer.NameComponentServer

- 描述

    用于设置生物的自定义名称，跟原版命名牌作用相同，玩家和新版流浪商人暂不支持

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateName(entityId)
comp.SetName("new Name")
```



## SetPersistent

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    设置实体不会因为离玩家太远而被[清除](https://minecraft.fandom.com/zh/wiki/%E7%94%9F%E6%88%90#.E5.9F.BA.E5.B2.A9.E7.89.88_2)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | persistent | bool | 设置为True时，则实体不会被清除 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 使用CreateEngineEntityByTypeStr创建isNpc为True的实体时，默认不会被清除

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.SetPersistent(True)
```



## SetPlayerLookAtPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.rotCompClient.RotComponentClient

- 描述

    设置本地玩家看向某个位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 要看向的目标位置 |
    | pitchStep | float | 俯仰角方向旋转的角速度（每帧），最小为0.2 |
    | yawStep | float | 偏航角方向旋转的角速度（每帧），最小为0.2 |
    | blockInput | bool | 转向目标角度时是否屏蔽玩家操作，默认为True<br>True:屏蔽玩家操作，此时玩家无法转向、移动<br>False:不屏蔽玩家操作，此时如果玩家有移动、镜头转向操作将会打断通过本接口设置的转向 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功，True为成功，False为失败 |

- 备注
    - 当本地玩家未与摄像机分离时，调用本接口会导致摄像机一同看向指定位置<br>当本地玩家与摄像机分离时，调用本接口将只改变本地玩家模型的朝向

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRot(localPlayerId)
# 设置本地玩家以0.2度每帧的俯仰角速度、1度每帧的偏航角速度看向(0,78,0)这个位置，转向过程中屏蔽玩家操作
comp.SetPlayerLookAtPos((0,78,0), 0.2, 1, True)
```



## SetPos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.posCompServer.PosComponentServer

- 描述

    设置实体位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | xyz值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 行为与使用tp命令一致，实体会瞬移到目标点
    - 对于所有类型的实体都是设置脚底位置，与[SetFootPos](#setfootpos)等价
    - 在床上时调用该接口会返回False

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePos(entityId)
comp.SetPos((1,2,3))
```



## SetRecoverTotalAirSupplyTime

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.breathCompServer.BreathCompServer

- 描述

    设置恢复最大氧气量的时间，单位秒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timeSec | float | 恢复生物最大氧气值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意：当设置的最大氧气值小于（timeSec*10）时，生物每帧恢复氧气量的值为0

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBreath(entityId)
comp.SetRecoverTotalAirSupplyTime(10)
```



## SetRot

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.rotCompServer.RotComponentServer

- 描述

    设置实体头与水平方向的俯仰角度和竖直方向的旋转角度 <a href="../../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | （上下角度，左右角度）单位是角度而不是弧度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRot(entityId)
comp.SetRot((30,0))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.rotCompClient.RotComponentClient

- 描述

    设置实体头与水平方向的俯仰角度和竖直方向的旋转角度 <a href="../../../../mcguide/20-玩法开发/10-基本概念/10-Vector3.html">MC坐标系说明</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向旋转的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 建议只用来设置本地玩家。如果设置其他生物，会被生物自身行为覆盖。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateRot(entityId)
# 设为向上仰视45度，并朝向世界z轴正方向
comp.SetRot((-45, 0))
```



## SetSize

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.collisionBoxCompServer.CollisionBoxComponentServer

- 描述

    设置实体的包围盒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | size | tuple(float,float) | 第一位表示宽度和长度，第二位表示高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 对新生产的实体需要经过5帧之后再设置包围盒的大小才会生效

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateCollisionBox(entityId)
comp.SetSize((2,3))
```



## isEntityInLava

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.attrCompClient.AttrCompClient

- 描述

    实体是否在岩浆中

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否在岩浆中，True为在岩浆中，False为不在岩浆中 |

- 备注
    - 只能获取到本地客户端已加载的实体是否在岩浆中，若实体在其他维度或未加载（距离本地玩家太远），将获取失败

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
isInLava = comp.isEntityInLava()
```



## isEntityOnGround

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.attrCompClient.AttrCompClient

- 描述

    实体是否触地

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否触地，True为触地，False为不触地 |

- 备注
    - 客户端实体刚创建时引擎计算还没完成，此时获取该实体是否着地将返回默认值True，需要延迟一帧进行获取才能获取到正确的数据
    - 生物处于骑乘状态时，如玩家骑在猪身上，也视作触地
    - 只能获取到本地客户端已加载的实体是否触地，若实体在其他维度或未加载（距离本地玩家太远），将获取失败

- 示例

```python
comp = clientApi.GetEngineCompFactory().CreateAttr(entityId)
isOnGound = comp.isEntityOnGround()
```

## 抛射物

# 抛射物

## GetSourceEntityId

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.bulletAttributesCompServer.BulletAttributesComponentServer

- 描述

    获取抛射物发射者实体id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 抛射物发射者实体id |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBulletAttributes(entityId)
comp.GetSourceEntityId()
```

## 标签

# 标签

## AddEntityTag

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tagCompServer.TagComponentServer

- 描述

    增加实体标签

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tag | str | 标签名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
comp.AddEntityTag("AAA")
```



## EntityHasTag

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tagCompServer.TagComponentServer

- 描述

    判断实体是否存在某个指定的标签

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tag | str | 标签名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否包含标签 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
comp.EntityHasTag("AAA")
```



## GetEntityTags

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tagCompServer.TagComponentServer

- 描述

    获取实体标签列表

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(str) | 标签列表 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
comp.GetEntityTags()
```



## RemoveEntityTag

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tagCompServer.TagComponentServer

- 描述

    移除实体某个指定的标签

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tag | str | 标签名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTag(entityId)
comp.RemoveEntityTag("AAA")
```

## 渲染

# 渲染

## AddActorAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染动画

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |
    | animationKey | str | 动画键 |
    | animationName | str | 动画名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorAnimation("minecraft:pig", "custom_move", "animation.pig.custom_move")
```



## AddActorAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物的identifier |
    | animationControllerKey | str | 动画控制器键 |
    | animationControllerName | str | 动画控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
comp.AddActorAnimationController("minecraft:skeleton", "controller__use_item_progress", "controller.animation.humanoid.use_item_progress")
```



## AddActorBlockGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    为实体添加方块几何体模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | offset | tuple(float,float,float) | 方块几何体模型相对实体的位置偏移值，可选参数，默认为(0, 0, 0)。 |
    | rotation | tuple(float,float,float) | 方块几何体模型相对实体的旋转角度，可选参数，默认为(0, 0, 0)，分别表示绕x,y,z轴的旋转角度，旋转顺序按z,x,y顺序旋转。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功，成功返回True，失败返回False。如果实体已经拥有了相同名称的模型，则也会返回True |

- 备注
    - 请在确保世界已经初始化完成后（例如，监听UiInitFinished事件）再调用该接口，否则过早调用会导致接口执行失败。

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 合并方块并转换为名叫"my_block_geometry"的方块几何体模型
geometryName = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
# 添加到实体id为-4294967295的实体中
print actorRenderComp.AddActorBlockGeometry(geometryName)
```



## AddActorGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染几何体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物实体identifier |
    | geometryKey | str | 渲染几何体键，如default |
    | geometryName | str | 渲染几何体名称，如熊猫几何体geometry.panda |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效
        动画和贴图都是与几何体密切相关的，改变几何体也需要改变动画与贴图。建议先修改生物的动画以及动画控制器后再修改生物的几何。
    - 某些生物受初始动画影响，几何体会有初始偏移，会导致修改几何体后表现异常。若修改后的几何体没有当前动画需要的骨骼时，会触发报错。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorGeometry("minecraft:sheep", "default", "geometry.panda")
```



## AddActorParticleEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物特效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |
    | effectKey | str | 特效资源Key，如bee.entity.json中的nectar_dripping |
    | effectName | str | 特效资源名称，如minecraft:nectar_drip_particle |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorParticleEffect("minecraft:villager", "nectar_dripping", "minecraft:nectar_drip_particle")
```



## AddActorRenderController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物[渲染控制器](/mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物identifier |
    | renderControllerName | str | 渲染控制器名称 |
    | condition | str | 渲染控制器条件，当该条件成立时，renderControllerName指向的渲染控制器才会生效 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorRenderController('minecraft:villager', 'custom_render_controller_name', 'query.mod.condition')
```



## AddActorRenderControllerArray

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染控制器列表中字典arrays元素

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |
    | renderControllerName | str | 实体生物渲染控制器名称 |
    | arrayType | int | 渲染控制器arrays类型([渲染控制器arrays类型枚举](../../枚举值/RenderControllerArrayType.md)) |
    | arrayName | str | 数组名称 |
    | expression | str | 待添加元素表达式 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 该接口增加render_controller->arrays—>materials/textures/geometries->array.***中的元素
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
comp.AddActorRenderControllerArray("minecraft:pig", "controller.render.pig", clientApi.GetMinecraftEnum().RenderControllerArrayType.Texture, "Array.skins", "Texture.test")
```



## AddActorRenderMaterial

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染需要的[材质](/mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_3-自定义材质)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物的identifier |
    | materialKey | str | 材质key |
    | materialName | str | 材质名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 添加是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(playerId)
comp.AddActorRenderMaterial('minecraft:villager', 'custom_material_key', 'custom_material_name')
```



## AddActorScriptAnimate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    在生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |
    | animateName | str | 动画/动画控制器名称，如look_at_target |
    | condition | str | 动画/动画控制器控制表达式，默认为空，如query.mod.index > 0 |
    | autoReplace | bool | 是否覆盖已存在的动画/动画控制器，默认值为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 对于已经存在的生物，在调用CreateActorRender时需要传生物Id才能马上生效，对于不存在的生物，直接传levelId即可。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
comp.AddActorAnimationController("minecraft:pig", "animation_controller_short_name", "controller.animation.pig.custom_animation_controller")
comp.AddActorScriptAnimate("minecraft:pig", "animation_controller_short_name", "query.mod.index > 0")
```



## AddActorSoundEffect

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物音效资源

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |
    | soundKey | str | 音效资源Key |
    | soundName | str | 音效资源名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 目前只支持在动作(animation)中播放音效，不支持在动作控制器(animation controller)中播放音效。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorSoundEffect("minecraft:villager", "sound_thunder", "ambient.weather.thunder")
```



## AddActorTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    增加生物渲染贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物实体identifier |
    | textureKey | str | 贴图键 |
    | texturePath | str | 贴图路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.AddActorTexture("minecraft:sheep", "default", "textures/entity/panda/panda")
```



## BindEntityToEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.modelCompClient.ModelComponentClient

- 描述

    绑定骨骼模型跟随其他entity,摄像机也跟随其他entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | bindEntityId | str | 绑定跟随的实体Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | False表示失败，True表示成功 |

- 备注
    - 本接口只实现视觉效果，本质上实体还是在原地，因此需要调用接口设置实体的位置到其他entity的位置上，否则当实体本身不在摄像机范围内的时候就会不进行渲染了。

- 示例

```python
import mod.client.extraClientApi as clientApi
# 将entityId的实体绑定至bindEntityId的实体
comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
comp.BindEntityToEntity(bindEntityId)
```



## ClearActorBlockGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除实体中所有的方块几何体模型。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 合并方块并转换为名叫"my_block_geometry"的方块几何体模型
geometryName = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
# 添加到实体id为-4294967295的实体中
print actorRenderComp.AddActorBlockGeometry(geometryName)
# 清空实体中所有的方块几何体
print actorRenderComp.ClearActorBlockGeometry()
```



## DeleteActorBlockGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除实体中指定方块几何体模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 合并方块并转换为名叫"my_block_geometry"的方块几何体模型
geometryName = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
# 添加到实体id为-4294967295的实体中
print actorRenderComp.AddActorBlockGeometry(geometryName)
# 删除刚才添加的方块几何体
print actorRenderComp.DeleteActorBlockGeometry(geometryName)
```



## GetNotRenderAtAll

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    获取实体是否不渲染

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示不渲染 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
notRender = comp.GetNotRenderAtAll()
```



## RebuildActorRender

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    重建生物的数据渲染器（该接口不支持玩家，玩家请使用RebuildPlayerRender）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 实体identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 重建是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.RebuildActorRender('minecraft:villager')
```



## RemoveActorAnimationController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    移除生物渲染动画控制器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物的identifier |
    | animationControllKey | str | 动画控制器键，注意，该值需要在json中动画控制器键加上前缀“controller__” |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
comp.RemoveActorAnimationController("minecraft:villager", "controller__use_item_progress")
```



## RemoveActorGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除生物渲染几何体

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物实体identifier |
    | geometryKey | str | 渲染几何体名称，如熊猫几何体geometry.panda |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效
        动画和贴图都是与几何体密切相关的，改变几何体也需要改变动画与贴图

- 示例

```python
import mod.client.extraClientApi as clientApi
# geometry definition in panda.entity.json
# "geometry": {
#     "default": "geometry.panda"
# },
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.RemoveActorGeometry("minecraft:panda", "default")
```



## RemoveActorRenderController

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除生物[渲染控制器](/mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_7-自定义渲染控制器)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物identifier |
    | renderControllerName | str | 渲染控制器名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 删除是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.RemoveActorRenderController('minecraft:villager', 'custom_render_controller_name')
```



## RemoveActorTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    删除生物渲染贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | actorIdentifier | str | 生物实体identifier |
    | textureKey | str | 贴图键，如default |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 调用该接口后需要调用RebuildActorRender才会生效

- 示例

```python
import mod.client.extraClientApi as clientApi
# texture definition in panda.entity.json
# "textures": {
#     "default": "textures/entity/panda/panda",
#     "lazy": "textures/entity/panda/panda_lazy",
#     "worried": "textures/entity/panda/panda_worried",
#     "playful": "textures/entity/panda/panda_playful",
#     "brown": "textures/entity/panda/panda_brown",
#     "weak": "textures/entity/panda/panda_sneezy",
#     "aggressive": "textures/entity/panda/panda_aggressive"
# }
comp = clientApi.GetEngineCompFactory().CreateActorRender(levelId)
comp.RemoveActorTexture("minecraft:panda", "default")
```



## ResetBindEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.modelCompClient.ModelComponentClient

- 描述

    取消目标entity的绑定实体，取消后不再跟随任何其他entity

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | False表示失败，True表示成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateModel(entityId)
comp.ResetBindEntity()
```



## SetActorAllBlockGeometryVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置实体中所有的方块几何体模型是否显示。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | visible | bool | 设置是否显示或隐藏，True表示显示，False表示隐藏 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 合并方块并转换为名叫"my_block_geometry"的方块几何体模型
geometryName = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
# 添加到实体id为-4294967295的实体中
print actorRenderComp.AddActorBlockGeometry(geometryName)
# 隐藏所有的方块几何体
print actorRenderComp.SetActorAllBlockGeometryVisible(False)
```



## SetActorBlockGeometryVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置实体中指定的方块几何体模型是否显示。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | visible | bool | 设置是否显示或隐藏，True表示显示，False表示隐藏 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 合并方块并转换为名叫"my_block_geometry"的方块几何体模型
geometryName = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
# 添加到实体id为-4294967295的实体中
print actorRenderComp.AddActorBlockGeometry(geometryName)
# 隐藏刚才添加的方块几何体
print actorRenderComp.SetActorBlockGeometryVisible(geometryName, False)
```



## SetAlwaysShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.nameCompClient.NameComponentClient

- 描述

    设置生物名字是否一直显示，瞄准点不指向生物时也能显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | True为显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 备注
    - 该接口只对普通生物生效，对玩家设置不起作用

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateName(entityId)
# 不显示头上的名字
comp.SetAlwaysShowName(False)
```



## SetColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.healthCompClient.HealthComponentClient

- 描述

    设置血条的颜色及背景色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | front | tuple(float,float,float,float) | 血条颜色的RGBA值，范围0-1 |
    | back | tuple(float,float,float,float) | 背景颜色的RGBA值，范围0-1 |

- 返回值

    无

- 备注
    - 必须用game组件设置ShowHealthBar时才能显示血条！！

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
comp.SetColor((0, 0, 0, 1), (1, 1, 1, 1))
```



## SetHealthBarDeviation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.healthCompClient.HealthComponentClient

- 描述

    设置某个entity血条的相对高度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | health_bar_deviation | float | 血条的相对高度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 必须用game组件设置ShowHealthBar时才能显示血条；血条默认在生物AABB上方1.5高度处

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
# 设置血条的相对高度
comp.SetHealthBarDeviation(1.0)
```



## SetNameDeeptest

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    设置名字是否透视

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | deeptest | bool | True为不透视。默认情况下为透视 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
# 设置为不透视
comp.SetNameDeeptest(True)
```



## SetNotRenderAtAll

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置是否关闭实体渲染

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | notRender | bool | True表示不渲染该实体 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
# 不渲染单个实体 entityId
comp = clientApi.GetEngineCompFactory().CreateActorRender(entityId)
comp.SetNotRenderAtAll(True)
# 重新开始渲染该实体
comp.SetNotRenderAtAll(False)
```



## SetRenderLocalPlayer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    设置本地玩家是否渲染

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | render | bool | True为渲染 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
# 不渲染本地玩家
comp.SetRenderLocalPlayer(False)
```



## SetShowName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.nameCompClient.NameComponentClient

- 描述

    设置生物名字是否按照默认游戏逻辑显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | True为显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 备注
    - 当设置为True时，生物的名字显示遵循游戏默认的渲染逻辑，即普通生物需要中心点指向生物才显示名字，玩家则是会一直显示名字

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateName(entityId)
# 不显示头上的名字
comp.SetShowName(False)
```



## ShowHealth

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.healthCompClient.HealthComponentClient

- 描述

    设置某个entity是否显示血条，默认为显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | 设置是否显示 |

- 返回值

    无

- 备注
    - 必须用game组件设置ShowHealthBar时才能显示血条！！

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateHealth(entityId)
# 设置该entity不显示血条
comp.ShowHealth(False)
```



## ShowHealthBar

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    设置是否显示血条

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | show | bool | True为显示。开启后可用health组件单独设置某个实体的血条颜色及是否显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.ShowHealthBar(True)
```

## 状态效果

# 状态效果

## AddEffectToEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.effectCompServer.EffectComponentServer

- 描述

    为实体添加指定状态效果，如果添加的状态已存在则有以下集中情况：1、等级大于已存在则更新状态等级及持续时间；2、状态等级相等且剩余时间duration大于已存在则刷新剩余时间；3、等级小于已存在则不做修改；4、粒子效果以新的为准

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectName | str | 状态效果名称字符串，包括自定义状态效果和原版状态效果，原版状态效果可在wiki查询 |
    | duration | int | 状态效果持续时间，单位秒 |
    | amplifier | int | 状态效果的额外等级。必须在0至255之间（含）。若未指定，默认为0。注意，状态效果的第一级（如生命恢复 I）对应为0，因此第二级状态效果，如生命回复 II，应指定强度为1。部分效果及自定义状态效果没有强度之分，如夜视 |
    | showParticles | bool | 是否显示粒子效果，True显示，False不显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
res = comp.AddEffectToEntity("speed", 30, 2, True)
```



## GetAllEffects

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.effectCompServer.EffectComponentServer

- 描述

    获取实体当前所有状态效果

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(dict) | 状态效果信息字典的list |

- 备注
    - 状态效果信息字典 effectDict
        | 关键字     | 数据类型              | 说明     |
        | ----------| --------------------- | ---------|
        | effectName | str | 状态效果名称 |
        | duration  | int | 状态效果剩余持续时间，单位秒 |
        | amplifier  | int | 状态效果额外等级 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
effectDictList = comp.GetAllEffects()
```



## RemoveEffectFromEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.effectCompServer.EffectComponentServer

- 描述

    为实体删除指定状态效果

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effectName | str | 状态效果名称字符串，包括自定义状态效果和原版状态效果，原版状态效果可在wiki查询 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示删除成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateEffect(entityId)
res = comp.RemoveEffectFromEntity("speed")
```

## 经验球

# 经验球

## GetOrbExperience

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    获取经验球的经验

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 经验值，正整数。获取失败的情况下返回-1。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
print(comp.GetOrbExperience())
```



## SetOrbExperience

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.expCompServer.ExpComponentServer

- 描述

    设置经验球经验

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | exp | int | 经验球经验 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 设置经验球经验，entityId是经验球的entityId,如果经验小于等于0，拾取后不再加经验

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateExp(entityId)
comp.SetOrbExperience(25)
```

## 背包

# 背包

## GetEntityItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取生物物品，支持获取背包，盔甲栏，副手以及主手物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | [ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | slotPos | int | 槽位，获取INVENTORY及ARMOR时需要设置，其他情况写0即可 |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 物品信息字典，没有物品则返回None |

- 备注
    - 左右手及装备可以替代GetPlayerItem接口获取玩家的物品，但背包不行。获取生物背包目前支持驴、骡、羊驼以及其他带背包的自定义生物

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
comp.GetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, 0)
```



## GetEquItemEnchant

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取装备槽位中盔甲的附魔

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | [ArmorSlotType枚举](../../枚举值/ArmorSlotType.md)枚举 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(int,int)) | 盔甲的附魔 |

- 备注
    - 如果物品不存在，或者没有附魔值，返回None。如果存在返回tuple数组，每个tuple由附魔类型([EnchantType枚举](../../枚举值/EnchantType.md))和附魔等级组成

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetEquItemEnchant(serverApi.GetMinecraftEnum().ArmorSlotType.HEAD)
```



## GetEquItemModEnchant

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取装备槽位中盔甲的自定义附魔

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | slotPos | int | [ArmorSlotType枚举](../../枚举值/ArmorSlotType.md)枚举 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(str,int)) | list中每个tuple由自定义附魔id和附魔等级组成，没有自定义附魔则返回空列表 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetEquItemModEnchant(serverApi.GetMinecraftEnum().ArmorSlotType.HEAD)
```



## SetEntityItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    设置生物物品，建议开发者根据生物特性来进行设置，部分生物设置装备后可能不显示但是死亡后仍然会掉落所设置的装备

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posType | int | [ItemPosType枚举](../../枚举值/ItemPosType.md) |
    | itemDict | dict | 生物身上不同位置的<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>列表，如果传入None将清除当前位置的物品/装备 |
    | slotPos | int | 容器槽位，如果ItemPosType为左右手可不传，如果ItemPosType为背包则对应背包槽位，如果ItemPosType为armor则对应装备位置，具体请看[ArmorSlotType枚举](../../枚举值/ArmorSlotType.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置成功返回True |

- 备注
    - 设置生物背包目前支持驴、骡、羊驼以及其他带背包的自定义生物。该接口与spawnTo系列接口相比多了槽位限制，只能设置对应槽位的装备、左手物品，并且右手不能设置装备。溺尸暂不支持设置自定义装备。如果传入的itemDict为None或{}，itemName为minecraft:air，count为0，均可以达到清除物品的效果。玩家背包请使用SpawnItemToPlayerInv来生成物品，使用SetInvItemNum设置0来清除物品，其他部位也可以用该接口设置。
    - posType设置成serverApi.GetMinecraftEnum().ItemPosType.OFFHAND，itemDict设置成None可替代ClearPlayerOffHand

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(entityId)
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1,
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': {},
}
comp.SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.INVENTORY, itemDict, 0)

#替代ClearPlayerOffHand接口的做法
comp.SetEntityItem(serverApi.GetMinecraftEnum().ItemPosType.OFFHAND, None, 0)
```

## 自定义属性

# 自定义属性

## GetAttr

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.modAttrCompServer.ModAttrComponentServer

- 描述

    获取属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | defaultValue | any | 属性默认值，属性不存在时返回该默认值，此时属性值依然未设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | 返回属性值 |

- 备注
    - defaultValue不传的时候默认为None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.GetAttr('health')
# 如果直接修改GetAttr出来的集合类型，需要重新调用一遍SetAttr确保有进行更新
testDict = comp.GetAttr('testDict')
testDict['key'] = 'newValue'
comp.SetAttr('testDict', testDict)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.modAttrCompClient.ModAttrComponentClient

- 描述

    获取属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | defaultValue | any | 属性默认值，属性不存在时返回该默认值，此时属性值依然未设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | 返回属性值 |

- 备注
    - defaultValue不传的时候默认为None

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.GetAttr('health')
```



## RegisterUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.modAttrCompClient.ModAttrComponentClient

- 描述

    注册属性值变换时的回调函数，当属性变化时会调用该函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 回调函数需要接受一个参数，参数是dict，具体数据示例：{'oldValue': 0, 'newValue': 1, 'entityId': ’-433231231231‘}

- 示例

```python
import mod.client.extraClientApi as clientApi
# 这个entityId传的是所需要监听的对象的Id
comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.RegisterUpdateFunc('health', self.jumpingText)
# 当脚本层的health属性变化时则会调用self.jumpingText
def jumpingText(self, data):
    entityId = data['entityId']
    oldValue = data['oldValue']
    newValue = data['newValue']
```



## SetAttr

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.modAttrCompServer.ModAttrComponentServer

- 描述

    设置属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | paramValue | any | 属性值，支持python基础数据 |

- 返回值

    无

- 备注
    - 注意：tuple、set在同步时会转成list。建议优先使用数字和字符串等非集合类型。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.SetAttr('health', 1)
comp.SetAttr('testDict', {'key':'value'})
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.modAttrCompClient.ModAttrComponentClient

- 描述

    设置客户端属性值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 属性名称，str的名称建议以mod命名为前缀，避免多个mod之间冲突 |
    | paramValue | any | 属性值，支持python基础数据 |

- 返回值

    无

- 备注
    - 注意：这里设置了只在本地有效，并不会同步到服务端和其他客户端

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.SetAttr('health', 1)
```



## UnRegisterUpdateFunc

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.modAttrCompClient.ModAttrComponentClient

- 描述

    反注册属性值变换时的回调函数

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | paramName | str | 监听的属性名称 |
    | func | function | 监听的回调函数 |

- 返回值

    无

- 备注
    - 需要传注册时的同一个函数作为参数

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateModAttr(entityId)
comp.UnRegisterUpdateFunc('health', self.jumpingText)
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

## 行为

# 行为

## AddEntityAroundEntityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给实体（不含玩家）添加对实体环绕运动器

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
    - 该接口不屏蔽生物本身的AI运动以及重力作用，当有AI运动发生时，最终的表现结果可能与预期有差异。
    - 环绕运动器可叠加多个，且可与速度运动器互相叠加。
    - 由于引擎中在加载的区块以外的实体时会停止一切活动，建议将实体的运动范围控制在玩家位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
axis=(-1, 1, 1)
mID = motionComp.AddEntityAroundEntityMotion(eID, 1.0, axis, lockDir=False, stopRad=0)
```



## AddEntityAroundPointMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给实体（不含玩家）添加对点环绕运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | center | tuple(float,float,float) | 要环绕的圆心点坐标 |
    | angularVelocity | float | 圆周运动的角速度（弧度/秒） |
    | axis | tuple(float,float,float) | 圆周运动的轴，决定了在哪个平面上做圆周运动，默认为(0, 1, 0) |
    | lockDir | bool | 是否在运动器生效时锁定实体的朝向，不锁定则实体的朝向会随着运动而改变，默认为False。 |
    | stopRad | float | 停止该运动器所需要的弧度，当stopRad为0时，该运动器会一直运行，默认为0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽生物本身的AI运动以及重力作用，当有AI运动发生时，最终的表现结果可能与预期有差异。
    - 环绕运动器可叠加多个，且可与速度运动器互相叠加。
    - 由于引擎中在加载的区块以外的实体时会停止一切活动，建议将实体的运动范围控制在玩家位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
center = (0, 8, 0)
axis=(-1, 1, 1)
mID = motionComp.AddEntityAroundPointMotion(center, 1.0, axis, lockDir=False, stopRad=0)
```



## AddEntityTrackMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给实体（不含玩家）添加轨迹运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 轨迹终点 |
    | duraTime | float | 到达终点所需要的时间 |
    | startPos | tuple(float,float,float) | 轨迹起点，默认为None，表示以调用[StartEntityMotion](#StartEntityMotion)的位置作为起点。 |
    | relativeCoord | bool | 是否使用相对坐标设置起点和终点，默认为False。 |
    | isLoop | bool | 是否循环，若设为True，则实体会在起点和终点之间往复运动。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 运动器ID，添加失败时返回-1 |

- 备注
    - 该接口不屏蔽生物本身的AI运动，并且生物在空中时会受到跌落伤害，当有AI运动发生时，最终的表现结果可能与预期有差异，建议将生物设置为NPC。
    - 轨迹运动器不可叠加，仅能添加一个。
    - 由于引擎中在加载的区块以外的实体时会停止一切活动，建议将运动范围控制在玩家位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
target = (5, 0, 0)
mID = motionComp.AddEntityTrackMotion(target, 3.0, startPos=None, relativeCoord=True, isLoop=False)
```



## AddEntityVelocityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    给实体（不含玩家）添加速度运动器

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
    - 该接口不屏蔽生物本身的AI运动以及重力作用，当有AI运动发生时，最终的表现结果可能与预期有差异。
    - 速度运动器可叠加多个，且可与环绕运动器互相叠加。
    - 由于引擎中在加载的区块以外的实体时会停止一切活动，建议将实体的运动范围控制在玩家位置±100内。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
velocity = (0, 0, 1)
accelerate = (0, 0, -1)
mID = motionComp.AddEntityVelocityMotion(velocity, accelerate, useVelocityDir=True)
```



## GetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actionCompServer.ActionCompServer

- 描述

    获取仇恨目标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 返回仇恨目标的实体id。如果传入的实体id所对应的实体没有仇恨目标，则返回-1。如果传入的实体id所对应的实体不存在，则返回None。 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
comp.GetAttackTarget()
```



## GetBlockControlAi

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.controlAiCompServer.ControlAiCompServer

- 描述

    获取生物原生AI是否被屏蔽

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | AI是否保留。False为AI被屏蔽。 |

- 备注
    - 屏蔽AI后的生物无法行动，不受重力且不会被推动。但是可以受到伤害，也可以被玩家交互（例如马被骑或村民被交易）

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
comp.GetBlockControlAi()
```



## GetCustomGoalCls

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    用于获取服务器自定义行为节点的基类。实现新的行为节点时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(CustomGoal) | 服务端自定义行为节点类 |

- 示例

```python
import mod.server.extraServerApi as serverApi
CustomGoal = serverApi.GetCustomGoalCls()
class CustomGoalDemo(CustomGoal):
    def __init__(self, entityId, argsJson):
        CustomGoalCls.__init__(self, entityId, argsJson)
```



## GetEntityMotions

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    获取实体（不含玩家）身上的所有运动器

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
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motions = motionComp.GetEntityMotions()
# motions = {
#   0:1,
#   1:2
# }
```



## GetMotion

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    获取生物（含玩家）的瞬时移动方向向量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 瞬时移动方向向量，异常时返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.GetMotion()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.actorMotionCompClient.ActorMotionComponentClient

- 描述

    获取生物的瞬时移动方向向量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 瞬时移动方向向量，异常时返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.GetMotion()
```



## GetOwnerId

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tameCompServer.TameComponentServer

- 描述

    获取驯服生物的主人id

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 主人id，不存在时返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateTame(entityId)
oid = comp.GetOwnerId()
```



## GetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    返回玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 台阶高度 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
print(comp.GetStepHeight())
```



## Hurt

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.hurtCompServer.HurtCompServer

- 描述

    设置实体伤害

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | damage | int | 伤害值 |
    | cause | str | 伤害来源，详见Minecraft枚举值文档的[ActorDamageCause枚举](../../枚举值/ActorDamageCause.md) |
    | attackerId | str | 伤害来源的实体id，默认为None |
    | childAttackerId | str | 伤害来源的子实体id，默认为None，比如玩家使用抛射物对实体造成伤害，该值应为抛射物Id |
    | knocked | bool | 实体是否被击退，默认值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateHurt(playerId)
comp.Hurt(10, serverApi.GetMinecraftEnum().ActorDamageCause.EntityAttack, attackerId, None, False)
```



## ImmuneDamage

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.hurtCompServer.HurtCompServer

- 描述

    设置实体是否免疫伤害（该属性存档）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | immune | bool | 是否免疫伤害 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateHurt(entityId)
comp.ImmuneDamage(True)
```



## IsEntityOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    获取实体是否着火

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否着火 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
isOnFire = comp.IsEntityOnFire()
```



## RemoveEntityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    移除实体（不含玩家）身上的运动器

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
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.RemoveEntityMotion(mID)
```



## ResetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actionCompServer.ActionCompServer

- 描述

    清除仇恨目标

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
comp.ResetAttackTarget()
```



## ResetMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    重置生物（不含玩家）的瞬时移动方向向量

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 该接口只能重置SetMotion所设置的瞬时移动方向向量，无法影响由生物本身的AI所产生的运动。

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.ResetMotion()
```



## ResetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.ResetStepHeight()
```



## SetActorCollidable

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorCollidableCompClient.ActorCollidableCompClient

- 描述

    设置实体是否可碰撞

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isCollidable | int | 0:不可碰撞  1:可碰撞 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateActorCollidable(entityId)
success = comp.SetActorCollidable(1)
```



## SetActorPushable

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorPushableCompServer.ActorPushableCompServer

- 描述

    设置实体是否可推动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPushable | int | 0:不可推动  1:可推动 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateActorPushable(entityId)
success = comp.SetActorPushable(1)
```



## SetAttackTarget

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actionCompServer.ActionCompServer

- 描述

    设置仇恨目标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 目标实体id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
comp.SetAttackTarget(targetId)
```



## SetBlockControlAi

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.controlAiCompServer.ControlAiCompServer

- 描述

    设置屏蔽生物原生AI

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isBlock | bool | 是否保留AI，False为屏蔽 |
    | freezeAnim | bool | 屏蔽AI时是否冻结动作，默认为False，仅当isBlock为False时生效。重进世界会恢复成初始动作 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 屏蔽AI后的生物无法行动，不受重力且不会被推动，但是可以受到伤害，也可以被玩家交互（例如马被骑或村民被交易）
    - 对玩家无效

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateControlAi(entityId)
comp.SetBlockControlAi(False, True)
```



## SetCanOtherPlayerRide

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    设置其他玩家是否有权限骑乘，True表示每个玩家都能骑乘，False只有驯服者才能骑乘

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tamedEntityId | str | 可骑乘生物id |
    | canRide | bool | 是否控制 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
# 驯服生物
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetCanOtherPlayerRide(entityId,False)
```



## SetControl

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    设置该生物无需装备鞍就可以控制行走跳跃

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tamedEntityId | str | 可骑乘生物id |
    | isControl | bool | 是否控制 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 该接口仅对已被驯服的可骑乘生物生效，若使用SetEntityRide接口驯服生物，需间隔一定帧数后再调用本接口。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetControl(entityId,True)
```



## SetEntityInteractFilter

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.interactCompServer.InteractComponentServer

- 描述

    设置与生物可交互的条件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | index | int | 交互列表下标 |
    | interactFilter | str | 可交互的条件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 该接口修改minecraft:interact->on_interact中的filters的定义
    - 仅当生物存在minecraft:interact组件时才能调用该接口，例如牛、羊驼、猪灵等

- 示例

```python
import mod.server.extraServerApi as serverApi
import json
comp = serverApi.GetEngineCompFactory().CreateInteract(entityId)
filterDict = {
    "filters": {
        "all_of": [
            { "test": "is_family", "subject" : "other", "value" :  "player"},
            { "test": "has_equipment", "domain": "hand", "subject": "other", "value": "bucket:0"}
        ]
    }
}
filterStr = json.dumps(filterDict)
comp.SetEntityInteractFilter(0, filterStr)
```



## SetEntityOnFire

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    设置实体着火

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | seconds | int | 着火时间（单位：秒） |
    | burn_damage | int | 着火状态下每秒扣的血量,不传的话默认是1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 在水中或者雨中不会生效，着火时间受生物装备、生物的状态影响。burn_damage取值范围是0~1000,小于0将取0，大于1000将取1000

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
comp.SetEntityOnFire(1, 2)
```



## SetEntityRide

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    驯服可骑乘生物

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | tamedEntityId | str | 要驯服的可骑乘生物id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 驯服信息会被存盘

- 示例

```python
# 驯服生物
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetEntityRide(playerId,entityId)
```



## SetEntityShareablesItems

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.shareableCompServer.ShareableComponentServer

- 描述

    设置生物可分享/可拾取的物品列表

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | items | list(itemdict) | 可分享/可拾取的物品列表 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 该接口修改minecraft:shareables的items定义
    - 仅当生物存在minecraft:shareables组件时才能调用该接口，例如狐狸、尸壳、猪灵等。若admire为True,则生物还需要有minecraft:admire_item组件。若barter为True,则生物还需有minecraft:behavior.barter行为。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateShareables(entityId)
shareableItems = []
shareableItems.append({
    "item": "minecraft:golden_sword",
    "auxValue": 0,
    "priority": 1,
    "pickupLimit": 1,
    "barter": True,
    "admire": True,
})
comp.SetEntityShareablesItems(shareableItems)
```



## SetEntityTamed

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.tameCompServer.TameComponentServer

- 描述

    设置生物驯服，需要配合 entityEvent组件使用。该类驯服不包含骑乘功能。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 驯服玩家Id |
    | tamedId | str | 被驯服的生物Id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 驯服一个生物，需要按以下步骤：
        1. 搭配修改生物json文件，使其能够被驯服：
          - 添加minecraft:tameable组件
          - 添加一个component group，里面放驯服后的行为
          - 添加一个event，添加刚刚添加的component group，并移除不需要的component group
        2. 使用SetEntityTamed使目标生物被驯服
        3. 使用TriggerCustomEvent触发驯服event
        如果是对原版可驯服生物使用，则无需按照第一步修改json，而是找到已有的event，在第三步中触发即可
    - 如修改苦力怕可被驯服，json做如下修改：
        ```json
        {
            "format_version": "1.8.0",
            "minecraft:entity": {
            "description": {
              "identifier": "minecraft:creeper",
              "is_spawnable": true,
              "is_summonable": true,
              "is_experimental": false
            },
            "component_groups": {
                ...
                //增加驯服状态
                "netease:creeper_tame":{
                  "minecraft:is_tamed": {
                  },
                  //跟随主人
                  "minecraft:behavior.follow_owner": {
                    "priority": 4,  //优先级要高于其他移动行为
                    "speed_multiplier": 1.0,
                    "start_distance": 10,
                    "stop_distance": 2
                  }
                }
              },
        
              "components": {
                ...
                //增加驯服组件，使用骨头驯服
                "minecraft:tameable": {
                  "probability": 0.33,
                  "tameItems": "bone",
                  "tame_event": {
                    "event": "netease:on_tame",
                    "target": "self"
                  }
                }
              },
        
              "events": {
                ...
                //增加驯服事件
                "netease:on_tame": {
                  //移除掉所有跟爆炸有关的逻辑
                  "remove": {
                    "component_groups": [
                      "minecraft:exploding",
                      "minecraft:charged_exploding",
                      "minecraft:forced_exploding",
                      "minecraft:forced_charged_exploding",
                      "minecraft:charged_creeper"
                    ]
                  },
                  //添加netease:creeper_tame
                  "add": {
                    "component_groups": [
                      "netease:creeper_tame"
                    ]
                  }
                }
              }
            }
        }
        ```

- 示例

```python
import mod.server.extraServerApi as serverApi
# 使tamedId被playerId驯服
tameComp = serverApi.GetEngineCompFactory().CreateTame(tamedId)
tameComp.SetEntityTamed(playerId,tamedId)
# 触发tamedId的netease:on_tame自定义event
envComp = serverApi.GetEngineCompFactory().CreateEntityEvent(tamedId)
envComp.TriggerCustomEvent(tamedId,'netease:on_tame')
```



## SetJumpPower

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.gravityCompServer.GravityComponentServer

- 描述

    设置生物跳跃力度，0.42表示正常水平

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | jumpPower | float | 跳跃力度，正常是0.42 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 生物跳跃力度影响生物跳跃高度；本接口调用时需要客户端加载完成，如在AddServerPlayer中，客户端还没加载完成，要延后执行才能生效

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGravity(entityId)
comp.SetJumpPower(0.84)
```



## SetMobKnockback

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actionCompServer.ActionCompServer

- 描述

    设置击退的初始速度，需要考虑阻力的影响

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | xd | float | x轴方向，用來控制角度 |
    | zd | float | z轴方向，用來控制角度 |
    | power | float | 用来控制水平方向的初速度 |
    | height | float | 竖直方向的初速度 |
    | heightCap | float | 向上速度阈值，当实体本身已经有向上的速度时需要考虑这个值，用来确保最终向上的速度不会超过heightCap |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | None | 无返回值 |

- 备注
    - 在damageEvent事件里面使用该接口时，需把damageEvent事件回调的knock参数设置为False
    - 该接口会触发OnKnockBackServerEvent事件，所以当需要在该事件中使用时，请编写逻辑避免循环调用

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAction(entityId)
comp.SetMobKnockback(0.1, 0.1, 1.0, 1.0, 1.0)
```



## SetMotion

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    设置生物（不含玩家）的瞬时移动方向向量

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motion | tuple(float,float,float) | 世界坐标系下的向量，该方向为世界坐标系下的向量，以x,z,y三个轴的正方向为正值，可以通过当前生物的rot组件判断目前玩家面向的方向，可在开发模式下打开F3观察数值变化。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 在damageEvent事件里面使用该接口时，需把damageEvent事件回调的knock参数设置为False

- 示例

```python
import mod.server.extraServerApi as serverApi
# 使生物向准星的方向突进一段距离
rotComp = serverApi.GetEngineCompFactory().CreateRot(entityId)
rot = rotComp.GetRot()
x, y, z = serverApi.GetDirFromRot(rot)
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.SetMotion((x * 5, y * 5, z * 5))
# rot 和 世界坐标系关系
#               ^ x -90°
#               |
# 180°/-180  ----------> z 0°
#               | 90°
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.actorMotionCompClient.ActorMotionComponentClient

- 描述

    设置瞬时的移动方向向量，用于本地玩家

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motion | tuple(float,float,float) | 世界坐标系下的向量，该方向为世界坐标系下的向量，以x,z,y三个轴的正方向为正值，可以通过当前玩家的rot组件判断目前玩家面向的方向，可在开发模式下打开F3观察数值变化。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如果频繁快速修改本地玩家的瞬时移动向量，可能会触发引擎服务端的反作弊机制（例如掉落伤害），需要频繁快速修改时最好搭配服务端SetMotion同步修改

- 示例

```python
import mod.client.extraClientApi as clientApi
# 使玩家向准星的方向突进一段距离
localPlayerId = clientApi.GetLocalPlayerId()
rotComp = clientApi.GetEngineCompFactory().CreateRot(localPlayerId)
rot = rotComp.GetRot()
x, y, z = clientApi.GetDirFromRot(rot)
motionComp = clientApi.GetEngineCompFactory().CreateActorMotion(localPlayerId)
motionComp.SetMotion((x * 5, y * 5, z * 5))
# rot 和 世界坐标系关系
#               ^ x -90°
#               |
# 180°/-180  ----------> z 0°
#               | 90°
```



## SetMoveSetting

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.moveToCompServer.MoveToComponentServer

- 描述

    寻路组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 寻路目标位置 |
    | speed | float | 移动速度，指正常移动速度的倍率。如1.0表示正常速度，2.0表示两倍速 |
    | maxIteration | int | 寻路算法最大迭代次数 默认200 |
    | callback | function | 寻路结束回调函数 |

- 返回值

    无

- 备注
    - 使用该接口时，需要在生物中配置有寻路的json组件。配置寻路json组件后，该接口会自动选择相应类型的寻路
        目前支持的寻路json组件包括：
        - minecraft:navigation.walk
            陆地寻路，与原版僵尸的寻路相同
        - minecraft:navigation.generic
            水陆寻路，支持陆地与水中，与原版溺尸的寻路相同
        - minecraft:navigation.climb
            陆地寻路，但是支持爬墙，与原版蜘蛛的寻路相同。这种寻路可能会被头顶方块阻挡，一直无法抵达目的地
        - minecraft:navigation.fly
            空中寻路，与原版鹦鹉的寻路相同
        以上的寻路都需要搭配一些其他json组件（例如movement）使用，具体可以参考NavigationMod的示例
        上面没有提到的navigation类型暂不支持，例如minecraft:navigation.float（如原版恶魂），minecraft:navigation.hover（如原版蜜蜂）
    - 不同的生物拥有不同的默认最大跟随距离，若要寻路的目标点距离大于此值引擎会拒绝寻路，要修改该距离可以通过在entity的json中配置.
        ```json
        {
          "format_version": "1.8.0",
          "minecraft:entity": {
              "components": {
                  "minecraft:follow_range": {
                    "value": 48,
                    "max": 48
                  }
              }
          }
        }
        ```
    - 关于maxIteration参数
        该参数会影响实际寻到路径的长度。若寻路算法迭代一定次数后，未寻到目标点，会返回局部最优解，即生物只会走到半路。
        在无大型障碍物的情况下，参数对应的参考寻路距离如下：该参数默认值200，最大值2000,请开发者根据实际情况选择。
        | maxIteration | 与目标点直线距离 |
        | ------------ | ---------------- |
        | 200          | 13               |
        | 500          | 20               |
        | 1000         | 30               |
        | 2000         | 43               |
    - 关于callback函数
        该函数需要接受两个参数，第一个参数为寻路的entityId，类型str，第二个参数为寻路结果，类型int
        （玩家获取到的位置比地面会高1.62格，若以玩家位置为目标点需要先把y轴减去1.62，否则callback会一直返回1）
        | 结果 | 说明                                                         |
        | ---- | ------------------------------------------------------------ |
        | -3   | 寻路失败，大于跟随距离，或者生物周围没有可行走位置，或者对正在寻路的飞行系生物使用       |
        | -2   | 寻路失败，生物没有寻路组件（指minecraft:navigation）         |
        | -1   | 寻路失败，参数错误，或生物不存在                             |
        | 0    | 寻路完成。到达设定的目标点                                   |
        | 1    | 寻路完成，但未到达目标点（可能由于maxIteration参数偏小）     |
        | 2    | 寻路中断。中途遇到障碍物被阻碍                               |
        | 3    | 寻路中断。被生物原版寻路行为覆盖，或寻路未结束时重复调用moveTo组件。<br>若生物的移速太低（真实速度小于0.3格每秒），也会被当成寻路被卡住，返回该错误码 |
    - 对于各种类型寻路的生物，还需要满足以下初始条件：
        1. 陆地寻路，水陆寻路与爬墙寻路：需要满足以下任一条件：
            - 生物着地
            - 生物正在骑乘，并且骑乘物着地
            - 生物在液体中
            - 生物是凋零
        2. 飞行寻路：需要满足以下任一条件：
            - 不在骑乘状态
            - 在液体中
            - 生物着地
            - json配置中的can_path_from_air属性为true
    - demo简介：
        聊天栏输入walk/generic/climb/fly会原地生成一个使用对应navigation json组件的生物，然后跑到其他位置，再输入go，会将刚才生成的生物导航到玩家当前位置。
        这4种示例生物的行为json可以在NavigationMod_behavior/entities目录查看。
        4种示例生物的最大寻路距离都设置为了48格。

- 示例

```python
from mod_log import logger as logger
def myCallback(entityId, result):
    if result in (-1,-2,-3):
        logger.info('[error] [SetMoveSetting] failed')
    elif result==0:
        logger.info('[info] [SetMoveSetting] success')
    elif result in (1,2,3):
        logger.info('[warn] [SetMoveSetting] terminated')

import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateMoveTo(entityId)
comp.SetMoveSetting((x,y,z),2.0,200,myCallback)
```



## SetPersistence

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.persistenceCompServer.PersistenceCompServer

- 描述

    设置实体是否持久化。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isPersistent | bool | True为设置实体持久化，False为设置实体不持久化。 |

- 返回值

    无

- 备注
    - 游戏中，实体默认持久化，若设置不持久化，则实体会在区块卸载和退出存档时被删除，不会存档。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePersistence(entityId)
comp.SetPersistence(True)
```



## SetRidePos

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    设置生物骑乘位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | tamedEntityId | str | 可骑乘生物id |
    | pos | tuple(float,float,float) | 骑乘时挂接点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetRidePos(entityId,(1,1,1))
```



## SetRiderRideEntity

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.rideCompServer.RideCompServer

- 描述

    设置实体骑乘生物（或者船与矿车）

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | riderId | str | 骑乘生物id |
    | riddenEntityId | str | 被骑乘生物id。要求被骑乘生物的定义中具有minecraft:rideable组件，且组件中family_types含有可骑乘者的类型声明 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 通常需要配合SetEntityRide、SetControl一起使用，需要被骑乘生物json中骑乘组件支持骑乘者的生物类型
        当被控制的entity有多个位置时且开发者想要添加多个玩家时，第一个被添加的玩家会被引擎默认设置为控制者

- 示例

```python
# 骑上坐骑
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRide(entityId)
comp.SetRiderRideEntity(playerId,rideEntityId)
```



## SetStepHeight

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.attrCompServer.AttrCompServer

- 描述

    设置玩家前进非跳跃状态下能上的最大台阶高度, 默认值为0.5625，1的话表示能上一个台阶

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | stepHeight | float | 最大高度，需要大于0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 为了避免因浮点数误差导致错误，设置的时候通常会增加1/16个方块大小，即0.0625。所以此处我们设置2.0625。游戏中默认值是0.5625，即半格高度。
    - 只对玩家生效，无法修改其它实体该属性
    - 修改后不影响跳跃逻辑及跳跃高度，并不会因此而跳到更高，因此在某些特定情况下，你可以走上方块但跳不上去。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAttr(entityId)
#如果前面放置有两格高的方块，玩家按前进能直接上去，无须跳跃
comp.SetStepHeight(2.0625)
```



## StartEntityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    启动实体（不含玩家）身上的某个运动器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | motionId | int | 要启动的某个运动器的ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功启动 |

- 示例

```python
import mod.server.extraServerApi as serverApi
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.StartEntityMotion(mID)
```



## StopEntityMotion

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.actorMotionCompServer.ActorMotionComponentServer

- 描述

    停止实体（不含玩家）身上的某个运动器

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
motionComp = serverApi.GetEngineCompFactory().CreateActorMotion(entityId)
motionComp.StopEntityMotion(mID)
```



## TriggerCustomEvent

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.entityEventCompServer.EntityEventComponentServer

- 描述

    触发生物自定义事件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 生物Id |
    | eventName | str | 事件名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 触发苦力怕爆炸
        在苦力怕的entity json文件中`events`字段下增加如下事件,然后在mod中运行示例代码：
        ```json
        "netease:custom_exploading":{
                  "sequence": [
                    {
                      "filters": {
                    "test": "has_component",
                        "operator": "!=",
                        "value": "minecraft:is_charged"
                      },
                      "add": {
                        "component_groups": [
                          "minecraft:forced_exploding"
                        ]
                      }
                    },
                    {
                      "filters": {
                        "test": "has_component",
                        "value": "minecraft:is_charged"
                      },
                      "add": {
                        "component_groups": [
                          "minecraft:forced_charged_exploding"
                        ]
                      }
                    }
                  ]
                }
        ```
    - 触发事件所添加或移除的component_groups，会在下一帧才真正生效。

- 示例

```python
import mod.server.extraServerApi as serverApi
#触发entity自定义event
eventName = "netease:custom_exploading"
comp = serverApi.GetEngineCompFactory().CreateEntityEvent(entityId)
comp.TriggerCustomEvent(entityId,eventName)
```

## 附加值

# 附加值

## GetAuxValue

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.auxValueCompServer.AuxValueComponentServer

- 描述

    获取射出的弓箭或投掷出的药水的附加值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | auxValue |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateAuxValue(entityId)
comp.GetAuxValue()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.auxValueCompClient.AuxValueComponentClient

- 描述

    获取射出的弓箭或投掷出的药水的附加值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 具体数值见wiki的“箭”及“药水”页面 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateAuxValue(entityId)
auxValue = comp.GetAuxValue()
```

