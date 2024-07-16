import os
from datetime import datetime
  #导入os,datetime模块

pctime = datetime.now()
# 获取当前时间

pctimeh = pctime.hour
pctimem = pctime.minute
pctimes = pctime.second
# 提取时、分、秒

def gy():
        print("#作者:shuaisir360725")
        print("#网站:https://github.com/Sshuaisir360725/Automatic-shutdown")
        print("#邮箱:Sshuaisir360725@outlook.com & shuasir360725@163.com(163邮箱的关注度较低)")
        print("#更新日志v1.0.3:")
        print("1.加入时间显示功能")
        print("2.增加“自定义关机时间”功能")
        print("3.细节优化")
        print("4.程序结构优化")
#关于内容
while True:  
    #--------------------------------------------------------------------------------输出选项:
    print("----------------定时关机V1.0.3--------------")
    print("当前时间是: {}时{}分{}秒".format(pctimeh, pctimem, pctimes))
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
    a=input("请输入选项:")
    a=int(a)
    #--------------------------------------------------------------------------------执行部分:
    #-s指的是执行的操作为关机 -t是是延迟时间 以秒为单位
    if a==1:
        print("正在执行...")
        os.system('shutdown -s -t 0')
    elif a==2:
        print("正在执行...")
        os.system('shutdown -s -t 300')
    elif a==3:
        print("正在执行...")
        os.system('shutdown -s -t 600')
    elif a==4:
        print("正在执行...")
        os.system('shutdown -s -t 1800')
    elif a==5:
        print("正在执行...")
        os.system('shutdown -s -t 3600')
    elif a==6:
        print("正在执行...")
        os.system("shutdown /a")
    elif a==7:
        time = input("请输入自定义时间(大于零的正整数,单位为秒):")
        if time.isdigit():
            time = int(time) 
            print("正在执行...")
            os.system(f'shutdown -s -t {time}')
            print("成功执行,电脑将在",time,"秒后关闭")
        else:
                print("输入的时间无效，必须为大于零的正整数。")
    elif a==8:
        inputimeh = int(input("输入希望关机的时间(时,且大于当前时间)"))
        inputimem = int(input("输入希望关机的时间(分)"))
        inputimes = int(input("输入希望关机的时间(秒)"))
        pctimeh = pctime.hour
        pctimem = pctime.minute
        pctimes = pctime.second
        if  inputimeh<pctimeh:
            print("输入的时间无效!请重试!") 
        else:
            gettimeh = inputimeh - pctimeh
            gettimem = inputimem - pctimem
            gettimes = inputimes - pctimes
            gettime = 3600*gettimeh + 60*gettimem + gettimes
            print("正在执行...")
            os.system(f'shutdown -s -t {gettime}')            
    elif a==9:
        gy()
    elif a==10:
        break
        print("正在退出...")
    else:
        print("无效选项")