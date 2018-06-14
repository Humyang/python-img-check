import win32gui

def get_window_info(hwnd):  # 获取阴阳师窗口信息
    wdname = u'阴阳师-网易游戏'
    # handle = win32gui.FindWindow(pid,'')  # 获取窗口句柄
    t = win32gui.GetWindowText(hwnd)
    if t:
        print(t)
    # if handle == 0:
    #     # text.insert('end', '小轩提示：请打开PC端阴阳师\n')
    #     # text.see('end')  # 自动显示底部
    #     return None
    # else:
    #     return win32gui.GetWindowRect(handle)

def callback_a(a,b):
    get_window_info(a)
    # print(a,b)
    # win32gui.FindWindow(0, wdname)

# win32gui.EnumWindows(callback_a,[])
