# ModAPI 接口-特效

## 目录

- [序列帧](#序列帧)
- [微软粒子](#微软粒子)
- [文字面板](#文字面板)
- [模型特效](#模型特效)
- [粒子](#粒子)
- [通用](#通用)

---

## 序列帧

# 序列帧

## Bind

<span style="display:inline;color:#7575f9">客户端</span>

<span id="0"></span>
method in mod.client.component.frameAniEntityBindComp.FrameAniEntityBindComp

- 描述

    绑定entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | bindEntityId | str | 绑定的entity的ID |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniEntityBind(frameEntityId)
comp.Bind(entityId, (0, 1, 0), (0, 0, 0))
```



<span id="1"></span>
method in mod.client.component.frameAniSkeletonBindComp.FrameAniSkeletonBindComp

- 描述

    绑定骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | modelId | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | boneName | str | 绑定具体骨骼的名称 |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniSkeletonBind(frameEntityId)
comp.Bind(modelId, "root", (0, 1, 0), (0, 0, 0))
```



## CreateEngineSfx

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    创建序列帧特效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，不用后缀名 |
    | pos | tuple(float,float,float) | 创建位置，可选，没传则可以创建完用frameAniTrans组件设置 |
    | rot | tuple(float,float,float) | 角度，可选，没传则可以创建完用frameAniTrans组件设置 |
    | scale | tuple(float,float,float) | 缩放系数，可选，没传则可以创建完用frameAniTrans组件设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | frameEntityId或者None |

- 备注
    - 创建序列帧后，可以用返回的frameEntityId创建序列帧分类中的相关组件，设置所需属性，以实现各种表现效果
    - 切换维度后会自动隐藏非本维度创建的而且没有绑定实体的序列帧, 回到该维度后会自动重新显示
    - 需要注意，序列帧创建之后需要调用frameAniControl组件的play函数才会播放,如果播放非本维度创建的序列帧,会同时修改该序列帧的创建维度为当前维度

- 示例

```python
import mod.client.extraClientApi as clientApi
class MyClientSystem(ClientSystem):
    # 创建
    def createSfx(self):
        frameEntityId = self.CreateEngineSfx("textures/sfxs/snow_3")
        frameAniTransComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
        frameAniTransComp.SetPos((10,10,10))
        frameAniTransComp.SetRot((0,0,0))
        frameAniTransComp.SetScale((1,1,1))
        frameAniControlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
        frameAniControlComp.Play()

    # 删除
    def removeSfx(self, frameEntityId):
        self.DestroyEntity(frameEntityId)
```



## CreateEngineSfxFromEditor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    指使用资源包中effects/xxx.json，按照编辑器中编辑好的参数创建序列帧。支持环状序列帧

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效配置路径，需要为"effects/xxx.json"，"xxx"为编辑器创建序列帧时填写的名称 |
    | pos | tuple(float,float,float) | 创建位置，可选，没传则可以创建完用frameAniTrans组件设置，一般需要设置播放的位置 |
    | rot | tuple(float,float,float) | 角度，可选，没传则可以创建完用frameAniTrans组件设置 |
    | scale | tuple(float,float,float) | 缩放系数，可选，没传则可以创建完用frameAniTrans组件设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | frameEntityId或者None |

- 备注
    - 创建序列帧后，可以用返回的frameEntityId创建序列帧分类中的相关组件，设置所需属性，以实现各种表现效果
    - 需要注意，序列帧创建之后需要调用frameAniControl组件的play函数才会播放
    - 根据editor配置生成序列帧后还需要设置位置或绑定，以及进行播放。

- 示例

```python
import mod.client.extraClientApi as clientApi
class MyClientSystem(ClientSystem):
    # 创建
    def createSfxFromEditor(self):
        frameEntityId = self.CreateEngineSfxFromEditor("effects/mySfx.json")
        frameAniTransComp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
        frameAniTransComp.SetPos((10,10,10))
        frameAniTransComp.SetRot((0,0,0))
        frameAniTransComp.SetScale((1,1,1))
        frameAniControlComp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
        frameAniControlComp.Play()

    # 删除
    def removeSfx(self, frameEntityId):
        self.DestroyEntity(frameEntityId)
```



## GetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    获取序列帧特效的位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 返回序列帧特效的世界坐标位置。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
comp.GetPos()
```



## GetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    获取序列帧特效的旋转角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 返回序列帧特效的旋转角度。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
comp.GetRot()
```



## GetScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    获取序列帧特效的缩放值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 返回序列帧特效的缩放值。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
comp.GetScale()
```



## Pause

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    暂停播放，序列帧定格在当前时刻，再次调用Play时继续播放

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
comp.Pause()
```



## Play

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    播放序列帧

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
comp.Play()
```



## SetDeepTest

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧是否透视，默认为否

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | deepTest | bool | False表示透视，则被物体/方块阻挡时仍然能看到序列帧 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置为透视
comp.SetDeepTest(False)
```



## SetFaceCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧是否始终朝向摄像机，默认为是

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | face | bool | True表示朝摄像机 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置为不始终朝摄像机
comp.SetFaceCamera(False)
```



## SetFadeDistance

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧开始自动调整透明度的距离。序列帧与摄像机之间的距离小于该值时会自动调整序列帧的透明度，距离摄像机越近，序列帧越透明

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fadeDistance | float | 自动调整透明度的距离，应为正数，负数将视作零来处理 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置该序列帧在与相机距离小于3时会自动调整透明度
comp.SetFadeDistance(3)
```



## SetLayer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧渲染层级，默认层级为1，当层级不为1时表示该特效开启特效分层渲染功能。特效（粒子和帧动画）分层渲染时，层级越高渲染越靠后，层级大的会遮挡层级低的，且同一层级的特效会根据特效的相对位置产生正确的相互遮挡关系。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | layer | int | 粒子渲染层级，总共包含0-15的层级。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 该接口只针对序列帧进行设置，粒子特效请使用particleControl组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置为渲染层级为2
comp.SetLayer(2)
```



## SetLoop

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧是否循环播放，默认为否

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | loop | bool | True表示循环播放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置为循环播放
comp.SetLoop(True)
```



## SetMixColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧混合颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float,float) | 颜色的RGBA值，范围0-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置颜色为红色半透明
color = (1, 0, 0, 0.5)
comp.SetMixColor(color)
```



## SetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    设置序列帧的位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 世界坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
comp.SetPos((0, 5, 0))
```



## SetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    设置序列帧的旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float,float) | 按顺序绕局部坐标系的+x，-y，+z轴旋转的角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
# 绕y轴旋转90度，然后绕z轴旋转90度
comp.SetRot((0, 90, 90))
```



## SetRotUseZXY

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    设置序列帧的旋转，旋转顺序按照绕z,x,y轴旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float,float) | 绕局部坐标系的+z，+x，+y轴旋转的角度，旋转顺序按照绕z,x,y轴旋转。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
# 绕z轴旋转90度，然后绕y轴旋转90度
comp.SetRotUseZXY((0, 90, 90))
```



## SetScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniTransComp.FrameAniTransComp

- 描述

    设置序列帧的缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | 对于平面序列帧，第一个参数为贴图横向上的缩放，第二个参数为纵向上的缩放，第三个参数无用。对于环状序列帧，为三个坐标轴上的缩放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniTrans(frameEntityId)
# 横向拉伸为2倍，纵向不变
comp.SetScale((2, 1, 1))
```



## SetUsePointFiltering

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    设置序列帧是否使用点滤波

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | use | bool | True为使用点滤波，False为使用双线性插值（默认使用） |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 使用点滤波的图像通常边缘清晰、可能会有较强烈的锯齿感；使用双线性插值的图像通常比较平滑、可能会使图像一定程度上变得模糊

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
# 设置该序列帧使用点滤波
comp.SetUsePointFiltering(True)
```



## Stop

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.frameAniControlComp.FrameAniControlComp

- 描述

    停止序列帧（不是暂停）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateFrameAniControl(frameEntityId)
comp.Stop()
```

## 微软粒子

# 微软粒子

## BindEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    绑定粒子发射器到指定实体的指定骨骼上

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 需要已经创建且未被销毁的粒子发射器 |
    | entity_id | str或int | 需要绑定的实体id |
    | bone_name | str | 需要绑定的骨骼名称(不区分大小写) 默认值为"body" |
    | offset | tuple | 三维 表示粒子发射器的绑定偏移 默认值为(0, 0, 0) |
    | rotation | tuple | 表示粒子发射器绑定的三维旋转(角度制，按照ZYX顺序旋转) 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 绑定变换的计算是在局部空间下完成的。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.Create("netease:tutorial_particle")
comp.BindEntity(parId, localId, "rightitem", (0, 0, 0), (0, 0, 0))
```



## BindModel

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    绑定粒子发射器到指定骨骼模型的指定骨骼上

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 需要已经创建且未被销毁的粒子发射器 |
    | model_id | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | bone_name | str | 绑定具体骨骼的名称(不区分大小写)，默认值为"root" |
    | offset | tuple(float,float,float) | 三维 表示粒子发射器的绑定偏移 默认值为(0, 0, 0) |
    | rotation | tuple(float,float,float) | 表示粒子发射器绑定的三维旋转(角度制，按照ZYX顺序旋转) 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 绑定变换的计算是在局部空间下完成的，没有指定骨骼的情况下默认绑定到"root"上，如果root不存在则该粒子不会显示，也不会被销毁。
    - 切换至其他骨骼模型后导致model_id改变，所以绑定到原model_id上的粒子发射器也会一起消失。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(clientApi.GetLevelId())

par_Id = comp.Create("netease:tutorial_particle")
comp.BindModel(par_Id, model_id, "root", (0, 0, 0), (0, 0, 0))
```



## Create

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    创建粒子发射器, 创建后立即播放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effect_name | str | 粒子发射器名称(粒子发射器json文件中的identifier) |
    | offset | tuple | 三维 表示在某处创建粒子发射器 默认值为(0, 0, 0) |
    | rotation | tuple | 粒子发射器创建后使用的三维旋转(使用角度制，按照ZYX顺序旋转) 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 粒子发射器实例ID 返回0表示创建失败 |

- 备注
    - 粒子发射器json文件可以通过微软官方编辑器SnowStorm进行创建编辑，
        开发者们可以通过访问在线网站 https://snowstorm.app 或在Visual Studio Code扩展商店中搜索"snowstorm"来使用这个编辑器
    - 粒子发射器json文件应存放在 资源包/particles 路径下
    - 粒子发射器json文件内容不应该包含中文，否则会无法解析
    - 请注意，如果粒子发射器出现在世界空间(即 没有绑定实体)，
        即使粒子发射器json文件定义了minecraft:emitter_lifetime_looping组件，
        也只会播放一次或一个周期，随后销毁
    - 部分原版粒子使用了minecraft:emitter_rate_manual组件，需要额外调用EmitManually函数才能发射粒子

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
parId = comp.Create("netease:tutorial_particle", (0, 0, 0), (0, 0, 0))
```



## CreateBindEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    创建粒子发射器并绑定到指定实体的指定骨骼上, 创建后立即播放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effect_name | str | 粒子发射器名称(粒子发射器json文件中的identifier) |
    | entity_id | str或int | 需要绑定的实体id |
    | bone_name | str | 需要绑定的骨骼名称(不区分大小写) 默认值为"body" |
    | offset | tuple | 三维 表示粒子发射器的绑定偏移 默认值为(0, 0, 0) |
    | rotation | tuple | 表示粒子发射器绑定的三维旋转(使用角度制，按照ZYX顺序旋转) 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 粒子发射器实例id 返回0表示创建失败 |

- 备注
    - 粒子发射器json文件可以通过微软官方编辑器SnowStorm进行创建编辑，
        开发者们可以通过访问在线网站 https://snowstorm.app 或在Visual Studio Code扩展商店中搜索"snowstorm"来使用这个编辑器
    - 粒子发射器json文件应存放在 资源包/particles 路径下
    - 粒子发射器json文件内容不应该包含中文，否则会无法解析
    - 绑定变换的计算是在局部空间下完成的。
    - 部分原版粒子使用了minecraft:emitter_rate_manual组件，需要额外调用EmitManually函数才能发射粒子

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
```



## EmitManually

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    手动发射粒子一次

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 需要已经创建且未被销毁的粒子发射器 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 部分原版粒子使用了minecraft:emitter_rate_manual组件，在创建粒子发射器后不会自动发射粒子，需要额外调用该函数

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("minecraft:water_evaporation_manual", localId, "rightitem")
comp.EmitManually(parId) # 手动发射一次粒子
```



## Exist

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    判断指定粒子发射器是否存在

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回True时，表示指定的粒子发射器存在于场景中 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.Exist(parId)
comp.RemoveAll()
print comp.Exist(parId)
```



## GetActiveDuration

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器的激活周期

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器激活周期 粒子发射器无效时会返回0.0 |

- 备注
    - 粒子发射器的激活周期在其对应的json文件(资源包/particles/xxx.json)中定义
    - 粒子发射器的播放周期等于 激活周期(active_time) + 休眠周期(sleep_time)
    - 对于没有定义激活周期的粒子发射器，其返回值为一个较大的数字(大约为1000000)

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetActiveDuration(parId)
```



## GetBindingID

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    返回绑定的目标id 没有则返回"0"

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 绑定的实体id |

- 备注
    - 可用GetBindingModleID获取绑定的骨骼模型id

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.Create("netease:tutorial_particle")
print comp.GetBindingID(parId)

comp.BindEntity(parId, localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetBindingID(parId)
```



## GetBindingModleID

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    返回绑定的骨骼模型id 没有则返回-1

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 绑定的骨骼模型id |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(clientApi.GetLevelId())
localId = clientApi.GetLocalPlayerId()

parId = comp.Create("netease:tutorial_particle")
print comp.GetBindingID(parId)

comp.BindModel(parId, modID, 'root', (0, 0, 0), (0, 0, 0))
print comp.GetBindingModleID(parId)
```



## GetDuration

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器的播放周期(激活+休眠时间)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器播放周期 粒子发射器无效时会返回0.0 |

- 备注
    - 粒子发射器的播放周期在其对应的json文件(资源包/particles/xxx.json)中定义
    - 粒子发射器的播放周期等于 激活周期(active_time) + 休眠周期(sleep_time)
    - 对于没有定义播放周期的粒子发射器，其返回值为一个较大的数字(大约为1000000)

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetDuration(parId)
```



## GetFacingMode

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    返回粒子发射器的粒子朝向模式

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 粒子朝向模式字符串 返回字符串"none"表示非法 |

- 备注
    - 朝向模式暂不支持使用脚本设置，可以在粒子编辑器SnowStorm中编辑该属性:https://snowstorm.app
    - 目前支持的朝向模式如下:
        
            rotate_xyz              粒子朝向相机，面片与相机视角垂直
            rotate_y                粒子朝向相机，但是面片只旋转世界Y轴
            lookat_xyz              粒子旋转XYZ轴看向相机位置
            lookat_y                粒子仅旋转Y轴来看向相机位置
            lookat_direction        可以选择根据速度方向或者自定义方向来决定粒子面片朝向
            direction_x             粒子面片朝向发射器的x轴
            direction_y             粒子面片朝向发射器的y轴
            direction_z             粒子面片朝向发射器的z轴
            emitter_transform_xy    跟随粒子发射器的xy面朝向
            emitter_transform_xz    跟随粒子发射器的xz面朝向
            emitter_transform_yz    跟随粒子发射器的yz面朝向

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetFacingMode(parId)
```



## GetLoopAge

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器当前播放周期内已播放的时间

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器在当前播放周期内已播放的时间 粒子发射器id无效时会返回0.0 |

- 备注
    - 0.0 <= 已播放的时间 <= 粒子发射器播放周期
    - 返回的周期内已播放时间，受到SetTimeScale、Replay和PlayAt等函数的影响。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetLoopAge(parId)
comp.PlayAt(parId, 0.5)
print comp.GetLoopAge(parId)
```



## GetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | is_local | bool | 是否获取局部空间 | 绑定偏移 默认值为True(即 默认获取局部空间位置 | 绑定偏移) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Tuple | 表示粒子发射器位置的三维向量 |

- 备注
    - 如果粒子没有进行绑定(即 没有放在世界空间)，则它的局部空间位置等于世界空间位置。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 1, 0), (0, 0, 0))
parId1 = comp.Create("netease:tutorial_particle", (0, 1, 0), (0, 0, 0))
print 'local position:', comp.GetPos(parId0, True)
print 'local position:', comp.GetPos(parId1)

print 'world position:', comp.GetPos(parId0, False)
print 'world position:', comp.GetPos(parId1, False)
```



## GetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器局部旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | is_local | bool | 表示是否获取局部空间旋转 默认值为True(即 默认获取局部空间旋转) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | Tuple | 粒子发射器三维旋转(使用角度制) |

- 备注
    - 如果粒子发射器没有进行绑定，则它的局部空间旋转等于世界空间旋转

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (45, 0, 45))
print comp.GetRot(parId) # True
print comp.GetRot(parId, False)
```



## GetSleepDuration

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器的休眠周期

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器休眠周期 粒子发射器无效时会返回0.0 |

- 备注
    - 粒子发射器的休眠周期在其对应的json文件(资源包/particles/xxx.json)中定义
    - 粒子发射器的播放周期等于 激活周期(active_time) + 休眠周期(sleep_time)
    - 对于没有定义休眠周期的粒子发射器，其返回值为0.0

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetSleepDuration(parId)
```



## GetTimeScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器的播放速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器播放速度 粒子发射器无效时会返回0.0 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem")
print comp.GetTimeScale(parId)
comp.SetTimeScale(parId, 0.2)
print comp.GetTimeScale(parId)
```



## GetVariable

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    获取粒子发射器的Molang变量值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | variable_name | str | Molang变量名(例如variable.emitter_age) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 表示粒子发射器的Molang变量值 无效时会返回0.0 |

- 备注
    - Molang变量可以在粒子发射器json文件内自行定义。
    - 另外，粒子发射器以及粒子内置了一些Molang变量可供使用:
        
            variable.emitter_random_1   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_2   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_3   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_4   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_lifetime   粒子发射器的播放周期(生命周期)
            variable.emitter_age        粒子发射器当前播放时间
            variable.entity_scale       当粒子发射器绑定实体时，这个值表示绑定实体的大小缩放
            variable.particle_lifetime  粒子的生命周期
            variable.particle_age       粒子生成后已经过的时间
            variable.particle_random_1  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_2  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_3  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_4  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
    - 关于Molang表达式的使用，目前大家可以参考微软官方文档:
        https://docs.microsoft.com/en-us/minecraft/creator/reference/content/molangreference/examples/molangconcepts/molangintroduction

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetVariable(parId, 'variable.custom_size') # variable.custom_size 是粒子json文件中自定义的变量
```



## Hide

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    隐藏粒子发射器(不渲染)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 请注意，这个函数并不停止粒子发射器的更新，因此粒子发射器在没有绑定实体或被设计为仅播放一次的情况下，会因为播放结束而自然销毁。
    - 可以和Show函数配合使用。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.IsHiding(parId)

# 可以等待粒子出现后调用
comp.Hide(parId)
print comp.IsHiding(parId)
```



## IsHiding

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    返回粒子发射器是否正在被隐藏(不渲染)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示粒子发射器是否正在隐藏 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.IsHiding(parId)
comp.Hide(parId)
print comp.IsHiding(parId)
```



## IsPausing

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    返回粒子发射器的逻辑是否正在被暂停

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示粒子发射器是否被暂停 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.IsPausing(parId)
comp.Pause(parId)
print comp.IsPausing(parId)
```



## Pause

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    暂停粒子发射器的逻辑更新，但保持渲染状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 可以和Resume函数配合使用，用于暂停粒子发射器的逻辑。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.IsPausing(parId)

# 等待一段时间后调用可以看到时间静止的效果
comp.Pause(parId)
print comp.IsPausing(parId)
```



## Play

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    播放粒子发射器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 粒子发射器在创建时就会立即播放，因此不需要手动调用这个函数。
    - 这个函数等价于调用Resume和Show，如果同时需要这两个功能，建议直接使用这个函数。
    - 这个函数用于和Stop函数配合使用，可以使粒子发射器在被停止的时间点继续播放(恢复逻辑更新、开启渲染)。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
comp.Stop(parId)
print comp.IsHiding(parId)
print comp.IsPausing(parId)

comp.Play(parId)
print comp.IsHiding(parId)
print comp.IsPausing(parId)
```



## PlayAt

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子发射器播放时间点

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | at_second | float | 播放时间点 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 这个函数可以和Stop函数配合使用(跳转到指定时间点、继续逻辑更新且开启渲染)。
    - 这个函数可以使粒子发射器跳转到它的某个时间点进行播放。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.GetLoopAge(parId)

comp.PlayAt(parId, 0.5)
print comp.GetLoopAge(parId)
```



## Remove

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    销毁指定粒子发射器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 对于不存在的粒子发射器id不会进行任何操作 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 原版的雨水等粒子发射器目前无法通过类似接口销毁，可能是因为它们使用了旧版的微软粒子系统

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.Exist(parId)
comp.Remove(parId)
print comp.Exist(parId)
```



## RemoveByName

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    销毁场景中指定名称(粒子发射器json中的identifier)的所有粒子发射器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | effect_name | str | 粒子发射器名称(json中的identifier) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 原版的雨水等粒子发射器目前无法通过类似接口销毁，可能是因为它们使用了旧版的微软粒子系统进行管理

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.Exist(parId)
comp.RemoveByName("netease:tutorial_particle")
print comp.Exist(parId)
```



## Replay

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    重播粒子发射器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 这个函数可以和Stop函数配合使用(重新进行逻辑更新、开启渲染)。
    - 这个函数可以使粒子发射器回到它的时间点零，重新播放(不能用于已经被销毁的粒子发射器)。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))

# 可以等待一段时间后调用
comp.Replay(parId)
```



## Resume

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    恢复粒子发射器的逻辑更新，不影响渲染状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 可以和Pause函数配合使用，用于恢复粒子发射器的逻辑更新。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
comp.Pause(parId)
print comp.IsPausing(parId)

# 可以等待一段时间后调用
comp.Resume(parId)
print comp.IsPausing(parId)
```



## SetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子发射器位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | pos | Tuple | 三维 表示粒子发射器局部空间位置 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 粒子发射器没有进行绑定(即 被放在世界空间)时，它的局部空间位置就是世界空间位置。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "leftitem", (0, 1, 0), (0, 0, 0))
parId1 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, -1, 0), (0, 0, 0))

comp.SetPos(parId0, (0, 0.5, 0))
comp.SetPos(parId1) # (0, 0, 0)
```



## SetRelative

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子是否在局部空间进行计算

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 需要粒子发射器已绑定实体 |
    | is_relative | bool | 表示粒子是否在局部空间进行计算 默认参数值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 此函数对于没有绑定的粒子发射器无效
    - 有关的值可以在粒子发射器json文件中的minecraft:emitter_local_space组件内预先定义，
        如果没有该组件，则默认在世界坐标系下(False)进行变换
    - 设置relative为False时，涉及粒子运动相关的计算都会当作是在世界空间进行的。
    - 设置relative为True时，涉及粒子运动相关的计算都会当作是在局部空间进行的。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

# 开发者可以对比两者的区别来理解两个不同的计算空间
parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "leftitem", (0, 1.0, 0), (90, 0, 0))
comp.SetRelative(parId0, False)
parId1 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 1.0, 0), (90, 0, 0))
comp.SetRelative(parId1, True)
```



## SetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子发射器局部旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | rot | Tuple | 粒子发射器三维旋转(使用角度制，按照ZYX顺序旋转) 默认值为(0, 0, 0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 如果粒子发射器没有进行绑定，则它的局部空间旋转就是世界空间旋转

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "leftitem", (0, 0, 0), (0, 0, 0))
parId1 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
comp.SetRot(parId1, (0, 0, 90))
```



## SetTimeScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子发射器的播放速度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | scale | float | 表示播放倍率 可以为负数进行倒放 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 倒放时已经消失的粒子(请注意是单个粒子而不是粒子发射器)不会重新出现，也不会生成新的粒子
    - 如果倒放到了时间点0，没有绑定或者不循环播放的粒子发射器会被销毁

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "leftitem")
# comp.SetTimeScale(parId0, 1.0)
parId1 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem")
comp.SetTimeScale(parId1, 0.2)
```



## SetVariable

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    设置粒子发射器的Molang变量值

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |
    | variable_name | str | Molang变量名 |
    | value | float | 表示粒子发射器的Molang变量值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - Molang变量可以在粒子发射器json文件内自行定义。
    - 另外，粒子发射器以及粒子内置了一些Molang变量可供使用:
        
            variable.emitter_random_1   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_2   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_3   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_random_4   粒子发射器随机数，范围是0.0到1.0，仅在粒子发射器创建时生成一次
            variable.emitter_lifetime   粒子发射器的播放周期(生命周期)
            variable.emitter_age        粒子发射器当前播放时间
            variable.entity_scale       当粒子发射器绑定实体时，这个值表示绑定实体的大小缩放
            variable.particle_lifetime  粒子的生命周期
            variable.particle_age       粒子生成后已经过的时间
            variable.particle_random_1  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_2  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_3  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
            variable.particle_random_4  粒子随机数，范围是0.0到1.0，仅在粒子生成时生成一次
        部分内置的变量(例如variable.emitter_age)会每帧进行刷新，修改它们的值可能会没有任何效果。
    - 关于Molang表达式的使用，目前大家可以参考微软官方文档:
        https://docs.microsoft.com/en-us/minecraft/creator/reference/content/molangreference/examples/molangconcepts/molangintroduction

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId0 = comp.CreateBindEntity("netease:tutorial_particle", localId, "leftitem", (0, 0, 0), (0, 0, 0))
parId1 = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))

