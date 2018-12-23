import time
import os, win32gui, win32ui, win32con, win32api

#dpath是保存的路径
#srcbmp是列表
#srcbmp 第3, 4个元素代表截取的大小
#scrbmb 第1, 2个元素代表截取的位置
def window_capture(dpath, srcbmp=[0, 0, None, None]):
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
    #saveDC.BitBlt((0,0),(w, h) , mfcDC, (0,0), win32con.SRCCOPY)
    ddss = (srcbmp[2], srcbmp[3])
    saveDC.BitBlt((0,0), ddss , mfcDC, (srcbmp[0], srcbmp[1]), win32con.SRCCOPY)
    cc=time.gmtime()
    bmpname=dpath+str(cc[0])+str(cc[1])+str(cc[2])+str(cc[3]+8)+str(cc[4])+str(cc[5])+'.bmp'
    saveBitMap.SaveBitmapFile(saveDC, bmpname)


#调用截屏函数
if __name__ == '__main__':
    window_capture('D:\\Tools\\', [300, 0, 740, 750])
