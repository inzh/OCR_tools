#!/usr/bin/python3
# encoding:utf-8
import requests
import base64
import tools
from tkinter import *
import time, threading
'''
身份证识别
'''

key = None
value = None
access_token = None

def ocr():
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open('D:\\SKM_754e20062111120_0001.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"id_card_side":"front","image":img}
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        return response

def get_token():
    client_id = tools.getAK()
    client_secret = tools.getSK()
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret
    response = requests.post(host)
    # print(response.json())
    token = response.json()
    global access_token
    access_token = token["access_token"]


def output(text):
    str = key +'-----'+ value +'\n'
    text.insert(END,str)

def getres(text):
    res = ocr()
    global key
    global value
    key = res.json()['words_result']['姓名']['words']
    value = res.json()['words_result']['公民身份号码']['words']
    output(text)
    time.sleep(2)
    output(text)
    time.sleep(2)
    output(text)
    time.sleep(2)
    output(text)
    time.sleep(2)
    output(text)
    time.sleep(2)



def main(text):
    get_token()
    t = threading.Thread(target=getres(text))
    t.setDaemon(True)
    t.start()
