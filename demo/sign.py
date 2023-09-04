import requests

def get_binding_list(cred):
    # 获取绑定列表
    binding_url = "https://zonai.skland.com/api/v1/game/player/binding"
    header = {
        "Cred": cred
    }
    response = requests.get(binding_url, headers=header)
    binding_data = response.json()
    
    if binding_data["code"] == 0:
        binding_list = binding_data["data"]["list"]
        return binding_list
    else:
        print("获取绑定列表失败:", binding_data["message"])
        return []

def complete_attendance(cred, uid, channel_master_id):
    # 完成签到
    attendance_url = "https://zonai.skland.com/api/v1/game/attendance"
    header = {
        "Cred": cred
    }
    body = {
        "uid": uid,
        "gameId": channel_master_id
    }
    response = requests.post(attendance_url, headers=header, json=body)
    attendance_data = response.json()
    
    if attendance_data["code"] == 0:
        print("签到成功")
    else:
        print("签到失败:", attendance_data["message"])

cred = "demoCred"

if cred:
    print("获取的Cred:", cred)
    # 获取绑定列表
    binding_list = get_binding_list(cred)
    
    if binding_list:
        for item in binding_list:
            uid = item["bindingList"][0]["uid"]
            channel_master_id = item["bindingList"][0]["channelMasterId"]
            complete_attendance(cred, uid, channel_master_id)