comp.SetVariable(parId1, "variable.custom_size", 0.1) # 修改内置的Molang值效果不明显甚至无效，因此建议自定义变量名
```



## Show

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    显示粒子发射器(开启渲染)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 可以和Hide函数配合使用，用于恢复粒子发射器的显示。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
# 可以等待粒子出现后调用
comp.Hide(parId)
print comp.IsHiding(parId)

# 可以等待粒子隐藏后调用
comp.Show(parId)
print comp.IsHiding(parId)
```



## Stop

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    停止粒子发射器播放(不渲染且不更新逻辑)

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - 这个函数等价于调用Pause和Hide，如果同时需要这两个功能，建议直接使用这个函数。
    - 因为逻辑被停止更新，所以粒子发射器不会由于播放结束而被自然销毁。
    - 可以使用Play、Replay或PlayAt函数来播放被停止的粒子发射器。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (0, 0, 0), (0, 0, 0))
print comp.IsHiding(parId)
print comp.IsPausing(parId)

# 可以等待一段时间后调用
comp.Stop(parId)
print comp.IsHiding(parId)
print comp.IsPausing(parId)
```



## Unbind

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleSystemCompClient.ParticleSystemCompClient

- 描述

    解除指定粒子发射器的绑定状态

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | par_id | int | 粒子发射器id 需要已经创建且未被销毁的粒子发射器 |
    | keep_position | bool | 解绑后是否保持粒子发射器在世界空间的位置 默认值为True |
    | keep_rotation | bool | 解绑后是否保持粒子发射器在世界空间的旋转 默认值为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 表示调用是否成功 |

- 备注
    - keep_position为False时，解绑后的粒子发射器将使用绑定时的局部偏移作为世界空间位置(即例子中的(6, 6, 6))
        keep_rotation为False时，解绑后的粒子发射器将使用绑定时的局部旋转作为世界空间旋转(即例子中的(0, 0, 0))
    - keep_position为True时，解绑后的粒子发射器会保持在解绑前一刻所在的世界空间位置
        keep_rotation为True时，解绑后的粒子发射器会保持解绑前一刻的世界空间旋转
    - 请注意，如果粒子发射器出现在世界空间(即 没有绑定实体)，
        即使粒子发射器json文件定义了minecraft:emitter_lifetime_looping组件，
        也只会播放一次或一个周期，随后销毁

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSystem(None)
localId = clientApi.GetLocalPlayerId()

parId = comp.CreateBindEntity("netease:tutorial_particle", localId, "rightitem", (6, 6, 6), (0, 0, 0))
comp.Unbind(parId)
```

