import ctypes
from configparser import ConfigParser

def get_size(width, height):
    winWidth = width
    winHeight = height
    # 获取屏幕分辨率
    winapi = ctypes.windll.user32
    screenWidth = winapi.GetSystemMetrics(0)
    screenHeight = winapi.GetSystemMetrics(1)
    # screenWidth = x
    # screenHeight = y
    # print(screenWidth)
    # print(screenHeight)
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    return ("%sx%s+%s+%s" % (winWidth, winHeight, x, y))

def configSeting(ak, sk):
    conf = ConfigParser()
    conf.add_section("config")
    conf.set('config', 'Api Key', ak)
    conf.set('config', 'Secret Key', sk)
    with open('config.ini', 'w') as fw:
        conf.write(fw)

def PathSeting(path):
    conf = ConfigParser()
    conf.add_section("path")
    conf.set('path', 'path', path)
    with open('config.cfg', 'a') as fw:
        conf.write(fw)

def getAK():
    conf = ConfigParser()
    file = 'config.cfg'
    conf.read(file)
    ak = conf.get("config","api key")
    return ak

def getSK():
    conf = ConfigParser()
    file = 'config.cfg'
    conf.read(file)
    sk = conf.get("config", "secret key")
    return sk

# def output(text，key, value):
#     text.insert(key, key+'------'+value+'\n')

