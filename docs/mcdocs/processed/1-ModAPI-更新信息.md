# ModAPI 更新信息

## 1.21

# 1.21

**2021.1.28：版本号（v1.21 BE1.16.10）**

- 版本重大更新
  
  1. 小地图增加如下更新：
  
     1）优化地图渲染，避免在低端机下出现明显的卡顿；
  
     2）支持自定义大小，同时可通过接口[SetSize](../接口/自定义UI/UI控件.md#setsize)动态改变大小；
  
     3）标记图标支持默认使用本地玩家的脸部显示，并可配置其大小与背景色，详见<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#minimap" rel="noopenner"> MiniMap </a></a>
  
     4）接口[AddEntityMarker](../接口/自定义UI/UI界面.md#addentitymarker)支持朝向标记；
  
     5）增加地图缩小放大功能，见接口[ZoomIn](../接口/自定义UI/UI界面.md#zoomin)和[ZoomOut](../接口/自定义UI/UI界面.md#zoomout)；
  
     6）静态标记默认保存到本地；
  
     7）小地图背景可在ui json中进行定制；
  
     8）更新了小地图示例<a href="../../../mcguide/20-玩法开发/13-模组SDK编程/60-Demo示例.html#custommapmod" rel="noopenner"> CustomMapMod </a></a>
  
  2. 若干方块相关事件中的添加维度信息
  
  3. 物品贴图支持使用<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/6-自定义物品贴图使用序列帧动画.html" rel="noopenner"> 序列帧动画 </a></a>

  4. 支持动态修改物品、盔甲和方块贴图，详见[ChangeItemTexture](../接口/物品.md#changeitemtexture)、[ChangeArmorTextures](../接口/物品.md#changearmortextures)、[ChangeBlockTextures](../接口/方块/渲染.md#changeblocktextures)

  5. 支持UI控件对象化开发，用法详见<a href="../../../mcguide/18-界面与交互/50-UI控件对象.html" rel="noopenner"> UI控件对象 </a></a>

     1）实现控件基类BaseUIControl，包含控件的基础功能接口，详见[BaseUIControl](../接口/自定义UI/UI控件.md#baseuicontrol)；
  
     2）实现按钮控件类，继承自BaseUIControl，除基础功能接口外包含按钮相关功能接口，详见[ButtonUIControl](../接口/自定义UI/UI控件.md#buttonuicontrol)；
  
     3）实现网格控件类，继承自BaseUIControl，除基础功能接口外包含网格相关功能接口，详见[GridUIControl](../接口/自定义UI/UI控件.md#griduicontrol)；
  
     4）实现图片控件类，继承自BaseUIControl，除基础功能接口外包含图片相关功能接口，详见[ImageUIControl](../接口/自定义UI/UI控件.md#imageuicontrol)；
  
     5）实现文本控件类，继承自BaseUIControl，除基础功能接口外包含文本相关功能接口，详见[LabelUIControl](../接口/自定义UI/UI控件.md#labeluicontrol)；
  
     6）实现纸娃娃控件类，继承自BaseUIControl，除基础功能接口外包含纸娃娃相关功能接口，详见[NeteasePaperDollUIControl](../接口/自定义UI/UI控件.md#neteasepaperdolluicontrol)；
  
     7）实现进度条控件类，继承自BaseUIControl，除基础功能接口外包含进度条相关功能接口，详见[ProgressBarUIControl](../接口/自定义UI/UI控件.md#progressbaruicontrol)；
  
     8）实现滚动列表控件类，继承自BaseUIControl，除基础功能接口外包含滚动列表相关功能接口，详见[ScrollViewUIControl](../接口/自定义UI/UI控件.md#scrollviewuicontrol)
  
     9）实现开关控件类，继承自BaseUIControl，除基础功能接口外包含开关相关功能接口，详见[SwitchToggleUIControl](../接口/自定义UI/UI控件.md#switchtoggleuicontrol)
  
     10）实现文本输入框控件类，继承自BaseUIControl，除基础功能接口外包含文本输入框相关功能接口，详见[TextEditBoxUIControl](../接口/自定义UI/UI控件.md#texteditboxuicontrol)

- 新增

1. 新增[IsInApollo](../接口/通用/本地设备.md#isinapollo)，返回当前游戏Mod是否运行在Apollo网络服<!--by xltang-->

1. 新增[HideHorseHealthGui](../接口/原生UI.md#hidehorsehealthgui)，隐藏hud界面的坐骑的血量显示<!--by sutao-->

1. 新增[SetStepHeight](../接口/实体/行为.md#setstepheight)，设置玩家前进非跳跃状态下能上的最大台阶高度<!--by sutao-->

1. 新增[GetStepHeight](../接口/实体/行为.md#getstepheight)，返回玩家前进非跳跃状态下能上的最大台阶高度<!--by sutao-->

1. 新增[ResetStepHeight](../接口/实体/行为.md#resetstepheight)，恢复引擎默认玩家前进非跳跃状态下能上的最大台阶高度，即恢复为原来的0.5625<!--by sutao-->

1. 新增[MayPlace](../接口/世界/地图.md#mayplace)，判断方块是否可以放置<!--by gzhuabo-->

1. 新增[ListenOnBlockRemoveEvent](../事件/方块.md#listenonblockremoveevent)，是否监听方块[BlockRemoveServerEvent](../事件/方块.html#blockremoveserverevent)事件<!--by gzhuabo-->

1. 新增[GetOrbExperience](../接口/实体/经验球.md#getorbexperience)，获取经验球的经验<!--by sutao-->

1. 新增[GetPlayerTotalExp](../接口/玩家/属性.md#getplayertotalexp)，获取玩家的总经验值<!--by sutao-->

1. 新增[SetPlayerTotalExp](../接口/玩家/属性.md#setplayertotalexp)，设置玩家的总经验值<!--by sutao-->

1. 新增[GetSpawnPosition](../接口/世界/地图.md#getspawnposition)，获取世界出生点坐标<!--by czh-->

1. 新增[Hurt](../接口/实体/行为.md#hurt)，设置实体伤害<!--by gzhuabo-->

1. 新增[GetBannedItemList](../接口/世界/游戏规则.md#getbanneditemlist)，新增获取禁用物品列表<!--by jishaobin-->

1. 新增[SpawnItemToContainer](../接口/方块/容器.md#spawnitemtocontainer)，新增生成物品到容器<!--by jishaobin-->

1. 新增[SpawnItemToEnderChest](../接口/方块/容器.md#spawnitemtoenderchest)，新增生成物品到末影箱<!--by jishaobin-->

1. 新增[GetContainerSize](../接口/方块/容器.md#getcontainersize)，新增获取容器容量大小<!--by jishaobin-->

1. 新增[MayPlaceOn](../接口/世界/地图.md#mayplaceon)，判断物品是否可以放到指定的位置上<!--by gzhuabo-->

1. 新增[GetItemDurability](../接口/物品.md#getitemdurability)，获取指定槽位的物品耐久<!--by gzhuabo-->

1. 新增[SetItemDurability](../接口/物品.md#setitemdurability)，设置物品的耐久值<!--by gzhuabo-->

1. 新增[SetMaxStackSize](../接口/物品.md#setmaxstacksize)，设置物品的最大堆叠数量（存档）<!--by gzhuabo-->

1. 新增[SetAttackDamage](../接口/物品.md#setattackdamage)，设置物品的攻击伤害值<!--by gzhuabo-->

1. 新增[SetItemTierLevel](../接口/物品.md#setitemtierlevel)，设置工具类物品的挖掘等级<!--by gzhuabo-->

1. 新增[SetItemTierSpeed](../接口/物品.md#setitemtierspeed)，设置工具类物品的挖掘速度<!--by gzhuabo-->

1. 新增[ShowCommonHurtColor](../接口/模型.md#showcommonhurtcolor)，设置挂接骨骼模型的实体是否显示通用的受伤变红效果<!--by gzhuabo-->

1. 新增[SetPlayerRespawnPos](../接口/玩家/行为.md#setplayerrespawnpos)，设置玩家复活的位置，当前玩家的复活点仅支持主世界<!--by xltang-->

1. 新增[ChangeArmorTextures](../接口/物品.md#changearmortextures)，修改盔甲贴图<!--by sutao-->

1. 新增[ChangeBlockTextures](../接口/方块/渲染.md#changeblocktextures)，替换方块的贴图，使用该贴图的所有方块朝向或者使用该贴图的其它方块也会同时被改变<!--by sutao-->

1. 新增[GetConfigData](../接口/通用/本地存储.md#getconfigdata)，获取本地配置文件中存储的数据<!--by gzhuabo-->

1. 新增[SetConfigData](../接口/通用/本地存储.md#setconfigdata)，以本地配置文件的方式存储数据<!--by gzhuabo-->

1. 新增[GetCurrentDimension](../接口/世界/地图.md#getcurrentdimension)，获取客户端当前维度<!--by czh-->

1. 新增[ChangeItemTexture](../接口/物品.md#changeitemtexture)，替换物品的贴图<!--by sutao-->

1. 新增[ShowCommonHurtColor](../接口/模型.md#showcommonhurtcolor)，设置挂接骨骼模型的实体是否显示通用的受伤变红效果<!--by gzhuabo-->

1. 新增[SetUIProfile](../接口/游戏设置.md#setuiprofile)，设置"UI 档案"模式<!--by sutao-->

1. 新增[SetToggleOption](../接口/游戏设置.md#settoggleoption)，修改开关型设置的接口<!--by sutao-->

1. 新增[GetToggleOption](../接口/游戏设置.md#gettoggleoption)，获得某个开关设置值的接口<!--by sutao-->

1. 新增[HighlightBoxSelection](../接口/游戏设置.md#highlightboxselection)，镜头移动时高亮当前视角中心所指的方块<!--by sutao-->

1. 新增[SetSelectControl](../接口/自定义UI/UI界面.md#setselectcontrol)，设置当前焦点所在的控件<!--by panlei-->

1. 新增[ZoomIn](../接口/自定义UI/UI界面.md#zoomin)，放大地图<!--by gzhuabo-->

1. 新增[ZoomOut](../接口/自定义UI/UI界面.md#zoomout)，缩小地图<!--by gzhuabo-->

1. 新增[ZoomReset](../接口/自定义UI/UI界面.md#zoomreset)，恢复地图放缩大小为默认值<!--by gzhuabo-->

1. 新增[ServerEntityTryPlaceBlockEvent](../事件/方块.md#serverentitytryplaceblockevent)，新增维度id参数，新增朝向参数<!--by czh-->

1. 新增[DestroyBlockEvent](../事件/方块.md#destroyblockevent)，新增维度id参数<!--by czh-->

1. 新增[ServerPreBlockPatternEvent](../事件/世界.md#serverpreblockpatternevent)，新增维度id参数<!--by czh-->

1. 新增[ServerBlockUseEvent](../事件/方块.md#serverblockuseevent)，新增维度id参数<!--by czh-->

1. 新增[StepOnBlockServerEvent](../事件/实体.md#steponblockserverevent)，新增维度id参数<!--by czh-->

1. 新增[MobGriefingBlockServerEvent](../事件/实体.md#mobgriefingblockserverevent)，新增维度id参数<!--by czh-->

1. 新增[ExplosionServerEvent](../事件/世界.md#explosionserverevent)，新增维度id参数<!--by czh-->

1. 新增[PlayerRespawnFinishServerEvent](../事件/玩家.md#playerrespawnfinishserverevent)，玩家复活完毕事件<!--by czh-->

1. 新增[ServerPostBlockPatternEvent](../事件/世界.md#serverpostblockpatternevent)，新增维度id参数<!--by czh-->

1. 新增[PlaceNeteaseStructureFeatureEvent](../事件/世界.md#placeneteasestructurefeatureevent)，新增维度id参数<!--by czh-->

1. 新增[OnPlayerHitBlockServerEvent](../事件/玩家.md#onplayerhitblockserverevent)，新增维度id以及auxValue参数<!--by czh-->

1. 新增[EntityPlaceBlockAfterServerEvent](../事件/方块.md#entityplaceblockafterserverevent)，新增维度id参数<!--by czh-->

1. 新增[HopperTryPullInServerEvent](../事件/方块.md#hoppertrypullinserverevent)，新增维度id参数<!--by czh-->

1. 新增[HopperTryPullOutServerEvent](../事件/方块.md#hoppertrypulloutserverevent)，新增维度id参数<!--by czh-->

1. 新增[EntityEffectDamageServerEvent](../事件/实体.md#entityeffectdamageserverevent)，生物受到状态伤害事件。<!--by gzhuabo-->

1. 新增[OnCommandOutputServerEvent](../事件/世界.md#oncommandoutputserverevent)，Command命令执行成功事件。<!--by gzhuabo-->

1. 新增[PlayerChatButtonClickClientEvent](../事件/UI.md#playerchatbuttonclickclientevent)，玩家点击聊天按钮或回车键触发呼出聊天窗口时客户端抛出的事件<!--by pl-->

1. 新增[PerspChangeClientEvent](../事件/玩家.md#perspchangeclientevent)，视角切换事件<!--by sutao-->

1. 新增[ColorCode](../枚举值/ColorCode.md)，代替GenerateColor接口<!--by czh-->

1. 新增[UiBaseLayer](../枚举值/UiBaseLayer.md)，自定义UI界面的层次宏定义<!--by xltang-->

- 调整

1. 调整[SetEntityOnFire](../接口/实体/行为.md#setentityonfire)，调整说明，可通过事件[OnFireHurtEvent](../事件/实体.html#onfirehurtevent)取消着火伤害<!--by gzhuabo-->

1. 调整[SpawnItemToArmor](../接口/玩家/背包.md#spawnitemtoarmor)，支持清除指定槽位的装备<!--by gzhuabo-->

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)，新增idAux字段，用于ui物品控件的绑定<!--by czh-->

1. 调整[SetMoveSetting](../接口/实体/行为.md#setmovesetting)，现在支持游泳，爬墙与飞行生物<!--by czh-->

1. 调整[GetRecipesByResult](../接口/世界/配方.md#getrecipesbyresult)，返回的配方中将包含输出的物品<!--by sutao-->

1. 调整[AddPlayerRenderMaterial](../接口/玩家/渲染.md#addplayerrendermaterial)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddPlayerRenderController](../接口/玩家/渲染.md#addplayerrendercontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RemovePlayerRenderController](../接口/玩家/渲染.md#removeplayerrendercontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RemovePlayerGeometry](../接口/玩家/渲染.md#removeplayergeometry)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddPlayerGeometry](../接口/玩家/渲染.md#addplayergeometry)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddPlayerTexture](../接口/玩家/渲染.md#addplayertexture)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddPlayerAnimation](../接口/玩家/渲染.md#addplayeranimation)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddPlayerAnimationController](../接口/玩家/渲染.md#addplayeranimationcontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RemovePlayerAnimationController](../接口/玩家/渲染.md#removeplayeranimationcontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RebuildPlayerRender](../接口/玩家/渲染.md#rebuildplayerrender)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddActorRenderMaterial](../接口/实体/渲染.md#addactorrendermaterial)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[AddActorRenderController](../接口/实体/渲染.md#addactorrendercontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RemoveActorRenderController](../接口/实体/渲染.md#removeactorrendercontroller)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[RebuildActorRender](../接口/实体/渲染.md#rebuildactorrender)，修复从后台切回来被重置的问题<!--by gzhuabo-->

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)，新增idAux字段，用于ui物品控件的绑定<!--by czh-->

1. 调整[SetLegacyBindRot](../接口/模型.md#setlegacybindrot)，为了适配studio，调整为骨骼模型创建时默认为False，不再需要设置。但是对于旧版特效，仍然可以设置为True来适配。<!--by czh-->

1. 调整[SetUiItem](../接口/自定义UI/UI界面.md#setuiitem)，新增支持焰火之星<!--by panlei-->

1. 调整[AddEntityMarker](../接口/自定义UI/UI界面.md#addentitymarker)，支持实体标记旋转角度<!--by gzhuabo-->

1. 调整[AddStaticMarker](../接口/自定义UI/UI界面.md#addstaticmarker)，静态标记会保存在本地<!--by gzhuabo-->

1. 调整[RemoveStaticMarker](../接口/自定义UI/UI界面.md#removestaticmarker)，删除静态标记会删除本地数据<!--by gzhuabo-->

1. 调整[ServerPlayerTryDestroyBlockEvent](../事件/方块.md#serverplayertrydestroyblockevent)，参数新增方块被敲击的面向id，维度id以及是否生成掉落物<!--by jishaobin-->

1. 调整[ChestBlockTryPairWithServerEvent](../事件/方块.md#chestblocktrypairwithserverevent)，新增维度id参数<!--by czh-->

1. 调整[OnFireHurtEvent](../事件/实体.md#onfirehurtevent)，新增着火时间参数fireTime和取消伤害参数cancel<!--by gzhuabo-->

1. 调整[ServerItemUseOnEvent](../事件/物品.md#serveritemuseonevent)，新增维度id，blockName，以及blockAuxValue参数<!--by czh-->

1. 调整[ItemUseOnAfterServerEvent](../事件/物品.md#itemuseonafterserverevent)，新增维度id，blockName，以及blockAuxValue参数<!--by czh-->

1. 调整[AddEffectServerEvent](../事件/实体.md#addeffectserverevent)，新增伤害参数damage<!--by gzhuabo-->

1. 调整[WillAddEffectServerEvent](../事件/实体.md#willaddeffectserverevent)，新增伤害参数damage<!--by gzhuabo-->

1. 调整[RefreshEffectServerEvent](../事件/实体.md#refresheffectserverevent)，新增伤害参数damage<!--by gzhuabo-->

1. 调整[BlockStrengthChangedServerEvent](../事件/方块.md#blockstrengthchangedserverevent)，增加维度参数<!--by gzhuabo-->

1. 调整[BlockRemoveServerEvent](../事件/方块.md#blockremoveserverevent)，可以动态对方块的该事件进行监听<!--by gzhuabo-->

1. 调整[StartDestroyBlockServerEvent](../事件/方块.md#startdestroyblockserverevent)，新增维度id参数<!--by czh-->

1. 调整[ClientItemUseOnEvent](../事件/物品.md#clientitemuseonevent)，新增blockName、blockAuxValue、face参数<!--by czh-->

1. 调整[PlayerTryDestroyBlockClientEvent](../事件/方块.md#playertrydestroyblockclientevent)，参数新增方块被敲击的面向id<!--by jishaobin-->

1. 调整[OnPlayerHitBlockClientEvent](../事件/玩家.md#onplayerhitblockclientevent)，新增auxValue参数<!--by czh-->

1. 调整[OnCommandOutputClientEvent](../事件/世界.md#oncommandoutputclientevent)，分类从“玩家”改为“世界”<!--by gzhuabo-->

- 废弃（将在未来不可用）

1. 废弃GenerateColor，请使用ColorCode枚举

1. 废弃DefineEvent，监听自定义事件前不再需要DefineEvent

1. 废弃GetEntityIdentifier，请使用GetEngineTypeStr

1. 废弃GetItemEntityItemIdentifier，请使用GetDroppedItem

1. 废弃SetHurtByEntity，请使用Hurt

1. 废弃IsSneaking，请使用isSneaking

1. 废弃IsSwiming，请使用isSwimming

1. 废弃BindModelSfx，请使用CreateEngineSfx或CreateEngineSfxFromEditor创建序列帧，并使用Bind绑定骨骼模型

1. 废弃Create，请使用CreateEngineSfxFromEditor

1. 废弃SetVisible，推荐使用UI面向对象BaseUIControl.SetVisible接口

1. 废弃GetVisible，推荐使用UI面向对象BaseUIControl.GetVisible接口

1. 废弃GetText，推荐使用UI面向对象LabelUIControl.GetText接口

1. 废弃SetText，推荐使用UI面向对象LabelUIControl.SetText接口

1. 废弃GetEditText，推荐使用UI面向对象TextEditBoxUIControl.GetEditText接口

1. 废弃SetEditText，推荐使用UI面向对象TextEditBoxUIControl.SetEditText接口

1. 废弃GetTextColor，推荐使用UI面向对象LabelUIControl.GetTextColor接口

1. 废弃SetTextColor，推荐使用UI面向对象LabelUIControl.SetTextColor接口

1. 废弃SetEditTextMaxLength，推荐使用UI面向对象TextEditBoxUIControl.SetEditTextMaxLength接口

1. 废弃SetTextFontSize，推荐使用UI面向对象LabelUIControl.SetTextFontSize接口

1. 废弃SetPosition，推荐使用UI面向对象BaseUIControl.SetPosition接口

1. 废弃GetPosition，推荐使用UI面向对象BaseUIControl.GetPosition接口

1. 废弃SetAlpha，推荐使用UI面向对象BaseUIControl.SetAlpha接口

1. 废弃SetSize，推荐使用UI面向对象BaseUIControl.SetSize接口

1. 废弃GetSize，推荐使用UI面向对象BaseUIControl.GetSize接口

1. 废弃SetSprite，推荐使用UI面向对象ImageUIControl.SetSprite接口

1. 废弃SetSpriteColor，推荐使用UI面向对象ImageUIControl.SetSpriteColor接口

1. 废弃SetSpriteGray，推荐使用UI面向对象ImageUIControl.SetSpriteGray接口

1. 废弃SetSpriteUV，推荐使用UI面向对象ImageUIControl.SetSpriteUV接口

1. 废弃SetSpriteUVSize，推荐使用UI面向对象ImageUIControl.SetSpriteUVSize接口

1. 废弃SetSpriteClipRatio，推荐使用UI面向对象ImageUIControl.SetSpriteClipRatio接口

1. 废弃SetTouchEnable，推荐使用UI面向对象BaseUIControl.SetTouchEnable接口

1. 废弃AddTouchEventHandler，推荐使用UI面向对象ButtonUIControl.AddTouchEventParams接口开启按钮回调功能并通过SetButtonTouchUpCallback等接口绑定回调函数

1. 废弃RenderPaperDoll，推荐使用UI面向对象NeteasePaperDollUIControl.RenderEntity接口渲染实体或NeteasePaperDollUIControl.RenderSkeletonModel接口渲染骨骼模型

1. 废弃SetGridDimension，推荐使用UI面向对象GridUIControl.SetGridDimension接口

1. 废弃SetToggleState，推荐使用UI面向对象SwitchToggleUIControl.SetToggleState接口

1. 废弃SetScrollViewPos，推荐使用UI面向对象ScrollViewUIControl.SetScrollViewPos接口

1. 废弃GetScrollViewPos，推荐使用UI面向对象ScrollViewUIControl.GetScrollViewPos接口

1. 废弃SetScrollViewPercentValue，推荐使用UI面向对象ScrollViewUIControl.SetScrollViewPercentValue接口

1. 废弃GetNeteasePaperDollModelId，推荐使用UI面向对象NeteasePaperDollUIControl.GetModelId接口

1. 废弃ServerExplosionBlockEvent，请使用ExplosionServerEvent

1. 废弃PistonFacing，请使用Facing枚举



## 1.22

# 1.22

**2021.04.08：版本号（v1.22 BE1.16.10）**

- 重大更新

  1. 新增自定义场景，场景内支持以下元素：
     	1）摄像机
     	2）骨骼模型
     	3）序列帧与粒子特效
     	4）文字面板

     详见[虚拟世界](../接口/虚拟世界/索引.md)

  2. 常用的原版界面（例如：背包、熔炉、合成台、箱子）可挂接自定义控件，详见<a href="../../../mcguide/18-界面与交互/60-原生界面添加自定义UI使用文档.html" rel="noopenner"> 原生界面添加自定义UI使用文档 </a></a>

- 新增

1. 新增[GetNativeScreenManagerCls](../接口/自定义UI/通用.md#getnativescreenmanagercls)，获得NativeScreenManager类<!--by panlei-->

1. 新增[GetCustomUIControlProxyCls](../接口/自定义UI/通用.md#getcustomuicontrolproxycls)，获得原生界面自定义UI代理基类<!--by panlei-->

1. 新增[SetHudChatStackVisible](../接口/原生UI.md#sethudchatstackvisible)，设置HUD界面左上小聊天窗口可见性接口<!--by panlei-->

1. 新增[SetHudChatStackPosition](../接口/原生UI.md#sethudchatstackposition)，设置HUD界面左上小聊天窗口位置接口<!--by panlei-->

1. 新增[SpawnResourcesSilkTouched](../接口/世界/实体管理.md#spawnresourcessilktouched)，模拟方块精准采集掉落<!--by gzhuabo-->

1. 新增[GetDestroyTotalTime](../接口/世界/方块管理.md#getdestroytotaltime)，获取使用物品破坏方块需要的时间<!--by gzhuabo-->

1. 新增[GetOpenContainerItem](../接口/方块/容器.md#getopencontaineritem)，获取开放容器的物品<!--by jishaobin-->

1. 新增[GetRecipesByInput](../接口/世界/配方.md#getrecipesbyinput)，通过输入物品查询配方<!--by sutao-->

1. 新增[SetEntityLookAtPos](../接口/实体/属性.md#setentitylookatpos)，设置非玩家实体看向某个位置<!--by liaoyi-->

1. 新增[AddActorAnimationController](../接口/实体/渲染.md#addactoranimationcontroller)，增加生物渲染动画控制器<!--by gzhuabo-->

1. 新增[RemoveActorAnimationController](../接口/实体/渲染.md#removeactoranimationcontroller)，移除生物渲染动画控制器<!--by gzhuabo-->

1. 新增[AddPlayerParticleEffect](../接口/玩家/渲染.md#addplayerparticleeffect)，增加玩家特效资源<!--by gzhuabo-->

1. 新增[AddActorParticleEffect](../接口/实体/渲染.md#addactorparticleeffect)，增加生物特效资源<!--by gzhuabo-->

1. 新增[AddPlayerSoundEffect](../接口/玩家/渲染.md#addplayersoundeffect)，增加玩家音效资源<!--by gzhuabo-->

1. 新增[AddActorSoundEffect](../接口/实体/渲染.md#addactorsoundeffect)，增加生物音效资源<!--by gzhuabo-->

1. 新增[AddPlayerAnimationIntoState](../接口/玩家/渲染.md#addplayeranimationintostate)，在玩家的动画控制器中的状态添加动画<!--by gzhuabo-->

1. 新增[AddActorScriptAnimate](../接口/实体/渲染.md#addactorscriptanimate)，在生物的客户端实体定义（minecraft:client_entity）json中的scripts/animate节点添加动画/动画控制器<!--by gzhuabo-->

1. 新增[AddActorAnimation](../接口/实体/渲染.md#addactoranimation)，增加生物渲染动画<!--by gzhuabo-->

1. 新增[isEntityInLava](../接口/实体/属性.md#isentityinlava)，获取实体是否在岩浆中<!--by liaoyi-->

1. 新增[isEntityOnGround](../接口/实体/属性.md#isentityonground)，获取实体是否触地<!--by liaoyi-->

1. 新增[GetDestroyTotalTime](../接口/世界/方块管理.md#getdestroytotaltime)，获取使用物品破坏方块需要的时间<!--by gzhuabo-->

1. 新增[PlayTpAnimation](../接口/玩家/动画.md#playtpanimation)，第三人称视角播放玩家通用动作<!--by gzhuabo-->

1. 新增[StopAnimation](../接口/玩家/动画.md#stopanimation)，停止播放玩家通用动作<!--by gzhuabo-->

1. 新增[GetRecipesByInput](../接口/世界/配方.md#getrecipesbyinput)，通过输入物品查询配方<!--by sutao-->

1. 新增[LockLocalPlayerRot](../接口/实体/属性.md#locklocalplayerrot)，在分离摄像机时，锁定本地玩家的头部角度<!--by liaoyi-->

1. 新增[SetPlayerLookAtPos](../接口/实体/属性.md#setplayerlookatpos)，设置本地玩家看向某个位置<!--by liaoyi-->

1. 新增[VirtualWorldCreate](../接口/虚拟世界/世界.md#virtualworldcreate)，创建虚拟世界<!--by sutao-->

1. 新增[VirtualWorldDestroy](../接口/虚拟世界/世界.md#virtualworlddestroy)，销毁虚拟世界<!--by sutao-->

1. 新增[VirtualWorldToggleVisibility](../接口/虚拟世界/世界.md#virtualworldtogglevisibility)，设置虚拟世界是否显示<!--by sutao-->

1. 新增[VirtualWorldSetCollidersVisible](../接口/虚拟世界/世界.md#virtualworldsetcollidersvisible)，设置虚拟世界中模型的包围盒是否显示<!--by sutao-->

1. 新增[CameraSetPos](../接口/虚拟世界/相机.md#camerasetpos)，设置相机位置<!--by sutao-->

1. 新增[CameraGetPos](../接口/虚拟世界/相机.md#cameragetpos)，返回相机位置<!--by sutao-->

1. 新增[CameraSetFov](../接口/虚拟世界/相机.md#camerasetfov)，设置相机视野大小<!--by sutao-->

1. 新增[CameraGetFov](../接口/虚拟世界/相机.md#cameragetfov)，获取相机视野大小<!--by sutao-->

1. 新增[CameraSetZoom](../接口/虚拟世界/相机.md#camerasetzoom)，设置相机缩放<!--by sutao-->

1. 新增[CameraLookAt](../接口/虚拟世界/相机.md#cameralookat)，修改相机朝向<!--by sutao-->

1. 新增[CameraMoveTo](../接口/虚拟世界/相机.md#cameramoveto)，设置相机移动动画<!--by sutao-->

1. 新增[CameraStopActions](../接口/虚拟世界/相机.md#camerastopactions)，停止相机移动动画<!--by sutao-->

1. 新增[CameraGetZoom](../接口/虚拟世界/相机.md#cameragetzoom)，获取相机的缩放值<!--by sutao-->

1. 新增[CameraGetClickModel](../接口/虚拟世界/相机.md#cameragetclickmodel)，获取相机当前指向的模型的id<!--by sutao-->

1. 新增[ModelCreateObject](../接口/虚拟世界/模型.md#modelcreateobject)，在虚拟世界中创建模型<!--by sutao-->

1. 新增[ModelSetVisible](../接口/虚拟世界/模型.md#modelsetvisible)，设置模型可见性<!--by sutao-->

1. 新增[ModelIsVisible](../接口/虚拟世界/模型.md#modelisvisible)，返回模型可见性<!--by sutao-->

1. 新增[ModelPlayAnimation](../接口/虚拟世界/模型.md#modelplayanimation)，模型播放动画<!--by sutao-->

1. 新增[ModelSetBoxCollider](../接口/虚拟世界/模型.md#modelsetboxcollider)，设置模型的包围盒<!--by sutao-->

1. 新增[ModelRemove](../接口/虚拟世界/模型.md#modelremove)，销毁模型<!--by sutao-->

1. 新增[ModelRotate](../接口/虚拟世界/模型.md#modelrotate)，模型绕某个轴旋转多少度<!--by sutao-->

1. 新增[ModelSetPos](../接口/虚拟世界/模型.md#modelsetpos)，设置模型的坐标<!--by sutao-->

1. 新增[ModelGetPos](../接口/虚拟世界/模型.md#modelgetpos)，获取模型的坐标<!--by sutao-->

1. 新增[ModelSetRot](../接口/虚拟世界/模型.md#modelsetrot)，设置模型的旋转角度<!--by sutao-->

1. 新增[ModelGetRot](../接口/虚拟世界/模型.md#modelgetrot)，返回模型的旋转角度<!--by sutao-->

1. 新增[ModelSetScale](../接口/虚拟世界/模型.md#modelsetscale)，设置模型的缩放值<!--by sutao-->

1. 新增[ModelMoveTo](../接口/虚拟世界/模型.md#modelmoveto)，设置模型平移运动<!--by sutao-->

1. 新增[ModelRotateTo](../接口/虚拟世界/模型.md#modelrotateto)，设置模型旋转运动<!--by sutao-->

1. 新增[ModelStopActions](../接口/虚拟世界/模型.md#modelstopactions)，停止模型的移动和旋转运动<!--by sutao-->

1. 新增[MoveToVirtualWorld](../接口/虚拟世界/其它对象.md#movetovirtualworld)，把对象从主世界移到虚拟世界<!--by sutao-->

1. 新增[BindModel](../接口/虚拟世界/其它对象.md#bindmodel)，对象绑定到模型上<!--by sutao-->

1. 新增[BindVirtualWorldModel](../接口/自定义UI/UI界面.md#bindvirtualworldmodel)，绑定虚拟世界中的模型<!--by sutao-->

1. 新增[UpdateScreen](../接口/自定义UI/UI界面.md#updatescreen)，刷新界面，重新计算各个控件的相关数据<!--by panlei-->

1. 新增[SetHighestY](../接口/自定义UI/UI界面.md#sethighesty)，设置绘制地图的最大高度<!--by gzhuabo-->

1. 新增[SetLayer](../接口/自定义UI/UI控件.md#setlayer)，外放SetLayer接口<!--by panlei-->

1. 新增[ZoomIn](../接口/自定义UI/UI控件.md#zoomin)，放大地图<!--by gzhuabo-->

1. 新增[SetHighestY](../接口/自定义UI/UI控件.md#sethighesty)，设置绘制地图的最大高度<!--by gzhuabo-->

1. 新增[InventoryItemChangedServerEvent](../事件/物品.md#inventoryitemchangedserverevent)，玩家背包物品变化时的服务端事件<!--by jishaobin-->

1. 新增[CraftItemOutputChangeServerEvent](../事件/物品.md#craftitemoutputchangeserverevent)，拿出生成物品时抛出的事件。<!--by jishaobin-->

1. 新增[OnRainLevelChangeServerEvent](../事件/世界.md#onrainlevelchangeserverevent)，下雨强度改变事件。<!--by czh-->

1. 新增[OnLightningLevelChangeServerEvent](../事件/世界.md#onlightninglevelchangeserverevent)，打雷强度改变事件。<!--by czh-->

1. 新增[PlaySoundClientEvent](../事件/音效.md#playsoundclientevent)，播放场景音效或UI音效事件<!--by czh-->

1. 新增[PlayMusicClientEvent](../事件/音效.md#playmusicclientevent)，播放背景音乐事件<!--by czh-->

1. 新增[InventoryItemChangedClientEvent](../事件/物品.md#inventoryitemchangedclientevent)，玩家背包物品变化时的客户端事件<!--by jishaobin-->

1. 新增[TimeEaseType](../枚举值/TimeEaseType.md)，时间变化类型<!--by sutao-->

1. 新增[VirtualWorldObjectType](../枚举值/VirtualWorldObjectType.md)，虚拟世界对象类型<!--by sutao-->

- 调整

1. 调整[StartRecordPacket](../接口/通用/调试.md#startrecordpacket)，添加仅支持租赁服与Apollo环境的说明<!--by xltang-->

1. 调整[StopRecordPacket](../接口/通用/调试.md#stoprecordpacket)，添加仅支持租赁服与Apollo环境的说明<!--by xltang-->

1. 调整[StartRecordEvent](../接口/通用/调试.md#startrecordevent)，添加仅支持租赁服与Apollo环境的说明<!--by xltang-->

1. 调整[StopRecordEvent](../接口/通用/调试.md#stoprecordevent)，添加仅支持租赁服与Apollo环境的说明<!--by xltang-->

1. 调整[SetAttrValue](../接口/实体/属性.md#setattrvalue)，新增对AttrType.LAVA_SPEED的支持，可设置实体在岩浆中的移动速度<!--by liaoyi-->

1. 调整[GetAttrValue](../接口/实体/属性.md#getattrvalue)，新增对AttrType.LAVA_SPEED的支持，可获取实体在岩浆中的移动速度<!--by liaoyi-->

1. 调整[SetAttrMaxValue](../接口/实体/属性.md#setattrmaxvalue)，新增对AttrType.LAVA_SPEED的支持，可设置实体在岩浆中的最大移动速度<!--by liaoyi-->

1. 调整[PlayerDestoryBlock](../接口/玩家/行为.md#playerdestoryblock)，新增particle参数，用于设置是否开启破坏粒子效果,1:开启,0:关闭,默认为1<!--by jishaobin-->

1. 调整[SpawnResources](../接口/世界/实体管理.md#spawnresources)，新增是否随机采集参数allowRandomness<!--by gzhuabo-->

1. 调整[ChangeEntityDimension](../接口/实体/属性.md#changeentitydimension)，该接口无法对玩家使用，玩家请使用ChangePlayerDimension<!--by likaiyu-->

1. 调整[CreateDimension](../接口/世界/地图.md#createdimension)，支持自定义维度的创建<!--by xltang-->

1. 调整[UpgradeMapDimensionVersion](../接口/世界/地图.md#upgrademapdimensionversion)，增加使用时机限制的说明：建议仅在游戏启动初始化的时期调用<!--by xltang-->

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)，新增itemCategory,itemType,itemTierLevel字段<!--by jisahobin-->

1. 调整[SetPlayerRespawnPos](../接口/玩家/行为.md#setplayerrespawnpos)，新增参数dimensionId，支持设置复活维度<!--by xltang-->

1. 调整[SetCameraPos](../接口/玩家/摄像机.md#setcamerapos)，调整设置效果为不存档<!--by xujiarong-->

1. 调整[SetCameraOffset](../接口/玩家/摄像机.md#setcameraoffset)，调整设置效果为不存档<!--by xujiarong-->

1. 调整[SetCameraAnchor](../接口/玩家/摄像机.md#setcameraanchor)，调整设置效果为不存档<!--by xujiarong-->

1. 调整[SetCameraPitchLimit](../接口/玩家/摄像机.md#setcamerapitchlimit)，调整设置效果为不存档<!--by xujiarong-->

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)，新增itemCategory,itemType,itemTierLevel字段<!--by jisahobin-->

1. 调整[SetVisible](../)，添加说明可以设置componentPath为空字符串（""）调整整个JSON的显示/隐藏<!--by xltang-->

1. 调整[Clone](../接口/自定义UI/UI界面.md#clone)，增加是否同步刷新参数<!--by panlei-->

1. 调整[SetVisible](../接口/自定义UI/UI控件.md#setvisible)，添加说明可以通过传入空字符串（""）的方式来调整整个JSON的显示/隐藏<!--by xltang-->

1. 调整[WillTeleportToServerEvent](../事件/实体.md#willteleporttoserverevent)，补完参数说明中缺失的部分<!--by xltang-->

1. 调整[OnNewArmorExchangeServerEvent](../事件/物品.md#onnewarmorexchangeserverevent)，修改当装备为空时，关键字oldArmorDict、newArmorDict的内容说明<!--by xltang-->

- 修复

1. 修复[SetDisableDropItem](../接口/世界/游戏规则.md#setdisabledropitem)，修复了禁止丢弃物品后仍可在容器内（如背包、箱子）丢弃物品的问题。<!--by likaiyu-->

1. 修复[SetDefaultGameType](../接口/世界/游戏规则.md#setdefaultgametype)，修复了联机时可能不生效的问题<!--by likaiyu-->

1. 修复[GetGameRulesInfoServer](../接口/世界/游戏规则.md#getgamerulesinfoserver)，修复了always_day可能为错误值的问题<!--by likaiyu-->

1. 修复[AddBannedItem](../接口/世界/游戏规则.md#addbanneditem)，修复禁用打火石后引燃TNT仍起效问题<!--by xujiarong-->

1. 修复[SetItemTierLevel](../接口/物品.md#setitemtierlevel)，修复了等级3及以上时对哭泣的黑曜石无效的问题<!--by likaiyu-->

1. 修复[SetCameraRot](../接口/玩家/摄像机.md#setcamerarot)，修复第一人称下无法设置相机转向问题<!--by xujiarong-->

- 废弃（将在未来不可用）

1. 废弃HidePlayerName，该接口改名为HideNameTag

1. 废弃SetHurtBy，请使用SetAttackTarget

1. 废弃ResetHurtBy，请使用ResetAttackTarget

1. 废弃GetHurtBy，请使用GetAttackTarget

1. 废弃SpawnItemToPlayerOffHand，请使用接口SetEntityItem

1. 废弃SpawnItemToArmor，请使用SetEntityItem

1. 废弃isInLava，请使用isEntityInLava

1. 废弃isOnGround，请使用isEntityOnGround



## 1.23

# 1.23

**2021.06.24：版本号（v1.23 BE1.16.201）**

* 重大更新
  1. 由于部分物品的名称与附加值存在变更，物品信息字典添加了newItemName及newAuxValue字段以兼容，详见<a href="../../../mcguide/20-玩法开发/13-模组SDK编程/2-Python脚本开发/99-1.23版本物品id变更.html" rel="noopenner"> 1.23版本物品id变更 </a>
  2. 支持微缩方块，方块的形状支持根据地图或自定义数据生成，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/10-微缩方块.html" rel="noopenner"> 微缩方块 </a>
  3. 骨骼模型材质功能拓展，详见<a href="../../../mcguide/16-美术/7-材质与着色器/材质配置说明.html" rel="noopenner"> 材质配置说明 </a>，<a href="../../../mcguide/16-美术/7-材质与着色器/材质的分类.html" rel="noopenner"> 材质的分类 </a>，<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/9-骨骼模型自定义材质.html" rel="noopenner"> 骨骼模型自定义材质 </a>（1.23后续将会有更多材质与着色器的使用文档）。以及材质热更新的[ReloadAllMaterials](../接口/通用/调试.md#reloadallmaterials)，[ReloadOneShader](../接口/通用/调试.md#reloadoneshader)接口
  4. 支持骨骼模型动作融合，详见[SetAnimationBoneMask](../接口/模型.md#setanimationbonemask)，[SetAnimLayer](../接口/模型.md#setanimlayer)等模型分类下的接口
  5. 支持创建下界、末地、超平坦世界为模板的新维度，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/1-自定义维度.html#新维度配置" rel="noopenner"> 自定义维度 </a>
  6. 支持自定义剪刀，详见[SetShearsDestoryBlockSpeed](../接口/物品.md#setshearsdestoryblockspeed)，[ShearsDestoryBlockBeforeServerEvent](../事件/方块.md#shearsdestoryblockbeforeserverevent)等接口
  7. 支持局部维度时间规则，详见[SetUseLocalTime](../接口/世界/时间.md#setuselocaltime)等时间分类下的接口
  8. 支持自定义饥饿设置，详见[SetPlayerStarveLevel](../接口/玩家/属性.md#setplayerstarvelevel)，[SetPlayerStarveTick](../接口/玩家/属性.md#setplayerstarvetick)，[SetPlayerNaturalStarve](../接口/玩家/属性.md#setplayernaturalstarve)等接口

- 新增

1. 新增[ReloadAllMaterials](../接口/通用/调试.md#reloadallmaterials)，清空并重新加载所有材质文件<!--by sutao-->

1. 新增[ReloadAllShaders](../接口/通用/调试.md#reloadallshaders)，重新加载所有Shader文件<!--by sutao-->

1. 新增[ReloadOneShader](../接口/通用/调试.md#reloadoneshader)，重新加载某个Shader文件<!--by sutao-->

1. 新增[GetModConfigJson](../接口/通用/工具.md#getmodconfigjson)，以字典形式返回指定路径的json格式配置文件的内容<!--by xltang-->

1. 新增[SetEntityOwner](../接口/实体/属性.md#setentityowner)，设置实体的属主<!--by linzhiyi-->

1. 新增[GetEntityOwner](../接口/实体/属性.md#getentityowner)，获取实体的属主<!--by gzhuabo-->

1. 新增[CreateMicroBlockResStr](../接口/世界/方块组合.md#createmicroblockresstr)，创建微缩方块资源字符串<!--by guoxun-->

1. 新增[PlayerUseItemToPos](../接口/玩家/行为.md#playeruseitemtopos)，新增模拟玩家对某个坐标使用物品的接口<!--by guanmingyu-->

1. 新增[PlayerUseItemToEntity](../接口/玩家/行为.md#playeruseitemtoentity)，新增模拟玩家对某个生物使用物品的接口<!--by guanmingyu-->

1. 新增[GetLoadedChunks](../接口/世界/地图.md#getloadedchunks)，获取指定维度当前已经加载完毕的全部区块的坐标列表<!--by xltang-->

1. 新增[GetChunkEntites](../接口/世界/地图.md#getchunkentites)，获取指定位置的区块中，全部的实体和玩家的ID列表<!--by xltang-->

1. 新增[GetCommandPermissionLevel](../接口/世界/指令.md#getcommandpermissionlevel)，返回设定使用/op命令时OP的权限等级<!--by xltang-->

1. 新增[SetCommandPermissionLevel](../接口/世界/指令.md#setcommandpermissionlevel)，设置当玩家使用/op命令时OP的权限等级<!--by xltang-->

1. 新增[GetDefaultPlayerPermissionLevel](../接口/世界/指令.md#getdefaultplayerpermissionlevel)，返回新玩家加入时的权限身份<!--by xltang-->

1. 新增[SetDefaultPlayerPermissionLevel](../接口/世界/指令.md#setdefaultplayerpermissionlevel)，设置新玩家加入时的权限身份<!--by xltang-->

1. 新增[SetUseLocalTime](../接口/世界/时间.md#setuselocaltime)，让某个维度拥有自己的局部时间规则，开启后该维度可以拥有与其他维度不同的时间与是否昼夜更替的规则<!--by czh-->

1. 新增[GetUseLocalTime](../接口/世界/时间.md#getuselocaltime)，获取某个维度是否设置了使用局部时间规则<!--by czh-->

1. 新增[SetLocalTime](../接口/世界/时间.md#setlocaltime)，设置使用局部时间规则维度的时间<!--by czh-->

1. 新增[SetLocalTimeOfDay](../接口/世界/时间.md#setlocaltimeofday)，设置使用局部时间规则维度在一天内所在的时间<!--by czh-->

1. 新增[GetLocalTime](../接口/世界/时间.md#getlocaltime)，获取维度的时间<!--by czh-->

1. 新增[SetLocalDoDayNightCycle](../接口/世界/时间.md#setlocaldodaynightcycle)，设置使用局部时间规则的维度是否打开昼夜更替<!--by czh-->

1. 新增[GetLocalDoDayNightCycle](../接口/世界/时间.md#getlocaldodaynightcycle)，获取维度是否打开昼夜更替<!--by czh-->

1. 新增[SaveExtraData](../接口/实体/自定义数据.md#saveextradata)，保存实体的自定义数据或者世界的自定义数据<!--by gzhuabo-->

1. 新增[LocateNeteaseFeatureRule](../接口/世界/地图.md#locateneteasefeaturerule)，定位满足某个网易自定义特征规则分布条件的坐标<!--by liaoyi-->

1. 新增[IsEntityAlive](../接口/世界/实体管理.md#isentityalive)，服务端接口，判断生物实体是否存活或非生物实体是否存在<!--by xujiarong-->

1. 新增[SetMergeSpawnItemRadius](../接口/世界/地图.md#setmergespawnitemradius)，设置新生成的物品是否合堆<!--by sutao-->

1. 新增[GetChinese](../接口/通用/工具.md#getchinese)，获取langStr对应的中文<!--by xltang-->

1. 新增[SetShearsDestoryBlockSpeed](../接口/物品.md#setshearsdestoryblockspeed)，设置剪刀对某一方块的破坏速度<!--by likaiyu-->

1. 新增[CancelShearsDestoryBlockSpeed](../接口/物品.md#cancelshearsdestoryblockspeed)，取消剪刀对某一方块的破坏速度设置<!--by likaiyu-->

1. 新增[CancelShearsDestoryBlockSpeedAll](../接口/物品.md#cancelshearsdestoryblockspeedall)，取消剪刀对全部方块的破坏速度设置<!--by likaiyu-->

1. 新增[GetPlayerHealthLevel](../接口/玩家/属性.md#getplayerhealthlevel)，获取玩家健康临界值<!--by lidi-->

1. 新增[SetPlayerHealthLevel](../接口/玩家/属性.md#setplayerhealthlevel)，设置玩家健康临界值<!--by lidi-->

1. 新增[GetPlayerHealthTick](../接口/玩家/属性.md#getplayerhealthtick)，获取玩家自然恢复速度，单位刻<!--by lidi-->

1. 新增[SetPlayerHealthTick](../接口/玩家/属性.md#setplayerhealthtick)，设置玩家自然恢复速度，单位刻<!--by lidi-->

1. 新增[IsPlayerNaturalRegen](../接口/玩家/属性.md#isplayernaturalregen)，获取是否开启玩家自然恢复<!--by lidi-->

1. 新增[SetPlayerNaturalRegen](../接口/玩家/属性.md#setplayernaturalregen)，设置是否开启玩家自然恢复<!--by lidi-->

1. 新增[GetPlayerStarveLevel](../接口/玩家/属性.md#getplayerstarvelevel)，获取玩家饥饿临界值<!--by lidi-->

1. 新增[SetPlayerStarveLevel](../接口/玩家/属性.md#setplayerstarvelevel)，设置玩家饥饿临界值，如果该值大于健康临界值，将被设置为健康临界值<!--by lidi-->

1. 新增[GetPlayerStarveTick](../接口/玩家/属性.md#getplayerstarvetick)，获取玩家饥饿掉血速度，单位刻<!--by lidi-->

1. 新增[SetPlayerStarveTick](../接口/玩家/属性.md#setplayerstarvetick)，设置玩家饥饿掉血速度，单位刻<!--by lidi-->

1. 新增[IsPlayerNaturalStarve](../接口/玩家/属性.md#isplayernaturalstarve)，获取是否开启玩家饥饿掉血<!--by lidi-->

1. 新增[SetPlayerNaturalStarve](../接口/玩家/属性.md#setplayernaturalstarve)，设置是否开启玩家饥饿掉血<!--by lidi-->

1. 新增[SetTimeOfDay](../接口/世界/时间.md#settimeofday)，设置当前世界在一天内所在的时间<!--by czh-->

1. 新增[SetDeviceVibrate](../接口/控制.md#setdevicevibrate)，可以设置设备震动<!--by likaiyu-->

1. 新增[IsEntityAlive](../接口/世界/实体管理.md#isentityalive)，客户端接口，判断生物实体是否存活或非生物实体是否存在<!--by xujiarong-->

1. 新增[GetChinese](../接口/通用/工具.md#getchinese)，获取langStr对应的中文<!--by liaoyi-->

1. 新增[GetPlayingAnimList](../接口/模型.md#getplayinganimlist)，获取指定的骨骼模型中正在播放的骨骼动画名称列表<!--by xujiarong-->

1. 新增[SetShowArmModel](../接口/模型.md#setshowarmmodel)，设置使用骨骼模型后切换至第一人称时是否显示手部模型<!--by xujiarong-->

1. 新增[SetExtraUniformValue](../接口/模型.md#setextrauniformvalue)，设置shader中特定Uniform的值<!--by sutao-->

1. 新增[ModelStopAni](../接口/模型.md#modelstopani)，增加停止播放骨骼动画接口<!--by xujiarong-->

1. 新增[SetAnimationBoneMask](../接口/模型.md#setanimationbonemask)，新增动作融合功能接口：设置屏蔽骨骼动画中的指定骨骼<!--by xujiarong-->

1. 新增[SetAnimationAllBoneMask](../接口/模型.md#setanimationallbonemask)，新增动作融合功能接口：设置屏蔽骨骼动画中的所有骨骼<!--by xujiarong-->

1. 新增[CancelAllBoneMask](../接口/模型.md#cancelallbonemask)，新增动作融合功能接口：取消屏蔽骨骼动画中的骨骼屏蔽<!--by xujiarong-->

1. 新增[SetAnimLayer](../接口/模型.md#setanimlayer)，新增动作融合功能接口：设置骨骼动画层级<!--by xujiarong-->

1. 新增[RegisterAnim1DControlParam](../接口/模型.md#registeranim1dcontrolparam)，新增动作融合功能接口：注册用于控制两个动画融合的1D控制参数<!--by xujiarong-->

1. 新增[SetAnim1DControlParam](../接口/模型.md#setanim1dcontrolparam)，新增动作融合功能接口：设置用于控制两个动画融合的1D控制参数的值<!--by xujiarong-->

1. 新增[SetUsePointFiltering](../接口/特效/粒子.md#setusepointfiltering)，设置粒子材质的纹理滤波是否使用点滤波<!--by xujiarong-->

1. 新增[SetSplitControlCanChange](../接口/游戏设置.md#setsplitcontrolcanchange)，设置是否允许使用准星瞄准按钮(设了不允许就不能在设置里修改)<!--by guanmingyu-->

1. 新增[SetText](../接口/特效/文字面板.md#settext)，修改文字面板的内容<!--by czh-->

1. 新增[VirtualWorldSetSkyTexture](../接口/虚拟世界/世界.md#virtualworldsetskytexture)，设置虚拟世界中天空的贴图<!--by sutao-->

1. 新增[VirtualWorldSetSkyBgColor](../接口/虚拟世界/世界.md#virtualworldsetskybgcolor)，设置虚拟世界中天空背景的颜色<!--by sutao-->

1. 新增[ModelStopAnimation](../接口/虚拟世界/模型.md#modelstopanimation)，新增停止播放接口。<!--by xujiarong-->

1. 新增[ModelSetAnimBoneMask](../接口/虚拟世界/模型.md#modelsetanimbonemask)，新增虚拟世界动作融合功能接口：设置屏蔽骨骼动画中的指定骨骼<!--by xujiarong-->

1. 新增[ModelSetAnimAllBoneMask](../接口/虚拟世界/模型.md#modelsetanimallbonemask)，新增虚拟世界动作融合功能接口：设置屏蔽骨骼动画中的所有骨骼<!--by xujiarong-->

1. 新增[ModelCancelAllBoneMask](../接口/虚拟世界/模型.md#modelcancelallbonemask)，新增虚拟世界动作融合功能接口：取消屏蔽骨骼动画中的骨骼屏蔽<!--by xujiarong-->

1. 新增[ModelSetAnimLayer](../接口/虚拟世界/模型.md#modelsetanimlayer)，新增虚拟世界动作融合功能接口：设置骨骼动画层级<!--by xujiarong-->

1. 新增[ModelRegisterAnim1DControlParam](../接口/虚拟世界/模型.md#modelregisteranim1dcontrolparam)，新增虚拟世界动作融合功能接口：注册用于控制两个动画融合的1D控制参数<!--by xujiarong-->

1. 新增[ModelSetAnim1DControlParam](../接口/虚拟世界/模型.md#modelsetanim1dcontrolparam)，新增虚拟世界动作融合功能接口：设置用于控制两个动画融合的1D控制参数的值<!--by xujiarong-->

1. 新增[SetSpritePlatformHead](../接口/自定义UI/UI控件.md#setspriteplatformhead)，支持图片控件设置成我的世界移动端启动器当前帐号的头像<!--by panlei-->

1. 新增[SetSpritePlatformFrame](../接口/自定义UI/UI控件.md#setspriteplatformframe)，支持图片控件设置成我的世界移动端启动器当前帐号的头像框<!--by panlei-->

1. 新增[GetSliderValue](../接口/自定义UI/UI控件.md#getslidervalue)，获得滑动条的值<!--by panlei-->

1. 新增[SetSliderValue](../接口/自定义UI/UI控件.md#setslidervalue)，设置滑动条的值<!--by panlei-->

1. 新增[ShearsUseToBlockBeforeServerEvent](../事件/物品.md#shearsusetoblockbeforeserverevent)，增加实体手持剪刀对方块使用时事件，可取消剪刀效果<!--by likaiyu-->

1. 新增[NewOnEntityAreaEvent](../事件/世界.md#newonentityareaevent)，RegisterEntityAOIEvent注册过AOI事件后，当有实体进入或离开注册感应区域时触发该事件；回调参数类型是dict<!--by guanmingyu-->

1. 新增[ShearsDestoryBlockBeforeServerEvent](../事件/方块.md#shearsdestoryblockbeforeserverevent)，增加玩家手持剪刀破坏方块时事件，可取消剪刀效果<!--by likaiyu-->

1. 新增[CommandBlockUpdateEvent](../事件/方块.md#commandblockupdateevent)，玩家尝试修改命令方块的内置命令时触发事件<!--by xltang-->

1. 新增[CommandBlockContainerOpenEvent](../事件/方块.md#commandblockcontaineropenevent)，玩家点击命令方块，尝试打开命令方块的设置界面时触发事件<!--by xltang-->

1. 新增[OnBackButtonReleaseClientEvent](../事件/控制.md#onbackbuttonreleaseclientevent)，返回按钮松开事件<!--by likaiyu-->

1. 新增[AnvilCreateResultItemAfterClientEvent](../事件/物品.md#anvilcreateresultitemafterclientevent)，玩家点击铁砧合成的物品时抛出的事件<!--by likaiyu-->

1. 新增[DimensionChangeFinishClientEvent](../事件/玩家.md#dimensionchangefinishclientevent)，新增玩家改变维度事件<!--by sutao-->

1. 新增[ShearsDestoryBlockBeforeClientEvent](../事件/方块.md#shearsdestoryblockbeforeclientevent)，增加玩家手持剪刀破坏方块时事件，可取消剪刀效果<!--by likaiyu-->

- 调整

1. 调整[GetEngineActor](../接口/世界/实体管理.md#getengineactor)，返回结果中去掉当前已经确定要移除的实体<!--by xltang-->

1. 调整[SetEntityOnFire](../接口/实体/行为.md#setentityonfire)，新增参数burn_damage，可设置实体着火状态下每秒扣的血量<!--by guanmingyu-->

1. 调整[GetBiomeName](../接口/世界/地图.md#getbiomename)，支持自定义下界/自定义末地使用<!--by likaiyu-->

1. 调整[SetBlockNew](../接口/世界/方块管理.md#setblocknew)，增加接口使用说明<!--by likaiyu-->

1. 调整[PlayerDestoryBlock](../接口/玩家/行为.md#playerdestoryblock)，新增sendInv参数，用于同步服务端背包信息,默认为不同步<!--by sutao-->

1. 调整[GetBlockNew](../接口/世界/方块管理.md#getblocknew)，增加接口使用说明<!--by likaiyu-->

1. 调整[AddChunkPosWhiteList](../事件/世界.md#addchunkposwhitelist)，ChunkAcquireDiscardedServerEvent不再需要该接口添加白名单<!--by czh-->

1. 调整[RemoveChunkPosWhiteList](../事件/世界.md#removechunkposwhitelist)，ChunkAcquireDiscardedServerEvent不再需要该接口添加白名单<!--by czh-->

1. 调整[SetCommand](../接口/世界/指令.md#setcommand)，当命令执行成功时返回True，否则返回False<!--by xltang-->

1. 调整[ChangePlayerDimension](../接口/玩家/行为.md#changeplayerdimension)，新增接口使用备注<!--by likaiyu-->

1. 调整[RegisterEntityAOIEvent](../事件/世界.md#registerentityaoievent)，新增期待响应的实体类型的参数<!--by guanmingyu-->

1. 调整[SetExtraData](../接口/实体/自定义数据.md#setextradata)，新增参数autoSave，可设置是否自动保存数据，默认为True<!--by gzhuabo-->

1. 调整[ForbidLiquidFlow](../接口/世界/游戏规则.md#forbidliquidflow)，支持在单机环境使用<!--by xltang-->

1. 调整[UpgradeMapDimensionVersion](../接口/世界/地图.md#upgrademapdimensionversion)，调整使用时机的说明与建议<!--by likaiyu-->

1. 调整[SetPlayerAllItems](../接口/玩家/背包.md#setplayerallitems)，修正itemDict传入空字典时无法清空盔甲、裤子、鞋子部位装备的问题<!--by xltang-->

1. 调整[SetEntityItem](../接口/实体/背包.md#setentityitem)，支持设置[运输矿车]和[漏斗矿车]背包中的物品<!--by sutao-->

1. 调整[SpawnItemToContainer](../接口/方块/容器.md#spawnitemtocontainer)，支持使用下面参数清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0<!--by sutao-->

1. 调整[SpawnItemToEnderChest](../接口/方块/容器.md#spawnitemtoenderchest)，支持使用下面参数清空特定槽位:itemDict为空，为{}, 或itemName为minecraft:air，或者count为0<!--by sutao-->

1. 调整[DetectStructure](../接口/世界/地图.md#detectstructure)，新增dimensionId参数，默认为-1，传入非负值时不依赖playerId<!--by likaiyu-->

1. 调整[SetPos](../接口/实体/属性.md#setpos)，在床上时调用该接口会返回False<!--by likaiyu-->

1. 调整[SetFootPos](../接口/实体/属性.md#setfootpos)，在床上时调用该接口会返回False<!--by likaiyu-->

1. 调整[SetRiderRideEntity](../接口/实体/行为.md#setriderrideentity)，增加备注要求被骑乘生物的定义中具有minecraft:rideable组件，且组件中family_types含有可骑乘者的类型声明<!--by sutao-->

1. 调整[isEntityOnGround](../接口/实体/属性.md#isentityonground)，添加备注"客户端实体刚创建时引擎计算还没完成，此时获取该实体是否着地将返回默认值True，需要延迟一帧进行获取才能获取到正确的数据"<!--by sutao-->

1. 调整[PlayCustomMusic](../接口/音效.md#playcustommusic)，添加可以播放原版音效的描述。添加了与本地玩家距离大于16格则跳过播放的优化。<!--by czh-->

1. 调整[BindModelToModel](../接口/模型.md#bindmodeltomodel)，挂接的模型不再会与实体模型播放相同的动作，现在可以对挂接模型播放单独的骨骼动画。<!--by xujiarong-->

1. 调整[BindModelToEntity](../接口/模型.md#bindmodeltoentity)，挂接的模型不再会与实体模型播放相同的动作，现在可以对挂接模型播放单独的骨骼动画。<!--by xujiarong-->

1. 调整[ModelPlayAni](../接口/模型.md#modelplayani)，新增动画混合功能, 新增设置动画层级参数，增加是否播放成功的返回值。<!--by xujiarong-->

1. 调整[SetCanMove](../接口/控制.md#setcanmove)，调整接口使用说明<!--by likaiyu-->

1. 调整[SetMoveLock](../接口/控制.md#setmovelock)，调整接口使用说明<!--by likaiyu-->

1. 调整[ModelPlayAnimation](../接口/虚拟世界/模型.md#modelplayanimation)，新增动画混合功能, 新增设置动画层级参数。<!--by xujiarong-->

1. 调整[PlayerInventoryOpenScriptServerEvent](../事件/UI.md#playerinventoryopenscriptserverevent)，新增某个客户端打开物品背包界面的事件<!--by xltang-->

1. 调整[WillTeleportToServerEvent](../事件/实体.md#willteleporttoserverevent)，切维度接口以及changedimension指令现在会触发该事件。修复了tp指令触发时，toDimensionId异常的问题。<!--by czh-->

1. 调整[PlayerEatFoodServerEvent](../事件/玩家.md#playereatfoodserverevent)，增加饥饿度参数，可修改<!--by lidi-->

1. 调整[ChunkAcquireDiscardedServerEvent](../事件/世界.md#chunkacquirediscardedserverevent)，该事件不再需要注册区块白名单。事件参数添加了随区块卸载而从世界移除的实体以及自定义方块实体列表<!--by czh-->

1. 调整[HopperTryPullInServerEvent](../事件/方块.md#hoppertrypullinserverevent)，更正事件触发时机描述为：当漏斗上方连接容器后，容器往漏斗开始输入物品时触发，事件仅触发一次<!--by xujiarong-->

1. 调整[HopperTryPullOutServerEvent](../事件/方块.md#hoppertrypulloutserverevent)，更正事件触发时机描述为：当漏斗以毗邻的方式连接容器时，即从旁边连接容器时，漏斗向容器开始输出物品时触发，事件仅触发一次<!--by xujiarong-->

1. 调整[ClientPlayerInventoryOpenEvent](../事件/UI.md#clientplayerinventoryopenevent)，新增isCreative参数<!--by xltang-->

- 修复

1. 修复[SetGameRulesInfoServer](../接口/世界/游戏规则.md#setgamerulesinfoserver)，修复了设置cheat_info但是没填enable参数导致“激活作弊”选项无法开启的问题<!--by likaiyu-->

1. 修复[GetUserDataInEvent](../接口/物品.md#getuserdatainevent)，修复了可能对部分事件无效的问题<!--by likaiyu-->

1. 修复[GetUserDataInEvent](../接口/物品.md#getuserdatainevent)，修复了可能对部分事件无效的问题<!--by likaiyu-->

- 废弃（将在未来不可用）

1. 废弃PlaySystemSound，请使用PlayCustomMusic

1. 废弃LocateNeteaseFeature，请使用定位速度更快的接口LocateNeteaseFeatureRule

1. 废弃SpawnItemToChestBlock，请使用SpawnItemToContainer

1. 废弃Play，请使用PlayCustomMusic

1. 废弃GetPlayingAnim，现在骨骼模型支持同时播放多个动画，该接口仅返回单个动画名称。如需要获取正在播放的动画名称，请使用GetPlayingAnimList

1. 废弃PlayBodyAnim，1.23版本骨骼模型动画已增加动作融合功能，可通过动作融合实现上半身的动画播放和暂停。

1. 废弃StopBodyAnim，1.23版本骨骼模型动画已增加动作融合功能，可通过动作融合实现上半身的动画播放和暂停。

1. 废弃PlayLegAnim，1.23版本骨骼模型动画已增加动作融合功能，可通过动作融合实现下半身的动画播放和暂停。

1. 废弃StopLegAnim，1.23版本骨骼模型动画已增加动作融合功能，可通过动作融合实现下半身的动画播放和暂停。

1. 废弃OnEntityAreaEvent，请使用NewOnEntityAreaEvent



## 1.24

# 1.24

温馨提示，预计在9月23日，全渠道更新1.24版本玩家包体，玩家将陆续更新到1.24版本，请开发者合理安排更新节奏。

**2021.09.16：版本号（v1.24 BE1.16.202）**

<iframe src="https://cc.163.com/act/m/daily/iframeplayer/?id=61415ca248e27490891e9566" height="600" width="800" allow="fullscreen" />

- 重大功能介绍

1. 自定义流体

   - 包含流体颜色、贴图、范围、流速设置

   - 可自定义桶装载自定义流体

   - 可设置液体传播火的效果以及进入液体获得的效果

   详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/5-自定义流体.html" rel="noopenner"> 自定义流体 </a>，<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/7-自定义桶.html" rel="noopenner"> 自定义桶 </a>
2. 自定义附魔

   - 支持自定义魔咒、魔咒等级
   - 可在附魔书、附魔台、铁砧上获得自定义附魔
   - 物品上可包含自定义附魔

   详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/11-自定义附魔文档.html" rel="noopenner"> 自定义附魔 </a>
3. 自定义方块功能拓展：

   * 支持方块重力表现，可自定义铁砧、沙砾等下落效果。

     - 支持设置方块下落表现
     - 支持设置下落速度以及伤害
     - 可获取方块开始下落、结束下落、下落过程接触到实体的事件

     详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/6-自定义重力方块.html" rel="noopenner"> 自定义重力方块 </a>

   * 可获取实体下落到方块的事件，可自定义粘液块的弹跳效果。详见[OnAfterFallOnBlockServerEvent](../事件/方块.html#onafterfallonblockserverevent)，[OnAfterFallOnBlockClientEvent](../事件/方块.html#onafterfallonblockclientevent)
   * 可获取实体在方块上移动的事件，可自定义类似冰、灵魂沙等不同的摩擦效果。详见[OnStandOnBlockServerEvent](../事件/方块.html#onstandonblockserverevent)，[OnStandOnBlockClientEvent](../事件/方块.html#onstandonblockclientevent)

4. 自定义方块实体渲染，可实现表现力更强的自定义方块。

   - 方块实体支持添加动画，支持使用由BlockBench制作的原版模型或者是游戏原版模型。
   - 方块实体支持添加特效，可通过配置或者接口，为自定义方块实体附加粒子特效及序列帧特效。

   详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/4.1-自定义方块实体外观.html" rel="noopenner"> 自定义方块实体外观 </a>
5. 自定义分页、分组

   - 支持多个自定义分页，可让物品分类更灵活。

   - 支持把物品放在原有分组或自定义分组中，自定义分组支持多个，可让物品分类更规整。

   详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/12-自定义物品分组.html" rel="noopenner"> 自定义物品分组 </a>与<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/13-自定义物品分页.html" rel="noopenner"> 自定义物品分页 </a>

6. 后处理效果

   - 渐晕效果。画面随中心距离逐渐变暗，实现类似瞄准镜等视觉效果。

     详见[渐晕](../接口/后处理/渐晕.md)
   
   
   
   *(展示视频中涉及的demo下载地址如下：[自定义附魔](https://g79.gdl.netease.com/EnchantDemo.zip)、[其他内容](https://g79.gdl.netease.com/1.24demo.zip))*

- 新增

1. 新增<a href="../../../mcguide/16-美术/7-材质与着色器/Shader使用简介.html" rel="noopenner"> Shader使用简介 </a>教程

1. 新增[StartCoroutine](../接口/通用/工具.md#startcoroutine)，开启服务端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题<!--by handaoying-->

1. 新增[StopCoroutine](../接口/通用/工具.md#stopcoroutine)，停止服务端协程<!--by handaoying-->

1. 新增[OpenChatGui](../接口/原生UI.md#openchatgui)，打开原版聊天栏<!--by hdy-->

1. 新增[StartCoroutine](../接口/通用/工具.md#startcoroutine)，开启客户端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题<!--by handaoying-->

1. 新增[StopCoroutine](../接口/通用/工具.md#stopcoroutine)，停止客户端协程<!--by handaoying-->

1. 新增[GetTypeFamily](../接口/实体/属性.md#gettypefamily)，获取生物行为包字段 type_family<!--by hdy-->

1. 新增[AddModEnchantToInvItem](../接口/玩家/背包.md#addmodenchanttoinvitem)，新增给物品栏中物品添加自定义附魔信息接口<!--by liaoyi-->

1. 新增[RemoveEnchantToInvItem](../接口/玩家/背包.md#removeenchanttoinvitem)，新增给物品栏中物品移除附魔信息接口<!--by liaoyi-->

1. 新增[RemoveModEnchantToInvItem](../接口/玩家/背包.md#removemodenchanttoinvitem)，新增给物品栏中物品移除自定义附魔信息接口<!--by liaoyi-->

1. 新增[GetInvItemModEnchantData](../接口/玩家/背包.md#getinvitemmodenchantdata)，新增获取物品栏的物品自定义附魔信息<!--by liaoyi-->

1. 新增[GetEquItemModEnchant](../接口/实体/背包.md#getequitemmodenchant)，新增支持获取生物装备槽位中盔甲的自定义附魔<!--by liaoyi-->

1. 新增[SetItemMaxDurability](../接口/物品.md#setitemmaxdurability)，设置物品的最大耐久值<!--by likaiyu-->

1. 新增[GetItemMaxDurability](../接口/物品.md#getitemmaxdurability)，获取指定槽位的物品最大耐久<!--by likaiyu-->

1. 新增[GetPlayerExhaustionRatioByType](../接口/玩家/行为.md#getplayerexhaustionratiobytype)，获取玩家某行为饥饿度消耗倍率<!--by hdy-->

1. 新增[SetPlayerExhaustionRatioByType](../接口/玩家/行为.md#setplayerexhaustionratiobytype)，设置玩家某行为饥饿度消耗倍率<!--by hdy-->

1. 新增[SetPlayerAttackSpeedAmplifier](../接口/玩家/行为.md#setplayerattackspeedamplifier)，设置玩家攻击速度倍数<!--by gzhuabo-->

1. 新增[SetBlockEntityMolangValue](../接口/方块/方块实体.md#setblockentitymolangvalue)，设置自定义方块实体的Molang变量，用于控制自定义实体的动画转变。<!--by xujiarong-->

1. 新增[GetBlockEntityMolangValue](../接口/方块/方块实体.md#getblockentitymolangvalue)，获取自定义方块实体的Molang变量的值。<!--by xujiarong-->

1. 新增[SetEnableBlockEntityAnimations](../接口/方块/方块实体.md#setenableblockentityanimations)，是否开启自定义方块实体的动画效果。<!--by xujiarong-->

1. 新增[CreateParticleEffectForBlockEntity](../接口/方块/方块实体.md#createparticleeffectforblockentity)，在自定义方块实体上创建粒子特效。<!--by xujiarong-->

1. 新增[GetParticleEffectIdInBlockEntity](../接口/方块/方块实体.md#getparticleeffectidinblockentity)，获取在自定义方块实体中已创建的粒子特效的Id。<!--by xujiarong-->

1. 新增[RemoveParticleEffectInBlockEntity](../接口/方块/方块实体.md#removeparticleeffectinblockentity)，移除在自定义方块实体上创建的粒子特效。<!--by xujiarong-->

1. 新增[CreateFrameEffectForBlockEntity](../接口/方块/方块实体.md#createframeeffectforblockentity)，在自定义方块实体上创建序列帧特效。<!--by xujiarong-->

1. 新增[GetFrameEffectIdInBlockEntity](../接口/方块/方块实体.md#getframeeffectidinblockentity)，获取在自定义方块实体中已创建的序列帧特效的Id。<!--by xujiarong-->

1. 新增[RemoveFrameEffectInBlockEntity](../接口/方块/方块实体.md#removeframeeffectinblockentity)，移除在自定义方块实体上创建的序列帧特效。<!--by xujiarong-->

1. 新增[SetBlockEntityParticlePosOffset](../接口/方块/渲染.md#setblockentityparticleposoffset)，设置自定义方块实体中粒子特效位置的偏移值<!--by xujiarong-->

1. 新增[SetBlockEntityFramePosOffset](../接口/方块/渲染.md#setblockentityframeposoffset)，设置自定义方块实体中序列帧特效位置的偏移值<!--by xujiarong-->

1. 新增[SetBlockEntityModelPosOffset](../接口/方块/渲染.md#setblockentitymodelposoffset)，设置自定义方块实体的实体模型位置偏移值<!--by xujiarong-->

1. 新增[SetBlockEntityModelScale](../接口/方块/渲染.md#setblockentitymodelscale)，设置自定义方块实体的实体模型大小的缩放值。<!--by xujiarong-->

1. 新增[SetBlockEntityModelRotation](../接口/方块/渲染.md#setblockentitymodelrotation)，设置自定义方块实体的实体模型在各个轴上的旋转值。<!--by xujiarong-->

1. 新增[GetPos](../接口/特效/序列帧.md#getpos)，获取序列帧特效的世界坐标位置。<!--by xujiarong-->

1. 新增[GetRot](../接口/特效/序列帧.md#getrot)，获取序列帧特效的旋转角度。<!--by xujiarong-->

1. 新增[GetScale](../接口/特效/序列帧.md#getscale)，获取序列帧特效的缩放值。<!--by xujiarong-->

1. 新增[SetParticleSize](../接口/特效/粒子.md#setparticlesize)，设置粒子特效中粒子大小的最小值及最大值。<!--by xujiarong-->

1. 新增[GetParticleMaxSize](../接口/特效/粒子.md#getparticlemaxsize)，获取粒子特效中粒子大小的最大值。<!--by xujiarong-->

1. 新增[GetParticleMinSize](../接口/特效/粒子.md#getparticleminsize)，获取粒子特效中粒子大小的最小值。<!--by xujiarong-->

1. 新增[SetParticleVolumeSize](../接口/特效/粒子.md#setparticlevolumesize)，设置粒子发射器的体积大小缩放。<!--by xujiarong-->

1. 新增[GetParticleVolumeSize](../接口/特效/粒子.md#getparticlevolumesize)，获取粒子发射器的体积大小缩放值。<!--by xujiarong-->

1. 新增[SetParticleMaxNum](../接口/特效/粒子.md#setparticlemaxnum)，设置粒子发射器所包含的最大粒子数量。<!--by xujiarong-->

1. 新增[GetParticleMaxNum](../接口/特效/粒子.md#getparticlemaxnum)，获取粒子发射器包含的最大粒子数量。<!--by xujiarong-->

1. 新增[SetParticleEmissionRate](../接口/特效/粒子.md#setparticleemissionrate)，设置粒子发射器每帧发射粒子的频率。<!--by xujiarong-->

1. 新增[GetParticleEmissionRate](../接口/特效/粒子.md#getparticleemissionrate)，获取粒子发射器每帧发射粒子的频率。<!--by xujiarong-->

1. 新增[GetPos](../接口/特效/粒子.md#getpos)，获取粒子发射器的世界坐标位置。<!--by xujiarong-->

1. 新增[GetRot](../接口/特效/粒子.md#getrot)，获取粒子发射器的旋转角度。<!--by xujiarong-->

1. 新增[SetRotUseZXY](../接口/特效/粒子.md#setrotusezxy)，设置粒子发射器的旋转，旋转顺序按照绕z,x,y轴旋转<!--by xujiarong-->

1. 新增[Swing](../接口/玩家/属性.md#swing)，本地玩家播放原版攻击动作<!--by gzhuabo-->

1. 新增[SetEnableVignette](../接口/后处理/渐晕.md#setenablevignette)，是否开启渐晕效果<!--by xujiarong-->

1. 新增[CheckVignetteEnabled](../接口/后处理/渐晕.md#checkvignetteenabled)，检测是否开启渐晕效果<!--by xujiarong-->

1. 新增[SetVignetteRGB](../接口/后处理/渐晕.md#setvignettergb)，设置渐晕效果的渐晕颜色<!--by xujiarong-->

1. 新增[SetVignetteCenter](../接口/后处理/渐晕.md#setvignettecenter)，设置渐晕效果的渐晕中心位置<!--by xujiarong-->

1. 新增[SetVignetteRadius](../接口/后处理/渐晕.md#setvignetteradius)，设置渐晕效果的渐晕半径<!--by xujiarong-->

1. 新增[SetVignetteSmoothness](../接口/后处理/渐晕.md#setvignettesmoothness)，设置渐晕效果的渐晕模糊系数<!--by xujiarong-->

1. 新增[HeavyBlockStartFallingServerEvent](../事件/方块.md#heavyblockstartfallingserverevent)，增加重力方块变为下落的方块实体后触发的事件<!--by likaiyu-->

1. 新增[FallingBlockReturnHeavyBlockServerEvent](../事件/方块.md#fallingblockreturnheavyblockserverevent)，增加下落的方块实体变回普通重力方块时触发的事件<!--by likaiyu-->

1. 新增[FallingBlockBreakServerEvent](../事件/方块.md#fallingblockbreakserverevent)，增加下落的方块实体被破坏时触发的事件<!--by likaiyu-->

1. 新增[FallingBlockCauseDamageBeforeServerEvent](../事件/方块.md#fallingblockcausedamagebeforeserverevent)，增加下落的方块计算砸实体伤害的事件，可修改部分属性<!--by likaiyu-->

1. 新增[OnBeforeFallOnBlockServerEvent](../事件/方块.md#onbeforefallonblockserverevent)，增加实体刚降落到方块上时服务端触发的事件，主要用于伤害计算<!--by likaiyu-->

1. 新增[OnAfterFallOnBlockServerEvent](../事件/方块.md#onafterfallonblockserverevent)，增加实体刚降落到方块上时服务端触发的事件，主要用于力的计算<!--by likaiyu-->

1. 新增[OnStandOnBlockServerEvent](../事件/方块.md#onstandonblockserverevent)，增加当实体站立到方块上时服务端持续触发的事件<!--by likaiyu-->

1. 新增[PlayerTrySleepServerEvent](../事件/玩家.md#playertrysleepserverevent)，玩家尝试使用床睡觉。<!--by hdy-->

1. 新增[PlayerSleepServerEvent](../事件/玩家.md#playersleepserverevent)，玩家使用床睡觉成功。<!--by hdy-->

1. 新增[PlayerStopSleepServerEvent](../事件/玩家.md#playerstopsleepserverevent)，玩家停止睡觉<!--by hdy-->

1. 新增[OnItemPutInEnchantingModelServerEvent](../事件/物品.md#onitemputinenchantingmodelserverevent)，玩家将可附魔物品放到附魔台上时的事件，可修改此时附魔台的选项<!--by liaoyi-->

1. 新增[GrindStoneRemovedEnchantClientEvent](../事件/物品.md#grindstoneremovedenchantclientevent)，新增玩家点击砂轮合成得到的物品事件<!--by liaoyi-->

1. 新增[FallingBlockCauseDamageBeforeClientEvent](../事件/方块.md#fallingblockcausedamagebeforeclientevent)，增加下落的方块计算砸实体伤害的事件，可修改部分属性<!--by likaiyu-->

1. 新增[OnAfterFallOnBlockClientEvent](../事件/方块.md#onafterfallonblockclientevent)，增加实体刚降落到方块上时客户端触发的事件，主要用于力的计算<!--by likaiyu-->

1. 新增[OnStandOnBlockClientEvent](../事件/方块.md#onstandonblockclientevent)，增加当实体站立到方块上时客户端持续触发的事件<!--by likaiyu-->

1. 新增[EnchantSlotType](../枚举值/EnchantSlotType.md)，附魔槽位枚举值<!--by liaoyi-->

1. 新增[PlayerExhauseRatioType](../枚举值/PlayerExhauseRatioType.md)，饥饿度消耗倍率类型<!--by hdy-->

- 调整

1. 调整[SetMobKnockback](../接口/实体/行为.md#setmobknockback)，增加备注：在damageEvent事件里面使用该接口时，需把damageEvent事件回调的knock参数设置为False<!--by guanmingyu-->

1. 调整[SetMotion](../接口/实体/行为.md#setmotion)，增加备注：在damageEvent事件里面使用该接口时，需把damageEvent事件回调的knock参数设置为False<!--by guanmingyu-->

1. 调整[SetMotion](../接口/实体/行为.md#setmotion)，优化文档说明<!--by likaiyu-->

1. 调整[DepartCamera](../接口/玩家/摄像机.md#departcamera)，坐船情况下，分离相机后玩家的镜头水平转动时能够360度转动。<!--by xujiarong-->

1. 调整[SetEntityOpacity](../接口/模型.md#setentityopacity)，更正接口功能作用范围为：只对骨骼模型生效<!--by xujiarong-->

1. 调整[EntityTickServerEvent](../事件/实体.md#entitytickserverevent)，添加实体identifier参数<!--by hdy-->

1. 调整[ChunkLoadedServerEvent](../事件/世界.md#chunkloadedserverevent)，该事件不再需要添加区块白名单<!--by czh-->

1. 调整[AnvilCreateResultItemAfterClientEvent](../事件/物品.md#anvilcreateresultitemafterclientevent)，返回值新增合成前两个物品的物品信息字典<!--by liaoyi-->

1. 调整[ChunkLoadedClientEvent](../事件/世界.md#chunkloadedclientevent)，该事件不再需要添加区块白名单<!--by czh-->

1. 调整[ChunkAcquireDiscardedClientEvent](../事件/世界.md#chunkacquirediscardedclientevent)，该事件不再需要添加区块白名单<!--by czh-->

- 修复

1. 修复[GetBiomeName](../接口/世界/地图.md#getbiomename)，修复了在mod有自定义下界的情况下，获取原版下界未加载区块变成自定义下界群系的问题。<!--by likaiyu-->

1. 修复[SetEntityScale](../接口/模型.md#setentityscale)，修复了某些情况大小会被重置的问题<!--by czh-->

1. 修复[ActorAcquiredItemClientEvent](../事件/物品.md#actoracquireditemclientevent)，修复了与村民交易时会触发两次的问题<!--by czh-->

- 废弃（将在未来不可用）

1. 废弃AddChunkPosWhiteList，区块加载与卸载事件不再需要白名单

1. 废弃AddChunkPosWhiteList，区块加载与卸载事件不再需要白名单

1. 废弃SetRot，该接口设置的旋转值按照x,y,z轴旋转，与其他接口不兼容，故逐步废弃。请使用SetRotUseZXY接口

1. 废弃SetUiItem，推荐使用UI面向对象ItemRendererUIControl.SetUiItem接口



## 1.25

# 1.25

温馨提示，预计在11月26日，全渠道更新1.25版本玩家包体，玩家将陆续更新到1.25版本，请开发者合理安排更新节奏。



2021.11.18：版本号（v1.25 BE1.16.203）

- 新增重大功能介绍

1.自定义生物AI

- 可在脚本层扩展生物AI，实现更多的生物表现。

  详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/3-自定义生物/01-自定义基础生物.html#_11-自定义生物行为" rel="noopenner"> 自定义生物行为 </a>，举例详见[离线包](#demo离线包下载)中的CustomEntityMod。

2.虚拟世界支持微软原版模型

- 可更便捷实现回合制或小场景玩法。

    详见[ModelCreateMinecraftObject](../接口/虚拟世界/模型.md#modelcreateminecraftobject)以及[ModelUpdateAnimationMolangVariable](../接口/虚拟世界/模型.md#modelupdateanimationmolangvariable)，举例详见[离线包](#demo离线包下载)中的VirtualWorldDemo。

3.结构体功能拓展

- 结构体支持旋转，可旋转90，180，270度
- 支持使用PlaceStructure或通过结构特征json旋转

    详见[PlaceStructure](../接口/世界/地图.md#placestructure) 或 <a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/4-自定义特征.html" rel="noopenner"> 结构特征json旋转方式 </a>

4.自定义维度拓展

- 自定义维度新增netease:ban_vanilla_feature,可让该维度禁止生成原版feature,可用于解决类似空岛生存天空悬浮结构问题

    详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/1-自定义维度.html" rel="noopenner"> 自定义维度 </a>

5.支持按维度独立设置天气，详见[天气](../接口/世界/天气.html)

6.新增后处理功能，可实现高斯模糊、颜色矫正、景深、镜头污迹等效果，详见[后处理](../接口/后处理/索引.html)

- 新增

1. 自定义方块实体外观<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/4.1-自定义方块实体外观.html#_1-2-方块实体的多面向" rel="noopenner"> 支持多面向 </a>

1. 自定义方块增加<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/1-JSON组件.html#netease-on-entity-inside" rel="noopenner"> netease:on_entity_inside </a>、netease:on_step_on、netease:on_step_off组件

1. 自定义物品增加<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/1-自定义基础物品.html#netease-enchant-material" rel="noopenner"> netease:enchant_material组件 </a>

1. UI新增<a href="../../../mcguide/18-界面与交互/30-UI说明文档.html#neteasecombobox" rel="noopenner"> 单选下拉框控件 </a>

1. 新增[GetCustomGoalCls](../接口/实体/行为.md#getcustomgoalcls)(服务端)， 增加获取自定义行为节点基类的接口<!--by syy-->

1. 新增[SetEnableReconnectNetgame](../接口/通用/调试.md#setenablereconnectnetgame)(客户端)， 设置是否允许断线重连<!--by guanmingyu-->

1. 新增[SetResourceFastload](../接口/通用/调试.md#setresourcefastload)(客户端)， 设置资源快速加载<!--by jishaobin-->

1. 新增[GetResourceFastload](../接口/通用/调试.md#getresourcefastload)(客户端)， 获取资源快速加载设置<!--by jishaobin-->

1. 新增[GetEnableReconnectNetgame](../接口/通用/调试.md#getenablereconnectnetgame)(客户端)， 获取是否允许断线重连<!--by guanmingyu-->

1. 新增[OpenInventoryGui](../接口/原生UI.md#openinventorygui)(客户端)， 打开原版背包界面<!--by hdy-->

1. 新增[CreateEngineEffectBind](../接口/特效/模型特效.md#createengineeffectbind)(客户端)， 指用编辑器保存资源包中models/bind/xxx_bind.json生成编辑好的所有挂点的所有特效<!--by cyk-->

1. 新增[RegisterOnStandOn](../事件/方块.md#registeronstandon)(服务端)， 可以动态注册与修改原版方块的netease:on_stand_on组件(服务端接口)<!--by likaiyu-->

1. 新增[UnRegisterOnStandOn](../事件/方块.md#unregisteronstandon)(服务端)， 可以动态删除原版方块的netease:on_stand_on组件(服务端接口)<!--by likaiyu-->

1. 新增[RegisterOnStepOn](../事件/方块.md#registeronstepon)(服务端)， 可以动态注册与修改原版方块的netease:on_step_on组件(服务端接口)<!--by likaiyu-->

1. 新增[UnRegisterOnStepOn](../事件/方块.md#unregisteronstepon)(服务端)， 可以动态删除原版方块的netease:on_step_on组件(服务端接口)<!--by likaiyu-->

1. 新增[RegisterOnStepOff](../事件/方块.md#registeronstepoff)(服务端)， 可以动态注册与修改原版方块的netease:on_step_off组件(服务端接口)<!--by likaiyu-->

1. 新增[UnRegisterOnStepOff](../事件/方块.md#unregisteronstepoff)(服务端)， 可以动态删除原版方块的netease:on_step_off组件(服务端接口)<!--by likaiyu-->

1. 新增[RegisterOnEntityInside](../事件/方块.md#registeronentityinside)(服务端)， 可以动态注册与修改原版方块的netease:on_entity_inside组件(服务端接口)<!--by likaiyu-->

1. 新增[UnRegisterOnEntityInside](../事件/方块.md#unregisteronentityinside)(服务端)， 可以动态删除原版方块的netease:on_entity_inside组件(服务端接口)<!--by likaiyu-->

1. 新增[SetDimensionUseLocalWeather](../接口/世界/天气.md#setdimensionuselocalweather)(服务端)， 设置某个维度拥有自己的天气规则，开启后该维度可以拥有与其他维度不同的天气和天气更替的规则<!--by hdy-->

1. 新增[GetDimensionUseLocalWeather](../接口/世界/天气.md#getdimensionuselocalweather)(服务端)， 获取某个维度是否拥有自己的天气规则<!--by hdy-->

1. 新增[SetDimensionLocalRain](../接口/世界/天气.md#setdimensionlocalrain)(服务端)， 设置某个维度下雨(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)<!--by hdy-->

1. 新增[SetDimensionLocalThunder](../接口/世界/天气.md#setdimensionlocalthunder)(服务端)， 设置某个维度打雷(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)<!--by hdy-->

1. 新增[SetDimensionLocalDoWeatherCycle](../接口/世界/天气.md#setdimensionlocaldoweathercycle)(服务端)， 设置某个维度是否开启天气循环(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)<!--by hdy-->

1. 新增[GetDimensionLocalWeatherInfo](../接口/世界/天气.md#getdimensionlocalweatherinfo)(服务端)， 获取独立维度天气信息(必须先使用SetDimensionUseLocalWeather接口设置此维度拥有自己的独立天气)<!--by hdy-->

1. 新增[RegisterOnStandOn](../事件/方块.md#registeronstandon)(客户端)， 可以动态注册与修改原版方块的netease:on_stand_on组件（客户端接口）<!--by likaiyu-->

1. 新增[UnRegisterOnStandOn](../事件/方块.md#unregisteronstandon)(客户端)， 可以动态删除原版方块的netease:on_stand_on组件（客户端接口）<!--by likaiyu-->

1. 新增[RegisterOnStepOn](../事件/方块.md#registeronstepon)(客户端)， 可以动态注册与修改原版方块的netease:on_step_on组件（客户端接口）<!--by likaiyu-->

1. 新增[UnRegisterOnStepOn](../事件/方块.md#unregisteronstepon)(客户端)， 可以动态删除原版方块的netease:on_step_on组件（客户端接口）<!--by likaiyu-->

1. 新增[RegisterOnStepOff](../事件/方块.md#registeronstepoff)(客户端)， 可以动态注册与修改原版方块的netease:on_step_off组件（客户端接口）<!--by likaiyu-->

1. 新增[UnRegisterOnStepOff](../事件/方块.md#unregisteronstepoff)(客户端)， 可以动态删除原版方块的netease:on_step_off组件（客户端接口）<!--by likaiyu-->

1. 新增[RegisterOnEntityInside](../事件/方块.md#registeronentityinside)(客户端)， 可以动态注册与修改原版方块的netease:on_entity_inside组件（客户端接口）<!--by likaiyu-->

1. 新增[UnRegisterOnEntityInside](../事件/方块.md#unregisteronentityinside)(客户端)， 可以动态删除原版方块的netease:on_entity_inside组件（客户端接口）<!--by likaiyu-->

1. 新增[SetEnableGaussianBlur](../接口/后处理/模糊.md#setenablegaussianblur)(客户端)， 是否开启高斯模糊效果<!--by xujiarong-->

1. 新增[CheckGaussianBlurEnabled](../接口/后处理/模糊.md#checkgaussianblurenabled)(客户端)， 检测是否开启高斯模糊效果<!--by xujiarong-->

1. 新增[SetGaussianBlurRadius](../接口/后处理/模糊.md#setgaussianblurradius)(客户端)， 设置高斯模糊效果的模糊半径<!--by xujiarong-->

1. 新增[SetEnableColorAdjustment](../接口/后处理/色彩.md#setenablecoloradjustment)(客户端)， 是否开启色彩校正效果<!--by xujiarong-->

1. 新增[CheckColorAdjustmentEnabled](../接口/后处理/色彩.md#checkcoloradjustmentenabled)(客户端)， 检测是否开启色彩校正效果<!--by xujiarong-->

1. 新增[SetColorAdjustmentBrightness](../接口/后处理/色彩.md#setcoloradjustmentbrightness)(客户端)， 调整屏幕色彩亮度值<!--by xujiarong-->

1. 新增[SetColorAdjustmentSaturation](../接口/后处理/色彩.md#setcoloradjustmentsaturation)(客户端)， 调整屏幕色彩饱和度<!--by xujiarong-->

1. 新增[SetColorAdjustmentContrast](../接口/后处理/色彩.md#setcoloradjustmentcontrast)(客户端)， 调整屏幕色彩对比度<!--by xujiarong-->

1. 新增[SetColorAdjustmentTint](../接口/后处理/色彩.md#setcoloradjustmenttint)(客户端)， 调整屏幕色彩的色调<!--by xujiarong-->

1. 新增[SetEnableLensStain](../接口/后处理/镜头效果.md#setenablelensstain)(客户端)， 是否开启镜头污迹效果<!--by xujiarong-->

1. 新增[CheckLensStainEnabled](../接口/后处理/镜头效果.md#checklensstainenabled)(客户端)， 检测是否开启镜头污迹效果<!--by xujiarong-->

1. 新增[SetLensStainTexture](../接口/后处理/镜头效果.md#setlensstaintexture)(客户端)， 改变镜头污迹所使用的贴图<!--by xujiarong-->

1. 新增[ResetLensStainTexture](../接口/后处理/镜头效果.md#resetlensstaintexture)(客户端)， 重置镜头污迹所使用的贴图为系统默认贴图<!--by xujiarong-->

1. 新增[SetLensStainIntensity](../接口/后处理/镜头效果.md#setlensstainintensity)(客户端)， 调整镜头污迹强度<!--by xujiarong-->

1. 新增[SetLensStainColor](../接口/后处理/镜头效果.md#setlensstaincolor)(客户端)， 调整镜头污迹颜色<!--by xujiarong-->

1. 新增[SetEnableDepthOfField](../接口/后处理/镜头效果.md#setenabledepthoffield)(客户端)， 是否开启景深效果<!--by xujiarong-->

1. 新增[CheckDepthOfFieldEnabled](../接口/后处理/镜头效果.md#checkdepthoffieldenabled)(客户端)， 检测是否开启景深效果<!--by xujiarong-->

1. 新增[SetDepthOfFieldFocusDistance](../接口/后处理/镜头效果.md#setdepthoffieldfocusdistance)(客户端)， 调整景深效果焦点距离<!--by xujiarong-->

1. 新增[SetDepthOfFieldBlurRadius](../接口/后处理/镜头效果.md#setdepthoffieldblurradius)(客户端)， 调整景深效果模糊半径<!--by xujiarong-->

1. 新增[SetDepthOfFieldNearBlurScale](../接口/后处理/镜头效果.md#setdepthoffieldnearblurscale)(客户端)， 调整景深效果近景模糊大小<!--by xujiarong-->

1. 新增[SetDepthOfFieldFarBlurScale](../接口/后处理/镜头效果.md#setdepthoffieldfarblurscale)(客户端)， 调整景深效果远景模糊大小<!--by xujiarong-->

1. 新增[SetDepthOfFieldUseCenterFocus](../接口/后处理/镜头效果.md#setdepthoffieldusecenterfocus)(客户端)， 设置景深效果是否开启屏幕中心聚焦模式<!--by xujiarong-->

1. 新增[ModelCreateMinecraftObject](../接口/虚拟世界/模型.md#modelcreateminecraftobject)(客户端)， 在虚拟世界中创建微软原版模型<!--by sutao-->

1. 新增[ModelUpdateAnimationMolangVariable](../接口/虚拟世界/模型.md#modelupdateanimationmolangvariable)(客户端)， 更新微软原版模型表达式变量，可控制动作的改变<!--by sutao-->

1. 新增[asNeteaseComboBox](../接口/自定义UI/UI控件.md#asneteasecombobox)(客户端)， UI面向对象<!--by panlei-->

1. 新增[AddOption](../接口/自定义UI/UI控件.md#addoption)(客户端)， 添加下拉框项<!--by panlei01-->

1. 新增[ClearOptions](../接口/自定义UI/UI控件.md#clearoptions)(客户端)， 清空下拉框<!--by panlei01-->

1. 新增[ClearSelection](../接口/自定义UI/UI控件.md#clearselection)(客户端)， 清除当前选中<!--by panlei01-->

1. 新增[GetOptionIndexByShowName](../接口/自定义UI/UI控件.md#getoptionindexbyshowname)(客户端)， 根据展示文本查找对应下拉框项的索引位置<!--by panlei01-->

1. 新增[GetOptionShowNameByIndex](../接口/自定义UI/UI控件.md#getoptionshownamebyindex)(客户端)， 根据索引位置查找当前栈式文本<!--by panlei01-->

1. 新增[GetOptionCount](../接口/自定义UI/UI控件.md#getoptioncount)(客户端)， 获得选项数量<!--by panlei01-->

1. 新增[GetSelectOptionIndex](../接口/自定义UI/UI控件.md#getselectoptionindex)(客户端)， 获得当前选中项的索引<!--by panlei01-->

1. 新增[GetSelectOptionShowName](../接口/自定义UI/UI控件.md#getselectoptionshowname)(客户端)， 获得当前选中项的展示文本<!--by panlei01-->

1. 新增[RemoveOptionByShowName](../接口/自定义UI/UI控件.md#removeoptionbyshowname)(客户端)， 根据提供的展示文本移除对应下拉框项<!--by panlei01-->

1. 新增[RemoveOptionByIndex](../接口/自定义UI/UI控件.md#removeoptionbyindex)(客户端)， 根据提供的索引移除对应下拉框项<!--by panlei01-->

1. 新增[SetSelectOptionByIndex](../接口/自定义UI/UI控件.md#setselectoptionbyindex)(客户端)， 根据提供的索引移除对应下拉框项<!--by panlei01-->

1. 新增[SetSelectOptionByShowName](../接口/自定义UI/UI控件.md#setselectoptionbyshowname)(客户端)， 根据提供的展示文本选中对应下拉框项<!--by panlei01-->

1. 新增[RegisterOpenComboBoxCallback](../接口/自定义UI/UI控件.md#registeropencomboboxcallback)(客户端)， 注册展开下拉框事件回调<!--by panlei01-->

1. 新增[RegisterCloseComboBoxCallback](../接口/自定义UI/UI控件.md#registerclosecomboboxcallback)(客户端)， 注册关闭下拉框事件回调<!--by panlei01-->

1. 新增[RegisterSelectItemCallback](../接口/自定义UI/UI控件.md#registerselectitemcallback)(客户端)， 注册选中下拉框内容事件回调<!--by panlei01-->

1. 新增[StepOffBlockServerEvent](../事件/方块.md#stepoffblockserverevent)(服务端)， 新增实体移动离开一个实心方块时触发的事件<!--by likaiyu-->

1. 新增[PlayerIntendLeaveServerEvent](../事件/世界.md#playerintendleaveserverevent)(服务端)， 即将删除玩家事件，此时可以通过各种API获取玩家的当前状态。<!--by xltang-->

1. 新增[OnEntityInsideBlockServerEvent](../事件/方块.md#onentityinsideblockserverevent)(服务端)， 增加当实体碰撞盒所在区域有方块时服务端持续触发的事件<!--by likaiyu-->

1. 新增[OnLocalRainLevelChangeServerEvent](../事件/世界.md#onlocalrainlevelchangeserverevent)(服务端)， 独立维度天气下雨强度发生改变时触发<!--by hdy-->

1. 新增[OnLocalLightningLevelChangeServerEvent](../事件/世界.md#onlocallightninglevelchangeserverevent)(服务端)， 独立维度天气打雷强度发生改变时触发<!--by hdy-->

1. 新增[StepOffBlockClientEvent](../事件/方块.md#stepoffblockclientevent)(客户端)， 新增实体移动离开一个实心方块时触发的事件<!--by likaiyu-->

1. 新增[OnEntityInsideBlockClientEvent](../事件/方块.md#onentityinsideblockclientevent)(客户端)， 增加当实体碰撞盒所在区域有方块时客户端持续触发的事件<!--by likaiyu-->

1. 新增[PlayerTryDropItemClientEvent](../事件/物品.md#playertrydropitemclientevent)(客户端)， 新增客户端玩家尝试丢弃物品的事件。<!--by guanmingyu-->

1. 新增[InventoryType](../枚举值/InventoryType.md)， 添加自定义分页枚举<!--by hdy-->

- 调整

1. 调整[PlaceStructure](../接口/世界/地图.md#placestructure)(服务端)， 添加默认参数rotation，默认为0，可将放置的结构体沿y轴进行旋转<!--by hdy-->

1. 调整[GetRecipesByResult](../接口/世界/配方.md#getrecipesbyresult)(服务端)， 熔炉配方支持返回输出物品的数量<!--by czh-->

1. 调整[GetRecipesByInput](../接口/世界/配方.md#getrecipesbyinput)(服务端)， 熔炉配方支持返回输出物品的数量<!--by czh-->

1. 调整[GetRecipesByResult](../接口/世界/配方.md#getrecipesbyresult)(客户端)， 熔炉配方支持返回输出物品的数量<!--by czh-->

1. 调整[GetRecipesByInput](../接口/世界/配方.md#getrecipesbyinput)(客户端)， 熔炉配方支持返回输出物品的数量<!--by czh-->

1. 调整[SetToggleState](../接口/自定义UI/UI控件.md#settogglestate)(客户端)， 新增参数，可调整toggle路径<!--by panlei01-->

1. 调整[ServerSpawnMobEvent](../事件/世界.md#serverspawnmobevent)(服务端)， 新增realIdentifier参数<!--by guanmingyu-->

1. 调整[StepOnBlockServerEvent](../事件/方块.md#steponblockserverevent)(服务端)， 重大触发机制调整、备注说明更新<!--by likaiyu-->

1. 调整[OnStandOnBlockServerEvent](../事件/方块.md#onstandonblockserverevent)(服务端)， 增加了cancel、dimensionId参数，优化了备注文档说明<!--by likaiyu-->

1. 调整[StepOnBlockClientEvent](../事件/方块.md#steponblockclientevent)(客户端)， 重大触发机制调整、备注说明更新<!--by likaiyu-->

1. 调整[OnStandOnBlockClientEvent](../事件/方块.md#onstandonblockclientevent)(客户端)， 新增cancel、dimensionId参数<!--by likaiyu-->

- 修复

1. 修复[SetPlayerGameType](../接口/玩家/游戏模式.md#setplayergametype)(服务端)， 修复了在AddServerPlayerEvent中使用会导致崩溃的问题<!--by czh-->

1. 修复[PerspChangeClientEvent](../事件/玩家.md#perspchangeclientevent)(客户端)， 修复了在设置界面切换视角时不会触发该事件的问题<!--by likaiyu-->

- 废弃（将在未来不可用）

1. 废弃CreateEngineEffect，请使用CreateEngineEffectBind

1. 废弃ClearPlayerOffHand，已废弃，请使用SetEntityItem，itemDict传None即可

1. 废弃SetInvItemDurability，已废弃，请使用SetItemDurability

1. 废弃GetInvItemDurability，已废弃，请使用GetItemDurability

1. 废弃SetEquItemDurability，已废弃，请使用SetItemDurability

1. 废弃GetEquItemDurability，已废弃，请使用GetItemDurability



## 2.0

# 2.0

2022.1.13：版本号（v2.0 BE1.17.2）

包括Mod PC包，手机测试版启动器，和服务器引擎。

- 温馨提示

在1月21日，全渠道将更新2.0版本玩家包体，玩家将陆续更新到2.0版本，请开发者合理安排更新节奏。

- 新增重大功能介绍

1. 自定义地形

原版的群系只能在“minecraft:overworld_generation_rules”中改变群系的突变，以及根据温度来划分群系出现的概率，无法更加灵活的控制群系的布局，所以在2.0版本，我们引入了自定义群系源，用来解决原版hardcode群系布局的问题。

使用新的功能，你可以更精细的控制地形的生成，下面是使用Json生成的示例地形，具体的使用请参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/2-群系地貌.html#7.自定义群系生成流程（网易版）" rel="noopenner"> 自定义群系生成流程（网易版） </a>。

![image-20211220211830475](../picture/image-20211220211830475.png)

2. 自定义含水，含雪方块

自定义含水方块支持在组件中配置自定义方块含水的相关功能，并支持python监听事件、接口设置等，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/7-自定义含水方块.html" rel="noopenner"> 自定义含水方块 </a>。

自定义含雪方块支持在组件中配置自定义方块含雪的相关功能，并支持python监听事件、接口设置等，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/3-特殊方块/9-自定义含雪方块.html" rel="noopenner"> 自定义含雪方块 </a>。

3. 自定义方块实体支持原版粒子特效和音效

详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/4.1-自定义方块实体外观.html#添加微软原版粒子特效及音效" rel="noopenner"> 添加微软原版粒子特效及音效 </a>。

4. 自定义书

书本作为一种物品，主要是供玩家浏览信息，基于自定义书本，你可以提供一个书本界面给玩家，可以让玩家用翻书本的方式获取知识。详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/5-自定义书本/01-自定义基础书本.html" rel="noopenner"> 自定义书 </a>。

![image-20220104105922105](../picture/image-20220104105922105.png)


- 新增其他功能

自定义基础物品增加 netease:fuel 和 netease:cooldown 字段，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/1-自定义基础物品.html" rel="noopenner"> 自定义基础物品 </a>。

- 新增

1. 新增[GetTopScreen](../接口/自定义UI/通用.md#gettopscreen)，获取UI堆栈栈顶的UI节点<!--by mayexing-->

1. 新增[GetBookManager](../接口/自定义UI/自定义书本.md#getbookmanager)，获取书本管理对象<!--by myx-->

1. 新增[NotifyToMultiClients](../接口/通用/事件.md#notifytomulticlients)， 服务器发送事件到指定一批客户端<!--by xltang-->

1. 新增[ResetMotion](../接口/实体/行为.md#resetmotion)，重置生物的瞬时移动方向向量<!--by xujiarong02-->

1. 新增[SetPersistent](../接口/实体/属性.md#setpersistent)，设置实体不会因为离玩家太远而被[清除](https://minecraft.fandom.com/zh/wiki/%E7%94%9F%E6%88%90#.E5.9F.BA.E5.B2.A9.E7.89.88_2)<!--by czh-->

1. 新增[SetLiquidBlock](../接口/世界/方块管理.md#setliquidblock)，设置某一位置的方块的extraBlock接口<!--by guanmingyu-->

1. 新增[SetSnowBlock](../接口/世界/方块管理.md#setsnowblock)，设置某一位置的方块含雪<!--by guanmingyu-->

1. 新增[GetLiquidBlock](../接口/世界/方块管理.md#getliquidblock)，获取方块所含流体信息接口<!--by guanmingyu-->

1. 新增[GetBlockControlAi](../接口/实体/行为.md#getblockcontrolai)，获取生物原生AI是否被屏蔽<!--by czh-->

1. 新增[GetSpawnDimension](../接口/世界/地图.md#getspawndimension)，获取世界出生维度<!--by czh-->

1. 新增[SetSpawnDimensionAndPosition](../接口/世界/地图.md#setspawndimensionandposition)，设置世界出生点维度与坐标<!--by czh-->

1. 新增[GetPlayerUid](../接口/联机大厅.md#getplayeruid)，获取玩家的uid<!--by czh-->

1. 新增[QueryLobbyUserItem](../接口/联机大厅.md#querylobbyuseritem)，查询还没发货的订单接口<!--by gmy-->

1. 新增[LobbyGetStorage](../接口/联机大厅.md#lobbygetstorage)，获取存储的数据接口<!--by gmy-->

1. 新增[LobbySetStorageAndUserItem](../接口/联机大厅.md#lobbysetstorageanduseritem)，设置订单已发货或者存数据接口<!--by gmy-->

1. 新增[GetPlayerRespawnPos](../接口/玩家/行为.md#getplayerrespawnpos)，新增获取玩家复活点接口<!--by guanmingyu-->

1. 新增[GetEntityTags](../接口/实体/标签.md#getentitytags)，获取实体标签列表<!--by gzhuabo-->

1. 新增[AddEntityTag](../接口/实体/标签.md#addentitytag)，增加实体标签<!--by gzhuabo-->

1. 新增[RemoveEntityTag](../接口/实体/标签.md#removeentitytag)，移除实体某个指定的标签<!--by gzhuabo-->

1. 新增[EntityHasTag](../接口/实体/标签.md#entityhastag)，判断实体是否存在某个指定的标签<!--by gzhuabo-->

1. 新增[Pause](../接口/特效/模型特效.md#pause)，暂停模型特效<!--by czh-->

1. 新增[Resume](../接口/特效/模型特效.md#resume)，继续播放模型特效<!--by czh-->

1. 新增[Pause](../接口/特效/序列帧.md#pause)，暂停序列帧播放<!--by czh-->

1. 新增[SetRotUseZXY](../接口/特效/序列帧.md#setrotusezxy)，设置序列帧的旋转，旋转顺序按照绕z,x,y轴旋转<!--by xujiarong-->

1. 新增[SetFreeModelAniSpeed](../接口/模型.md#setfreemodelanispeed)，设置自由模型动画的播放速度<!--by xusifan-->

1. 新增[SetEntityShadowShow](../接口/模型.md#setentityshadowshow)，设置实体打开/关闭影子渲染<!--by guanmingyu-->

1. 新增[Pause](../接口/特效/粒子.md#pause)，暂停粒子播放<!--by czh-->

1. 新增[GetStringHash64](../接口/实体/molang.md#getstringhash64)，增加返回字符串变量的hash64的接口<!--by guanmingyu-->

1. 新增[Update](../接口/自定义UI/UI界面.md#update)，补充文档<!--by mayexing-->

1. 新增[GetScreenName](../接口/自定义UI/UI界面.md#getscreenname)，获得本界面的名称<!--by mayexing-->

1. 新增[lobbyGoodBuySucServerEvent](../事件/联机大厅.md#lobbygoodbuysucserverevent)，玩家联机大厅登录或者联机大厅游戏内购买商品时服务端抛出的事件<!--by guanmingyu-->

1. 新增[HealthChangeServerEvent](../事件/实体.md#healthchangeserverevent)，生物生命值发生变化的事件<!--by czh-->

1. 新增[BlockLiquidStateChangeServerEvent](../事件/方块.md#blockliquidstatechangeserverevent)，方块转为含水或者脱离含水(流体)前触发的事件<!--by guanmingyu-->

1. 新增[BlockLiquidStateChangeAfterServerEvent](../事件/方块.md#blockliquidstatechangeafterserverevent)，方块转为含水或者脱离含水(流体)后触发的事件<!--by guanmingyu-->

1. 新增[BlockSnowStateChangeServerEvent](../事件/方块.md#blocksnowstatechangeserverevent)，方块转为含雪或者脱离含雪前触发的事件<!--by guanmingyu-->

1. 新增[BlockSnowStateChangeAfterServerEvent](../事件/方块.md#blocksnowstatechangeafterserverevent)，方块转为含雪或者脱离含雪后触发的事件<!--by guanmingyu-->

1. 新增[OnModBlockNeteaseEffectCreatedClientEvent](../事件/方块.md#onmodblockneteaseeffectcreatedclientevent)，自定义方块实体绑定的特效创建成功事件<!--by xujiarong02-->

1. 新增[HealthChangeClientEvent](../事件/实体.md#healthchangeclientevent)，生物生命值发生变化的事件<!--by czh-->

1. 新增[EntityModelChangedClientEvent](../事件/实体.md#entitymodelchangedclientevent)，新增实体模型切换时触发的事件。<!--by guanmingyu-->

1. 新增[SetBlockType](../枚举值/SetBlockType.md)，方块设置的类型<!--by guanmingyu-->

- 调整

1. 调整[CreateUI](../接口/自定义UI/通用.md#createui)，添加备注<!--by mayexing-->

1. 调整[StartNavTo](../接口/玩家/导航.md#startnavto)，新增控制序列帧是否开启深度检测的参数<!--by czh-->

1. 调整[PushScreen](../接口/自定义UI/通用.md#pushscreen)，增加自定义参数<!--by mayexing-->

1. 调整[SetBlockControlAi](../接口/实体/行为.md#setblockcontrolai)，原版模型关闭AI时动作也会冻结<!--by czh-->

1. 调整[ChangePlayerFlyState](../接口/玩家/行为.md#changeplayerflystate)，新增使用限制说明<!--by guanmingyu-->

1. 调整[SetCanBlockSetOnFireByLightning](../接口/世界/游戏规则.md#setcanblocksetonfirebylightning)，外放这个接口<!--by guanmingyu-->

1. 调整[SetCanActorSetOnFireByLightning](../接口/世界/游戏规则.md#setcanactorsetonfirebylightning)，外放这个接口<!--by guanmingyu-->

1. 调整[GetAttrValue](../接口/实体/属性.md#getattrvalue)，新增客户端获取属性的接口<!--by guanmingyu-->

1. 调整[GetAttrMaxValue](../接口/实体/属性.md#getattrmaxvalue)，新增客户端获取属性最大值的接口<!--by guanmingyu-->

1. 调整[GetMolangValue](../接口/实体/molang.md#getmolangvalue)，扩展接口，增加返回molang变量hash64<!--by guanmingyu-->

1. 调整[ChangeBindAutoScale](../接口/自定义UI/UI界面.md#changebindautoscale)，添加备注<!--by mayexing-->

1. 调整[OnOffhandItemChangedServerEvent](../事件/物品.md#onoffhanditemchangedserverevent)，新增备注：切换耐久度不同的相同物品，不会触发该事件<!--by guanmingyu-->

1. 调整[OnCarriedNewItemChangedServerEvent](../事件/物品.md#oncarriednewitemchangedserverevent)，新增备注：切换耐久度不同的相同物品，不会触发该事件<!--by guanmingyu-->

1. 调整[ServerItemTryUseEvent](../事件/物品.md#serveritemtryuseevent)，新增使用场景的描述<!--by guanmingyu-->

1. 调整[OnItemPutInEnchantingModelServerEvent](../事件/物品.md#onitemputinenchantingmodelserverevent)，playerId的参数类型改为str<!--by xujiarong02-->

- 修复

1. 修复了可以通过summon npc指令召唤教育版npc的问题
1. 修复[ModelUpdateAnimationMolangVariable](../接口/虚拟世界/模型.md#modelupdateanimationmolangvariable)，修复了客户端实体中配置了scripts/initialize时接口不生效的问题<!--by czh-->

- 离线Demo下载

下载[DEMO](https://g79.gdl.netease.com/2.0DemoV4.zip)。



## 2.1

# 2.1

2022.4.15：版本号（v2.1 BE1.17.3）

包括Mod PC包，手机测试版启动器，和服务器引擎。

- 新增重大功能介绍

1. 自定义盾牌

对盾牌的自定义进行了支持，并且额外支持了盾牌的动画和模型，具体的使用请参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/8-自定义盾牌.html" rel="noopenner"> 自定义盾牌 </a>。

Demo见：<a href="../../../mcguide/20-玩法开发/13-模组SDK编程/60-Demo示例.html#demomod" rel="noopenner"> 示例简介 </a>

![image-20220314143215073](../picture/image-20220314143215073.png)

2. 方块合并网格体 & 设置网格体为实体模型

主要实现了3个功能。

1）获取指定的方块为一个方块调色板，调色板内记录有各方块的位置和类型，参考[GetBlockPaletteFromPosList](../接口/世界/方块组合.md#getblockpalettefromposlist)(服务端)以及其他接口。

2）使用方块调色板生成对应的网格体模型，参考[CombineBlockPaletteToGeometry](../接口/方块/方块几何体模型.md#combineblockpalettetogeometry)(客户端)以及其他接口。

3）为实体添加指定的网格体模型，参考[AddActorBlockGeometry](../接口/实体/渲染.md#addactorblockgeometry)(客户端)。

如下图，就是将一些方块合并为了网格体模型，并赋予一个可骑乘实体，实现了类似组装战车的效果。

![image-20220314143051215](../picture/image-20220314143051215.png)

Demo见：<a href="../../../mcguide/20-玩法开发/13-模组SDK编程/60-Demo示例.html#demomod" rel="noopenner"> 示例简介 </a>

3. 提供更多中国版群系源节点类型

2.1版本的群系源节点能做到以下功能：
1）将某个群系的部分替换成另外一个群系
2）当群系A与群系B相邻时，则在他们中间生成过渡群系
3）在核心群系的周围生成伴生群系
4）在一个固定长宽的矩形范围内，随机选择一个点放置关键群系
5）根据molang语句来实现群系源控制

![image-20220314150124467](../picture/image-20220314150124467.png)

4. 自定义战利品表扩展

玩家新增幸运值属性，影响战利品数量和权重，详见：<a href="../../../mconline/10-addon教程/第12章：更完善的自定义掉落物/课程02.战利品池.html#补充内容" rel="noopenner"> 战利品池 </a>和[属性值](../枚举值/AttrType.md)。

5. UI控件支持更多设置属性接口

详见[UI控件](../接口/自定义UI/UI控件.md)。

6. 新增屏蔽原版大型结构的10个json组件

可以在维度配置中屏蔽一些大型结构，详见：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/1-自定义维度.html#维度配置" rel="noopenner"> 维度配置 </a>

7. 新增定义物品描述信息的json字段

新增 netease:customtips 字段，详见：<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/1-自定义物品/1-自定义基础物品.html#netease-customtips（2-1beta版内容）" rel="noopenner"> netease-customtips </a>


- 新增

1. 新增[StartMemProfile](../接口/通用/调试.md#startmemprofile)(服务端)， 开始启动服务端脚本内存分析<!--by xusifan-->

1. 新增[StopMemProfile](../接口/通用/调试.md#stopmemprofile)(服务端)， 停止服务端脚本内存分析并生成火焰图<!--by xusifan-->

1. 新增[StartMemProfile](../接口/通用/调试.md#startmemprofile)(客户端)， 开始启动客户端脚本内存分析<!--by xusifan-->

1. 新增[StopMemProfile](../接口/通用/调试.md#stopmemprofile)(客户端)， 停止客户端脚本内存分析并生成火焰图<!--by xusifan-->

1. 新增[GetBlankBlockPalette](../接口/世界/方块组合.md#getblankblockpalette)(服务端)， 获取一个空白的方块调色板<!--by xujiarong02-->

1. 新增[GetBlockPaletteFromPosList](../接口/世界/方块组合.md#getblockpalettefromposlist)(服务端)， 根据输入的方块位置列表创建并获取一个方块调色板<!--by xujiarong02-->

1. 新增[GetBlockPaletteBetweenPos](../接口/世界/方块组合.md#getblockpalettebetweenpos)(服务端)， 根据输入的两个方块位置创建并获取一个方块调色板<!--by xujiarong02-->

1. 新增[SetBlockByBlockPalette](../接口/世界/方块组合.md#setblockbyblockpalette)(服务端)， 根据输入的方块调色板内容，将调色板内记录的所有方块设置为实际的方块。<!--by xujiarong02-->

1. 新增[GetBlockBasicInfo](../接口/方块/属性.md#getblockbasicinfo)(服务端)， 获取方块基本信息<!--by xusifan-->

1. 新增[SetBlockBasicInfo](../接口/方块/属性.md#setblockbasicinfo)(服务端)， 设置方块基本信息<!--by gmy-->

1. 新增[GetBlockCollision](../接口/世界/方块管理.md#getblockcollision)(服务端)， 获取指定位置方块当前collision的aabb接口<!--by xusifan-->

1. 新增[GetBlockClip](../接口/世界/方块管理.md#getblockclip)(服务端)， 获取指定位置方块当前clip的aabb接口<!--by xusifan-->

1. 新增[IsSlimeChunk](../接口/世界/地图.md#isslimechunk)(服务端)， 获取某个区块是否史莱姆区块。<!--by gmy-->

1. 新增[OpenMobHitBlockDetection](../事件/实体.md#openmobhitblockdetection)(服务端)， 开启碰撞方块的检测接口<!--by gmy-->

1. 新增[CloseMobHitBlockDetection](../事件/实体.md#closemobhitblockdetection)(服务端)， 关闭碰撞方块的检测接口<!--by gmy-->

1. 新增[SetJumpPower](../接口/实体/行为.md#setjumppower)(服务端)， 设置生物跳跃力度<!--by gmy-->

1. 新增[SetEntityInteractFilter](../接口/实体/行为.md#setentityinteractfilter)(服务端)， 设置与生物可交互的条件<!--by xiegang-->

1. 新增[GetPlayerUIItem](../接口/方块/容器.md#getplayeruiitem)(服务端)， 获取合成容器的物品<!--by jishaobin-->

1. 新增[GetItemDefenceAngle](../接口/物品.md#getitemdefenceangle)(服务端)， 获取盾牌物品的抵挡角度范围<!--by gmy-->

1. 新增[SetItemDefenceAngle](../接口/物品.md#setitemdefenceangle)(服务端)， 设置盾牌物品的抵挡角度范围<!--by gmy-->

1. 新增[SetInputSlotItem](../接口/方块/容器.md#setinputslotitem)(服务端)， 设置熔炉输入栏物品<!--by huangxiaojie03-->

1. 新增[GetInputSlotItem](../接口/方块/容器.md#getinputslotitem)(服务端)， 获取熔炉输入栏物品<!--by huangxiaojie03-->

1. 新增[GetOutputSlotItem](../接口/方块/容器.md#getoutputslotitem)(服务端)， 获取熔炉输出栏物品<!--by huangxiaojie03-->

1. 新增[GetIsBlocking](../接口/玩家/行为.md#getisblocking)(服务端)， 获取玩家是否处于抵挡状态<!--by gmy-->

1. 新增[AddBrewingRecipes](../接口/世界/配方.md#addbrewingrecipes)(服务端)， 新增添加酿造台配方的接口<!--by gmy-->

1. 新增[SetEntityShareablesItems](../接口/实体/行为.md#setentityshareablesitems)(服务端)， 设置实体可分享/可拾取的物品列表<!--by xiegang-->

1. 新增[AddActorRenderControllerArray](../接口/实体/渲染.md#addactorrendercontrollerarray)(客户端)， 添加实体渲染控制器数组中字典arrays元素<!--by xiegang01-->

1. 新增[AddActorBlockGeometry](../接口/实体/渲染.md#addactorblockgeometry)(客户端)， 为实体添加方块几何体模型<!--by xujiarong02-->

1. 新增[DeleteActorBlockGeometry](../接口/实体/渲染.md#deleteactorblockgeometry)(客户端)， 删除实体中的指定方块几何体模型<!--by xujiarong02-->

1. 新增[ClearActorBlockGeometry](../接口/实体/渲染.md#clearactorblockgeometry)(客户端)， 删除实体中的所有的方块几何体模型<!--by xujiarong02-->

1. 新增[SetActorBlockGeometryVisible](../接口/实体/渲染.md#setactorblockgeometryvisible)(客户端)， 设置实体中指定的方块几何体模型是否显示<!--by xujiarong02-->

1. 新增[SetActorAllBlockGeometryVisible](../接口/实体/渲染.md#setactorallblockgeometryvisible)(客户端)， 设置实体中所有的方块几何体模型是否显示<!--by xujiarong02-->

1. 新增[GetBlankBlockPalette](../接口/世界/方块组合.md#getblankblockpalette)(客户端)， 获取一个空白的方块调色板<!--by xujiarong02-->

1. 新增[GetBlockPaletteFromPosList](../接口/世界/方块组合.md#getblockpalettefromposlist)(客户端)， 根据输入的方块位置列表创建并获取一个方块调色板<!--by xujiarong02-->

1. 新增[GetBlockPaletteBetweenPos](../接口/世界/方块组合.md#getblockpalettebetweenpos)(客户端)， 根据输入的两个位置创建并获取一个方块调色板<!--by xujiarong02-->

1. 新增[CombineBlockPaletteToGeometry](../接口/方块/方块几何体模型.md#combineblockpalettetogeometry)(客户端)， 将BlockPalette中的所有方块合并并转换为能用于实体的几何体模型<!--by xujiarong02-->

1. 新增[CombineBlockBetweenPosToGeometry](../接口/方块/方块几何体模型.md#combineblockbetweenpostogeometry)(客户端)， 根据输入的两个位置，搜索这两个位置之间的所有方块，并将这些方块合并和转换为能用于实体的几何体模型<!--by xujiarong02-->

1. 新增[CombineBlockFromPosListToGeometry](../接口/方块/方块几何体模型.md#combineblockfromposlisttogeometry)(客户端)， 根据输入的两个位置，搜索这两个位置之间的所有方块，并将这些方块合并和转换为能用于实体的几何体模型<!--by xujiarong02-->

1. 新增[GetBlockClip](../接口/世界/方块管理.md#getblockclip)(客户端)， 获取指定位置方块当前clip的aabb<!--by xusifan-->

1. 新增[GetBlockCollision](../接口/世界/方块管理.md#getblockcollision)(客户端)， 获取指定位置方块当前collision的aabb<!--by xusifan-->

1. 新增[SetHealthBarDeviation](../接口/实体/渲染.md#sethealthbardeviation)(客户端)， 新增设置血条高度的接口<!--by gmy-->

1. 新增[GetTexture](../接口/模型.md#gettexture)(客户端)， 获取模型贴图名称路径<!--by huangxiaojie03-->

1. 新增[setUsingShield](../接口/玩家/行为.md#setusingshield)(客户端)， 激活盾牌状态<!--by gmy-->

1. 新增[SetFullSize](../接口/自定义UI/UI控件.md#setfullsize)(客户端)， 设置控件的大小，支持百分比以及绝对值<!--by mayexing-->

1. 新增[GetFullSize](../接口/自定义UI/UI控件.md#getfullsize)(客户端)， 获取控件的大小，支持比例值以及绝对值<!--by mayexing-->

1. 新增[SetFullPosition](../接口/自定义UI/UI控件.md#setfullposition)(客户端)， 设置控件的锚点坐标（全局坐标），支持比例值以及绝对值<!--by mayexing-->

1. 新增[GetFullPosition](../接口/自定义UI/UI控件.md#getfullposition)(客户端)， 获取控件的锚点坐标，支持比例值以及绝对值<!--by mayexing-->

1. 新增[SetAnchorFrom](../接口/自定义UI/UI控件.md#setanchorfrom)(客户端)， 设置控件相对于父节点的锚点<!--by mayexing-->

1. 新增[GetAnchorFrom](../接口/自定义UI/UI控件.md#getanchorfrom)(客户端)， 判断控件相对于父节点的哪个锚点来计算位置与大小<!--by mayexing-->

1. 新增[SetAnchorTo](../接口/自定义UI/UI控件.md#setanchorto)(客户端)， 设置控件自身锚点位置<!--by mayexing-->

1. 新增[GetAnchorTo](../接口/自定义UI/UI控件.md#getanchorto)(客户端)， 获取控件自身锚点位置信息<!--by mayexing-->

1. 新增[SetClipOffset](../接口/自定义UI/UI控件.md#setclipoffset)(客户端)， 设置控件的裁剪偏移信息<!--by mayexing-->

1. 新增[GetClipOffset](../接口/自定义UI/UI控件.md#getclipoffset)(客户端)， 获取控件的裁剪偏移信息<!--by mayexing-->

1. 新增[SetClipsChildren](../接口/自定义UI/UI控件.md#setclipschildren)(客户端)， 设置控件是否开启裁剪内容<!--by mayexing-->

1. 新增[GetClipsChildren](../接口/自定义UI/UI控件.md#getclipschildren)(客户端)， 根据控件路径返回某控件是否开启裁剪内容<!--by mayexing-->

1. 新增[SetMaxSize](../接口/自定义UI/UI控件.md#setmaxsize)(客户端)， 设置控件所允许的最大的大小值<!--by mayexing-->

1. 新增[GetMaxSize](../接口/自定义UI/UI控件.md#getmaxsize)(客户端)， 获取控件所允许的最大的大小值<!--by mayexing-->

1. 新增[SetMinSize](../接口/自定义UI/UI控件.md#setminsize)(客户端)， 设置控件所允许的最小的大小值<!--by mayexing-->

1. 新增[GetMinSize](../接口/自定义UI/UI控件.md#getminsize)(客户端)， 获取控件所允许的最小的大小值<!--by mayexing-->

1. 新增[asStackPanel](../接口/自定义UI/UI控件.md#asstackpanel)(客户端)， 将当前BaseUIControl转换为StackPanelUIControl实例<!--by mayexing-->

1. 新增[asInputPanel](../接口/自定义UI/UI控件.md#asinputpanel)(客户端)， 将当前BaseUIControl转换为InputPanelUIControl实例<!--by mayexing-->

1. 新增[SetClipDirection](../接口/自定义UI/UI控件.md#setclipdirection)(客户端)， 设置图片控件的裁剪方向<!--by mayexing-->

1. 新增[GetClipDirection](../接口/自定义UI/UI控件.md#getclipdirection)(客户端)， 获取图片控件的裁剪方向<!--by mayexing-->

1. 新增[SetImageAdaptionType](../接口/自定义UI/UI控件.md#setimageadaptiontype)(客户端)， 设置图片控件的图片适配方式以及信息<!--by mayexing-->

1. 新增[SetIsModal](../接口/自定义UI/UI控件.md#setismodal)(客户端)， 设置当前面板是否为模态框<!--by mayexing-->

1. 新增[GetIsModal](../接口/自定义UI/UI控件.md#getismodal)(客户端)， 判断当前面板是否为模态框<!--by mayexing-->

1. 新增[SetTextAlignment](../接口/自定义UI/UI控件.md#settextalignment)(客户端)， 设置文本控件的文本对齐方式<!--by mayexing-->

1. 新增[GetTextAlignment](../接口/自定义UI/UI控件.md#gettextalignment)(客户端)， 获取文本控件的文本对齐方式<!--by mayexing-->

1. 新增[SetTextLinePadding](../接口/自定义UI/UI控件.md#settextlinepadding)(客户端)， 设置文本控件的行间距<!--by mayexing-->

1. 新增[GetTextLinePadding](../接口/自定义UI/UI控件.md#gettextlinepadding)(客户端)， 获取文本控件的行间距<!--by mayexing-->

1. 新增[EnableTextShadow](../接口/自定义UI/UI控件.md#enabletextshadow)(客户端)， 使文本控件显示阴影<!--by mayexing-->

1. 新增[DisableTextShadow](../接口/自定义UI/UI控件.md#disabletextshadow)(客户端)， 关闭文本控件显示阴影<!--by mayexing-->

1. 新增[IsTextShadowEnabled](../接口/自定义UI/UI控件.md#istextshadowenabled)(客户端)， 判断文本控件是否显示阴影<!--by mayexing-->

1. 新增[SetOrientation](../接口/自定义UI/UI控件.md#setorientation)(客户端)， 设置stackPanel的排列方向<!--by mayexing-->

1. 新增[GetOrientation](../接口/自定义UI/UI控件.md#getorientation)(客户端)， 获取stackPanel的排列方向<!--by mayexing-->

1. 新增[SerializeBlockPalette](../接口/方块/方块调色板.md#serializeblockpalette)(客户端/服务端)， 序列化方块调色板中的数据，用于方块调色板在客户端及服务端的事件数据之间传输<!--by xujiarong02-->

1. 新增[DeserializeBlockPalette](../接口/方块/方块调色板.md#deserializeblockpalette)(客户端/服务端)， 反序列化方块调色板数据字典中的数据，用于方块调色板在客户端及服务端的事件数据之间传输<!--by xujiarong02-->

1. 新增[GetBlockCountInBlockPalette](../接口/方块/方块调色板.md#getblockcountinblockpalette)(客户端/服务端)， 获取方块调色板BlockPalette中某个类型的方块的数量<!--by xujiarong02-->

1. 新增[DeleteBlockInBlockPalette](../接口/方块/方块调色板.md#deleteblockinblockpalette)(客户端/服务端)， 删除方块调色板BlockPalette中某个类型的方块<!--by xujiarong02-->

1. 新增[ReplaceBlockInBlockPalette](../接口/方块/方块调色板.md#replaceblockinblockpalette)(客户端/服务端)， 替换方块调色板BlockPalette中某个类型的方块<!--by xujiarong02-->

1. 新增[ReplaceAirByStructureVoid](../接口/方块/方块调色板.md#replaceairbystructurevoid)(客户端/服务端)， 设置是否将方块调色板BlockPalette中所有空气替换为结构空位<!--by xujiarong02-->

1. 新增[GetVolumeOfBlockPalette](../接口/方块/方块调色板.md#getvolumeofblockpalette)(客户端/服务端)， 获取方块调色板BlockPalette所占据的长方体的长宽高<!--by xujiarong02-->

1. 新增[GetLocalPosListOfBlocks](../接口/方块/方块调色板.md#getlocalposlistofblocks)(客户端/服务端)， 获取方块调色板中某种方块的相对位置列表<!--by xujiarong02-->

1. 新增[OnGroundServerEvent](../事件/实体.md#ongroundserverevent)(服务端)， 服务端实体着地事件<!--by xusifan-->

1. 新增[FurnaceBurnFinishedServerEvent](../事件/物品.md#furnaceburnfinishedserverevent)(服务端)， 服务端熔炉烧制触发事件<!--by huangxiaojie03-->

1. 新增[UIContainerItemChangedServerEvent](../事件/物品.md#uicontaineritemchangedserverevent)(服务端)， 新增合成容器物品变化事件<!--by jishaobin-->

1. 新增[ContainerItemChangedServerEvent](../事件/物品.md#containeritemchangedserverevent)(服务端)， 新增容器物品变化事件<!--by jishaobin-->

1. 新增[OnMobHitBlockServerEvent](../事件/实体.md#onmobhitblockserverevent)(服务端)， 生物和方块碰撞事件<!--by gmy-->

1. 新增[HealthChangeBeforeServerEvent](../事件/实体.md#healthchangebeforeserverevent)(服务端)， 生物生命值发生变化之前的事件<!--by gmy-->

1. 新增[EntityDroppedItemServerEvent](../事件/实体.md#entitydroppeditemserverevent)(服务端)， 生物扔出物品时触发的事件<!--by xiegang-->

1. 新增[EntityPickupItemServerEvent](../事件/实体.md#entitypickupitemserverevent)(服务端)， 生物拾取物品时触发的事件（玩家不触发）<!--by xiegang-->

1. 新增[OnPlayerBlockedByShieldBeforeServerEvent](../事件/物品.md#onplayerblockedbyshieldbeforeserverevent)(服务端)， 玩家使用盾牌抵挡伤害之前触发的事件<!--by guanmingyu-->

1. 新增[OnPlayerBlockedByShieldAfterServerEvent](../事件/物品.md#onplayerblockedbyshieldafterserverevent)(服务端)， 玩家使用盾牌抵挡伤害之后触发的事件<!--by guanmingyu-->

1. 新增[OnPlayerActiveShieldServerEvent](../事件/物品.md#onplayeractiveshieldserverevent)(服务端)， 玩家激活盾牌触发的事件<!--by guanmingyu-->

1. 新增[BlockDestroyByLiquidServerEvent](../事件/方块.md#blockdestroybyliquidserverevent)(服务端)， 方块被水流破坏的事件<!--by guanmingyu-->

1. 新增[FarmBlockToDirtBlockServerEvent](../事件/方块.md#farmblocktodirtblockserverevent)(服务端)， 耕地退化为泥土时触发<!--by guanmingyu-->

1. 新增[DirtBlockToGrassBlockServerEvent](../事件/方块.md#dirtblocktograssblockserverevent)(服务端)， 泥土方块变成草方块时触发<!--by guanmingyu-->

1. 新增[GrassBlockToDirtBlockServerEvent](../事件/方块.md#grassblocktodirtblockserverevent)(服务端)， 草方块变成泥土方块时触发<!--by guanmingyu-->

1. 新增[PlayerDoInteractServerEvent](../事件/实体.md#playerdointeractserverevent)(服务端)， 玩家与生物交互时触发的事件<!--by xiegang-->

1. 新增[BlockBreathability](../枚举值/BlockBreathability.md)， 方块的可呼吸性<!--by xusifan-->

1. 新增[ItemCategory](../枚举值/ItemCategory.md)， 物品所属创造栏类型<!--by xusifan-->

1. 新增[RenderControllerArrayType](../枚举值/RenderControllerArrayType.md)， 渲染控制器字典中材质、贴图、模型的枚举值<!--by xiegang01-->

1. 新增[RenderLayer](../枚举值/RenderLayer.md)， 方块渲染时的材质类型<!--by xusifan-->

- 调整

1. 调整[GetLiquidBlock](../接口/世界/方块管理.md#getliquidblock)(服务端)， 增加一下备注<!--by guanmingyu-->

1. 调整[SetAddArea](../接口/世界/地图.md#setaddarea)(服务端)， 新增fill指令说明<!--by jishaobin-->

1. 调整[SetBlockControlAi](../接口/实体/行为.md#setblockcontrolai)(服务端)， 新增是否冻结动作的参数<!--by czh-->

1. 调整[GetEntitiesAround](../接口/世界/地图.md#getentitiesaround)(服务端)， 增加过滤器中subject的说明<!--by jishaobin-->

1. 调整[CraftItemOutputChangeServerEvent](../事件/物品.md#craftitemoutputchangeserverevent)(服务端)， 新增当前界面类型参数<!--by jishaobin-->

示例Demo下载地址：[2.1 Demo](https://g79.gdl.netease.com/2.1DemoV5.zip)。

## 2.2

# 2.2

2022.6.21：版本号（v2.2 BE1.18.0）

包括Mod PC包，手机测试版启动器，和服务器引擎。

- 温馨提示

在6月7日，上线2.2第一个beta版。

在6月21日，上线2.2第二个beta版。

在6月30日，上线2.2的稳定版。

在7月8日，全渠道将更新2.2版本玩家包体，玩家将陆续更新到2.2版本，请开发者合理安排更新节奏。

下载[2.2 Demo](https://g79.gdl.netease.com/2.2BetaDemoV4.zip)。

- 新增重大功能介绍

1. 新增对微软粒子的创建，播放控制和挂接支持，详见[微软粒子](../接口/特效/微软粒子.md)

![微软粒子1](../picture/wrlz.gif)

2. 自定义方块自由模型的每张贴图支持最大64×64，关于自定义方块模型的制作请参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/5-自定义方块模型.html">这篇文档</a>。

3. 方块几何体模型支持门、床、活塞、粘性活塞、告示牌、箱子类方块

![方块合并网格体](../picture/fkhewgt.png)

4. 自定义方块及自定义方块模型的群系颜色，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/2-功能.html#自定义方块及自定义方块模型的群系颜色(2.2beta版本内容)" rel="noopenner"> 这篇文档 </a>

![方块群系](../picture/fkqx.png)

5. 部分UI控件支持属性动画，详见<a href="../../../mcguide/18-界面与交互/19-控件属性动画.html" rel="noopenner"> 这篇文档 </a>。

6. 新增自定义成就系统，支持开发者定义自己的成就事件并展示，详见<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/16-自定义成就系统.html" rel="noopenner">自定义成就</a>

​	![achievementWindow](../picture/achievementWindow.png)

- 特殊说明

自定义维度中，如果使用了群系地貌（netease_biomes目录中定义），则默认使用2d群系规则。

**注：在2.2以及之后的版本，我们对自定义生物的移动流量进行了优化，距离玩家较远的生物会出现瞬移的情况，如果感觉效果较差，可在components手动添加netease:ban_bandwidth_optimization:{}组件来主动关闭此优化**

- 新增

1. 新增[GetRotFromDir](../接口/通用/数学.md#getrotfromdir)(服务端)， 通过玩家当前朝向获取旋转角度<!--by xujiarong-->

1. 新增[GetRotFromDir](../接口/通用/数学.md#getrotfromdir)(客户端)， 通过玩家当前朝向获取旋转角度<!--by xujiarong-->

1. 新增[GetNodeDetailInfo](../接口/自定义UI/自定义成就系统.md#getnodedetailinfo)(服务端)， 获取自定义成就系统的成就节点信息的接口<!--by cxz-->

1. 新增[SetNodeFinish](../接口/自定义UI/自定义成就系统.md#setnodefinish)(服务端)， 设置自定成就系统某个成就节点完成的接口<!--by cxz-->

1. 新增[AddNodeProgress](../接口/自定义UI/自定义成就系统.md#addnodeprogress)(服务端)， 添加自定义成就系统成就节点进度的接口<!--by cxz-->

1. 新增[GetChildrenNode](../接口/自定义UI/自定义成就系统.md#getchildrennode)(服务端)， 获得自定义成就系统中某成就节点的下一级所有孩子节点的接口<!--by cxz-->

1. 新增[LobbyGetAchievementStorage](../接口/成就.md#lobbygetachievementstorage)(服务端)， 获取云成就存储进度的数据接口<!--by cxz-->

1. 新增[LobbySetAchievementStorage](../接口/成就.md#lobbysetachievementstorage)(服务端)， 添加云成就成就进度的数据接口<!--by cxz-->

1. 新增[SetActorBlockGeometryOffset](../接口/方块/方块几何体模型.md#setactorblockgeometryoffset)(客户端)， 设置实体的方块几何体模型的位置偏移。<!--by xujiarong02-->

1. 新增[SetActorBlockGeometryRotation](../接口/方块/方块几何体模型.md#setactorblockgeometryrotation)(客户端)， 设置实体的方块几何体模型的旋转角度。<!--by xujiarong02-->

1. 新增[EnableActorBlockGeometryTransparent](../接口/方块/方块几何体模型.md#enableactorblockgeometrytransparent)(客户端)， 设置是否允许实体的方块几何体模型产生透明度。<!--by xujiarong02-->

1. 新增[SetActorBlockGeometryTransparency](../接口/方块/方块几何体模型.md#setactorblockgeometrytransparency)(客户端)， 设置实体的方块几何体模型的透明度。<!--by xujiarong02-->

1. 新增[Create](../接口/特效/微软粒子.md#create)(客户端)， 创建粒子发射器<!--by dengruitao-->

1. 新增[CreateBindEntity](../接口/特效/微软粒子.md#createbindentity)(客户端)， 创建粒子发射器并绑定实体<!--by dengruitao-->

1. 新增[EmitManually](../接口/特效/微软粒子.md#emitmanually)(客户端)， 手动发射粒子<!--by dengruitao-->

1. 新增[BindEntity](../接口/特效/微软粒子.md#bindentity)(客户端)， 绑定粒子发射器到指定实体<!--by dengruitao-->

1. 新增[Unbind](../接口/特效/微软粒子.md#unbind)(客户端)， 解除粒子发射器绑定<!--by dengruitao-->

1. 新增[SetRelative](../接口/特效/微软粒子.md#setrelative)(客户端)， 设置粒子是否在局部空间进行计算<!--by dengruitao-->

1. 新增[GetBindingID](../接口/特效/微软粒子.md#getbindingid)(客户端)， 获取粒子发射器绑定的目标ID<!--by dengruitao-->

1. 新增[Remove](../接口/特效/微软粒子.md#remove)(客户端)， 销毁指定粒子发射器<!--by dengruitao-->

1. 新增[RemoveByName](../接口/特效/微软粒子.md#removebyname)(客户端)， 销毁所有具有指定identifier的粒子发射器<!--by dengruitao-->

1. 新增[Exist](../接口/特效/微软粒子.md#exist)(客户端)， 判断指定粒子发射器是否存在<!--by dengruitao-->

1. 新增[Play](../接口/特效/微软粒子.md#play)(客户端)， 播放粒子发射器<!--by dengruitao-->

1. 新增[Stop](../接口/特效/微软粒子.md#stop)(客户端)， 停止粒子发射器播放<!--by dengruitao-->

1. 新增[Hide](../接口/特效/微软粒子.md#hide)(客户端)， 隐藏粒子发射器<!--by dengruitao-->

1. 新增[Show](../接口/特效/微软粒子.md#show)(客户端)， 显示粒子发射器<!--by dengruitao-->

1. 新增[Pause](../接口/特效/微软粒子.md#pause)(客户端)， 暂停粒子发射器更新<!--by dengruitao-->

1. 新增[Resume](../接口/特效/微软粒子.md#resume)(客户端)， 恢复粒子发射器更新<!--by dengruitao-->

1. 新增[Replay](../接口/特效/微软粒子.md#replay)(客户端)， 重播粒子发射器<!--by dengruitao-->

1. 新增[PlayAt](../接口/特效/微软粒子.md#playat)(客户端)， 设置粒子发射器播放时间点<!--by dengruitao-->

1. 新增[IsPausing](../接口/特效/微软粒子.md#ispausing)(客户端)， 判断粒子发射器是否被暂停<!--by dengruitao-->

1. 新增[IsHiding](../接口/特效/微软粒子.md#ishiding)(客户端)， 判断粒子发射器是否被隐藏<!--by dengruitao-->

1. 新增[SetPos](../接口/特效/微软粒子.md#setpos)(客户端)， 设置粒子发射器位置<!--by dengruitao-->

1. 新增[GetPos](../接口/特效/微软粒子.md#getpos)(客户端)， 获取粒子发射器位置<!--by dengruitao-->

1. 新增[SetRot](../接口/特效/微软粒子.md#setrot)(客户端)， 设置粒子发射器旋转<!--by dengruitao-->

1. 新增[GetRot](../接口/特效/微软粒子.md#getrot)(客户端)， 获取粒子发射器旋转<!--by dengruitao-->

1. 新增[SetTimeScale](../接口/特效/微软粒子.md#settimescale)(客户端)， 设置粒子发射器播放速度<!--by dengruitao-->

1. 新增[GetTimeScale](../接口/特效/微软粒子.md#gettimescale)(客户端)， 获取粒子发射器播放速度<!--by dengruitao-->

1. 新增[GetDuration](../接口/特效/微软粒子.md#getduration)(客户端)， 获取粒子发射器播放周期<!--by dengruitao-->

1. 新增[GetActiveDuration](../接口/特效/微软粒子.md#getactiveduration)(客户端)， 获取粒子发射器激活周期<!--by dengruitao-->

1. 新增[GetSleepDuration](../接口/特效/微软粒子.md#getsleepduration)(客户端)， 获取粒子发射器休眠周期<!--by dengruitao-->

1. 新增[GetLoopAge](../接口/特效/微软粒子.md#getloopage)(客户端)， 获取粒子发射器周期内已播放时间<!--by dengruitao-->

1. 新增[GetVariable](../接口/特效/微软粒子.md#getvariable)(客户端)， 获取粒子发射器的Molang变量值<!--by dengruitao-->

1. 新增[SetVariable](../接口/特效/微软粒子.md#setvariable)(客户端)， 设置粒子发射器的Molang变量值<!--by dengruitao-->

1. 新增[GetFacingMode](../接口/特效/微软粒子.md#getfacingmode)(客户端)， 返回粒子发射器的粒子朝向模式<!--by dengruitao-->

1. 新增[resetAnimation](../接口/自定义UI/UI控件.md#resetanimation)(客户端)， 重置该控件的动画<!--by panlei-->

1. 新增[SetButtonScreenExitCallback](../接口/自定义UI/UI控件.md#setbuttonscreenexitcallback)(客户端)， 设置按钮所在画布退出时若鼠标仍未抬起时触发回调函数<!--by panlei-->

1. 新增[SetOffsetDelta](../接口/自定义UI/UI控件.md#setoffsetdelta)(客户端)， 设置点击面板的拖拽偏移量<!--by panlei-->

1. 新增[GetOffsetDelta](../接口/自定义UI/UI控件.md#getoffsetdelta)(客户端)， 获得点击面板的拖拽偏移量<!--by panlei-->

1. 新增[OnMobHitMobServerEvent](../事件/实体.md#onmobhitmobserverevent)(服务端)， 生物碰撞事件<!--by wdd-->

1. 新增[OnMobHitMobClientEvent](../事件/实体.md#onmobhitmobclientevent)(客户端)， 生物碰撞事件<!--by wdd-->

- 调整

1. 调整[SetPlayerRideEntity](../接口/玩家/行为.md#setplayerrideentity)(服务端)， 支持骑乘船与矿车<!--by czh-->

1. 调整[SetRiderRideEntity](../接口/实体/行为.md#setriderrideentity)(服务端)， 支持骑乘船与矿车<!--by czh-->

- 废弃（将在未来不可用）

1. 废弃OnPlayerHitMobServerEvent，添加了新事件OnMobHitMobServerEvent代替该事件

1. 废弃OnPlayerHitMobClientEvent，添加了新事件OnMobHitMobClientEvent代替该事件



## 2.3

# 2.3

2022.8.23：版本号（v2.3 BE1.18.0）

包括Mod PC包，手机测试版启动器，和服务器引擎。

- 温馨提示

在8月23日，上线2.3第一个beta版。

在9月6日，上线2.3第二个beta版。

在9月15日，上线2.3的稳定版。

在9月23日，全渠道将更新2.3版本玩家包体，玩家将陆续更新到2.3版本，请开发者合理安排更新节奏。

下载[2.3 Demo](https://g79.gdl.netease.com/2.3DemoV2.zip)。

## 新增重大功能介绍

### 1. 自定义地形高度

新增了2种高度控制节点，开发者可将其配置在群系配置文件中，灵活控制指定群系下不同位置地形的高度。
例如下图就是使用新版的填充节点实现的效果。
详情参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/2-群系地貌.html#5.自定义群系高度（网易版）">这篇文档</a>。

![自定义地形高度1](../picture/zdydxgd1.png)


### 2. 支持骨骼模型挂接微软粒子

详情请见[微软粒子接口](../接口/特效/微软粒子.md#bindmodel)

![微软粒子1](../picture/skeleton_model_with_particle.gif)

### 3. colormap支持对方块指定面生效

详情参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/2-自定义方块/2-功能.html#自定义方块及自定义方块模型的群系颜色">这篇文档</a>。

![corlormap](../picture/colormap.png)

### 4. 实体支持接口设置网格体和贴图

详情见[实体接口](../接口/实体/渲染.md#AddActorGeometry)

![实体设置网格体](../picture/entitysetgeo.png)



## API改动
 
### 新增

1. 新增[PlayHudHeartBlinkAnim](../接口/原生UI.md#playhudheartblinkanim)(客户端)， 播放原版受伤时血量变化的动画<!--by wangjian18-->

2. 新增[SetPlayerUIItem](../接口/方块/容器.md#setplayeruiitem)(服务端)， 设置合成容器的物品<!--by wangdingdong-->

3. 新增[AddActorGeometry](../接口/实体/渲染.md#addactorgeometry)(客户端)， 增加生物渲染几何体<!--by wangdingdong-->

4. 新增[RemoveActorGeometry](../接口/实体/渲染.md#removeactorgeometry)(客户端)， 删除生物渲染几何体<!--by wangdingdong-->

5. 新增[AddActorTexture](../接口/实体/渲染.md#addactortexture)(客户端)， 增加生物渲染贴图<!--by wangdingdong-->

6. 新增[RemoveActorTexture](../接口/实体/渲染.md#removeactortexture)(客户端)， 删除生物渲染贴图<!--by wangdingdong-->

7. 新增[SetPlayerItemInHandVisible](../接口/玩家/渲染.md#setplayeriteminhandvisible)(客户端)， 设置是否隐藏玩家的手持物品模型显示<!--by xujiarong02-->

8. 新增[GetBlockTextures](../接口/方块/渲染.md#getblocktextures)(客户端)， 获取方块的初始贴图信息<!--by wangdingdong-->

9. 新增[SetEmoteSwitch](../接口/原生UI.md#setemoteswitch)(客户端)， 设置表情开关<!--by huangxiaojie03-->

10. 新增[BindModel](../接口/特效/微软粒子.md#bindmodel)(客户端)， 绑定粒子发射器到骨骼模型上<!--by wangdingdong-->

11. 新增[GetBindingModleID](../接口/特效/微软粒子.md#getbindingmodleid)(客户端)， 获取粒子发射器绑定的骨骼模型id<!--by wangdingdong-->

12. 新增[AchievementCompleteEvent](../事件/世界.md#achievementcompleteevent)(服务端)， 玩家完成自定义成就的事件<!--by cxz-->

13. 新增[AddPlayerCreatedClientEvent](../事件/世界.md#addplayercreatedclientevent)(客户端)， 增加客户端其他玩家进入区块AOI后资源加载完成的事件<!--by wdd-->

### 调整

1. 调整[GetPlayerList](../接口/世界/实体管理.md#getplayerlist)(服务端)， 返回列表按照id进行排序<!--by wdd-->

2. 调整[SetAttrValue](../接口/实体/属性.md#setattrvalue)(服务端)， 设置值超过float表示范围时返回False<!--by wangdingdong-->

3. 调整[SetAttrMaxValue](../接口/实体/属性.md#setattrmaxvalue)(服务端)， 设置值超过float表示范围时返回False<!--by wangdingdong-->

4. 调整[RegisterBlockPatterns](../接口/世界/方块组合.md#registerblockpatterns)(服务端)， 已有相同pattern以及defines组合的合成时返回False<!--by wdd-->

5. 调整[SetBlockNew](../接口/世界/方块管理.md#setblocknew)(服务端)， 增加参数isLegacy，默认为False即使用最新版本的aux对应的state<!--by wdd-->

6. 调整[OnPlayerActiveShieldServerEvent](../事件/物品.md#onplayeractiveshieldserverevent)(服务端)， 在潜行状态切换盾牌也会触发该事件<!--by czh-->

7. 调整[StartRidingClientEvent](../事件/实体.md#startridingclientevent)(客户端)， 删除cancel参数，客户端触发事件时，玩家已经上马<!--by xusifan-->

### 废弃（将在未来不可用）

1. 废弃UnDefineEvent，监听自定义事件前不再需要DefineEvent，所以也不再需要使用UnDefineEvent


## 2.4

# 2.4

2022.11.08：版本号（v2.4 BE1.18.0）

包括Mod PC包，手机测试版启动器，和服务器引擎。

### 温馨提示

1. 在10月27日，上线2.4第一个beta版。

2. 在11月8日，上线2.4的稳定版。

3. 在11月25日，全渠道将更新2.4版本玩家包体，玩家将陆续更新到2.4版本，请开发者合理安排更新节奏。


4. 下载[2.4 Demo](https://g79.gdl.netease.com/2.4DemoV4.zip)。

## 重大功能介绍

### 1. 实体&玩家运动器接口

对实体和玩家分别新增了三套不同类型的运动器接口，可用于控制实体玩家的运动轨迹：
1. 轨迹运动器：用于驱动实体、玩家从一点到另一点的直线运动。

![轨迹运动器](../picture/trackmotion.gif)

2. 速度运动器：用于驱动实体、玩家根据初速度和加速度进行匀速/变速运动。

![速度运动器](../picture/velocitymotion.gif)

3. 环绕运动器：用于驱动实体、玩家环绕指定坐标或指定实体运动。

![环绕运动器](../picture/rotatemotion.gif)

详情请参考[实体运动器接口](../接口/实体/行为.md#addentitytrackmotion)和[玩家运动器接口](../接口/玩家/行为.md#addplayertrackmotion)




### 2. 自定义地形高度：增加替换节点
新增了1种高度控制节点：替换节点，开发者可将其配置在群系配置文件中，灵活控制和替换地形中的方块。
例如下图就是使用新版的替换节点实现的效果。

详情参考<a href="../../../mcguide/20-玩法开发/15-自定义游戏内容/4-自定义维度/2-群系地貌.html#5.自定义群系高度（网易版）">这篇文档</a>。

![自定义地形高度1](../picture/custom_height_66.png)


### 3. 原生UI控制接口补充
1. 新增了一系列接口，补充了对原生UI的动态开启/关闭支持,详见接口[原生UI](../接口/原生UI.md)
2. 新增了获取和弹出所有UI堆栈顶的接口，覆盖支持了自定义UI和原生UI两种类型，详见接口[GetTopUI](../接口/自定义UI/通用.md#gettopui)

### 4. UI支持渲染方块网格体
新增了[渲染方块网格体模型接口](../接口/自定义UI/UI控件.md#renderblockgeometrymodel)，支持将方块网格体数据渲染至UI，可配合纸娃娃控件达成拖拽旋转效果。

![渲染网格体](../picture/uimesh.gif)


## API改动

### 新增

1. 新增[HidePauseGUI](../接口/原生UI.md#hidepausegui)(客户端)， 隐藏暂停按钮原生UI<!--by hxj-->

1. 新增[HideChatGUI](../接口/原生UI.md#hidechatgui)(客户端)， 隐藏聊天按钮原生UI<!--by hxj-->

1. 新增[HideReportGUI](../接口/原生UI.md#hidereportgui)(客户端)， 隐藏举报按钮原生UI<!--by hxj-->

1. 新增[HideFoldGUI](../接口/原生UI.md#hidefoldgui)(客户端)， 隐藏下拉按钮原生UI<!--by hxj-->

1. 新增[HideEmoteGUI](../接口/原生UI.md#hideemotegui)(客户端)， 打开表情界面<!--by hxj-->

1. 新增[HideVoiceGUI](../接口/原生UI.md#hidevoicegui)(客户端)， 隐藏语音按钮原生UI<!--by hxj-->

1. 新增[GetTopUI](../接口/自定义UI/通用.md#gettopui)(客户端)， 获取UI堆栈栈顶的UI名称，可获得原生UI也可获得PushScreen生成的UI<!--by cxz-->

1. 新增[PopTopUI](../接口/自定义UI/通用.md#poptopui)(客户端)， 弹出UI堆栈栈顶的UI<!--by cxz-->

1. 新增[OpenPauseGui](../接口/原生UI.md#openpausegui)(客户端)， 打开原版暂停界面<!--by hxj-->

1. 新增[OpenFoldGui](../接口/原生UI.md#openfoldgui)(客户端)， 打开原版下拉界面<!--by hxj-->

1. 新增[OpenVoiceGui](../接口/原生UI.md#openvoicegui)(客户端)， 打开原版语音界面<!--by hxj-->

1. 新增[OpenReportGui](../接口/原生UI.md#openreportgui)(客户端)， 打开原版举报界面<!--by hxj-->

1. 新增[OpenEmoteGui](../接口/原生UI.md#openemotegui)(客户端)， 打开表情界面<!--by hxj-->

1. 新增[AddEntityTrackMotion](../接口/实体/行为.md#addentitytrackmotion)(服务端)， 给实体（不含玩家）添加轨迹运动器<!--by wangdingdong-->

1. 新增[AddEntityVelocityMotion](../接口/实体/行为.md#addentityvelocitymotion)(服务端)， 给实体（不含玩家）添加速度运动器<!--by wangdingdong-->

1. 新增[AddEntityAroundPointMotion](../接口/实体/行为.md#addentityaroundpointmotion)(服务端)， 给实体（不含玩家）添加对点环绕运动器<!--by wangdingdong-->

1. 新增[AddEntityAroundEntityMotion](../接口/实体/行为.md#addentityaroundentitymotion)(服务端)， 给实体（不含玩家）添加对实体环绕运动器<!--by wangdingdong-->

1. 新增[GetEntityMotions](../接口/实体/行为.md#getentitymotions)(服务端)， 获取实体（不含玩家）身上所有运动器<!--by wangdingdong-->

1. 新增[RemoveEntityMotion](../接口/实体/行为.md#removeentitymotion)(服务端)， 移除实体（不含玩家）身上的运动器<!--by wangdingdong-->

1. 新增[StartEntityMotion](../接口/实体/行为.md#startentitymotion)(服务端)， 启动实体（不含玩家）身上的某个运动器<!--by wangdingdong-->

1. 新增[StopEntityMotion](../接口/实体/行为.md#stopentitymotion)(服务端)， 停止实体（不含玩家）身上的某个运动器<!--by wangdingdong-->

1. 新增[AddPlayerTrackMotion](../接口/玩家/行为.md#addplayertrackmotion)(服务端)， 给玩家添加轨迹运动器<!--by wangdingdong-->

1. 新增[AddPlayerVelocityMotion](../接口/玩家/行为.md#addplayervelocitymotion)(服务端)， 给玩家添加速度运动器<!--by wangdingdong-->

1. 新增[AddPlayerAroundPointMotion](../接口/玩家/行为.md#addplayeraroundpointmotion)(服务端)， 给玩家添加对点环绕运动器<!--by wangdingdong-->

1. 新增[AddPlayerAroundEntityMotion](../接口/玩家/行为.md#addplayeraroundentitymotion)(服务端)， 给玩家添加对实体环绕运动器<!--by wangdingdong-->

1. 新增[GetPlayerMotions](../接口/玩家/行为.md#getplayermotions)(服务端)， 获取玩家身上所有运动器<!--by wangdingdong-->

1. 新增[RemovePlayerMotion](../接口/玩家/行为.md#removeplayermotion)(服务端)， 移除玩家身上的运动器<!--by wangdingdong-->

1. 新增[StartPlayerMotion](../接口/玩家/行为.md#startplayermotion)(服务端)， 启动玩家身上的某个运动器<!--by wangdingdong-->

1. 新增[StopPlayerMotion](../接口/玩家/行为.md#stopplayermotion)(服务端)， 停止玩家身上的某个运动器<!--by wangdingdong-->

1. 新增[HideShopGate](../接口/商城.md#hideshopgate)(客户端)， 隐藏网易商城入口<!--by cxz-->

1. 新增[ShowShopGate](../接口/商城.md#showshopgate)(客户端)， 显示网易商城入口<!--by cxz-->

1. 新增[OpenShopWindow](../接口/商城.md#openshopwindow)(客户端)， 打开网易商城窗口<!--by cxz-->

1. 新增[OpenItemDetailWindow](../接口/商城.md#openitemdetailwindow)(客户端)， 打开特定商品的详情界面<!--by cxz-->

1. 新增[CloseShopWindow](../接口/商城.md#closeshopwindow)(客户端)， 关闭网易商城窗口<!--by cxz-->

1. 新增[RenderBlockGeometryModel](../接口/自定义UI/UI控件.md#renderblockgeometrymodel)(客户端)， 渲染网格体模型<!--by jishaobin-->

1. 新增[EntityMotionStartServerEvent](../事件/实体.md#entitymotionstartserverevent)(服务端)， 实体运动器开始事件<!--by wangdingdong-->

1. 新增[EntityMotionStopServerEvent](../事件/实体.md#entitymotionstopserverevent)(服务端)， 实体运动器停止事件<!--by wangdingdong-->

1. 新增[UrgeShipEvent](../事件/UI.md#urgeshipevent)(服务端)， 玩家点击商城催促发货按钮时触发该事件<!--by cxz-->

1. 新增[InputMode](../枚举值/InputMode.md)， 控制器输入模式<!--by cxz-->

1. 新增[UICategory](../枚举值/UICategory.md)， 原生UI类型名<!--by cxz-->

### 调整

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)(服务端)，    新增燃料时间，食物饱食度，食物营养值，武器攻击力，防具防御力字段<!--by huangxiaojie03-->

1. 调整[GetItemBasicInfo](../接口/物品.md#getitembasicinfo)(客户端)，    新增燃料时间，食物饱食度，食物营养值，武器攻击力，防具防御力字段<!--by huangxiaojie03-->

1. 调整[ServerSpawnMobEvent](../事件/世界.md#serverspawnmobevent)(服务端)， 新增entityId返回参数<!--by cxz-->

1. 调整[AddPlayerCreatedClientEvent](../事件/世界.md#addplayercreatedclientevent)(客户端)， 调整事件触发时机，并对localPlayer也起效<!--by wangdingdong-->



