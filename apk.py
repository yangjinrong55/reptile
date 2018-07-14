#/usr/bin/env python
#coding:utf-8


import os




class App(object):

    def Install(self):
        print unicode("请输入apk存放的路径（注：路径不能包含中文,所安装的apk名字不能有中文）：" ,"utf-8")
        path1 = raw_input(r"")
        print "start install..."
        for (root, dirt, files) in os.walk(path1):
            for fileName in files:
                packageName = os.path.join(root, fileName).decode('gbk').encode('utf-8')
                print packageName
                os.popen("adb install " + packageName)


        print "success install..."


    def Uninstall(self):
        #os.popen("adb wait-for-device")
        print "start uninstall..."
        for packages in os.popen("adb shell pm list packages -3").readlines():
            packageName = packages.split(":")[-1].splitlines()[0]
            print packageName
            os.popen("adb uninstall " + packageName)

        print "uninstall success..."

def main():
    print "=" * 20
    print unicode("批量安装功能按数字：1", "utf-8")
    print unicode("批量卸载功能按数字：2", "utf-8")
    print unicode("退出按数字：3", "utf-8")
    print "=" * 20

    while True:
        print unicode("请输入所需要的操作：", "utf-8")
        try:
            a = int(raw_input(""))
        except Exception as a:
            print unicode("请输入数字！", "utf-8")
        if a == 1:
            b = App()
            b.Install()
        elif a == 2:
            b = App()
            b.Uninstall()
        elif a == 3:
            break
        else:
            print unicode("请重新输入所需要的操作：", "utf-8")



if __name__ == "__main__":
    main()

