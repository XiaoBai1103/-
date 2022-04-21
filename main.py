'''
    特别说明：本人不对使用该程序造成的任何后果负责，建议合理使用本程序
    该程序签到功能仅在我的电脑实验成功
    请务必用管理员身份运行，否则无法签到！！！
    如果之后有时间了话写个UI界面
    XiaoBai Apr 22,2022 
'''
from time import sleep 
import cv2
import pyautogui   #自动GUI操作
import pyscreeze   #屏幕截图

count = 0 #签到次数   
while 1:       
    ####目标图片读取&截屏，路径根据自己需要更改####
    target_button=cv2.imread(r'C://pic/button.png', cv2.IMREAD_GRAYSCALE) #读入灰度图片，设置签到照片图片，最好用自己电脑截图
    screenshot=pyscreeze.screenshot('C://pic/screenshot.png')#截图
    target_screenshot=cv2.imread(r'C://pic/screenshot.png', cv2.IMREAD_GRAYSCALE)#cv2读入截屏
    ####获取签到按钮照片的宽高####  
    sp=target_button.shape
    button_height=sp[0]
    button_width=sp[1]
    ####获取屏幕截图宽高####
    sp=target_screenshot.shape
    screenshot_height=sp[0]
    screenshot_width=sp[1]
    ####图片匹配#####
    result = cv2.matchTemplate(target_screenshot, target_button, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    #min_val、max_val都是输入的矩阵中的最小值和最大值
    #min_loc、 max_loc都是最小值 最大值所对应的坐标元组          
    if max_val >= 0.8:
        ####计算签到按钮位置####                                        
        taget_X=max_loc[0]+int(button_width/2)
        taget_Y=max_loc[1]+int(button_height/2)          
        ###鼠标左键点击所计算的目标点####            
        pyautogui.click(taget_X, taget_Y, button='left') 
        ####结果输出#####
        count+=1
        print("已经完成",count,"次签到")
        sleep(10) #暂停10秒继续执行 可以根据老师签到时间把这个值改高点
