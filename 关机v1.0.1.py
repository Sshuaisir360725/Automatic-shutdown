import os
while True:
    #--------------------------------------------------------------------------------
    print("-----------------定时关机V1.0.1---------------")
    print("1.立即关机")
    print("2.5分后关机")
    print("3.10分钟后关机")
    print("4.30分后关机")
    print("5.1小时后关机")
    print("6.取消任何的延时关机")
    print("7.退出程序")
    print("--------------------------------------------")
    a=input("请输入选项:")
    a=int(a)
    #--------------------------------------------------------------------------------

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
        break
        print("正在退出...")