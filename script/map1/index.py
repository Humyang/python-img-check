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
import dnf_function
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
        updateImgGray()
        # 选择地下城难度
        stage=mouse.findImgAndClick(img_gray=img_gray,
        target='./img/pick_map_stage_add.jpg',
        value=0.8,
        offsetX=25,
        offsetY=25,clickNum=3)
        updateImgGray()
    else:
            # 点击进入地下城
        mf2=mouse.findImgAndClick(img_gray=img_gray,
            target='./img/a.jpg',
            value=0.8,
            offsetX=25,
            offsetY=-125)
        if mf2!=True:
            # 选择地下城难度
            stage=mouse.findImgAndClick(img_gray=img_gray,
            target='./img/pick_map_stage_add.jpg',
            value=0.8,
            offsetX=25,
            offsetY=25,clickNum=3)
    # 点击进入地下城
    mouse.findImgAndClick(img_gray=img_gray,
        target='./img/a.jpg',
        value=0.8,
        offsetX=25,
        offsetY=-125)


enterMap1=False
def onMap1():
    global enterMap1
    m1=picture.match_multiple(img_gray,'./img/map1_a.jpg',0.9)
    
    if m1!=False and enterMap1==False:
        # 刚进入图1
        enterMap1=True
        print('图1a 召唤兽')
        callAll()
        
    else:
        m2=picture.match_multiple(img_gray,'./img/map1_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            print('图1 行走')
            print(m2)
            
            moveNext.map1MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map1_b_2.jpg',0.9)
            if m3!=False:
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                print('图1 行走')
                print(m3)
                moveNext.map1MoveNext()
            else:
                print('no map1')
enterMap2=False
def onMap2():
    global enterMap2
    m1=picture.match_multiple(img_gray,'./img/map2_a.jpg',0.9)
    if m1!=False and enterMap2==False:
        enterMap2=True
        print('刚进入图2')
    else:
        m2=picture.match_multiple(img_gray,'./img/map2_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            print('图2 行走')
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            moveNext.map2MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map2_b_2.jpg',0.9)
            if m3!=False:
                print('图2 行走')
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                moveNext.map2MoveNext()
                # updateImgGray()
            else:
                print('no map2')

enterMap3=False
def onMap3():
    global enterMap3
    m1=picture.match_multiple(img_gray,'./img/map3_a.jpg',0.9)
    if m1!=False and enterMap3==False:
        enterMap3=True
        print('刚进入图3')
    else:
        m2=picture.match_multiple(img_gray,'./img/map3_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            print('图3 行走')
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            moveNext.map3MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map3_b_2.jpg',0.9)
            if m3!=False:
                print('图3 行走')
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                moveNext.map3MoveNext()
                # updateImgGray()
            else:
                print('no map3')

enterMap4=False
def onMap4():
    global enterMap4
    m1=picture.match_multiple(img_gray,'./img/map4_a.jpg',0.9)
    if m1!=False and enterMap4==False:
        enterMap4=True
        print('刚进入图4')
        
    else:
        m2=picture.match_multiple(img_gray,'./img/map4_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            print('图4 行走')
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            moveNext.map4MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map4_b_2.jpg',0.9)
            if m3!=False:
                print('图4 行走')
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                moveNext.map4MoveNext()
                # updateImgGray()
            else:
                print('no map4')

enterMap5=False
def onMap5():
    global enterMap5
    m1=picture.match_multiple(img_gray,'./img/map5_a.jpg',0.9)
    if m1!=False and enterMap5==False:
        enterMap5=True
        print('刚进入图5')
        print('召唤兽')
        callAll()
    else:
        m2=picture.match_multiple(img_gray,'./img/map5_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            print('图5 行走')
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            moveNext.map5MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map5_b_2.jpg',0.9)
            if m3!=False:
                print('图5 行走')
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                moveNext.map5MoveNext()
                # updateImgGray()
            else:
                print('no map5')

enterMap6=False
def onMap6():
    global enterMap6
    m1=picture.match_multiple(img_gray,'./img/map6_a.jpg',0.9)
    if m1!=False and enterMap6==False:
        print('刚进入图6')
        enterMap6=True
        
    else:
        m2=picture.match_multiple(img_gray,'./img/map6_b_1.jpg',0.9)
        if m2!=False:
            #图1 结束
            print('图6 行走')
            dnf_function.pick()
            dnf_function.chart_to_center(img_gray)
            moveNext.map6MoveNext()
            # updateImgGray()
        else:
            m3=picture.match_multiple(img_gray,'./img/map6_b_2.jpg',0.9)
            if m3!=False:
                print('图6 行走')
                dnf_function.pick()
                dnf_function.chart_to_center(img_gray)
                moveNext.map6MoveNext()
                # updateImgGray()
            else:
                print('no map6')

enterMap7=False
def onMap7():
    # BOSS 房间
    global enterMap1
    global enterMap2
    global enterMap3
    global enterMap4
    global enterMap5
    global enterMap6
    global enterMap7
    m1=picture.match_multiple(img_gray,'./img/map7_a.jpg',0.9)
    if m1!=False and enterMap7==False:
        print('刚进入图7')
        enterMap7=True
        dm.KeyPressStr('hy',2000)
    else:
        # 翻牌
        fanpai=picture.match_multiple(img_gray,'./img/map7_b.jpg',0.9)
        if fanpai!=False:
            print('翻牌')
            dm.KeyPressStr('37',200)
        # 加百利商店
        # 再次挑战
        agint=picture.match_multiple(img_gray,'./img/map7_c.jpg',0.7)
        if agint!=False:

            dnf_function.pick()
            print('再次挑战')
            dm.KeyPress(121)
            enterMap1=False
            enterMap2=False
            enterMap3=False
            enterMap4=False
            enterMap5=False
            enterMap6=False
            enterMap7=False

# 召唤所有生物
def callAll():
    dm.KeyPressStr('qwertasdfg',1000)
def updateImgGray():
    global img_gray
    img_gray=picture.get_image_gray()

firstEnter()
def main():
    
    updateImgGray()
    
    print(enterMap1,enterMap2,enterMap3,enterMap4,enterMap5,enterMap6)
    if enterMap2==False :
        onMap1()
    if enterMap3==False:
        onMap2()
    if enterMap4==False:
        onMap3()
    if enterMap5==False:
        onMap4()
    if enterMap6==False:
        onMap5()
    # if enterMap7==False:
    onMap6()
    onMap7()
    
    main()

main()
# dnf_function.chart_to_center(img_gray)
# print(picture.get_target_on_screen_point(img_gray,'./img/pointA.jpg',0.8))

# moveNext.map2MoveNext()
# dnf_function.pick()
# onMap1()
# main()
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
