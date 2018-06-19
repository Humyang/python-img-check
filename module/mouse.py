import sys
sys.path.append('../../module/')
import picture
import reg
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')
dm.Reg(reg.getRegCode(),"")
import picture
import time
# 搜索图片并且点击
def findImgAndClick(img_gray,
target,
value=0.5,
offsetX=0,
offsetY=0,
clickNum=1,
sleepTime=500):
    pick_map=picture.match_multiple(img_gray,target,value)
    if pick_map!=False:
        # print(target)
        # print(pick_map)
        # print(pick_map[0]+offsetX,pick_map[1]+offsetY)
        dm.MoveTo(pick_map[0]+offsetX,pick_map[1]+offsetY)
        for clickIndex in range(clickNum):
            print('click')
            dm.LeftClick()
            time.sleep(sleepTime/1000)
        
        return True
    else:
        return False