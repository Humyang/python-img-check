import cv2
import numpy as np

# 在image匹配Target，并且画一个框框标注
def mathc_img(image,Target,value):
    img_rgb = cv2.imread(image)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(Target,0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = value
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (7,249,151),1)
    cv2.imshow('Detected',img_rgb)
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

# 屏幕截图
# def screen_catch():
    # 获取目标窗口坐标
    # 截取指定位置图片，保存在临时文件夹
    # 返回截图文件路径

# mathc_img('./current_img.jpg','./pointB.jpg',0.8)

# image=("test_2_a.jpg")
# Target=('test_2_b.jpg')
# value=0.4

# print(get_point(image,Target,value))
