#!/usr/bin/python3
# encoding:utf-8
import apisettings as apis
import os,time,tools,msvcrt
global path,access_token



from colorama import init
init(autoreset=True)


def printline():
    print("-----------------------------------")

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
            print("\033[31m设置错误！ 请输入正确的Api Key和Secret Key")
            apis.configSeting()
            token = apis.get_token()
    global access_token
    access_token = token
    # print(access_token)
    print("\033[32m设置正确！")
    print("-----------------------------------")
    return True

def setpath():
    global path
    path = input("请填写身份证图片所在文件夹：")
    while not os.path.exists(path):
        print("\033[31m路径设置错误! 请重新输入")
        printline()
        path = input("请填写身份证图片所在文件夹：")
    print("\033[32m路径设置正确")
    printline()




def ocrmain():
    tools.create_sheet()
    tools.set_sheet()
    f_list = os.listdir(path)
    # print f_list
    for filename in f_list:
        # os.path.splitext():分离文件名与扩展名
        suf = os.path.splitext(filename)[1]
        if suf == '.jpg' or suf == '.png':
            global access_token
            apis.ocr(path,filename,access_token)
            time.sleep(1)


if __name__ =="__main__":
    welcomeinfo()
    checkapi()
    setpath()
    ocrmain()
    print("识别完成，按d退出程序")
    while True:
        if ord(msvcrt.getch()) in [68, 100]:
            break