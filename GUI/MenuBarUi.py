#!/usr/bin/python3
# encoding:utf-8
from tkinter import *
from tkinter.filedialog import askdirectory
import tkinter.messagebox as ms
import tools


# 创建API设置弹窗
def createAPiUi():
    top = Toplevel()
    top.title('API设置')
    top.geometry(tools.get_size(width=240, height=100))
    top.resizable(0, 0)
    akVar = StringVar()
    skVar = StringVar()
    lable_ak = Label(top, text='Api Key：')
    lable_sk = Label(top, text='Secret Key：')
    entry_ak = Entry(top, textvariable=akVar)
    entry_sk = Entry(top, textvariable=skVar)
    button = Button(top, text="确定", width=19, command=lambda:submit(akVar=akVar, skVar=skVar, top = top))
    # 放置部件
    lable_ak.grid(row=0, column=0)
    lable_sk.grid(row=1, column=0)
    entry_ak.grid(row=0, column=1)
    entry_sk.grid(row=1, column=1)
    button.grid(row=2, column=1)

def submit(akVar, skVar, top):
    # tools.configSeting(ak=,sk=)
    ak = akVar.get()
    sk = skVar.get()
    if (ak=="" or sk==""):
        ms.showwarning("警告", "请正确输入信息")
    else:
        tools.configSeting(ak=ak, sk=sk)
        ms.showinfo("提示", "保存成功")
    top.destroy()

def createPathUi():
    top = Toplevel()
    top.title('图片目录选择')
    top.geometry(tools.get_size(width=240, height=100))
    top.resizable(0, 0)
    pathVar = StringVar()

    lable_path = Label(top, text='路径选择：')
    entry_path = Entry(top, textvariable=pathVar)
    button = Button(top, text="选择目录", width=19, command=lambda:selectPath(pathVar, top))
    # 放置部件
    lable_path.grid(row=0, column=0)
    entry_path.grid(row=0, column=1)
    button.grid(row=1, column=1)

def selectPath(pathVar, top):
    path_ = askdirectory()
    pathVar.set(path_)
    path = pathVar.get()
    if (path == ""):
        ms.showwarning("警告", "请选择正确的路径")
    else:
        tools.PathSeting(path=path)
        ms.showinfo("提示", "路径选择成功")
        tools.output()
    top.destroy()


