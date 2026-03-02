# ModAPI 接口-后处理

## 目录

- [模糊](#模糊)
- [渐晕](#渐晕)
- [色彩](#色彩)
- [镜头效果](#镜头效果)

---

## 模糊

# 模糊

## CheckGaussianBlurEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    检测是否开启了高斯模糊效果。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True为已开启，False为已关闭。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.CheckGaussianBlurEnabled()
```



## SetEnableGaussianBlur

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置是否开启高斯模糊效果，开启后玩家屏幕周围被模糊，可通过高斯模糊其他接口设置效果参数。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启高斯模糊效果，True为开启，False为关闭。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.SetEnableGaussianBlur(True)
```



## SetGaussianBlurRadius

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置高斯模糊效果的模糊半径，半径越大，模糊程度越大，反之则模糊程度越小。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | radius | float | 模糊半径大小，值的范围为[0,10]，小于或大于这个范围的值将被截取为边界值0或10 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整高斯模糊半径为3
comp.SetGaussianBlurRadius(3)
```

## 渐晕

# 渐晕

## CheckVignetteEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    检测是否开启了屏幕渐晕（Vignette）效果。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True为已开启，False为已关闭。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.CheckVignetteEnabled()
```



## SetEnableVignette

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置是否开启屏幕渐晕（Vignette）效果，开启后玩家屏幕周围将出现渐晕，可通过Vignette其他接口设置效果参数。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启Vignette效果，True为开启，False为关闭。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.SetEnableVignette(True)
```



## SetVignetteCenter

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置渐晕（Vignette）的渐晕中心位置，可改变屏幕渐晕的位置。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | center | tuple(float,float) | 按顺序分别为屏幕位置的x及y值。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整渐晕中心位置为屏幕中心
comp.SetVignetteCenter((0.5,0.5))
```



## SetVignetteRGB

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置渐晕（Vignette）的渐晕颜色，可改变屏幕渐晕的颜色。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | color | tuple(float,float,float) | 按顺序分别为颜色的RGB值，值的范围为[0,255]，小于或大于这个范围的值将被截取为边界值0或255 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 设置颜色的值为红色。
comp.SetVignetteRGB((255,0,0))
```



## SetVignetteRadius

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置渐晕（Vignette）的渐晕半径，半径越大，渐晕越小，玩家的视野范围越大。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | radius | float | 渐晕半径大小，值的范围为[0,1]，小于或大于这个范围的值将被截取为边界值0或1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整渐晕半径为0.5
comp.SetVignetteRadius(0.5)
```



## SetVignetteSmoothness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置渐晕（Vignette）的渐晕模糊系数，模糊系数越大，则渐晕边缘越模糊，模糊的范围也越大

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | radius | float | 渐晕模糊系数，值的范围为[0,1]，小于或大于这个范围的值将被截取为边界值0或1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整渐晕模糊系数为0.5
comp.SetVignetteSmoothness(0.5)
```

## 色彩

# 色彩

## CheckColorAdjustmentEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    检测是否开启了色彩校正效果。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True为已开启，False为已关闭。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.CheckColorAdjustmentEnabled()
```



## SetColorAdjustmentBrightness

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整屏幕色彩亮度，亮度值越大，屏幕越亮，反之则越暗。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | brightness | float | 亮度值大小，值的范围为[0,5]，小于或大于这个范围的值将被截取为边界值0或5 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整亮度值为3
comp.SetColorAdjustmentBrightness(3)
```



## SetColorAdjustmentContrast

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整屏幕色彩对比度，屏幕对比度值越大，色彩差异则越明显，反之则色彩差异越小。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | contrast | float | 对比度值大小，值的范围为[0,5]，小于或大于这个范围的值将被截取为边界值0或5 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整对比度值为3
comp.SetColorAdjustmentContrast(3)
```



## SetColorAdjustmentSaturation

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整屏幕色彩饱和度，屏幕饱和度值越大，色彩则越明显，反之则越灰暗。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | saturation | float | 饱和度值大小，值的范围为[0,5]，小于或大于这个范围的值将被截取为边界值0或5 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整饱和度值为3
comp.SetColorAdjustmentSaturation(3)
```



## SetColorAdjustmentTint

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整屏幕色彩的色调，根据输入的色调和强度来调整屏幕色彩，当强度越大时，屏幕整体颜色越偏向输入的色调。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | intensity | float | 色调强度，值的范围为[0,1]，小于或大于这个范围的值将被截取为边界值0或1 |
    | color | tuple(float,float,float) | 色调值，按顺序分别为颜色的RGB值，值的范围为[0,255]，小于或大于这个范围的值将被截取为边界值0或255 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整屏幕色调为偏红色，强度为0.3
comp.SetColorAdjustmentTint(0.3, (255,0,0))
```



## SetEnableColorAdjustment

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置是否开启色彩校正效果，开启后可进行屏幕色彩调整，可通过色彩校正效果其他接口设置效果参数。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启色彩校正效果，True为开启，False为关闭。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.SetEnableColorAdjustment(True)
```

## 镜头效果

# 镜头效果

## CheckDepthOfFieldEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    检测是否开启了景深效果。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True为已开启，False为已关闭。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.CheckDepthOfFieldEnabled()
```



## CheckLensStainEnabled

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    检测是否开启了镜头污迹效果。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True为已开启，False为已关闭。 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.CheckLensStainEnabled()
```



## ResetLensStainTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    重置污迹效果使用的贴图为系统默认贴图。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.ResetLensStainTexture()
```



## SetDepthOfFieldBlurRadius

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整景深效果模糊半径，模糊半径越大，模糊程度越大，反之则越小。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | radius | float | 模糊半径值大小，值的范围为[0,5]，小于或大于这个范围的值将被截取为边界值0或5 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整模糊半径值为0.3
comp.SetDepthOfFieldBlurRadius(0.3)
```



## SetDepthOfFieldFarBlurScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整景深效果远景模糊大小，远景模糊大小越大，远景的模糊程度越大，反之则越小。注意，远景模糊程度的调节依赖于焦点距离，如果焦点处于较近的距离，那么此时远景处于较清晰的状态，模糊程度大小调节不会很明显。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | float | 远景模糊大小，值的范围为[0,15]，小于或大于这个范围的值将被截取为边界值0或15 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整远景模糊大小值为1.0
comp.SetDepthOfFieldFarBlurScale(1.0)
```



## SetDepthOfFieldFocusDistance

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整景深效果焦点距离，距离越小，则远处模糊，近处清晰；距离越大，则远处清晰，近处模糊。该距离为实际距离，即以玩家相机为起点的世界坐标距离。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | distance | float | 焦点距离值大小，值的范围为[0,100]，小于或大于这个范围的值将被截取为边界值0或100。距离值接近100时将被视为无限远的远景。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 如果想要较好地确认聚焦平面的位置，可以先使用SetDepthOfFieldNearBlurScale以及SetDepthOfFieldFarBlurScale将近景模糊大小和远景模糊大小均设置到最大值，此时只有聚焦平面所在的区域显得清晰，这样可以较为直观的看到聚焦平面的位置，从而方便地调节聚焦平面距离。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整焦点距离值为4，即聚焦在距离玩家4个方块边长的位置上
comp.SetDepthOfFieldFocusDistance(4)
```



## SetDepthOfFieldNearBlurScale

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整景深效果近景模糊大小，近景模糊大小越大，近景的模糊程度越大，反之则越小。注意，近景模糊程度的调节依赖于焦点距离，如果焦点处于较近的距离，那么此时近景处于较清晰的状态，模糊程度大小调节不会很明显。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | scale | float | 近景模糊大小，值的范围为[0,15]，小于或大于这个范围的值将被截取为边界值0或15 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整近景模糊大小值为1.0
comp.SetDepthOfFieldNearBlurScale(1.0)
```



## SetDepthOfFieldUseCenterFocus

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置景深效果是否开启屏幕中心聚焦模式，开启后聚焦距离将被自动设置为屏幕中心所对应的物体所在的距离。在第一人称视角下，聚焦距离将被自动设置为屏幕准心所对应的物体与相机的距离，即自动聚焦准心所对应的物体。在第三人称视角下，由于屏幕中心总是对应着玩家，因此聚焦距离将被自动设置为玩家与相机的距离，即自动聚焦在玩家自己。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启景深效果屏幕中心聚焦模式，True为开启，False为关闭。开启后，原有的焦点距离设置将不再有效，接口SetDepthOfFieldFocusDistance也将失效。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 备注
    - 同样，如果想要较好地确认聚焦点所在的位置，可以先使用SetDepthOfFieldNearBlurScale以及SetDepthOfFieldFarBlurScale将近景模糊大小和远景模糊大小均设置到最大值，此时只有聚焦平面所在的区域显得清晰，这样可以较为直观的看到聚焦平面的位置，从而方便地调节聚焦平面距离。

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 开启屏幕中心聚焦模式
comp.SetDepthOfFieldUseCenterFocus(True)
```



## SetEnableDepthOfField

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置是否开启景深效果，开启后屏幕出现景深效果，根据焦点距离呈现远处模糊近处清晰或者近处模糊远处清晰的效果。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启景深效果，True为开启，False为关闭。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.SetEnableDepthOfField(True)
```



## SetEnableLensStain

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    设置是否开启镜头污迹效果，开启后镜头出现污迹效果，可改变使用的污迹贴图及污迹颜色。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | enable | bool | 是否开启镜头污迹效果，True为开启，False为关闭。 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
comp.SetEnableLensStain(True)
```



## SetLensStainColor

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整镜头污迹颜色，根据输入的颜色和强度来调整污迹色彩，当强度越大时，污迹颜色越偏向输入的颜色。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | intensity | float | 颜色强度，值的范围为[0,1]，小于或大于这个范围的值将被截取为边界值0或1 |
    | color | tuple(float,float,float) | 颜色值，按顺序分别为颜色的RGB值，值的范围为[0,255]，小于或大于这个范围的值将被截取为边界值0或255 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整镜头污迹颜色为偏红色，强度为0.3
comp.SetLensStainColor(0.3, (255,0,0))
```



## SetLensStainIntensity

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    调整镜头污迹强度，强度越大，污迹越明显，反之则越透明。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | intensity | float | 镜头污迹强度值大小，值的范围为[0,1]，小于或大于这个范围的值将被截取为边界值0或1 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 调整污迹强度值为0.4
comp.SetLensStainIntensity(0.4)
```



## SetLensStainTexture

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.postProcessControlComp.PostProcessComponent

- 描述

    开启镜头污迹效果后，污迹效果使用的为系统默认贴图。该接口可改变镜头污迹所使用的贴图。注意贴图最好使用透明背景，否则屏幕将被贴图覆盖。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | texturePath | str | 贴图的相对路径，以“textures/"开头，不需要后缀名 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 设置是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreatePostProcess(levelId)
# 改变污迹贴图为textures/postprocess目录下的my_dirtiness.png。
comp.SetLensStainTexture("textures/postprocess/my_dirtiness")
```

