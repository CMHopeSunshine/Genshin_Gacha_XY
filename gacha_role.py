import os
import json


FILE_PATH = os.path.dirname(__file__)
USER_INFO_PATH = os.path.join(FILE_PATH,"user_info.json")


user_info = {}


def save_user_info():
    with open(USER_INFO_PATH,'w',encoding='UTF-8') as f:
        json.dump(user_info,f,ensure_ascii=False)

# 检查user_info.json是否存在，没有创建空的
if not os.path.exists(USER_INFO_PATH):
    save_user_info()

# 读取user_info.json的信息
with open(USER_INFO_PATH,'r',encoding='UTF-8') as f:
    user_info = json.load(f)


def init_user_info(uid:str):
    if not (uid in user_info):
        user_info[uid] = {}
        user_info[uid]["fate"] = 200
        user_info[uid]["gacha_list"] = {}
        user_info[uid]["gacha_list"]["wish_total"] = 0
        user_info[uid]["gacha_list"]["wish_4"] = 0
        user_info[uid]["gacha_list"]["wish_5"] = 0
        user_info[uid]["gacha_list"]["wish_4_up"] = 0
        user_info[uid]["gacha_list"]["wish_5_up"] = 0
        user_info[uid]["gacha_list"]["gacha_5_role"] = 0
        user_info[uid]["gacha_list"]["gacha_5_weapon"] = 0
        user_info[uid]["gacha_list"]["gacha_5_permanent"] = 0
        user_info[uid]["gacha_list"]["gacha_4_role"] = 0
        user_info[uid]["gacha_list"]["gacha_4_weapon"] = 0
        user_info[uid]["gacha_list"]["gacha_4_permanent"] = 0
        user_info[uid]["gacha_list"]["is_up_5_role"] = False
        user_info[uid]["gacha_list"]["is_up_5_weapon"] = False
        user_info[uid]["gacha_list"]["is_up_4_role"] = False
        user_info[uid]["gacha_list"]["is_up_4_weapon"] = False
        user_info[uid]["gacha_list"]["dg_name"] = ''
        user_info[uid]["gacha_list"]["dg_time"] = 0
        user_info[uid]["role_list"] = {}
        user_info[uid]["role_list"]["旅行者"] = {}
        user_info[uid]["role_list"]["旅行者"]["星级"] = '★★★★★'
        user_info[uid]["role_list"]["旅行者"]["数量"] = 6
        user_info[uid]["role_list"]["旅行者"]["出货"] = [0]
        user_info[uid]["weapon_list"] = {}
        save_user_info()
