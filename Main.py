# encoding:utf-8
import requests
import base64
import json

'''
身份证识别
'''


def get_token():
    client_id = '2MLY2GOxSa7Y6uqoLhP4CN6E'
    client_secret = 'fO1PQKpGCyGLKCONriLVMWodmBbbdymt'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id='+client_id+'&client_secret='+client_secret
    response = requests.post(host)
    json_str = json.dumps(response.json())
    token = json.loads(json_str)
    return token["access_token"]


def ocr():
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/idcard"
    # 二进制方式打开图片文件
    f = open('D:\\SKM_754e20062111120_0001.jpg', 'rb')
    img = base64.b64encode(f.read())
    params = {"id_card_side":"front","image":img}
    access_token = get_token()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())

ocr()