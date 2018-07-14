import urllib.request
import re
from lxml import etree
import os
import csv
def getShuxing(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request).read()
    html = response.decode("gbk")

    # xpath匹配
    content = etree.HTML(html)
    # 获取属性名称
    lists = content.xpath('//div[5]/div/div[1]/div/dl[3]/dd//a/@title')
    # 获取url值
    listUrl = content.xpath('//div[5]/div/div[1]/div/dl[3]/dd//a/@href')

    # 各个属性的url
    list1 = str(listUrl[0])
    url = "https:" + list1
    getStyleUrl(url)
    # for list1 in listUrl:
    #     print(list1)

    # 获取属性文件名
    for list in lists:
        root = "E://男士上装//"
        path = root + list
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            os.mkdir(path)




#得到每个属性的URL值
def getStyleUrl(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request).read()
    html = response.decode("utf-8")
    content1 = etree.HTML(html)
    oneList = content1.xpath(".//*[@id='J_goodsList']/ul//li/div/div[1]/a/@href")
    oneUrl = "https:" + str(oneList[4])

    getOneUrl(oneUrl)
#得到其中一个属性的一个代表URL
def getOneUrl(oneUrl):
    num = 1
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    }
    request = urllib.request.Request(url=oneUrl, headers=headers)
    response = urllib.request.urlopen(request).read()
    html1 = response

    content2 = etree.HTML(html1)
    #获取文本内容

    texts = content2.xpath(".//*[@id='detail']/div[2]/div[1]/div[1]/ul[2]//li/text()")
    # filename = texts[0]
    saveText(str(texts))


    #获取图片内容
    imgLists = content2.xpath(".//*[@id='spec-list']/ul//li/img/@src")
    for imgList in imgLists:
        saveImg(imgList,num)
        num += 1




#保存图
def saveImg(imgList,num):
    filename = "第" + str(num) + "张"
    root = "E://男士上装"
    # 获取创建的文件路径，保存图片
    for root, dirs, files in os.walk(root):
        for dir in dirs:
            path = os.path.join(root, dir)
            print(path)
            path1 = path + '//' + filename
            print("正在保存第" + str(num) + "张图片")
            try:
                if not os.path.exists(path):
                    os.mkdir(path)
                if not os.path.exists(path1):
                    with open(path1, "wb") as f:
                        f.write(imgList)
            except:
                print("保存失败！")
#保存文本
def saveText(text):
    #获取单个属性，商品属性保存的路径
    root = "E://男士上装"
    #获取创建的文件路径
    for root,dirs,files in os.walk(root):
        for dir in dirs:
            path = os.path.join(root,dir)
            root1 = path + "//" + '衣服属性' + '.txt'
            if not os.path.exists(path):
                os.mkdir(path)
            if not os.path.exists(root1):
                with open(root1, "w") as f:
                    f.write(text)

if __name__ == "__main__":
    url = "https://channel.jd.com/1315-1342.html"
    getShuxing(url)


