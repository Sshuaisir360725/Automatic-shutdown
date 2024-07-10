import os  #导入os模块

while True:  
    #--------------------------------------------------------------------------------输出选项:
    print("----------------定时关机V1.0.2--------------")
    print("1.立即关机")
    print("2.5分后关机")
    print("3.10分钟后关机")
    print("4.30分后关机")
    print("5.1小时后关机")
    print("6.取消任何的延时关机")
    print("7.自定义时间")
    print("8.关于")
    print("9.退出程序")
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
        print("#作者:shuaisir360725")
        print("#网站:https://github.com/Sshuaisir360725/Automatic-shutdown")
        print("#邮箱:Sshuaisir360725@outlook.com & shuasir360725@163.com(163邮箱的关注度较低)")
        print("#更新日志v1.0.2:")
        print("1.加入了“关于”选项,添加了“更新日志”")
        print("2.加入了“无效选项”")
        print("3.添加了“自定义时间”选项,可以自由设置关机时间")
        print("4.小BUG修复")
    elif a==9:
        break
        print("正在退出...")
    else:
        print("无效选项")