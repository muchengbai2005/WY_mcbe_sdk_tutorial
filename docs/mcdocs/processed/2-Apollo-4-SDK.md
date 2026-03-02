# Apollo 4-SDK

## 目录

- [1-大厅与游戏服事件](#1-大厅与游戏服事件)
- [10-启动器信息API](#10-启动器信息api)
- [2-控制服事件](#2-控制服事件)
- [3-功能服事件](#3-功能服事件)
- [4-控制服API](#4-控制服api)
- [5-功能服API](#5-功能服api)
- [6-大厅与游戏服API](#6-大厅与游戏服api)
- [7-公共API](#7-公共api)
- [8-服务器通信](#8-服务器通信)
- [9-运营指令](#9-运营指令)

---

## 1-大厅与游戏服事件

# <span id="1-大厅与游戏服事件"></span>1-大厅与游戏服事件


事件的定义。

<span id="服务器"></span>
## 服务器

<span id="MasterConnectStatusEvent"></span>
### MasterConnectStatusEvent

- 描述

    master成功连接到当前服务器事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | isConnect | int | 1代表连接建立，0代表连接中断 |
    | serverId | int | 当前lobby/game服务器id |
- 返回值

    无
<span id="MasterForceShutDownEvent"></span>
### MasterForceShutDownEvent

- 描述

    不建议开发者使用，强制关闭当前服务器时会触发本事件
    
- 返回值

    无
<span id="MasterGraceShutDownEvent"></span>
### MasterGraceShutDownEvent

- 描述

    不建议开发者使用，优雅关闭当前服务器时会触发本事件
    
- 返回值

    无
<span id="ServerWillShutDownEvent"></span>
### ServerWillShutDownEvent

- 描述

    不建议开发者使用，游戏即将强制关闭触发本事件。事件回调函数需要好清理和存档工作，同时终止或强制join所有异步线程
    
- 返回值

    无
<span id="ServiceConnectEvent"></span>
### ServiceConnectEvent

- 描述

    service与lobby/game的成功建立连接事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | service的服务器id |
    | serviceType | str | service的服务器类型 |
- 返回值

    无
<span id="ServiceDisconnectEvent"></span>
### ServiceDisconnectEvent

- 描述

    service与lobby/game断开连接事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | service的服务器id |
- 返回值

    无
<span id="ServiceRegisterModuleEvent"></span>
### ServiceRegisterModuleEvent

- 描述

    不建议开发者使用，service向lobby/game注册module
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | service服务器id |
    | moduleName | str | 模块名，是公共配置中module_names中某个module |
- 返回值

    无
<span id="配置"></span>
## 配置

<span id="ReloadCommonConfigEvent"></span>
### ReloadCommonConfigEvent

- 描述

    不建议开发者使用，公共配置发生变化时触发本事件，注意只有与本服相关配置发生变化时才会触发本事件，比如日志等级
    
- 返回值

    无
<span id="玩家"></span>
## 玩家

<span id="MasterResponseTransferFailServerEvent"></span>
### MasterResponseTransferFailServerEvent

- 描述

    转服失败事件，当玩家试图转服时，没有符合条件的目标服务器时抛出此事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid，玩家的唯一标识 |
    | reason | int | 失败的错误码，serverApi.GetMinecraftEnum().TransferServerFailReason |
- 返回值

    无
<span id="MasterResponseTransferSucServerEvent"></span>
### MasterResponseTransferSucServerEvent

- 描述

    转服成功事件，当玩家试图转服时，成功定位到可转服的目标服务器时抛出此事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid，玩家的唯一标识 |
- 返回值

    无
<span id="ServerGetPlayerLockEvent"></span>
### ServerGetPlayerLockEvent

- 描述

    玩家登录到lobby/game过程中，获取玩家在线锁事件。事件触发时，玩家还处于开始登录阶段，
    还没有下载行为包，且没有在地图中出生。在线锁实质是redis中记录的玩家在线信息，redis key格式
    是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |
    | serverId | int | 当前服务器id |
    | proxyId | int | 当前客户端连接的proxy服务器id |
- 返回值

    无
<span id="ServerPlayerBornPosEvent"></span>
### ServerPlayerBornPosEvent

- 描述

    创建玩家对象过程中，设置玩家出生位置时触发本事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | userId | int | 玩家的netease uid |
    | dimensionId | int | 玩家出生dimension，支持修改 |
    | posx | int | 玩家出生位置，支持修改 |
    | posy | int | 玩家出生位置，支持修改 |
    | posz | int | 玩家出生位置，支持修改 |
    | deltax | int | 玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。 |
    | deltay | int | 玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。 |
    | deltaz | int | 玩家motion位置，初始值为存档中的数据。若修改了posx/posy/posz，则建议设置为0。 |
    | rotx | int | 玩家的rot，初始值为存档中的数据，支持修改 |
    | roty | int | 玩家的rot，初始值为存档中的数据，支持修改 |
    | ret | bool | 是否需要修改玩家初始位置，设置为True后其他数据的修改才会生效 |
- 返回值

    无
<span id="ServerReleasePlayerLockEvent"></span>
### ServerReleasePlayerLockEvent

- 描述

    玩家下线过程中，释放在redis中的玩家在线锁事件。事件触发时，客户端同服务端断开了连接，玩
    家数据已经保存到地图，玩家已经不存在于mc的世界中。在线锁实质是redis中记录的玩家在线信息，
    redis key格式是“user:online: + netease uid”，它是个hash表，包含两个hash key:serverid,proxyid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |
- 返回值

    无
<span id="ServerReleasePlayerLockOnShutDownEvent"></span>
### ServerReleasePlayerLockOnShutDownEvent

- 描述

    不建议开发者使用，游戏强制关闭过程中，玩家强制下线时触发本事件。事件回调函数需要释放在redis中的
    玩家的在线锁
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | idx | int | 事件唯一id，回调时返回 |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |
- 返回值

    无
<span id="StoreBuySuccServerEvent"></span>
### StoreBuySuccServerEvent

- 描述

    玩家游戏内购买商品时服务端抛出的事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    无
<span id="queryPlayerDataEvent"></span>
### queryPlayerDataEvent

- 描述

    不建议开发者使用，玩家上线时，引擎读取玩家entity存档数据时触发本事件。
    只有【SetUseDatabaseSave】设置使用数据库存档后，本事件才有效。
    触发本事件，开发者需要从存档中读取玩家entity数据，然后通过【SavePlayerDataResult】
    将修改后玩家entity数据设置回引擎
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | idx | int | 事件唯一id，【QueryPlayerDataResult】会使用到这个id |
    | playerKey | str | 玩家uid字符串，玩家的唯一标识 |
    | dbName | str | 数据库存档的前缀，可以通过【SetUseDatabaseSave】设置dbname |
- 返回值

    无
<span id="savePlayerDataEvent"></span>
### savePlayerDataEvent

- 描述

    保存玩家数据事件，玩家下线时也会触发该事件。只有【SetUseDatabaseSave】 设置
    useDatabase为True时，本事件才生效。本事件的回调函数
    必须调用【SavePlayerDataResult】函数，把存档状态告知引擎
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | idx | int | 引擎回调函数id，【SavePlayerDataResult】会使用这个id |
    | playerKey | str | 玩家uid字符串，玩家的唯一标识 |
- 返回值

    无
<span id="savePlayerDataOnShutDownEvent"></span>
### savePlayerDataOnShutDownEvent

- 描述

    游戏强制关闭过程中，玩家下线时会触发本事件。另外，只有【SetUseDatabaseSave】 设置
    useDatabase为True时，本事件才生效。本事件的回调函数必须调用
    【SavePlayerDataResult】函数，把存档状态告知引擎
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | idx | int | 引擎回调函数id，【SavePlayerDataResult】函数会使用这个id |
    | playerKey | str | 玩家uid字符串，玩家的唯一标识 |
- 返回值

    无

## 10-启动器信息API

# <span id="启动器信息API"></span>启动器信息API

下面获取启动器信息的接口

<span id="玩家"></span>
### 玩家

<span id="ApplyUserFriend"></span>
#### ApplyUserFriend

- 描述

    **Lobby/Game接口**，申请添加为启动器中的好友
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | requestUID | int | 玩家的uid |
    | appliedUID | int | 被申请添加好友玩家的uid |
    | message | str | 申请的好友的描述信息 |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段b_success，b_success表示申请是否成功。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #申请成功返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_success': true}}
        #申请失败返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_success': false}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.ApplyUserFriend(123, 456, '我想加个好友', callback)
 ```
<span id="GetPcGameUserLike"></span>
#### GetPcGameUserLike

- 描述

    **Master/Service/Lobby/Game接口**，获取玩家是否点赞了当前网络服（仅支持PC玩家）
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的pc uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段is_like，值为bool，表示玩家是否点赞 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'is_like': True}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetPeGameUserStars(123, callback)
 ```
<span id="GetPeGameUserStars"></span>
#### GetPeGameUserStars

- 描述

    **Master/Service/Lobby/Game接口**，获取玩家对本游戏的评分
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段stars，表示玩家评分，评分正常范围为1-5，值为-1表示没有评分数据。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'stars': 1}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetPeGameUserStars(123, callback)
 ```
<span id="GetUIDByNickname"></span>
#### GetUIDByNickname

- 描述

    **Master/Service/Lobby/Game接口**，根据玩家昵称获取玩家uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | nickname | str | 玩家昵称，要求是utf8编码 |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段uid，表示玩家的uid。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'uid': 2147583768}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUIDByNickname('我的昵称', callback)
 ```
<span id="GetUserAuthInfo"></span>
#### GetUserAuthInfo

- 描述

    **Master/Service/Lobby/Game接口**，获取在线玩家实名制、是否绑定信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含下面字段：b_real_name表示玩家是否实名制,        id_hash表示玩家身份的唯一标识，未实名时为空（多个账号可以绑定到一个身份证，可以通过这个字段判断多个账号是否绑定到一个身份），        b_bind_phone表示玩家是否绑定手机 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例，玩家实名认证且绑定手机:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_real_name': True, u'id_hash':u'92251e8665e19be62c86ff039528e16e', u'b_bind_phone':True}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUserAuthInfo(123, callback)
 ```
<span id="GetUserFriend"></span>
#### GetUserFriend

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家好友信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段friend_uids，friend_uids对应内容是个list，对应好友玩家uid列表。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'friend_uids': [234,456]}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUserFriend(123, callback)
 ```
<span id="GetUserGuest"></span>
#### GetUserGuest

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家是否游客的信息, 此接口已废弃
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段guest，表示玩家是否游客，字段意义 0：非游客，1：游客，2：不确定。 |
- 返回值

    无
- 备注

    除了官网渠道和苹果渠道之外，其他第三方渠道启动器无法返回确定的游客信息，guest字段返回2
    
    此接口已废弃
    
    
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'guest': 1}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUserGuest(123, callback)
 ```
<span id="GetUsersVIP"></span>
#### GetUsersVIP

- 描述

    **Master/Service/Lobby/Game接口**，获取启动器中玩家会员信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uids | list(int/long) | 玩家的uid列表，列表长度不超过20 |
    | callback | function | 回调函数，该函数会被异步执行。函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；        "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段users_vip，users_vip对应内容是个dict，key表示玩家uid，value表示是否是vip。 |
- 返回值

    无
- 备注

    只能获取体验过本游戏玩家会员信息。要求在MCStudio中配置游戏ID（路径：服务器配置->更多->游戏ID）
    
    
- 示例

```python
def callback(response):
        #正常返回示例:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'users_vip': {u'123': True}}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.GetUsersVIP([123], callback)
 ```
<span id="IsGameUnderMaintenance"></span>
#### IsGameUnderMaintenance

- 描述

    **Master/Service/Lobby/Game接口**，游戏是否在维护中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | callback | function | 回调函数，函数只有一个dict类型参数。dict说明："code":状态码，0表示正确，其他表示失败；      "message"状态信息;"details"：状态的详细信息，为空字符串;"entity"：是个字典，包含字段b_maintain，表示玩家的是否维护中。 |
- 返回值

    无
- 示例

```python
def callback(response):
        #正常返回示例，游戏维护中:{u'message': '正常返回', u'code': 0, u'details': u'', u'entity': {u'b_maintain': True}}
        #错误返回示例:{u'message': '参数错误', u'code': 1, u'details': u'', u'entity': ''}
        print 'callback', response
import apolloCommon.launcherApi as launcherApi
launcherApi.IsGameUnderMaintenance(callback)
 ```
<span id="ShareApolloGame"></span>
#### ShareApolloGame

- 描述

    **Lobby/Game接口**，在RN上拉起“网络游戏分享”的界面，界面包含游戏ICON以及描述
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
    | message | str | 分享的描述信息，不能超过20个字符，要求传入utf8字符串 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 拉起分享界面是否成功。False：存在敏感词或游戏ID为0或玩家不在线或分享信息超过20个字符 |
- 备注

    此函数只能在大厅服和游戏服中调用，不支持功能服和控制服环境
    
    此函数仅支持在手机端登录的玩家
    
    
- 示例

```python
import apolloCommon.launcherApi as launcherApi
# 注意要求传入utf8字符串
ret = launcherApi.ShareApolloGame(123, u'这款游戏挺不错的，大家试试')
 ```

## 2-控制服事件

# <span id="2-控制服事件"></span>2-控制服事件


事件的定义。

<span id="服务器"></span>
## 服务器

<span id="ResetGamesBeginEvent"></span>
### ResetGamesBeginEvent

- 描述

    开始重置lobby/game事件。具体可以参见API【ResetServer】
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    无
<span id="ResetGamesEndEvent"></span>
### ResetGamesEndEvent

- 描述

    重置lobby/game结束事件。本事件只是表示重置完成了，但是服务器可能还未完成初始化。具体可以参见API【ResetServer】
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
    | bSuccess | bool | 重置是否成功。true表示重置成功，否则表示失败 |
- 返回值

    无
<span id="RollingCloseServersEndEvent"></span>
### RollingCloseServersEndEvent

- 描述

    使用RollingCloseServersEndEvent滚动关服结束事件。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | request | str | 滚动关服的请求参数，为json格式字符串，包含以下属性：serverlist，serverIds，apolloid，apollo_key |
    | response | str | 滚动关服的返回参数，为json格式字符串，包含以下属性：code错误码，message错误信息，entity移除的服务器信息，其中字段与RollingUpdateServersEndEvent相同 |
    | suc | bool | 滚动关服是否成功 |
- 返回值

    无
<span id="RollingUpdateServersEndEvent"></span>
### RollingUpdateServersEndEvent

- 描述

    使用RollingUpdateServers滚动更新服务器结束事件。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | request | str | 滚动更新的请求参数，为json格式字符串，包含以下属性：app_version，ip，server_type，add_num，apolloid，apollo_key |
    | response | str | 滚动更新的返回参数，为json格式字符串，包含以下属性：code错误码，message错误信息，entity新增或移除的服务器信息 |
    | suc | bool | 滚动更新是否成功 |
- 返回值

    无
- 备注

    entity为一个list(dict)，每个元素包含以下字段，对应mcstudio的服务器配置：
    | 字段 | 类型 | 说明 |
    | --- | --- | --- |
    | serverid | int | 服务器id |
    | ip | str | 服务器ip |
    | mods | str | 服务器mod列表 |
    | app_type | str | game/lobby/proxy |
    | type | str | 服务器类型 |
    | save | bool | 是否保存地图 |
    | save_id | int | 使用地图 |
    | gb | int | 单进程内存 |
    
    
<span id="ServerConnectedEvent"></span>
### ServerConnectedEvent

- 描述

    lobby/game/proxy成功建立连接时触发
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
    | protocolVersion | int | 协议版本号 |
- 返回值

    无
<span id="ServerDisconnectEvent"></span>
### ServerDisconnectEvent

- 描述

    lobby/game/proxy断开连接时触发
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    无
<span id="配置"></span>
## 配置

<span id="NetGameCommonConfChangeEvent"></span>
### NetGameCommonConfChangeEvent

- 描述

    公共配置发生变化时触发，具体包括：新增或删服服务器；服务器相关配置变化；日志等级发生变化
    
- 返回值

    无
<span id="玩家"></span>
## 玩家

<span id="PlayerLoginServerEvent"></span>
### PlayerLoginServerEvent

- 描述

    玩家开始登陆事件，此时master开始给玩家分配lobby/game，可以区分玩家是登录还是切服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 客户端即将登录的服务器id |
    | uid | int/long | 玩家的uid |
    | protocolVersion | int | 协议版本号 |
    | isTransfer | bool | True: 切服，False：登录 |
    | isReconnect | bool | True: 断线重连，False：正常登录 |
    | isPeUser | bool | True: 玩家从手机端登录，False：玩家从PC端登录 |
- 返回值

    无
<span id="PlayerLogoutServerEvent"></span>
### PlayerLogoutServerEvent

- 描述

    玩家登出时触发，玩家在lobby/game下载行为包的过程中退出也会触发该事件，可以以区分玩家是登出还是切服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 客户端连接的proxy服务器id |
    | uid | int/long | 玩家的uid |
    | isTransfer | bool | True: 切服，False：登出 |
- 返回值

    无
<span id="PlayerTransferServerEvent"></span>
### PlayerTransferServerEvent

- 描述

    玩家开始切服事件，此时master开始为玩家准备服务器，玩家还没切服完毕，后续可能切服失败
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 客户端连接的proxy服务器id |
    | uid | int/long | 玩家的uid |
    | targetServerId | int | 目标lobby/game服务器id |
    | targetServerType | str | 目标服务器类型，比如"game"或"lobby"。若targetServerId为0，则会从目标类型的多个服务器中随机选一个，作为目标服务器 |
    | protocolVersion | int | 协议版本号 |
    | transferParam | str | 切服参数。调用【TransferToOtherServer】或【TransferToOtherServerById】传入的切服参数。 |
- 返回值

    无

## 3-功能服事件

# <span id="3-功能服事件"></span>3-功能服事件


事件的定义。

<span id="服务器"></span>
## 服务器

<span id="ServerConnectedEvent"></span>
### ServerConnectedEvent

- 描述

    lobby/game/proxy成功建立连接时触发
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
    | protocolVersion | int | 协议版本号 |
- 返回值

    无
<span id="ServerDisconnectEvent"></span>
### ServerDisconnectEvent

- 描述

    lobby/game/proxy断开连接时触发
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    无
<span id="UpdateServerStatusEvent"></span>
### UpdateServerStatusEvent

- 描述

    lobby/game/proxy状态发生变化时触发
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dict类型，key：str，服务器id的字符串，value：str，服务器状态字符串。服务器状态如下：‘1’ | 就绪状态，‘2’ | 停止状态，‘3’ 准备状态。服务器状态为'1'时，服务器才可用，其他状态下，服务器不可用。 |
- 返回值

    无
- 示例

```python
class TestService(ServiceSystem):
        def __init__(self, namespace, systemName):
        ServiceSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(
                serviceApi.GetEngineNamespace(),
                serviceApi.GetEngineSystemName(),
                "UpdateServerStatusEvent",
                self,
                self.OnUpdateServerStatusEvent)
  def OnUpdateServerStatusEvent(self, args):
          print args
          # 结果的一个示例:{'1000000':'1', '2000000':'3'}
          # 含义：服务器id为1000000的服务器正常运行，服务器id为2000000的服务器处于准备状态。
 ```
<span id="配置"></span>
## 配置

<span id="NetGameCommonConfChangeEvent"></span>
### NetGameCommonConfChangeEvent

- 描述

    服务器配置发生变化时触发，具体包括：新增或删服服务器；服务器相关配置变化；日志等级发生变化
    
- 返回值

    无

## 4-控制服API

# <span id="4-控制服API"></span>4-控制服API

这里是一些Master的基础API接口。

<span id="配置"></span>
### 配置

<span id="GetCommonConfig"></span>
#### GetCommonConfig

- 描述

    获取服务器公共配置，包括所有服务器和db的配置，具体参见备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 配置内容 |
- 备注

    服务器公共配置的示例如下，只展示了核心配置信息：
    ```
    {
    "apolloid":111,
    "extra_redis":{
    },
    "game_id":0,
    "game_key":"game_key",
    "gas_server_url":"http://127.0.0.1:111",
    "log_debug_level":true,
    "master":{
    "app_type":"master",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "keep_alive_period":30,
    "master_port":0,
    "mods":"",
    "port":8000,
    "serverid":0,
    "type":"master"
    },
    "mongo":null,
    "mysql":{
    "database":"test_db",
    "host":"127.0.0.1",
    "password":"test_password",
    "port":3306,
    "user":"test_user"
    },
    "redis":{
    "host":"127.0.0.1",
    "password":"",
    "port":6379
    },
    "review_stage":0,
    "serverlist":[
    {
    "app_type":"proxy",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":11003,
    "max_players":0,
    "mods":"",
    "optimum_players":0,
    "port":11002,
    "save":false,
    "serverid":2000,
    "type":"proxy"
    },
    {
    "app_type":"lobby",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":13003,
    "max_players":200,
    "mods":"neteaseRound",
    "optimum_players":0,
    "port":13002,
    "save":false,
    "serverid":4000,
    "type":"lobby"
    }
    ],
    "servicelist":[
    ],
    }
    ```
    
    
- 示例

```python
import master.netgameApi as netMasterApi
conf = netMasterApi.GetCommonConfig()
serverlist = conf['serverlist'] #获取serverlist配置
bDebugLevel = conf['log_debug_level'] #获取日志等级配置
 ```
<span id="GetGameTypeByServerId"></span>
#### GetGameTypeByServerId

- 描述

    获取指定ID服务器的类型
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器ID |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | None或str | 指定ID的服务器的类型，没有符合条件的服务器时返回None |
- 示例

```python
import master.netgameApi as netMasterApi
gameType = netMasterApi.GetGameTypeByServerId(6000)
 ```
<span id="GetServerIdsByGameType"></span>
#### GetServerIdsByGameType

- 描述

    获取指定类型的服务器id列表
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | gameType | str | 服务器类型名 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(int) | 指定类型的服务器ID的列表，没有符合条件的服务器时返回空列表 |
- 示例

```python
import master.netgameApi as netMasterApi
idList = netMasterApi.GetServerIdsByGameType("gameA")
 ```
<span id="GetServerLoadedModsById"></span>
#### GetServerLoadedModsById

- 描述

    根据服务器id获取服务器加载mod列表
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id，id为0表示master |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(str) | 服务器mod列表 |
- 示例

```python
import master.netgameApi as netMasterApi
#返回的一个示例：["neteaseAnnounce", "neteaseAuth", "neteaseShop"]
mods = netMasterApi.GetServerLoadedModsById(4000)
 ```
<span id="GetServerLoadedModsByType"></span>
#### GetServerLoadedModsByType

- 描述

    根据服务器类型获取服务器加载mod列表。若同种类型服务器配置了不同的mod，则返回其中一个对应mod列表。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(str) | 服务器mod列表 |
- 示例

```python
import master.netgameApi as netMasterApi
#返回的一个示例：["neteaseAnnounce", "neteaseAuth", "neteaseShop"]
mods = netMasterApi.GetServerLoadedModsByType("survivalGame")
 ```
<span id="IsService"></span>
#### IsService

- 描述

    服务器是否是service服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True表示是service，False不是service |
- 备注

    本api取代【masterConf.isService】，【masterConf.isService】废弃。
    
    
- 示例

```python
import master.netgameApi as netMasterApi
bService = netMasterApi.IsService(10)
 ```
<span id="玩家"></span>
### 玩家

<span id="BanUser"></span>
#### BanUser

- 描述

    封禁某个玩家
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
    | banTime | int | 封禁时间，单位为秒，-1表示永封 |
    | reason | str | 封禁原因，使用utf8编码 |
    | bCombineReason | bool | 是否组合显示封禁原因。若为True，则按备注说明处理，否则被封禁玩家登陆会提示【reason】 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 备注

    效果说明如下：
    
    若banTime>0，则被封禁玩家登陆会提示：您的账号已经被封禁，剩余封禁时间：x天y小时z分，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    
    若banTime=-1，则被封禁玩家登陆会提示：您的账号已经被永久封禁，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    
    
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456，被封禁86400秒，登陆链提示：您的账号已经被封禁，剩余封禁时间：1天0小时0分，封禁原因：作弊被封禁一天
netMasterApi.BanUser(123456, 86400, '作弊被封禁一天', True)
#玩家123457，被封禁86400秒，登陆链提示：作弊被封禁一天
netMasterApi.BanUser(123457, 86400, '作弊被封禁一天', False)
 ```
<span id="GetBanUserInfo"></span>
#### GetBanUserInfo

- 描述

    获取玩家的封禁信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
    | callback | function | 回调函数，包含两个参数：第一个参数是uid；第二个参数是封禁信息，若获取失败，则为None，若没有被封禁则为“{}”，若被封禁，则为dict，解释参见备注 |
- 返回值

    无
- 备注

    callback中的第二个dict参数内容解释如下：
    
    | 关键字     | 数据类型              | 说明     |
    | ----------| --------------------- | ---------|
    | banTime | int | 封禁持续时间，单位是秒，-1表示永久封禁|
    | banTimestamp | int | 开始封禁的时间戳，若不是永久封禁，则截止时间为：banTimestamp + banTime |
    | reason | str | 封禁原因 |
    
    
    
    
- 示例

```python
import master.netgameApi as netMasterApi
def cb(uid, info):
        #若被封禁返回示例：result 123456 {banTime：10, banTimestamp: 1623325971, reason:"作弊"}
        #若未被封禁返回示例： result 123456 {}
        print 'result', uid, info
netMasterApi.GetBanUserInfo(123456, cb)
 ```
<span id="GetOnlineUidList"></span>
#### GetOnlineUidList

- 描述

    获取所有在线玩家的uid列表
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(int) | 在线玩家的uid列表，当没有玩家在线时返回空列表 |
- 备注

    在线玩家的uid列表是缓存再内存中的，档Master意外dump重启之后，只能获取到重启后再登录的玩家的uid
    
    此接口返回的uid列表可能会很大，不建议在正式环境使用
    
    
- 示例

```python
import master.netgameApi as netMasterApi
uidList = netMasterApi.GetOnlineUidList()
 ```
<span id="GetProtocolVersionByUID"></span>
#### GetProtocolVersionByUID

- 描述

    获取在线玩家客户端协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的UID |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | None或者int | 玩家在线时，返回此玩家客户端协议版本号，玩家不在线时返回None |
- 示例

```python
import master.netgameApi as netMasterApi
protocolVersion = netMasterApi.GetProtocolVersionByUID(123456)
 ```
<span id="GetServerIdByUid"></span>
#### GetServerIdByUid

- 描述

    获取在线玩家所在的服务器的ID，返回的信息为当前控制服内存缓存中的信息，玩家很可能很快就离线或者转服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 需要获取的玩家的UID |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | None或者int | 玩家在线时，返回此玩家当前所在的服务器ID，玩家不在线时返回None |
- 备注

    玩家与当前所在服务器ID的映射关系是缓存在内存中的，当Master意外dump重启之后，只能获取到重启后再登录的玩家当前所在的服务器ID
    
    
- 示例

```python
import master.netgameApi as netMasterApi
serverId = netMasterApi.GetServerIdByUid(123456)
 ```
<span id="GetUserSilentInfo"></span>
#### GetUserSilentInfo

- 描述

    获取玩家的禁言信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
    | callback | function | 回调函数，包含两个参数：第一个参数是uid；第二个参数是禁言信息，若获取失败，则为None，若没有被禁言则为“{}”，若被禁言，则为dict，解释如下： |
- 返回值

    无
- 备注

    callback中的第二个dict参数内容解释如下：
    
    | 关键字     | 数据类型              | 说明     |
    | ----------| --------------------- | ---------|
    | banTime | int | 禁言持续时间，单位是秒，-1表示永久禁言|
    | banTimestamp | int | 开始禁言的时间戳，若不是永久禁言，则截止时间为：banTimestamp + banTime |
    | reason | str | 禁言原因 |
    
    
    
    
- 示例

```python
import master.netgameApi as netMasterApi
def cb(uid, info):
        #若被禁言返回示例：result 123456 {banTime：10, banTimestamp: 1623325971, reason:"谈论敏感话题"}
        #若未被禁言返回示例： result 123456 {}
        print 'result', uid, info
netMasterApi.GetUserSilentInfo(123456, cb)
 ```
<span id="SetLoginStratege"></span>
#### SetLoginStratege

- 描述

    设置玩家登陆选服策略，要求服务器启动后加载mod时候设置
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | func | function | 计算玩家登陆服务器，包含两个参数：第一个参数为玩家uid；第二个参数为回调函数，执行后续登陆逻辑，无论登陆是否成功，必须要执行，回调函数只有一个参数，也即目标服务器。 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 备注

    示例中提供了两种设置登陆策略方法，示例1是方便开发者理解接口，最好不要应用于生产环境，示例2是生产环境使用方法
    
    调用此API修改选服策略之后，配置的单服最高人数限制会失效，选服策略需要考虑单服的承载力与玩家人数平衡问题，但配置的全服最高人数限制不会失效
    
    
- 示例

```python
#示例1，不考虑滚动更新，设置固定目标服务器
def loginStratege(uid, callback):
        targetId = 20000 #登陆到id为20000的服务器
        callback(targetId) #必须执行，执行登陆后续操作
import master.netgameApi as netMasterApi
netMasterApi.SetLoginStratege(loginStratege)
#示例2，考虑滚动更新，滚动更新过程中服务器id会发生变化，因此需要提供机制，确保目标服务器的有效性
#master mod
class testMaster(MasterSystem):
        def __init__(self,namespace,systemName):
                MasterSystem.__init__(self, namespace, systemName)
                self.mTargetServerIds = [] #包含有效的目标服务器id列表
                def loginStratege(uid, callback):
                        targetId = random.choice(self.mTargetServerIds) #选择目标服务器
                        if not serverManager.IsValidServer(targetId):#检查目标服务器是否有效。因为滚动更新过程中，服务器会慢慢下线，处于无效状态
                                #若发现有无效服务器，则过滤掉所有无效服务器，然后重新选择目标服务器
                                self.mTargetServerIds = [server for server in self.mTargetServerIds if serverManager.IsValidServer(server)]
                                targetId = random.choice(self.mTargetServerIds)
                        callback(targetId) #必须执行，执行登陆后续操作
                netMasterApi.SetLoginStratege(loginStratege)
                self.ListenForEvent('lobbyNameaspace', 'lobbySystem', 'NewLoginServerEvent', self, self.OnNewLoginServer)
        
        def OnNewLoginServer(self, args):
                # 将有效目标服务器记录下来
                serverId = args['serverId]
                if serverId not in self.mTargetServerIds:
                        self.mTargetServerIds.append(serverId)
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'MasterConnectStatusEvent', self,
                        self.OnMasterConnectStatus)
        def OnMasterConnectStatus(self, args):
                # 同master建立连接后，马上向master注册为有效服务器
                if args['isConnect']:
                        data = {'serverId' : lobbyGameApi.GetServerId()}
                        self.NotifyToMaster('NewLoginServerEvent', data)
 ```
<span id="SilentByUID"></span>
#### SilentByUID

- 描述

    禁言某个玩家
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
    | banTime | int | 禁言时间，单位为秒，-1表示永封 |
    | reason | str | 禁言原因，使用utf8编码 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456被禁言，禁言86400秒，禁言原因“说了敏感内容，被禁言一天”
netMasterApi.SilentByUID(123456, 86400, '说了敏感内容，被禁言一天')
 ```
<span id="UnBanUser"></span>
#### UnBanUser

- 描述

    解除某个玩家的封禁
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456解除封禁
netMasterApi.UnBanUser(123456)
 ```
<span id="UnSilentByUID"></span>
#### UnSilentByUID

- 描述

    解除某个玩家的禁言
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True设置成功，False表示失败。失败后请延迟一帧后重试 |
- 示例

```python
import master.netgameApi as netMasterApi
#玩家123456被解除禁言
netMasterApi.UnSilentByUID(123456)
 ```
这里是Master的Http接口

<span id="HTTP服务器"></span>
### HTTP服务器

<span id="RegisterMasterHttp"></span>
#### RegisterMasterHttp

- 描述

    注册一个新的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
    | binder | instance | 响应HTTP请求的实例 |
    | func | function | 响应HTTP请求的实例函数 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                masterHttp.RegisterMasterHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，SendHttpResponse中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果。code必须为1表示处理成功，否则service请求时会认为请求失败。
                response = '{"code":1,"message":"ok"}'
                masterHttp.SendHttpResponse(clientId, response)
 ```
<span id="SendHttpRequestToService"></span>
#### SendHttpRequestToService

- 描述

    给service发送http请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | service的服务器id |
    | requestUrl | str | 请求url，例如“/test-reqeust” |
    | body | str | HTTP post body，是个json字符串 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
params = {
        "message":"content",
        "code":1
 }
url = "/test-reqeust"
masterHttp.SendHttpRequestToService(8000, url, json.dumps(params))
 ```
<span id="SendHttpResponse"></span>
#### SendHttpResponse

- 描述

    发送HTTP的Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | message | str | HTTP Response的内容 |
- 返回值

    无
- 示例

```python
import json
import master.masterHttp as masterHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                masterHttp.RegisterMasterHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，SendHttpResponse中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果
                response = '{"code":0,"message":"ok"}'
                masterHttp.SendHttpResponse(clientId, response)
 ```
这里是master关于服务器管理的一些接口

<span id="服务器管理"></span>
### 服务器管理

<span id="GetAllResetingServers"></span>
#### GetAllResetingServers

- 描述

    获取所有重置中服务器的id列表
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(int) | 服务器id列表 |
- 示例

```python
import master.serverManager as serverManager
servers = serverManager.GetAllResetingServers()
 ```
<span id="GetAllServerStatus"></span>
#### GetAllServerStatus

- 描述

    获取所有服务器的状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务。
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | key:int类型，服务器id，value:int类型，服务器状态。服务器状态如下：<br/> 1:断开连接状态<br/>2:已连接状态<br/> 3:关服状态<br/>4:优雅关服状态<br/>6, 滚动更新中间状态，即将转换到状态7<br/>7 也是滚动更新中间状态，即将转换到状态1或2 |
- 备注

    服务器状态中，2表示正常服务，其他表示不能正常服务。
    
    
- 示例

```python
import master.serverManager as serverManager
statusDict = serverManager.GetAllServerStatus()
 ```
<span id="GetAllServersOnlineNum"></span>
#### GetAllServersOnlineNum

- 描述

    获取所有服务器的在线人数
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | key，int类型，表示服务器id，value，int类型，表示服务器在线人数 |
- 示例

```python
import master.serverManager as serverManager
onlineDict = serverManager.GetAllServersOnlineNum()
 ```
<span id="GetConnectedLobbyAndGameIds"></span>
#### GetConnectedLobbyAndGameIds

- 描述

    获取所有已经连接的lobby/game的服务器id列表
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list | 服务器id列表，服务器id是int类型。 |
- 示例

```python
import master.serverManager as serverManager
idList = serverManager.GetConnectedLobbyAndGameIds()
 ```
<span id="GetOneServerStatus"></span>
#### GetOneServerStatus

- 描述

    获取服务器状态。只有状态2表示服务器正常服务，其他状态表示服务器不能服务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务器状态。服务器状态如下：<br/> 1:断开连接状态<br/>2:已连接状态<br/> 3:关服状态<br/>4:优雅关服状态<br/>6, 滚动更新中间状态，即将转换到状态7<br/>7 也是滚动更新中间状态，即将转换到状态1或2 |
- 示例

```python
import master.serverManager as serverManager
status = serverManager.GetOneServerStatus(6000)
 ```
<span id="GetOnlineNumByServerId"></span>
#### GetOnlineNumByServerId

- 描述

    获取服务器(lobby/game/proxy)的在线人数
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetOnlineNumByServerId(4000)
 ```
<span id="GetOnlineNumByServerType"></span>
#### GetOnlineNumByServerType

- 描述

    获取某类型服务器的在线人数
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型，支持代理服/大厅服/游戏服的游戏类型（具体查看studio游戏配置中“类型”配置） |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetOnlineNumByServerType("lobby")
 ```
<span id="GetServerProtocolVersion"></span>
#### GetServerProtocolVersion

- 描述

    获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 协议版本 |
- 示例

```python
import master.serverManager as serverManager
version = serverManager.GetServerProtocolVersion(4000)
 ```
<span id="GetTotalOnlineNum"></span>
#### GetTotalOnlineNum

- 描述

    获取总得在线人数
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 在线人数 |
- 示例

```python
import master.serverManager as serverManager
num = serverManager.GetTotalOnlineNum()
 ```
<span id="IsConnectedServer"></span>
#### IsConnectedServer

- 描述

    master是否与lobby/game/proxy建立连接
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，已经建立连接;False未建立连接 |
- 示例

```python
import master.serverManager as serverManager
bConnect = serverManager.IsConnectedServer(4000)
 ```
<span id="IsValidServer"></span>
#### IsValidServer

- 描述

    服务器是否有效。一种用途：master将玩家分配到服务器之前，会检查服务器是否有效，避免把玩家分配到一个即将关闭的服务器中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，master已经同服务器建立链接，且服务器正在提供服务，不是即将关闭的服务。 |
- 示例

```python
import master.serverManager as serverManager
bValid = serverManager.IsValidServer(4000)
 ```
<span id="ResetServer"></span>
#### ResetServer

- 描述

    重置某个lobby/game。它会将服务器地图恢复到启动时状态并重启服务器。开始重置会触发ResetGamesBeginEvent事件，重置结束会触发ResetGamesEndEvent事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game的服务器id |
- 返回值

    无
- 备注

    
    注意，对于生存服，若使用了存档A，则重置后仍使用存档A，且重置过程中不会保存地图。
    
    
    若需要重置游戏服GameA，使用方法：重置前确保玩家退出对应GameA，重置过程不允许玩家进入GameA，GameA重置完毕后GameA可以发消息告知master或service，告知GameA就绪，然后玩家可以进入GameA了
    
    
- 示例

```python
import master.serverManager as serverManager
serverManager.ResetServer(4000)
 ```
<span id="RollingCloseServers"></span>
#### RollingCloseServers

- 描述

    滚动关服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverIds | list(int) | 服务器id列表 |
- 返回值

    无
- 示例

```python
import master.serverManager as serverManager
serverManager.RollingCloseServers([6000])
 ```
<span id="RollingUpdateServers"></span>
#### RollingUpdateServers

- 描述

    滚动更新服务器，要求网络服使用了这个ip，要求至少存在一个服务器类型为serverType、引擎版本为appVersion的服务器在运行，只能滚动更新代理服/大厅服/游戏服
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型，支持代理服/大厅服/游戏服的游戏类型（具体查看studio游戏配置中“类型”配置） |
    | appVersion | str | 引擎app_verion |
    | ip | str | 服务器ip |
    | addNum | int | 新增数量，可以是负数 |
- 返回值

    无
- 示例

```python
import master.serverManager as serverManager
serverManager.RollingUpdateServers('lobby', '2.0.0.release20220120', '10.0.0.1', 1)
 ```
<span id="StopServerByServerid"></span>
#### StopServerByServerid

- 描述

    关闭某个服务器。若MCStudio配置网络游戏时设置了“崩溃自动拉起”，则关闭服务器后会被自动拉起，实现重启功能
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | proxy/lobby/game服务器id |
    | actType | int | 1:强制踢出所有玩家后关服;2:等待所有玩家退出后关服 |
- 返回值

    无
- 示例

```python
import master.serverManager as serverManager
serverManager.StopServerByServerid(4000, 2)
 ```

## 5-功能服API

# <span id="5-功能服API"></span>5-功能服API

这里是Service的一些接口

<span id="配置"></span>
### 配置

<span id="GetCommonConfig"></span>
#### GetCommonConfig

- 描述

    获取服务器公共配置，包括所有服务器和db的配置，具体参见备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 配置内容 |
- 备注

    服务器公共配置的示例如下，只展示了核心配置信息：
    ```
    {
    "apolloid":111,
    "extra_redis":{
    },
    "game_id":0,
    "game_key":"game_key",
    "gas_server_url":"http://127.0.0.1:111",
    "log_debug_level":true,
    "master":{
    "app_type":"master",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "keep_alive_period":30,
    "master_port":0,
    "mods":"",
    "port":8000,
    "serverid":0,
    "type":"master"
    },
    "mongo":null,
    "mysql":{
    "database":"test_db",
    "host":"127.0.0.1",
    "password":"test_password",
    "port":3306,
    "user":"test_user"
    },
    "redis":{
    "host":"127.0.0.1",
    "password":"",
    "port":6379
    },
    "review_stage":0,
    "serverlist":[
    {
    "app_type":"proxy",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":11003,
    "max_players":0,
    "mods":"",
    "optimum_players":0,
    "port":11002,
    "save":false,
    "serverid":2000,
    "type":"proxy"
    },
    {
    "app_type":"lobby",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":13003,
    "max_players":200,
    "mods":"neteaseRound",
    "optimum_players":0,
    "port":13002,
    "save":false,
    "serverid":4000,
    "type":"lobby"
    }
    ],
    "servicelist":[
    ],
    }
    ```
    
    
- 示例

```python
import service.netgameApi as netServiceApi
conf = netServiceApi.GetCommonConfig()
serverlist = conf['serverlist'] #获取serverlist配置
serverlist = conf['log_debug_level'] #获取日志等级配置
 ```
<span id="GetServerId"></span>
#### GetServerId

- 描述

    获取服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务器id |
- 示例

```python
import service.netgameApi as netServiceApi
serverId = netServiceApi.GetServerId()
 ```
<span id="GetServerLoadedModsById"></span>
#### GetServerLoadedModsById

- 描述

    根据服务器id获取服务器加载mod列表
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id，id为0表示master |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(str) | 服务器mod列表 |
- 示例

```python
import service.netgameApi as netServiceApi
#返回的一个示例：["neteaseAnnounce", "neteaseAuth", "neteaseShop"]
mods = netServiceApi.GetServerLoadedModsById(4000)
 ```
<span id="GetServerLoadedModsByType"></span>
#### GetServerLoadedModsByType

- 描述

    根据服务器类型获取服务器加载mod列表。若同种类型服务器配置了不同的mod，则返回其中一个对应mod列表。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(str) | 服务器mod列表 |
- 示例

```python
import service.netgameApi as netServiceApi
#返回的一个示例：["neteaseAnnounce", "neteaseAuth", "neteaseShop"]
mods = netServiceApi.GetServerLoadedModsByType("survivalGame")
 ```
<span id="GetServiceConfig"></span>
#### GetServiceConfig

- 描述

    获取service配置，该配置对应公共配置中servicelist下对应service的配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 配置内容 |
- 示例

```python
import service.netgameApi as netServiceApi
serviceConf = netServiceApi.GetServiceConfig()
print serviceConf
# 结果实例如下：
# {
#        "app_type": "service", 
#        "app_version": "1.15.0.release20191128", 
#        "http_port": 8520, 
#        "ip": "127.0.0.1", 
#        "mods": "service", 
#        "module_names": [
#                "netease_salog_0", 
#                "netease_salog_1",
#               "netease_uniqueid",
#               "netease_stats_log_0",
#               "netease_stats_log_1",
#               "netease_stats_monitor"
#        ], 
#        "serverid": 11, 
#        "type": "service"
# }
 ```
<span id="通用"></span>
### 通用

<span id="StartRecordEvent"></span>
#### StartRecordEvent

- 描述

    开始启动大厅服/游戏服与功能服之间的脚本事件收发包统计，启动后调用[StopRecordEvent()](#StopRecordEvent)即可获取两个函数调用之间引擎收发包的统计信息
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import service.netgameApi as netServiceApi
suc = netServiceApi.StartRecordEvent()
# 之后通过计时器或者其他触发方式调用StopRecordEvent
result = netServiceApi.StopRecordEvent()
# sendEvent对应的value保存了功能服主动发送给大厅服/游戏服、甚至客户端的事件统计
for eventName, data in result["sendEvent"].iteritems():
        print "sendEvent event[{}] send={} sendSize={}".format(eventName, data["send_num"], data["send_size"])
# sendRequest对应的value保存了功能服发送给其他的功能服事件，以及对应的功能服返回结果的事件
for eventName, data in result["sendRequest"].iteritems():
        print "sendRequest event[{}] request={} requestSize={} response={} responseSize={}".format(eventName, data["request_num"], data["request_size"], data["response_num"], data["response_size"])
# recvRequest对应的value保存了功能服接收到的来自其他服务端的请求，以及对应的返回结果的事件
for eventName, data in result["recvRequest"].iteritems():
        print "recvRequest event[{}] request={} requestSize={} response={} responseSize={}".format(eventName, data["request_num"], data["request_size"], data["response_num"], data["response_size"])
 ```
<span id="StopRecordEvent"></span>
#### StopRecordEvent

- 描述

    停止大厅服/游戏服与功能服之间的脚本事件收发包统计并输出结果，与[StartRecordEvent()](#StartRecordEvent)配合使用，输出结果为字典，具体见示例
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 收发包信息，具体见示例，假如没有调用过StartRecordEvent，则返回为None |
- 示例

```python
import service.netgameApi as netServiceApi
suc = netServiceApi.StartRecordEvent()
# 之后通过计时器或者其他触发方式调用StopRecordEvent
result = netServiceApi.StopRecordEvent()
# sendEvent对应的value保存了功能服主动发送给大厅服/游戏服、甚至客户端的事件统计
for eventName, data in result["sendEvent"].iteritems():
        print "sendEvent event[{}] send={} sendSize={}".format(eventName, data["send_num"], data["send_size"])
# sendRequest对应的value保存了功能服发送给其他的功能服事件，以及对应的功能服返回结果的事件
for eventName, data in result["sendRequest"].iteritems():
        print "sendRequest event[{}] request={} requestSize={} response={} responseSize={}".format(eventName, data["request_num"], data["request_size"], data["response_num"], data["response_size"])
# recvRequest对应的value保存了功能服接收到的来自其他服务端的请求，以及对应的返回结果的事件
for eventName, data in result["recvRequest"].iteritems():
        print "recvRequest event[{}] request={} requestSize={} response={} responseSize={}".format(eventName, data["request_num"], data["request_size"], data["response_num"], data["response_size"])
 ```
<span id="HTTP服务器"></span>
### HTTP服务器

<span id="RegisterOpCommand"></span>
#### RegisterOpCommand

- 描述

    注册一个新的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
    | callback | function | 响应HTTP请求的实例函数，参数有两个，第一个参数clientId，类型为int，是请求方的唯一标识，用于返回请求处理结果；第二个参数requestData，类型为dict，包含HTTP请求的参数（requestBody） |
- 返回值

    无
- 备注

    当多个游戏服/功能服都注册了同一个url的时候，请求会默认被广播到所有注册了这个url的服务器，返回结果中也会综合所有服务器的返回结果
    
    通过在请求中增加opUid【类型为int】参数，可以指定此请求仅转发给对应uid当前在线的服务器
    
    通过在请求中增加opServerIds【类型为list(int)】参数，可以指定此请求仅转发给服务器ID在opServerIds列表中的服务器
    
    通过在请求中增加opServerType【类型为str】参数，可以指定此请求仅转发给服务器类型为opServerType的服务器
    
    当此API注册的url和【masterHttp.RegisterMasterHttp】注册的url相同时，两者只能保留一个，晚执行的语句会顶替掉先执行语句的回调
    
    
- 示例

```python
import service.netgameApi as serviceNetgameApi
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                serviceNetgameApi.RegisterOpCommand("/api/game-url-test1", self.OnServiceUrlTest1)
        
        def OnServiceUrlTest1(self, clientId, requestData):
                print "OnServiceUrlTest1", clientId, requestData
                # 返回处理结果
                serviceNetgameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
<span id="ResponseOpCommandFail"></span>
#### ResponseOpCommandFail

- 描述

    发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | code | int | 请求的失败原因code |
    | message | str | 请求的失败原因的文本 |
- 返回值

    无
- 示例

```python
import service.netgameApi as serviceNetgameApi
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                serviceNetgameApi.RegisterOpCommand("/api/game-url-test3", self.OnServiceUrlTest3)
        
        def OnServiceUrlTest3(self, clientId, requestData):
                print "OnServiceUrlTest3", clientId, requestData
                # 返回处理结果
                lobbyGameApi.ResponseOpCommandFail(clientId, 1, "exec failed")
 ```
<span id="ResponseOpCommandSuccess"></span>
#### ResponseOpCommandSuccess

- 描述

    发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | entity | dict | 请求中需要返回的内容，可自定义key/value的含义 |
- 返回值

    无
- 示例

```python
import service.netgameApi as serviceNetgameApi
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                serviceNetgameApi.RegisterOpCommand("/api/game-url-test1", self.OnServiceUrlTest1)
        
        def OnServiceUrlTest1(self, clientId, requestData):
                print "OnServiceUrlTest1", clientId, requestData
                # 返回处理结果
                serviceNetgameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
<span id="UnRegisterOpCommand"></span>
#### UnRegisterOpCommand

- 描述

    注销一个已注册的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
- 返回值

    无
- 示例

```python
import service.netgameApi as serviceNetgameApi
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                serviceNetgameApi.RegisterOpCommand("/api/game-url-test1", self.OnServiceUrlTest1)
        
        def Destroy(self):
                serviceNetgameApi.UnRegisterOpCommand("/api/game-url-test1")
        
        def OnServiceUrlTest1(self, clientId, requestData):
                print "OnServiceUrlTest1", clientId, requestData
                # 返回处理结果
                serviceNetgameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
这里是service的一些HTTP接口

<span id="HTTP服务器"></span>
### HTTP服务器

<span id="RegisterServiceHttp"></span>
#### RegisterServiceHttp

- 描述

    注册一个新的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | string | 接口url |
    | binder | instance | 响应HTTP请求的实例 |
    | func | function | 响应HTTP请求的实例函数 |
- 返回值

    无
- 示例

```python
import service.serviceHttp as serviceHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                serviceHttp.RegisterServiceHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，send_http_response中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果。code必须为1表示处理成功，否则master请求时会认为请求失败。
                response = '{"code":1,"message":"ok"}'
                serviceHttp.SendHttpResponse(clientId, response)
 ```
<span id="SendHttpRequestToMaster"></span>
#### SendHttpRequestToMaster

- 描述

    给master发送http请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | requestUrl | string | 请求url，例如“/test-reqeust” |
    | message | string | HTTP post body，是个json字符串 |
- 返回值

    无
- 示例

```python
import service.serviceHttp as serviceHttp
params = {
        "message":"content",
        "code":1
}
url = "/test-reqeust"
serviceHttp.SendHttpRequestToMaster(url, json.dumps(params))
 ```
<span id="SendHttpResponse"></span>
#### SendHttpResponse

- 描述

    发送HTTP的Response。支持异步返回，返回时指定输入clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求 |
    | message | string | HTTP Response的内容 |
- 返回值

    无
- 示例

```python
import service.serviceHttp as serviceHttp
class HttpHandler(object):
        def __init__(self):
                # 设置接口URI及回调
                url = '/kick-user'
                func = self.HttpTest
                # 注册
                serviceHttp.RegisterServiceHttp(url, self, func)
        def HttpTest(self, clientId, requestBody):
                # clientId识别请求唯一id，send_http_response中要携带该参数
                # requestBody为post body内容。如果是json格式，则可以通过下面方式加载内容。
                # import ujson as json
                # request = json.loads(requestBody)
                # 返回处理结果
                response = '{"code":0,"message":"ok"}'
                serviceHttp.SendHttpResponse(clientId, response)
 ```
这里是service的一些服务的管理接口

<span id="服务器"></span>
### 服务器

<span id="ResetServer"></span>
#### ResetServer

- 描述

    重置服务器
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game的服务器id |
- 返回值

    无
- 备注

    
    注意，对于生存服，若使用了存档A，则重置后仍使用存档A，且重置过程中不会保存地图。
    
    
    若需要重置游戏服GameA，使用方法：重置前确保玩家退出对应GameA，重置过程不允许玩家进入GameA，GameA重置完毕后GameA可以发消息告知master或service，告知GameA就绪，然后玩家可以进入GameA了
    
    
- 示例

```python
import service.serverManager as serverManager
serverManager.ResetServer(4000)
 ```
<span id="服务器管理"></span>
### 服务器管理

<span id="GetServerIdsByServerType"></span>
#### GetServerIdsByServerType

- 描述

    根据类型获取服务器id列表
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | 服务器类型 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(int) | 服务器id列表，若服务器类型不存在，则返回空列表 |
- 示例

```python
import service.serverManager as serverManager
#返回的一个示例：[4000, 4001]
serverIds = serverManager.GetServerIdsByServerType("lobby")
 ```
<span id="GetServerProtocolVersion"></span>
#### GetServerProtocolVersion

- 描述

    获取服务器的协议版本号。多协议版本引擎中（比如同时支持1.14客户端和1.15客户端），需要把客户端分配到相同协议版本的lobby/game中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 协议版本 |
- 示例

```python
import service.serverManager as serverManager
version = serverManager.GetServerProtocolVersion(6000)
 ```
<span id="GetServerType"></span>
#### GetServerType

- 描述

    获取服务器类型
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | master/service/lobby/game服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 服务器类型字符串。若服务器不存在，则返回空字符串 |
- 示例

```python
import service.serverManager as serverManager
serverType = serverManager.GetServerType(6000)
 ```
<span id="GetServersStatus"></span>
#### GetServersStatus

- 描述

    获取所有lobby/game服务器的状态。只有状态1表示服务器正常服务，其他状态表示服务器不能对外服务
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | key:int, 服务器id，value:int 服务器状态。服务器状态如下：<br/>1:正常状态<br/>2:正在滚动更新关闭状态，服务器马上会下架 <br/>3:滚动更新新增服务器状态，服务器就绪后会转化为状态1 <br/>4:服务器已上架，但是未同service建立连接状态（可能是服务器崩溃或被重置或关服等原因导致），建立连接后会转换为状态1 |
- 示例

```python
import service.serverManager as serverManager
statusDict = serverManager.GetServersStatus()
 ```
<span id="IsConnectedServer"></span>
#### IsConnectedServer

- 描述

    service是否与lobby/game/proxy建立连接
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，已经建立连接;False未建立连接 |
- 示例

```python
import service.serverManager as serverManager
bConnect = serverManager.IsConnectedServer(4000)
 ```

## 6-大厅与游戏服API

# <span id="6-大厅与游戏服API"></span>6-大厅与游戏服API

这里是lobbygame的一些通用的接口

<span id="存档"></span>
### 存档

<span id="QueryPlayerDataResult"></span>
#### QueryPlayerDataResult

- 描述

    不建议开发者使用，把mc地图中玩家存档字符串告知引擎。需要在queryPlayerDataEvent事件的监听函数中调用本api
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbCallIndex | int | 对应【queryPlayerDataEvent】事件的传入唯一ID |
    | success | bool | 是否成功 |
    | dataStr | str | mc地图中玩家存档字符串。 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.QueryPlayerDataResult(dbCallIndex, success, dataStr)
 ```
<span id="SavePlayerDataResult"></span>
#### SavePlayerDataResult

- 描述

    不建议开发者使用，把玩家数据存档状态告知引擎。mod中需要把玩家数据保存到mysql/mongo中。在savePlayerDataOnShutDownEvent/savePlayerDataEvent事件的监听函数中调用本api
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbCallIndex | int | 【savePlayerDataEvent/savePlayerDataOnShutDownEvent】事件中传入唯一ID |
    | success | bool | 存档是否成功 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SavePlayerDataResult(dbCallIndex, success)
 ```
<span id="SetUseDatabaseSave"></span>
#### SetUseDatabaseSave

- 描述

    设置是否使用数据库定时存档。定时存档会定时触发savePlayerDataEvent事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | bUseDatabase | bool | 是否使用数据库 |
    | dbName | str | 30个字符内的英文字符串，建议使用项目英文名 |
    | internalSaveSecond | int | 触发定时存档的时间间隔，单位秒 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetUseDatabaseSave(True, 'test', 30)
 ```
<span id="配置"></span>
### 配置

<span id="GetCommonConfig"></span>
#### GetCommonConfig

- 描述

    获取服务器公共配置，包括本服、所有db和所有功能服的配置，具体参见备注，注意可能不包含其他大厅服和游戏服配置，不能获取所有服的配置
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 配置内容 |
- 备注

    服务器公共配置的示例如下，只展示了核心配置信息，注意可能不包含其他游戏服和大厅服配置
    ```
    {
    "apolloid":111,
    "extra_redis":{
    },
    "game_id":0,
    "game_key":"game_key",
    "gas_server_url":"http://127.0.0.1:111",
    "log_debug_level":true,
    "master":{
    "app_type":"master",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "keep_alive_period":30,
    "master_port":0,
    "mods":"",
    "port":8000,
    "serverid":0,
    "type":"master"
    },
    "mongo":null,
    "mysql":{
    "database":"test_db",
    "host":"127.0.0.1",
    "password":"test_password",
    "port":3306,
    "user":"test_user"
    },
    "redis":{
    "host":"127.0.0.1",
    "password":"",
    "port":6379
    },
    "review_stage":0,
    "serverlist":[
    {
    "app_type":"lobby",
    "app_version":"1.21.0.release20210401",
    "gb":8,
    "ip":"127.0.0.1",
    "log_debug_level":false,
    "master_port":13003,
    "max_players":200,
    "mods":"neteaseRound",
    "optimum_players":0,
    "port":13002,
    "save":false,
    "serverid":4000,
    "type":"lobby"
    }
    ],
    "servicelist":[
    ],
    }
    ```
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
conf = lobbyGameApi.GetCommonConfig()
bDebugLevel = conf['log_debug_level'] #获取日志等级配置
 ```
<span id="GetMongoConfig"></span>
#### GetMongoConfig

- 描述

    获取mongo数据库的连接参数，对应公共配置中mongo配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | tuple | (exist, host, user, password, database, port).exist：bool,是否存在mongo数据库配置; host：str, mongo数据库的地址;user：str,mongo数据库的访问用户; port：int, mongo数据库的端口; password：str,mongo数据库的访问密码;database：str,mongo数据库的数据库名 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
exist, host, user, password, database, port = lobbyGameApi.GetMongoConfig()
 ```
<span id="GetMysqlConfig"></span>
#### GetMysqlConfig

- 描述

    获取mysql数据库的连接参数，对应公共配置中mysql配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | tuple | (exist, host, user, password, database, port).exist：bool,是否存在mysql数据库配置; host：string, mysql数据库的地址;user：string,mysql数据库的访问用户; port：int, mysql数据库的端口; password：string,mysql数据库的访问密码;database：string,mysql数据库的数据库名 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
exist, host, user, password, database, port = lobbyGameApi.GetMysqlConfig()
 ```
<span id="GetRedisConfig"></span>
#### GetRedisConfig

- 描述

    获取redis数据库的连接参数，对应公共配置中redis配置，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | tuple | (exist, host, port, password).exist：bool,是否存在redis配置; host：str, redis数据库的地址;port：int, redis数据库的端口; password：str,redis数据库的访问密码 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
exist, host, port, password = lobbyGameApi.GetRedisConfig()
 ```
<span id="GetServerId"></span>
#### GetServerId

- 描述

    获取本服的服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务器id |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
serverId = lobbyGameApi.GetServerId()
 ```
<span id="地图"></span>
### 地图

<span id="DelForbidDragonEggTeleportField"></span>
#### DelForbidDragonEggTeleportField

- 描述

    删除禁止龙蛋传送的地图区域
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fid | int | 区域的唯一ID，必须大于等于0 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否成功删除（对应fid无法找到返回删除失败） |
- 备注

    具体使用方式可以参考领地插件
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.DelForbidDragonEggTeleportField(1)
 ```
<span id="DelForbidFlowField"></span>
#### DelForbidFlowField

- 描述

    删除地图区域，不同的ID的区域边界会阻挡流体的流动
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fid | int | 区域的唯一ID，必须大于等于0 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否成功删除（对应fid无法找到返回删除失败） |
- 备注

    具体使用方式可以参考领地插件
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.DelForbidFlowField(1)
 ```
<span id="SetEnableLimitArea"></span>
#### SetEnableLimitArea

- 描述

    设置地图最大区域，超过区域的地形不再生成
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | limit | bool | 是否启用地区区域限制 |
    | x | int | 地图区域的中心点 |
    | y | int | 地图区域的中心点 |
    | z | int | 地图区域的中心点 |
    | offsetX | int | 地图区域在x方向和z方向的最大偏移 |
    | offsetZ | int | 地图区域在x方向和z方向的最大偏移 |
- 返回值

    无
- 备注

    真实应用中，请用墙壁把区域围起来。
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetEnableLimitArea(limit, x, y, z, offsetX, offsetZ)
 ```
<span id="SetForbidDragonEggTeleportField"></span>
#### SetForbidDragonEggTeleportField

- 描述

    设置禁止龙蛋传送的地图区域
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fid | int | 区域的唯一ID，必须大于等于0 |
    | dimensionId | int | 区域所在的维度 |
    | minPos | tuple(int) | 长方体区域的x，y，z值最小的点，x，y，z为方块的坐标，而不是像素坐标 |
    | maxPos | tuple(int) | 长方体区域的x，y，z值最大的点，x，y，z为方块的坐标，而不是像素坐标 |
    | priority | int | 区域的优先级，缺损时默认值为0，当一个点位于多个区域包围时，最终会以优先级最高的区域为准 |
    | isForbid | bool | 是否禁止龙蛋传送，为了处理嵌套区域之间的权限冲突，只要是独立的区域都需要设置是否禁止龙蛋传送 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否成功设置 |
- 备注

    具体使用方式可以参考领地插件
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.SetForbidDragonEggTeleportField(1, 0, (-5, -5, -5), (5, 5, 5), 0, True)
 ```
<span id="SetForbidFlowField"></span>
#### SetForbidFlowField

- 描述

    设置地图区域，不同的ID的区域边界会阻挡流体的流动
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fid | int | 区域的唯一ID，必须大于等于0 |
    | dimensionId | int | 区域所在的维度 |
    | minPos | tuple(int) | 长方体区域的x，y，z值最小的点，x，y，z为方块的坐标，而不是像素坐标 |
    | maxPos | tuple(int) | 长方体区域的x，y，z值最大的点，x，y，z为方块的坐标，而不是像素坐标 |
    | priority | int | 区域的优先级，缺损时默认值为0，当一个点位于多个区域包围时，最终会以优先级最高的区域为准 |
    | isForbid | bool | 是否禁止流体流动，为了处理嵌套区域之间的权限冲突，只要是独立的区域都需要设置是否禁止流体流动 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否设置成功 |
- 备注

    具体使用方式可以参考领地插件
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.SetForbidFlowField(1, 0, (-5, -5, -5), (5, 5, 5), 0, True)
 ```
<span id="SetLevelGameType"></span>
#### SetLevelGameType

- 描述

    强制设置游戏的玩法模式
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | mode | int | 0生存模式，1创造模式，2冒险模式 |
- 返回值

    无
- 备注

    真实应用中，请在服务器Mod初始化时调用此函数
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetLevelGameType(2)
 ```
<span id="SetShowFakeSeed"></span>
#### SetShowFakeSeed

- 描述

    在客户端【设置】中，显示虚假的游戏地图种子
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fakeSeed | int | 想要在客户端显示的虚假的地图种子，必须为正整数，可缺损，缺损时会自动随机一个数字 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 备注

    此API只影响调用之后才登录的玩家，所以强烈建议在Mod初始化时就调用此API
    
    此API调用效果会持久化保存到地图文件中
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.SetShowFakeSeed(123456789)
print "SetShowFakeSeed suc={}".format(suc)
 ```
<span id="StopShowFakeSeed"></span>
#### StopShowFakeSeed

- 描述

    在客户端【设置】中，显示真实的游戏地图种子
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 备注

    此API只影响调用之后才登录的玩家，所以强烈建议在Mod初始化时就调用此API
    
    此API调用效果会持久化保存到地图文件中
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.StopShowFakeSeed()
print "StopShowFakeSeed suc={}".format(suc)
 ```
<span id="玩家"></span>
### 玩家

<span id="GetConnectingProxyIdOfPlayer"></span>
#### GetConnectingProxyIdOfPlayer

- 描述

    获取玩家客户端连接的proxy服务器id
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | proxy服务器id |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
nickname = lobbyGameApi.GetConnectingProxyIdOfPlayer(playerId)
 ```
<span id="GetPlatformUid"></span>
#### GetPlatformUid

- 描述

    获取玩家登录端的uid，假如玩家从手机端登录，返回手机端的uid，否则返回PC端的uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int/long/None | 玩家不在线时返回None，在线时假如玩家从手机端登录，返回手机端的uid，否则返回PC端的uid |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
platformUid = lobbyGameApi.GetPlatformUid(playerId)
 ```
<span id="GetPlayerIdByUid"></span>
#### GetPlayerIdByUid

- 描述

    根据玩家uid获取玩家ID（也即playerId）。若玩家不在这个lobby/game，则返回为空字符
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 玩家id，也即玩家的playerId |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
playerId = lobbyGameApi.GetPlayerIdByUid(123)
 ```
<span id="GetPlayerLockResult"></span>
#### GetPlayerLockResult

- 描述

    不建议开发者使用，把获取玩家在线锁结果告知给引擎层
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | id | int | 对应【ServerGetPlayerLockEvent】事件的传入唯一ID |
    | success | bool | 是否成功 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.GetPlayerLockResult(id, suc)
 ```
<span id="GetPlayerNickname"></span>
#### GetPlayerNickname

- 描述

    获取玩家的昵称。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 昵称 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
nickname = lobbyGameApi.GetPlayerNickname(playerId)
 ```
<span id="GetPlayerUid"></span>
#### GetPlayerUid

- 描述

    获取玩家的uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int/long | 玩家的uid；玩家的唯一标识 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
uid = lobbyGameApi.GetPlayerUid(playerId)
 ```
<span id="GetUidIsSilent"></span>
#### GetUidIsSilent

- 描述

    根据玩家uid获取是否被禁言
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 0:全局禁言，1:普通禁言，2:没有被禁言 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
isSilent = lobbyGameApi.GetUidIsSilent(123)
 ```
<span id="HidePlayerFootprint"></span>
#### HidePlayerFootprint

- 描述

    隐藏某个玩家的会员脚印外观
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | str | playerId | 玩家id |
    | hide | bool | 是否隐藏，True为隐藏脚印，False为恢复脚印显示 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True:设置成功<br>False:设置失败 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
# 隐藏玩家的会员脚印外观
result = lobbyGameApi.HidePlayerFootprint(playerId, True)
 ```
<span id="HidePlayerMagicCircle"></span>
#### HidePlayerMagicCircle

- 描述

    隐藏某个玩家的会员法阵外观
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | str | playerId | 玩家id |
    | hide | bool | 是否隐藏，True为隐藏法阵，False为恢复法阵显示 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True:设置成功<br>False:设置失败 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
# 隐藏玩家的会员法阵外观
result = lobbyGameApi.HidePlayerMagicCircle(playerId, True)
 ```
<span id="IsPlayerPeUser"></span>
#### IsPlayerPeUser

- 描述

    获取玩家是否从手机端登录
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool/None | 玩家不在线时返回None，在线时返回True代表此玩家本次从手机端登录，返回False代表此玩家从PC端登录 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
isPeUser = lobbyGameApi.IsPlayerPeUser(playerId)
 ```
<span id="ReleasePlayerLockResult"></span>
#### ReleasePlayerLockResult

- 描述

    不建议开发者使用，把释放玩家在线锁结果告知给引擎层
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | id | int | 对应【ServerReleasePlayerLockEvent/ServerReleasePlayerLockOnShutDownEvent】事件传入的唯一ID |
    | success | bool | 是否成功 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.ReleasePlayerLockResult(id, suc)
 ```
<span id="SetAutoRespawn"></span>
#### SetAutoRespawn

- 描述

    设置是否启用自动重生逻辑
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | autoRespawn | bool | 是否启用自动重生逻辑 |
    | internalSeconds | int | 每隔多少秒，检查是否满足自动重生条件 |
    | minY | int | 高度低于多少，就会触发自动重生逻辑 |
    | x | int | 自动重生逻辑触发后，重生点的坐标 |
    | y | int | 自动重生逻辑触发后，重生点的坐标 |
    | z | int | 自动重生逻辑触发后，重生点的坐标 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetAutoRespawn(autoRespawn, internalSeconds, minY, x, y, z)
 ```
<span id="ShieldPlayerJoinText"></span>
#### ShieldPlayerJoinText

- 描述

    是否屏蔽客户端左上角 “xxx 加入了游戏”的提示
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | bShield | bool | True，不显示提示；False，显示提示 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.ShieldPlayerJoinText(True)
 ```
<span id="TryToKickoutPlayer"></span>
#### TryToKickoutPlayer

- 描述

    把玩家踢下线，message中的文字会显示在客户端的断线提示中
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家对象的entityId |
    | message | str | 踢掉玩家的理由，默认为空 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.TryToKickoutPlayer(playerId, "GM把你踢下线")
 ```
<span id="调试"></span>
### 调试

<span id="StartChunkProfile"></span>
#### StartChunkProfile

- 描述

    开始启动服务端区块读写性能统计，启动后调用[StopChunkProfile](#StopChunkProfile)即可获得近期的服务端区块读写信息
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 备注

    启动区块读写信息记录有比较大的消耗，不建议长期启用
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.StartChunkProfile()
print "StartChunkProfile suc={}".format(suc)
# 之后通过计时器或者其他触发方式调用StopChunkProfile
data = lobbyGameApi.StopChunkProfile()
for singleData in data:
        print "time is {}".format(time.strftime("%H:%M:%S", time.localtime(singleData["timestamp"])))
        print "saveChunks is {}".format(singleData["saveChunks"])
        print "loadChunks is {}".format(singleData["loadChunks"])
 ```
<span id="StopChunkProfile"></span>
#### StopChunkProfile

- 描述

    结束服务端区块读写性能统计，并返回近期区块读写信息，与[StartChunkProfile](#StartChunkProfile)配合使用
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list(dict) | 每个字典都是1秒内的区块读写信息，按照时间线排序，timestamp：类型为int，统计的具体时间（秒）；saveChunks：类型为list(dict)，1秒内写chunk的坐标和维度；loadChunks：类型为list(dict)，1秒内读chunk的坐标和维度 |
- 备注

    启动区块读写信息记录有比较大的消耗，不建议长期启用
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
suc = lobbyGameApi.StartChunkProfile()
print "StartChunkProfile suc={}".format(suc)
# 之后通过计时器或者其他触发方式调用StopChunkProfile
data = lobbyGameApi.StopChunkProfile()
for singleData in data:
        print "time is {}".format(time.strftime("%H:%M:%S", time.localtime(singleData["timestamp"])))
        print "saveChunks is {}".format(singleData["saveChunks"])
        print "loadChunks is {}".format(singleData["loadChunks"])
 ```
<span id="关服"></span>
### 关服

<span id="SetGracefulShutdownOk"></span>
#### SetGracefulShutdownOk

- 描述

    不建议开发者使用，设置脚本层的优雅关机逻辑已经执行完毕，引擎可以开始优雅关机了
    
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetGracefulShutdownOk()
 ```
<span id="SetShutdownOk"></span>
#### SetShutdownOk

- 描述

    不建议开发者使用，设置脚本层的强制关机逻辑已经执行完毕，引擎可以开始强制关机了
    
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetShutdownOk()
 ```
<span id="ShutdownServer"></span>
#### ShutdownServer

- 描述

    强制关机
    
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.ShutdownServer()
 ```
<span id="服务器"></span>
### 服务器

<span id="CheckMasterExist"></span>
#### CheckMasterExist

- 描述

    检查服务器是否与master建立连接
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否与master建立连接 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
exist = lobbyGameApi.CheckMasterExist()
 ```
<span id="GetLastFrameTime"></span>
#### GetLastFrameTime

- 描述

    获取服务端脚本上一帧运行时间
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务端脚本上一帧运行时间,单位纳秒 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lastFrameTime = lobbyGameApi.GetLastFrameTime()
 ```
<span id="GetOnlinePlayerNum"></span>
#### GetOnlinePlayerNum

- 描述

    获取当前服务器的在线人数
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 当前服务器在线人数 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
num = lobbyGameApi.GetOnlinePlayerNum()
 ```
<span id="GetServerProtocolVersion"></span>
#### GetServerProtocolVersion

- 描述

    获取服务器的协议版本号
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 服务器的协议版本号 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
protocolVersion = lobbyGameApi.GetServerProtocolVersion()
 ```
<span id="IsServiceConnected"></span>
#### IsServiceConnected

- 描述

    检查服务器是否与某个service建立连接
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 是否与service建立连接 |
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
bConnected = lobbyGameApi.IsServiceConnected(8000)
 ```
<span id="IsShowDebugLog"></span>
#### IsShowDebugLog

- 描述

    当前服务器是否打印debug等级的日志
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | True，打印debug log，否则不打印debug log |
- 备注

    基本无需关注
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
bDebug = lobbyGameApi.IsShowDebugLog()
 ```
<span id="ResetServer"></span>
#### ResetServer

- 描述

    重置服务器
    
- 返回值

    无
- 备注

    
    注意，对于生存服，若使用了存档A，则重置后仍使用存档A，且重置过程中不会保存地图。
    
    
    重置本服的方法：重置前确保玩家退出本服，重置过程不允许玩家进入本服，本服启动后可以发消息给master或service，告知本服就绪，然后玩家可以进入本服了
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.ResetServer()
 ```
<span id="切服"></span>
### 切服

<span id="TransferToOtherServer"></span>
#### TransferToOtherServer

- 描述

    玩家转移到指定类型的服务器，假如同类服务器有多个，就根据负载均衡选择一个
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | typeName | str | 目标服务器的类型，对应MCStudio中配置：服务器配置->游戏配置->类型 |
    | transferParam | str | 切服传入参数，默认空字符串。当玩家跳转到目标服务器触发AddServerPlayerEvent事件时，AddServerPlayerEvent事件会携带这个参数 |
    | callback | function | 回调函数，返回转服API经过master的逻辑判定之后的结果，参数有三个，isSuc(bool), reasonCode(int), message(str)，isSuc返回是否成功；reasonCode代表失败的错误码，message为失败的理由的中文描述 |
- 返回值

    无
- 备注

    玩家只会切到一个可用的服务，也即要求目标服务器是正常工作状态，不能是断开连接、滚动关服、已关服等异常状态，若转移的目标服务器不可用，则切服失败
    
    
- 示例

```python
import json
import lobbyGame.netgameApi as lobbyGameApi
transData = {'position' : [1,2,3]}
def cbFunc(isSuc, reasonCode, message):
        print "TransferToOtherServer callback, isSuc={} reason={}".format(isSuc, message)
lobbyGameApi.TransferToOtherServer('123', 'game', json.dumps(transData), cbFunc)
 ```
<span id="TransferToOtherServerById"></span>
#### TransferToOtherServerById

- 描述

    玩家迁移到指定服务器id的服务器
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
    | serverId | str | 目标服务器id，服务器id对应公共配置中serverid，公共配置参见[GetCommonConfig](#GetCommonConfig)备注 |
    | transferParam | str | 切服传入参数，默认空字符串。当玩家跳转到目标服务器触发AddServerPlayerEvent事件时，AddServerPlayerEvent事件会携带这个参数 |
    | callback | function | 回调函数，返回转服API经过master的逻辑判定之后的结果，参数有三个，isSuc(bool), reasonCode(int), message(str)，isSuc返回是否成功；reasonCode代表失败的错误码，message为失败的理由的中文描述 |
- 返回值

    无
- 备注

    用法详情见示例Mod sample
    
    要求目标服务器是正常工作状态，不能是断开连接、滚动关服、已关服等异常状态，若转移的目标服务器不可用，则切服失败
    
    
- 示例

```python
import json
import lobbyGame.netgameApi as lobbyGameApi
transData = {'position' : [1,2,3]}
def cbFunc(isSuc, reasonCode, message):
        print "TransferToOtherServerById callback, isSuc={} reason={}".format(isSuc, message)
lobbyGameApi.TransferToOtherServerById('123', 2000000, json.dumps(transData), cbFunc)
 ```
<span id="主城模式"></span>
### 主城模式

<span id="SetCityMode"></span>
#### SetCityMode

- 描述

    设置游戏为主城模式：包括有无法改变地形，不切换日夜，不改变天气，不刷新生物等限制
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | isCityMode | bool | 是否为主城模式 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.SetCityMode(isCityMode)
 ```
<span id="HTTP服务器"></span>
### HTTP服务器

<span id="RegisterOpCommand"></span>
#### RegisterOpCommand

- 描述

    注册一个新的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
    | callback | function | 响应HTTP请求的实例函数，参数有两个，第一个参数clientId，类型为int，是请求方的唯一标识，用于返回请求处理结果；第二个参数requestData，类型为dict，包含HTTP请求的参数（requestBody） |
- 返回值

    无
- 备注

    当多个游戏服/功能服都注册了同一个url的时候，请求会默认被广播到所有注册了这个url的服务器，返回结果中也会综合所有服务器的返回结果
    
    通过在请求中增加opUid【类型为int】参数，可以指定此请求仅转发给对应uid当前在线的服务器
    
    通过在请求中增加opServerIds【类型为list(int)】参数，可以指定此请求仅转发给服务器ID在opServerIds列表中的服务器
    
    通过在请求中增加opServerType【类型为str】参数，可以指定此请求仅转发给服务器类型为opServerType的服务器
    
    当此API注册的url和【masterHttp.RegisterMasterHttp】注册的url相同时，两者只能保留一个，晚执行的语句会顶替掉先执行语句的回调
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
class GameExtraApiSystem(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                lobbyGameApi.RegisterOpCommand("/api/game-url-test1", self.OnGameUrlTest1)
        def OnGameUrlTest1(self, clientId, requestData):
                print "OnGameUrlTest1", clientId, requestData
                # 返回处理结果
                lobbyGameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
<span id="ResponseOpCommandFail"></span>
#### ResponseOpCommandFail

- 描述

    发送HTTP的失败Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | code | int | 请求的失败原因code |
    | message | str | 请求的失败原因的文本 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
class GameExtraApiSystem(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                lobbyGameApi.RegisterOpCommand("/api/game-url-test2", self.OnServiceUrlTest2)
        
        def OnServiceUrlTest2(self, clientId, requestData):
                print "OnServiceUrlTest2", clientId, requestData
                # 返回处理结果
                lobbyGameApi.ResponseOpCommandFail(clientId, 1, "exec failed")
 ```
<span id="ResponseOpCommandSuccess"></span>
#### ResponseOpCommandSuccess

- 描述

    发送HTTP的成功Response，支持异步返回，返回时候指定请求传入的clientId
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | clientId | int | 请求唯一id，识别HTTP请求。 |
    | entity | dict | 请求中需要返回的内容，可自定义key/value的含义 |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
class GameExtraApiSystem(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                lobbyGameApi.RegisterOpCommand("/api/game-url-test1", self.OnGameUrlTest1)
        def OnGameUrlTest1(self, clientId, requestData):
                print "OnGameUrlTest1", clientId, requestData
                # 返回处理结果
                lobbyGameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
<span id="UnRegisterOpCommand"></span>
#### UnRegisterOpCommand

- 描述

    注销一个已注册的HTTP接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | url | str | 接口url |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
class GameExtraApiSystem(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                lobbyGameApi.RegisterOpCommand("/api/game-url-test1", self.OnGameUrlTest1)
        
        def Destroy(self):
                lobbyGameApi.UnRegisterOpCommand("/api/game-url-test1")
        
        def OnGameUrlTest1(self, clientId, requestData):
                print "OnGameUrlTest1", clientId, requestData
                # 返回处理结果
                lobbyGameApi.ResponseOpCommandSuccess(clientId, {"result":"exec success"})
 ```
<span id="商城"></span>
### 商城

<span id="NotifyClientToOpenShopUi"></span>
#### NotifyClientToOpenShopUi

- 描述

    通知客户端打开商城界面
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | playerId | str | 玩家id |
- 返回值

    无
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.NotifyClientToOpenShopUi('123456')
 ```
<span id="性能开关"></span>
### 性能开关

<span id="ChangeAllPerformanceSwitch"></span>
#### ChangeAllPerformanceSwitch

- 描述

    整体关闭/打开预定义的游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），
    只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提
    高服务器的性能，承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务
    器初始化时调用此接口，同时不要在服务器运行中途修改
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | is_disable | bool | True代表【关】，False代表【开】 |
    | extra | list | 剔除掉不需要改变开关状态的具体功能的枚举值列表。默认为空 |
- 返回值

    无
- 备注

    当extra的值为None的时候，默认影响到的开关不包括【LoadSavedEntityFromChunk】。
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.ChangeAllPerformanceSwitch(True)
 ```
<span id="ChangePerformanceSwitch"></span>
#### ChangePerformanceSwitch

- 描述

    关闭/打开某个游戏原生逻辑，所有的逻辑默认状态均为【开】（也就是is_disable=False），
    只有当调用此接口关闭之后，才会进入到【关】的状态，关闭这类原生逻辑能够提高服务器的性能，
    承载更高的同时在线人数，同时也会使一些生存服的玩法失效。另外，强烈建议在服务器初始化时调用此接口，同时不要在服务器运行中途修改
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | int | 具体功能的枚举值，详情见备注 |
    | isDisable | bool | True代表【关】，False代表【开】 |
- 返回值

    无
- 备注

    所有开关的枚举值以及涵义
    ```python
    class DisableSwitch(object):
    '''
    -------------------ChunkLoadUsePriority-------------------
    开关介绍：加载chunk时，是否根据chunk的坐标与当前在线玩家的坐标计算加权优先级（性能较低），disable后所有chunk的加载优先级相同
    适用情况：提供了特定地图，不需要服务器生成地图
    影响mod sdk的范围：不影响mod sdk
    '''
    ChunkLoadUsePriority = 1
    '''
    -------------------RedstoneOnTick-------------------
    开关介绍：屏蔽红石电路逻辑，disable后红石相关逻辑不生效
    适用情况：未使用红石以及电路相关功能
    影响mod sdk的范围：
    1、能自定义红石
    2、服务端事件：不触发BlockStrengthChangedServerEvent
    3、服务端组件：redStone不生效
    '''
    RedstoneOnTick = 2
    '''
    -------------------ChunkSaveOnTick-------------------
    开关介绍：否存档chunk，disable后对地图chunk的修改不会再存档到地图文件
    适用情况：地图不会改变
    影响mod sdk的范围：
    1、服务端事件都不受影响
    2、受影响API：
    （1）SetBlockTileEntityCustomData 设置的内容不会保存到地图
    （2）SetBlockStates 方块状态不会保存到地图
    （3）SetBlockNew 可以设置方块，但是设置内容不保存到地图
    '''
    ChunkSaveOnTick = 3
    '''
    -------------------WalkAnimPostEvent-------------------
    开关介绍：是否关闭服务器的移动开始/移动结束事件（性能较低），disable后服务器引擎层不再dispatch上述两个事件
    适用情况：没有监听WalkAnimBeginServerEvent事件和WalkAnimEndServerEvent事件（一般可以用客户端的WalkAnimBeginClientEvent与WalkAnimEndClientEvent代替）
    影响mod sdk的范围：不触发WalkAnimBeginServerEvent事件和WalkAnimEndServerEvent事件
    '''
    WalkAnimPostEvent = 4
    '''
    -------------------RecipesSyncOnLogin-------------------
    开关介绍：是否在登录完成后发送服务器配方表，disable后客户端无法收到登录后的配方表，客户端无法进行合成，烧炼以及炼药
    适用情况：玩家不进行合成，烧炼以及炼药
    影响mod sdk的范围：不影响sdk
    '''
    RecipesSyncOnLogin = 5
    '''
    -------------------UpdateGlidingOnTick-------------------
    开关介绍：是否屏蔽玩家的滑翔功能，disable后一旦进入滑翔状态，将会出现状态更新异常
    适用情况：玩家不进行滑翔操作
    影响mod sdk的范围：不影响sdk
    '''
    UpdateGlidingOnTick = 6
    '''
    -------------------UpdateContainerOnTick-------------------
    开关介绍：是否执行容器的每帧刷新逻辑，disable后熔炉、炼药锅、高炉、烟熏炉、酿造台无法使用
    适用情况：没有使用熔炉、炼药锅、高炉、烟熏炉、酿造台
    影响mod sdk的范围：不影响sdk
    '''
    UpdateContainerOnTick = 7
    '''
    -------------------PushEntitiesOnTick-------------------
    开关介绍：是否执行玩家推挤物品/entity的逻辑，disable后玩家无法推动地图上的物品/entity
    适用情况：不考虑玩家推挤功能
    影响mod sdk的范围：
    服务端事件：不触发OnPlayerHitMobServerEvent
    服务端组件：组件actorPushable不生效
    '''
    PushEntitiesOnTick = 8
    '''
    -------------------UpdateInsideBlockOnTick-------------------
    开关介绍：是否执行entity在block中的每帧特殊判定逻辑，disable后传送门无法启动传送，另外在仙人掌侧面、在甜浆果丛上都不会掉血
    适用情况：不用考虑上面特殊逻辑
    影响mod sdk的范围：
    服务端事件：不触发 WillTeleportToServerEvent、DimensionChangeFinishServerEvent、DimensionChangeServerEvent
    服务端组件：没有受到影响
    '''
    UpdateInsideBlockOnTick = 9
    '''
    -------------------BlockDamageOnTick-------------------
    开关介绍：是否执行entity在特殊地形上的每帧特殊判定逻辑，disable后站在岩浆块、点燃的营火上面不会受伤
    适用情况：不用考虑上面特殊逻辑
    影响mod sdk的范围：不影响sdk
    '''
    BlockDamageOnTick = 10
    '''
    -------------------SendDirtyActorPerTick-------------------
    开关介绍：是否每帧检查entity属性变化并同步，disable之后从每帧检测降频到每秒检测。会导致玩家掉血后延迟一秒才会同步到本地
    适用情况：允许延迟同步生物属性
    影响mod sdk的范围：SyncModDataServerEvent事件会延迟触发
    '''
    SendDirtyActorPerTick = 13
    '''
    -------------------ApplyExhaustionOnTick-------------------
    开关介绍：是否执行玩家移动时的饥饿逻辑，disable后玩家走路，跑步，游泳不会消耗饥饿度，跳跃，饥饿效果等也不会减饥饿值
    适用情况：饥饿值不变，或使用了SetDisableHunger接口屏蔽了玩家饥饿度
    影响mod sdk的范围：不影响sdk
    '''
    ApplyExhaustionOnTick = 14
    '''
    -------------------UpdateInteractionOnTick-------------------
    开关介绍：是否每帧检查人物交互，disable之后，准心指向可交互实体时不会显示交互按钮，但是长按依然可以触发交互
    适用情况：不考虑交互的文字提示
    影响mod sdk的范围：不触发OnCarriedNewItemChangedServerEvent事件
    '''
    UpdateInteractionOnTick = 15
    '''
    -------------------UpdateOffhandItemOnTick-------------------
    开关介绍：是否每帧检查人物副手装备属性变化并同步，disable之后副手持有地图位置不会更新
    适用情况：副手没有使用地图
    影响mod sdk的范围：不影响sdk
    '''
    UpdateOffhandItemOnTick = 16
    '''
    -------------------PickEntityOnTick-------------------
    开关介绍：是否每帧检查附近可捡取的物品道具，disable之后会捡不到物品
    适用情况：玩家不捡取附近道具
    影响mod sdk的范围：
    1、服务端事件：不触发ServerPlayerTryTouchEvent
    2、服务端组件：player组件中SetPickUpArea 无用
    '''
    PickEntityOnTick = 17
    '''
    -------------------SyncComplexItemOnTick-------------------
    开关介绍：是否每帧同步玩家地图（ Map）或空地图（ Empty Map）内容，disable之后不同步地图或空白地图
    适用情况：不使用地图（ Map）或空地图（ Empty Map）
    影响mod sdk的范围：不影响sdk
    '''
    SyncComplexItemOnTick = 18
    '''
    -------------------UpdateChunkPerTick-------------------
    开关介绍：是否每帧执行chunk的tick逻辑，disable之后从每帧执行降频到4帧一次
    适用情况：地图上的实体逻辑、方块实体逻辑、方块的随机刻的更新存在延迟
    影响mod sdk的范围：不影响sdk
    '''
    UpdateChunkPerTick = 19
    '''
    -------------------SpawnMobsOnTick-------------------
    开关介绍：是否自动生成怪物，disable之后游戏中不会自动生成怪物
    适用情况：游戏中不自动生成怪物，并且生物不会伴随结构生成（例如村庄不会生成村民）
    影响mod sdk的范围：不触发ServerSpawnMobEvent服务端事件
    '''
    SpawnMobsOnTick = 20
    '''
    -------------------UpdateBlocksOnTick-------------------
    开关介绍：是否每帧刷新block逻辑，disable之后闪电、骷髅陷阱不再刷新，block不受天气影响，不执行随机刻 (Random tick)
    适用情况：适用于地图不变、天气不变场景
    影响mod sdk的范围：不触发BlockRandomTickServerEvent服务端事件
    '''
    UpdateBlocksOnTick = 22
    '''
    -------------------UpdateWeatherOnTick-------------------
    开关介绍：是否每帧执行天气刷新逻辑，disable之后，天气不再刷新（打雷下雨）,季节也不变
    适用情况：天气和季节不变
    影响mod sdk的范围：不影响sdk
    '''
    UpdateWeatherOnTick = 23
    '''
    -------------------LoadSavedEntityFromChunk-------------------
    开关介绍：是否不加载chunk存档中的entity，disable之后，entity的存档将失效
    适用情况：不从地图中加载entity，不存档entity
    影响mod sdk的范围：不影响sdk
    '''
    LoadSavedEntityFromChunk = 27
    ```
    
    
- 示例

```python
import lobbyGame.netgameApi as lobbyGameApi
import lobbyGame.netgameConsts as netgameConsts
lobbyGameApi.ChangePerformanceSwitch(netgameConsts.DisableSwitch.ChunkLoadUsePriority, True)
 ```
这里是lobby的一些接口

<span id="主城模式"></span>
### 主城模式

<span id="SetCityMode"></span>
#### SetCityMode

- 描述

    【废弃】设置游戏为主城模式：包括有无法改变地形，不切换日夜，不改变天气，不刷新生物等限制
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | isCityMode | bool | 是否为主城模式 |
- 返回值

    无
- 示例

```python
import lobby.netgameApi as lobbyApi
lobbyApi.SetCityMode(isCityMode)
 ```

## 7-公共API

# <span id="7-公共API"></span>7-公共API

下面是异步任务池的接口

<span id="异步线程池"></span>
### 异步线程池

<span id="EmitOrder"></span>
#### EmitOrder

- 描述

    添加一个异步任务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | string/int | 相同key的任务，线程池顺序执行；不同key的任务，线程池会并行执行。可以确认某些任务按照顺序执行。 |
    | func | function | 任务对应的函数，该函数会在线程池中运行。该任务和主线程会并行执行，需要确认任务是线程安全的。函数必须返回一个元组，若返回为空则要求返回空元组("()")。函数输入参数是*args |
    | callback | function | 回调函数，它在主线程执行。func的返回值会是callback的实参。若没有回调，则传入None。 |
    | *args | *args | func函数的非关键字参数 |
- 返回值

    无
- 示例

```python
import time
import apolloCommon.workerPool as workerPool
def Callbacks(idx, result):
        print "callbacks",idx, result
def Test(idx):
        print "test start %d" % idx
        time.sleep(1)
        print "test fin %d" % idx
        result = idx + 5
        return (idx, result)#任务必须有返回值。若没有返回值，请返回 "()"
ins = workerPool.ForkNewPool(4)
for i in xrange(4):
        #添加异步任务。i为奇数的任务顺序执行，i为偶数的任务顺序执行。这两批任务并行执行。
        ins.EmitOrder(i%2, Test, Callbacks, i)
ins.Finish(None) #等待线程池退出。
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待线程池退出，线程池会执行完所有异步任务后退出，会阻塞主线程。建议Mod退出时执行
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | timeout | int | 等待线程池退出时间，单位秒。若为None，则会一直等待。建议用None。 |
- 返回值

    无
- 示例

```python
import apolloCommon.workerPool as workerPool
ins = workerPool.ForkNewPool(4)
ins.Finish(None) #等待线程池退出。
 ```
<span id="ForkNewPool"></span>
#### ForkNewPool

- 描述

    创建线程池，设置线程池大小
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | orderSize | int | 线程池的大小 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | MainPool | 线程池实例 |
- 示例

```python
import apolloCommon.workerPool as workerPool
ins = workerPool.ForkNewPool(10)
 ```
下面是mysql线程池的接口

<span id="mysql连接池"></span>
### mysql连接池

<span id="AsyncExecuteFunctionWithOrderKey"></span>
#### AsyncExecuteFunctionWithOrderKey

- 描述

    添加一个异步mysql任务，func将在子线程中执行，注意func中不支持执行引擎提供的API
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | func | function | mysql异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mysql长连接，可以通过conn.cursor()获取cursor |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的其它非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用。 |
- 返回值

    无
- 示例

```python
def TestMysqlPoolCallback(records):
        if records is None:
                print "TestMysqlPoolCallback execute fail"
        else:
                print "TestMysqlPoolCallback execute success"
                for line in records:
                        print "single record=%s" % str(line)
def mysqlFunc(conn, num):
        cursor = conn.cursor()
        query = "SELECT * FROM neteaseUserMail LIMIT %s"
        params = (num, )
        try:
                cursor.execute(query, params)
                records = cursor.fetchall()
        except Exception as e:
                logout.error("mysqlFunc error=%s"%str(e))
                records = None
        finally:
                cursor.close()
        return records
#执行事务的一个示例
def mysqlTransactionTest(conn):
        conn.autocommit(False)
        cursor = conn.cursor()
        try:
                params = (2, 'test_items')
                query = "insert into neteaseCloudItems (uid, cloud_items) values (%s, %s)"
                cursor.execute(query, params)
                conn.commit()
        except:
                conn.rollback()
        finally:
                cursor.close()
                conn.autocommit(True)#请务必将连接还原
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(5)
mysqlPool.AsyncExecuteFunctionWithOrderKey(mysqlFunc, "global", TestMysqlPoolCallback, 5)
mysqlPool.AsyncExecuteFunctionWithOrderKey(mysqlTransactionTest, "test_trans", None)
mysqlPool.Finish()
 ```
<span id="AsyncExecuteWithOrderKey"></span>
#### AsyncExecuteWithOrderKey

- 描述

    添加一个异步mysql任务，执行所有mysql操作
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | str | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(30)
def Cb(t):
        #插入成功情况下，t的值：True
        #插入失败情况下，t的值：False
        print "cb", t
#添加异步任务。
mysqlPool.AsyncExecuteWithOrderKey('player', 'insert into player values (%s, %s)', (1, "test1"), Cb)
mysqlPool.Finish()
 ```
<span id="AsyncExecutemanyWithOrderKey"></span>
#### AsyncExecutemanyWithOrderKey

- 描述

    添加一个异步mysql任务，针对同一条sql语句，使用paramsList中的每个参数各执行一次，并且返回成功修改/新建的记录数，其中任何一条语句执行失败，最终所有语句都会被执行失败，返回None
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | orderKey | string/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | string | mysql插入语句，格式化字符串 |
    | callback | function | 回调函数，在主线程执行，只有唯一一个参数，成功修改/新建的记录数，假如sql执行失败，返回参数将会是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import time
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(30)
def Cb(t):
        #插入成功情况下，t的值：3
        #插入失败情况下，可能出现部分数据插入成功问题，此时t的值：None
        print "cb", t
#添加异步任务。
mysqlPool.AsyncExecutemanyWithOrderKey('pay', 'insert into pay values (%s, %s)', [(1,"648"),(2,"328"), (3,"345")], Cb)
for i in xrange(100):
        mysqlPool.Tick()
        time.sleep(0.2)
mysqlPool.Finish()
 ```
<span id="AsyncInsertOneWithOrderKey"></span>
#### AsyncInsertOneWithOrderKey

- 描述

    添加一个异步mysql任务，向主键为AUTO INCREASEl类型的表格中插入一条记录，并且返回新建记录的主键
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | orderKey | string/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | string | mysql插入语句，格式化字符串 |
    | params | tuple | 填充sql |
    | callback | function | 回调函数，在主线程执行，只有唯一一个参数，是新建记录的主键，假如sql执行失败，返回参数将会是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
# 表testTable的创建语句如下
# CREATE TABLE IF NOT EXISTS `testTable` (
#       `id` bigint unsigned NOT NULL AUTO_INCREMENT,
#       `col_1` varchar(50) NOT NULL,
#       PRIMARY KEY (`uid`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(30)
def Cb(t):
        #插入成功情况下，t的一个示例值（也即表testTable中列id对应值）：1
        #插入失败情况下，t的值：None
        print "cb", t
#添加异步任务。
mysqlPool.AsyncInsertOneWithOrderKey('pay', 'insert into testTable (col_1) values (%s)', ("648"), Cb)
mysqlPool.Finish()
 ```
<span id="AsyncQueryWithOrderKey"></span>
#### AsyncQueryWithOrderKey

- 描述

    添加一个异步mysql任务，执行mysql查询
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | str | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(30)
def Cb(t):
        #查询到一条记录情况下，t的一个示例值：((1L, u'test_name_1', 0L),)
        #查询为空情况下，t的值：()
        #查询报错情况，t的值：None
        print "cb", t
#添加异步任务。
mysqlPool.AsyncQueryWithOrderKey('player', 'select uid,name from player where uid = %s', (1,), Cb)
#等价于
#mysqlPool.AsyncQuery('player', 'select uid,name from player where uid = %s', (1,), Cb)
#orderKey都是'player'，两个任务顺序执行。
mysqlPool.AsyncQueryWithOrderKey('player', 'select uid,name from player where uid = %s', (1,), Cb)
mysqlPool.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待mysql线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化myqsl连接池，要求在MCStudio的“服务器配置”中配置mysql
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
mysqlPool.InitDB(30)
 ```
<span id="SyncFetchAll"></span>
#### SyncFetchAll

- 描述

    阻塞性执行sql语句，查询数据
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | sql | string | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | None/list | 错误返回None，否则返回列表，列表中每个元素表示一条查询记录 |
- 备注

    建议只在初始化mod时执行这个api，不要在运行期间执行本api。它会阻塞主流程，可能导致服务器卡顿。
    
    
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
sql = 'select _id, name from test_user where _id > %s'
#查询成功情况下，allRecords的一个示例值：((1L, u'test_name_1', 0L), (2L, u'test22', 2222L), (3L, u'test33', 333L))
#查询失败情况下，allRecords的值：None
allRecords = mysqlPool.SyncFetchAll(sql, (0, ))
for record in allRecords:
        user['_id'] = record[0]#对应select后的第一个字段
        user['name'] = record[1]#对应select后的第二个字段
 ```
<span id="SyncInsert"></span>
#### SyncInsert

- 描述

    阻塞性执行sql语句，插入数据
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | sql | string | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | None/id | 错误返回None，否则返回成功插入的id |
- 备注

    建议只在初始化mod时执行这个api，不要在运行期间执行本api。它会阻塞主流程，可能导致服务器卡顿。
    
    
- 示例

```python
import apolloCommon.mysqlPool as mysqlPool
sql = 'insert into test_user(name, age) values(%s, %s)'
#插入成功情况下，返回值是插入的主键id
#插入失败情况下，返回值是0
insertId = mysqlPool.SyncInsert(sql, ("steve", 20))
 ```
下面是redis线程池的接口

<span id="redis连接池"></span>
### redis连接池

<span id="AsyncDelete"></span>
#### AsyncDelete

- 描述

    执行redis操作，删除某个redis key,相当于redis中执行命令:del key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | string | redis中的key |
    | callback | function | 回调函数，输入参数是redis操作返回值,是个int，表示删除redis key的个数 ,它在主线程执行。可以不传入回调函数。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
def Cb1(t):
        #执行成功且redis key "player_121"存在情况下，t的值：1
        #执行成功且redis key "player_121"不存在情况下，t的值：0
        #执行失败时，t的值：None
        print "cb", t
redisPool.InitDB(30) #建立连接池
redisPool.AsyncDelete('player_121', cb1)
redisPool.Finish()
 ```
<span id="AsyncFuncWithKey"></span>
#### AsyncFuncWithKey

- 描述

    添加一个异步redis任务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | func | function | redis异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个redis长连接，是一个redis.StrictRedis实例，其他参数是*args |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值是callback的输入参数。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的其它非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用。 |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
redisPool.InitDB(30) #建立连接池
#回调，可以获取player的信息。这里只是打印结果。
def Cb1(t):
        #执行成功且存在redis key "player_123"情况下，t的一个示例值：'test_string_value'
        #执行成功且不存在redis key "player_123"情况下，t的值：""
        #执行失败时，key的值：None
        print "cb", t
#第一个参数是redis.StrictRedis实例。
def GetValueFromKey(conn, key):
        ret = conn.get(key)
        return ret if ret is not None else ""
#插入一个任务，从redis中获取uid为123玩家的信息。
redisPool.AsyncFuncWithKey(GetValueFromKey, "player_123", Cb1, 123)
#插入同样任务，orderKey都是“player_123”,因此两个任务会顺序执行。
redisPool.AsyncFuncWithKey(GetValueFromKey, "player_123", Cb1, 123)
redisPool.Finish()
 ```
<span id="AsyncGet"></span>
#### AsyncGet

- 描述

    执行redis操作，获取key的value,相当于redis中执行命令:get key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | str | redis中的key |
    | callback | function | 回调函数，默认为空。函数输入参数是redis key对应的value字符串，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
def Cb1(t):
        #执行成功且存在redis key "player_123"情况下，t的一个示例值：'test_string_value'
        #执行成功且不存在redis key "player_123"情况下，t的值：None
        #执行失败时，key的值：None
        print "cb", t
redisPool.InitDB(30) #建立连接池
redisPool.AsyncGet("player_123", Cb1)
redisPool.Finish()
 ```
<span id="AsyncHgetall"></span>
#### AsyncHgetall

- 描述

    执行redis操作，获取key的value,相当于redis中执行命令:hgetall key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | string | redis中的key |
    | callback | function | 回调函数，输入参数是redis key对应的值，是个dict，它在主线程执行。可以不传入回调函数。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
def Cb1(t):
        #执行成功且redis key "player_123"不为空情况下，t的一个示例值：{'name': 'name', 'lv': '2'}
        #执行成功且redis key "player_123"为空情况下，t的值：{}
        #执行失败时，t的值：None
        print "cb", t
redisPool.InitDB(30) #建立连接池
redisPool.AsyncHgetall("h_player_123", Cb1)
redisPool.Finish()
 ```
<span id="AsyncMget"></span>
#### AsyncMget

- 描述

    执行redis操作，获取多个key的值,相当于redis中执行命令:mget key1 key2 ...
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | list/tuple | 多个redis中的key |
    | callback | function | 回调函数，默认为空。函数输入参数redis操作返回值, 是个列表，每个元素对应单个redis key的值，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
def Cb1(t):
        #执行成功且redis key "test_value_None"不存在情况下，t的一个示例值：{'1': 'str', None}
        #执行失败时，t的值：None
        print "cb", t
redisPool.InitDB(30) #建立连接池
keys = ("test_value_1", "test_value_str", "test_value_None")
redisPool.AsyncMget(keys, Cb1)
redisPool.Finish()
 ```
<span id="AsyncSet"></span>
#### AsyncSet

- 描述

    执行redis操作，设置key的值为value,相当于redis中执行命令:set key value
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | key | string | redis中的key |
    | value | string | redis中key的值 |
    | callback | function | 回调函数，默认为空。函数输入参数是redis操作返回值，True表示设置成功，False失败。 若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
redisPool.InitDB(30) #建立连接池
def cb1(t):
        #执行成功时，t的值：True
        #执行失败时，t的值：False
        print "cb", t
redisPool.AsyncSet('player_123', "{'name':'nickname'}", cb1)
redisPool.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待redis线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
redisPool.InitDB(30) #建立连接池
#添加异步任务。在redis中执行:set "key1", "value11"
redisPool.AsyncSet("key1", "value11")
redisPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化redis连接池，要求在MCStudio的“服务器配置”中配置redis
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 示例

```python
import apolloCommon.redisPool as redisPool
redisPool.InitDB(30)
 ```
下面是mongo线程池的接口

<span id="mongo连接池"></span>
### mongo连接池

<span id="AsyncExecute"></span>
#### AsyncExecute

- 描述

    添加一个异步mongo任务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | collection | str | mongo中的一个集合，相同集合的所有操作串行执行，不同集合操作并行执行 |
    | func | function | mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的其它非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用 |
- 返回值

    无
- 备注

    query mongo数据库返回的字典中，大于signed int的整数，返回的数据类型并不是int，而是bson.int64.Int64(虽然直接打印的结果类似【50000L】)，bson.int64.Int64类型的数据无法作为eventData发送给客户端或功能服，需要使用API:ConvertBsonToInt转换为Int类型
    
    
- 示例

```python
import apolloCommon.mongoPool as mongoPool
mongoPool.InitDB(32)
def Insert(col):
        postData = {
                'title': 'Python and MongoDB',
                'content': 'PyMongo is fun, you guys',
                'author': 'Scott'
        }
        col.insert_one(postData)
def Cb(t):
        print "cb", t
#添加异步任务。
mongoPool.AsyncExecute("test_col", Insert, Cb)
mongoPool.Finish()
 ```
<span id="AsyncExecuteWithOrderKey"></span>
#### AsyncExecuteWithOrderKey

- 描述

    添加一个异步mongo任务。同async_execute区别是，可以显示设置orderKey
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | collection | str | mongo中的一个集合 |
    | func | function | mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接 |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的其它非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用。 |
- 返回值

    无
- 备注

    query mongo数据库返回的字典中，大于signed int的整数，返回的数据类型并不是int，而是bson.int64.Int64(虽然直接打印的结果类似【50000L】)，bson.int64.Int64类型的数据无法作为eventData发送给客户端或功能服，需要使用API:ConvertBsonToInt转换为Int类型
    
    
- 示例

```python
import apolloCommon.mongoPool as mongoPool
mongoPool.InitDB(32)
def Insert(col):
        postData = {
                'title': 'Python and MongoDB',
                'content': 'PyMongo is fun, you guys',
                'author': 'Scott'
        }
        col.insert_one(postData)
def Cb(t):
        print "cb", t
#添加异步任务。
#下面操作相当于:mongoPool.AsyncExecute("test_col", Insert, Cb)
mongoPool.AsyncExecuteWithOrderKey("test_col", Insert, "test_col", Cb)
#添加相同任务，两个任务顺序执行。
mongoPool.AsyncExecuteWithOrderKey("test_col", Insert, "test_col", Cb)
mongoPool.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待mongo线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.mongoPool as mongoPool
mongoPool.InitDB(32)
mongoPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化mongo连接池，要求在MCStudio的“服务器配置”中配置mongo
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 示例

```python
import apolloCommon.mongoPool as mongoPool
mongoPool.InitDB(32)
 ```
下面是mysql扩展线程池的一些接口

<span id="mysql连接池扩展"></span>
### mysql连接池扩展

<span id="AsyncExecuteWithOrderKey"></span>
#### AsyncExecuteWithOrderKey

- 描述

    添加一个异步mysql任务，执行所有mysql操作。同AsyncExecute的区别是可以显示指定orderKey
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | string | mysql db名字，名字在deploy.json中extra_mysql下配置，具体参见[InitDB](#InitDB)备注说明 |
    | orderKey | string/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | string | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraMysqlPool as extraMysqlPool
extraMysqlPool.InitDB('mysql_test1', 30)
def Cb(t):
        print "cb", t
#添加异步任务
extraMysqlPool.AsyncExecuteWithOrderKey('mysql_test1', 'player', 'insert into player values (%s, %s)', (1, "test1"), Cb)
extraMysqlPool.Finish()
 ```
<span id="AsyncQueryWithOrderKey"></span>
#### AsyncQueryWithOrderKey

- 描述

    添加一个异步mysql任务，执行mysql查询。同AsyncQuery区别是可以显示指定orderKey
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | string | mysql db名字，名字在deploy.json中extra_mysql下配置，具体参见[InitDB](#InitDB)备注说明 |
    | orderKey | string/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | sql | string | mysql查询语句，格式化字符串 |
    | params | tuple | 填充sql |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraMysqlPool as extraMysqlPool
extraMysqlPool.InitDB('mysql_test1', 30)
def Cb(t):
        print "cb", t
#添加异步任务
extraMysqlPool.AsyncQueryWithOrderKey('mysql_test1', 'player', 'select uid,name from player where uid = %s', (1,), Cb)
#orderKey都是'player'，两个任务顺序执行
extraMysqlPool.AsyncQueryWithOrderKey('mysql_test1','player', 'select uid,name from player where uid = %s', (1,), Cb)
extraMysqlPool.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待mysql线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.extraMysqlPool as extraMysqlPool
extraMysqlPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化mysql连接池。可以支持多个mysql实例，它可以同“mysql连接池”一起使用。MCStudio打开配置文件目录，在deploy.json文件中配置extra_mysql，配置方法参见备注
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | string | mysql db名字，名字在deploy.json中extra_mysql下配置，比如示例配置中 “mysql_test1” |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 备注

    deploy.json中部分配置的示例如下：
    ```
    "mysql": {
    "database": "mod_test",
    "host": "127.0.0.1",
    "password": "test",
    "port": 3306,
    "user": "test"
    },
    "extra_mysql":{
    "test1":{
    "database": "mysql_test1",
    "host": "127.0.0.2",
    "password": "test",
    "port": 3306,
    "user": "test"
    },
    "test2":{
    "database": "mysql_test2",
    "host": "127.0.0.3",
    "password": "test",
    "port": 3306,
    "user": "test"
    }
    },
    ```
    
    
- 示例

```python
import apolloCommon.extraMysqlPool as extraMysqlPool
extraMysqlPool.InitDB('mysql_test1', 30)
 ```
下面是redis扩展线程池的一些接口

<span id="redis连接池扩展"></span>
### redis连接池扩展

<span id="AsyncDelete"></span>
#### AsyncDelete

- 描述

    执行redis操作，删除某个redis key,相当于redis中执行命令:del key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | key | str | redis中的key |
    | callback | function | 回调函数，默认为空。函数输入参数是redis操作返回值,是个int，表示删除redis key的个数 ,它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
def Cb1(t):
        print "cb", t
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
extraRedisPool.AsyncDelete('extra_redis1', 'player_121', Cb1)
extraRedisPool.Finish()
 ```
<span id="AsyncFuncWithKey"></span>
#### AsyncFuncWithKey

- 描述

    添加一个异步redis任务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | func | function | redis异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个redis长连接，是一个redis.StrictRedis实例，其他参数是*args |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值是callback的输入参数。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的其它非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用 |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
#回调，可以获取player的信息。这里只是打印结果。
def Cb1(t):
        print "cb", t
#第一个参数是redis.StrictRedis实例。
def GetValueFromKey(conn, key):
        return conn.get(key)
#插入一个任务，从redis中获取uid为123玩家的信息。
extraRedisPool.AsyncFuncWithKey('extra_redis1', GetValueFromKey, 'player_123', Cb1, 123)
#插入同样任务，orderKey都是“player_123”,因此两个任务会顺序执行。
extraRedisPool.AsyncFuncWithKey('extra_redis1', GetValueFromKey, 'player_123', Cb1, 123)
extraRedisPool.Finish()
 ```
<span id="AsyncGet"></span>
#### AsyncGet

- 描述

    执行redis操作，获取key的value,相当于redis中执行命令:get key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | key | str | redis中的key |
    | callback | function | 回调函数，默认为空。函数输入参数是redis key对应的value字符串，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
def Cb1(t):
        print "cb", t
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
extraRedisPool.AsyncGet('extra_redis1','player_123', Cb1)
extraRedisPool.Finish()
 ```
<span id="AsyncHgetall"></span>
#### AsyncHgetall

- 描述

    执行redis操作，获取key的value,相当于redis中执行命令:hgetall key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | key | str | redis中的key |
    | callback | function | 回调函数，默认为空，函数输入参数是redis key对应的值，是个dict，它在主线程执行。若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
def Cb1(t):
        print "cb", t
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
extraRedisPool.AsyncHgetall('extra_redis1', 'player_123', Cb1)
extraRedisPool.Finish()
 ```
<span id="AsyncMget"></span>
#### AsyncMget

- 描述

    执行redis操作，获取多个key的值,相当于redis中执行命令:mget key1 key2 ...
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | keys | list/tuple | 多个redis key |
    | callback | function | 回调函数，默认为空，函数输入参数redis操作返回值, 是个列表，每个元素对应单个redis key的值，它在主线程执行。若redis操作抛出异常，则callback输入参数是None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
def Cb1(t):
        print "cb", t
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
keys = ('player_121', 'player_122')
extraRedisPool.AsyncMget('extra_redis1', keys, Cb1)
extraRedisPool.Finish()
 ```
<span id="AsyncSet"></span>
#### AsyncSet

- 描述

    执行redis操作，设置key的值为value,相当于redis中执行命令:set key value
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis db名字，名字对应MCStudio中新增redis实例的实例名称 |
    | key | str | redis中的key |
    | value | str | redis中key的值 |
    | callback | function | 回调函数，默认为空。函数输入参数是redis操作返回值，True表示设置成功，False失败。 若redis操作抛出异常，则callback输入参数是None。若没有回调，则传入None |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
extraRedisPool.AsyncSet('extra_redis1', 'player_123', "{'name':'nickname'}")
extraRedisPool.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待redis db线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
extraRedisPool.InitDB('extra_redis1', 30) #建立连接池
#回调，可以获取player的信息。这里只是打印结果。
def Cb1(t):
        print "cb", t
#第一个参数是redis.StrictRedis实例。
def GetValueFromKey(conn, key):
        return conn.get(key)
#插入一个任务，从redis中获取uid为123玩家的信息。
extraRedisPool.AsyncFuncWithKey('extra_redis1', GetValueFromKey, 'player_123', Cb1, 123)
extraRedisPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化redis连接池，要求在MCStudio的“服务器配置”中“新增redis实例”
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | redis实例名字，对应MCStudio中redis“实例名称”配置 |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 示例

```python
import apolloCommon.extraRedisPool as extraRedisPool
extraRedisPool.InitDB('extra_redis1', 30)
 ```
下面是mongo扩展线程池的一些接口

<span id="mongo连接池扩展"></span>
### mongo连接池扩展

<span id="AsyncExecute"></span>
#### AsyncExecute

- 描述

    添加一个异步mongo任务
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | mongo db名字，名字在deploy.json中extra_mongo下配置，具体参见[InitDB](#InitDB)备注说明 |
    | collection | str | mongo中的一个集合，相同集合的所有操作串行执行，不同集合操作并行执行 |
    | func | function | mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留用 |
- 返回值

    无
- 示例

```python
import apolloCommon.extraMongoPool as extraMongoPool
extraMongoPool.InitDB('mongo_test1', 32)
def Insert(col):
        postData = {
                'title': 'Python and MongoDB',
                'content': 'PyMongo is fun, you guys',
                'author': 'Scott'
        }
        col.insert_one(postData)
def Cb(t):
        print "cb", t
#添加异步任务。
extraMongoPool.AsyncExecute('mongo_test1', 'test_col', Insert, Cb)
extraMongoPool.Finish()
 ```
<span id="AsyncExecuteWithOrderKey"></span>
#### AsyncExecuteWithOrderKey

- 描述

    添加一个异步mongo任务。同async_execute区别是，可以显示设置orderKey
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | mongo db名字，名字在deploy.json中extra_mongo下配置，具体参见[InitDB](#InitDB)备注说明 |
    | collection | str | mongo中的一个集合 |
    | func | function | mongo异步任务，可以没有返回值。该任务和主线程会并行执行，要求任务是线程安全的。第一个参数是一个mongo长连接，是pymongo.MongoClient连接池实例中的一个连接，其他参数是*args |
    | orderKey | str/int | 相同的orderKey会顺序执行，不同的orderKey会并行执行 |
    | callback | function | 回调函数，只有一个输入参数，它在主线程执行。func的返回值会是callback的实参。若func抛出异常，则callback输入参数是None。若没有回调，则传入None |
    | *args | *args | func的非关键字参数 |
    | **kwargs | **kwargs | 暂无用，预留 |
- 返回值

    无
- 示例

```python
import apolloCommon.extraMongoPool as extraMongoPool
extraMongoPool.InitDB('mongo_test1', 32)
def Insert(col):
        postData = {
                'title': 'Python and MongoDB',
                'content': 'PyMongo is fun, you guys',
                'author': 'Scott'
        }
        col.insert_one(postData)
def Cb(t):
        print "cb", t
#添加异步任务
#下面操作相当于:apolloCommon.AsyncExecute('mongo_test1', 'test_col', Insert, Cb)
apolloCommon.AsyncExecuteWithOrderKey('mongo_test1', 'test_col', Insert, 'test_col', Cb)
#添加相同任务，两个任务顺序执行
apolloCommon.AsyncExecuteWithOrderKey('mongo_test1', 'test_col', Insert, 'test_col', Cb)
apolloCommon.Finish()
 ```
<span id="Finish"></span>
#### Finish

- 描述

    等待mongo线程池退出，会等待线程池中所有异步任务执行完毕后退出
    
- 返回值

    无
- 示例

```python
import apolloCommon.extraMongoPool as extraMongoPool
extraMongoPool.Finish()
 ```
<span id="InitDB"></span>
#### InitDB

- 描述

    初始化mongo连接池。可以支持多个mongo实例，它可以同“mongo连接池”一起使用。MCStudio打开配置文件目录，在deploy.json文件中配置extra_mongo，配置方法参见备注
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | dbName | str | mongo db名字，名字在deploy.json中extra_mongo下配置，比如示例配置中 “mongo_test1” |
    | poolSize | int | 连接池大小 |
- 返回值

    无
- 备注

    deploy.json部分配置的示例如下：
    ```
    "mongo": {
    "database": "test",
    "host": "127.0.0.1",
    "password": "test",
    "port": 27017,
    "user": "test"
    },
    "extra_mongo":{
    "testname1" : {
    "database": "mongo_test1",
    "host": "127.0.0.2",
    "password": "test",
    "port": 27017,
    "user": "test"
    },
    "testname2" : {
    "database": "mongo_test2",
    "host": "127.0.0.3",
    "password": "test",
    "port": 27017,
    "user": "test"
    }
    },
    ```
    
    
- 示例

```python
import apolloCommon.extraMongoPool as extraMongoPool
extraMongoPool.InitDB('mongo_test1', 30)
 ```
下面是公共的接口

<span id="通用"></span>
### 通用

<span id="ChangeDatabaseSlowLogLimit"></span>
#### ChangeDatabaseSlowLogLimit

- 描述

    修改数据库连接池慢请求报警日志限定时间
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | db | str | 数据库连接池类型，mysql/redis/mongo |
    | interval | float | 慢请求限制时间，单个请求返回时间超过这个值就会记录慢请求日志，单位秒，mysql和mongo默认配置值为1.0秒，redis默认配置为0.1秒 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
suc = commonNetgameApi.ChangeDatabaseSlowLogLimit("mysql", 0.1)
print "ChangeDatabaseSlowLogLimit for mysql suc=%s" % suc
 ```
<span id="CheckNameValid"></span>
#### CheckNameValid

- 描述

    判定一个输入的string是否通过了命名库敏感词检查，没有敏感词返回1，存在敏感词返回0
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | name | str | 需要做敏感词检查的string |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 1代表没有敏感词，0代表存在敏感词 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
isOk = commonNetgameApi.CheckNameValid("xxxxxx")
if not isOk:
        print "输入中存在敏感词"
        return
 ```
<span id="CheckWordsValid"></span>
#### CheckWordsValid

- 描述

    判定一个输入的string是否通过了通用库敏感词检查，没有敏感词返回1，存在敏感词返回0
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | words | str | 需要做敏感词检查的string |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 1代表没有敏感词，0代表存在敏感词 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
isOk = commonNetgameApi.CheckSensitiveByName("xxxxxx")
if not isOk:
        print "输入中存在敏感词"
        return
 ```
<span id="CloseAsyncTaskSlowCheck"></span>
#### CloseAsyncTaskSlowCheck

- 描述

    停止每帧检查异步线程池中的任务
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.CloseAsyncTaskSlowCheck()
 ```
<span id="ConvertBsonToInt"></span>
#### ConvertBsonToInt

- 描述

    递归转换输入数据中的所有bson.int64.Int64类型的对象为int类型
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | input | dict/list/tuple/str/unicode | 需要转换的输入数据 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict/list/tuple/str/unicode | 和输入数据格式相同，其中bson.int64.Int64类型的对象会被转换为int类型 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
import bson
bsonInt = bson.Int64(5000000000)
input = {
        "a1": bsonInt,
        "a2": [bsonInt, bsonInt],
        "a3": (bsonInt, bsonInt),
}
ret = commonNetgameApi.ConvertBsonToInt(input)
 ```
<span id="DumpAsyncTaskPool"></span>
#### DumpAsyncTaskPool

- 描述

    打印当前异步线程池中的正在排队和执行中的任务信息
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.DumpAsyncTaskPool()
 ```
<span id="GetApolloGameId"></span>
#### GetApolloGameId

- 描述

    获取游戏当前项目的gameId（商城查询订单时需要）
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 游戏当前项目的gameId |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
gameId = commonNetgameApi.GetApolloGameId()
 ```
<span id="GetApolloGameKey"></span>
#### GetApolloGameKey

- 描述

    获取游戏当前项目的gameKey（商城查询订单时需要）
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 游戏当前项目的gameKey |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
gameKey = commonNetgameApi.GetApolloGameKey()
 ```
<span id="GetApolloReviewStage"></span>
#### GetApolloReviewStage

- 描述

    获取游戏当前审核阶段
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 0 测试阶段，1 审核阶段 2 上线阶段 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
reviewStage = commonNetgameApi.GetApolloReviewStage()
 ```
<span id="GetApolloUniqueId"></span>
#### GetApolloUniqueId

- 描述

    获取游戏当前项目唯一ID
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int | 游戏当前项目唯一ID |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
apolloId = commonNetgameApi.GetApolloUniqueId()
 ```
<span id="GetModJsonConfig"></span>
#### GetModJsonConfig

- 描述

    根据脚本根目录读取mod.json配置文件。要求mod已经被加载
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | scriptRootName | str | python脚本的根目录名 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | mod.json里面的内容信息 |
- 示例

```python
#目录结构
# |-developer_mods
#       |- neteaseNpcLobbyDev
#               mod.json
#               |- neteaseNpcLobby
import apolloCommon.commonNetgameApi as commonNetgameApi
confDict = commonNetgameApi.GetModJsonConfig("neteaseNpcLobby")
print confDict["description"]#打印mod.json中description配置内容
#mod.json取出的字符串都是unicode编码。若是中文，需要手动转成UTF-8编码。转码方法如下：
npcName = confDict["name"].encode('utf-8')
 ```
<span id="GetModJsonConfigByName"></span>
#### GetModJsonConfigByName

- 描述

    读取基于脚本根目录的[pathFile]路径下的json格式配置文件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | scriptRootName | str | python脚本的根目录名 |
    | pathFile | str | 相对于python脚本的根目录的文件名（包括相对路径） |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict | 对应目录下json文件里面的内容信息 |
- 示例

```python
#目录结构
# |-developer_mods
#       |- neteaseNpcLobbyDev
#               mod.json
#               |- neteaseNpcLobby
#               |- modData
#                       skill1.json
import apolloCommon.commonNetgameApi as commonNetgameApi
confDict = commonNetgameApi.GetModJsonConfig("neteaseNpcLobby", "modData/skill1.json")
print confDict # 打印skill1.json文件的内容
#json取出的字符串都是unicode编码。若是中文，需要手动转成UTF-8编码。转码方法如下：
npcName = confDict["name"].encode('utf-8')
 ```
<span id="GetModScriptRootDir"></span>
#### GetModScriptRootDir

- 描述

    获取脚本根目录的绝对路径。要求mod已经被加载
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | scriptRootName | str | python脚本的根目录名 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 脚本根目录的绝对路径 |
- 示例

```python
#目录结构
# |-developer_mods
#       |- neteaseNpcLobbyDev
#               mod.json
#               |- neteaseNpcLobby
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.GetModScriptRootDir("neteaseNpcLobby")
#结果:/home/fuzhu/netgame/app/template/lobby/lobby_lobby_2000000/developer_mods/neteaseNpcLobbyDev/
 ```
<span id="GetServerType"></span>
#### GetServerType

- 描述

    获取本服的服务器类型，对应MCStudio中配置：服务器配置->游戏配置->类型
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 服务器类型 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.GetServerType() #结果是:"gameBattleA"
 ```
<span id="OpenAsyncTaskSlowCheck"></span>
#### OpenAsyncTaskSlowCheck

- 描述

    启动每帧检查异步线程池中的任务，并且打印执行时间超过指定时间且尚未完成的任务，此功能消耗较大，仅建议在测试阶段和遇到线上紧急问题时启用
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | interval | float | 任务限制时间，单个任务进入异步线程池排队+执行时间超过此时间还没有完成的，会以warning日志的形式输出 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.OpenAsyncTaskSlowCheck(0.01)
 ```
<span id="StartDatabaseProfile"></span>
#### StartDatabaseProfile

- 描述

    开始记录数据库连接池请求信息统计，启动后调用[StopDatabaseMysqlProfile(db)](#StopDatabaseMysqlProfile)即可获取两个函数调用之间数据库连接池请求记录信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | db | str | 数据库连接池类型，mysql/redis/mongo |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.StartDatabaseProfile("mysql")
# 之后通过计时器或者其他触发方式调用StopDatabaseMysqlProfile
result = commonNetgameApi.StopDatabaseMysqlProfile("mysql")
for single in result:
        action = single["action"]
        if action == "executefunc":
                print "do {} func={} orderKey={} cost={}s ret={}".format(action, single["func"], single["orderKey"], single["costTp"], single["ret"])
        else:
                print "do {} orderKey={} cost={}s ret={}".format(action, single["orderKey"], single["costTp"], single["ret"])
 ```
<span id="StartYappiProfile"></span>
#### StartYappiProfile

- 描述

    开始启动服务端脚本性能分析，启动后调用[StopYappiProfile(path)](#StopYappiProfile)即可在路径path生成函数性能火焰图
    
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.StartYappiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopYappiProfile
commonNetgameApi.StopYappiProfile()
 ```
<span id="StopDatabaseMysqlProfile"></span>
#### StopDatabaseMysqlProfile

- 描述

    停止记录数据库连接池请求信息并输出统计结果，与[StartDatabaseProfile(db)](#StartDatabaseProfile)配合使用，输出结果为字典，具体见示例
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | db | str | 数据库连接池类型，mysql/redis/mongo |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | list | 数据库连接池请求统计信息，具体见示例，假如没有调用过StartDatabaseProfile，则返回为None |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.StartDatabaseProfile("mysql")
# 之后通过计时器或者其他触发方式调用StopDatabaseMysqlProfile
result = commonNetgameApi.StopDatabaseMysqlProfile("mysql")
for single in result:
        action = single["action"]
        if action == "executefunc":
                print "do {} func={} orderKey={} cost={}s".format(action, single["func"], single["orderKey"], single["costTp"])
        else:
                print "do {} orderKey={} cost={}s".format(action, single["orderKey"], single["costTp"])
 ```
<span id="StopYappiProfile"></span>
#### StopYappiProfile

- 描述

    停止服务端脚本性能分析并生成火焰图，与[StartYappiProfile()](#StartYappiProfile)配合使用
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于Apollo服务端启动目录的路径，默认为"flamegraph.svg"，位于Apollo服务端启动目录下，自定义路径请确保文件后缀名为".svg" |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.StartYappiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopYappiProfile
commonNetgameApi.StopYappiProfile()
 ```
<span id="UnicodeConvert"></span>
#### UnicodeConvert

- 描述

    递归转换输入数据中的所有unicode格式的字符串为utf-8格式
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | input | dict/list/tuple/str/unicode | 需要转换的输入数据 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | dict/list/tuple/str/unicode | 和输入数据格式相同，其中的unicode格式的字符串会被转换为utf-8格式 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
unicodeStr = "我是unicode编码的".decode("utf-8")
input = {
        "a1": unicodeStr,
        "a2": [unicodeStr, unicodeStr],
        "a3": (unicodeStr, unicodeStr),
}
ret = commonNetgameApi.UnicodeConvert(input)
 ```
<span id="世界"></span>
### 世界

<span id="AddRepeatedTimer"></span>
#### AddRepeatedTimer

- 描述

    添加服务端触发的定时器，重复执行
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | func | 定时器触发函数 |
    | *args | *args | 变长参数，可以不设置 |
    | **kwargs | **kwargs | 字典变长参数，可以不设置 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | timer | 返回单次触发的定时器 |
- 示例

```python
def doRepeatPrint(info):
        print "doRepeatPrint", info
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.AddRepeatedTimer(2.0, doRepeatPrint, "this is repeat timer")
 ```
<span id="AddTimer"></span>
#### AddTimer

- 描述

    添加服务端触发的定时器，非重复
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | func | 定时器触发函数 |
    | *args | *args | 变长参数，可以不设置 |
    | **kwargs | **kwargs | 字典变长参数，可以不设置 |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | timer | 返回单次触发的定时器 |
- 示例

```python
def doOncePrint(info):
        print "doOncePrint", info
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.AddTimer(5.0, doOncePrint, "this is once timer")
 ```
<span id="CancelTimer"></span>
#### CancelTimer

- 描述

    取消定时器
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | timer | timer对象 | AddTimer和AddRepeatedTimer时返回的定时器对象 |
- 返回值

    无
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.CancelTimer(timer)
 ```
<span id="玩家"></span>
### 玩家

<span id="GetOnlineKey"></span>
#### GetOnlineKey

- 描述

    输入玩家uid，返回此玩家保存在redis中的在线标识的key
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 此玩家保存在redis中的在线标识的key；它是个hash表，包含两个hash key:serverid,proxyid，假如无法获取到或者只获取到proxyid获取不到serverid，说明此玩家当前不在线 |
- 示例

```python
import apolloCommon.commonNetgameApi as commonNetgameApi
onlineKey = commonNetgameApi.GetOnlineKey(123)
 ```
<span id="GetOnlineServerInfoOfMultiPlayers"></span>
#### GetOnlineServerInfoOfMultiPlayers

- 描述

    获取多个玩家在线信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uids | list(int/long) | 玩家的netease uid列表，列表不能超过100，若超过100，本api会抛出Exception |
    | callback | function | 回调函数，该函数会被异步执行。函数只需要一个参数，是list(dict)类型。每个dict包含的键以及含义说明："uid":玩家的netease uid；      "serverId"：玩家所在lobby或game的服务器id， 若玩家不在线则为None;"proxyId"：客户端连接的proxy服务器id， 若玩家不在线则为None;     "protocolVersion"：玩家客户端协议版本号， 若玩家不在线则为None |
- 返回值

    无
- 示例

```python
def GetPlayersOnlineCb(args):
        #若参数是：{["uid":123, "isPeUser":True, "serverId" :2000000, "proxyId" :1000000, "protocolVersion":422},{"uid":234, "isPeUser":False, "serverId" :None, "proxyId" :None, "protocolVersion":None}]
        #参数含义：第一个玩家uid是123，玩家最后一次登录游戏是从手机端登录的，玩家是在线的，所在lobby或game的服务器id是2000000，玩家连接的proxy服务器id是1000000，玩家客户端协议版本号是422；
        # 第二个玩家玩家uid是234，玩家最后一次登录游戏是从PC端登录的，玩家是离线的
        print 'GetOnlineServerCb', args
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.GetOnlineServerInfoOfMultiPlayers([123, 234], GetPlayersOnlineCb)
 ```
<span id="GetOnlineServerInfoOfPlayer"></span>
#### GetOnlineServerInfoOfPlayer

- 描述

    获取玩家在线信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |
    | callback | function | 回调函数，该函数会被异步执行。函数只需要一个参数，是dict类型。dict包含的键以及含义说明："uid":玩家的netease uid；  "serverId"：玩家所在lobby或game的服务器id， 若玩家不在线则为None;"proxyId"：客户端连接的proxy服务器id， 若玩家不在线则为None；   "protocolVersion"：玩家客户端协议版本号， 若玩家不在线则为None |
- 返回值

    无
- 示例

```python
def GetOnlineCb(args):
        #若参数是：{"uid":123, "isPeUser":True, "serverId" :2000000, "proxyId" :1000000, "protocolVersion":422}
        #参数含义：玩家uid是123，玩家最后一次登录游戏是从手机端登录的，玩家是在线的，所在lobby或game的服务器id是2000000，玩家连接的proxy服务器id是1000000，玩家客户端协议版本号是422
        #若参数是：{"uid":123, "isPeUser":False, "serverId" :None, "proxyId" :None, "protocolVersion":None}
        #参数含义：玩家uid是123，玩家最后一次登录游戏是从PC端登录的，玩家是离线的
        #参数含义：isPeUser的值是None的话，说明此玩家从来没有登录过本游戏
        print 'GetOnlineServerCb', args
import apolloCommon.commonNetgameApi as commonNetgameApi
commonNetgameApi.GetOnlineServerInfoOfPlayer(123, GetOnlineCb)
 ```
<span id="GetWeekOnlineKey"></span>
#### GetWeekOnlineKey

- 描述

    输入玩家uid，返回此玩家保存在redis中的本周的在线时间
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | str | 此玩家保存在redis中的本周在线时间的key；它是个string，转化为int后就是此玩家本周在线时间的秒数 |
<span id="ToPcUid"></span>
#### ToPcUid

- 描述

    将玩家的uid转换为pc平台的uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int/long | pc平台的玩家uid |
<span id="ToPeUid"></span>
#### ToPeUid

- 描述

    将玩家的uid转换为pe平台的uid
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的uid |
- 返回值

    | 数据类型 | 说明 |
    | :--- | :--- |
    | int/long | pe平台的玩家uid |

## 8-服务器通信

# <span id="8-服务器通信"></span>8-服务器通信

### 通信接口图示

通信接口图示如下

细箭头为单点消息，粗箭头为广播消息



#### 客户端通信接口

发往客户端消息的接口如下

![transaction_client](../images/transaction_client.png)



#### lobby/game通信接口

发往lobby/game消息的接口如下

![transaction_game](../images/transaction_game.png)



#### 控制服通信接口

发往控制服消息的接口如下

![transaction_master](../images/transaction_master.png)

#### 功能服通信接口

发往功能服消息的接口如下

![transaction_service](../images/transaction_service.png)



#### 功能服RPC调用流程

1. **功能服**调用`RegisterRpcMethodForMod`注册RPC调用，设置回调函数为`ServiceCallback`
2. **控制服/lobby/game**调用`RequestToServiceMod`触发RPC调用，同时设置回调函数为`ServerCallback`
3. **功能服**执行`ServiceCallback`
4. **功能服**发送响应消息到**控制服/lobby/game**
5. **控制服/lobby/game**执行回调`ServerCallback`

流程如下

![tranasaction_rpc](../images/tranasaction_rpc.png)
Apollo通信相关api。

<span id="client和game/lobby通信"></span>
### client和game/lobby通信

<span id="NotifyToClient"></span>
#### NotifyToClient

- 描述

    game/lobby接口，game/lobby发送事件到指定客户端
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 玩家playerId |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#服务端给客户端发送消息的示例
#client mod
class testClient(ClientSystem):
        def __init__(self,namespace,systemName):
                ClientSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('serverNamespace', 'serverSystem', 'PlayerJoinOKEvent', self, self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
#game/lobby mod
class testServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def testNotifyClient(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                playerId = '456'
                self.NotifyToClient(playerId, "PlayerJoinOKEvent", player)
 ```
<span id="NotifyToServer"></span>
#### NotifyToServer

- 描述

    客户端接口，给lobby/game服务器发送事件。注意，玩家只能存在于一个game或lobby，不可能同时存在于两个服务器
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#客户端给服务端发送消息的示例
#client mod
class testClient(ClientSystem):
        def __init__(self,namespace,systemName):
                ClientSystem.__init__(self, namespace, systemName)
        def testNotifyServer(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.NotifyToServer("PlayerJoinEvent", data)
#game/lobby mod
class testServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('clientNamespace', 'clientSystem', 'PlayerJoinEvent', self, self.OnPlayerJoin)
        def OnPlayerJoin(self, args):
                #args结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoin', args
 ```
Apollo通信相关api。

<span id="master和game/lobby通信"></span>
### master和game/lobby通信

<span id="NotifyToMaster"></span>
#### NotifyToMaster

- 描述

    lobby/game接口，lobby/game给master发事件。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#服务器给master发消息的示例
#master mod
class testMaster(MasterSystem):
        def __init__(self,namespace,systemName):
                MasterSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('lobbyNamespace', 'lobbySystem', 'PlayerJoinOKEvent', self, self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def testNotifyMaster(self, args):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.NotifyToMaster("PlayerJoinOKEvent", player)
 ```
<span id="NotifyToServerNode"></span>
#### NotifyToServerNode

- 描述

    master接口，master给某个lobby/game发事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | int | lobby/game的服务器id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#master给某个服务器发消息的示例
#master mod
class testMaster(MasterSystem):
        def __init__(self,namespace,systemName):
                MasterSystem.__init__(self, namespace, systemName)
        def testNotifyServer(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.NotifyToServerNode(4000, "PlayerJoinEvent", data)
#lobby mod，服务器id为4000
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('masterNamespace', 'masterSystem', 'PlayerJoinEvent', self, self.OnPlayerJoin)
        def OnPlayerJoin(self, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoin', args
 ```
Apollo通信相关api。

<span id="service和master通信"></span>
### service和master通信

<span id="BroadcastToService"></span>
#### BroadcastToService

- 描述

    master接口，master给所有service广播消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#master给所有service广播消息。
#service mod
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.ListenForEvent("NeteaseExtraApi", "extraApiMaster", "MasterBroadcastEvent", self, self.OnMasterBroadcastEvent)
        def OnMasterBroadcastEvent(self, args):
                print "OnMasterBroadcastEvent", args
        
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
                masterHttp.RegisterMasterHttp("/api/service-broadcast-event", self, self.OnServiceBroadcastEvent)
        def OnServiceBroadcastEvent(self, clientId, requestBody):
                reqData = json.loads(requestBody)
                self.BroadcastToService("MasterBroadcastEvent", reqData)
                responseBody = json.dumps({
                        'code': 0,
                        'message': "success",
                        'entity': {},
                })
                masterHttp.SendHttpResponse(clientId, responseBody)
 ```
<span id="NotifyToServiceNode"></span>
#### NotifyToServiceNode

- 描述

    master接口，master给某个service发消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | int | service的服务器id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#master给某个service发消息。
#service mod
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.ListenForEvent("NeteaseExtraApi", "extraApiMaster", "MasterEvent", self, self.OnMasterEvent)
        def OnMasterEvent(self, args):
                print "OnMasterEvent", args
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
                masterHttp.RegisterMasterHttp("/api/service-event", self, self.OnServiceEvent)
        def OnServiceEvent(self, clientId, requestBody):
                reqData = json.loads(requestBody)
                self.NotifyToServiceNode(8000, "MasterEvent", reqData)
                responseBody = json.dumps({
                        'code': 0,
                        'message': "success",
                        'entity': {},
                })
                masterHttp.SendHttpResponse(clientId, responseBody)
 ```
<span id="service和service/master通信"></span>
### service和service/master通信

<span id="RegisterRpcMethod"></span>
#### RegisterRpcMethod

- 描述

    service/master接口，用于监听service/master发过来请求，通常用于官方插件开发，服主请使用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)。要求：MCStudio打开配置文件目录，打开deploy.json文件，然后给service配置module_names信息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | module | str | service/master所属模块，deploy.json文件中module_names中某个module |
    | event | str | 事件名 |
    | func | function | 监听函数 |
- 返回值

    无
- 示例

```python
#service同master通信示例.service同service通信与此类似，这里不重复了
        #service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                #注册service方法，注意一个事件只能注册一次，否则后面监听函数会覆盖前面监听函数
                self.RegisterRpcMethod('idv_service','PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToService("idv_service", "PlayerJoinOKEvent", data, self.OnCallback, 2)
 ```
<span id="RegisterRpcMethodForMod"></span>
#### RegisterRpcMethodForMod

- 描述

    service接口，监听service/master发过来的请求。service/master使用[RequestToServiceMod](#RequestToServiceMod)发送请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | func | function | 监听函数 |
    | event | str | 事件名 |
- 返回值

    无
- 示例

```python
#service同master通信示例.service同service通信与此类似，这里不重复了
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                #注册service方法，注意一个事件只能注册一次，否则后面监听函数会覆盖前面监听函数
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", data, self.OnCallback, 2)
 ```
<span id="RequestToService"></span>
#### RequestToService

- 描述

    service/master接口，给service/master发请求，通常用于官方插件开发，服主请使用[RequestToServiceMod](#RequestToServiceMod)
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | module | str | service/master所属模块，需要在service mod的根目录新增mod.json文件并配置module_names，具体可以参考任意插件中service中mod.json配置 |
    | event | str | 事件名 |
    | eventData | dict | 事件参数 |
    | callback | function | 用于处理service/master返回消息， 默认为空，表示没有回调函数。回调函数参数包括：是否成功状态、service/master返回数据。若超时，则参数为False、None |
    | timeout | int | 回调函数超时时间，单位秒。默认是2s |
- 返回值

    无
- 示例

```python
#service同master通信示例.service同service通信与此类似，这里不重复了
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
        def OnCallbackFromMaster(self, suc, args):
                #若成功：suc=True，args= {'result' : 'hello'}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallbackFromMaster success', args
        def testNotifyMaster(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToService("master_module", "RequestMasterEvent", player, self.OnCallbackFromMaster, 2)
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
                #注册master方法，注意一个事件只能注册一次，否则后面监听函数会覆盖前面监听函数
                self.RegisterRpcMethod("master_module", 'RequestMasterEvent', self.OnRequestMaster)
        def OnRequestMaster(self, serverId, callbackId, args):
                #args结果为：{'uid':123, 'name':'nickname'}
                print 'OnRequestMaster', args
                response = {}
                response['result'] = 'hello'
                self.ResponseToServer(serverId, callbackId, response)
 ```
<span id="RequestToServiceMod"></span>
#### RequestToServiceMod

- 描述

    master接口，给service发请求。要求service调用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)监听请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | modname | string | service进程的type，对应MCStudio中功能服配置下的“类型”配置 |
    | method | string | 事件名 |
    | args | dict | 事件参数 |
    | callback | function | 用于处理service返回消息，默认为空，表示没有回调函数。回调函数参数包括：是否成功状态、service返回数据。若超时，则参数为False、None |
    | timeout | int | 回调函数超时时间，单位秒。默认是2s |
- 返回值

    无
- 示例

```python
#service同master通信示例.service同service通信与此类似，这里不重复了。
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                #注册service方法，注意一个事件只能注册一次，否则后面监听函数会覆盖前面监听函数
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", data, self.OnCallback, 2)
 ```
<span id="ResponseToServer"></span>
#### ResponseToServer

- 描述

    service/master接口，给service/master返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | master/service服务器id |
    | callbackId | int | 回调函数id |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service同master通信示例.service同service通信与此类似，这里不重复了
        #service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                #注册service方法，注意一个事件只能注册一次，否则后面监听函数会覆盖前面监听函数
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#master mod
class masterServer(MasterSystem):
        def __init__(self, namespace, systemName):
                MasterSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", data, self.OnCallback, 2)
 ```
Apollo通信相关api。

<span id="service和master通信"></span>
### service和master通信

<span id="NotifyToMaster"></span>
#### NotifyToMaster

- 描述

    service接口，service给master发消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service给master发消息。
#master mod
class MasterApiSys(MasterSystem):
        def __init__(self,namespace,systemName):
                MasterSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('NeteaseExtraApi', 'extraApiService', 'ServiceEvent', self, self.OnServiceEvent)
        def OnServiceEvent(self, args):
                print "OnServiceEvent", args
#service mod
class ServiceApiSys(ServiceSystem):
        def __init__(self, namespace, systemName):
                ServiceSystem.__init__(self, namespace, systemName)
        def DoSendToMaster(self, args):
                self.NotifyToMaster("ServiceEvent", args)
 ```
<span id="service和game/lobby通信"></span>
### service和game/lobby通信

<span id="BroadcastToServerByType"></span>
#### BroadcastToServerByType

- 描述

    service接口，service给某种类型服务器广播消息
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverType | str | lobby/game的服务类型 |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
import server.extraServiceApi as serviceApi
ServiceSystem = serviceApi.GetServiceSystemCls()
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
        def testNotify(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.BroadcastToServerByType('battle_game_server_type', 
                        "PlayerJoinEvent", player)
#lobby mod(服务器类型为battle_game_server_type)
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('serviceNamespace', 'serviceSystem', 
                        'PlayerJoinEvent', self, self.OnPlayerJoin)
        def OnPlayerJoin(self, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoin', args
 ```
<span id="BroadcastToService"></span>
#### BroadcastToService

- 描述

    service/lobby/game接口，service/lobby/game给所有service广播消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service/lobby/game给所有service广播消息。
#service mod
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.ListenForEvent("NeteaseExtraApi", "extraApiDev", "ServerBroadcastEvent", self, self.OnServerBroadcastEvent)
                self.ListenForEvent("NeteaseExtraApi", "extraApiService", "ServiceBroadcastEvent", self, self.OnServiceBroadcastEvent)
        def OnServerBroadcastEvent(self, args):
                print "OnServerBroadcastEvent", args
                self.BroadcastToService("ServiceBroadcastEvent", args)
        
        def OnServiceBroadcastEvent(self, args):
                print "OnServiceBroadcastEvent", args
        
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def DoBroadcastToService(self, args):
                self.BroadcastToService("ServerBroadcastEvent", args)
 ```
<span id="NotifyToServerNode"></span>
#### NotifyToServerNode

- 描述

    service接口，service给某个lobby/game发消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | int | lobby/game的服务器id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service给game/lobby发消息
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
        def testNotifyServer(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.NotifyToServerNode(4000, "PlayerJoinEvent", player)
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('serviceNamespace', 'serviceSystem', 'PlayerJoinEvent', self, self.OnPlayerJoin)
        def OnPlayerJoin(self, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoin', args
 ```
<span id="NotifyToServiceNode"></span>
#### NotifyToServiceNode

- 描述

    service/lobby/game接口，service/lobby/game给某个service发消息。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | targetId | int | service的服务器id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service/lobby/game给某个service发消息
#service mod
class ServiceApiSys(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.ListenForEvent("NeteaseExtraApi", "extraApiDev", "ServerEvent", self, self.OnServerEvent)
                self.ListenForEvent("NeteaseExtraApi", "extraApiService", "ServiceEvent", self, self.OnServiceEvent)
        def OnServerEvent(self, args):
                print "OnServerEvent", args
                self.NotifyToServiceNode(8001, "ServiceEvent", args)
        def OnServiceEvent(self, args):
                print "OnServiceEvent", args
        
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def DoSendToService(self, args):
                self.NotifyToServiceNode(8000, "ServerEvent", args)
 ```
<span id="RegisterRpcMethod"></span>
#### RegisterRpcMethod

- 描述

    service接口，通常用于官方插件开发，服主请使用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)。本接口注册一个监听函数，用于监听lobby/game发过来的请求。
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | module | str | service所属模块，需要在service mod的根目录新增mod.json文件并配置module_names，具体可以参考任意插件中service中mod.json配置 |
    | func | function | 监听函数 |
    | event | str | 事件名 |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.RegisterRpcMethod("idv_service", 'PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToService("idv_service", "PlayerJoinOKEvent", args)
 ```
<span id="RegisterRpcMethodForMod"></span>
#### RegisterRpcMethodForMod

- 描述

    service接口，监听lobby/game发过来的请求，lobby/game使用[RequestToServiceMod](#RequestToServiceMod)发送请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | method | string | 事件名 |
    | func | function | 监听函数 |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", args, self.OnCallback, 2)
 ```
<span id="RequestToService"></span>
#### RequestToService

- 描述

    service/lobby/game接口，通常用于官方插件开发，服主请使用[RequestToServiceMod](#RequestToServiceMod)。lobby/game给service发请求，两个service间可以通过这个接口通信
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | module | str | service所属模块，需要在service mod的根目录新增mod.json文件并配置module_names，具体可以参考任意插件中service中mod.json配置 |
    | event | str | 事件名 |
    | eventData | dict | 事件参数 |
    | callback | function | 用于处理service返回消息，默认为空，表示没有回调函数。回调函数参数包括：是否成功状态、service返回数据。若超时，则参数为False、None |
    | timeout | int | 回调函数超时时间，单位秒。默认是2s |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.RegisterRpcMethod("idv_service", 'PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToService("idv_service", "PlayerJoinOKEvent", args)
 ```
<span id="RequestToServiceMod"></span>
#### RequestToServiceMod

- 描述

    lobby/game接口，lobby/game给service发送事件。要求service调用[RegisterRpcMethodForMod](#RegisterRpcMethodForMod)监听请求
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | modname | string | service进程的type，对应MCStudio中功能服配置下的“类型”配置 |
    | method | string | 事件名 |
    | args | dict | 事件参数 |
    | callback | function | 用于处理service返回消息，默认为空，表示没有回调函数。回调函数参数包括：是否成功状态、service返回数据。若超时，则参数为False、None |
    | timeout | int | 回调函数超时时间，单位秒。默认是2s |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", args, self.OnCallback, 2)
 ```
<span id="ResponseToServer"></span>
#### ResponseToServer

- 描述

    service接口，给lobby/game返回一个消息。若函数RequestToService的callback参数为空，则不能调用该接口
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | lobby/game服务器id |
    | callbackId | int | 回调函数id |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service同game/lobby通信示例
#service mod
class testService(ServiceSystem):
        def __init__(self,namespace,systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.RegisterRpcMethodForMod('PlayerJoinOKEvent', self.OnPlayerJoinOK)
        def OnPlayerJoinOK(self, serverId, callbackId, args):
                #args的结果为：{'uid':123, 'name':'nickname'}
                print 'OnPlayerJoinOK', args
                response = {}
                response['result'] = 1
                self.ResponseToServer(serverId, callbackId, response)
#lobby mod
class lobbyServer(ServerSystem):
        def __init__(self, namespace, systemName):
                ServerSystem.__init__(self, namespace, systemName)
        def OnCallback(self, suc, args):
                #若成功：suc=True，args= {'result' : 1}
                #若超时，则suc为False
                if not suc:
                        print 'OnCallback timeout'
                        return
                print 'OnCallback success', args
        def testNotifyService(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RequestToServiceMod("idv_service", "PlayerJoinOKEvent", args, self.OnCallback, 2)
 ```
Apollo通信相关api。

<span id="client和service通信"></span>
### client和service通信

<span id="NotifyToServiceNode"></span>
#### NotifyToServiceNode

- 描述

    客户端接口，给service服务器发送事件
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | serverId | int | 服务器id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，包含：`__neteaseProxyId__`，表示当前客户端连接的proxy服务器id；`__uid__`，表示当前客户端的uid |
- 返回值

    无
- 示例

```python
#客户端给service发送消息的示例
#client mod
import client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class testClient(ClientSystem):
        def __init__(self,namespace,systemName):
                ClientSystem.__init__(self, namespace, systemName)
        def testNotify(self):
                player = {}
                player['name'] = 'nickname'
                self.NotifyToServiceNode(8000, 'ClientToServiceEvent', player)
#service mod
class testService(ServiceSystem):
        def __init__(self, namespace, systemName):
                ServiceSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('clientNamespace', 'clientSystem', 'ClientToServiceEvent', self, self.OnClientToService)
        def OnClientToService(self, args):
                #args结果：{'__neteaseProxyId__': 2000, '__uid__': 123, 'name': nickname}
                print 'OnClientToService', args
 ```
<span id="RemoteNotifyToClient"></span>
#### RemoteNotifyToClient

- 描述

    service接口，service发送事件到指定客户端
    
- 参数

    | 参数名 | 数据类型 | 说明 |
    | :--- | :--- | :--- |
    | uid | int/long | 玩家的netease uid，玩家的唯一标识 |
    | proxyId | int | 当前客户端连接的proxy服务器id，可以通过NotifyToServiceNode、AddServerPlayerEvent、GetOnlineServerInfoOfPlayer、GetOnlineServerInfoOfMultiPlayers接口或事件获取该参数 |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数 |
- 返回值

    无
- 示例

```python
#service给客户端发送消息的示例
#client mod
import client.extraClientApi as clientApi
ClientSystem = clientApi.uid()
class testClient(ClientSystem):
        def __init__(self,namespace,systemName):
                ClientSystem.__init__(self, namespace, systemName)
                self.ListenForEvent('serviceNamespace', 'serviceSystem', 'ServiceToClientEvent', self, self.OnServiceToClient)
        def OnServiceToClient(self, args):
                #args的结果：{'uid': 123, 'name': nickname}
                print 'OnServiceToClient', args
#service mod
class testService(ServiceSystem):
        def __init__(self, namespace, systemName):
                ServiceSystem.__init__(self, namespace, systemName)
        def testNotify(self):
                player = {}
                player['uid'] = 123
                player['name'] = 'nickname'
                self.RemoteNotifyToClient(123, 8000, 'ServiceToClientEvent', player)
 ```

## 9-运营指令

# 运营指令

- 使用方法
    ```
    post url: http:masterip:masterport/baseurl
    post body:
       json格式，例如：
       {
	      "serverId":3,
	      "ip":"192.168.43.170",
	      "port":12001,
	      "masterPort":12002,
	      "type":"lobby"
       }
    response:
        json格式，格式:
        {
            "code":1, #1是成功，2是失败
            "message":"reason",#若是失败，则介绍失败原因
            "entity":content #详细信息
        }
    ```
    开发者可以登录到master所在机器，用curl命令发请求，使用方式如下：
    ```
     curl -X POST http://masterip:masterport/baseurl -d 'postbody' 
    ```
    若通过"/online-num/query"指令获取game在线人数，则可以在master上发送如下curl命令：
    ```
     curl -X POST http://11.11.11.11:8503/online-num/query -d '{"server_type":"game"}' 
    ```
    若需要使用商城插件neteaseShop中查询订单运营指令（/check-single-order指令），则可以在master上发送如下curl命令：
    ```
     curl -X POST http://11.11.11.11:8503/check-single-order -d '{"orderid" : 1234,"uid" : 123456789}' 
    ```

## 查询UID

* **/netease/get-online-uids**

    - 描述

      查询当前在线玩家的uid

    - 无post body json参数

    - response entity参数
      dict。key是服务器id，value是在线玩家uid列表；当对应服务器中不存在玩家时，服务器id不会作为key出现
      
    - 示例:
    ```
    post url: http://111.222.333.444:1101/netease/get-online-uids
    post body:
    {
    } 
    response:
    {
      "code": 0,
      "message": "",
      "entity": {
        "4000":[1989540401,2147585444]
      }
    } 
    ```

* **/netease/get-lazy-uids**

    - 描述

      查询最近请求登录玩家的uid以及请求登录时间

    - 无post body json参数

    - response entity参数
      list(string)。每条记录上有uid和对应请求登录的时间，按照登录请求时间远近排序（越近越在前）;最多30条
      
    - 示例:
    ```
    post url: http://111.222.333.444:1101/netease/get-lazy-uids
    post body:
    {
    } 
    response:
    {
      "code": 0,
      "message": "",
      "entity": {
        "uid=680116908 login=2021-05-26 15:12:41",
        "uid=1989540401 login=2021-05-26 15:12:08",
        "uid=2147585444 login=2021-05-26 15:11:24"
      }
    } 
    ```

## 在线人数
* **/netease/update-player-online-limit**

    - 描述

      修改全局最高同时在线人数限制
	
    - post body 参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | online_limit | int      | 需要设置的最高同时在线人数，当设置为0时代表不限制最高同时在线|
    
    - response entity参数
      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | code | int      | 整个指令的返回码，1为成功，其他数字为失败|
      | message | str      | 整个指令的返回结果描述，一般成功时会空，失败时会描述失败原因|
      | entity | dict      | 关键字version为当前配置文件中，全局同时在线人数限制的版本号，暂时无用；关键字old_online_limit为修改前，全局最高同时在线人数的限制，返回0代表修改前，没有限制最高同时在线|
    
    - 示例:
     ```
     post url: http://111.222.333.444:1101/netease/update-player-online-limit
     post body:
     {
	    "online_limit":8000
     } 
     response:
     {
         "code": 1,
         "entity": {
             "version": 0,
             "old_online_limit": 6000
           },
           "message": ""
     } 
     ```

* **/online-num/query**

    - 描述

      获取proxy/lobby/game在线人数或获取总在线人数。

    - post body 参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | serverType | str      | 服务器类型，比如"lobby","game"，"proxy",若不传入该值，则表示总在线人数|
    
    - response entity参数
      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | onlineNum | int      | 在线人数|
    - 示例:
     ```
     post url: http://111.222.333.444:1101/online-num/query
     post body:
     {
	    "serverType":"game"
     } 
     response:
     {
         "code": 1,
         "entity": {
             "onlineNum": 0
           },
           "message": ""
     } 
     ```

* **/online-num/query-by-server-id**

    - 描述

      获取某个proxy/game/lobby在线人数

    - post body参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | serverId | int      | 服务器id|
    
    - response entity参数
      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | onlineNum | int      | 在线人数|
    - 示例:

    ```
     post url: http://111.222.333.444:1101/online-num/query-by-server-id
     post body:
     {
	    "serverId":1
     } 
     response:
     {
         "code": 1,
         "entity": {
             "onlineNum": 2
           },
           "message": ""
     }      
    ```

## 日志等级

* **/conf/set-log-debug-level**

    - 描述

      开服工具日志等级设置为debug或info level等级

    - post body 参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | debugLevel | bool      | true:则日志设置为debug log level；false：日志设置为info log level |
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/conf/set-log-debug-level
     post body:
     {
	    "debugLevel":false
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```

* **/conf/set-server-log-debug-level**

    - 描述

      设置某个服务器的日志等级。

    - post body 参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | serverId | int      | 服务器id。可以是proxy、lobby、game、service的serverid。若为0，则表示master。|
      | debugLevel | bool      | true:则日志设置为debug log level；false：日志设置为info log level |
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/conf/set-server-log-debug-level
     post body:
     {
	    "serverId":1,
	    "debugLevel":false
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
## 服务器

* **/query-all-server-status**

    - 描述

      查询所有服务器状态

    - 无post body json参数
    
    - response entity参数
      dict。key是服务器id，value是服务器状态。服务器状态有：
          1:断开连接状态
          2:已连接状态  
          3:关服状态
          4:优雅关服状态    
          6, 滚动更新中间状态，即将转换到状态7  
          7 也是滚动更新中间状态，即将转换到状态1或2


    - 示例:
     ```
     post url: http://111.222.333.444:1101/query-all-server-status
     post body:
     {
     } 
     response:
     {
         "code": 1,
         "entity": {
        	"1": 1,
        	"2": 1
    	  }
          "message": ""
     }
     ```

* **/query-one-server-status**

    - 描述

      查询某个服务器状态

    - post body 参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | serverId | int      | proxy/lobby/game服务器id |
      
    - response entity参数

      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | status | int      | 服务器状态。服务器状态有：服务器状态如下：<br/>      1:断开连接状态<br/>      2:已连接状态<br/>      3:关服状态<br/>      4:优雅关服状态<br/>      6, 滚动更新中间状态，即将转换到状态7<br/>      7 也是滚动更新中间状态，即将转换到状态1或2 |
      
    - 示例:
     ```
     post url: http://111.222.333.444:1101/query-one-server-status
     post body:
     {
     	"serverId":1
     } 
     response:
     {
         "message": "",
         "code": 1,
         "entity": {
             "status": 1
         }
     }
     ```
## 禁言，解除禁言

* **/silent**

    - 描述

      禁言某个玩家

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uid |int      | 玩家id |
      | banTime |int      | 禁言时间，单位为秒，-1表示永封|
      | reason |str      | 禁言原因|
      | type |str      | 禁言类型，可自定义，公屏禁言为`Commom`|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/silent
     post body:
     {
	    "uid":11111,
	    "banTime":40,
        "reason":"玩家作弊",
	    "type":"Common"
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
    
* **/unban-silent**

    - 描述

      解除某个玩家的禁言

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uid |int      | 解除禁言玩家的uid|
      | type |str      | 禁言类型，可自定义，公屏禁言为`Commom`|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/unban-silent
     post body:
     {
	    "uid":11111,
	    "type":"Commom"
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
    
* **/global-silent**

    - 描述

      全局公屏禁言开关

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | isSilent |bool      | 全局禁言开关,`true`表示开启全局禁言,`false`表示关闭全局禁言|
      | reason |str      | 禁言原因|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/global-silent
     post body:
     {
	    "isSilent":true,
	    "reason":"系统维护"
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```

## 踢出玩家

* **/kickout-user**

    - 描述

      把某个玩家从游戏中踢出

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uid |int      | 被踢出玩家的uid|
      | reason |str      | 踢出原因|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/kickout-user
     post body:
     {
	    "uid":11111,
        "reason":"玩家作弊",
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
## 封禁，解除封禁

* **/ban-user**

    - 描述

      封禁某个玩家

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uid |int      | 封禁玩家的uid|
      | banTime |int      | 封禁时间，单位为秒，-1表示永封|
      | reason |str      | 封禁原因|
      | bCombineReason |bool      | 是否组合显示封禁原因。若为True，则按备注说明处理，否则被封禁玩家登陆会提示【reason】|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/ban-user
     post body:
     {
	    "uid":11111,
	    "banTime":40,
        "reason":"玩家作弊",
     } 
     response:
     {
         "code": 1,
         "entity": null,
          "message": ""
     }
     ```
    - 备注
    若banTime>0，则被封禁玩家登陆提示：您的账号已经被封禁，剩余封禁时间：x天y小时z分，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    若banTime=-1，则被封禁玩家登陆提示：您的账号已经被永久封禁，封禁原因：【reason】。如有疑问，请前往客服专区反馈
    
* **/unban-user**

    - 描述

      解除某个玩家的封禁

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uid |uint32      | 解除封禁玩家的uid|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/unban-user
     post body:
     {
	    "uid":11111,
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
## 强制解除玩家在线标识

* **/netease/release-online-lock**

    - 描述

      强制解除指定UID玩家的在线标识

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | uidList |list(int)      | 需要解除在线标识的玩家的UID列表|
    
    - response entity参数
      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | sucUids | list(int)     | 成功解除玩家在线标识的UID列表，包括请求时已经不在线的|
      | failUids | list(int)  |  解除玩家在线标识失败的UID列表|
    
    - 示例:
     ```
     post url: http://111.222.333.444:1101/netease/release-online-lock
     post body:
     {
	    "uidList":[2147585444,2819362897],
     } 
     response:
     {
         "code": 1,
         "message": "",
         "entity": {
           "sucUids": [2147585444,2819362897],
           "failUids": []
         }
     }
     ```

* **/netease/release-online-lock-by-server**

    - 描述

      强制解除指定ID服务器当前在线玩家的在线标识

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | serverId |list(int)      | 需要解除在线标识的服务器ID|
    
    - response entity参数
      | 关键字     | 数据类型 | 说明         |
      | ---------- | -------- | ------------ |
      | sucUids | list(int)     | 成功解除玩家在线标识的UID列表|
      | failUids | list(int)  |  解除玩家在线标识的UID列表|
    
    - 示例:
     ```
     post url: http://111.222.333.444:1101/netease/release-online-lock-by-server
     post body:
     {
	    "serverId": 4000,
     } 
     response:
     {
         "code": 1,
         "message": "",
         "entity": {
           "sucUids": [2147585444,2819362897],
           "failUids": []
         }
     }
     ```


## 停服维护

* **/invalid-all-servers**

    - 描述

      开启/关闭停服维护

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | invalid |bool      | 停服维护开关，`true`表示开启停服维护,`false`表示关闭停服维护|
      | reason |str      | 停服维护原因|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/invalid-all-servers
     post body:
     {
	    "invalid":true,
        "reason":"停服维护",
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     ```
## Hunter调试命令

* **/netease/hunter-debug**

    - 描述

      使目的服务器执行Python脚本，脚本中使用**print**打印的信息会体现在请求返回中，同时，也会打印到目的服务器的日志文件中，具体是"hunterDebug exec"日志的下面n行日志。
    
    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | opServerIds |list(int)    |可选参数，需要执行python脚本的服务器ID列表，0表示为master|
      | opServerType |str    |可选参数，需要执行python脚本的服务器类型列表|
      | script |str      | 服务器需要执行的python脚本，用`\n`换行|
      | command |str      | 服务器需要执行的控制台命令|
    
    - response entity参数
      dict。key是服务器id，value也是一个dict，有两个key，code和message
      code=0代表在对应服务器上执行脚本成功，此时message中的信息为脚本中**print**打印的信息；
      code=1代表在对应服务器上执行脚本失败，此时message中的信息为失败的原因；

    - 示例:
     ```
     post url: http://111.222.333.444:1101/netease/hunter-debug
     post body:
     {
        "opServerIds": [0,8000,4000,6000],
        "script":"import time\nprint time.time()"
     } 
     response:
     {
        "code": 0, 
        "message": "", 
        "entity": {
          "0": {"message": "1623327430.98\n", "code": 0}, 
          "4000": {"message": "1623327431.04\n", "code": 0}, 
          "6000": {"message": "1623327431.04\n", "code": 0}, 
          "8000": {"message": "1623327431.04\n", "code": 0}
          }
      }
     对应服务器日志文件中包含下面日志：
     [2019-06-03 10:21:29 INFO] Python:hunterDebug exec
     [2019-06-03 10:21:29 INFO] Python:1559543269.12
     ```

* **/hunter-debug**

    - 描述

      使目的服务器执行Python脚本，其结果打印到目的服务器的日志文件中，具体是"hunterDebug exec"日志的下面n行日志。

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | serverId |int      |服务器对应ID，0表示为master|
      | script |str      | 服务器需要执行的python脚本，用`\n`换行|
      | command |str      | 服务器需要执行的控制台命令|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/hunter-debug
     post body:
     {
	    "serverId":101,
        "script":"import time\nprint time.time()"
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }
     101服务器日志文件中包含下面日志：
     [2019-06-03 10:21:29 INFO] Python:hunterDebug exec
     [2019-06-03 10:21:29 INFO] Python:1559543269.12
     ```
## 性能分析

* **/check-memory-run**

    - 描述

      检查服务器脚本层内存泄漏。需要执行两次指令，第一次生成快照，第二次生成同第一次的diff。

    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | serverId |int      ||
      | useList |list      | 通常是 ["tracemalloc", "objreport"]|
      | objNames |list      | 通常是空|
    
    - 无response entity参数

    - 示例:
     ```
     post url: http://111.222.333.444:1101/check-memory-run
     post body:
     {
	    "serverId":101,
        "useList":["tracemalloc", "objreport"],
		"objNames":[]
     } 
     response:
     {
         "code": 1,
         "entity": null,
         "message": ""
     }

     服务器日志文件包含下面日志：
	[2019-09-11 17:09:33 INFO] Python:run_tracemalloc traceback
	[2019-09-11 17:09:33 INFO] Python:[ Top 10 differences ]
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/obj_report.py:43: size=12.0 KiB (+12.0 KiB), count=1 (+1), average=12.0 KiB
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/obj_report.py:45: size=10.0 KiB (+10.0 KiB), count=11 (+11), average=992 B
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/check_memory.py:61: size=10.0 KiB (+10.0 KiB), count=127 (+127), average=84 B
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/obj_report.py:12: size=1736 B (+1736 B), count=6 (+6), average=289 B
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/obj_report.py:6: size=1007 B (+1007 B), count=5 (+5), average=201 B
	[2019-09-11 17:09:33 INFO] Python:/usr/local/lib/python2.7/site-packages/tracemalloc.py:380: size=864 B (+864 B), count=4 (+4), average=216 B
	[2019-09-11 17:09:33 INFO] Python:/usr/local/lib/python2.7/json/decoder.py:380: size=704 B (+704 B), count=11 (+11), average=64 B
	[2019-09-11 17:09:33 INFO] Python:/usr/local/lib/python2.7/site-packages/tracemalloc.py:518: size=672 B (+672 B), count=4 (+4), average=168 B
	[2019-09-11 17:09:33 INFO] Python:<unknown>:0: size=650 B (+650 B), count=2 (+2), average=325 B
	[2019-09-11 17:09:33 INFO] Python:/tmp/tmpxlycSu/scripts/mod/server/memory/check_memory.py:66: size=544 B (+544 B), count=1 (+1), average=544 B
	[2019-09-11 17:09:33 INFO] Python:[QA] [DIFF_MORE]
	[2019-09-11 17:09:33 INFO] Python:[QA] [DIFF_LESS]
	[2019-09-11 17:09:33 INFO] Python:-2        <type 'tuple'>

	日志说明，打印了两次【/check-memory】间，内存变化前十的文件，两次指令间，减少了2个tuple的实例。
	 ```

* **/profile**
    - 描述

      用于测量python函数占用cpu时间。需要执行两次指令，第一次开始profile，第二次生成性能数据文件。性能数据文件放到执行文件所在目录下的profile子目录中。性能数据文件名的格式：profile+生成文件的时间戳
    - post body json参数

      | 关键字      | 数据类型| 说明        |
      | ------------ | -----------| ------------ |
      | serverId |int      ||服务器对应ID。0表示为master，-1表示所有服务器，其他表示lobby/game/service的服务器ID|
      | bBegin |bool      |true：开始profile；false：完成profile|
    
    - 无response entity参数
    - 示例:
    ```
    性能数据文件名：profile_1574325974
    文件内容：
         33 function calls in 0.000 seconds
	
   Ordered by: internal time
	
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 {_log.logInfo}
        2    0.000    0.000    0.000    0.000 logout.py:83(write)
        1    0.000    0.000    0.000    0.000 logout.py:62(split_and_log)
        1    0.000    0.000    0.000    0.000 netServerApp.py:17(TickApp)
        1    0.000    0.000    0.000    0.000 Queue.py:93(empty)
        1    0.000    0.000    0.000    0.000 timer.py:72(scheduler)
        1    0.000    0.000    0.000    0.000 idvScript.modMaster.httpHandlerSys:141(Update)
        1    0.000    0.000    0.000    0.000 async_task_pool.py:293(schedule)
        1    0.000    0.000    0.000    0.000 netgameApp.py:3(Tick)
        1    0.000    0.000    0.000    0.000 async_task_pool.py:302(exec_callback)
        2    0.000    0.000    0.000    0.000 {len}
        1    0.000    0.000    0.000    0.000 baseApp.py:73(ClearNeedsUpdate)
        5    0.000    0.000    0.000    0.000 {method 'has_key' of 'dict' objects}
        1    0.000    0.000    0.000    0.000 {time.time}
        1    0.000    0.000    0.000    0.000 {method 'acquire' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
        2    0.000    0.000    0.000    0.000 {method 'splitlines' of 'str' objects}
        1    0.000    0.000    0.000    0.000 mongopool.py:194(tick)
        1    0.000    0.000    0.000    0.000 redispool.py:274(do_tick)
        1    0.000    0.000    0.000    0.000 Queue.py:200(_qsize)
        1    0.000    0.000    0.000    0.000 memoryScripts.MasterMemorySys:21(Update)
        1    0.000    0.000    0.000    0.000 {method 'release' of 'thread.lock' objects}
        1    0.000    0.000    0.000    0.000 redispool.py:271(tick)
        3    0.000    0.000    0.000    0.000 baseSystem.py:86(Update)
    内容解读：
    第一行：33个函数调用被监控，这些函数占用cpu总运行时间为0.000秒
    接下来输出个字段含义：
    ncalls：表示函数调用的次数；
    tottime：表示指定函数的总的运行时间，除掉函数中调用子函数的运行时间；
    percall：（第一个percall）等于 tottime/ncalls；
    cumtime：表示该函数及其所有子函数的调用运行的时间，即函数开始调用到返回的时间；
    percall：（第二个percall）即函数运行一次的平均时间，等于 cumtime/ncalls；
    filename:lineno(function)：每个函数调用的具体信息；
        
	```

