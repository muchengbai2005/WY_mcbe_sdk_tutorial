# ModAPI 接口-通用

## 目录

- [Component](#component)
- [System](#system)
- [事件](#事件)
- [工具](#工具)
- [数学](#数学)
- [本地存储](#本地存储)
- [本地设备](#本地设备)
- [调试](#调试)

---

## Component

# Component

## CreateComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    给实体创建服务端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.CreateComponent(entityId, "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，与GetComponent类似，如果已经创建会自动直接Get
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    给实体创建客户端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str或int | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.CreateComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，与GetComponent类似，如果已经创建会自动直接Get
```



## DestroyComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    删除实体的服务端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
# entityId 根据游戏实际Id获取，这里'-12345678910'只是随便写的
comp = serverApi.DestroyComponent('-12345678910', "Minecraft", "item")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    删除实体的客户端组件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.DestroyComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
```



## GetComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取实体的服务端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例或者None |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetComponent(entityId, "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，如果没有创建过会返回None
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取实体的客户端组件。一般用来判断某个组件是否创建过，其他情况请使用CreateComponent

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | entityId | str | 该组件属主的实体id |
    | nameSpace | str | 组件的命名空间，registerComponent的namespace |
    | name | str | 组件的名字 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | BaseComponent | 组件实例或者None |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetComponent(clientApi.GetLocalPlayerId(), "Minecraft", "item")
# 拿到comp后就可以做一些逻辑内容，如果没有创建过会返回None
```



## GetComponentCls

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于获取服务器component基类。实现新的component时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(BaseComponent) | 组件基类 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerComponentCls = serverApi.GetComponentCls()
# Component要继承于基类才能生效
class ShootComponentServer(ServerComponentCls):
    def __init__(self, entityId):
        ServerComponentCls.__init__(self, entityId)
        # 这里设置了一个开关来开关更新射击
        self.mShoot = False
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于获取客户端component基类。实现新的component时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(BaseComponent) | 组件基类 |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientComponentCls = clientApi.GetComponentCls()
# Component要继承于基类才能生效
class ShootComponentClient(ClientComponentCls):
    def __init__(self, entityId):
        ClientComponentCls.__init__(self, entityId)
        # 这里设置了一个开关来开关更新射击
        self.mShoot = False
```



## GetEngineCompFactory

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取引擎组件的工厂，通过工厂可以创建服务端的引擎组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EngineCompFactoryServer | 服务端引擎组件工厂 |

- 示例

```python
import mod.server.extraServerApi as serverApi
compFactory = serverApi.GetEngineCompFactory()
gameComp = compFactory.CreateGame(serverApi.GetLevelId())
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取引擎组件的工厂，通过工厂可以创建客户端的引擎组件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | EngineCompFactoryClient | 客户端引擎组件工厂 |

- 示例

```python
import mod.client.extraClientApi as clientApi
compFactory = clientApi.GetEngineCompFactory()
gameComp = compFactory.CreateGame(clientApi.GetLevelId())
```



## RegisterComponent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于将组件注册到引擎中

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | name | str | 组件名称 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注册成功与否 |

- 示例

```python
import mod.server.extraServerApi as serverApi
@Mod.InitServer()
def TutorialServerInit(self):
    # 注册一个自定义的服务端Component
    serverApi.RegisterComponent("TutorialMod", "ServerShoot", "tutorialScripts.modServer.serverComponent.shootComponentServer.ShootComponentServer")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于将组件注册到引擎中

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | name | str | 组件名称 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 注册成功与否 |

- 示例

```python
import mod.client.extraClientApi as clientApi
@Mod.InitClient()
def TutorialClientInit(self):
    # 注册一个自定义的客户端Component
    clientApi.RegisterComponent("TutorialMod", "ClientShoot", "tutorialScripts.modClient.clientComponent.shootComponentClient.ShootComponentClient")
```

## System

# System

## GetClientSystemCls

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    用于获取客户端system基类。实现新的system时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(ClientSystem) | 客户端系统类 |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
```



## GetServerSystemCls

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    用于获取服务器system基类。实现新的system时，需要继承该接口返回的类

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | type(ServerSystem) | 服务端系统类 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
```



## GetSystem

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取已注册的系统

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | systemName | str | 系统名称，自定义名称，可以使用英文、拼音和下划线，建议尽量个性化 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ServerSystem | 返回具体系统的实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverSystem = serverApi.GetSystem("TutorialMod", "TutorialServerSystem")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于获取其他系统实例

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 系统注册的命名空间，一般为mod名字 |
    | systemName | str | 要获取的系统名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ClientSystem | 返回具体系统的实例，如果获取不到则返回 None |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.tutorialSystem = clientApi.GetSystem("TutorialMod", "TutorialClientSystem")
```



## RegisterSystem

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与客户端进行通讯等。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | systemName | str | 系统名称，自定义名称，可以使用英文、拼音和下划线，建议尽量个性化 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ServerSystem | 返回具体系统的实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
# 系统system的注册是在modMain.py的MOD类中
# 服务端系统system的注册方式
@Mod.InitServer()
def TutorialServerInit(self):
    serverApi.RegisterSystem("TutorialMod", "TutorialServerSystem", "tutorialScripts.tutorialServerSystem.TutorialServerSystem")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于将系统注册到引擎中，引擎会创建一个该系统的实例，并在退出游戏时回收。系统可以执行我们引擎赋予的基本逻辑，例如监听事件、执行Tick函数、与服务端进行通讯等。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | nameSpace | str | 命名空间，建议为mod名字 |
    | systemName | str | 系统名称，自定义名称，可以使用英文、拼音和下划线，建议尽量个性化 |
    | clsPath | str | 组件类路径，路径从脚本的第一层开始算起 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | ClientSystem | 返回具体系统的实例 |

- 示例

```python
import mod.client.extraClientApi as clientApi
# 系统system的注册是在modMain.py的MOD类中
# 客户端系统system的注册方式
@Mod.InitClient()
def TutorialClientInit(self):
    clientApi.RegisterSystem("TutorialMod", "TutorialClientSystem", "tutorialScripts.tutorialClientSystem.TutorialClientSystem")
```

## 事件

# 事件

## BroadcastEvent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.system.baseSystem.BaseSystem

- 描述

    本地广播事件，客户端system广播的事件仅客户端system能监听，服务器system广播的事件仅服务端system能监听。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def BroadCastEventTest(self, args):
        self.BroadcastEvent("bulletShootEvent", args)
```



## BroadcastToAllClient

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    服务器广播事件到所有客户端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def BroadCastEventTest(self, args):
        self.BroadcastToAllClient("bulletShootEvent", args)

```



## CreateEventData

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.system.baseSystem.BaseSystem

- 描述

    创建自定义事件的数据，eventData用于发送事件。创建的eventData可以理解为一个dict，可以嵌套赋值dict,list和基本数据类型，但不支持tuple

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 事件数据 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def shoot(self):
        shootData = self.CreateEventData()
        shootData["id"] = self.mPlayerId
        # 向客户端发送事件，传递了一个playerId
        self.NotifyToClient('-12345678910','BulletHit', shootData)
```



## GetEngineNamespace

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 引擎的命名空间 |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), ‘AddServerPlayerEvent’, self, self.OnPlayerAdd)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取引擎事件的命名空间。监听引擎事件时，namespace传该接口返回的namespace

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 引擎的命名空间 |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.OnUIInitFinished)
```



## GetEngineSystemName

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 引擎的systemName |

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def __init__(self, namespace, systemName):
        ServerSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), ‘AddServerPlayerEvent’, self, self.OnPlayerAdd)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取引擎系统名。监听引擎事件时，systemName传该接口返回的systemName

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 引擎的systemName |

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def __init__(self, namespace, systemName):
        ClientSystem.__init__(self, namespace, systemName)
        self.ListenForEvent(clientApi.GetEngineNamespace(), clientApi.GetEngineSystemName(), 'UiInitFinished', self, self.OnUIInitFinished)
```



## ListenForEvent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.system.baseSystem.BaseSystem

- 描述

    注册监听某个系统抛出的事件。若监听引擎事件时，namespace和systemName分别为GetEngineNamespace()和GetEngineSystemName()。具体每个事件的详细事件data可以参考"事件"分类下的内容

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 所监听事件的来源系统的namespace |
    | systemName | str | 所监听事件的来源系统的systemName |
    | eventName | str | 事件名 |
    | instance | any | 回调函数所属的类的实例 |
    | func | function | 回调函数 |
    | priority | int | 这个回调函数的优先级。默认值为0，这个数值越大表示被执行的优先级越高，最高为10。 |

- 返回值

    无

- 备注
    - 服务端system监听的客户端系统事件的回调参数中会自带一个叫"__id__"的key，值为对应客户端的玩家id

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def ListenEvent(self):
        # 监听了引擎事件'ServerChatEvent'
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
        # 监听客户端系统事件
        self.ListenForEvent("MyFpsMod", "FpsClientSystem", "MyEvent", self, self.OnMyEvent)

    def OnServerChat(self, args):
        print 'OnServerChat', args

    def OnMyEvent(self, args):
        print 'OnMyEvent', args['__id__'], args
```



## NotifyToClient

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    服务器发送事件到指定客户端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetId | str | 客户端对应的Id，一般就是玩家Id |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def NotifyToClientTest(self, args):
        self.NotifyToClient('-1234567890',"bulletShootEvent", args)
```



## NotifyToMultiClients

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.system.serverSystem.ServerSystem

- 描述

    2.0版本仅Apollo可用，服务器发送事件到指定一批客户端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | targetIdList | list(str) | 客户端对应的playerId列表，playerId为玩家的entityId |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def NotifyToClientTest(self, args):
        self.NotifyToMultiClients(['-1234567890', '-321654987'],"bulletShootEvent", args)
```



## NotifyToServer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.system.clientSystem.ClientSystem

- 描述

    客户端发送事件到服务器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | eventName | str | 事件名 |
    | eventData | dict | 事件参数，一般用CreateEventData的返回值 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
ClientSystem = clientApi.GetClientSystemCls()
class FpsClientSystem(ClientSystem):
    def NotifyToServerTest(self, args):
        self.NotifyToServer("bulletShootEvent", args)
```



## UnListenAllEvents

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.system.baseSystem.BaseSystem

- 描述

    反注册监听某个系统抛出的所有事件，即不再监听。

- 参数

    无

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def ListenEvent(self):
        # 服务端脚本自定义了1个事件
        self.DefineEvent('BulletHit')
        # 服务器端脚本监听了引擎的1个事件'ServerChatEvent'
        # 具体每个事件的详细事件data可以参考《MODSDK文档》
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
    def UnListenEvent(self):
        # 取消自定义的事件
        self.UnDefineEvent('BulletHit')
        # 取消监听的系统事件
        self.UnListenAllEvents()
```



## UnListenForEvent

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

method in mod.common.system.baseSystem.BaseSystem

- 描述

    反注册监听某个系统抛出的事件，即不再监听。若是引擎事件，则namespace和systemName分别为[GetEngineNamespace](#getenginenamespace)和[GetEngineSystemName](#getenginesystemname)。与ListenForEvent对应。

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | namespace | str | 所监听事件的来源系统的namespace |
    | systemName | str | 所监听事件的来源系统的systemName |
    | eventName | str | 事件名 |
    | instance | any | 回调函数所属的类的实例 |
    | func | function | 回调函数 |
    | priority | int | 这个回调函数的优先级。默认值为0，这个数值越大表示被执行的优先级越高。 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
ServerSystem = serverApi.GetServerSystemCls()
class FpsServerSystem(ServerSystem):
    def ListenEvent(self):
        # 服务端脚本自定义了1个事件
        self.DefineEvent('BulletHit')
        # 服务器端脚本监听了引擎的1个事件'ServerChatEvent'
        self.ListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
    def UnListenEvent(self):
        # 取消自定义的事件
        self.UnDefineEvent('BulletHit')
        # 取消监听的系统事件
        self.UnListenForEvent(serverApi.GetEngineNamespace(), serverApi.GetEngineSystemName(), 'ServerChatEvent', self, self.OnServerChat)
```

## 工具

# 工具

## AddRepeatedTimer

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    添加服务端触发的定时器，重复执行

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回触发的定时器实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddRepeatedTimer(3.0,func,args,kwargs)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    添加客户端触发的定时器，重复执行

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回触发的定时器实例 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddRepeatedTimer(3.0,func,args,kwargs)
```



## AddTimer

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    添加服务端触发的定时器，非重复

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回单次触发的定时器实例 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddTimer(3.0,func,args,kwargs)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    添加客户端触发的定时器，非重复

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | delay | float | 延迟时间，单位秒 |
    | func | function | 定时器触发函数 |
    | *args | any | 变长参数，可以不设置 |
    | **kwargs | any | 字典变长参数，可以不设置 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | CallLater | 返回单次触发的定时器实例 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.AddTimer(3.0,func,args,kwargs)
```



## CancelTimer

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    取消定时器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timer | CallLater | AddTimer和AddRepeatedTimer时返回的定时器实例 |

- 返回值

    无

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
comp.CancelTimer(timer)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    取消定时器

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | timer | CallLater | AddOnceTimer和AddRepeatedTimer时返回的定时器实例 |

- 返回值

    无

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
comp.CancelTimer(timer)
```



## CheckNameValid

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    检查昵称是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 昵称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:昵称合法 False:昵称非法 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
isValid = comp.CheckNameValid("史蒂夫")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    检查昵称是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | name | str | 昵称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:昵称合法 False:昵称非法 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
isValid = comp.CheckNameValid("史蒂夫")
```



## CheckWordsValid

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    检查语句是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | words | str | 语句 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:语句合法<br>False:语句非法 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
isValid = comp.CheckWordsValid("creeper? Aww man")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    检查语句是否合法，即不包含敏感词

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | words | str | 语句 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:语句合法<br>False:语句非法 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
isValid = comp.CheckWordsValid("creeper? Aww man")
```



## GetChinese

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.component.gameCompServer.GameComponentServer

- 描述

    获取langStr对应的中文，可参考PC开发包中\handheld\localization\handheld\data\resource_packs\vanilla\texts\zh_CN.lang

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | langStr | str | 传入的langStr |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | langStr对应的中文，若找不到对应的中文，则会返回langStr本身 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(levelId)
# 获取"entity.wolf.name"对应的中文（"狼"）
Chinese = comp.GetChinese("entity.wolf.name")
```



### 客户端接口

<span id="c0"></span>
method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    获取langStr对应的中文，可参考PC开发包中\handheld\localization\handheld\data\resource_packs\vanilla\texts\zh_CN.lang

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | langStr | str | 传入的langStr |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | langStr对应的中文，若找不到对应的中文，则会返回langStr本身 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
# 获取"entity.wolf.name"对应的中文（"狼"）
Chinese = comp.GetChinese("entity.wolf.name")
```



## GetFps

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.gameCompClient.GameComponentClient

- 描述

    获取fps

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | float | 当前fps值 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(levelId)
fps = comp.GetFps()
```



## GetMinecraftEnum

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    用于获取[枚举值文档](../../枚举值/索引.md)中的枚举值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | minecraftEnum | 枚举集合类 |

- 示例

```python
import mod.server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreatePlayer(playerId)
# 使用枚举值作为其他接口的参数
comp.SetPlayerGameType(serverApi.GetMinecraftEnum().GameType.Survival)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    用于获取[枚举值文档](../../枚举值/索引.md)中的枚举值

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | minecraftEnum | 枚举集合类 |

- 示例

```python
import mod.client.extraClientApi as clientApi
# 使用枚举值与事件参数比较
class BattleUI(ScreenNode):
    def OnButtonTouch(self, args):
        touchEventEnum = clientApi.GetMinecraftEnum().TouchEvent
        if touchEvent == touchEventEnum.TouchUp:
            pass

    def Create(self):
        self.AddTouchEventHandler("/panel/test_btn", self.OnButtonTouch, {"isSwallow":True})
```



## GetModConfigJson

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    以字典形式返回指定路径的json格式配置文件的内容，文件必须放置在资源包的/modconfigs目录下

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | path | str | 指定路径的json文件 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 配置内容的字典，当读取文件失败时返回空字典 |

- 示例

```python
import mod.client.extraClientApi as clientApi
data = clientApi.GetModConfigJson("modconfigs/monster.json")
```



## StartCoroutine

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    开启服务端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | iterOrFunc | generator或callable([],generator) | 传入带有yield函数或传入生成器。如传入生成器则将从生成器中断位置开始执行,如传入函数将从头开始执行 |
    | callback | function | 协程执行完后的回调函数，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | generator | 函数生成器 |

- 示例

```python
#通过生成器执行协程
import server.extraServerApi as serverApi
comp = serverApi.GetEngineCompFactory().CreateGame(serverApi.GetLevelId())

def callback():
    print "callback"

def coroutineTest():
    for i in xrange(1000):
        print i
        yield

generator = serverApi.StartCoroutine(coroutineTest, callback)
#执行1秒后停止协程
comp.AddTimer(1.0, serverApi.StopCoroutine, generator)
#5秒后传入StartCoroutine返回的生成器，则函数将从停止位置继续执行
comp.AddTimer(5.0, serverApi.StartCoroutine, generator, callback)

#----------------------------------------------------------------

#通过函数执行协程
import server.extraServerApi as serverApi
def callback():
    print "callback"

def coroutineTest():
    for i in xrange(1000):
        print i
        yield
#传入函数，函数将从头开始执行
serverApi.StartCoroutine(coroutineTest, callback)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    开启客户端协程，实现函数分段式执行，可用于缓解复杂逻辑计算导致游戏卡顿问题

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | iterOrFunc | generator或callable([],generator) | 传入带有yield函数或传入生成器。如传入生成器则将从生成器中断位置开始执行,如传入函数将从头开始执行 |
    | callback | function | 协程执行完后的回调函数，默认为None |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | generator | 函数生成器 |

- 示例

```python
#通过生成器执行协程
import client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateGame(clientApi.GetLevelId())

def callback():
    print "callback"

def coroutineTest():
    for i in xrange(1000):
        print i
        yield

generator = clientApi.StartCoroutine(coroutineTest, callback)
#执行1秒后停止协程
comp.AddTimer(1.0, clientApi.StopCoroutine, generator)
#执行5秒后传入StartCoroutine返回的生成器，则函数将从停止位置继续执行
comp.AddTimer(5.0, clientApi.StartCoroutine, generator, callback)

#----------------------------------------------------------------

#通过函数执行协程
import client.extraClientApi as clientApi
def callback():
    print "callback"

def coroutineTest():
    for i in xrange(1000):
        print i
        yield
#传入函数，函数将从头开始执行
clientApi.StartCoroutine(coroutineTest, callback)
```



## StopCoroutine

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    停止协程

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | iter | generator | 需要停止的生成器对象,StartCoroutine的返回值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StopCoroutine(generator)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    停止客户端协程

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | iter | generator | 需要停止的生成器对象,StartCoroutine的返回值 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StopCoroutine(generator)
```

## 数学

# 数学

## GetDirFromRot

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    通过旋转角度获取朝向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 玩家朝向的单位向量 |

- 示例

```python
import mod.server.extraServerApi as serverApi
direction = serverApi.GetDirFromRot((0, 0))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    通过旋转角度获取朝向

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | rot | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float,float) | 玩家朝向的单位向量 |

- 示例

```python
import mod.client.extraClientApi as clientApi
direction = clientApi.GetDirFromRot((0, 0))
```



## GetRotFromDir

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    通过朝向获取旋转角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dir | tuple(float,float,float) | 玩家朝向的单位向量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 示例

```python
import mod.server.extraServerApi as serverApi
rot = serverApi.GetRotFromDir((1, 0, 1))
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    通过朝向获取旋转角度

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | dir | tuple(float,float,float) | 玩家朝向的单位向量 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | tuple(float,float) | 俯仰角度及绕竖直方向的角度，单位是角度 |

- 示例

```python
import mod.client.extraClientApi as clientApi
rot = clientApi.GetRotFromDir((1, 0, 1))
```

## 本地存储

# 本地存储

## GetConfigData

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.configCompClient.ConfigCompClient

- 描述

    获取本地配置文件中存储的数据

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | configName | str | 配置名称，只能包含字母、数字和下划线字符，另外为了避免addon之间的冲突，建议加上addon的命名空间作为前缀 |
    | isGlobal | bool | 存档配置or全局配置，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 返回本地存储数据 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateConfigClient(clientApi.GetLevelId())
configDict = comp.GetConfigData("addon_namespace_global_config_name", True)
```



## SetConfigData

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.component.configCompClient.ConfigCompClient

- 描述

    以本地配置文件的方式存储数据

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | configName | str | 配置名称，只能包含字母、数字和下划线字符，另外为了避免addon之间的冲突，建议加上addon的命名空间作为前缀 |
    | value | dict | 数据 |
    | isGlobal | bool | 为True时是全局配置，否则为存档配置，默认为False |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
comp = clientApi.GetEngineCompFactory().CreateConfigClient(clientApi.GetLevelId())
data = {}
data["key"] = "value"
comp.SetConfigData("addon_namespace_global_config_name", data, True)
```

## 本地设备

# 本地设备

## GetIP

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取本地玩家的ip地址

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | str | 本地玩家的ip地址 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.GetIP()
```



## GetPlatform

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    获取脚本运行的平台

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0：Window；1：IOS；2：Android；-1：其他，例如联机大厅，阿波罗等linux服务器 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.GetPlatform()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    获取脚本运行的平台

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | int | 0：Window；1：IOS；2：Android；-1：其他 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.GetPlatform()
```



## IsInApollo

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    返回当前游戏Mod是否运行在Apollo网络服

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True：当前Mod运行于Apollo网络服环境<br>False：当前Mod运行于租赁服、联机大厅或者单机环境 |

- 示例

```python
import mod.server.extraServerApi as serverApi
IsInApollo = serverApi.IsInApollo()
```



## IsInServer

<span style="display:inline;color:#ff5555">服务端</span>

method in mod.server.extraServerApi

- 描述

    获取当前游戏是否跑在服务器环境下

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | True:在服务器环境下<br>False:不在服务器环境下 |

- 示例

```python
import mod.server.extraServerApi as serverApi
isInServer = serverApi.IsInServer()
```

## 调试

# 调试

## GetEnableReconnectNetgame

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取是否允许断线重连

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否允许断线重连 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.GetEnableReconnectNetgame()
```



## GetKeepResourceWhenTransfer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取快速切服设置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否设置快速切服 |

- 示例

```python
# 先打开快速切服开关
import mod.client.extraClientApi as clientApi
print clientApi.GetKeepResourceWhenTransfer()
```



## GetResourceFastload

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    获取资源快速加载设置

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否开启资源快速加载 |

- 示例

```python
import mod.client.extraClientApi as clientApi
print clientApi.GetResourceFastload()
```



## ReloadAllMaterials

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    重新加载所有材质文件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.ReloadAllMaterials()
```



## ReloadAllShaders

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    重新加载所有Shader文件

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 若修改到材质，建议使用ReloadAllMaterials方法。

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.ReloadAllShaders()
```



## ReloadOneShader

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    重新加载某个Shader文件

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | shaderName | str | shader名称 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 若同时修改了多个Shader，建议使用ReloadAllShaders方法。

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.ReloadOneShader("entity.fragment")
```



## SetEnableReconnectNetgame

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    设置是否允许断线重连

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | keep | bool | 是否允许断线重连 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.SetEnableReconnectNetgame(True)
```



## SetKeepResourceWhenTransfer

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    设置快速切服

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | keep | bool | 是否在切服时保留资源,True为保留资源,False为不保留资源 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 快速切服通过在切服时保留资源实现，可以缩短切服等待时间。
    - 切服前后的两个服，需要保证资源完全一样，即服务器类型一致。
    - 快速切服设置在退出游戏之前一直有效，如果要切到其他类型的服务器，需要在切服前调用clientApi.SetKeepResourceWhenTransfer(False)

- 示例

```python
# 先打开快速切服开关
import mod.client.extraClientApi as clientApi
clientApi.SetKeepResourceWhenTransfer(True)

# 然后切服
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.TransferToOtherServer('123', 'game')
```



## SetResourceFastload

<span style="display:inline;color:#7575f9">客户端</span>

method in mod.client.extraClientApi

- 描述

    设置资源快速加载

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fastload | bool | 是否在进入游戏时快速加载资源,True为快速加载资源,False为不快速加载资源 |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 是否成功 |

- 备注
    - 开启资源快速加载，可以缩短切服等待时间。
    - 开启资源快速加载，切服速度比设置SetKeepResourceWhenTransfer慢，但不要求切服前后两个服资源完全一致。
    - 物品和方块的自定义贴图需要定义在item_texture.json和terrain_texture.json中，才能开启资源快速加载
    - 设置资源快速加载在退出游戏之前一直有效，退出游戏后自动恢复为False

- 示例

```python
# 先设置资源快速加载
import mod.client.extraClientApi as clientApi
clientApi.SetResourceFastload(True)

# 然后切服
import lobbyGame.netgameApi as lobbyGameApi
lobbyGameApi.TransferToOtherServer('123', 'game')
```



## StartMemProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    开始启动服务端脚本内存分析，启动后调用[StopMemProfile](#stopMemProfile)即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 备注
    - 由于分析时并不区分服务端和客户端，在进行分析时，只需要其中一端startmemprofile和stopmemprofile即可,无需双端同时进行。
    - 将鼠标放在一个函数块上时，下方会显示当前函数对应的详细信息，具体含义可见<a href="../../../../mcguide/27-网络游戏/课程5：实用知识/第6节：插件调试小技巧.html#获取性能分析火焰图">获取性能分析火焰图</a>

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartMemProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMemProfile
serverApi.StopMemProfile(fileName)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    开始启动客户端脚本内存分析，启动后调用[StopMemProfile](#stopMemProfile)即可在路径fileName生成函数内存火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 备注
    - 由于分析时并不区分服务端和客户端，在进行分析时，只需要其中一端startmemprofile和stopmemprofile即可,无需双端同时进行。
    - 将鼠标放在一个函数块上时，下方会显示当前函数对应的详细信息，具体含义可见<a href="../../../../mcguide/27-网络游戏/课程5：实用知识/第6节：插件调试小技巧.html#获取性能分析火焰图">获取性能分析火焰图</a>

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartMemProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMemProfile
clientApi.StopMemProfile(fileName)
```



## StartMultiProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    开始启动服务端与客户端双端脚本性能分析，启动后调用[StopMultiProfile](#stopmultiprofile)即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用[StartProfile](#startprofile)单端版本，此接口只支持PC端

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartMultiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMultiProfile
serverApi.StopMultiProfile()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    开始启动服务端与客户端双端脚本性能分析，启动后调用[StopMultiProfile](#stopmultiprofile)即可在路径fileName生成函数性能火焰图。双端采集时数据误差较大，建议优先使用[StartProfile](#startprofile)单端版本，此接口只支持PC端

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartMultiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMultiProfile
clientApi.StopMultiProfile()
```



## StartProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    开始启动服务端脚本性能分析，启动后调用[StopProfile](#stopprofile)即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 备注
    - 火焰图主页面示例：<br>![火焰图示意图](../../picture/flameGraph_mainPage.png)
    - 如火焰图所示，竖直方向表示调用栈，每一层都是一个函数。调用栈越深，火焰就越高，顶部就是正在执行的函数，下方都是它的父函数。分析性能时主要看火焰图的宽度（其中颜色没有特别意义），火焰图越宽，表示该函数对整体性能的消耗越大。因此需要对该函数进行优化。
    - 将鼠标放在一个函数块上时，下方会显示当前函数对应的详细信息，具体含义可见<a href="../../../../mcguide/27-网络游戏/课程5：实用知识/第6节：插件调试小技巧.html#获取性能分析火焰图">获取性能分析火焰图</a>
    - 优化的核心主要是减少调用次数以及优化函数的写法。其中对于开发者而言，只需要关注开发者开发的代码即可，对于部分函数调用到mod框架或者引擎顶层框架进而导致性能消耗较大的，可以尝试通过减少调用次数来进行优化。
    - 另外，火焰图支持通过右上方的Search框或者“F3”快捷键对函数关键词进行搜索。同时可以点击函数缩放查看对应的调用栈。

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopProfile
serverApi.StopProfile()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    开始启动客户端脚本性能分析，启动后调用[StopProfile](#stopprofile)即可在路径fileName生成函数性能火焰图，此接口只支持PC端。生成的火焰图可以用浏览器打开，推荐chrome浏览器。

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 备注
    - 火焰图主页面示例：<br>![火焰图示意图](../../picture/flameGraph_mainPage.png)
    - 如火焰图所示，竖直方向表示调用栈，每一层都是一个函数。调用栈越深，火焰就越高，顶部就是正在执行的函数，下方都是它的父函数。分析性能时主要看火焰图的宽度（其中颜色没有特别意义），火焰图越宽，表示该函数对整体性能的消耗越大。因此需要对该函数进行优化。
    - 将鼠标放在一个函数块上时，下方会显示当前函数对应的详细信息，具体含义可见<a href="../../../../mcguide/27-网络游戏/课程5：实用知识/第6节：插件调试小技巧.html#获取性能分析火焰图">获取性能分析火焰图</a>
    - 优化的核心主要是减少调用次数以及优化函数的写法。其中对于开发者而言，只需要关注开发者开发的代码即可，对于部分函数调用到mod框架或者引擎顶层框架进而导致性能消耗较大的，可以尝试通过减少调用次数来进行优化。
    - 另外，火焰图支持通过右上方的Search框或者“F3”快捷键对函数关键词进行搜索。同时可以点击函数缩放查看对应的调用栈。
    - 上架时请去掉这个接口的调用

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopProfile
clientApi.StopProfile()
```



## StartRecordEvent

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.extraServerApi

- 描述

    开始启动服务端与客户端之间的脚本事件收发统计，启动后调用[StopRecordEvent](#stoprecordevent)即可获取两个函数调用之间脚本事件收发的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
suc = serverApi.StartRecordEvent()
# 之后通过计时器或者其他触发方式调用StopRecordEvent
result = serverApi.StopRecordEvent()
for eventName, data in result.iteritems():
    print "event[{}] send={} sendSize={} recv={} recvSize={}".format(eventName, data["send_num"], data["send_size"], data["recv_num"], data["recv_size"])
```



## StartRecordPacket

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.extraServerApi

- 描述

    开始启动服务端与客户端之间的引擎收发包统计，启动后调用[StopRecordPacket](#stoprecordpacket)即可获取两个函数调用之间引擎收发包的统计信息，仅支持租赁服与Apollo网络服环境（不支持单机环境）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
suc = serverApi.StartRecordPacket()
# 之后通过计时器或者其他触发方式调用StopRecordPacket
result = serverApi.StopRecordPacket()
for packetName, data in result.iteritems():
    print "packet[{}] send={} sendSize={} recv={} recvSize={}".format(packetName, data["send_num"], data["send_size"], data["recv_num"], data["recv_size"])
```



## StopMemProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    停止服务端脚本内存分析并生成火焰图，与[StartMemProfile](#startMemProfile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartMemProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMemProfile
serverApi.StopMemProfile(fileName)
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    停止客户端脚本内存分析并生成火焰图，与[StartMemProfile](#startMemProfile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartMemProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMemProfile
clientApi.StopMemProfile(fileName)
```



## StopMultiProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    停止双端脚本性能分析并生成火焰图，与[StartMultiProfile](#startmultiprofile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartMultiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMultiProfile
serverApi.StopMultiProfile()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    停止双端脚本性能分析并生成火焰图，与[StartMultiProfile](#startmultiprofile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartMultiProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopMultiProfile
clientApi.StopMultiProfile()
```



## StopProfile

<span style="display:inline;color:#ff5555">服务端</span><span style="display:inline;color:#7575f9">客户端</span>

### 服务端接口

<span id="s0"></span>
method in mod.server.extraServerApi

- 描述

    停止服务端脚本性能分析并生成火焰图，与[StartProfile](#startprofile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.server.extraServerApi as serverApi
serverApi.StartProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopProfile
serverApi.StopProfile()
```



### 客户端接口

<span id="c0"></span>
method in mod.client.extraClientApi

- 描述

    停止客户端脚本性能分析并生成火焰图，与[StartProfile](#startprofile)配合使用，此接口只支持PC端

- 参数

    | 参数名 | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- | :--- |
    | fileName | str | 具体路径，相对于PC开发包的路径，默认为"flamegraph.svg"，位于PC开发包目录下，自定义路径请确保文件后缀名为".svg" |

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | bool | 执行结果 |

- 示例

```python
import mod.client.extraClientApi as clientApi
clientApi.StartProfile()
modfunc()# 处理对应的逻辑
# 之后通过计时器或者其他触发方式调用StopProfile
clientApi.StopProfile()
```



## StopRecordEvent

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.extraServerApi

- 描述

    停止服务端与客户端之间的脚本事件收发统计并输出结果，与[StartRecordEvent](#startrecordevent)配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 收发包信息，假如没有调用过StartRecordEvent，则返回为None |

- 示例

```python
import mod.server.extraServerApi as serverApi
suc = serverApi.StartRecordEvent()
# 之后通过计时器或者其他触发方式调用StopRecordEvent
result = serverApi.StopRecordEvent()
for eventName, data in result.iteritems():
    print "event[{}] send={} sendSize={} recv={} recvSize={}".format(eventName, data["send_num"], data["send_size"], data["recv_num"], data["recv_size"])
```



## StopRecordPacket

<span style="display:inline;color:#ff5555">仅Apollo可用</span>

method in mod.server.extraServerApi

- 描述

    停止服务端与客户端之间的引擎收发包统计并输出结果，与[StartRecordPacket](#startrecordpacket)配合使用，输出结果为字典，key为网络包名，value字典中记录收发信息，具体见示例，仅支持租赁服与Apollo网络服环境（不支持单机环境）

- 参数

    无

- 返回值

    | <div style="width: 4em">数据类型</div> | 说明 |
    | :--- | :--- |
    | dict | 收发包信息，假如没有调用过StartRecordPacket，则返回为None |

- 示例

```python
import mod.server.extraServerApi as serverApi
suc = serverApi.StartRecordPacket()
# 之后通过计时器或者其他触发方式调用StopRecordPacket
result = serverApi.StopRecordPacket()
for packetName, data in result.iteritems():
    print "packet[{}] send={} sendSize={} recv={} recvSize={}".format(packetName, data["send_num"], data["send_size"], data["recv_num"], data["recv_size"])
```