## 文字面板

# 文字面板

## CreateTextBoardInWorld

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    创建文字面板

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | text | str | 文字显示内容 |
    | textColor | tuple(float,float,float,float) | 文字颜色的RGBA值，范围0-1 |
    | boardColor | tuple(float,float,float,float) | 可选参数，默认None，设置为黑色，面板颜色的RGBA值，范围0-1 |
    | faceCamera | bool | 是否始终朝向相机, 默认为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 返回生成的id，如果生成失败，返回None |

- 备注
    - 切换维度后会自动隐藏非本维度创建的而且没有绑定实体的文字面板, 回到该维度后会自动重新显示

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
comp.CreateTextBoardInWorld("我显示在世界坐标位置",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1), True)
```



## RemoveTextBoard

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    删除文字面板

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 创建的时候返回的id |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否删除成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在世界坐标位置",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1), True)
if boardId:
    comp.RemoveTextBoard(boardId)
```



## SetBoardBackgroundColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    修改背景颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | backgroundColor | tuple(float,float,float,float) | 颜色的RGBA值，范围0-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardBackgroundColor(boardId, (1.0, 1.0, 1.0, 1.0))
```



## SetBoardBindEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    文字面板绑定实体对象

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | bindEntityId | str | 绑定entity的Id; 如果为None，则为取消实体绑定, 此时下面参数为世界坐标和旋转 |
    | offset | tuple(float,float,float) | 相对于实体的偏移量 |
    | rot | tuple(float,float,float) | 相对于实体的偏移角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
```



