# PresetAPI 更新信息

## 目录

- [1.23.0](#1230)
- [1.23.1](#1231)
- [1.23.2](#1232)
- [1.23.3](#1233)
- [1.23.4](#1234)
- [1.24.0](#1240)
- [1.24.1](#1241)
- [1.25.0](#1250)
- [2.0.1](#201)
- [2.0.2](#202)
- [2.0.3](#203)
- [2.2.0](#220)

---

## 1.23.0

# 1.23.0

- 新增

1. 新增[Preset.Model.GameObject.GameObject](../预设对象/通用/游戏对象GameObject.md#__init__)，游戏对象<!--by gzxuguobin-->

1. 新增[Preset.Model.GameObject.GameObject.LoadFile](../预设对象/通用/游戏对象GameObject.md#loadfile)，加载指定路径的非python脚本文件内容<!--by gzxuguobin-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset](../预设对象/预设/实体预设EntityPreset.md#__init__)，实体预设<!--by gzxuguobin-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetHealth](../预设对象/预设/实体预设EntityPreset.md#gethealth)，获取实体预设的生命值<!--by gzxuguobin-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetHealth](../预设对象/预设/实体预设EntityPreset.md#sethealth)，设置实体预设的生命值<!--by gzxuguobin-->

1. 新增[Preset.Model.Effect.EffectPreset.EffectPreset](../预设对象/预设/特效预设EffectPreset.md#__init__)，特效预设<!--by gzxuguobin-->

1. 新增[Preset.Model.Effect.EffectPreset.EffectPreset.Play](../预设对象/预设/特效预设EffectPreset.md#play)，播放特效<!--by gzxuguobin-->

1. 新增[Preset.Model.Effect.EffectPreset.EffectPreset.Stop](../预设对象/预设/特效预设EffectPreset.md#stop)，停止播放特效<!--by gzxuguobin-->

1. 新增[Preset.Model.Effect.EffectPreset.EffectPreset.GetResource](../预设对象/预设/特效预设EffectPreset.md#getresource)，获取绑定的json资源<!--by gzxuguobin-->

1. 新增[Preset.Model.Effect.EffectPreset.EffectPreset.SetResource](../预设对象/预设/特效预设EffectPreset.md#setresource)，设置绑定的json资源<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform](../预设对象/通用/坐标变换Transform.md#__init__)，坐标变换Transform<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform.AddOffset](../预设对象/通用/坐标变换Transform.md#addoffset)，给坐标变换位置增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform.AddRotation](../预设对象/通用/坐标变换Transform.md#addrotation)，给坐标变换旋转增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform.AddScale](../预设对象/通用/坐标变换Transform.md#addscale)，给坐标变换缩放增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform.AddTransform](../预设对象/通用/坐标变换Transform.md#addtransform)，给坐标变换增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.Transform.Transform.GetMatrix](../预设对象/通用/坐标变换Transform.md#getmatrix)，获取坐标变换矩阵<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase](../预设对象/零件/零件PartBase.md#__init__)，零件基类<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.InitClient](../预设对象/零件/零件PartBase.md#initclient)，客户端的零件对象初始化入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.InitServer](../预设对象/零件/零件PartBase.md#initserver)，服务端的零件对象初始化入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.TickClient](../预设对象/零件/零件PartBase.md#tickclient)，客户端的零件对象逻辑驱动入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.TickServer](../预设对象/零件/零件PartBase.md#tickserver)，服务端的零件对象逻辑驱动入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnloadClient](../预设对象/零件/零件PartBase.md#unloadclient)，客户端的零件对象卸载逻辑入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnloadServer](../预设对象/零件/零件PartBase.md#unloadserver)，服务端的零件对象卸载逻辑入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.DestroyClient](../预设对象/零件/零件PartBase.md#destroyclient)，客户端的零件对象销毁逻辑入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.DestroyServer](../预设对象/零件/零件PartBase.md#destroyserver)，服务端的零件对象销毁逻辑入口<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.CanAdd](../预设对象/零件/零件PartBase.md#canadd)，判断零件是否可以挂接到指定的父节点上<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.GetTickCount](../预设对象/零件/零件PartBase.md#gettickcount)，获取当前帧数<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.ListenForEvent](../预设对象/零件/零件PartBase.md#listenforevent)，监听指定的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnListenForEvent](../预设对象/零件/零件PartBase.md#unlistenforevent)，反监听指定的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.DefineEvent](../预设对象/零件/零件PartBase.md#defineevent)，定义事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnDefineEvent](../预设对象/零件/零件PartBase.md#undefineevent)，反定义事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.BroadcastEvent](../预设对象/零件/零件PartBase.md#broadcastevent)，广播事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.BroadcastClientEvent](../预设对象/零件/零件PartBase.md#broadcastclientevent)，广播给所有客户端<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.BroadcastServerEvent](../预设对象/零件/零件PartBase.md#broadcastserverevent)，广播给所有服务端<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.NotifyToServer](../预设对象/零件/零件PartBase.md#notifytoserver)，通知服务端触发事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.NotifyToClient](../预设对象/零件/零件PartBase.md#notifytoclient)，通知指定客户端触发事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.BroadcastToAllClient](../预设对象/零件/零件PartBase.md#broadcasttoallclient)，通知指所有客户端触发事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.ListenSelfEvent](../预设对象/零件/零件PartBase.md#listenselfevent)，监听来自自己的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnListenSelfEvent](../预设对象/零件/零件PartBase.md#unlistenselfevent)，反监听来自自己的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.ListenPartEvent](../预设对象/零件/零件PartBase.md#listenpartevent)，监听来自指定零件的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.UnListenPartEvent](../预设对象/零件/零件PartBase.md#unlistenpartevent)，反监听来自指定零件的事件<!--by gzxuguobin-->

1. 新增[Preset.Model.PartBase.PartBase.CreateComponent](../预设对象/零件/零件PartBase.md#createcomponent)，给实体创建组件<!--by gzxuguobin-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset](../预设对象/预设/玩家预设PlayerPreset.md#__init__)，玩家预设<!--by gzxuguobin-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetPlayerId](../预设对象/预设/玩家预设PlayerPreset.md#getplayerid)，获取玩家预设的玩家ID<!--by gzxuguobin-->

1. 新增[Preset.Model.Block.BlockPreset.BlockPreset](../预设对象/预设/方块预设BlockPreset.md#__init__)，方块预设<!--by gzxuguobin-->

1. 新增[Preset.Model.Block.BlockPreset.BlockPreset.GetEngineTypeStr](../预设对象/预设/方块预设BlockPreset.md#getenginetypestr)，获取方块预设的方块类型ID<!--by gzxuguobin-->

1. 新增[Preset.Model.BoxData.BoxData](../预设对象/通用/素材数据BoxData.md#__init__)，素材数据<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase](../预设对象/预设/预设基类PresetBase.md#__init__)，预设基类<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetIsAlive](../预设对象/预设/预设基类PresetBase.md#getisalive)，获取预设的存活状态<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetGameObjectById](../预设对象/预设/预设基类PresetBase.md#getgameobjectbyid)，获取当前预设节点底下指定ID的游戏对象<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetGameObjectByEntityId](../预设对象/预设/预设基类PresetBase.md#getgameobjectbyentityid)，获取当前预设节点底下指定实体ID的游戏对象<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildPresets](../预设对象/预设/预设基类PresetBase.md#getchildpresets)，获取当前预设的所有子预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildPresetsByName](../预设对象/预设/预设基类PresetBase.md#getchildpresetsbyname)，获取指定名称的所有子预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildPresetsByType](../预设对象/预设/预设基类PresetBase.md#getchildpresetsbytype)，获取指定类型的所有子预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.Replicate](../预设对象/预设/预设基类PresetBase.md#replicate)，在指定位置坐标下复制当前预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.RemoveChild](../预设对象/预设/预设基类PresetBase.md#removechild)，移除指定的子节点对象<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.AddBoxData](../预设对象/预设/预设基类PresetBase.md#addboxdata)，添加指定的素材数据<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.RemoveBoxData](../预设对象/预设/预设基类PresetBase.md#removeboxdata)，移除指定的素材数据<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.AddPreset](../预设对象/预设/预设基类PresetBase.md#addpreset)，添加指定预设作为子预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.RemovePreset](../预设对象/预设/预设基类PresetBase.md#removepreset)，移除指定的子预设<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.AddPart](../预设对象/预设/预设基类PresetBase.md#addpart)，添加指定零件作为子零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.RemovePart](../预设对象/预设/预设基类PresetBase.md#removepart)，移除指定的子零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetPartsByName](../预设对象/预设/预设基类PresetBase.md#getpartsbyname)，获取指定名称的所有零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetPartByName](../预设对象/预设/预设基类PresetBase.md#getpartbyname)，获取指定名称的第一个零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetPartsByType](../预设对象/预设/预设基类PresetBase.md#getpartsbytype)，获取指定类型的所有零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetPartByType](../预设对象/预设/预设基类PresetBase.md#getpartbytype)，获取指定类型的第一个零件<!--by gzxuguobin-->

1. 新增[Preset.Model.PresetBase.PresetBase.RemovePartsByType](../预设对象/预设/预设基类PresetBase.md#removepartsbytype)，移除指定类型的所有零件<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject](../预设对象/通用/变换对象TransformObject.md#__init__)，变换对象<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetDependencyChunks](../预设对象/通用/变换对象TransformObject.md#getdependencychunks)，获取所有依赖的chunkPos<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetChildTransformObjects](../预设对象/通用/变换对象TransformObject.md#getchildtransformobjects)，获取子TransformObject列表<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetTransformObjects](../预设对象/通用/变换对象TransformObject.md#gettransformobjects)，获取TransformObject列表<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetChildGameObjects](../预设对象/通用/变换对象TransformObject.md#getchildgameobjects)，获取GameObject列表<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetGameObjects](../预设对象/通用/变换对象TransformObject.md#getgameobjects)，获取GameObject列表<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetGameObjectById](../预设对象/通用/变换对象TransformObject.md#getgameobjectbyid)，根据ID获取GameObject<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetGameObjectByEntityId](../预设对象/通用/变换对象TransformObject.md#getgameobjectbyentityid)，根据实体ID获取GameObject<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLevelId](../预设对象/通用/变换对象TransformObject.md#getlevelid)，获取当前对象所在的level_id<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetDisplayName](../预设对象/通用/变换对象TransformObject.md#getdisplayname)，获取当前预设的显示名称<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetDisplayPath](../预设对象/通用/变换对象TransformObject.md#getdisplaypath)，获取当前预设到根节点的显示路径<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLocalTransform](../预设对象/通用/变换对象TransformObject.md#getlocaltransform)，获取当前预设的局部坐标变换<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetLocalTransform](../预设对象/通用/变换对象TransformObject.md#setlocaltransform)，设置当前预设的局部坐标变换<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLocalPosition](../预设对象/通用/变换对象TransformObject.md#getlocalposition)，获取当前预设的局部坐标位置<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetLocalPosition](../预设对象/通用/变换对象TransformObject.md#setlocalposition)，设置当前预设的局部坐标位置<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLocalRotation](../预设对象/通用/变换对象TransformObject.md#getlocalrotation)，获取当前预设的局部坐标旋转<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetLocalRotation](../预设对象/通用/变换对象TransformObject.md#setlocalrotation)，设置当前预设的局部坐标旋转<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLocalScale](../预设对象/通用/变换对象TransformObject.md#getlocalscale)，获取当前预设的局部坐标缩放<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetLocalScale](../预设对象/通用/变换对象TransformObject.md#setlocalscale)，设置当前预设的局部坐标缩放<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetWorldTransform](../预设对象/通用/变换对象TransformObject.md#getworldtransform)，获取当前预设的世界坐标变换<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetWorldMatrix](../预设对象/通用/变换对象TransformObject.md#getworldmatrix)，获取世界坐标变换矩阵<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetLocalMatrix](../预设对象/通用/变换对象TransformObject.md#getlocalmatrix)，获取局部坐标变换矩阵<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetWorldTransform](../预设对象/通用/变换对象TransformObject.md#setworldtransform)，设置当前预设的世界坐标变换<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetWorldPosition](../预设对象/通用/变换对象TransformObject.md#getworldposition)，获取当前预设的世界坐标位置<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetWorldPosition](../预设对象/通用/变换对象TransformObject.md#setworldposition)，设置当前预设的世界坐标位置<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetWorldRotation](../预设对象/通用/变换对象TransformObject.md#getworldrotation)，获取当前预设的世界坐标旋转<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetWorldRotation](../预设对象/通用/变换对象TransformObject.md#setworldrotation)，设置当前预设的世界坐标旋转<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetWorldScale](../预设对象/通用/变换对象TransformObject.md#getworldscale)，获取当前预设的世界坐标缩放<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetWorldScale](../预设对象/通用/变换对象TransformObject.md#setworldscale)，设置当前预设的世界坐标缩放<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddLocalOffset](../预设对象/通用/变换对象TransformObject.md#addlocaloffset)，给局部坐标变换位置增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddWorldOffset](../预设对象/通用/变换对象TransformObject.md#addworldoffset)，给世界坐标变换位置增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddLocalRotation](../预设对象/通用/变换对象TransformObject.md#addlocalrotation)，给局部坐标变换旋转增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddWorldRotation](../预设对象/通用/变换对象TransformObject.md#addworldrotation)，给世界坐标变换旋转增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddLocalScale](../预设对象/通用/变换对象TransformObject.md#addlocalscale)，给局部坐标变换缩放增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddWorldScale](../预设对象/通用/变换对象TransformObject.md#addworldscale)，给世界坐标变换缩放增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddLocalTransform](../预设对象/通用/变换对象TransformObject.md#addlocaltransform)，给局部坐标变换增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.AddWorldTransform](../预设对象/通用/变换对象TransformObject.md#addworldtransform)，给世界坐标变换增加偏移量<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetRootParent](../预设对象/通用/变换对象TransformObject.md#getrootparent)，获取当前预设所在的根预设<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetParent](../预设对象/通用/变换对象TransformObject.md#getparent)，获取当前预设的父预设<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.SetParent](../预设对象/通用/变换对象TransformObject.md#setparent)，设置当前预设的父预设<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.GetManager](../预设对象/通用/变换对象TransformObject.md#getmanager)，获取当前预设所在的预设管理器<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.Unload](../预设对象/通用/变换对象TransformObject.md#unload)，卸载当前预设<!--by gzxuguobin-->

1. 新增[Preset.Model.TransformObject.TransformObject.Destroy](../预设对象/通用/变换对象TransformObject.md#destroy)，销毁当前预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetAllPresets](../预设管理/PresetApi.md#getallpresets)，获取所有预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetBlockPresetByPosition](../预设管理/PresetApi.md#getblockpresetbyposition)，获取指定位置的第一个方块预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetGameObjectByEntityId](../预设管理/PresetApi.md#getgameobjectbyentityid)，获取指定实体ID的游戏对象<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetGameObjectById](../预设管理/PresetApi.md#getgameobjectbyid)，获取指定ID的游戏对象<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetManager](../预设管理/PresetApi.md#getmanager)，获取预设管理器<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetPresetByName](../预设管理/PresetApi.md#getpresetbyname)，获取指定名称的第一个预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetPresetByType](../预设管理/PresetApi.md#getpresetbytype)，获取指定类型的第一个预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetPresetsByName](../预设管理/PresetApi.md#getpresetsbyname)，获取指定名称的所有预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetPresetsByType](../预设管理/PresetApi.md#getpresetsbytype)，获取指定类型的所有预设<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.GetTickCount](../预设管理/PresetApi.md#gettickcount)，获取当前帧数<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.LoadPartByModulePath](../预设管理/PresetApi.md#loadpartbymodulepath)，通过模块相对路径加载零件并实例化<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.LoadPartByType](../预设管理/PresetApi.md#loadpartbytype)，通过类名加载零件并实例化<!--by gzxuguobin-->

1. 新增[Preset.Controller.PresetApi.SpawnPreset](../预设管理/PresetApi.md#spawnpreset)，在指定坐标变换处生成指定预设<!--by gzxuguobin-->

1. 新增[Preset.Parts.PartEvent.OnTriggerEntityEnter](../预设对象/零件/零件事件PartEvent.md#ontriggerentityenter)，触发器范围有实体进入时触发<!--by gzxuguobin-->

1. 新增[Preset.Parts.PartEvent.OnTriggerEntityExit](../预设对象/零件/零件事件PartEvent.md#ontriggerentityexit)，触发器范围有实体离开时触发<!--by gzxuguobin-->

1. 新增[Preset.Parts.PartEvent.OnTriggerEntityStay](../预设对象/零件/零件事件PartEvent.md#ontriggerentitystay)，触发器范围有实体停留时触发<!--by gzxuguobin-->



## 1.23.1

# 1.23.1

* 注：该版本功能仅在modpc开发包生效，移动端生效请期待1.24大版本更新。

- 新增

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetMaxHealth](../预设对象/预设/实体预设EntityPreset.md#getmaxhealth)，获取实体预设的最大生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetMaxHealth](../预设对象/预设/实体预设EntityPreset.md#setmaxhealth)，设置实体预设的最大生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetSpeed](../预设对象/预设/实体预设EntityPreset.md#getspeed)，获取实体预设的速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetSpeed](../预设对象/预设/实体预设EntityPreset.md#setspeed)，设置实体预设的速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetMaxSpeed](../预设对象/预设/实体预设EntityPreset.md#getmaxspeed)，获取实体预设的最大速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetMaxSpeed](../预设对象/预设/实体预设EntityPreset.md#setmaxspeed)，设置实体预设的最大速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetDamage](../预设对象/预设/实体预设EntityPreset.md#getdamage)，获取实体预设的伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetDamage](../预设对象/预设/实体预设EntityPreset.md#setdamage)，设置实体预设的伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetMaxDamage](../预设对象/预设/实体预设EntityPreset.md#getmaxdamage)，获取实体预设的最大伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetMaxDamage](../预设对象/预设/实体预设EntityPreset.md#setmaxdamage)，设置实体预设的最大伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.ShowHealth](../预设对象/预设/实体预设EntityPreset.md#showhealth)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetAttackTarget](../预设对象/预设/实体预设EntityPreset.md#setattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.ResetAttackTarget](../预设对象/预设/实体预设EntityPreset.md#resetattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetAttackTarget](../预设对象/预设/实体预设EntityPreset.md#getattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetKnockback](../预设对象/预设/实体预设EntityPreset.md#setknockback)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetOwner](../预设对象/预设/实体预设EntityPreset.md#setowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetOwner](../预设对象/预设/实体预设EntityPreset.md#getowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.IsOnFire](../预设对象/预设/实体预设EntityPreset.md#isonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetOnFire](../预设对象/预设/实体预设EntityPreset.md#setonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetAttrValue](../预设对象/预设/实体预设EntityPreset.md#getattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetAttrMaxValue](../预设对象/预设/实体预设EntityPreset.md#getattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetAttrValue](../预设对象/预设/实体预设EntityPreset.md#setattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetAttrMaxValue](../预设对象/预设/实体预设EntityPreset.md#setattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.IsInLava](../预设对象/预设/实体预设EntityPreset.md#isinlava)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.IsOnGround](../预设对象/预设/实体预设EntityPreset.md#isonground)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetAuxValue](../预设对象/预设/实体预设EntityPreset.md#getauxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetCurrentAirSupply](../预设对象/预设/实体预设EntityPreset.md#getcurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetMaxAirSupply](../预设对象/预设/实体预设EntityPreset.md#getmaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetCurrentAirSupply](../预设对象/预设/实体预设EntityPreset.md#setcurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetMaxAirSupply](../预设对象/预设/实体预设EntityPreset.md#setmaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.IsConsumingAirSupply](../预设对象/预设/实体预设EntityPreset.md#isconsumingairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetRecoverTotalAirSupplyTime](../预设对象/预设/实体预设EntityPreset.md#setrecovertotalairsupplytime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetSourceId](../预设对象/预设/实体预设EntityPreset.md#getsourceid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetCollisionBoxSize](../预设对象/预设/实体预设EntityPreset.md#setcollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetCollisionBoxSize](../预设对象/预设/实体预设EntityPreset.md#getcollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetBlockControlAi](../预设对象/预设/实体预设EntityPreset.md#setblockcontrolai)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetDimensionId](../预设对象/预设/实体预设EntityPreset.md#getdimensionid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.ChangeDimension](../预设对象/预设/实体预设EntityPreset.md#changedimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.RemoveEffect](../预设对象/预设/实体预设EntityPreset.md#removeeffect)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.AddEffect](../预设对象/预设/实体预设EntityPreset.md#addeffect)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetEffects](../预设对象/预设/实体预设EntityPreset.md#geteffects)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.TriggerCustomEvent](../预设对象/预设/实体预设EntityPreset.md#triggercustomevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.IsAlive](../预设对象/预设/实体预设EntityPreset.md#isalive)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetGravity](../预设对象/预设/实体预设EntityPreset.md#getgravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetGravity](../预设对象/预设/实体预设EntityPreset.md#setgravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetHurt](../预设对象/预设/实体预设EntityPreset.md#sethurt)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetImmuneDamage](../预设对象/预设/实体预设EntityPreset.md#setimmunedamage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetModAttr](../预设对象/预设/实体预设EntityPreset.md#setmodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetModAttr](../预设对象/预设/实体预设EntityPreset.md#getmodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.RegisterModAttrUpdateFunc](../预设对象/预设/实体预设EntityPreset.md#registermodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.UnRegisterModAttrUpdateFunc](../预设对象/预设/实体预设EntityPreset.md#unregistermodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.GetName](../预设对象/预设/实体预设EntityPreset.md#getname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetName](../预设对象/预设/实体预设EntityPreset.md#setname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetShowName](../预设对象/预设/实体预设EntityPreset.md#setshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetAlwaysShowName](../预设对象/预设/实体预设EntityPreset.md#setalwaysshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityPreset.EntityPreset.SetPersistence](../预设对象/预设/实体预设EntityPreset.md#setpersistence)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetGameObjectById](../预设对象/零件/零件PartBase.md#getgameobjectbyid)，获取指定ID的游戏对象<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetGameObjectByEntityId](../预设对象/零件/零件PartBase.md#getgameobjectbyentityid)，获取指定实体ID的游戏对象<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.CreateGameObjectByEntityId](../预设对象/零件/零件PartBase.md#creategameobjectbyentityid)，根据指定实体ID创建游戏对象，已存在则直接返回<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.CreateEventData](../预设对象/零件/零件PartBase.md#createeventdata)，反定义事件<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.IsSneaking](../预设对象/预设/玩家预设PlayerPreset.md#issneaking)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetHunger](../预设对象/预设/玩家预设PlayerPreset.md#gethunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.SetHunger](../预设对象/预设/玩家预设PlayerPreset.md#sethunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.SetMotion](../预设对象/预设/玩家预设PlayerPreset.md#setmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetMotion](../预设对象/预设/玩家预设PlayerPreset.md#getmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.SetStepHeight](../预设对象/预设/玩家预设PlayerPreset.md#setstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetStepHeight](../预设对象/预设/玩家预设PlayerPreset.md#getstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.ResetStepHeight](../预设对象/预设/玩家预设PlayerPreset.md#resetstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetExp](../预设对象/预设/玩家预设PlayerPreset.md#getexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.AddExp](../预设对象/预设/玩家预设PlayerPreset.md#addexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetTotalExp](../预设对象/预设/玩家预设PlayerPreset.md#gettotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.SetTotalExp](../预设对象/预设/玩家预设PlayerPreset.md#settotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.IsFlying](../预设对象/预设/玩家预设PlayerPreset.md#isflying)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.ChangeFlyState](../预设对象/预设/玩家预设PlayerPreset.md#changeflystate)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.GetLevel](../预设对象/预设/玩家预设PlayerPreset.md#getlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.AddLevel](../预设对象/预设/玩家预设PlayerPreset.md#addlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerPreset.PlayerPreset.SetPrefixAndSuffixName](../预设对象/预设/玩家预设PlayerPreset.md#setprefixandsuffixname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcomponent)，给实体创建组件<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActionComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactioncomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityAttackTarget](../预设对象/通用/SDK接口封装SdkInterface.md#setentityattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ResetEntityAttackTarget](../预设对象/通用/SDK接口封装SdkInterface.md#resetentityattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityAttackTarget](../预设对象/通用/SDK接口封装SdkInterface.md#getentityattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetMobKnockback](../预设对象/通用/SDK接口封装SdkInterface.md#setmobknockback)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorLootComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactorlootcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnLootTable](../预设对象/通用/SDK接口封装SdkInterface.md#spawnloottable)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnLootTableWithActor](../预设对象/通用/SDK接口封装SdkInterface.md#spawnloottablewithactor)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorMotionComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactormotioncomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetDirFromRot](../预设对象/通用/SDK接口封装SdkInterface.md#getdirfromrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityMotion](../预设对象/通用/SDK接口封装SdkInterface.md#setentitymotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityMotion](../预设对象/通用/SDK接口封装SdkInterface.md#getentitymotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetInputVector](../预设对象/通用/SDK接口封装SdkInterface.md#getinputvector)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.LockInputVector](../预设对象/通用/SDK接口封装SdkInterface.md#lockinputvector)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.UnlockInputVector](../预设对象/通用/SDK接口封装SdkInterface.md#unlockinputvector)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorOwnerComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactorownercomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityOwner](../预设对象/通用/SDK接口封装SdkInterface.md#setentityowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityOwner](../预设对象/通用/SDK接口封装SdkInterface.md#getentityowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorPushableComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactorpushablecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetActorPushable](../预设对象/通用/SDK接口封装SdkInterface.md#setactorpushable)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateAttrComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createattrcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsEntityOnFire](../预设对象/通用/SDK接口封装SdkInterface.md#isentityonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityOnFire](../预设对象/通用/SDK接口封装SdkInterface.md#setentityonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityAttrValue](../预设对象/通用/SDK接口封装SdkInterface.md#getentityattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityAttrMaxValue](../预设对象/通用/SDK接口封装SdkInterface.md#getentityattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityAttrValue](../预设对象/通用/SDK接口封装SdkInterface.md#setentityattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityAttrMaxValue](../预设对象/通用/SDK接口封装SdkInterface.md#setentityattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerStepHeight](../预设对象/通用/SDK接口封装SdkInterface.md#setplayerstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerStepHeight](../预设对象/通用/SDK接口封装SdkInterface.md#getplayerstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ResetPlayerStepHeight](../预设对象/通用/SDK接口封装SdkInterface.md#resetplayerstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsEntityInLava](../预设对象/通用/SDK接口封装SdkInterface.md#isentityinlava)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsEntityOnGround](../预设对象/通用/SDK接口封装SdkInterface.md#isentityonground)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateAuxValueComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createauxvaluecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityAuxValue](../预设对象/通用/SDK接口封装SdkInterface.md#getentityauxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBiomeComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createbiomecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBiomeName](../预设对象/通用/SDK接口封装SdkInterface.md#getbiomename)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBlockComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createblockcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RegisterBlockPatterns](../预设对象/通用/SDK接口封装SdkInterface.md#registerblockpatterns)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateMicroBlockResStr](../预设对象/通用/SDK接口封装SdkInterface.md#createmicroblockresstr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBlockEntityData](../预设对象/通用/SDK接口封装SdkInterface.md#createblockentitydata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetCustomBlockEntityData](../预设对象/通用/SDK接口封装SdkInterface.md#getcustomblockentitydata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBlockInfoComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createblockinfocomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlock](../预设对象/通用/SDK接口封装SdkInterface.md#getblock)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetBlock](../预设对象/通用/SDK接口封装SdkInterface.md#setblock)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetTopBlockHeight](../预设对象/通用/SDK接口封装SdkInterface.md#gettopblockheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlockDestroyTime](../预设对象/通用/SDK接口封装SdkInterface.md#getblockdestroytime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlockEntityData](../预设对象/通用/SDK接口封装SdkInterface.md#getblockentitydata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBlockStateComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createblockstatecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlockStates](../预设对象/通用/SDK接口封装SdkInterface.md#getblockstates)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetBlockStates](../预设对象/通用/SDK接口封装SdkInterface.md#setblockstates)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlockAuxValueFromStates](../预设对象/通用/SDK接口封装SdkInterface.md#getblockauxvaluefromstates)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBlockStatesFromAuxValue](../预设对象/通用/SDK接口封装SdkInterface.md#getblockstatesfromauxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBlockUseEventWhiteList](../预设对象/通用/SDK接口封装SdkInterface.md#createblockuseeventwhitelist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddBlockItemListenForUseEvent](../预设对象/通用/SDK接口封装SdkInterface.md#addblockitemlistenforuseevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RemoveBlockItemListenForUseEvent](../预设对象/通用/SDK接口封装SdkInterface.md#removeblockitemlistenforuseevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ClearAllListenForBlockUseEventItems](../预设对象/通用/SDK接口封装SdkInterface.md#clearalllistenforblockuseeventitems)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBreathComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createbreathcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetUnitBubbleAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#getunitbubbleairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityCurrentAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#getentitycurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityMaxAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#getentitymaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityCurrentAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#setentitycurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityMaxAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#setentitymaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsEntityConsumingAirSupply](../预设对象/通用/SDK接口封装SdkInterface.md#isentityconsumingairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityRecoverTotalAirSupplyTime](../预设对象/通用/SDK接口封装SdkInterface.md#setentityrecovertotalairsupplytime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBulletAttributesComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createbulletattributescomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntitySourceId](../预设对象/通用/SDK接口封装SdkInterface.md#getentitysourceid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateChestBlockComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createchestblockcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetChestBoxSize](../预设对象/通用/SDK接口封装SdkInterface.md#getchestboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetChestBoxItemNum](../预设对象/通用/SDK接口封装SdkInterface.md#setchestboxitemnum)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetChestBoxItemExchange](../预设对象/通用/SDK接口封装SdkInterface.md#setchestboxitemexchange)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateChunkSourceComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createchunksourcecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetAddArea](../预设对象/通用/SDK接口封装SdkInterface.md#setaddarea)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.DeleteArea](../预设对象/通用/SDK接口封装SdkInterface.md#deletearea)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.DeleteAllArea](../预设对象/通用/SDK接口封装SdkInterface.md#deleteallarea)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetAllAreaKeys](../预设对象/通用/SDK接口封装SdkInterface.md#getallareakeys)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CheckChunkState](../预设对象/通用/SDK接口封装SdkInterface.md#checkchunkstate)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetLoadedChunks](../预设对象/通用/SDK接口封装SdkInterface.md#getloadedchunks)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetChunkEntities](../预设对象/通用/SDK接口封装SdkInterface.md#getchunkentities)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetChunkMobNum](../预设对象/通用/SDK接口封装SdkInterface.md#getchunkmobnum)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsChunkGenerated](../预设对象/通用/SDK接口封装SdkInterface.md#ischunkgenerated)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateCollisionBoxComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcollisionboxcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityCollisionBoxSize](../预设对象/通用/SDK接口封装SdkInterface.md#setentitycollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityCollisionBoxSize](../预设对象/通用/SDK接口封装SdkInterface.md#getentitycollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateCommandComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcommandcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetCommand](../预设对象/通用/SDK接口封装SdkInterface.md#setcommand)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetCommandPermissionLevel](../预设对象/通用/SDK接口封装SdkInterface.md#getcommandpermissionlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetCommandPermissionLevel](../预设对象/通用/SDK接口封装SdkInterface.md#setcommandpermissionlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetDefaultPlayerPermissionLevel](../预设对象/通用/SDK接口封装SdkInterface.md#getdefaultplayerpermissionlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetDefaultPlayerPermissionLevel](../预设对象/通用/SDK接口封装SdkInterface.md#setdefaultplayerpermissionlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateControlAiComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcontrolaicomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityBlockControlAi](../预设对象/通用/SDK接口封装SdkInterface.md#setentityblockcontrolai)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateDimensionComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createdimensioncomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityDimensionId](../预设对象/通用/SDK接口封装SdkInterface.md#getentitydimensionid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ChangeEntityDimension](../预设对象/通用/SDK接口封装SdkInterface.md#changeentitydimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ChangePlayerDimension](../预设对象/通用/SDK接口封装SdkInterface.md#changeplayerdimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.MirrorDimension](../预设对象/通用/SDK接口封装SdkInterface.md#mirrordimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateDimension](../预设对象/通用/SDK接口封装SdkInterface.md#createdimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RegisterEntityAOIEvent](../预设对象/通用/SDK接口封装SdkInterface.md#registerentityaoievent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.UnRegisterEntityAOIEvent](../预设对象/通用/SDK接口封装SdkInterface.md#unregisterentityaoievent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetUseLocalTime](../预设对象/通用/SDK接口封装SdkInterface.md#setuselocaltime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetUseLocalTime](../预设对象/通用/SDK接口封装SdkInterface.md#getuselocaltime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetLocalTime](../预设对象/通用/SDK接口封装SdkInterface.md#setlocaltime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetLocalTimeOfDay](../预设对象/通用/SDK接口封装SdkInterface.md#setlocaltimeofday)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetLocalTime](../预设对象/通用/SDK接口封装SdkInterface.md#getlocaltime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetLocalDoDayNightCycle](../预设对象/通用/SDK接口封装SdkInterface.md#setlocaldodaynightcycle)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetLocalDoDayNightCycle](../预设对象/通用/SDK接口封装SdkInterface.md#getlocaldodaynightcycle)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateEffectComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createeffectcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RemoveEffectFromEntity](../预设对象/通用/SDK接口封装SdkInterface.md#removeeffectfromentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddEffectToEntity](../预设对象/通用/SDK接口封装SdkInterface.md#addeffecttoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityEffects](../预设对象/通用/SDK接口封装SdkInterface.md#getentityeffects)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateEngineTypeComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createenginetypecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityEngineTypeStr](../预设对象/通用/SDK接口封装SdkInterface.md#getentityenginetypestr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityEngineType](../预设对象/通用/SDK接口封装SdkInterface.md#getentityenginetype)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateEntityEventComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createentityeventcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.TriggerEntityCustomEvent](../预设对象/通用/SDK接口封装SdkInterface.md#triggerentitycustomevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateExtraDataComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createextradatacomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#getextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SaveExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#saveextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#setextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CleanExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#cleanextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetWholeExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#getwholeextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateExpComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createexpcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerExp](../预设对象/通用/SDK接口封装SdkInterface.md#getplayerexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddPlayerExp](../预设对象/通用/SDK接口封装SdkInterface.md#addplayerexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerTotalExp](../预设对象/通用/SDK接口封装SdkInterface.md#getplayertotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerTotalExp](../预设对象/通用/SDK接口封装SdkInterface.md#setplayertotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetOrbExperience](../预设对象/通用/SDK接口封装SdkInterface.md#getorbexperience)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetOrbExperience](../预设对象/通用/SDK接口封装SdkInterface.md#setorbexperience)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateExperienceOrb](../预设对象/通用/SDK接口封装SdkInterface.md#createexperienceorb)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateExplosionComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createexplosioncomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateExplosion](../预设对象/通用/SDK接口封装SdkInterface.md#createexplosion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFeatureComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createfeaturecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddNeteaseFeatureWhiteList](../预设对象/通用/SDK接口封装SdkInterface.md#addneteasefeaturewhitelist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RemoveNeteaseFeatureWhiteList](../预设对象/通用/SDK接口封装SdkInterface.md#removeneteasefeaturewhitelist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ClearAllNeteaseFeatureWhiteList](../预设对象/通用/SDK接口封装SdkInterface.md#clearallneteasefeaturewhitelist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.LocateStructureFeature](../预设对象/通用/SDK接口封装SdkInterface.md#locatestructurefeature)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.LocateNeteaseFeatureRule](../预设对象/通用/SDK接口封装SdkInterface.md#locateneteasefeaturerule)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFlyComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createflycomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsPlayerFlying](../预设对象/通用/SDK接口封装SdkInterface.md#isplayerflying)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ChangePlayerFlyState](../预设对象/通用/SDK接口封装SdkInterface.md#changeplayerflystate)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateGameComponent](../预设对象/通用/SDK接口封装SdkInterface.md#creategamecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.KillEntity](../预设对象/通用/SDK接口封装SdkInterface.md#killentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateEngineEntityByTypeStr](../预设对象/通用/SDK接口封装SdkInterface.md#createengineentitybytypestr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.PlaceStructure](../预设对象/通用/SDK接口封装SdkInterface.md#placestructure)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddTimer](../预设对象/通用/SDK接口封装SdkInterface.md#addtimer)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddRepeatedTimer](../预设对象/通用/SDK接口封装SdkInterface.md#addrepeatedtimer)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CancelTimer](../预设对象/通用/SDK接口封装SdkInterface.md#canceltimer)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntitiesInArea](../预设对象/通用/SDK接口封装SdkInterface.md#getentitiesinarea)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntitiesAround](../预设对象/通用/SDK接口封装SdkInterface.md#getentitiesaround)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ShowHealthBar](../预设对象/通用/SDK接口封装SdkInterface.md#showhealthbar)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetNameDeeptest](../预设对象/通用/SDK接口封装SdkInterface.md#setnamedeeptest)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetScreenSize](../预设对象/通用/SDK接口封装SdkInterface.md#getscreensize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetRenderLocalPlayer](../预设对象/通用/SDK接口封装SdkInterface.md#setrenderlocalplayer)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddPickBlacklist](../预设对象/通用/SDK接口封装SdkInterface.md#addpickblacklist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ClearPickBlacklist](../预设对象/通用/SDK接口封装SdkInterface.md#clearpickblacklist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CheckWordsValid](../预设对象/通用/SDK接口封装SdkInterface.md#checkwordsvalid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CheckNameValid](../预设对象/通用/SDK接口封装SdkInterface.md#checknamevalid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetScreenViewInfo](../预设对象/通用/SDK接口封装SdkInterface.md#getscreenviewinfo)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SimulateTouchWithMouse](../预设对象/通用/SDK接口封装SdkInterface.md#simulatetouchwithmouse)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetCurrentDimension](../预设对象/通用/SDK接口封装SdkInterface.md#getcurrentdimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetChinese](../预设对象/通用/SDK接口封装SdkInterface.md#getchinese)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetDisableHunger](../预设对象/通用/SDK接口封装SdkInterface.md#setdisablehunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetOneTipMessage](../预设对象/通用/SDK接口封装SdkInterface.md#setonetipmessage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPopupNotice](../预设对象/通用/SDK接口封装SdkInterface.md#setpopupnotice)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetTipMessage](../预设对象/通用/SDK接口封装SdkInterface.md#settipmessage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetNotifyMsg](../预设对象/通用/SDK接口封装SdkInterface.md#setnotifymsg)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerGameType](../预设对象/通用/SDK接口封装SdkInterface.md#getplayergametype)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.HasEntity](../预设对象/通用/SDK接口封装SdkInterface.md#hasentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsEntityAlive](../预设对象/通用/SDK接口封装SdkInterface.md#isentityalive)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateGravityComponent](../预设对象/通用/SDK接口封装SdkInterface.md#creategravitycomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityGravity](../预设对象/通用/SDK接口封装SdkInterface.md#getentitygravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityGravity](../预设对象/通用/SDK接口封装SdkInterface.md#setentitygravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateHurtComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createhurtcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetHurtByEntity](../预设对象/通用/SDK接口封装SdkInterface.md#sethurtbyentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetHurtByEntityNew](../预设对象/通用/SDK接口封装SdkInterface.md#sethurtbyentitynew)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityImmuneDamage](../预设对象/通用/SDK接口封装SdkInterface.md#setentityimmunedamage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateItemBannedComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createitembannedcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddBannedItem](../预设对象/通用/SDK接口封装SdkInterface.md#addbanneditem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBannedItemList](../预设对象/通用/SDK接口封装SdkInterface.md#getbanneditemlist)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RemoveBannedItem](../预设对象/通用/SDK接口封装SdkInterface.md#removebanneditem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ClearBannedItems](../预设对象/通用/SDK接口封装SdkInterface.md#clearbanneditems)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateItemComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createitemcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetItemBasicInfo](../预设对象/通用/SDK接口封装SdkInterface.md#getitembasicinfo)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ClearPlayerOffHand](../预设对象/通用/SDK接口封装SdkInterface.md#clearplayeroffhand)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerItem](../预设对象/通用/SDK接口封装SdkInterface.md#getplayeritem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ChangePlayerItemTipsAndExtraId](../预设对象/通用/SDK接口封装SdkInterface.md#changeplayeritemtipsandextraid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddEnchantToInvItem](../预设对象/通用/SDK接口封装SdkInterface.md#addenchanttoinvitem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetInvItemEnchantData](../预设对象/通用/SDK接口封装SdkInterface.md#getinvitemenchantdata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetOffhandItem](../预设对象/通用/SDK接口封装SdkInterface.md#getoffhanditem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetInvItemNum](../预设对象/通用/SDK接口封装SdkInterface.md#setinvitemnum)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnItemToLevel](../预设对象/通用/SDK接口封装SdkInterface.md#spawnitemtolevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnItemToPlayerInv](../预设对象/通用/SDK接口封装SdkInterface.md#spawnitemtoplayerinv)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnItemToPlayerCarried](../预设对象/通用/SDK接口封装SdkInterface.md#spawnitemtoplayercarried)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetCarriedItem](../预设对象/通用/SDK接口封装SdkInterface.md#getcarrieditem)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetSlotId](../预设对象/通用/SDK接口封装SdkInterface.md#getslotid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetItemFormattedHoverText](../预设对象/通用/SDK接口封装SdkInterface.md#getitemformattedhovertext)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetItemHoverName](../预设对象/通用/SDK接口封装SdkInterface.md#getitemhovername)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetItemEffectName](../预设对象/通用/SDK接口封装SdkInterface.md#getitemeffectname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetUserDataInEvent](../预设对象/通用/SDK接口封装SdkInterface.md#getuserdatainevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ChangeItemTexture](../预设对象/通用/SDK接口封装SdkInterface.md#changeitemtexture)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateLvComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createlvcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerLevel](../预设对象/通用/SDK接口封装SdkInterface.md#getplayerlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddPlayerLevel](../预设对象/通用/SDK接口封装SdkInterface.md#addplayerlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateMobSpawnComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createmobspawncomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SpawnCustomModule](../预设对象/通用/SDK接口封装SdkInterface.md#spawncustommodule)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateModAttrComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createmodattrcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityModAttr](../预设对象/通用/SDK接口封装SdkInterface.md#setentitymodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityModAttr](../预设对象/通用/SDK接口封装SdkInterface.md#getentitymodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RegisterEntityModAttrUpdateFunc](../预设对象/通用/SDK接口封装SdkInterface.md#registerentitymodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.UnRegisterEntityModAttrUpdateFunc](../预设对象/通用/SDK接口封装SdkInterface.md#unregisterentitymodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateModelComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createmodelcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityOpacity](../预设对象/通用/SDK接口封装SdkInterface.md#setentityopacity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.PlayEntityAnim](../预设对象/通用/SDK接口封装SdkInterface.md#playentityanim)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetModelId](../预设对象/通用/SDK接口封装SdkInterface.md#getmodelid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityModel](../预设对象/通用/SDK接口封装SdkInterface.md#setentitymodel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ResetEntityModel](../预设对象/通用/SDK接口封装SdkInterface.md#resetentitymodel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.BindModelToEntity](../预设对象/通用/SDK接口封装SdkInterface.md#bindmodeltoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.UnBindModelToEntity](../预设对象/通用/SDK接口封装SdkInterface.md#unbindmodeltoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateMoveToComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createmovetocomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityMoveSetting](../预设对象/通用/SDK接口封装SdkInterface.md#setentitymovesetting)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateMsgComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createmsgcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SendMsg](../预设对象/通用/SDK接口封装SdkInterface.md#sendmsg)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SendMsgToPlayer](../预设对象/通用/SDK接口封装SdkInterface.md#sendmsgtoplayer)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.NotifyOneMessage](../预设对象/通用/SDK接口封装SdkInterface.md#notifyonemessage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateNameComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createnamecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityName](../预设对象/通用/SDK接口封装SdkInterface.md#getentityname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityName](../预设对象/通用/SDK接口封装SdkInterface.md#setentityname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerPrefixAndSuffixName](../预设对象/通用/SDK接口封装SdkInterface.md#setplayerprefixandsuffixname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityShowName](../预设对象/通用/SDK接口封装SdkInterface.md#setentityshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityAlwaysShowName](../预设对象/通用/SDK接口封装SdkInterface.md#setentityalwaysshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePersistenceComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createpersistencecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityPersistence](../预设对象/通用/SDK接口封装SdkInterface.md#setentitypersistence)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePetComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createpetcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.DisablePet](../预设对象/通用/SDK接口封装SdkInterface.md#disablepet)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.EnablePet](../预设对象/通用/SDK接口封装SdkInterface.md#enablepet)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePlayerComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createplayercomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.IsPlayerSneaking](../预设对象/零件/零件PartBase.md#isplayersneaking)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerHunger](../预设对象/零件/零件PartBase.md#getplayerhunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerHunger](../预设对象/零件/零件PartBase.md#setplayerhunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePortalComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createportalcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePosComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createposcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityPos](../预设对象/通用/SDK接口封装SdkInterface.md#getentitypos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityFootPos](../预设对象/通用/SDK接口封装SdkInterface.md#getentityfootpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityPos](../预设对象/通用/SDK接口封装SdkInterface.md#setentitypos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityFootPos](../预设对象/通用/SDK接口封装SdkInterface.md#setentityfootpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateProjectileComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createprojectilecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateProjectileEntity](../预设对象/通用/SDK接口封装SdkInterface.md#createprojectileentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateRecipeComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createrecipecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetRecipeResult](../预设对象/通用/SDK接口封装SdkInterface.md#getreciperesult)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetRecipesByResult](../预设对象/通用/SDK接口封装SdkInterface.md#getrecipesbyresult)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetRecipesByInput](../预设对象/通用/SDK接口封装SdkInterface.md#getrecipesbyinput)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateRedStoneComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createredstonecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateRideComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createridecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateRotComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createrotcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityRot](../预设对象/通用/SDK接口封装SdkInterface.md#getentityrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityRot](../预设对象/通用/SDK接口封装SdkInterface.md#setentityrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetEntityLookAtPos](../预设对象/通用/SDK接口封装SdkInterface.md#setentitylookatpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetBodyRot](../预设对象/通用/SDK接口封装SdkInterface.md#getbodyrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.LockLocalPlayerRot](../预设对象/通用/SDK接口封装SdkInterface.md#locklocalplayerrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerLookAtPos](../预设对象/通用/SDK接口封装SdkInterface.md#setplayerlookatpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateScaleComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createscalecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateTameComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createtamecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateTimeComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createtimecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetTime](../预设对象/通用/SDK接口封装SdkInterface.md#gettime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateWeatherComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createweathercomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorCollidableComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactorcollidablecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateActorRenderComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createactorrendercomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateCustomAudioComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcustomaudiocomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateBrightnessComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createbrightnesscomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateCameraComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createcameracomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.PickFacing](../预设对象/通用/SDK接口封装SdkInterface.md#pickfacing)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFogComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createfogcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFrameAniControlComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createframeanicontrolcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniLoop](../预设对象/通用/SDK接口封装SdkInterface.md#setframeaniloop)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniFaceCamera](../预设对象/通用/SDK接口封装SdkInterface.md#setframeanifacecamera)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniDeepTest](../预设对象/通用/SDK接口封装SdkInterface.md#setframeanideeptest)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFrameAniEntityBindComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createframeanientitybindcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFrameAniSkeletonBindComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createframeaniskeletonbindcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateFrameAniTransComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createframeanitranscomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniPos](../预设对象/通用/SDK接口封装SdkInterface.md#setframeanipos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniRot](../预设对象/通用/SDK接口封装SdkInterface.md#setframeanirot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetFrameAniScale](../预设对象/通用/SDK接口封装SdkInterface.md#setframeaniscale)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateHealthComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createhealthcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ShowEntityHealth](../预设对象/通用/SDK接口封装SdkInterface.md#showentityhealth)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateOperationComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createoperationcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetCanAll](../预设对象/通用/SDK接口封装SdkInterface.md#setcanall)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateDeviceComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createdevicecomponent)，创建device组件<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateParticleControlComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createparticlecontrolcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateParticleEntityBindComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createparticleentitybindcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateParticleSkeletonBindComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createparticleskeletonbindcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateParticleTransComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createparticletranscomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetParticlePos](../预设对象/通用/SDK接口封装SdkInterface.md#setparticlepos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetParticleRot](../预设对象/通用/SDK接口封装SdkInterface.md#setparticlerot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePlayerViewComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createplayerviewcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetPlayerPerspective](../预设对象/通用/SDK接口封装SdkInterface.md#getplayerperspective)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SetPlayerPerspective](../预设对象/通用/SDK接口封装SdkInterface.md#setplayerperspective)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.LockPlayerPerspective](../预设对象/通用/SDK接口封装SdkInterface.md#lockplayerperspective)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateQueryVariableComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createqueryvariablecomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateSkyRenderComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createskyrendercomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateTextBoardComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createtextboardcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateTextNotifyClientComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createtextnotifyclientcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateConfigClientComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createconfigclientcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreateVirtualWorldComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createvirtualworldcomponent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePlayerAnimComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createplayeranimcomponent)，组件工厂化<!--by xgb-->



## 1.23.2

# 1.23.2

* 注：该版本功能仅在modpc开发包生效，移动端生效请期待1.24大版本更新。

- 新增

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetServerSystem](../预设对象/通用/SDK接口封装SdkInterface.md#getserversystem)，返回当前对象可使用的服务端system<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetClientSystem](../预设对象/通用/SDK接口封装SdkInterface.md#getclientsystem)，返回当前对象可使用的客户端system<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetSystem](../预设对象/通用/SDK接口封装SdkInterface.md#getsystem)，返回当前对象可使用的system<!--by xgb-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset](../预设对象/预设/界面预设UIPreset.md#__init__)，界面预设<!--by panlei01-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset.SetUiActive](../预设对象/预设/界面预设UIPreset.md#setuiactive)，界面预设<!--by panlei01-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset.GetUiActive](../预设对象/预设/界面预设UIPreset.md#getuiactive)，界面预设<!--by panlei01-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset.SetUiVisible](../预设对象/预设/界面预设UIPreset.md#setuivisible)，界面预设<!--by panlei01-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset.GetUiVisible](../预设对象/预设/界面预设UIPreset.md#getuivisible)，界面预设<!--by panlei01-->

1. 新增[Preset.Model.UI.UIPreset.UIPreset.GetScreenNode](../预设对象/预设/界面预设UIPreset.md#getscreennode)，界面预设<!--by panlei01-->



## 1.23.3

# 1.23.3

- 注：该版本功能仅在modpc开发包生效，移动端生效请期待1.24大版本更新。
- 新增

1. 新增[Preset.Model.PartBase.PartBase.LogDebug](../预设对象/零件/零件PartBase.md#logdebug)，打印调试日志，仅PC开发包有效<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.LogInfo](../预设对象/零件/零件PartBase.md#loginfo)，打印消息日志<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.LogError](../预设对象/零件/零件PartBase.md#logerror)，打印错误日志<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.ListenForEngineEvent](../预设对象/零件/零件PartBase.md#listenforengineevent)，监听指定的引擎事件<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.UnListenForEngineEvent](../预设对象/零件/零件PartBase.md#unlistenforengineevent)，反监听指定的引擎事件<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetApi](../预设对象/零件/零件PartBase.md#getapi)，返回当前对象可使用的SDK API模块<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#getextradata)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.SaveExtraData](../预设对象/通用/SDK接口封装SdkInterface.md#saveextradata)，组件工厂化<!--by xgb-->



## 1.23.4

# 1.23.4

- 注：该版本功能仅在modpc开发包生效，移动端生效请期待1.25大版本更新。
- 新增

1. 新增[Preset.Model.Effect.EffectObject.EffectObject](../预设对象/预设/特效对象EffectObject.md#__init__)，特效对象<!--by xgb-->

1. 新增[Preset.Model.Effect.EffectObject.EffectObject.Play](../预设对象/预设/特效对象EffectObject.md#play)，播放特效<!--by xgb-->

1. 新增[Preset.Model.Effect.EffectObject.EffectObject.Stop](../预设对象/预设/特效对象EffectObject.md#stop)，停止播放特效<!--by xgb-->

1. 新增[Preset.Model.Effect.EffectObject.EffectObject.BindToEntity](../预设对象/预设/特效对象EffectObject.md#bindtoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Effect.EffectObject.EffectObject.BindToSkeleton](../预设对象/预设/特效对象EffectObject.md#bindtoskeleton)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject](../预设对象/预设/玩家对象PlayerObject.md#__init__)，玩家对象<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetPlayerId](../预设对象/预设/玩家对象PlayerObject.md#getplayerid)，获取玩家预设的玩家ID<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.IsLocalPlayer](../预设对象/预设/玩家对象PlayerObject.md#islocalplayer)，判断当前玩家对象是否本地玩家，服务端为False<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.IsSneaking](../预设对象/预设/玩家对象PlayerObject.md#issneaking)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetHunger](../预设对象/预设/玩家对象PlayerObject.md#gethunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetHunger](../预设对象/预设/玩家对象PlayerObject.md#sethunger)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetMotion](../预设对象/预设/玩家对象PlayerObject.md#setmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetMotion](../预设对象/预设/玩家对象PlayerObject.md#getmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetStepHeight](../预设对象/预设/玩家对象PlayerObject.md#setstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetStepHeight](../预设对象/预设/玩家对象PlayerObject.md#getstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.ResetStepHeight](../预设对象/预设/玩家对象PlayerObject.md#resetstepheight)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetExp](../预设对象/预设/玩家对象PlayerObject.md#getexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddExp](../预设对象/预设/玩家对象PlayerObject.md#addexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetTotalExp](../预设对象/预设/玩家对象PlayerObject.md#gettotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetTotalExp](../预设对象/预设/玩家对象PlayerObject.md#settotalexp)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.IsFlying](../预设对象/预设/玩家对象PlayerObject.md#isflying)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.ChangeFlyState](../预设对象/预设/玩家对象PlayerObject.md#changeflystate)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.GetLevel](../预设对象/预设/玩家对象PlayerObject.md#getlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddLevel](../预设对象/预设/玩家对象PlayerObject.md#addlevel)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetPrefixAndSuffixName](../预设对象/预设/玩家对象PlayerObject.md#setprefixandsuffixname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetPlayerObject](../预设对象/零件/零件PartBase.md#getplayerobject)，获取玩家对象<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetEntityObject](../预设对象/零件/零件PartBase.md#getentityobject)，获取实体对象<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetEffectObject](../预设对象/零件/零件PartBase.md#geteffectobject)，获取特效对象<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.CreateEffectPreset](../预设对象/零件/零件PartBase.md#createeffectpreset)，创建特效对象<!--by xgb-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildPresetsByName](../预设对象/预设/预设基类PresetBase.md#getchildpresetsbyname)，增加递归查找参数<!--by xgb-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildObjectByTypeName](../预设对象/预设/预设基类PresetBase.md#getchildobjectbytypename)，获取指定类型和名称的第一个游戏对象<!--by xgb-->

1. 新增[Preset.Model.PresetBase.PresetBase.GetChildObjectsByTypeName](../预设对象/预设/预设基类PresetBase.md#getchildobjectsbytypename)，获取指定类型和名称的第一个游戏对象<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.GetEntityId](../预设对象/通用/SDK接口封装SdkInterface.md#getentityid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ToPlayerPreset](../预设对象/通用/SDK接口封装SdkInterface.md#toplayerpreset)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ToEntityPreset](../预设对象/通用/SDK接口封装SdkInterface.md#toentitypreset)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ToEffectPreset](../预设对象/通用/SDK接口封装SdkInterface.md#toeffectpreset)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ToBlockPreset](../预设对象/通用/SDK接口封装SdkInterface.md#toblockpreset)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.ToUIPreset](../预设对象/通用/SDK接口封装SdkInterface.md#touipreset)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.DestroyEntity](../预设对象/通用/SDK接口封装SdkInterface.md#destroyentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.BindFrameAniToEntity](../预设对象/通用/SDK接口封装SdkInterface.md#bindframeanitoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.BindFrameAniToSkeleton](../预设对象/通用/SDK接口封装SdkInterface.md#bindframeanitoskeleton)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.BindParticleToEntity](../预设对象/通用/SDK接口封装SdkInterface.md#bindparticletoentity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.BindParticleToSkeleton](../预设对象/通用/SDK接口封装SdkInterface.md#bindparticletoskeleton)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject](../预设对象/预设/实体对象EntityObject.md#__init__)，实体对象<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetEngineTypeStr](../预设对象/预设/实体对象EntityObject.md#getenginetypestr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetEngineType](../预设对象/预设/实体对象EntityObject.md#getenginetype)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetModelId](../预设对象/预设/实体对象EntityObject.md#getmodelid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.PlayAnim](../预设对象/预设/实体对象EntityObject.md#playanim)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetOpacity](../预设对象/预设/实体对象EntityObject.md#setopacity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetHealth](../预设对象/预设/实体对象EntityObject.md#gethealth)，获取实体预设的生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetHealth](../预设对象/预设/实体对象EntityObject.md#sethealth)，设置实体预设的生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMaxHealth](../预设对象/预设/实体对象EntityObject.md#getmaxhealth)，获取实体预设的最大生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMaxHealth](../预设对象/预设/实体对象EntityObject.md#setmaxhealth)，设置实体预设的最大生命值<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetSpeed](../预设对象/预设/实体对象EntityObject.md#getspeed)，获取实体预设的速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetSpeed](../预设对象/预设/实体对象EntityObject.md#setspeed)，设置实体预设的速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMaxSpeed](../预设对象/预设/实体对象EntityObject.md#getmaxspeed)，获取实体预设的最大速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMaxSpeed](../预设对象/预设/实体对象EntityObject.md#setmaxspeed)，设置实体预设的最大速度<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetDamage](../预设对象/预设/实体对象EntityObject.md#getdamage)，获取实体预设的伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetDamage](../预设对象/预设/实体对象EntityObject.md#setdamage)，设置实体预设的伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMaxDamage](../预设对象/预设/实体对象EntityObject.md#getmaxdamage)，获取实体预设的最大伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMaxDamage](../预设对象/预设/实体对象EntityObject.md#setmaxdamage)，设置实体预设的最大伤害<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.ShowHealth](../预设对象/预设/实体对象EntityObject.md#showhealth)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetAttackTarget](../预设对象/预设/实体对象EntityObject.md#setattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.ResetAttackTarget](../预设对象/预设/实体对象EntityObject.md#resetattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetAttackTarget](../预设对象/预设/实体对象EntityObject.md#getattacktarget)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetKnockback](../预设对象/预设/实体对象EntityObject.md#setknockback)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetOwner](../预设对象/预设/实体对象EntityObject.md#setowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetOwner](../预设对象/预设/实体对象EntityObject.md#getowner)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.IsOnFire](../预设对象/预设/实体对象EntityObject.md#isonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetOnFire](../预设对象/预设/实体对象EntityObject.md#setonfire)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetAttrValue](../预设对象/预设/实体对象EntityObject.md#getattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetAttrMaxValue](../预设对象/预设/实体对象EntityObject.md#getattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetAttrValue](../预设对象/预设/实体对象EntityObject.md#setattrvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetAttrMaxValue](../预设对象/预设/实体对象EntityObject.md#setattrmaxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.IsInLava](../预设对象/预设/实体对象EntityObject.md#isinlava)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.IsOnGround](../预设对象/预设/实体对象EntityObject.md#isonground)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetAuxValue](../预设对象/预设/实体对象EntityObject.md#getauxvalue)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetCurrentAirSupply](../预设对象/预设/实体对象EntityObject.md#getcurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMaxAirSupply](../预设对象/预设/实体对象EntityObject.md#getmaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetCurrentAirSupply](../预设对象/预设/实体对象EntityObject.md#setcurrentairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMaxAirSupply](../预设对象/预设/实体对象EntityObject.md#setmaxairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.IsConsumingAirSupply](../预设对象/预设/实体对象EntityObject.md#isconsumingairsupply)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetRecoverTotalAirSupplyTime](../预设对象/预设/实体对象EntityObject.md#setrecovertotalairsupplytime)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetSourceId](../预设对象/预设/实体对象EntityObject.md#getsourceid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetCollisionBoxSize](../预设对象/预设/实体对象EntityObject.md#setcollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetCollisionBoxSize](../预设对象/预设/实体对象EntityObject.md#getcollisionboxsize)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetBlockControlAi](../预设对象/预设/实体对象EntityObject.md#setblockcontrolai)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetDimensionId](../预设对象/预设/实体对象EntityObject.md#getdimensionid)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.ChangeDimension](../预设对象/预设/实体对象EntityObject.md#changedimension)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.RemoveEffect](../预设对象/预设/实体对象EntityObject.md#removeeffect)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddEffect](../预设对象/预设/实体对象EntityObject.md#addeffect)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetEffects](../预设对象/预设/实体对象EntityObject.md#geteffects)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.TriggerCustomEvent](../预设对象/预设/实体对象EntityObject.md#triggercustomevent)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.IsAlive](../预设对象/预设/实体对象EntityObject.md#isalive)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetGravity](../预设对象/预设/实体对象EntityObject.md#getgravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetGravity](../预设对象/预设/实体对象EntityObject.md#setgravity)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetHurt](../预设对象/预设/实体对象EntityObject.md#sethurt)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetImmuneDamage](../预设对象/预设/实体对象EntityObject.md#setimmunedamage)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetModAttr](../预设对象/预设/实体对象EntityObject.md#setmodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetModAttr](../预设对象/预设/实体对象EntityObject.md#getmodattr)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.RegisterModAttrUpdateFunc](../预设对象/预设/实体对象EntityObject.md#registermodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.UnRegisterModAttrUpdateFunc](../预设对象/预设/实体对象EntityObject.md#unregistermodattrupdatefunc)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetName](../预设对象/预设/实体对象EntityObject.md#getname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetName](../预设对象/预设/实体对象EntityObject.md#setname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetShowName](../预设对象/预设/实体对象EntityObject.md#setshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetAlwaysShowName](../预设对象/预设/实体对象EntityObject.md#setalwaysshowname)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetPersistence](../预设对象/预设/实体对象EntityObject.md#setpersistence)，组件工厂化<!--by xgb-->

1. 新增[Preset.Controller.PresetApi.GetGameObjectByTypeName](../预设管理/PresetApi.md#getgameobjectbytypename)，获取指定类型和名称的第一个游戏对象<!--by xgb-->

1. 新增[Preset.Controller.PresetApi.GetGameObjectsByTypeName](../预设管理/PresetApi.md#getgameobjectsbytypename)，获取指定类型和名称的所有游戏对象<!--by xgb-->

1. 新增[Preset.Controller.PresetApi.GetPartApi](../预设管理/PresetApi.md#getpartapi)，获取零件API<!--by xgb-->



## 1.24.0

# 1.24.0

- 注：该版本功能仅在modpc开发包生效，移动端生效请期待1.25大版本更新。
- 新增

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.EnableKeepInventory](../预设对象/预设/玩家对象PlayerObject.md#enablekeepinventory)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.GetLoadedPlayers](../预设对象/零件/零件PartBase.md#getloadedplayers)，获取服务器所有玩家的ID列表<!--by xgb-->

1. 新增[Preset.Model.PartBase.PartBase.BroadcastPresetSystemEvent](../预设对象/零件/零件PartBase.md#broadcastpresetsystemevent)，广播给预设系统<!--by zqh-->

1. 新增[Preset.Model.PartBase.PartBase.ListenPresetSystemEvent](../预设对象/零件/零件PartBase.md#listenpresetsystemevent)，监听来自预设系统的事件<!--by zqh-->

1. 新增[Preset.Model.PartBase.PartBase.UnListenPresetSystemEvent](../预设对象/零件/零件PartBase.md#unlistenpresetsystemevent)，反监听来自预设系统的事件<!--by zqh-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.EnablePlayerKeepInventory](../预设对象/通用/SDK接口封装SdkInterface.md#enableplayerkeepinventory)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetPos](../预设对象/预设/实体对象EntityObject.md#getpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetFootPos](../预设对象/预设/实体对象EntityObject.md#getfootpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetPos](../预设对象/预设/实体对象EntityObject.md#setpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetFootPos](../预设对象/预设/实体对象EntityObject.md#setfootpos)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetRot](../预设对象/预设/实体对象EntityObject.md#getrot)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetRot](../预设对象/预设/实体对象EntityObject.md#setrot)，组件工厂化<!--by xgb-->



## 1.24.1

# 1.24.1

- 新增

1. 新增[Preset.Model.TransformObject.TransformObject.GetId](../预设对象/通用/变换对象TransformObject.md#getid)，获取当前预设的ID<!--by czk-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.AddBlockProtectField](../预设对象/通用/SDK接口封装SdkInterface.md#addblockprotectfield)，设置一个方块无法被玩家/实体破坏的区域<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.RemoveBlockProtectField](../预设对象/通用/SDK接口封装SdkInterface.md#removeblockprotectfield)，取消一个方块无法被玩家/实体破坏的区域<!--by xgb-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CleanBlockProtectField](../预设对象/通用/SDK接口封装SdkInterface.md#cleanblockprotectfield)，取消全部已设置的方块无法被玩家/实体破坏的区域<!--by xgb-->

1. 新增[Preset.Parts.TriggerPart.TriggerPart](../预设对象/零件/触发器零件TriggerPart.md#__init__)，触发器零件<!--by xgb-->

1. 新增[Preset.Parts.TriggerPart.TriggerPart.GetEntitiesInTrigger](../预设对象/零件/触发器零件TriggerPart.md#getentitiesintrigger)，获取当前在触发器区域的实体列表<!--by xgb-->

1. 新增[Preset.Parts.NavPointsPart.NavPointsPart](../预设对象/零件/导航路径零件NavPointsPart.md#__init__)，导航路径零件<!--by panlei-->

1. 新增[Preset.Parts.EntityBasePart.EntityBasePart](../预设对象/零件/实体零件EntityBasePart.md#__init__)，实体零件<!--by xgb-->

1. 新增[Preset.Parts.EntityBasePart.EntityBasePart.CreateVirtualEntity](../预设对象/零件/实体零件EntityBasePart.md#createvirtualentity)，手动创建关联实体<!--by xgb-->

1. 新增[Preset.Parts.EntityBasePart.EntityBasePart.DestroyVirtualEntity](../预设对象/零件/实体零件EntityBasePart.md#destroyvirtualentity)，移除已创建的关联实体<!--by xgb-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart](../预设对象/零件/相机轨迹CameraTrackPart.md#__init__)，相机轨迹零件<!--by panlei-->

1. 新增[Preset.Parts.PortalPart.PortalPart](../预设对象/零件/传送门零件PortalPart.md#__init__)，传送门零件<!--by xgb-->

1. 新增[Preset.Parts.PlayerBasicPart.PlayerBasicPart](../预设对象/零件/玩家基础属性零件PlayerBasicPart.md#__init__)，玩家基础属性零件<!--by xgb-->

1. 新增[Preset.Parts.WorldPart.WorldPart](../预设对象/零件/世界属性零件WorldPart.md#__init__)，世界属性零件<!--by xgb-->



## 1.25.0

# 1.25.0

- 新增

1. 新增[Preset.Model.PresetBase.PresetBase.SetBlockProtect](../预设对象/预设/预设基类PresetBase.md#setblockprotect)，设置预设内的所有素材区域的方块保护状态<!--by xgb-->

1. 新增[Preset.Model.GameObject.type.fromDict](../预设对象/通用/游戏对象GameObject.md#fromdict)，将字典根据classType字段转换为对应类型的对象，该类型必须使用@registerGenericClass装饰<!--by xgb-->

1. 新增[Preset.Parts.NavPointsPart.NavPointsPart](../预设对象/零件/导航路径零件NavPointsPart.md#__init__)，导航路径零件<!--by panlei-->

1. 新增[Preset.Parts.NavPointsPart.NavPointsPart.GetNavigationPoints](../预设对象/零件/导航路径零件NavPointsPart.md#getnavigationpoints)，获得路径点的世界坐标列表<!--by panlei-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart](../预设对象/零件/相机轨迹CameraTrackPart.md#__init__)，相机轨迹零件<!--by panlei-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart.PlayFromStart](../预设对象/零件/相机轨迹CameraTrackPart.md#playfromstart)，从头开始播放相机运动轨迹<!--by panlei-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart.Pause](../预设对象/零件/相机轨迹CameraTrackPart.md#pause)，暂停播放相机轨迹<!--by panlei-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart.Continue](../预设对象/零件/相机轨迹CameraTrackPart.md#continue)，继续播放相机轨迹<!--by panlei-->

1. 新增[Preset.Parts.CameraTrackPart.CameraTrackPart.Stop](../预设对象/零件/相机轨迹CameraTrackPart.md#stop)，停止播放相机轨迹<!--by panlei-->



## 2.0.1

# 2.0.1

- 新增

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMotion](../预设对象/预设/实体对象EntityObject.md#setmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMotion](../预设对象/预设/实体对象EntityObject.md#getmotion)，组件工厂化<!--by xgb-->

1. 新增[Preset.Parts.NavPointsPart.NavPointsPart.GetNavigationRadius](../预设对象/零件/导航路径零件NavPointsPart.md#getnavigationradius)，获得路径点的随机半径列表<!--by panlei-->



## 2.0.2

# 2.0.2

- 新增

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddAnimation](../预设对象/预设/玩家对象PlayerObject.md#addanimation)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetHealthLevel](../预设对象/预设/玩家对象PlayerObject.md#sethealthlevel)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetStarveLevel](../预设对象/预设/玩家对象PlayerObject.md#setstarvelevel)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetNaturalStarve](../预设对象/预设/玩家对象PlayerObject.md#setnaturalstarve)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetStarveTick](../预设对象/预设/玩家对象PlayerObject.md#setstarvetick)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetNaturalRegen](../预设对象/预设/玩家对象PlayerObject.md#setnaturalregen)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetHealthTick](../预设对象/预设/玩家对象PlayerObject.md#sethealthtick)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetMaxExhaustionValue](../预设对象/预设/玩家对象PlayerObject.md#setmaxexhaustionvalue)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetPickUpArea](../预设对象/预设/玩家对象PlayerObject.md#setpickuparea)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetJumpable](../预设对象/预设/玩家对象PlayerObject.md#setjumpable)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetMovable](../预设对象/预设/玩家对象PlayerObject.md#setmovable)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddAnimationController](../预设对象/预设/玩家对象PlayerObject.md#addanimationcontroller)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddAnimationIntoState](../预设对象/预设/玩家对象PlayerObject.md#addanimationintostate)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddGeometry](../预设对象/预设/玩家对象PlayerObject.md#addgeometry)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddParticleEffect](../预设对象/预设/玩家对象PlayerObject.md#addparticleeffect)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddRenderController](../预设对象/预设/玩家对象PlayerObject.md#addrendercontroller)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddRenderMaterial](../预设对象/预设/玩家对象PlayerObject.md#addrendermaterial)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddSoundEffect](../预设对象/预设/玩家对象PlayerObject.md#addsoundeffect)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.AddTexture](../预设对象/预设/玩家对象PlayerObject.md#addtexture)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Player.PlayerObject.PlayerObject.SetSkin](../预设对象/预设/玩家对象PlayerObject.md#setskin)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetItem](../预设对象/预设/实体对象EntityObject.md#setitem)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetCanOtherPlayerRide](../预设对象/预设/实体对象EntityObject.md#setcanotherplayerride)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetControl](../预设对象/预设/实体对象EntityObject.md#setcontrol)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetRidePos](../预设对象/预设/实体对象EntityObject.md#setridepos)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetNotRender](../预设对象/预设/实体对象EntityObject.md#setnotrender)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetCollidable](../预设对象/预设/实体对象EntityObject.md#setcollidable)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetHealthColor](../预设对象/预设/实体对象EntityObject.md#sethealthcolor)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddAnimation](../预设对象/预设/实体对象EntityObject.md#addanimation)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddAnimationController](../预设对象/预设/实体对象EntityObject.md#addanimationcontroller)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddScriptAnimate](../预设对象/预设/实体对象EntityObject.md#addscriptanimate)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddParticleEffect](../预设对象/预设/实体对象EntityObject.md#addparticleeffect)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddRenderController](../预设对象/预设/实体对象EntityObject.md#addrendercontroller)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddRenderMaterial](../预设对象/预设/实体对象EntityObject.md#addrendermaterial)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.AddSoundEffect](../预设对象/预设/实体对象EntityObject.md#addsoundeffect)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetPushable](../预设对象/预设/实体对象EntityObject.md#setpushable)，铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetModel](../预设对象/预设/实体对象EntityObject.md#setmodel)，铺量属性接口<!--by OOP-->



## 2.0.3

# 2.0.3

- 新增

1. 新增[Preset.Model.PartBase.PartBase.CreateTextboardPreset](../预设对象/零件/零件PartBase.md#createtextboardpreset)(客户端/服务端)， 创建文字面板对象<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardPreset.TextboardPreset](../预设对象/预设/文字面板预设TextboardPreset.md#__init__)(客户端/服务端)， 文字面板预设<!--by OOP-->

1. 新增[Preset.Model.SdkInterface.SdkInterface.CreatePostProcessComponent](../预设对象/通用/SDK接口封装SdkInterface.md#createpostprocesscomponent)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetLavaSpeed](../预设对象/预设/实体对象EntityObject.md#getlavaspeed)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetLavaSpeed](../预设对象/预设/实体对象EntityObject.md#setlavaspeed)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.GetMaxLavaSpeed](../预设对象/预设/实体对象EntityObject.md#getmaxlavaspeed)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Entity.EntityObject.EntityObject.SetMaxLavaSpeed](../预设对象/预设/实体对象EntityObject.md#setmaxlavaspeed)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject](../预设对象/预设/文字面板对象TextboardObject.md#__init__)(客户端/服务端)， 文字面板对象<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetBindEntity](../预设对象/预设/文字面板对象TextboardObject.md#setbindentity)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetPos](../预设对象/预设/文字面板对象TextboardObject.md#setpos)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetRot](../预设对象/预设/文字面板对象TextboardObject.md#setrot)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetScale](../预设对象/预设/文字面板对象TextboardObject.md#setscale)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetText](../预设对象/预设/文字面板对象TextboardObject.md#settext)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetColor](../预设对象/预设/文字面板对象TextboardObject.md#setcolor)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetBackgroundColor](../预设对象/预设/文字面板对象TextboardObject.md#setbackgroundcolor)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetFaceCamera](../预设对象/预设/文字面板对象TextboardObject.md#setfacecamera)(客户端/服务端)， 铺量属性接口<!--by OOP-->

1. 新增[Preset.Model.Textboard.TextboardObject.TextboardObject.SetBoardDepthTest](../预设对象/预设/文字面板对象TextboardObject.md#setboarddepthtest)(客户端/服务端)， 铺量属性接口<!--by OOP-->



## 2.2.0

# 2.2.0

- 新增

1. 新增[Preset.Controller.PresetApi.CreateTransform](../预设管理/PresetApi.md#createtransform)(客户端/服务端)， 构造变换对象<!--by czk-->



