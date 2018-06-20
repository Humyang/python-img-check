import sys
sys.path.append('../../module/')
import cv2
import numpy as np
import pyautogui
import picture

import reg
import mouse
import time
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')
dm.Reg(reg.getRegCode(),"")


# image = pyautogui.screenshot()
# img_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
img_gray=picture.get_image_gray()

# 搜索图1（城镇状态）
    # 进入地下城选择页面
        # 获取当前位置
        # 获取入口位置(地图直接进入)
        # 移动至入口
def firstEnter():
    global img_gray
#搜索图2（地下城选择页面)
    # 搜索要刷的地下城
        #鼠标移动到该位置
            #点击进入
    pick_map=mouse.findImgAndClick(img_gray=img_gray,
    target='./img/b.jpg',
    value=0.8,
    offsetX=50,
    offsetY=50)
    if pick_map==True:
        img_gray=picture.get_image_gray()
        # 选择地下城难度
        stage=mouse.findImgAndClick(img_gray=img_gray,
        target='./img/pick_map_stage_add.jpg',
        value=0.8,
        offsetX=25,
        offsetY=25,clickNum=3)
        img_gray=picture.get_image_gray()
    else:
        # 选择地下城难度
        stage=mouse.findImgAndClick(img_gray=img_gray,
        target='./img/pick_map_stage_add.jpg',
        value=0.8,
        offsetX=25,
        offsetY=25,clickNum=3)
        img_gray=picture.get_image_gray()
    # 点击进入地下城
    mouse.findImgAndClick(img_gray=img_gray,
        target='./img/a.jpg',
        value=0.8,
        offsetX=25,
        offsetY=-125)

def onMap():
    onJob=picture.match_multiple(img_gray,'./img/map1_a.jpg')
    print(onJob)
    if onJob!=False:
        # 召唤所有
        callAll()
    else:
        print(1)
    #搜索图3（处于地下城中)
    # 召唤宠物
        # 顺序按下技能键


# 召唤所有生物
def callAll():
    dm.KeyPressStr('qwertasdfg',200)

def main():
    firstEnter()
    onMap()
    main()
main()


#搜索图4（地下城房间清除完毕）
    # 进入下一个房间
        # 获取当前位置
        # 获取入口位置
        # 移动至入口

#搜索图5（地下城清除完成）
    # 再次挑战

#搜索图6（发现物品掉落）
    #移动至物品
        #点击拾取