## SetBoardDepthTest

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    设置是否开启深度测试, 默认状态下是开启

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | depthTest | bool | True为开启深度测试,False为不开启 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardDepthTest(boardId, False)
```



## SetBoardFaceCamera

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    设置文字面板的朝向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | faceCamera | bool | 是否始终朝向相机, 默认为True |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardFaceCamera(boardId, True)
```



## SetBoardPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    修改位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | pos | tuple(float,float,float) | 坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardPos(boardId, (0.0, 3.0, 0.0))
```



## SetBoardRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    修改旋转角度, 若设置了文本朝向相机，则旋转角度的修改不会生效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | rot | tuple(float,float,float) | 角度(不是弧度) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardRot(boardId, (45.0, 90.0, 0.0))
```



## SetBoardScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    内容整体缩放

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | scale | tuple(float,float) | x,y方向上的缩放值,要求值大于0,正常状态下是(1.0,1.0) |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardScale(boardId, (2.0, 2.0))
```



## SetBoardTextColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    修改字体颜色

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板的id |
    | textColor | tuple(float,float,float,float) | 颜色的RGBA值，范围0-1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 返回是否设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("我显示在玩家头顶",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetBoardBindEntity(boardId, clientApi.GetLocalPlayerId(), (0.0, 1.5, 0.0), (0.0, 0.0, 0.0))
    comp.SetBoardTextColor(boardId, (1.0, 1.0, 0.0, 0.8))
```



