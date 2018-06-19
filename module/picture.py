import cv2
import numpy as np
# import handle
# 在image匹配Target，并且画一个框框标注
def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    # w=int(w*2.5)
    # h=int(h*2.5)
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151),1)

    # cv2.imshow('Detected',img_rgb)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL) 
    # imS = cv2.resize(img_rgb, (w, h))                  # Resize image
    cv2.imshow("output", img_rgb)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 获取 Target在Image的坐标
def get_point(image,Target,value):
    # 获取template在目标的位置
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    # print(loc)
    result=''
    for pt in zip(*loc[::-1]):
        result=pt
    return result

import pyautogui
def get_target_on_screen_point(Target,value):
    image = pyautogui.screenshot()
    img_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    # print(loc)
    result=''
    for pt in zip(*loc[::-1]):
        result=pt
    
    return result

def match_multiple(img_gray,Target,value=0.8):
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    # print(loc)
    result=(-1,-1)
    for pt in zip(*loc[::-1]):
        result=pt
    
    if result==(-1,-1):
        return False
    else:
        return result
    
def get_image_gray():
    image = pyautogui.screenshot()
    img_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    return img_gray

def test():
    image = pyautogui.screenshot()
    img_gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)
    m2=match_multiple(img_gray,'../script/map1/img/pick_map_stage_add.jpg',0.6)
    print(m2)


# test()
# import datetime
# print(datetime.datetime.now())

# print(datetime.datetime.now())
# m1=match_multiple(img_gray,'../script/map1/img/a.jpg')
# print(m1)
# print(datetime.datetime.now())
# m2=match_multiple(img_gray,'../script/map1/img/b.jpg')
# print(m2)
# print(datetime.datetime.now())
# print(match_multiple(img_gray,'../script/map1/img/c.jpg'))
# print(datetime.datetime.now())
# print(match_multiple(img_gray,'../script/map1/img/d.jpg'))
# print(match_multiple(img_gray,'../script/map1/img/e.jpg'))
# print(match_multiple(img_gray,'../script/map1/img/f.jpg'))
# print(datetime.datetime.now())
# print(match_multiple(img_gray,'../script/map1/img/g.jpg'))
# mathc_img('./temp_screen/2018615233215.jpg','./temp_screen/pointA.jpg',0.4)
# print(get_point('./temp_screen/2018615235658.jpg','./temp_screen/pointA.jpg',0.4))
# image=("test_2_a.jpg")
# Target=('test_2_b.jpg')
# value=0.4

# print(get_target_on_screen_point('./temp_screen/pointA.jpg',0.6))
# print(get_point(image,Target,value))
