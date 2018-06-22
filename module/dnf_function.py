import picture as picture
import time
import win32com.client
import reg
dm = win32com.client.Dispatch('dm.dmsoft')

dm.Reg(reg.getRegCode(),"")

move_on_milX=0.486 #每毫秒移动20像素
move_on_milY=0.32

def pickF(target,keyPress=False,offsetX=50,valueb=0.8):
    global img_gray
    global isClear
    pick1=charct_to_pic(img_gray,'../map1/img/pointA.jpg',target,offsetX,offsetY=200,valuea=0.6,valueb=valueb)
    if pick1!=False:
        isClear=False
        if keyPress==True:
            dm.keyPressChar('x')
            time.sleep(300/1000)
        
        img_gray=picture.get_image_gray(region=(0,0, 800*2.5, 500*2.5))
    # return False

hidden_count=0
def chart_is_hidden():
    global img_gray
    global hidden_count
    # 确保可以发现人物
    lv=picture.match_multiple(img_gray,'../map1/img/pointA.jpg',0.6)
    if lv==False:
        if hidden_count<3:
            dm.keyDownChar('left')
            time.sleep(300/1000)
            dm.keyUpChar('left')
        elif hidden_count<6:
            dm.keyDownChar('right')
            time.sleep(300/1000)
            dm.keyUpChar('right')
        elif hidden_count<9:
            dm.keyDownChar('up')
            time.sleep(300/1000)
            dm.keyUpChar('up')
        elif hidden_count <12:
            dm.keyDownChar('down')
            time.sleep(300/1000)
            dm.keyUpChar('down')
        img_gray=picture.get_image_gray()
        hidden_count+=1
        chart_is_hidden()
    else:
        hidden_count=0
        
# 拾取地图物品
img_gray=picture.get_image_gray(region=(0,0, 800*2.5, 500*2.5))
isClear=True
def pick():
    print('拾取物品')

    # 确保可以寻找人物
    chart_is_hidden()
    global img_gray
    global isClear
    isClear=True
    img_gray=picture.get_image_gray(region=(0,0, 800*2.5, 500*2.5))
    # 捡魔法装备
    


    # 魔法装备
    # pickF('../map1/img/pick1.jpg',True)
    # 金币
    pickF('../map1/img/pick2.jpg',False)
    # 银质硬币
    pickF('../map1/img/pick3.jpg',False)
    # 团队的感恩
    pickF('../map1/img/pick4.jpg',False)
    # # 金刚石
    # pickF('../map1/img/pick5.jpg',True)
    # # 紫玛瑙
    # pickF('../map1/img/pick6.jpg',True)
    # 赫仑的印章
    pickF('../map1/img/pick7.jpg',True)
    # 魔刹石
    pickF('../map1/img/pick8.jpg',True)
    # 钻石
    pickF('../map1/img/pick9.jpg',True)
    # 拼图碎片
    pickF('../map1/img/pick10.jpg',False)
    # # 生锈的铁片
    # pickF('../map1/img/pick11.jpg',True)
    # # 硬化剂
    # pickF('../map1/img/pick12.jpg',True)
    # 达人mp
    # pickF('../map1/img/pick13.jpg',True)
    # 派对邀请函
    pickF('../map1/img/pick14.jpg',True)
    # 结晶
    pickF('../map1/img/pick15.jpg',True)
    # 绿色的勋章
    # pickF('../map1/img/pick16.jpg',True)
    # 紫色格子
    # pickF('../map1/img/pick18.jpg',True,valueb=0.7,offsetX=0)
    pickF('../map1/img/pick19.jpg',True,valueb=0.8,offsetX=0)
    if isClear==False:
        pick()
    else:
        # dm.keyDownChar('down')
        # dm.keyDownChar('right')
        # time.sleep(1500/1000)
        # dm.keyUpChar('down')
        # dm.keyUpChar('right')
        return True

    # dm.keyPressChar('x')
#人物行走到指定图片位置
def charct_to_pic(img_gray,char_img,point,offsetX=0,offsetY=0,valuea=0.6,valueb=0.6):
    # char_img='../temp_screen/pointA.jpg'# 角色关键图
    
    bd=between_distance(img_gray,char_img,point,offsetX,offsetY,valuea,valueb)
    if bd==False:
        print(char_img,point)
        return False

    # if bd[0]>0:
    #     bb=bd[0]+offsetX
    # else:
    #     bb=bd[0]-offsetX
    # if bd[1]>0:
    #     bc=bd[1]+offsetY
    # else:
    #     bc=bd[1]-offsetY
    
    #获取图片在屏幕上的坐标
    # 计算出需要行走的像素
    #生成人物行走的代码
    run_to_point(bd)

# 计算两个图片在主图之中相距的距离
def between_distance(img_gray,pointA,pointB,offsetX=0,offsetY=0,valuea=0.6,valueb=0.6):
    # print(parentImg,pointA)
    pa=picture.get_target_on_screen_point(img_gray,pointA,valuea)
    pb=picture.get_target_on_screen_point(img_gray,pointB,valueb)
    
    if pa==False:
        print('pa error')
        return False
    
    if pb==False:
        print('pb error')
        return False
    print(pa,pb)
    # dm.MoveTo(pa[0],pa[1])
    mx=pb[0]-(pa[0]+offsetX)
    my=(pa[1]+offsetY)-pb[1]
    #x的y的计算顺序是相反的
    # print(mx,my)
    return (mx,my)
    # return 0

def run_to_point(m):
    # dm.LeftDoubleClick()
    # 获取变量：每毫秒移动的像素值
    # move_y(m[1])
    # move_x(m[0])
    move_xy(m)

def move_xy(m):
    
    mx = m[0]
    my = m[1]
    print(mx,my)
    downX=-1
    downY=-1
    if mx>0:
        # 大于0则往右边移动，按下右箭头
        downX=39
    else:
        # 小于0往左边移动，按下左箭头
        downX=37

    if my>0:
        # 大于 0 则往上移动
        downY=38
    else:
        # 小于 0 则往下移动
        downY=40

    print(downX,downY)
    dm.KeyDown(downX)
    dm.KeyDown(downY)
    sleepX = abs(mx /move_on_milX)/1000
    sleepY = abs(my /move_on_milY)/1000
    sleep1=0
    sleep2=0
    if sleepX >sleepY:
        sleep1 = sleepY
        sleep2 = sleepX - sleepY
        time.sleep(sleep1)
        dm.KeyUp(downY)
        time.sleep(sleep2)
        dm.KeyUp(downX)
    else:
        sleep1 = sleepX
        sleep2 = sleepY - sleepX
        time.sleep(sleep1)
        dm.KeyUp(downX)
        time.sleep(sleep2)
        dm.KeyUp(downY)

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

def chart_to_center(img_gray):
    pa=picture.get_target_on_screen_point(img_gray,'./img/pointA.jpg',0.7)
    if pa==False:
        print('chart_to_center:pa error')
        return False
    pb=(1022, 722)
    mx=pb[0]-(pa[0])
    my=(pa[1])-pb[1]
    run_to_point((mx,my))

# charct_to_pic('./temp_screen/moveToB.jpg',-200)
# pick()