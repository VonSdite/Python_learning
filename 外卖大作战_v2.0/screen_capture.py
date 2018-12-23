#截屏功能, 注意不要去移动窗口
import time
import os, win32gui, win32ui, win32con, win32api
from PIL import Image

#dpath是保存的路径
#srcbmp是列表
#srcbmp 第3, 4个元素代表截取的大小
#scrbmb 第1, 2个元素代表截取的位置
def window_capture(dpath="", srcbmp=[0, 0, None, None]):
    hwnd = 0
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC=win32ui.CreateDCFromHandle(hwndDC)
    saveDC=mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev=win32api.EnumDisplayMonitors(None,None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    if srcbmp[2]==None or (srcbmp[0]+srcbmp[2]>w):
        srcbmp[2] = w
    if srcbmp[3]==None or (srcbmp[1]+srcbmp[3]>w):
        srcbmp[3] = h
    saveBitMap.CreateCompatibleBitmap(mfcDC, srcbmp[2], srcbmp[3])
    saveDC.SelectObject(saveBitMap)
    ddss = (srcbmp[2], srcbmp[3])
    saveDC.BitBlt((0,0), ddss , mfcDC, (srcbmp[0], srcbmp[1]), win32con.SRCCOPY)
    cc=time.gmtime()
    bmpname=dpath+'Result'+'.bmp'
    saveBitMap.SaveBitmapFile(saveDC, bmpname)
    pic = Image.open(bmpname)
    pic.save(dpath + 'Result.jpg')
    os.remove(bmpname)


#调用截屏函数
if __name__ == '__main__':
    window_capture('D:\\Tools\\', [300, 0, 740, 750])
