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

import moveNext

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



def onMap1():
    m1=picture.match_multiple(img_gray,'./img/map1_a.jpg',0.9)
    
    if m1!=False:
        # 刚进入图1
        print('图1a 召唤兽')
        callAll()
        
    else:
        m2=picture.match_multiple(img_gray,'./img/map1_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图1 行走')
            moveNext.map1MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map1_b_2.jpg')
            if m3!=False:
                print('图1 行走')
                moveNext.map1MoveNext()
            else:
                print('no map1')

def onMap2():
    m1=picture.match_multiple(img_gray,'./img/map2_a.jpg',0.9)
    if m1!=False:
        print('刚进入图2')
    else:
        m2=picture.match_multiple(img_gray,'./img/map2_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图2 行走')
            moveNext.map2MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map2_b_2.jpg')
            if m3!=False:
                print('图2 行走')
                moveNext.map2MoveNext()
            else:
                print('no map2')
def onMap3():
    m1=picture.match_multiple(img_gray,'./img/map3_a.jpg',0.9)
    if m1!=False:
        print('刚进入图3')
    else:
        m2=picture.match_multiple(img_gray,'./img/map3_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图3 行走')
            moveNext.map3MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map3_b_2.jpg')
            if m3!=False:
                print('图3 行走')
                moveNext.map3MoveNext()
            else:
                print('no map3')

def onMap4():
    m1=picture.match_multiple(img_gray,'./img/map4_a.jpg',0.9)
    if m1!=False:
        print('刚进入图4')
    else:
        m2=picture.match_multiple(img_gray,'./img/map4_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图4 行走')
            moveNext.map4MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map4_b_2.jpg')
            if m3!=False:
                print('图4 行走')
                moveNext.map4MoveNext()
            else:
                print('no map4')

def onMap5():
    m1=picture.match_multiple(img_gray,'./img/map5_a.jpg',0.9)
    if m1!=False:
        print('刚进入图5')
    else:
        m2=picture.match_multiple(img_gray,'./img/map5_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图5 行走')
            moveNext.map5MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map5_b_2.jpg')
            if m3!=False:
                print('图5 行走')
                moveNext.map5MoveNext()
            else:
                print('no map5')

def onMap6():
    m1=picture.match_multiple(img_gray,'./img/map6_a.jpg',0.9)
    if m1!=False:
        print('刚进入图6')
    else:
        m2=picture.match_multiple(img_gray,'./img/map6_b_1.jpg')
        if m2!=False:
            #图1 结束
            print('图6 行走')
            moveNext.map6MoveNext()
        else:
            m3=picture.match_multiple(img_gray,'./img/map6_b_2.jpg')
            if m3!=False:
                print('图6 行走')
                moveNext.map6MoveNext()
            else:
                print('no map6')

# 召唤所有生物
def callAll():
    dm.KeyPressStr('qwertasdfg',1000)

def main():
    firstEnter()
    onMap1()
    onMap2()
    onMap3()
    onMap4()
    onMap5()
    onMap6()
    main()

main()
# moveNext.map2MoveNext()
# map1MoveNext()
# map2MoveNext()
# map3MoveNext()
# map4MoveNext()
# map5MoveNext()
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
