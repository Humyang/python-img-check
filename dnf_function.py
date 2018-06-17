import picture as picture
import time
import win32com.client
import reg
dm = win32com.client.Dispatch('dm.dmsoft')

dm.Reg(reg.getRegCode(),"")

move_on_milX=0.486 #每毫秒移动20像素
move_on_milY=0.32
#人物行走到指定图片位置
def charct_to_pic(point,offsetX=0,offsetY=0):
    char_img='./temp_screen/pointA.jpg'# 角色关键图
    bd=between_distance(char_img,point)
    bb=bd[0]+offsetX
    bc=bd[1]+offsetY
    #获取图片在屏幕上的坐标
    # 计算出需要行走的像素
    #生成人物行走的代码
    run_to_point((bb,bc))

# 计算两个图片在主图之中相距的距离
def between_distance(pointA,pointB):
    # print(parentImg,pointA)
    pa=picture.get_target_on_screen_point(pointA,0.6)
    pb=picture.get_target_on_screen_point(pointB,0.6)
    dm.MoveTo(pa[0],pa[1])
    mx=pb[0]-pa[0]
    my=pa[1]-pb[1]#x的y的计算顺序是相反的
    print(mx,my)
    return (mx,my)
    # return 0

def run_to_point(m):
    dm.LeftDoubleClick()
    # 获取变量：每毫秒移动的像素值
    move_x(m[0])
    move_y(m[1])

def move_x(value):
    if value>0:
        # 大于0则往右边移动，按下右箭头
        print('按住右箭头',abs(value /move_on_milX),'毫秒')
        dm.KeyDown(39)
        time.sleep(abs(value /move_on_milX)/1000)
        dm.keyUp(39)   
    else:
        print('按住左箭头',abs(value /move_on_milX),'毫秒')
        # 小于0往左边移动，按下左箭头
        dm.KeyDown(37)
        time.sleep(abs(value /move_on_milX)/1000)
        dm.keyUp(37)  

def move_y(value):
    if value>0:
        print('按住上箭头',abs(value /move_on_milY),'毫秒')
        dm.KeyDown(38)
        time.sleep(abs(value /move_on_milY)/1000)
        dm.keyUp(38) 
        # 大于 0 则往上移动
    else:
        print('按住下箭头',abs(value /move_on_milY),'毫秒')
        # 小于 0 则往下移动
        dm.KeyDown(40)
        time.sleep(abs(value /move_on_milY)/1000)
        dm.keyUp(40) 

charct_to_pic('./temp_screen/moveToB.jpg',-200)
