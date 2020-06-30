#!/usr/bin/python3
# encoding:utf-8
import apisettings as apis
from tkinter import *
import tkinter.filedialog
import os

def welcomeinfo():
    print("--------------------------------------------------")
    print("           欢迎使用身份证批量OCR工具"+"\033[31m[v0.0.1]")
    print("\033[0m             -- 作者 | 收集阳光的暖风 --")
    print('\033[0m--------------------------------------------------')

def checkapi():
    token = None
    while(token == None):
        print("\033[32m正在检查百度Api是否正确设置......")
        token = apis.get_token()
        if token==False:
            print("设置错误！ 请输入正确的Api Key和Secret Key")
            token = apis.configSeting()
    print("设置正确！")
    print("-----------------------------------")
    return True

def setpath():
    path = input("请填写身份证图片所在文件夹：")
    if os.path.exists(path)
        print("路径设置错误，请重新输入：")

if __name__ =="__main__":
    welcomeinfo()
    checkapi()
    setpath()