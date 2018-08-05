#-*-coding:utf-8-*-
import requests
from queue import Queue
import threading
import urllib.request
from time import sleep
import os
#采集类
class threadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue):
        super(threadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        #self.dataQueue = dataQueue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"}
    def run(self):

        #启动爬取线程
        print("启动" + self.threadName)
        while not Exit:
            try:
                page = self.pageQueue.get(False)
                #img = requests.get(url=page, headers=self.headers)
                img = urllib.request.Request(url=page,headers= self.headers)
                img1 = urllib.request.urlopen(img)
                html = img1.read()
                sleep(2)
                global i
                i += 1
                img_save = r'C:\动物'
                print("正在保存" + str(i) + "张图片")
                if not os.path.exists(img_save):
                    os.mkdir(img_save)
                if not os.path.exists(img_save + "\\" + str(i) + ".jpg"):
                    with open(img_save + "\\" + str(i) + ".jpg","wb") as f:
                        f.write(html)
                # self.pageQueue.put(img1)
            # except:
            #     pass
            except urllib.request.HTTPError as reason:
                    print("fail to download, caused by HTTPError")
                    continue
            except urllib.request.URLError as reason:
                    print("fail to download, caused by URLError")
                    continue
            except:
                    print("FAILED for unknow reason!")
                    continue
        print("关闭" + self.threadName)



# class threadParse(threading.Thread):
#     def __init__(self,threadName,dataQueue):
#         super(threadParse,self).__init__()
#         self.threadName = threadName
#         self.dataQueue = dataQueue
#     def run(self):
#         i = 0
#         print("启动" + self.threadName)
#         img_save = r'C:\image3'
#         #root = img_save + "\\" + str(i) + ".jpg"
#         while not Pass:
#             try:
#                 img = self.dataQueue.get(False)
#                 print(img)
#                 sleep(1)
#                 i +=1
#                 print(i)
#                 if not os.path.exists(img_save):
#                     os.mkdir(img_save)
#                 if not os.path.exists(img_save + "\\" + str(i) + ".jpg"):
#                     with open(img_save + "\\" + str(i) + ".jpg","wb") as f:
#                         f.write(img.content)
#             except:
#
#               pass
i = 0
Exit = False
#Pass = False
def main():
    fileurl = r'C:\Users\ADMIN\Desktop\animalUrl.txt'
    f = open(fileurl,encoding="utf-8")
    pageQueue = Queue()
    #dataQueue = Queue()
    for url in f:
        pageQueue.put(url)
    crawlList = ["一号线程", "二号线程", "三号线程"]
    # 存储三个线程采集
    threadCraw = []
    for threadName in crawlList:
        thread = threadCrawl(threadName, pageQueue)
        thread.start()
        threadCraw.append(thread)
    # #存储三个采集线程
    # parseList = ["解析线程1号", "解析线程2号", "解析线程3号"]
    # parseCraw = []
    # for threadName in parseList:
    #     thread = threadParse(threadName,dataQueue)
    #     thread.start()
    #     parseCraw.append(thread)
    #pageQueue不为空，执行
    while not pageQueue.empty():
        pass
    #pageQueue为空，退出hu
    global Exit
    Exit = True
    print("pageQueue采集线程为空")
    for thread in threadCraw:
        thread.join()

    # while not dataQueue.empty():
    #     pass
    # #dataQueue为空，退出hu
    # global Pass
    # Pass = True
    # print("pageQueue采集线程为空")
    # for thread in parseCraw:
    #     thread.join()
    print("谢谢使用")






if __name__ == "__main__":
    main()