## SetText

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.textBoardCompClient.TextBoardComponentClient

- 描述

    修改文字面板内容

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | boardId | int | 文字面板id |
    | text | str | 文字内容 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否修改成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateTextBoard(clientApi.GetLevelId())
boardId = comp.CreateTextBoardInWorld("初始文字",(0.5, 0.4, 0.3, 0.8),(0, 0, 0, 1),True)
if boardId:
    comp.SetText(boardId, "修改后的文字")
```

## 模型特效

# 模型特效

## CreateEngineEffectBind

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    指用编辑器保存资源包中models/bind/xxx_bind.json生成编辑好的所有挂点的所有特效。生成的特效会自动进行挂接及播放，编辑器中设为不可见的特效也会进行播放。并且使用这种方式创建的特效，开发者不用维护entity进出视野导致的挂接特效被移除，引擎会在entity每次进入视野时自动创建所有特效。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效配置路径，需要包含json后缀名 |
    | bindEntity | str | 绑定实体的Id |
    | aniName | str | 选择使用哪个模型动作的特效 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | effectEntityId或者None |

- 备注
    - 创建特效前需要将entity的骨骼模型替换为编辑器中的一致（或者其他骨骼相同的模型），否则将挂接失败，替换模型见服务端和客户端的model组件。

- 示例

```python
import mod.client.extraClientApi as clientApi
class MyClientSystem(ClientSystem):
    # 创建
    def createEffect(self):
        # 绑定在本地玩家身上的模型特效
        effectEntityId = self.CreateEngineEffectBind("models/bind/xuenv_bind.json", clientApi.GetLocalPlayerId(), 'idle')

    # 删除
    def removeEffect(self, effectEntityId):
        self.DestroyEntity(effectEntityId)
