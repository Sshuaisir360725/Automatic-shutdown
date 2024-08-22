import os
from datetime import datetime
import time
  #导入os,datetime,time模块

version = "v1.0.6"


def gy():
    print("\033[0;31m#\033[0m作者:shuaisir360725")
    print("\033[0;31m#\033[0m网站:https://github.com/Sshuaisir360725/Automatic-shutdown")
    print("\033[0;31m#\033[0m邮箱:Sshuaisir360725@outlook.com & shuasir360725@163.com(163邮箱的关注度较低)")
    print("\033[0;31m#\033[0m更新日志",version,":")
    print(" 1.修复了自定义关机时间无法使用的重大bug")
    print(" 2.由于技术原因,自定义关机时间的“时”无法填写小于本机时间的数")
    print(" 3.修复了延时关机无法使用的问题")
    print(" 4.bug修复及优化")

#关于内容

def ys():
    print("--------------------------------------------")
    print("可以操作的选项:")
    print("1.立即关机                      2.1分后关机")
    print("3.5分后关机                     4.10分后关机")
    print("5.30分后关机                    6.1时后关机")
    print("7.2时后关机                     8.退出")
    print("--------------------------------------------")
    
    chose_ys_s = int(input("\033[0;33m请输入选项:\33[0m"))

    if chose_ys_s == 1 :
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 0')
    elif chose_ys_s == 2:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 60')
    elif chose_ys_s == 3:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 300')
    elif chose_ys_s == 4:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 600')
    elif chose_ys_s == 5:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 1800')
    elif chose_ys_s == 6:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 3600')
    elif chose_ys_s == 7:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 7200')
    elif chose_ys_s == 8:
        print("\033[0;32m正在退出...\033[0m")        
    else:
        print("\033[0;31m无效选项\033[0m")

#预设内容


while True:
    
    pctime = datetime.now()
    # 获取当前时间

    pctimeh = pctime.hour
    pctimem = pctime.minute
    pctimes = pctime.second
    # 提取时、分、秒

    #--------------------------------------------------------------------------------输出选项:
    print("----------------定时关机",version,"------------")
    print("\033[0;34m当前时间是: {}时{}分{}秒\33[0m".format(pctimeh, pctimem, pctimes))
    print("可以操作的选项:")
    print("1.预设                   2.取消任何延时关机")
    print("3.自定义延时             4.自定义关机时间")
    print("5.关于                   6.退出程序")
    print("--------------------------------------------")
    a=input("\033[0;33m请输入选项:\33[0m")
    a=int(a)
    #--------------------------------------------------------------------------------执行部分:
    #-s指的是执行的操作为关机 -t是是延迟时间 以秒为单位
    if a==1:
        ys()
    elif a==2:
        print("\033[0;32m正在执行...\033[0m")
        os.system("shutdown /a")
    elif a==3:
        print("1.使用秒为单位的自定义延时")
        print("2.使用时、分、秒为单位的自定义延时")
        print("3.退出程序")
        chose = int(input("\033[0;33m请选择选项:\033[0m"))
        if chose == 1:
            inputtime = input("\033[0;36m请输入自定义时间(大于零的正整数,单位为秒):\033[0m")
            inputtime = int(inputtime)
            if inputtime > 0:                
                print("\033[0;32m正在执行...\033[0m")
                os.system(f'shutdown -s -t {inputtime}')
                print("\033[0;32m成功执行,电脑将在",inputtime,"秒后关闭\033[0m")
            else:
                    print("\033[0;31m输入的时间无效,必须为大于零的正整数。\033[0m")
        elif chose == 2:
            timeh = int(input("\033[0;36m请输入自定义时间(时,大于零的正整数):\033[0m"))
            timem = int(input("\033[0;36m请输入自定义时间(分,大于零的正整数):\033[0m"))
            times = int(input("\033[0;36m请输入自定义时间(秒,大于零的正整数):\033[0m"))
            if timeh < 0 or timeh < 0 or timeh < 0 :
                print("\033[0;31m有一个输入的时间无效,时、分、秒必须为大于零的正整数。\033[0m")
            else:
                time = 3600*timeh + 60*timem + times
                os.system(f'shutdown -s -t {time}')
                print("\033[0;32m成功执行,电脑将在",timeh,"时",timem,"分",times,"秒后关闭\033[0m")
        elif chose == 3:
            print("\033[0;32m正在退出...\033[0m")         
        else:
            print("\033[0;31m选项无效\033[0m")
    elif a==4:
        inputimeh = int(input("\033[0;36m输入希望关机的时间(时):\033[0m"))
        inputimem = int(input("\033[0;36m输入希望关机的时间(分):\033[0m"))
        inputimes = int(input("\033[0;36m输入希望关机的时间(秒):\033[0m"))
        
        pctime = datetime.now()
        # 获取当前时间

        pctimeh = pctime.hour
        pctimem = pctime.minute
        pctimes = pctime.second
        
        if inputimeh > pctimeh:
            gettimeh = inputimeh - pctimeh
            gettimem = inputimem - pctimem
            gettimes = inputimes - pctimes

        else:
            print("\033[0;31m输入的时间无效。\033[0m") 

        gettime = 3600*gettimeh + 60*gettimem + gettimes
        print("\033[0;32m正在执行...\033[0m")
        os.system(f'shutdown -s -t {gettime}')           
    
    elif a==5:
        gy()
    elif a==6:
        print("\033[0;32m正在退出...\033[0m")    
        break
    else:
        print("\033[0;31m无效选项\033[0m")
    
    
    print("\033[0;33m3秒后继续\033[0m")
    time.sleep(3)