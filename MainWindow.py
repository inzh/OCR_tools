#!/usr/bin/python3
# encoding:utf-8
from tkinter import *
import apiSettingPage

class MainWindow(Frame):
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
        self.master.geometry(self.get_size(600, 400))
        self.master.resizable(0, 0)
        # 菜单设置
        MenuBar = Menu(self.master)
        # MenuBar.add_cascade(label="百度API设置", command=self.api_settings)
        MenuBar.add_cascade(label="百度API设置", command=apiSettingPage.main)
        self.master.config(menu = MenuBar)

    # 百度API设置页面
    def api_settings(self):
        # 创建顶级窗口
        apiPage = Toplevel()
        # 设置窗口大小、标题
        apiPage.title("百度API设置")
        apiPage.geometry(self.tl.get_size(300, 200))
        apiPage.resizable(0, 0)
        # 设置entry
        ApiKey = StringVar()
        SecretKey = StringVar()
        e1 = Entry(apiPage,textvariable=ApiKey,width=30)
        e2 = Entry(apiPage,textvariable=SecretKey,width=30)
        e1.grid(row=1, column=0, padx=3, pady=50)
        e2.grid(row=2, column=0, padx=1, pady=1)

    # 获取窗口大小
    def get_size(self, width, height):
        winWidth = width
        winHeight = height
        # 获取屏幕分辨率
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        return ("%sx%s+%s+%s" % (winWidth, winHeight, x, y))

    # 推出窗口
    def client_exit(self):
        exit()

if __name__ == '__main__':
    root = Tk()
    app = MainWindow(master=root)
    app.mainloop()