```



## Pause

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.engineEffectBindControlComp.EngineEffectBindControlComp

- 描述

    暂停模型特效（即使用CreateEngineEffectBind创建的特效）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateEngineEffectBindControl(effectEntityId)
comp.Pause()
```



## Resume

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.engineEffectBindControlComp.EngineEffectBindControlComp

- 描述

    继续播放模型特效（即使用CreateEngineEffectBind创建的特效）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True表示设置成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateEngineEffectBindControl(effectEntityId)
comp.Resume()
```

## 粒子

# 粒子

## Bind

<span style="display:inline;color:#7575f9">客户端</span>

<span id="0"></span>
method in mod.client.component.particleEntityBindComp.ParticleEntityBindComp

- 描述

    绑定entity

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | bindEntityId | str | 绑定的entity的ID |
    | offset | tuple(float,float,float) | 绑定的偏移量，相对绑定entity脚下中心 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |
    | correction | bool | 默认不开启，开启后可以使特效的旋转角度准确设置为参照玩家的相对角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleEntityBind(particleEntityId)
comp.Bind(entityId, (0, 1, 0), (0, 0, 0))
```



<span id="1"></span>
method in mod.client.component.particleSkeletonBindComp.ParticleSkeletonBindComp

- 描述

    绑定骨骼模型

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | modelId | int | 绑定的骨骼模型的ID（见model组件的GetModelId） |
    | boneName | str | 绑定具体骨骼的名称 |
    | offset | tuple(float,float,float) | 绑定的偏移量 |
    | rot | tuple(float,float,float) | 绑定的旋转角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleSkeletonBind(particleEntityId)
