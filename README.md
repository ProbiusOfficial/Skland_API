# Skland_API
森空岛API接口合集以及文档示例

因为工作和时间关系本项目不再维护。

[明日方舟工具箱 / 罗德岛移动终端 开发组](https://www.bilibili.com/video/BV13Z421J7QF)

## 说明

该文档中的API接口均基于鹰角网络森空岛APP中的游戏数据页面。

根据APP内显示数据 本文档可能包含的 API 以及json数据路径

更多实现以及可能请关注 [API数据解读](##API数据解读) 部分

| 数据项                        | 数据值                                        |
| ----------------------------- | --------------------------------------------- |
| **---Header---**              |                                               |
| 入职日期时间戳                | data.status.registerTs                        |
| 游戏昵称                      | data.status.name                              |
| 作战进度                      | data.status.mainStageProgress                 |
| 家具保有数                    | data.building.furniture                       |
| 雇佣干员数                    | 好像没有直接返回，像是遍历 data.chars 数组    |
| **助战干员**                  |                                               |
| 助战干员                      | data.assistChars                              |
| **---实时数据---**            |                                               |
| 理智 & 恢复时间               | data.status.ap.current /.completeRecoveryTime |
| 公开招募进度                  | data.building.hire.completeWorkTime           |
| 公招刷新                      | data.building.hire.refreshCount               |
| 训练室状态                    | data.building.training.trainee                |
| 每周报酬合成玉进度 & 刷新时间 | data.campaign.reward                          |
| 每日任务进度 & 刷新时间       | data.routine.daily                            |
| 每周任务进度 & 刷新时间       | data.routine.weekly                           |
| 数据增补仪进度 & 刷新时间     | data.tower.reward.lowerItem                   |
| 数据增补条进度 & 刷新时间     | data.tower.reward.higherItem                  |
| **---我的干员---**            |                                               |
| 干员数据                      | data.chars                                    |
| 时装数据                      | data.skins                                    |
| **---基建数据---**            |                                               |
| 订单进度 \| 贸易站数据        | data.building.tradings                        |
| 制造进度 \| 制造站数据        | data.building.manufactures                    |
| 休息进度 \| 宿舍数据          | data.building.dormitories                     |
| 线索收集进度 \| 会客室数据    | data.building.meeting.clue.board              |
| 干员疲劳状态                  | data.building.tiredChars                      |
| 无人机数据                    | data.building.labor                           |
| **---游戏战绩---**            |                                               |
| 别传插曲数据                  |                                               |
| 剿灭作战数据                  | data.campaign                                 |
| 保全派驻数据                  | data.tower                                    |
| 集成战略数据                  | data.rogue                                    |

在没有特殊说明的情况下，下面的情况保持默认  
**状态码：**
- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述  

**响应说明:**
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。

## 获取鹰角账号凭证(登录)

注意 鹰角网络通行证账号登录凭证 是用于 鹰角网络账号系统校验您登录的唯一凭证，

是鹰角网络所有API交互的身份标识基础。

泄露登录凭证属于极度危险操作，为了您的账号安全，请勿将此凭证以任何形式告知他人！

### 使用账号密码登录

**API名称：** 通过手机号和密码获取凭证

**API请求URL：** `https://as.hypergryph.com/user/auth/v1/token_by_phone_password`

**请求方法：** /POST

**请求参数：** JSON格式(application/json)

| 参数名   | 类型   | 必需 | 描述       |
| -------- | ------ | ---- | ---------- |
| phone    | string | 是   | 用户手机号 |
| password | string | 是   | 用户密码   |

**请求示例：**

```json
{
  "phone": "手机号",
  "password": "密码"
}
```

**响应：** JSON格式

| 参数名 | 类型   | 描述                   |
| ------ | ------ | ---------------------- |
| status | int    | 响应状态码 (0表示成功) |
| type   | string | 响应类型               |
| msg    | string | 响应消息               |
| data   | object | 响应数据               |

**响应示例：**

```json
{
    "status": 0,
    "type": "A",
    "msg": "OK",
    "data": {
        "token": "xxx"
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含用户令牌的JSON数据。


### 使用手机验证码登录

#### 发送手机验证码

此 API 允许用户请求发送验证码到指定手机号，用于后续的验证码登录流程。

**请求URL：** `https://as.hypergryph.com/general/v1/send_phone_code`

**请求方法：** POST

**请求参数：** JSON格式(application/json)

| 参数名 | 类型   | 必需 | 描述                     |
| ------ | ------ | ---- | ------------------------ |
| phone  | string | 是   | 用户手机号               |
| type   | int    | 是   | 验证码类型 (这里填写 2 ) |

**请求示例：**

```json
{
  "phone": "199********",
  "type": 2
}
```

**响应:**

```json
{
    "status": 0,
    "type": "A",
    "msg": "OK"
}
```



#### 获取验证码登录令牌

用户在输入收到的验证码后，使用此 API 获取与手机号相关联的令牌，以完成登录流程。

**请求URL：** `https://as.hypergryph.com/user/auth/v2/token_by_phone_code`

**请求方法：** POST

**请求参数：** JSON格式(application/json)

| 参数名 | 类型   | 必需 | 描述         |
| ------ | ------ | ---- | ------------ |
| phone  | string | 是   | 用户手机号   |
| code   | string | 是   | 输入的验证码 |

**请求示例：**

```json
{
  "phone": "199********",
  "code": "******"
}
```

**响应：** JSON格式

| 参数名 | 类型   | 描述                   |
| ------ | ------ | ---------------------- |
| status | int    | 响应状态码 (0表示成功) |
| type   | string | 响应类型               |
| msg    | string | 响应消息               |
| data   | object | 响应数据               |

**响应示例：**

```json
{
    "status": 0,
    "type": "A",
    "msg": "OK",
    "data": {
        "token": "FQyXK4vy**********GkI7Rr"
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含用户令牌的JSON数据。



### 鹰角账号凭证校验

**请求URL：** `https://as.hypergryph.com/user/info/v1/basic?token=鹰角账号凭证`

**请求方法：** GET

**请求参数：**

| 参数名 | 类型   | 必需 | 描述         |
| ------ | ------ | ---- | ------------ |
| token  | string | 是   | 鹰角账号凭证 |

**请求示例：**

```
无请求体，仅包含查询参数 token
```

**响应：** JSON格式

| 参数名 | 类型   | 描述                   |
| ------ | ------ | ---------------------- |
| status | int    | 响应状态码 (0表示成功) |
| type   | string | 响应类型               |
| msg    | string | 响应消息               |
| data   | object | 响应数据               |

**响应示例：**

```json
{
    "status": 0,
    "type": "A",
    "msg": "OK",
    "data": {
        "hgId": "1*********6",// 鹰角账号id 注意，该部分会完全显示
        "phone": "199****9999",// 手机号 注意，打码部分不会显示
        "email": null, // 绑定邮箱
        "identityNum": "1111**********1111", // 身份证信息 注意，中间打码部分不会显示
        "identityName": "探**",// 姓名信息 注意，只会显示姓氏
        "isMinor": false, // 是否未成年
        "isLatestUserAgreement": true // 用户是否已同意了最新的用户协议
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含用户基本信息的JSON数据。



## 获取森空岛凭证

森空岛的API使用cred作为身份凭证，当然该凭证基于鹰角网络通行证账号登录凭证生成。

### 获取 OAuth2 授权代码

此 API 允许用户使用令牌进行 OAuth2 授权操作。

**请求URL：** `https://as.hypergryph.com/user/oauth2/v2/grant`

**请求方法：** POST

**请求参数：** JSON格式(application/json)

| 参数名  | 类型   | 必需 | 描述                                                   |
| ------- | ------ | ---- | ------------------------------------------------------ |
| token   | string | 是   | 鹰角网络通行证账号登录凭证                             |
| appCode | string | 是   | 应用程序代码<br />(此处为 : `4ca99fa6b56cc2ba` 固定值) |
| type    | int    | 是   | 授权类型 (此处为：0)                                   |

**请求示例：**

```json
{
  "token": "FQyXK4vy**********GkI7Rr",
  "appCode": "4ca99fa6b56cc2ba",
  "type": 0
}
```

**响应：** JSON格式

| 参数名 | 类型   | 描述                   |
| ------ | ------ | ---------------------- |
| status | int    | 响应状态码 (0表示成功) |
| type   | string | 响应类型               |
| msg    | string | 响应消息               |
| data   | object | 响应数据               |

**响应示例：**

```json
{
    "status": 0,
    "type": "A",
    "msg": "OK",
    "data": {
        "code": "mmKkGqm******************************************************************UjnSamjI9ow==",
        "uid": "12**********1"
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含授权代码和用户ID的JSON数据。



### 获取Cred

此 API 将使用上一步的OAuth2 授权代码获取Cred。

**请求URL：** `https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code`

**请求方法：** POST

**请求参数：** JSON格式

| 参数名 | 类型   | 必需 | 描述               |
| ------ | ------ | ---- | ------------------ |
| kind   | int    | 是   | 授权类型 (例如：1) |
| code   | string | 是   | 授权代码           |

**请求示例：**

```
{
  "kind": 1,
  "code": "mmKkGqm******************************************************************UjnSamjI9ow=="
}
```

**响应：** JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应示例：**

```
{
    "code": 0,
    "message": "OK",
    "data": {
        "cred": "********************************",
        "userId": "8****3"
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含Cred和用户ID的JSON数据。


### Cred校验

此 API 可以校验Cred的有效性，可用于过期提醒和其他操作。

**请求URL：** `https://zonai.skland.com/api/v1/user/check`

**请求方法：** GET

**请求头：**

| Header | 值                               |
| ------ | -------------------------------- |
| Cred   | `********************************` 32位 Cred 的值 |

**请求示例：**

```
无请求体，仅包含请求头
```

**响应：** JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应示例：**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "policyList": [],
        "isNewUser": false
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含策略列表和新用户状态的JSON数据。



## 功能性接口

### 获取账号信息

（其实就是把Cookie中的ACCOUNT取出来显示罢了，对普通用户的辅助API吧xd）

**请求URL：** `https://web-api.skland.com/account/info/hg`

**请求方法：** GET

**请求头：**

| Header | 值                            |
| ------ | ----------------------------- |
| Cookie | ACCOUNT=`JZ*********+Zk2sXaas` |

**请求示例：**

```
无请求体，仅包含请求头
```

**响应：** JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应示例：**

```json
{
    "code": 0,
    "data": {
        "content": "JZ*********+Zk2sXaas"
    },
    "msg": "接口会返回您的鹰角网络通行证账号的登录凭证，此凭证可以用于鹰角网络账号系统校验您登录的有效性。泄露登录凭证属于极度危险操作，为了您的账号安全，请勿将此凭证以任何形式告知他人！"
}
```

## 森空岛APP

### 获取玩家绑定角色列表

**请求URL：** `https://zonai.skland.com/api/v1/game/player/binding`

**请求方法：** GET

**请求头：**

| Header | 值           |
| ------ | ------------ |
| Cred   | 鹰角账号凭证 |

**请求示例：**

```
无请求体，仅包含请求头
```

**响应：** JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应示例：**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "list": [
            {
                "appCode": "arknights",
                "appName": "明日方舟",
                "bindingList": [
                    {
                        "uid": "68463675",
                        "isOfficial": true,
                        "isDefault": true,
                        "channelMasterId": "1",
                        "channelName": "官服",
                        "nickName": "探姬#9315",
                        "isDelete": false
                    }
                ],
                "defaultUid": ""
            }
        ]
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含游戏玩家绑定信息的JSON数据。

### 签到

此 API 允许用户进行游戏签到操作，获取签到奖励。

**请求URL：** `https://zonai.skland.com/api/v1/game/attendance`

**请求方法：** POST

**请求头：**

| Header | 值   |
| ------ | ---- |
| cred   | xxxx |

**请求体：** JSON格式

| 参数名 | 类型   | 必需 | 描述            |
| ------ | ------ | ---- | --------------- |
| uid    | string | 是   | uid             |
| gameId | string | 是   | channelMasterId |

**请求示例：**

```json
{
    "uid": "uid",
    "gameId": "channelMasterId"
}
```

**响应：**  JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应数据示例：**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        "ts": "1693823939",
        "awards": [
            {
                "resource": {
                    "id": "4003",
                    "type": "DIAMOND_SHD",
                    "name": "合成玉",
                    "rarity": 4
                },
                "count": 500,
                "type": "first"
            },
            {
                "resource": {
                    "id": "2002",
                    "type": "CARD_EXP",
                    "name": "初级作战记录",
                    "rarity": 2
                },
                "count": 3,
                "type": "daily"
            }
        ]
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含签到奖励信息的JSON数据。

## 游戏内数据

### 获取玩家数据

此 API 允许用户通过Cred和用户ID（uid）获取其在游戏内的相关数据，emm 直接dump了1w行（（（

**请求URL：** `https://zonai.skland.com/api/v1/game/player/info`

**请求方法：** GET

**请求头：**

| Header | 值   |
| ------ | ---- |
| cred   | xxxx |

**请求参数：**

| 参数名 | 类型   | 必需 | 描述   |
| ------ | ------ | ---- | ------ |
| uid    | string | 是   | 用户ID |

**请求示例：**

```
Copy code
无请求体，仅包含查询参数 uid
```

**响应：**JSON格式

| 参数名  | 类型   | 描述                   |
| ------- | ------ | ---------------------- |
| code    | int    | 响应状态码 (0表示成功) |
| message | string | 响应消息               |
| data    | object | 响应数据               |

**响应数据示例：**

```json
{
    "code": 0,
    "message": "OK",
    "data": {
        // huge data
    }
}
```

**响应说明:**

- 当请求成功时，会返回状态码0，以及一个包含游戏内玩家数据的JSON数据。

(由于篇幅原因 放在[dump.json](./dump.json) 中 有需要的博士可以自行查看（悲)

## API数据解读
部分数据解读，欢迎pr更新，以便完成自动化更多的可能性:p

| 键                               | 描述                                                         |
| -------------------------------- | ------------------------------------------------------------ |
| data.status.uid                  | 用户id                                                       |
| data.status.name                 | 用户昵称                                                     |
| data.status.level                | 用户等级                                                     |
| data.status.avatar               | 用户头像，但是是中文key，需要app本地缓存图片对应上           |
| data.status.registerTs           | 注册日期                                                     |
| data.status.mainStageProgress    | 主线剧情（全通关是返回空，其他情况需要账号测试）             |
| data.status.secretary            | 未知！！！！！！！！！！！！！                               |
| data.status.ap                   | 理智数据                                                     |
|                   |                                                    |
| data.assistChars                 | 助战数据                                                     |
| data.assistChars.charId          | 助战人员key                                                  |
| data.assistChars.skinId          | 皮肤key                                                      |
| data.assistChars.evolvePhase     | 精英化等级                                                   |
| data.assistChars.level           | 等级                                                         |
| data.assistChars.potentialRank   | 潜力                                                         |
| data.assistChars.skillId         | 技能key                                                      |
| data.assistChars.mainSkillLvl    | 技能等级                                                     |
| data.assistChars.specializeLevel | 技能专精等级                                                 |
| data.assistChars.equip           | 模组key和等级                                                |
|                   |                                                    |
| data.chars                       | 所有干员数据！（等级专精获得时间等所有数据）                 |
| data.skins                       | 所有皮肤数据！皮肤key和获得时间                              |
|                   |                                                    |
| data.building                    | 基建数据                                                     |
| data.building.tiredChars         | 看起来像是疲劳到底的干员列表，未确定！！！！！！！！！！！！！ |
| data.building.powers             | 看起来是发电站数据，但数据结构没看懂是干嘛的                 |
| data.building.manufactures       | 制造站数据                                                   |
| data.building.tradings           | 贸易站数据                                                   |
| data.building.dormitories        | 宿舍数据                                                     |
| data.building.meeting            | 会客室数据                                                   |
| data.building.hire               | 办公室数据                                                   |
| data.building.training           | 训练室数据                                                   |
| data.building.labor              | 无人机数据                                                   |
| data.building.furniture          | 家具数量                                                     |
| data.building.elevators          | 未知！！！！ 有12条数据                                      |
| data.building.corridors          | 未知！！！！ 有8条数据                                       |
| data.building.control            | 控制中枢进驻信息                                             |
|                   |                                                    |
| data.recruit                     | 公招4个栏位的信息                                            |
|                   |                                                    |
| data.campaign                    | 剿灭                                                         |
| data.campaign.records            | 剿灭各地图的key和最大击杀数（由此可推断某些图还要打）        |
| data.campaign.reward             | 剿灭每周合成玉奖励数据：总数和已获得数                       |
|                   |                                                    |
| data.tower                       | 保全派驻数据，数据结构同剿灭                                 |
|                   |                                                    |
| data.rogue                       | 肉鸽数据                                                     |
| data.rogue.relicCnt              | 收藏品数量                                                   |
| data.rogue.bank                  | 前瞻性投资系统                                               |
|                   |                                                    |
| data.routine                     | 任务完成情况，总数和已完成数                                 |
| data.activity                    | 看起来像是别转数据                                           |
| data.charInfoMap                 | 根据干员key获取干员详情，但数据未看懂做什么用！！！！！！    |
| data.skinInfoMap                 | 根据皮肤key获取皮肤详情，包含获得方式和brandId               |
| data.activityBannerList          | 森空岛的banner，和时机活动无关，还展示的火山旅梦数据         |

