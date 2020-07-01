#!/usr/bin/python3
# encoding:utf-8

import requests
import base64
import tools
from configparser import ConfigParser


def ocr(path,filename,access_token):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    print(path+filename)
    f = open(path+"\\"+filename, 'rb')
    img = base64.b64encode(f.read())
    params = {"id_card_side":"front","image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json()["words_result"]["公民身份号码"]["words"])
        print(response.json()["words_result"]["姓名"]["words"])

def get_token():
    # client_id = "2MLY2GOxSa7Y6uqoLhP4CN6E"
    # client_secret = "fO1PQKpGCyGLKCONriLVMWodmBbbdymt"
    client_id = tools.getAK()
    client_secret = tools.getSK()

    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret
    response = requests.post(host)
    # print(response.json())
    try:
        access_token = response.json()["access_token"]
        # print(access_token)
    except KeyError:
        return False
    else:
        return access_token


def configSeting():
    ak = input("请输入API Key：")
    sk = input("请输入Secret Key：")
    conf = ConfigParser()
    conf.add_section("config")
    conf.set('config', 'Api Key', ak)
    conf.set('config', 'Secret Key', sk)
    with open('config.cfg', 'w') as fw:
        conf.write(fw)
    print("保存成功")
    print("---------------------------------------------")
# print(get_token())

if __name__ =="__main__":
    get_token()