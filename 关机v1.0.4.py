import os
from datetime import datetime
import time
  #导入os,datetime,time模块

version = "v1.0.4"

def gy():
        print("#作者:shuaisir360725")
        print("#网站:https://github.com/Sshuaisir360725/Automatic-shutdown")
        print("#邮箱:Sshuaisir360725@outlook.com & shuasir360725@163.com(163邮箱的关注度较低)")
        print("#更新日志",version,":")
        print("1.为“自定义延时”功能添加了“时分秒”模式")
        print("2.为一些字添加了颜色")
        print("3.新增在一次程序运行之后等待三秒的机制")
        print("4.bug修复及优化")
#关于内容
while True:
    
    pctime = datetime.now()
    # 获取当前时间

    pctimeh = pctime.hour
    pctimem = pctime.minute
    pctimes = pctime.second
    # 提取时、分、秒

    #--------------------------------------------------------------------------------输出选项:
    print("----------------定时关机",version,"--------------")
    print("\033[0;34m当前时间是: {}时{}分{}秒\33[0m".format(pctimeh, pctimem, pctimes))
    print("可以操作的选项:")
    print("1.立即关机")
    print("2.5分后关机")
    print("3.10分钟后关机")
    print("4.30分后关机")
    print("5.1小时后关机")
    print("6.取消任何的延时关机")
    print("7.自定义延时")
    print("8.自定义关机时间")
    print("9.关于")
    print("10.退出程序")
    print("--------------------------------------------")
    a=input("\033[0;33m请输入选项:\33[0m")
    a=int(a)
    #--------------------------------------------------------------------------------执行部分:
    #-s指的是执行的操作为关机 -t是是延迟时间 以秒为单位
    if a==1:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 0')
    elif a==2:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 300')
    elif a==3:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 600')
    elif a==4:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 1800')
    elif a==5:
        print("\033[0;32m正在执行...\033[0m")
        os.system('shutdown -s -t 3600')
    elif a==6:
        print("\033[0;32m正在执行...\033[0m")
        os.system("shutdown /a")
    elif a==7:
        print("1.使用秒为单位的自定义延时")
        print("2.使用时、分、秒为单位的自定义延时")
        chose = int(input("\033[0;33m请选择选项:\033[0m"))
        if chose == 1:
            inputtime = input("\033[0;36m请输入自定义时间(大于零的正整数,单位为秒):\033[0m")
            if time.isdigit():
                inputtime = int(inputtime) 
                print("\033[0;32m正在执行...\033[0m")
                os.system(f'shutdown -s -t {inputtime}')
                print("\033[0;32m成功执行,电脑将在",time,"秒后关闭\033[0m")
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
    elif a==8:
        inputimeh = int(input("\033[0;36m输入希望关机的时间(时,且大于当前时间)\033[0m"))
        inputimem = int(input("\033[0;36m输入希望关机的时间(分)\033[0m"))
        inputimes = int(input("\033[0;36m输入希望关机的时间(秒)\033[0m"))
        pctimeh = pctime.hour
        pctimem = pctime.minute
        pctimes = pctime.second
        if  inputimeh<pctimeh:
            print("\033[0;31m输入的时间无效!请重试!\033[0m") 
        else:
            gettimeh = inputimeh - pctimeh
            gettimem = inputimem - pctimem
            gettimes = inputimes - pctimes
            gettime = 3600*gettimeh + 60*gettimem + gettimes
            print("\033[0;32m正在执行...\033[0m")
            os.system(f'shutdown -s -t {gettime}')            
    elif a==9:
        gy()
    elif a==10:
        print("\033[0;32m正在退出...\033[0m")    
        break
    else:
        print("\033[0;31m无效选项\033[0m")
    print("\033[0;33m3秒后继续\033[0m")
    time.sleep(3)