comp.Bind(modelId, "root", (0, 1, 0), (0, 0, 0))
```



## CreateEngineParticle

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    用于创建粒子特效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 特效资源路径，需要加上后缀名（一般是json） |
    | pos | tuple(float,float,float) | 创建位置坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int或None | particleEntityId或者None |

- 备注
    - 创建粒子后，可以用返回的particleEntityId创建客户端粒子分类中的相关组件，设置所需属性，以实现各种表现效果。
    - 切换维度后会自动隐藏非本维度创建的而且没有绑定实体的粒子, 回到该维度后会自动重新显示
    - 粒子创建之后需要调用particleControl组件的Play函数才会播放，如果播放非本维度创建的粒子,会同时修改该粒子的创建维度为当前维度

- 示例

```python
import mod.client.extraClientApi as clientApi
class MyClientSystem(ClientSystem):
    # 创建
    def createParticle(self):
        particleEntityId = self.CreateEngineParticle("effects/fire.json", (0,5,0))
        particleControlComp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
        particleControlComp.Play()

    # 删除
    def removeParticle(self, particleEntityId):
        self.DestroyEntity(particleEntityId)
```



## GetParticleEmissionRate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    获取粒子发射器每帧发射粒子的频率。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 粒子发射器每帧发射粒子的频率。 |

- 备注
    - 该接口所获取的值对应粒子特效json文件中"emissionrate"的值

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.GetParticleEmissionRate()
```



## GetParticleMaxNum

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    获取粒子发射器包含的最大粒子数量。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 粒子发射器所包含的最大粒子数量。 |

- 备注
    - 该接口所获取的值对应粒子特效json文件中"numparticles"的值

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.GetParticleMaxNum()
```



## GetParticleMaxSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    获取粒子特效中粒子大小的最大值。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 粒子大小的最大值 |

- 备注
    - 该接口获取的值对应粒子特效json文件中"particlesize"的"max"值。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.GetParticleMaxSize()
```



## GetParticleMinSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    获取粒子特效中粒子大小的最小值。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 粒子大小的最小值。 |

- 备注
    - 该接口获取的值对应粒子特效json文件中"particlesize"的"min"值。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.GetParticleMinSize()
```



## GetParticleVolumeSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    获取粒子发射器的体积大小缩放值。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 粒子发射器的体积大小缩放值。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.GetParticleVolumeSize()
```



## GetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleTransComp.ParticleTransComp

- 描述

    获取粒子发射器的世界坐标位置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 返回粒子发射器的世界坐标位置 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
comp.GetPos()
```



## GetRot

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleTransComp.ParticleTransComp

- 描述

    获取粒子发射器的旋转角度

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 返回粒子发射器的旋转角度 |

- 备注
    - 注意，当使用SetRotation设置旋转角度时，设置的x轴方向的旋转接近90度或者-90度，此时会由于旋转的奇异性，计算旋转角度时会出现除0的问题，因此为了避免这种情况，会采用奇异情况下的计算公式来计算，这种情况接口返回的是与SetRotUseZXY接口所设置的值等价的旋转角度。
    - 该接口获取的旋转值对应接口SetRotUseZXY所设置的旋转值。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
comp.GetRot()
```



## Pause

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    暂停播放，粒子定格在当前时刻，再次调用Play时继续播放

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.Pause()
```



## Play

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    播放粒子特效

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.Play()
```



