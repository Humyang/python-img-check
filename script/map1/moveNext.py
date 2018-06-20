import sys
sys.path.append('../../module/')

import dnf_function
chart_img='../../temp_screen/pointA.jpg'
def map1MoveNext():
    # ../temp_screen/pointA.jpg
    dnf_function.charct_to_pic(chart_img,'./img/map1_d_1.jpg')
    dnf_function.charct_to_pic(chart_img,'./img/map1_d_2.jpg')
def map2MoveNext():
    dnf_function.charct_to_pic(chart_img,'./img/map2_d_1.jpg')
    dnf_function.charct_to_pic(chart_img,'./img/map2_d_2.jpg',1000,1000)
    # dnf_function.charct_to_pic(chart_img,'./img/map2_d_3.jpg')
def map3MoveNext():
    dnf_function.charct_to_pic(chart_img,'./img/map3_d_1.jpg')
    dnf_function.charct_to_pic(chart_img,'./img/map3_d_2.jpg')
def map4MoveNext():
    dnf_function.charct_to_pic(chart_img,'./img/map4_d_1.jpg',100,100)
def map5MoveNext():
    dnf_function.charct_to_pic(chart_img,'./img/map5_d_1.jpg',100,100)
    dnf_function.charct_to_pic(chart_img,'./img/map5_d_2.jpg',800,600)
def map6MoveNext():
    dnf_function.charct_to_pic(chart_img,'./img/map6_d_1.jpg',100,100)
    # dnf_function.charct_to_pic(chart_img,'./img/map5_d_2.jpg',800,600)