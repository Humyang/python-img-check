import sys
sys.path.append('../../module/')

import dnf_function
chart_img='../../temp_screen/pointA.jpg'
import picture

def map1MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    # ../temp_screen/pointA.jpg
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/common_p1.jpg',0,0,valueb=0.9)
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map1_d_2.jpg',-100,100)
def map2MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/common_p1.jpg')
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map2_d_2.jpg',50,200)
    # dnf_function.charct_to_pic(img_gray,chart_img,'./img/map2_d_3.jpg')
def map3MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/common_p1.jpg')
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map3_d_2.jpg')
def map4MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/common_p1.jpg',100,100)
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map4_d_1.jpg',100,100)
def map5MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/common_p1.jpg',0,-300,valueb=0.8)
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map5_d_2.jpg',0,-300,valueb=0.8)
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map5_d_3.jpg')
def map6MoveNext():
    global img_gray
    img_gray=picture.get_image_gray()
    dnf_function.charct_to_pic(img_gray,chart_img,'./img/map6_d_1.jpg',100,100)

# map1MoveNext()