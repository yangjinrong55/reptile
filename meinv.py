import urllib.request
from time import sleep
from lxml import etree
import os

def getPage(url,starPage,endPage):
    num = 0
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    for page in range(starPage+1,endPage+1):
        fullUrl = url + str(page) + ".html"
        request = urllib.request.Request(url = fullUrl,headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('gbk')
    #解析为xml文件
        content = etree.HTML(html)
        linkList = content.xpath('//div[@class="ABox"]/a/img/@src')
        for link in linkList:
            print(link)
            num += 1
            getImg(link,num)

def getImg(link,num):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
    request = urllib.request.Request(url=link, headers=headers)
    response = urllib.request.urlopen(request).read()
    html = response
    filename = link[-6:]
    path = "E://images//"
    root = path + filename
    print("正在保存第" + str(num) + "张图片")
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(root):
            with open(root,"wb") as f:
                f.write(html)

    except:
        print("保存失败！")


if __name__ == "__main__":
    url = "http://www.mmonly.cc/tag/cs/"
    try:
        starPage = int(input("请输入要爬取页面的开始页："))
        endPage = int(input("请输入要爬取页面的结束页："))
    except Exception:
        print("请输入数字！")
    getPage(url,starPage,endPage)
