import requests

def login_and_get_cred(phone, password):
    # 通过手机号和密码获取Token
    login_url = "https://as.hypergryph.com/user/auth/v1/token_by_phone_password"
    login_data = {
        "phone": phone,
        "password": password
    }
    login_response = requests.post(login_url, json=login_data)
    login_data = login_response.json()
    
    if login_data["status"] == 0:
        token = login_data["data"]["token"]
        
        # 使用Token获取OAuth2授权代码
        oauth2_url = "https://as.hypergryph.com/user/oauth2/v2/grant"
        oauth2_data = {
            "token": token,
            "appCode": "4ca99fa6b56cc2ba",  
            "type": 0
        }
        oauth2_response = requests.post(oauth2_url, json=oauth2_data)
        oauth2_data = oauth2_response.json()
        
        if oauth2_data["status"] == 0:
            auth_code = oauth2_data["data"]["code"]
            
            # 使用OAuth2授权代码获取Cred
            cred_url = "https://zonai.skland.com/api/v1/user/auth/generate_cred_by_code"
            cred_data = {
                "kind": 1,
                "code": auth_code
            }
            cred_response = requests.post(cred_url, json=cred_data)
            cred_data = cred_response.json()
            
            if cred_data["code"] == 0:
                cred = cred_data["data"]["cred"]
                return cred
            else:
                print("获取Cred失败:", cred_data["message"])
        else:
            print("获取OAuth2授权代码失败:", oauth2_data["message"])
    else:
        print("登录失败:", login_data["message"])
    
    return None

# 使用手机号和密码调用函数
phone = "demophone"
password = "demopasswd"
cred = login_and_get_cred(phone, password)
if cred:
    print("获取的Cred:", cred)
