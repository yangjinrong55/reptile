# -*- coding:utf-8 -*-
import threading
from queue import Queue
from lxml import etree
import requests
from time import sleep
import os
import urllib.request
class threadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        super(threadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    def run(self):
        print("启动" + self.threadName)
        while not Exit:
            try:
                #获取数据
                page = self.pageQueue.get(False)
                url = "http://www.mmonly.cc/ktmh/list_28_" + str(page) + ".html"
                content = requests.get(url,headers = self.headers)
                sleep(1)
                #存放数据
                content.encoding = content.apparent_encoding
                content1 = content.text
                #print(content1)
                self.dataQueue.put(content1)
                # imgList = content2.xpath(".//*[@id='infinite_scroll']//div/div[1]/div/div[1]/a/img/@original")
                # print(imgList)
                #.//*[@id='infinite_scroll']//div/div[1]/div/div[1]/a/img 获取图片
            except:
                pass
        print("关闭" + self.threadName)


class threadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,lock):
        super(threadParse,self).__init__()
        self.threadName = threadName
        self.dataQueue = dataQueue
        #self.fileName = fileName
        #锁
        self.lock = lock
    def run(self):
        print("启动" + self.threadName)
        while not Pass:
            try:
                #获取数据
                html = self.dataQueue.get(False)
                self.parse(html)
                #.//*[@id='infinite_scroll']//div/div[1]/div/div[1]/a/img 获取图片
            except:
                pass
        print("关闭" + self.threadName)
    def parse(self,html):
        num = 0
        content = etree.HTML(html)
        #图片
        imgList = content.xpath(".//*[@id='infinite_scroll']//div/div[1]/div/div[1]/a/img/@original")
        #图片名字
        imgNameList = content.xpath(".//*[@id='infinite_scroll']//div/div[1]/div/div[1]/a/img/@alt")
        #两个列表的for循环
        for img,imgName in zip(imgList,imgNameList):
            num += 1
            self.saveImage(img,imgName,num)


    def saveImage(self,img,imgName,num):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"
        }
        # html = requests.get(url = img,headers = self.headers)
        # html.encoding = html.apparent_encoding
        # html1 = html.text
        html = urllib.request.Request(url=img,headers=self.headers)
        html1 = urllib.request.urlopen(html).read()
        path = r"D:\python\第7章 爬虫\images"
        root = path + "\\" + imgName + ".jpg"
        print(imgName + "-->已保存")
        try:
            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(root):
                with open(root, "wb") as f:
                    f.write(html1)
        except:
            pass
        with self.lock:
            # 写入存储的解析后的数据
            #self.fileName.write(img)
            pass

Exit = False
Pass = False

def main():
    path = r"D:\python\第7章 爬虫\images\1.txt"
    #存储路径
    #fileName = open(path,"w")

    # 创建锁
    lock = threading.Lock()

    #页码的队列，表示10个页面
    pageQueue = Queue(3)
    #放入1-10的数字，先进先出
    for i in range(1,4):
        pageQueue.put(i)
    #采集结果（每页的HTML源码）的数据队列，参数为空表示不限制
    dataQueue = Queue()
    #三个采集线程的名字
    crawlList = ["一号线程","二号线程","三号线程"]
    #存储三个线程采集
    threadCraw = []
    for threadName in crawlList:
        thread = threadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        threadCraw.append(thread)
    #三个解析线程的名字
    parseList = ["解析线程1号","解析线程2号","解析线程3号"]
    #存储三个解析线程
    parseCraw = []
    for threadName in parseList:
        thread = threadParse(threadName,dataQueue,lock)
        thread.start()
        parseCraw.append(thread)


    #等待pageQueue队列为空，也就是等待之前操作执行完毕
    while not pageQueue.empty():
        pass
    #如果pageQueue为空，采集线程退出循环
    global Exit
    Exit = True
    print("pageQueue为空")
    for thread in threadCraw:
        thread.join()
    # 如果dataQueue为空，采集线程退出循环
    while not dataQueue.empty():
        pass

    global Pass
    Pass = True
    print("dataQueue为空")
    for thread in parseCraw:
        thread.join()
    # with lock:
    #     # 关闭文件
    #     fileName.close()
    print("谢谢使用！")

if __name__ == '__main__':
    main()