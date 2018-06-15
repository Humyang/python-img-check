# 搜索图1（城镇状态）
    # 进入地下城选择页面
        # 获取当前位置
        # 获取入口位置(地图直接进入)
        # 移动至入口

#搜索图2（地下城选择页面)
    # 搜索要刷的地下城
        #鼠标移动到该位置
            #点击进入

#搜索图3（处于地下城中)
    # 召唤宠物
        # 顺序按下技能键

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


import screenshort
import dnf_function
import picture
#计算移动距离因子
def get_distance_var():
    # 截图，获取人物当前位置
    # pyCDC=screenshort.window_capture('./temp_screen/')
    # print(moveStart)
    # bd=picture.get_point('./temp_screen/'+moveStart,'./temp_screen/pointA.jpg',0.4)
    bd=picture.get_target_on_screen_point('./temp_screen/pointA.jpg',0.4)
    # bd=picture.get_point(pyCDC,'./temp_screen/pointA.jpg',0.4)
    print(bd)
    # 行走500毫秒
    # 截图，获取人物当前位置
    # moveEnd=screenshort.window_capture('./temp_screen/')
    # 计算两图之间的偏移像素，得到距离因子
    # （结束位置-开始位置）/ 时间 = 每秒的移动距离

get_distance_var()