import cv2
import numpy as np

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

# mathc_img('./current_img.jpg','./pointB.jpg',0.8)

# image=("test_2_a.jpg")
# Target=('test_2_b.jpg')
# value=0.4
# print(get_point(image,Target,value))