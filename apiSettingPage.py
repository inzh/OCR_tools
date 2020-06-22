#!/usr/bin/python3
# encoding:utf-8
from tkinter import *


class ApiPage(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init_Window()

    def init_Window(self):
        # GUI标题
        self.master.title("API设置")
        # 窗口大小
        self.master.geometry(self.get_size(240, 100))
        self.master.resizable(0, 0)

        # 创建部件
        lable_ak = Label(self.master, text='Api Key：')
        lable_sk = Label(self.master, text='Secret Key：')
        entry_ak = Entry(self.master)
        entry_sk = Entry(self.master)
        button = Button(self.master, text="确定", width=19,command=self.get_Key)
        # 放置部件
        lable_ak.grid(row=0, column=0)
        lable_sk.grid(row=1, column=0)
        entry_ak.grid(row=0, column=1)
        entry_sk.grid(row=1, column=1)
        button.grid(row=2, column=1)

    # 填入api key 和 secret key
    def get_Key(self):
        print()

    # 获取界面大小
    def get_size(self, width, height):
        winWidth = width
        winHeight = height
        # 获取屏幕分辨率
        screenWidth = self.master.winfo_screenwidth()
        screenHeight = self.master.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        return ("%sx%s+%s+%s" % (winWidth, winHeight, x, y))


def main():
    root = Tk()
    app = ApiPage(master=root)
    app.mainloop()


if __name__ == '__main__':
    main()
