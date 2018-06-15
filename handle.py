import win32gui

# 根据窗口名称获取 获取窗口区域
def get_window_info(wname): 
    handle = win32gui.FindWindow(0,wname)
    # t = win32gui.GetWindowText(handle)
    # left, top, right, bottom
    rect=win32gui.GetWindowRect(handle)
    return rect

def callback_a(a,b):
    get_window_info(a)

# import win32api
from win32api import GetSystemMetrics
# # 获取屏幕分辨率
def DisplaySize():
    return GetSystemMetrics(0), GetSystemMetrics(1)

# a, b = DisplaySize()

# win32gui.EnumWindows(callback_a,[])
# def c:

# print(fw)
# c()
# print(get_window_info('无标题 - 画图'))
# print(DisplaySize())