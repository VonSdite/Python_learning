#设置窗口大小 并设置窗口位置
def center_window(root, x, y, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, x, y)  
    root.geometry(size)