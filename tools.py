def get_size(self, width, height):
    winWidth = width
    winHeight = height
    # 获取屏幕分辨率
    screenWidth = self.master.winfo_screenwidth()
    screenHeight = self.master.winfo_screenheight()
    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    return ("%sx%s+%s+%s" % (winWidth, winHeight, x, y))