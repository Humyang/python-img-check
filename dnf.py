

import screenshort
import dnf_function
import picture
import pyautogui
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')
import time
import datetime
#计算移动距离因子
def get_distance_var():
    # 截图，获取人物当前位置
    # pyCDC=screenshort.window_capture('./temp_screen/')
    # print(moveStart)
    # bd=picture.get_point('./temp_screen/'+moveStart,'./temp_screen/pointA.jpg',0.4)
    dm.Reg(reg.getRegCode(),"")

    bd=picture.get_target_on_screen_point('./temp_screen/pointA.jpg',0.4)
    
    
    # 进入游戏焦点
    # dm.SetSimMode(2)
    # print(dm.SetSimMode(2))#设置硬件模拟
    dm.MoveTo(bd[0],bd[1])
    dm.LeftDoubleClick()
    
    # 行走500毫秒
    dm.KeyDown(38)
    dm.KeyDown(39)
    time.sleep(500/1000)
    dm.KeyUp(38)
    dm.keyUp(39)

    # 截图，获取人物当前位置
    bd2=picture.get_target_on_screen_point('./temp_screen/pointA.jpg',0.4)
    x=abs((bd2[0]-bd[0])/500)
    y=abs((bd2[1]-bd[1])/500)
    return (x,y)
    # 计算两图之间的偏移像素，得到距离因子
    # （结束位置-开始位置）/ 时间 = 每秒的移动距离

print(get_distance_var())
