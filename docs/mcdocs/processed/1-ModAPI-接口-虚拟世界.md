# ModAPI 接口-虚拟世界

## 目录

- [世界](#世界)
- [其它对象](#其它对象)
- [模型](#模型)
- [相机](#相机)

---

## 世界

# 世界

## VirtualWorldCreate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    创建虚拟世界，虚拟世界只允许存在一个，已经存在虚拟世界的情况下再调用此方法则无效

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否创建成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.VirtualWorldCreate()
```



## VirtualWorldDestroy

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    销毁虚拟世界

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.VirtualWorldDestroy()
```



## VirtualWorldSetCollidersVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置虚拟世界中模型的包围盒是否显示,主要用于调试,默认为不显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isVisible | bool | 是否显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.VirtualWorldSetCollidersVisible(True)

id = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetBoxCollider(id, (2.0, 2.0, 2.0), (0.0, 0.0, 0.0))
```



## VirtualWorldSetSkyBgColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置虚拟世界中天空背景的颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float) | 颜色的r,g,b值，均为0.0到1.0的浮点值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
#设置天空为红色
virtualWorldComp.VirtualWorldSetSkyBgColor((1.0, 0.0, 0.0))
```



## VirtualWorldSetSkyTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置虚拟世界中天空的贴图

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | texturePath | str | 贴图路径 |
    | mode | int | 拉伸模式，0或1。0代表贴图宽高都拉伸至全屏，可能造成贴图变形；1代表高度拉伸至全屏，宽度按贴图原宽高比进行相应缩放，能保持贴图不被拉伸，但会造成贴图超出屏幕或不完全铺满屏幕。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.VirtualWorldSetSkyTexture("textures/virtualWorldSky", 0)
```



## VirtualWorldToggleVisibility

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置虚拟世界是否显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | isVisible | bool | 是否显示 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 建议在需要频繁在主世界跟虚拟世界切换的时候使用该方法，若后续长时间不需要使用虚拟世界，建议调用VirtualWorldDestroy进行销毁释放资源

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.VirtualWorldToggleVisibility(False)
```

## 其它对象

# 其它对象

## BindModel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    把对象绑定到模型上, 支持绑定序列帧，粒子，文本和其它模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | virtualWorldObjectType | int | 对象类型枚举, 支持VirtualWorldObjectType.Sfx, VirtualWorldObjectType.Textboard和VirtualWorldObjectType.Particle, VirtualWorldObjectType.Model |
    | objId | int | 要被绑定的对象的id |
    | targetId | int | 绑定到的目标对象的id, 该对象删掉时，绑定在上面的对象也会删除 |
    | posOffset | tuple(float,float,float) | 绑定后相对目标的位置偏移 |
    | rotOffset | tuple(float,float,float) | 绑定后相对目标的旋转角度偏移 |
    | boneName | str | 要绑定到目标对象哪个骨骼，默认为root |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 模型绑定模型暂时不支持绑定到具体骨骼
    - 模型绑定仅支持原版模型绑定原版模型，或者网易骨骼模型绑定网易骨骼模型，不支持原版模型绑定到网易骨骼模型这种类型交错的绑定
    - 序列帧，文本，粒子的生命周期与可见性需要玩家自己管理，虚拟世界在隐藏或者销毁时不做处理。

- 示例

```python
import client.extraClientApi as clientApi
VirtualWorldObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")

# 序列帧
frameEntityId = self.CreateEngineSfx("textures/sfxs/testSfx")
frameAniTransComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
frameAniControlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
frameAniControlComp.SetLoop(True)
frameAniControlComp.Play()
virtualWorldComp.BindModel(VirtualWorldObjectType.Sfx, frameEntityId, objId, (0.0, 3.0, 0.0), (0.0, 0.0, 0.0), "root")

# 文本
textBoardComp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
textBoardId = textBoardComp.CreateTextBoardInWorld("Hello", (0.5, 0.4, 0.3, 0.8), (0, 0, 0, 1), True)
virtualWorldComp.BindModel(VirtualWorldObjectType.Textboard, textBoardId, objId, (0.0, 3.0, 0.0), (0.0, 0.0, 0.0), "root")

# 粒子
particleEntityId = self.CreateEngineParticle("effects/testParticle.json", (0.0, 0.0, 0.0))
parComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
parComp.Play()
virtualWorldComp.BindModel(VirtualWorldObjectType.Particle, particleEntityId, objId, (0.0, 3.0, 0.0), (0.0, 0.0, 0.0), "root")

# 模型
childObj = virtualWorldComp.ModelCreateObject("datiangou", "fengxi")
virtualWorldComp.BindModel(VirtualWorldObjectType.Model, childObj, objId, (-1.0, 0.0, 0.0), (0.0, 0.0, 0.0))
```



## MoveToVirtualWorld

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    把对象从主世界移到虚拟世界, 非绑定的序列帧，文本，粒子需要调用该方法后才会出现在虚拟世界中，绑定的可以省略调用该方法。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | virtualWorldObjectType | int | 对象类型枚举, 支持VirtualWorldObjectType.Sfx, VirtualWorldObjectType.Textboard和VirtualWorldObjectType.Particle |
    | objId | int | 要移动的对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import client.extraClientApi as clientApi
VirtualWorldObjectType = clientApi.GetMinecraftEnum().VirtualWorldObjectType
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())

# 序列帧
frameEntityId = self.CreateEngineSfx("textures/sfxs/testSfx")
frameAniTransComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
frameAniTransComp.SetPos((0.0, 0.0, 0.0))
frameAniControlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
frameAniControlComp.SetLoop(True)
frameAniControlComp.Play()
virtualWorldComp.MoveToVirtualWorld(VirtualWorldObjectType.Sfx, frameEntityId)

# 文本
textBoardComp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
textBoardId = textBoardComp.CreateTextBoardInWorld("Hello", (0.5, 0.4, 0.3, 0.8), (0, 0, 0, 1), True)
virtualWorldComp.MoveToVirtualWorld(VirtualWorldObjectType.Textboard, textBoardId)

# 粒子
particleEntityId = self.CreateEngineParticle("effects/testParticle.json", (0.0, 0.0, 0.0))
parComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
parComp.Play()
virtualWorldComp.MoveToVirtualWorld(VirtualWorldObjectType.Particle, particleEntityId)
```

## 模型

# 模型

## ModelCancelAllBoneMask

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    取消动画中的所有骨骼屏蔽。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.ModelCancelAllBoneMask(objId, "attack")
```



## ModelCreateMinecraftObject

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    在虚拟世界中创建微软原版模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | identifier | str | 模型的identifier |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回模型对象的id, 失败时返回-1 |

- 备注
    - 创建模型后需要使用 ModelUpdateAnimationMolangVariable 为该模型json动作文件里面的所有变量进行赋值，不然运行时会有大量非空判断处理，会产生性能下降
    - 模型创建时初始默认朝向为+z方向, 位置为相机朝向的正前方10个单位，建议后续对坐标进行修改
    - 创建的原版模型需要改变播放的动作,只能通过 ModelUpdateAnimationMolangVariable 接口修改molang变量进行控制,不兼容组件中的其它动作接口
    - 暂不支持的微软原版模型：minecraft:horse（马）、minecraft:donkey（驴）、minecraft:mule（骡子）、minecraft:skeleton_horse（骷髅马）、minecraft:zombie_horse（僵尸马）、minecraft:llama（羊驼）、minecraft:tropicalfish（热带鱼）、minecraft:slime（史莱姆）、minecraft:magma_cube（岩浆怪）、minecraft:ghast（恶魂）、minecraft:shulker（潜影贝）、minecraft:ender_dragon（末影龙）、minecraft:thrown_trident（三叉戟）、minecraft:ender_crystal（末影水晶）、minecraft:boat（船）、minecraft:tnt（TNT）

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.ModelCreateMinecraftObject("minecraft:sheep")
virtualWorldComp.ModelUpdateAnimationMolangVariable(id, {"variable.state": 2, "variable.liedownamount": 0})
```



## ModelCreateObject

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    在虚拟世界中创建网易骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | modelName | str | 模型的资源 |
    | animationName | str | 模型的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回模型对象的id, 失败时返回-1 |

- 备注
    - 模型创建时初始默认朝向为+z方向, 位置为相机朝向的正前方10个单位，建议后续对坐标进行修改

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.ModelCreateObject("datiangou", "run")
```



## ModelGetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    获取模型的坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 模型的坐标(x, y, z), 模型不存在的话则返回None |

- 备注
    - 若对象绑定到其它对象上，则返回无意义，以绑定时参数为准

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetPos(objId, (0.0, 0.0, -10.0))
pos = virtualWorldComp.ModelGetPos(objId)
```



## ModelGetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    返回模型的旋转角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 旋转角度(x, y, z), 模型不存在则返回None |

- 备注
    - 若对象绑定到其它对象上，则返回无意义，以绑定时参数为准

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetRot(objId, (0.0, 90.0, 0.0))
rot = virtualWorldComp.ModelGetRot(objId)
```



## ModelIsVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    返回模型可见性

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否可见 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
id = virtualWorldComp.ModelCreateObject("datiangou", "run")
print(virtualWorldComp.ModelIsVisible(id))
```



## ModelMoveTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型平移运动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | pos | tuple(float,float,float) | 坐标值(x, y, z) |
    | time | float | 单位秒，运动时长（大于0的浮点数） |
    | ease | TimeEaseType | 时间变化函数, 默认值为clientApi.GetMinecraftEnum().TimeEaseType.linear, 参数不在枚举值中也当作linear |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetPos(objId, (0.0, 0.0, 0.0))
virtualWorldComp.ModelMoveTo(objId, (0.0, 0.0, -10.0), 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
```



## ModelPlayAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    模型播放动画，支持动作融合，其功能与模型接口ModelPlayAni相同。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |
    | loop | bool | 是否循环播放 |
    | isBlended | bool | 播放时是与当前动画混合还是中止当前动画的播放，默认False，即中止当前动画播放。设置为True时，将允许即将播放的动画进行混合(注意，在没有设置骨骼屏蔽或是设置线性混合参数的情况下不会产生混合效果)。另外，动画混合仅在相同层级的动画之间进行。若当前播放的动画与即将播放的动画层级不一样，则isBlended参数无效。 |
    | layer | int | 设置骨骼动画的层级，范围为0~255，默认为0。注意，如果播放的动画已经存在，则会将原有的动画层级覆盖。动画层级越大，则优先度越高，骨骼模型的骨骼优先播放优先度最高的动画。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelPlayAnimation(objId, "fengxi", True)
```



## ModelRegisterAnim1DControlParam

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    当同时播放多个骨骼动画时，新建用于控制动画进行1D线性混合的参数。目前线性混合仅支持对两个动画进行混合。新建的参数值范围为[0,1]。指定的骨骼将会按照这个参数的值对两个动画进行线性混合。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | leftAniName | str | 混合的第一个动画名称，当1D参数的值为0时指定的骨骼仅播放这个动画。 |
    | rightAniName | str | 混合的第二个动画名称，当1D参数的值为1时指定的骨骼仅播放这个动画。 |
    | paramName | str | 自定义的1D参数名称。该参数新建后的初始值为0。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 注意，如果对某个骨骼使用了骨骼屏蔽，则这个1D线性混合将对该骨骼不会生效。另外，如果在使用该接口时新建一个已经存在的参数名称，则会将原来的参数覆盖。

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
# 新建1D控制参数，用于对attack和walk这两个动画进行线性混合，参数的名称为“arm_control_param”。
virtualWorldComp.ModelRegisterAnim1DControlParam(objId, "attack", "walk", "arm_control_param")
# 相继播放这两个动画，设置isBlend为True，开启动画混合。
virtualWorldComp.ModelPlayAnimation(objId, "attack", True, True)
virtualWorldComp.ModelPlayAnimation(objId, "walk",True, True)
# 改变1D控制参数的值，两个动画将根据该值进行线性混合。可根据实际情况进行动态调整。
virtualWorldComp.ModelSetAnim1DControlParam(objId, "arm_control_param", 0.5)
```



## ModelRemove

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    销毁虚拟世界中的模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelRemove(objId)
```



## ModelRotate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    模型绕某个轴旋转多少度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | degreeAngle | float | 旋转角度，为了避免数值过大出现浮点误差，建议角度范围控制在-360度到360度 |
    | axis | tuple(float,float,float) | 旋转轴(x, y, z) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelRotate(objId, 90.0, (0.0, 1.0, 0.0))
```



## ModelRotateTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型旋转运动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | rot | tuple(float,float,float) | 旋转值(x, y, z) |
    | time | float | 单位秒，运动时长（大于0的浮点数） |
    | ease | TimeEaseType | 时间变化函数, 默认值为clientApi.GetMinecraftEnum().TimeEaseType.linear, 参数不在枚举值中也当作linear |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetRot(objId, (0.0, 0.0, 0.0))
virtualWorldComp.ModelRotateTo(objId, (0.0, 90.0, 0.0), 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
```



## ModelSetAnim1DControlParam

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    新建动画的1D控制参数后，使用该接口对相应的参数进行控制。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | paramName | str | 使用接口RegisterAnim1DControlParam所新建的自定义1D参数名称。该参数新建后的初始值为0。 |
    | value | float | 参数的值，范围为[0,1]。当1D参数的值为0时仅播放接口RegisterAnim1DControlParam中的leftAniName参数指定的动画，当1D参数的值为1时仅播放接口RegisterAnim1DControlParam中的rightAniName参数指定的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 注意，如果对某个骨骼使用了骨骼屏蔽，则这个1D线性混合将对该骨骼不会生效。

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
# 新建1D控制参数，用于对attack和walk这两个动画进行线性混合，参数的名称为“arm_control_param”。
virtualWorldComp.ModelRegisterAnim1DControlParam(objId, "attack", "walk", "arm_control_param")
# 相继播放这两个动画，设置isBlend为True，开启动画混合。
virtualWorldComp.ModelPlayAnimation(objId, "attack", True, True)
virtualWorldComp.ModelPlayAnimation(objId, "walk",True, True)
# 改变1D控制参数的值，两个动画将根据该值进行线性混合。可根据实际情况进行动态调整。
virtualWorldComp.ModelSetAnim1DControlParam(objId, "arm_control_param", 0.5)
```



## ModelSetAnimAllBoneMask

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置是否屏蔽动画中所有骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。该接口会对该动画中所有骨骼生效，可通过参数ignoreBoneList来指定不受影响的骨骼名称。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |
    | ignoreBonesList | list(str) | 忽视的骨骼名称列表。在这个列表中的骨骼将不会被影响。输入空列表时则对所有骨骼执行这次设置。 |
    | enable | bool | 是否启用该骨骼的动画。True为不屏蔽，启动该骨骼的动画。False为屏蔽，不启动该骨骼的动画。 |
    | applyToChild | bool | True为对ignoreBoneList中的骨骼的子骨骼也生效，False为仅对ignoreBoneList中的骨骼生效，默认为True。若ignoreBoneList为空列表，则applyToChild无效果。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 在使用该接口屏蔽上下半身的动画时，如果骨骼当中存在root骨骼，并且root骨骼的子骨骼包含上下半身的骨骼的话，root骨骼往往会控制整体骨骼模型的移动，要注意root骨骼对其他骨骼的影响。

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
# 屏蔽名为attack动画中所有骨骼的动画，"l_arm"及"r_arm"这两个不受影响，其子骨骼也不受影响
virtualWorldComp.ModelSetAnimAllBoneMask(objId, "attack", ["l_arm", "r_arm"], False, True)
```



## ModelSetAnimBoneMask

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置是否屏蔽动画中指定的骨骼的动画，若开启骨骼屏蔽后，该骨骼将不再播放该动画中的动作。通过屏蔽指定骨骼的动画可实现同一个骨骼模型同时在不同骨骼上播放不同的动作动画，从而实现快捷的动作融合。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |
    | boneNamesList | list(str) | 骨骼名称列表 |
    | enable | bool | 是否启用该骨骼的动画。True为不屏蔽，启动该骨骼的动画。False为屏蔽，不启动该骨骼的动画。 |
    | applyToChild | bool | True为对该骨骼及其子骨骼生效，False为仅对该骨骼生效，默认为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 在使用该接口屏蔽上下半身的动画时，如果骨骼当中存在root骨骼，并且root骨骼的子骨骼包含上下半身的骨骼的话，root骨骼往往会控制整体骨骼模型的移动，要注意root骨骼对其他骨骼的影响。

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
# 屏蔽名为attack动画中的"l_arm"及"r_arm"的骨骼的动画，对其子骨骼也生效
virtualWorldComp.ModelSetAnimBoneMask(objId, "attack", ["l_arm", "r_arm"], False, True)
```



## ModelSetAnimLayer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置骨骼动画的层级，动画层级越大，则优先度越高，骨骼模型的骨骼优先播放优先度最高的动画，相同层级的动画则优先播放率先播放的动画。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |
    | layer | int | 动画层级， 正整数，范围为0~255 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 注意，设置层级相同的情况下不会改变当前的优先播放序列。举个例子：当前存在动画A及动画B，动画A的层级为1，动画B的层级为0，此时骨骼模型播放的动画为动画A。如果将动画A的层级设置为0，即动画A及动画B的层级相同，则当前仍然会播放动画A，因为层级相同的情况下不会改变目前的优先播放序列。要想让骨骼模型播放动画B，则需要动画B的层级比动画A的层级高。

- 示例

```python
import mod.client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.ModelSetAnimLayer(objId, "attack", 1)
```



## ModelSetBoxCollider

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型的包围盒

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | lengths | tuple(float,float,float) | 模型包围盒各个方向的长度,(x,y,z) |
    | offset | tuple(float,float,float) | 模型包围盒中心的偏移,(x,y,z),默认为(0.0,0.0,0.0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetBoxCollider(objId, (2.0, 2.0, 2.0), (0.0, 0.0, 0.0))
```



## ModelSetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型坐标

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | pos | tuple(float,float,float) | 坐标(x, y, z) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 若对象绑定到其它对象上，则修改无效，实际位置以绑定时参数为准

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetPos(objId, (0.0, 0.0, -10.0))
```



## ModelSetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型的旋转角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | rot | tuple(float,float,float) | 旋转角度(x, y, z)初始默认为(0, 0, 0)，指向z轴负方向。 为了避免数值过大出现浮点误差，建议各维度角度控制范围在-360度到360度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 若对象绑定到其它对象上，则修改无效，实际旋转角度以绑定时参数为准

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetRot(objId, (0.0, 90.0, 0.0))
```



## ModelSetScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型的缩放值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | scales | tuple(float,float,float) | 缩放值(x, y, z) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetScale(objId, (2.0, 2.0, 2.0))
```



## ModelSetVisible

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置模型可见性

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | isVisible | bool | 是否可见 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
id = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetVisible(id, False)
```



## ModelStopActions

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    停止模型的移动和旋转运动

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否停止成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
objId = virtualWorldComp.ModelCreateObject("datiangou", "run")
virtualWorldComp.ModelSetPos(objId, (0.0, 0.0, 0.0))
virtualWorldComp.ModelSetRot(objId, (0.0, 0.0, 0.0))
virtualWorldComp.ModelMoveTo(objId, (0.0, 0.0, -10.0), 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
virtualWorldComp.ModelRotateTo(objId, (0.0, 90.0, 0.0), 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
virtualWorldComp.ModelStopActions(objId)
```



## ModelStopAnimation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    停止播放指定的模型动画。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | animationName | str | 模型的动画 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否暂停成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.ModelStopAnimation(objId, "fengxi")
```



## ModelUpdateAnimationMolangVariable

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    更新微软原版模型表达式变量，可控制动作的改变

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | objId | int | 模型对象的id |
    | molangDict | dict | 键值对形式的数据 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 备注
    - 如果创建模型后同一帧内马上调用该接口，则客户端实体配置中的scripts/initialize字段不再会执行。

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
id = virtualWorldComp.ModelCreateMinecraftObject("minecraft:cat")
virtualWorldComp.ModelUpdateAnimationMolangVariable(id, {"variable.state": 2, "variable.liedownamount": 0})
```

## 相机

# 相机

## CameraGetClickModel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    获取相机当前指向的模型的id，会返回离相机最近的，通常与GetEntityByCoordEvent配合使用

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 模型的id, 相机没有指向模型则返回-1 |

- 备注
    - 模型需要设置包围盒才能响应点击

- 示例

```python
# 当玩家点击屏幕时获取点击位置的模型的id
import mod.client.extraClientApi as clientApi
class MyClientSystem(ClientSystem):
    def __init__(self, namespace, name):
        ClientSystem.__init__(self, namespace, name)
        self.ListenForEvent('Minecraft', 'Engine', 'GetEntityByCoordEvent', self, self.click)
        self.initModel()

    def initModel(self):
        virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
        id = virtualWorldComp.ModelCreateObject("datiangou", "run")
        # 设置了包围盒才能响应点击
        virtualWorldComp.ModelSetBoxCollider(id, (2.0, 2.0, 2.0), (0.0, 0.0, 0.0))

    def click(self, args):
        import client.extraClientApi as clientApi
        virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
        id = virtualWorldComp.CameraGetClickModel()
        if id > 0:
            print("select:", id)
```



## CameraGetFov

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    获取相机视野大小

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 视野大小( field of view )，单位为角度, 范围为[30, 110]。不修改时默认为45。 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
fov = virtualWorldComp.CameraGetFov()
```



## CameraGetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    返回相机位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 坐标值(x, y, z), 若虚拟世界没有创建则返回None |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
cameraPos = virtualWorldComp.CameraGetPos()
```



## CameraGetZoom

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    获取相机的缩放值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 缩放值 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
zoom = virtualWorldComp.CameraGetZoom()
```



## CameraLookAt

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    修改相机朝向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetPos | tuple(float,float,float) | 目标的坐标 |
    | upVector | tuple(float,float,float) | 相机向上方向的向量, (x,y,z)初始默认为(0,1,0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否修改成功 |

- 备注
    - 相机初始默认朝向为-z轴

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraLookAt((0.0, 0.0, -10.0), (0.0, 1.0, 0.0))
```



## CameraMoveTo

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置相机移动动画, 会根据当前相机状态与传入参数按时间进行插值显示

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 目标点的坐标 |
    | targetPos | tuple(float,float,float) | 到达目标点后朝向的位置 |
    | upVector | tuple(float,float,float) | 到达目标点后相机向上方向的向量 |
    | zoom | float | 到达目标点相机的缩放值 |
    | time | float | 单位秒，动作时长（大于0的浮点数）。为了镜头连贯性，相机的运动与实际帧率有关，默认以60帧计算，会因实际帧率波动稍有偏差。 |
    | ease | TimeEaseType | 时间变化函数, 默认值为clientApi.GetMinecraftEnum().TimeEaseType.linear, 参数不在枚举值中也当作linear |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraMoveTo((0.0, 0.0, -10.0), (1.0, 1.0, -10.0), (0.0,1.0, 0.0), 1.0, 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
```



## CameraSetFov

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置相机视野大小

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fov | float | 视野大小( field of view )，单位为角度, 范围为[30, 110]，若fov小于30则设置为30，若fov大于110，则设置为110。不修改时默认为45。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraSetFov(60)
```



## CameraSetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置相机位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 坐标值(x,y,z)初始默认为 (0,0,0)，且朝向z轴负方向 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraSetPos((0.0, 6.0, 0.0))
```



## CameraSetZoom

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    设置相机缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | zoom | float | 缩放值, 范围为[0.1,100.0]，小于0.1则设置为0.1，大于100则设置为100，不修改时默认为1。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraSetZoom(2.0)
```



## CameraStopActions

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.virtualWorldCompClient.VirtualWorldCompClient

- 描述

    停止相机移动动画

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否停止成功 |

- 示例

```python
import client.extraClientApi as clientApi
virtualWorldComp = clientApi.GetEngineCompFactory().CreateVirtualWorld(clientApi.GetLevelId())
virtualWorldComp.CameraMoveTo((0.0, 0.0, -10.0), (1.0, 1.0, -10.0), (0.0,1.0, 0.0), 1.0, 3.0, clientApi.GetMinecraftEnum().TimeEaseType.linear)
virtualWorldComp.CameraStopActions()
```

