# coding=utf-8
import cv2
import numpy as np
from win32 import win32gui
import win32ui
import win32con
import win32api
import time


class GrabScreen:
    def __init__(self, region=None, windowed=False):
        scale_ratio = 1.25  # windows系统设置的缩放与布局
        if not windowed:
            self.hwin = win32gui.GetDesktopWindow()
        # win32gui.FindWindow(FrameClass, FrameTitle)
        else:
            self.hwin = win32gui.FindWindow("Valve001", "Counter-Strike: Global Offensive - Direct3D 9")
            # self.hwin = win32gui.FindWindow("ApplicationFrameInputSinkWindow", None)

        self.hwindc = win32gui.GetWindowDC(self.hwin)
        self.srcdc = win32ui.CreateDCFromHandle(self.hwindc)
        self.memdc = self.srcdc.CreateCompatibleDC()
        self.bmp = win32ui.CreateBitmap()
        if region:
            self.left, self.top, x2, y2 = region
            self.width = x2 - self.left
            self.height = y2 - self.top
        elif windowed:
            self.left, self.top, x2, y2 = win32gui.GetWindowRect(self.hwin)
            self.left = int(self.left * scale_ratio)
            self.top = int(self.top * scale_ratio)
            x2 = int(x2 * scale_ratio)
            y2 = int(y2 * scale_ratio)
            self.width = x2 - self.left
            self.height = y2 - self.top
        else:
            self.width = int(win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN) * scale_ratio)
            self.height = int(win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN) * scale_ratio)
            self.left = int(win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN) * scale_ratio)
            self.top = int(win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN) * scale_ratio)

        self.bmp.CreateCompatibleBitmap(self.srcdc, self.width, self.height)

    def release_all(self):
        self.srcdc.DeleteDC()
        self.memdc.DeleteDC()
        win32gui.ReleaseDC(self.hwin, self.hwindc)
        win32gui.DeleteObject(self.bmp.GetHandle())

    def grab(self, RGB=False):
        self.memdc.SelectObject(self.bmp)
        self.memdc.BitBlt((0, 0), (self.width, self.height), self.srcdc, (self.left, self.top), win32con.SRCCOPY)

        signedIntsArray = self.bmp.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        if RGB:
            return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
        else:
            return img[:, :, :-1]


if __name__ == "__main__":
    grab_screen = GrabScreen(region=(0, 0, 1280, 720))
    t1 = time.perf_counter()
    # i = 0
    for i in range(100):
        img = grab_screen.grab()
        # img = grab_screen.grab()
        # cv2.imwrite("./temp/%d_screen.jpg" % i, img)
        # i += 1
    t2 = time.perf_counter()

    print('程序运行时间:%s毫秒' % ((t2 - t1) * 1000))
    grab_screen.release_all()
