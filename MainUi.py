#!/usr/bin/python3
# encoding:utf-8
from tkinter import *
import MenuBarUi
import ocr, tools

class MainUi(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.init_Window()

    # 初始化主窗口
    def init_Window(self):
        # GUI标题
        self.master.title("OCR批量识别身份证")
        # 窗口大小
        self.master.geometry(tools.get_size(width=300, height=400))
        self.master.resizable(0, 0)

        MenuBar = Menu(self.master)
        MenuBar.add_cascade(label="开始运行", command=lambda:ocr.main(text))
        MenuBar.add_cascade(label="百度API设置", command=MenuBarUi.createAPiUi)
        MenuBar.add_cascade(label="选择图片目录", command=MenuBarUi.createPathUi)
        self.master.config(menu=MenuBar)
        scroll = Scrollbar()
        text = Text(self.master, width=40, height=400)
        scroll.pack(side=RIGHT, fill=Y)
        text.pack(side=RIGHT, fill=Y)
        scroll.config(command=text.yview)
        text.config(yscrollcommand=scroll.set)



if __name__ == '__main__':
    root = Tk()
    app = MainUi(master=root)
    app.mainloop()