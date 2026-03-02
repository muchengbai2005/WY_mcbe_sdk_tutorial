# ModAPI 接口-方块

## 目录

- [告示牌](#告示牌)
- [容器](#容器)
- [属性](#属性)
- [床](#床)
- [方块几何体模型](#方块几何体模型)
- [方块实体](#方块实体)
- [方块状态与附加值](#方块状态与附加值)
- [方块调色板](#方块调色板)
- [渲染](#渲染)
- [红石](#红石)

---

## 告示牌

# 告示牌

## GetSignBlockText

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取告示牌（方块）的文本内容

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 告示牌的位置坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 告示牌上的文本内容 |

- 备注
    - 当输入的坐标位置的方块不是告示牌的时候，返回None

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
text = comp.GetSignBlockText(pos)
print "GetSignBlockText text={}".format(text)
```



## SetSignBlockText

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置告示牌（方块）的文本内容

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 告示牌的位置坐标 |
    | text | str | 想要设置的文本内容 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
suc = comp.SetSignBlockText(pos, "文本内容")
print "SetSignBlockText suc={}".format(suc)
```

## 容器

# 容器

## GetChestBoxSize

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chestContainerCompServer.ChestContainerCompServer

- 描述

    获取箱子容量大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | None | 该参数已废弃 |
    | pos | tuple(int,int,int) | 箱子位置 |
    | dimensionId | int | 箱子所在维度，可获取对应维度的常加载区块内箱子容量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 箱子大小，错误值-1 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChestBlock(levelId)
comp.GetChestBoxSize(None, (x, y, z), 0)
```



## GetChestPairedPosition

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取与箱子A合并成一个大箱子的箱子B的坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 箱子A的位置坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int)或None | 箱子B的位置坐标，假如输入的箱子A坐标上的方块不是箱子类方块或者没有和其他箱子方块组合成一个大箱子，就会返回None |

- 备注
    - 该接口使用创建组件时的playerId来定位具体维度，且仅可获取玩家附近的方块，若方块位置离玩家太远，可能无法获取到正确的返回信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
otherPos = comp.GetChestPairedPosition(pos)
if otherPos:
    print "GetChestPairedPosition success pos=%s otherPos=%s" % (str(pos), str(otherPos))
else:
    print "GetChestPairedPosition failed pos=%s" % (str(pos), )
```



## GetContainerItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取容器内的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 容器位置 |
    | slotPos | int | 容器槽位 |
    | dimensionId | int | 方块所在维度 |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 备注
    - 容器的具体类型包括：箱子，陷阱箱，潜影盒，漏斗，木桶，投掷器，发射器
    - 此接口不支持末影箱。对应的末影箱接口请参考 [GetEnderChestItem](#getenderchestitem)

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
comp.GetContainerItem((x,y,z), 0, 2)
```



## GetContainerSize

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取容器容量大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 箱子位置 |
    | dimensionId | int | 容器所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 箱子大小,错误值-1 |

- 备注
    - 此接口不支持末影箱，因为末影箱的size固定为27。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
comp.GetContainerSize((x, y, z), 0)
```



## GetEnderChestItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取末影箱内的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | slotPos | int | 容器槽位 |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetEnderChestItem(playerId, 0)
```



## GetInputSlotItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取熔炉输入栏物品, 支持使用下面参数清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 容器位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
itemName = comp.GetInputSlotItem((x, y, z), 1)
```



## GetOpenContainerItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取开放容器的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | containerId | int | [开放容器Id枚举](../../枚举值/OpenContainerId.md) |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 备注
    - 需要在事件[CraftItemOutputChangeServerEvent](../../事件/物品.html#CraftItemOutputChangeServerEvent)的监听函数里面才能获取正确的结果
    - 开放容器为临时容器，用来保存交互过程中的物品，如铁砧输入位，砂轮输入位

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetOpenContainerItem(playerId,serverApi.GetMinecraftEnum().OpenContainerId.AnvilInputContainer, True)
```



## GetOutputSlotItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取熔炉输出栏物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 容器位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
itemName = comp.GetOutputSlotItem((x, y, z), 1)
```



## GetPlayerUIItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    获取合成容器的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | slot | int | 容器槽位，含义见：[容器类型枚举](../../枚举值/PlayerUISlot.md) |
    | getUserData | bool | 是否获取userData，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |

- 备注
    - 合成容器包括工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台。
    - 所有合成容器槽位共享，不会根据不同容器重新排列

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.GetPlayerUIItem(playerId, slot, True)
```



## SetChestBoxItemExchange

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chestContainerCompServer.ChestContainerCompServer

- 描述

    交换箱子里物品的槽位

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | pos | tuple(int,int,int) | 箱子位置 |
    | slotPos1 | int | 箱子槽位1 |
    | slotPos2 | int | 箱子槽位2 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置成功返回True，失败返回False |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChestBlock(playerId)
comp.SetChestBoxItemExchange(playerId, (x,y,z), 0, 1)
```



## SetChestBoxItemNum

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.chestContainerCompServer.ChestContainerCompServer

- 描述

    设置箱子槽位物品数目

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | None | 该参数已废弃 |
    | pos | tuple(int,int,int) | 箱子位置 |
    | slotPos | int | 箱子槽位 |
    | num | int | 物品数目 |
    | dimensionId | int | 方块所在维度，可在对应维度的常加载区块设置方块 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateChestBlock(levelId)
comp.SetChestBoxItemNum(None, (x,y,z), 0, 10, 0)
```



## SetInputSlotItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    设置熔炉输入栏物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | 物品字典信息, 包含三种key: itemName, auxValue, count |
    | pos | tuple(int,int,int) | 容器位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功设置 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
comp.SetInputSlotItem({"itemName": "minecraft:iron_ore", "auxValue": 0, "count": 1}, (x, y, z), 1)
```



## SetPlayerUIItem

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    设置合成容器的物品

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | slot | int | 容器槽位，含义见：[容器类型枚举](../../枚举值/PlayerUISlot.md) |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a>，没有物品则返回None |
    | needBack | bool | 是否将容器槽位的已有物品放回至玩家背包中，默认为True。设置为False时，则会直接用itemDict中的物品覆盖容器槽位的已有物品。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 合成容器包括工作台、铁砧、附魔台、织布机、砂轮、切石机、制图台、锻造台。
    - 如果原槽位有物品，则会将原有物品放入玩家背包。如果玩家背包已满，则会在世界中玩家当前的位置生成对应的物品掉落物。
    - 注意，所有合成容器槽位共享，不会根据不同容器重新排列，没有打开容器或者打开了别的容器，该接口会返回False。
    - 下面情况视为清空特定槽位:itemDict为None，为{}, 或itemName为minecraft:air，或者count为0，同时needBack参数为False
    - 由于创造输出物品生成位比较特殊，该接口已经屏蔽了slot = 50的情况，即无法设置创造输出位的物品。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateItem(playerId)
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1, # 可填入0达到删除某槽位物品的效果
    'auxValue': 0,
}
comp.SetPlayerUIItem(playerId, slot, itemDict)
# 也可以直接使用 comp.SetPlayerUIItem(playerId, slot, None, False) 来清空物品
```



## SpawnItemToContainer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    生成物品到容器方块的物品栏

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | slotPos | int | 箱子槽位 |
    | blockPos | tuple(int,int,int) | 箱子位置 |
    | dimensionId | int | 容器所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 此接口不支持末影箱。对应的末影箱接口请参考 [SpawnItemToEnderChest](#spawnitemtoenderchest)
    - 下面情况视为清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0
    - 目前该接口支持的容器类型方块：箱子、潜影盒、漏斗、木桶、投掷器、发射器

- 示例

```python
import mod.server.extraServerApi as serverApi
itemDict = {
    'itemName': 'minecraft:bow',
    'count': 1, # 可填入0达到删除某槽位物品的效果
    'enchantData': [(serverApi.GetMinecraftEnum().EnchantType.BowDamage, 1),],
    'auxValue': 0,
    'customTips':'§c new item §r',
    'extraId': 'abc',
    'userData': { },
}
# 生成物品到容器的0号槽位，容器位于维度0，坐标为(x,y,z)
comp = serverApi.GetEngineCompFactory().CreateItem(levelId)
comp.SpawnItemToContainer(itemDict, 0, (x,y,z), 0)
```



## SpawnItemToEnderChest

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.itemCompServer.ItemCompServer

- 描述

    生成物品到末影箱

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | itemDict | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#物品信息字典">物品信息字典</a> |
    | slotPos | int | 末影箱槽位 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果 |

- 备注
    - 下面情况视为清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0

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
comp.SpawnItemToEnderChest(itemDict, 0)
```

## 属性

# 属性

## GetBlockBasicInfo

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取方块基本信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | <a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块基本信息字典#方块基本信息字典">方块基本信息字典</a> |

- 备注
    - 基本信息字典中部分字段只在自定义方块时加上指定组件才会取到数据，具体见<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块基本信息字典#方块基本信息字典">方块基本信息字典</a>

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockDict = comp.GetBlockBasicInfo("minecraft:stone")
```



## SetBlockBasicInfo

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置方块基本信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块identifier |
    | infoDict | dict | 方块的<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#方块基本信息字典#方块基本信息字典">方块基本信息字典</a> |
    | auxValue | int | 方块附加值，默认是0 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 目前本接口支持的属性有 destroyTime:硬度；explosionResistance:爆炸抗性；loot:掉落属性；tier:挖掘属性；solid:是否实心；当方块json配置里有对应的组件才能修改

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockDict = comp.SetBlockBasicInfo("minecraft:stone", {"blockLightEmission":1,
"blockLightAbsorption":1,
"solid":False,
"tier":{"level":3}})
```

## 床

# 床

## GetBedColor

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    获取床（方块）的颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 床的位置坐标（床占地两格，任意一个格子都可以） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | [ItemColor枚举](../../枚举值/ItemColor.md) |

- 备注
    - 当输入的坐标位置的方块不是床的时候，返回-1

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
color = comp.GetBedColor(pos)
print "GetBedColor color={}".format(color)
```



## SetBedColor

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置床（方块）的颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 床的位置坐标（床占地两格，任意一个格子都可以） |
    | color | int | [ItemColor枚举](../../枚举值/ItemColor.md) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
suc = comp.SetBedColor(pos, serverApi.GetMinecraftEnum().ItemColor.Blue)
print "SetBedColor suc={}".format(suc)
```

## 方块几何体模型

# 方块几何体模型

## CombineBlockBetweenPosToGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockGeometryCompClient.BlockGeometryCompClient

- 描述

    根据输入的两个位置，搜索这两个位置之间的所有方块，并将这些方块合并和转换为能用于实体的几何体模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | startPos | tuple(int,int,int) | 起始位置 |
    | endPos | tuple(int,int,int) | 终点位置 |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | unsupportedMode | int | 不支持方块处理方式枚举，可选参数，可输入的值为0、1。默认的值为0。如果方块调色板中有不支持转变为几何体的方块的话，将按以下方式处理：0：跳过不支持的方块继续生成。1：停止生成 |
    | useStructureVoid | bool | 是否使用结构空位代替空气方块，可选参数，默认值为False。True表示使用结构空位，False表示不使用结构空位。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回合并过程中生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 如果之前已经拥有一个相同名称几何体模型，合并出来的新模型会覆盖之前的模型。因此需要注意，每次合并不同外观的模型时geometryName都应该互不相同。
    - 如果每次合并的模型都是外观相同的模型，则我们建议使用相同的geometryName,以节省存储模型的内存。当然，最优的情况下是尽量复用之前已经创建的方块几何体模型，而不是重复合并新的模型。
    - 目前尚不支持的方块类型有 (后续版本将陆续支持)：
        1. 自定义方块实体外观（见开发指南-玩法开发-自定义游戏内容-自定义方块-自定义方块实体外观）
        2. 微缩方块（见开发指南-玩法开发-自定义游戏内容-微缩方块）
        3. 火方块，水方块
        4. 花盆
        5. 钟
        6. 末地传送门，末地折跃门
        7. 屏障
        8. 潮涌核心
        9. 旗帜

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
palette = blockGeometryComp.CombineBlockBetweenPosToGeometry((200,64,200),(201,65,202),"my_block_geometry")
```



## CombineBlockFromPosListToGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockGeometryCompClient.BlockGeometryCompClient

- 描述

    根据输入的方块位置列表，搜索这些位置的所有方块，并将这些方块合并和转换为能用于实体的几何体模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | posList | list(tuple(int,int,int)) | 方块位置列表 |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | unsupportedMode | int | 不支持方块处理方式枚举，可选参数，可输入的值为0、1。默认的值为0。如果方块调色板中有不支持转变为几何体的方块的话，将按以下方式处理：0：跳过不支持的方块继续生成。1：停止生成 |
    | useStructureVoid | bool | 是否使用结构空位代替空气方块，可选参数，默认值为False。True表示使用结构空位，False表示不使用结构空位。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockPaletteComponent | 返回合并过程中生成的方块调色板实例，如创建失败则返回None |

- 备注
    - 如果之前已经拥有一个相同名称几何体模型，合并出来的新模型会覆盖之前的模型。因此需要注意，每次合并不同外观的模型时geometryName都应该互不相同。
    - 如果每次合并的模型都是外观相同的模型，则我们建议使用相同的geometryName,以节省存储模型的内存。当然，最优的情况下是尽量复用之前已经创建的方块几何体模型，而不是重复合并新的模型。
    - 目前尚不支持的方块类型有 (后续版本将陆续支持)：
        1. 自定义方块实体外观（见开发指南-玩法开发-自定义游戏内容-自定义方块-自定义方块实体外观）
        2. 微缩方块（见开发指南-玩法开发-自定义游戏内容-微缩方块）
        3. 火方块，水方块
        4. 花盆
        5. 钟
        6. 末地传送门，末地折跃门
        7. 屏障
        8. 潮涌核心
        9. 旗帜

- 示例

```python
import mod.client.extraClientApi as clientApi
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
palette = blockGeometryComp.CombineBlockFromPosListToGeometry([(200,64,200),(201,65,202)],"my_block_geometry")
```



## CombineBlockPaletteToGeometry

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockGeometryCompClient.BlockGeometryCompClient

- 描述

    将BlockPalette中的所有方块合并并转换为能用于实体的几何体模型。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockPalette | BlockPaletteComponent | 方块调色板，由GetBlockPaletteBetweenPos以及GetBlockPaletteFromPosList接口获取 |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id。 |
    | unsupportedMode | int | 不支持方块处理方式枚举，可选参数，可输入的值为0、1。默认的值为0。如果方块调色板中有不支持转变为几何体的方块的话，将按以下方式处理：0：跳过不支持的方块继续生成。1：停止生成 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 生成成功后返回几何体模型的名称，生成失败返回None。几何体模型名称与输入的参数geometryName一致。 |

- 备注
    - 如果之前已经拥有一个相同名称几何体模型，合并出来的新模型会覆盖之前的模型。因此需要注意，每次合并不同外观的模型时geometryName都应该互不相同。
    - 如果每次合并的模型都是外观相同的模型，则我们建议使用相同的geometryName,以节省存储模型的内存。当然，最优的情况下是尽量复用之前已经创建的方块几何体模型，而不是重复合并新的模型。
    - 目前尚不支持的方块类型有 (后续版本将陆续支持)：
        1. 自定义方块实体外观（见开发指南-玩法开发-自定义游戏内容-自定义方块-自定义方块实体外观）
        2. 微缩方块（见开发指南-玩法开发-自定义游戏内容-微缩方块）
        3. 火方块，水方块
        4. 花盆
        5. 钟
        6. 末地传送门，末地折跃门
        7. 屏障
        8. 潮涌核心
        9. 旗帜

- 示例

```python
import mod.client.extraClientApi as clientApi
blockComp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = blockComp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
blockGeometryComp = clientApi.GetEngineCompFactory().CreateBlockGeometry(levelId)
geometryName = blockGeometryComp.CombineBlockPaletteToGeometry(palette,"my_block_geometry")
print geometryName
```



## EnableActorBlockGeometryTransparent

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置是否允许实体的方块几何体模型产生透明度，允许开启后通过调节方块几何体的透明度将会使得方块几何体模型变得透明。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id。 |
    | enable | bool | 是否允许实体的方块几何体模型产生透明度，True表示允许，False表示不允许。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 允许方块几何体模型产生透明度
print actorRenderComp.EnableActorBlockGeometryTransparent("my_block_geometry", True)
# 调节方块几何体模型的透明度为0.5
print actorRenderComp.SetActorBlockGeometryTransparency("my_block_geometry", 0.5)
```



## SetActorBlockGeometryOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置实体的方块几何体模型的位置偏移。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | offset | tuple(float,float,float) | 方块几何体模型相对实体的位置偏移值，默认为(0, 0, 0)。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
print actorRenderComp.SetActorBlockGeometryOffset("my_block_geometry", (1,1,1))
```



## SetActorBlockGeometryRotation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置实体的方块几何体模型的旋转角度。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id |
    | rotation | tuple(float,float,float) | 方块几何体模型相对实体的旋转角度，默认为(0, 0, 0)，分别表示绕x,y,z轴的旋转角度，旋转顺序按z,x,y顺序旋转。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
print actorRenderComp.SetActorBlockGeometryRotation("my_block_geometry", (90,0,0))
```



## SetActorBlockGeometryTransparency

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.actorRenderCompClient.ActorRenderCompClient

- 描述

    设置实体的方块几何体模型的透明度。注意，只有调用接口EnableActorBlockGeometryTransparent开启了方块几何体模型的透明度后该接口才会生效。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | geometryName | str | 几何体模型的名称，用于标识每个几何体模型，相当于是该模型的id。 |
    | transparent | float | 方块几何体模型的透明度，范围值为[0,1]，超过这个范围的值将会被截取为0或1。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功，成功返回True，失败返回False。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
actorRenderComp = clientApi.GetEngineCompFactory().CreateActorRender("-4294967295")
# 允许方块几何体模型产生透明度
print actorRenderComp.EnableActorBlockGeometryTransparent("my_block_geometry", True)
# 调节方块几何体模型的透明度为0.5
print actorRenderComp.SetActorBlockGeometryTransparency("my_block_geometry", 0.5)
```

## 方块实体

# 方块实体

## CleanBlockTileEntityCustomData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    清空指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 绑定TileEntity的特殊方块的位置坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 清空结果，假如对应位置的block不存在或者没有绑定的TileEntity，就会失败 |

- 备注
    - 该接口使用创建组件时的playerId来定位具体维度，且仅可获取玩家附近的方块，若方块位置离玩家太远，可能无法获取到正确的返回信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
suc = comp.CleanBlockTileEntityCustomData(pos)
print "CleanBlockTileEntityCustomData pos=%s suc=%s" % (str(pos), suc)
```



## CreateFrameEffectForBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    在自定义方块实体上创建序列帧特效，创建后该接口返回序列帧特效的Id，利用该Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | path | str | 特效资源路径，不需要后缀名，路径为resource_pack/textures文件夹下或resource_pack/effects下的序列帧资源文件的路径，路径名分别以"textures/"开头或"effects/"开头。路径名以"textures/"开头时不需要加.json后缀名， 路径名以"effects/"开头时需要加.json后缀名。 |
    | frameKeyName | str | 该序列帧特效的自定义键值名称，创建序列帧特效后可以使用该键值名称通过GetFrameEffectIdInBlockEntity接口来获取序列帧特效的id。 |
    | effectPos | tuple(float,float,float) | 特效相对自定义方块实体的位置，即以自定方块实体所在的位置为原点的坐标系下的坐标位置。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 创建成功则返回序列帧特效的Id，创建失败则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 以自定义方块实体所在的位置为原点，在这个原点上的坐标(1.0, 1.0, 1.0)的位置上使用resource_pack/textures下的资源创建序列帧特效
id1 = comp.CreateFrameEffectForBlockEntity(pos, "textures/sfxs/snow", "my_frame1", (1.0, 1.0, 1.0))
# 以自定义方块实体所在的位置为原点，在这个原点上的坐标(1.0, 1.0, 1.0)的位置上使用resource_pack/effects下的资源创建序列帧特效
id2 = comp.CreateFrameEffectForBlockEntity(pos, "effects/sfxs/snow.json", "my_frame2", (1.0, 1.0, 1.0))
```



## CreateParticleEffectForBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    在自定义方块实体上创建粒子特效，创建后该接口返回粒子特效的Id，利用该Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。若自定义方块实体已存在键值名称相同的特效，则不会创建新的特效，接口返回已有的特效Id。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | path | str | 特效资源路径，需要加上后缀名（一般是json)。路径为resource_pack/effects文件下的粒子特效json文件路径，路径名以"effects/"开头。 |
    | particleKeyName | str | 该粒子特效的自定义键值名称，创建粒子特效后可以使用该键值名称通过GetParticleEffectIdInBlockEntity接口来获取粒子特效的id。 |
    | effectPos | tuple(float,float,float) | 特效相对自定义方块实体的位置，即以自定方块实体所在的位置为原点的坐标系下的坐标位置。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 创建成功则返回粒子特效的Id，创建失败则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 以自定义方块实体所在的位置为原点，在这个原点上的坐标(1.0, 1.0, 1.0)的位置上创建粒子特效
id = comp.CreateParticleEffectForBlockEntity(pos, "effects/fire.json", "my_particle1", (1.0, 1.0, 1.0))
```



## GetBlockEntityData

<span style="display:inline;color:#ff5555">服务端</span>

<span id="0"></span>
method in mod.server.component.blockEntityExDataCompServer.BlockEntityExDataCompServer

- 描述

    用于获取可操作某个自定义方块实体数据的对象，操作方式与dict类似

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 方块所在位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BlockEntityData或None | 可操作该方块实体内数据的对象 |

- 备注
    - GetBlockEntityData返回None通常是由于该方块所在区块未加载、正在退出游戏、该方块不是自定义方块或该自定义方块的json中并未配置netease:block_entity组件。<br>在对GetBlockEntityData返回对象进行操作前，请先判断它是否为空，否则会导致```'NoneType' object has no attribute '__getitem__'```错误。
    - 支持python基本数据类型(int/float/string/bool/dict/list)，不支持tuple且**dict的key必须为字符串**
    - **存储list时，list内各项的数据类型应相同，否则将存储失败**。如[True, False]可成功存储，[True, 1, 0.5]会存储失败
    - **虽然返回的对象操作与dict相似，但并不支持嵌套存储，只允许形如blockEntityData['key'] = value的直接赋值。如blockEntityData["value5"] ["v1"] = 9或blockEntityData["value6"].append(True)的操作将无法成功存储数据。**
    - 存储整数时，若数值范围超过int所能表示的最大范围，将无法成功存储。建议将此类数值转为字符串进行存储。

- 示例

```python
import mod.server.extraServerApi as serverApi
# 设置
blockEntitycomp = serverApi.GetEngineCompFactory().CreateBlockEntityData(levelId)
dimension = 0
pos = (4, 3, 2)
# GetBlockEntityData在某些情况下会返回None，对返回结果进行操作前务必先判断它是否为空
blockEntityData = blockEntitycomp.GetBlockEntityData(dimension, pos)
# 存储数据
# 支持存储python基本数据类型(int/float/string/bool/dict/list)，不支持tuple，并且key必须为字符串
# 存储list时，list内各项的数据类型应相同，否则将存储失败
if blockEntityData:
    blockEntityData['value1'] = 10
    blockEntityData['value2'] = 3.5
    blockEntityData['value3'] = True
    blockEntityData['value4'] = "hello"
    blockEntityData['value5'] = {"v1": 10, "v2": 3.5, "v3": [0,1,2]}
    blockEntityData['value6'] = [True, False]
# 读取数据
if blockEntityData:
    value1 = blockEntityData['value1']
    value5 = blockEntityData['value5']
    # 不存在于方块实体中的数据将返回None
    valueNone = blockEntityData['valueNone']
```



<span id="1"></span>
method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    用于获取方块（包括自定义方块）的数据，数据只读不可写

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dimension | int | 维度 |
    | pos | tuple(int,int,int) | 方块所在位置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict或None | 方块实体内数据的对象 |

- 备注
    - **随着版本更迭，方块中包含的数据结构可能被微软团队调整，并且不会公告，使用该接口的开发者需注意版本更新时做好测试和兼容。数据编码为UTF-8
        适用于：[方块实体](https://minecraft-zh.gamepedia.com/%E6%96%B9%E5%9D%97%E5%AE%9E%E4%BD%93)
        特殊情况：末影箱的物品信息不能通过该接口获取

- 示例

```python
import mod.server.extraServerApi as serverApi
blockEntitycomp = serverApi.GetEngineCompFactory().CreateBlockInfo(levelId)
blockEntityData = blockEntitycomp.GetBlockEntityData(0, (4, 3, 2))
```



## GetBlockEntityMolangValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取自定义方块实体的Molang变量的值。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | variableName | str | molang变量的名称，以"variable."开头，并且不能包含超过两个"."。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 该molang变量的值，如该变量不存在，则返回None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.GetBlockEntityMolangValue(pos, "query.mod.idle")
```



## GetBlockTileEntityCustomData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 绑定TileEntity的特殊方块的位置坐标 |
    | key | str | 自定义key |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | any | 设定的value值，假如对应的数据不存在，则会返回None |

- 备注
    - 该接口使用创建组件时的playerId来定位具体维度，且仅可获取玩家附近的方块，若方块位置离玩家太远，可能无法获取到正确的返回信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
key = "owner"
val = comp.GetBlockTileEntityCustomData(pos, key)
print "GetBlockTileEntityCustomData pos=%s key=%s value=%s" % (str(pos), key, val)
```



## GetBlockTileEntityWholeCustomData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    读取指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据字典。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 绑定TileEntity的特殊方块的位置坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict或None | TileEntity自定义存储数据字典，假如没有任何额外存储数据，那么返回None或者空字典 |

- 备注
    - 该接口使用创建组件时的playerId来定位具体维度，且仅可获取玩家附近的方块，若方块位置离玩家太远，可能无法获取到正确的返回信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
data = comp.GetBlockTileEntityWholeCustomData(pos)
if not data:
    print "GetBlockTileEntityWholeCustomData pos=%s return empty" % (str(pos), )
else:
    print "GetBlockTileEntityWholeCustomData pos=%s return success" % (str(pos), )
if data:
    for key, val in data.iteritems():
        print "key=%s val=%s" % (key, str(val))
```



## GetFrameEffectIdInBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取在自定义方块实体中已创建的指定序列帧特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_frame_effects”所定义的特效；二是使用接口CreateFrameEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/序列帧中的接口对该序列帧特效进行播放、设置位置、大小等操作。与实体的序列帧特效创建方式类似。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | frameKeyName | str | 序列帧特效的自定义键值名称，即：netease_frame_effects: {  "keyName" : {"path“：“textures/sfxs/xxx.json”, "pos": [1.0, 1.0, 1.0f]} } 中的"keyName"，又或者是通过CreateFrameEffectForBlockEntity创建特效时该接口中填写的frameKeyName参数。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 返回序列帧特效的Id，该键值不存在则返回None |

- 示例

```python
# 假设自定义方块实体定义了以下特效
# "minecraft:client_entity": {
#                  ...
#       "netease_frame_effects":{
#             "my_frame1" : { "path" : "textures/sfxs/snow.json", "pos": [1.0 , 1.0 , 1.0]},
#             ...
#        }
# }
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 获取名为"my_frame1"这个预设特效的特效Id
id = comp.GetFrameEffectIdInBlockEntity(pos, "my_frame1")
```



## GetParticleEffectIdInBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取在自定义方块实体中已创建的指定粒子特效的Id，已创建的特效分为两种：一是通过resource_pack/entity/下的实体json文件中使用“netease_particle_effects”所定义的特效；二是使用接口CreateParticleEffectForBlockEntity创建的特效。 返回的特效Id可以使用特效/粒子中的接口对该粒子特效进行播放、设置位置、大小等操作。与实体的粒子特效创建方式类似。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | particleKeyName | str | 粒子特效的自定义键值名称，即：netease_particle_effects: {  "keyName" : {"path“：“effects/xxx.json”, "pos": [1.0, 1.0, 1.0f]} } 中的"keyName"，又或者是通过CreateParticleEffectForBlockEntity创建特效时该接口中填写的particleKeyName参数。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | 返回粒子特效的Id，该键值不存在则返回None |

- 示例

```python
# 需要自定义方块实体的entity.json文件具有如下定义:
# "minecraft:client_entity": {
#                  ...
#       "netease_particle_effects":{
#             "my_particle1" : { "path" : "effects/fire.json", "pos": [1.0 , 1.0 , 1.0]},
#             ...
#        }
# }
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 获取名为"my_particle1"这个预设特效的特效Id
id = comp.GetParticleEffectIdInBlockEntity(pos, "my_particle1")
```



## RemoveFrameEffectInBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    移除在自定义方块实体上创建的序列帧特效。移除后的特效Id将会失效。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | frameKeyName | str | 该序列帧特效的自定义键值名称。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 移除成功返回True, 该键值不存在则返回False |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 移除键值名为"my_frame1"的特效
comp.RemoveFrameEffectInBlockEntity(pos, "my_frame1")
```



## RemoveParticleEffectInBlockEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    移除在自定义方块实体上创建的粒子特效。移除后的特效Id将会失效。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | particleKeyName | str | 该粒子特效的自定义键值名称。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 移除成功返回True, 该键值不存在则返回False |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 移除键值名为"my_particle1"的特效
comp.RemoveParticleEffectInBlockEntity(pos, "my_particle1")
```



## SetBlockEntityMolangValue

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体的Molang变量，与实体的molang变量作用相同。目前主要用于控制自定义实体的动画状态转变。Molang变量的定义方式与原版实体的Molang变量定义方法相同。详细可参考自定义方块实体动画的教学文档。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | variableName | str | molang变量的名称，以"variable."开头，并且不能包含超过两个"."。 |
    | value | float | molang变量的值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 注意，自定义方块实体的Molang变量与微软原版的Molang变量定义和使用方式相同， 因此不需要调用实体/molang/中的Register接口及UnRegister接口进行注册和反注册，只需在entity.json中进行定义和初始化即可，这点与微软原版实体的使用方法相同，可参考微软原版实体的entity.json文件。

- 示例

```python
# 需要自定义方块实体的entity.json文件具有如下定义:
# "minecraft:client_entity": {
#                  ...
#       "scripts":{
#             // 注册"variable.mod_is_moving"这个molang变量并将其值初始化为1.0
#             "initialize": [  "variable.mod_is_moving = 1.0;" ],
#             ...
#        }
# }
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 设置molang变量的值来转变动画状态
comp.SetBlockEntityMolangValue(pos, "variable.mod_is_moving", 2.0)
```



## SetBlockTileEntityCustomData

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockInfoCompServer.BlockInfoComponentServer

- 描述

    设置指定位置的特殊方块（箱子、头颅、熔炉、花盆等）绑定的TileEntity内存储的自定义数据。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 绑定TileEntity的特殊方块的位置坐标 |
    | key | str | 自定义key |
    | value | any | 支持python基本数据类型，tuple不支持 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置结果，假如对应位置的block不存在或者没有绑定的TileEntity，就会设置失败 |

- 备注
    - 该接口使用创建组件时的playerId来定位具体维度，且仅可获取玩家附近的方块，若方块位置离玩家太远，可能无法获取到正确的返回信息。

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockInfo(playerId)
pos = (-1, 4, 34)
suc = comp.SetBlockTileEntityCustomData(pos, "owner", "Jack")
print "SetBlockTileEntityCustomData pos=%s suc=%s" % (str(pos), suc)
```



## SetEnableBlockEntityAnimations

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置是否开启自定义方块实体的动画效果，开启之后，自定义实体方块会按照实体文件中animation_controller所定义的动画状态机进行动画播放。关闭之后，则会停止所有动画播放。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | enable | bool | 是否开启自定义方块实体的动画播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
comp.SetEnableBlockEntityAnimations(pos, True)
```

## 方块状态与附加值

# 方块状态与附加值

## GetBlockAuxValueFromStates

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockStateCompServer.BlockStateComponentServer

- 描述

    根据方块名称和<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>获取方块附加值AuxValue

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称 |
    | states | dict | 方块状态 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 方块附加值AuxValue，异常时为-1 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
states = comp.GetBlockAuxValueFromStates("minecraft:hopper", {"facing_direction": 0, "toggle_bit": 0})
```



## GetBlockStates

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockStateCompServer.BlockStateComponentServer

- 描述

    获取<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块位置 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块状态，异常时为None |

- 备注
    - 仅可获取到已加载区块内的方块状态，支持获取对应维度的常加载区块内方块状态

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
comp.GetBlockStates((4,4,3), 0)
```



## GetBlockStatesFromAuxValue

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockStateCompServer.BlockStateComponentServer

- 描述

    根据方块名称和方块附加值AuxValue获取<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称 |
    | auxValue | int | 方块附加值AuxValue |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块状态，异常时为None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
states = comp.GetBlockStatesFromAuxValue('minecraft:sapling', 9)
```



## SetBlockStates

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.blockStateCompServer.BlockStateComponentServer

- 描述

    设置<a href="../../../../mcguide/20-玩法开发/10-基本概念/1-我的世界基础概念.html#物品信息字典#方块状态">方块状态</a>

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块位置 |
    | data | dict | 方块状态 |
    | dimensionId | int | 方块所在维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 仅可设置已加载区块内的方块状态，支持设置对应维度的常加载区块内方块状态

- 示例

```python
# 将白色羊毛设置为橙色羊毛
pos = (4,4,3)
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlockState(levelId)
state = comp.GetBlockStates(pos, 0) # state = { 'color': 'white' }
state['color'] = 'orange'
comp.SetBlockStates(pos, state, 0)
```

## 方块调色板

# 方块调色板

## DeleteBlockInBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    删除方块调色板BlockPalette中某个类型的方块。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称。 |
    | auxValue | int | 方块附加值。可选参数，默认值为-1。不填写方块附加值时删除所有符合这个名称的方块。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回成功删除的方块数量 |

- 备注
    - 在删除门或者床的类型方块时，请使用床头的附加值或者门的下半部分的附加值进行删除。使用床尾及门的上半部分的附加值时删除过程将会无效。

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
count = palette.DeleteBlockInBlockPalette("minecraft:grass", 0)
print count
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
count = palette.DeleteBlockInBlockPalette("minecraft:grass", 0)
print count
```



## DeserializeBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    反序列化方块调色板数据字典中的数据，用于方块调色板在客户端及服务端的事件数据之间传输。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dataDict | dict | 方块调色板数据字典。使用接口SerializeBlockPalette获取。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 反序列化是否成功，成功返回True，失败返回False |

- 示例

```python
# 客户端调用
# 事件回调函数中
def onGetBlockPalette(self, data):
    dataDict = data['data']
    comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
    newPalette = comp.GetBlankBlockPalette()
    newPalette.DeserializeBlockPalette(dataDict)

# 服务端调用
# 事件回调函数中
def onGetBlockPalette(self, data):
    dataDict = data['data']
    comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
    newPalette = comp.GetBlankBlockPalette()
    newPalette.DeserializeBlockPalette(dataDict)
```



## GetBlockCountInBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    获取方块调色板BlockPalette中某个类型的方块的数量。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称 |
    | auxValue | int | 方块附加值。可选参数，默认值为-1。不填写方块附加值时获取所有符合这个名称的方块的数量。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回该类型的方块数量 |

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
count = palette.GetBlockCountInBlockPalette("minecraft:grass", 0)
print count
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
count = palette.GetBlockCountInBlockPalette("minecraft:grass", 0)
print count
```



## GetLocalPosListOfBlocks

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    获取方块调色板中某种方块的相对位置列表。方块调色板记录了多个方块组成的一个三维空间下的方块组合，而相对位置则指的是，以这些方块中最小坐标的方块所在位置作为原点的坐标轴下的相对位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块名称。 |
    | auxValue | int | 方块附加值。可选参数，默认值为-1。不填写方块附加值时则获取所有符合这个方块名称的方块的相对位置列表。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | list(tuple(int,int,int)) | 返回该类型方块的所占据相对位置列表。如该方块不存在，则返回空列表。 |

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
result = palette.GetLocalPosListOfBlocks("minecraft:grass")
print result
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
result = palette.GetLocalPosListOfBlocks("minecraft:grass")
print result
```



## GetVolumeOfBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    获取方块调色板BlockPalette所占据的长方体的长宽高。长指的是在方块调色板BlockPalette在世界坐标中占据的x轴方向的长度，宽指的是z轴方向的长度，高指的是y轴方向的长度。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(int,int,int) | 返回方块调色板BlockPalette的长宽高元组，按顺序分别为长，宽，高的数值。 |

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
result = palette.GetVolumeOfBlockPalette()
print result
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
result = palette.GetVolumeOfBlockPalette()
print result
```



## ReplaceAirByStructureVoid

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    设置是否将方块调色板BlockPalette中所有空气替换为结构空位。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否将空气方块替换为结构空位。True为替换为结构空位，False为使用空气方块 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 替换是否成功，成功返回True，失败返回False |

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
print palette.ReplaceAirByStructureVoid(True)
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
print palette.ReplaceAirByStructureVoid(True)
```



## ReplaceBlockInBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    替换方块调色板BlockPalette中某个类型的方块。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | newblockName | str | 新的方块名称。 |
    | newBlockAux | int | 新的方块的附加值。 |
    | oldBlockName | str | 将要被替换的方块名称。 |
    | oldBlockAux | int | 将要被替换的方块名称的附加值。可选参数。不填写附加值时将替换所有符合这个名称的方块。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回成功替换的方块数量 |

- 备注
    - 注意，在替换方块时，如果新的方块使用的是床方块以及床尾的附加值，或者是门方块以及的门的上半部分方块的附加值时，则该替换过程将会被忽略，请使用床头或门的下半部分的附加值进行替换。同理，被替换的方块也请使用床头或者门的上半部分的附加值。
    - 注意，在使用床方块以及床头的附加值，或者是门方块以及门的下半部分的附加值替换其他方块后，使用接口SetBlockByBlockPalette设置该调色板时，如果床尾位置或者门的上半部分存在其他方块调色板中的方块，将会造成冲突，冲突的处理方式会按照接口SetBlockByBlockPalette中的冲突模式参数进行处理。

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
count = palette.ReplaceBlockInBlockPalette("minecraft:vine", 4,"minecraft:grass", 0)
print count
# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
palette = comp.GetBlockPaletteBetweenPos(0, (200,64,200),(201,65,202))
count = palette.ReplaceBlockInBlockPalette("minecraft:vine", 4,"minecraft:grass", 0)
print count
```



## SerializeBlockPalette

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.component.blockPaletteComp.BlockPaletteComponent

- 描述

    序列化方块调色板中的数据，用于方块调色板在客户端及服务端的事件数据之间传输。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块调色板的序列化数据 |

- 示例

```python
# 客户端调用
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlock(levelId)
sourcePalette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
dataDict = sourcePalette.SerializeBlockPalette()
# 用于在事件中传递方块调色板数据
eventData = self.CreateEventData()
eventData['data'] = dataDict
self.NotifyToServer(modConfig.GetBlockPaletteEvent, eventData)

# 服务端调用
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateBlock(levelId)
sourcePalette = comp.GetBlockPaletteBetweenPos((200,64,200),(201,65,202))
dataDict = sourcePalette.SerializeBlockPalette()
# 用于在事件中传递方块调色板数据
eventData = self.CreateEventData()
eventData['data'] = dataDict
self.NotifyToClient(modConfig.GetBlockPaletteEvent, eventData)
```

## 渲染

# 渲染

## ChangeBlockTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    替换方块贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，格式[namespace:name:auxvalue]，auxvalue默认为0; 只支持普通的没有特殊渲染逻辑的方形方块，否则可能会显示异常 |
    | tileName | str | 原贴图在图集中对应的名字，对应terrain_texture.json中的配置 |
    | texturePath | str | 打算替换成的贴图的路径 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功（因为采用延迟加载，此处返回成功不代表贴图路径正确，路径错误会导致渲染时贴图丢失显示异常） |

- 备注
    - 对纹理会动态变化的方块无效
    - 调用此接口后tileName不会发生变化，后续如果想恢复设置，依旧需要用这个tileName
    - 贴图的分辨率高度需要为宽度的整数倍

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
#设置朝上的面的贴图为work_block_other
print(comp.ChangeBlockTextures("myblock:work_block:0", "myblock:work_block_faceup", "textures/blocks/work_block_other"))
#恢复朝上的面的贴图
#print(comp.ChangeBlockTextures("myblock:work_block:0", "myblock:work_block_faceup", "textures/blocks/work_block_faceup"))
```



## GetBlockTextures

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    获取方块的初始贴图信息

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | blockName | str | 方块标识符，格式[namespace:name] |
    | face | int | 需要获取的方块面，参考[Facing枚举](../../枚举值/Facing.md)，face默认值为6，此时获取方块所有面的贴图信息 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 方块的贴图信息textureInfoDict，获取错误（如特殊方块：门、床等）则返回为None |

- 备注
    - name为贴图在图集中对应的名字，方块所用的贴图名字见blocks.json
    - 每一个贴图名name在terrain_texture.json中可能存在多个路径，因此该接口也会返回同样多的路径。
    - 该接口只作为校验用，获取到的贴图信息为游戏加载后的初始信息，ChangeBlockTextures修改后该接口返回的仍是初始信息。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
textureInfoDict = comp.GetBlockTextures("customblocks:customblocks_test_ore")
# textureInfoDict 信息如下
# {
#   'North': {'paths': ['textures/blocks/customblocks_ore'], 'name': 'customblocks:customblocks_test_ore'},
#   'West': {'paths': ['textures/blocks/customblocks_ore'],'name': 'customblocks:customblocks_test_ore'},
#   'Up': {'paths': ['textures/blocks/customblocks_ore'], 'name': 'customblocks:customblocks_test_ore'},
#   'Down': {'paths': ['textures/blocks/customblocks_ore'], 'name': 'customblocks:customblocks_test_ore'},
#   'East': {'paths': ['textures/blocks/customblocks_ore'], 'name': 'customblocks:customblocks_test_ore'},
#   'South': {'paths': ['textures/blocks/customblocks_ore'], 'name': 'customblocks:customblocks_test_ore'}
# }
```



## SetBlockEntityFramePosOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体中序列帧特效位置偏移值，用于调整序列帧特效相对于方块位置的偏移。与特效/序列帧/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | frameKeyName | str | 该序列帧特效的自定义键值名称。 |
    | effectPosOffset | tuple(int,int,int) | 序列帧特效相对于方块位置的x，y，z方向的偏移值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 调整序列帧特效的位置，在方块的位置上向+x轴方向偏移1, +y轴方向偏移2, +z轴方向偏移1
comp.SetBlockEntityFramePosOffset(pos, "my_frame1", (1,2,1))
```



## SetBlockEntityModelPosOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体的实体模型位置偏移值，用于调整实体模型相对于方块位置的偏移。可通过该接口来调整自定义方块实体的实体模型的位置。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | modelPosOffset | tuple(int,int,int) | 实体模型相对于方块位置的x，y，z方向的偏移值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 在调整实体模型的位置时，注意不要设置模型位置离方块实体的位置过远。如果设置过远，在玩家将屏幕移动到其他地方而看不到方块实体时，实体模型会由于玩家屏幕里不存在该方块实体而停止渲染。在这种情况下，每当玩家屏幕里看不到这个方块实体所在的位置时，实体模型都会消失。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 调整模型的位置，偏移值为向+x轴方向偏移1, +y轴方向偏移2, +z轴方向偏移1
comp.SetBlockEntityModelPosOffset(pos, (1,2,1))
```



## SetBlockEntityModelRotation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体的实体模型在各个轴上的旋转值，可通过该接口来调整自定义方块实体的实体模型的旋转。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | angles | float | 旋转角度，范围为[-360,360]。 |
    | rotateAxis | str | 旋转轴，绕该轴进行旋转，该参数仅支持填写以下三个值之一: "x", "y", "z"，大小写均可。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 在调整旋转角度时，注意旋转的顺序和角度的设置，避免出现万向锁的问题。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 调整模型旋转，绕x轴旋转30度
comp.SetBlockEntityModelRotation(pos, 30, "x")
# 调整模型旋转，绕y轴旋转30度
comp.SetBlockEntityModelRotation(pos, 30, "y")
# 调整模型旋转，绕z轴旋转30度
comp.SetBlockEntityModelRotation(pos, 30, "z")
```



## SetBlockEntityModelScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体的实体模型大小的缩放值，可通过该接口来调整自定义方块实体的实体模型的大小。只有自定义方块实体定义实体模型才生效，实体模型在resource_pack/entity/下定义，详细可参考自定义方块实体动画的教学文档。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | scale | tuple(int,int,int) | 实体模型在x,y,z各个轴上的缩放值。支持负值，当某一轴的缩放值为负值时，表示模型将会在这个轴上进行以另外两个轴为对称平面的镜像变换。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 模型的大小可以通过两个方式来调整：
        (1) 在entity.json中scripts字段下定义scale，如下所示
            "minecraft:client_entity": {
                ...
                "scripts":{
                    // 整体模型大小缩放值，定义了"scale"之后scalex，scaley，scalez将无效
                    "scale" : "0.9375",
                    // 对三个轴方向的缩放值。注释掉上方"scale", 以下三个缩放值将生效。
                    "scalex": "0.9375",
                    "scaley": "0.9375",
                    "scalez": "0.9375",
                        ...
                    }
            }
        (2) 使用本接口SetBlockEntityModelScale来设置模型缩放值。
        以上两种方式，第一种方式是对所有的使用这个模型的方块实体生效，第二种方式是对指定的方块实体的模型生效。如果同时使用了第一种方式以及第二种方式来调整模型大小，则模型会先按照第一种方式来进行缩放，再按照第二种方式来进行缩放。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 调整模型大小为x轴方向放大为原来的2倍，y轴方向放大为原来的2倍，z轴方向缩小为原来的0.5倍
comp.SetBlockEntityModelScale(pos, (2,2,0.5))
```



## SetBlockEntityParticlePosOffset

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.blockInfoCompClient.BlockInfoComponentClient

- 描述

    设置自定义方块实体中粒子特效位置偏移值，用于调整粒子特效相对于方块位置的偏移。与特效/粒子/SetPos接口不同，该接口调整的是相对于方块位置的位置偏移值，而不是世界坐标。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(int,int,int) | 方块所在位置 |
    | particleKeyName | str | 该粒子特效的自定义键值名称。 |
    | effectPosOffset | tuple(int,int,int) | 粒子特效相对于方块位置的x，y，z方向的偏移值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateBlockInfo(levelId)
# 调整粒子特效的位置，在方块的位置上向+x轴方向偏移1, +y轴方向偏移2, +z轴方向偏移1
comp.SetBlockEntityParticlePosOffset(pos, "my_particle1", (1,2,1))
```

## 红石

# 红石

## GetBlockPoweredState

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.redStoneCompServer.RedStoneComponentServer

- 描述

    获取某个坐标方块的充能状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 方块坐标位置 |
    | dimensionId | int | 目标维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 充能状态 0:未充能；1：弱充能；2：强充能 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRedStone(levelId)
comp.GetBlockPoweredState((1,1,1), 0)
```



## GetStrength

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.component.redStoneCompServer.RedStoneComponentServer

- 描述

    获取某个坐标的红石信号强度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 坐标位置 |
    | dimensionId | int | 目标维度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 红石信号强度[0, 15] |

- 备注
    - 可获取对应维度的常加载区块内红石信号强度

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateRedStone(levelId)
comp.GetStrength((1,1,1), 0)
```

