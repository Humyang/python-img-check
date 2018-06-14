import picture as picture
move_on_mil=20 #每毫秒移动20像素
catch_img='./current_img.jpg'
#人物行走到指定图片位置
def charct_to_pic(img_path,offsetX,offsetY):
    char_img='./pointA.jpg'# 角色关键图
    bd=between_distance(catch_img,char_img,img_path)
    # print(bd)
    #获取图片在屏幕上的坐标
    # (0,0) -> (100,100)
    # 计算出需要行走的像素
    #生成人物行走的代码
    run_to_point(bd)
    
# 计算两个图片在主图的距离
def between_distance(parentImg,pointA,pointB):
    print(parentImg,pointA)
    pa=picture.get_point(parentImg,pointA,0.8)
    pb=picture.get_point(parentImg,pointB,0.8)
    # print(pb[0]-pa[0],pb[1]-pa[1])
    mx=pb[0]-pa[0]
    my=pb[1]-pa[1]
    return (mx,my)
    # return 0
    

def run_to_point(m):
    # 获取变量：每毫秒移动的像素值
    move_x(m[0])
    move_y(m[1])

def move_x(value):
    if value>0:
        print('按住右箭头',value /move_on_mil,'毫秒')
        # 大于0则往右边移动，按下右箭头
    else:
        print('按住左箭头')
        print('按住左箭头',value /move_on_mil,'毫秒')
        # 小于0往左边移动，按下左箭头

def move_y(value):
    if value>0:
        print('按住上箭头')
        print('按住上箭头',value /move_on_mil,'毫秒')
        # 大于 0 则往上移动
    else:
        print('按住下箭头')
        print('按住下箭头',value /move_on_mil,'毫秒')
        # 小于 0 则往下移动

charct_to_pic('./pointB.jpg',100,200)

