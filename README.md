# Skland_API
森空岛API接口合集以及文档示例

## 说明

该文档中的API接口均基于鹰角网络森空岛APP中的游戏数据页面。

根据APP内显示数据 本文档可能包含的 API 有：
```
---Header---
入职日 
游戏ID
作战进度
家具保有数
雇佣干员数

---助战干员---
助战干员

---实时数据---
理智 & 恢复时间
公开招募进度
公招刷新
训练室状态
每周报酬合成玉进度 & 刷新时间
每日任务进度 & 刷新时间
每周任务进度 & 刷新时间
数据增补仪进度 & 刷新时间

---我的干员---
干员数据
时装数据

---基建数据---
订单进度
制造进度
休息进度
线索收集进度
干员疲劳状态
无人机数据

---游戏战绩---
别传插曲数据
剿灭作战数据
保全派驻数据
集成战略数据
```

## API快查
```
---鹰角网络凭证获取---
/POST https://as.hypergryph.com/user/auth/v1/token_by_phone_password
{"phone": "手机号","password": "密码"}
返回 {"status":0,"type":"A","msg":"OK","data":{"token":"xxx"}}

/POST https://as.hypergryph.com/general/v1/send_phone_code
{"phone":"199********","type":2}
返回 {"status":0,"type":"A","msg":"OK"}

/POST https://as.hypergryph.com/user/auth/v2/token_by_phone_code
{"phone":"199********","code":"******"}
返回 {"status":0,"type":"A","msg":"OK","data":{"token":"FQyXK4vy**********GkI7Rr"}}

---森空岛凭证获取---
请先获取鹰角网络凭证
/POST https://as.hypergryph.com/user/oauth2/v2/grant
{"token":"鹰角网络凭证","appCode":"4ca99fa6b56cc2ba","type":0}
返回 {"status":0,"type":"A","msg":"OK","data":{"code":"****","uid":"12**********1"}}

/POST https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code
{"kind":1,"code":"****"}
返回 {"code":0,"message":"OK","data":{"cred":"32位凭证","userId":"8****3"}}

---森空岛凭证校验(存活/有效性)---
/POST https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code
header['cred'] = 32位cred

返回 {"code":0,"message":"OK","data":{"policyList":[],"isNewUser":false}}

```

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

**状态码：**

- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述

**响应说明：**

- 当请求成功时，会返回状态码0，以及一个包含用户令牌的JSON数据。
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。

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

**状态码：**

- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述

**响应说明：**

- 当请求成功时，会返回状态码0，以及一个包含用户令牌的JSON数据。
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。

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

**状态码：**

- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述

**响应说明**

- 当请求成功时，会返回状态码0，以及一个包含授权代码和用户ID的JSON数据。
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。

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

**状态码：**

- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述

**响应说明**

- 当请求成功时，会返回状态码0，以及一个包含Cred和用户ID的JSON数据。
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。

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

**状态码：**

- **0：** 请求成功
- **其他值：** 各种错误情况，可以在响应消息中查看详细描述

**响应说明**

- 当请求成功时，会返回状态码0，以及一个包含策略列表和新用户状态的JSON数据。
- 如果请求失败，状态码会反映错误的类型，并在响应消息中提供详细描述。