## SetFadeDistance

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子开始自动调整透明度的距离。粒子与摄像机之间的距离小于该值时会自动调整粒子的透明度，距离摄像机越近，粒子越透明

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fadeDistance | float | 自动调整透明度的距离，应为正数，负数将视作零来处理 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
# 设置该粒子在与相机距离小于3时会自动调整透明度
comp.SetFadeDistance(3)
```



## SetLayer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    粒子默认层级为1，当层级不为1时表示该特效开启特效分层渲染功能。特效（粒子和帧动画）分层渲染时，层级越高渲染越靠后，层级大的会遮挡层级低的，且同一层级的特效会根据特效的相对位置产生正确的相互遮挡关系。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | layer | int | 粒子渲染层级，总共包含0-15的层级。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 该接口只针对粒子进行设置，序列帧特效请使用frameAniControl组件

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
# 设置渲染层级为2
comp.SetLayer(2)
```



## SetParticleEmissionRate

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子发射器每帧发射粒子的频率，频率越大则每帧发射的粒子数量越多，但粒子数量不会超过粒子发射器的粒子容量，同时由于性能考虑，每帧发射的粒子数量也不会超过100个。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | minRate | float | 每帧发射粒子频率的最小值。每帧发射粒子的频率将在频率最小值和频率最大值之间取随机数进行插值。当该值设置为负值时设置将会失败，且该值不能比粒子频率的最大值大。 |
    | maxRate | float | 每帧发射粒子频率的最大值。每帧发射粒子的频率将在频率最小值和频率最大值之间取随机数进行插值。当该值设置为负值时设置将会失败，且该值不能比粒子频率的最小值小。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 该接口所设置的值对应粒子特效json文件中"emissionrate"的值

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
# 扩充粒子发射器的粒子容量
comp.SetParticleMaxNum(1000)
# 提高发射粒子的频率
comp.SetParticleEmissionRate(15,20)
```



## SetParticleMaxNum

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子发射器的粒子容量，即粒子发射器所包含的最大粒子数量。该数量并不代表目前粒子发射器所发射的粒子数量，如需要增加发射的粒子数量，需同时改变粒子的发射频率。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | num | int | 粒子发射器所包含的最大粒子数量，不能为负值，粒子的数量最大值不超过100000。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 考虑到性能的原因，请注意粒子的数量不要设置过大。该接口设置的值对应粒子特效json文件中"numparticles"的值

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.SetParticleMaxNum(1000)
```



## SetParticleSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子特效中粒子大小的最小值及最大值。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | minSize | tuple(float,float) | 粒子大小的最小值(x,y)。x值影响粒子的左右拉伸程度，y值影响粒子的上下拉伸程度。粒子特效中的粒子大小会在最小值和最大值当中取随机值进行决定。当该值设置为负值时设置将会失败，且该值不能比粒子大小的最大值大。 |
    | maxSize | tuple(float,float) | 粒子大小的最大值(x,y)。x值影响粒子的左右拉伸程度，y值影响粒子的上下拉伸程度。粒子特效中的粒子大小会在最小值和最大值当中取随机值进行决定。当该值设置为负值时设置将会失败，且该值不能比粒子大小的最小值小。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 该接口设置的值对应粒子特效json文件中"particlesize"的值。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.SetParticleSize((0.5,0.5),(0.6,0.6))
```



## SetParticleVolumeSize

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子发射器的体积大小缩放，不影响单个粒子的尺寸。粒子发射器的体积越大，则粒子的发射范围越大。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | tuple(float,float,float) | 粒子发射器的体积大小缩放值(x,y,z), x,y,z分别为各个坐标轴方向的缩放值，该值越大该方向发射粒子的范围越大。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 当粒子绑定实体时该设置无效

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.SetParticleVolumeSize((1,0,0))
```



## SetPos

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleTransComp.ParticleTransComp

- 描述

    设置粒子发射器的世界坐标位置

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | pos | tuple(float,float,float) | 世界坐标 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
comp.SetPos((0, 5, 0))
```



## SetRelative

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    当粒子绑定了entity或骨骼模型时，发射出的粒子使用entity坐标系还是世界坐标系。与mcstudio特效编辑器中粒子的“相对挂点运动”选项功能相同。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | relative | bool | True表示相对坐标系，False表示世界坐标系 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
# 使用世界坐标系
comp.SetRelative(False)
```



## SetRotUseZXY

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleTransComp.ParticleTransComp

- 描述

    设置粒子发射器的旋转，旋转顺序按照绕z,x,y轴旋转

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float,float) | 绕局部坐标系的+z，+x，+y轴旋转的角度，旋转顺序按照绕z,x,y轴旋转。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleTrans(particleEntityId)
# 绕z轴旋转90度，然后绕y轴旋转90度
comp.SetRotUseZXY((0, 90, 90))
```



## SetUsePointFiltering

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    设置粒子材质的纹理滤波是否使用点滤波方法。默认为使用双线性滤波

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | true为使用点滤波方法，false为使用默认的双线性滤波 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 使用点滤波的图像通常边缘清晰、可能会有较强烈的锯齿感；使用双线性插值的图像通常比较平滑、可能会使图像一定程度上变得模糊

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
# 设置使用点滤波
comp.SetUsePointFiltering(True)
comp.Play()
```



## Stop

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.particleControlComp.ParticleControlComp

- 描述

    停止粒子播放

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateParticleControl(particleEntityId)
comp.Stop()
```

## 通用

# 通用

## DestroyEntity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    销毁特效

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | int | 销毁的特效ID |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否销毁成功 |

- 备注
    - 支持销毁粒子，序列帧及模型特效，示例见对应的创建接口

