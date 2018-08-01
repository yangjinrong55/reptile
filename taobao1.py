#-*-coding:utf-8-*-

import urllib.parse
import os
import requests
#from bs4 import BeautifulSoup
import re
import urllib.request

def getPage(url,dir):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"}

    content = requests.get(url,headers = header)
    #查找商品ID,正则匹配原始字符串
    try:
        #查找商品的数目
        goodId = re.findall('"nid":".*?"',content.text)[0:7]
        for Id_1 in goodId:
            Id = Id_1.split(":")[1]
            #去掉左引号
            Id1 = Id.lstrip('"')
            #去掉右引号
            Id2 = Id1.rsplit('"')[0]
            #详情页评论地址
            commentUrl = "https://rate.taobao.com/feedRateList.htm?auctionNumId="+Id2+"&userNumId=750646293&currentPageNum=1&pageSize=20&rateType=3&orderType=sort_weight&attribute=&sku=&hasSku=false&folded=0&ua=098%23E1hv2QvWvRyvUpCkvvvvvjiPPsMv6jtWnLqysj3mPmPWAjrWPFFUQjYVRFLU0j3UR2yCvvpvvvvviQhvCvvv9UUEvpCWmWjrvvakfaClYC978BLhQnLhV3O0747B9Wma%2BoHoDO2hsC6tExjxAfev%2BulAozc60f06WeCp%2BExrAEeKNB3rsWBlHdUf8%2B3lYE7refyCvm9vvvv4phvv1vvv9kBvpvLXvvmm86Cv2vvvvUUdphvUOQvv9k1vpv1pkphvC99vvOC0p4yCvv9vvUvA%2Bmq%2FH9hCvvOvUvvvphvPvpvhMMGvv2yCvvpvvvvv3QhvCvvhvvmCvpvZznsocuNNznswPADfzgPGAn1K7eTrvpvEvvCXvdJzvUmI&_ksTS=1533045311015_1026&callback=jsonp_tbcrate_reviews_list"
            getComment(commentUrl,dir)
    except:
        pass
    # good = soup.find_all("a",{"class":"J_ClickStat"}))
def getComment(url,dir):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"}
    imageUrl = requests.get(url,headers=header).text
    #查找评论的图片url地址
    imageUrlLists = re.findall('"url":".*?"',imageUrl)
    for imageUrlList in imageUrlLists:
        imgUrl = imageUrlList.split(":")[1]
        # 去掉左引号
        imgUrl1 = imgUrl.lstrip('"')
        # 去掉右引号
        imgUrl2 = imgUrl1.rsplit('"')[0]
        fullImgUrl = "http:" + imgUrl2
        saveImg(fullImgUrl,dir)


i = 0
#保存图片
def saveImg(fullImageUrl,dir):
    #初始化i的值
    global i
    i += 1
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0"}
    img = requests.get(url=fullImageUrl,headers = header).content
    # request = urllib.request.Request(url=fullImageUrl,headers=header)
    # response = urllib.request.urlopen(request).read()
    path = r"C:\images2" + "\\" + dir
    # i = fullImageUrl[-35:]
    # print(i)
    # root = path + "\\" +i
    root = path + "\\" +str(i) + ".jpg"
    print("正在保存" + str(i) + "张图片")
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists(root):
        with open(root,"wb") as f:
            f.write(img)





def main():

    filePath = r"C:\Users\ADMIN\Desktop\品牌"
    for root,dirs,files in os.walk(filePath):
        for dir in dirs:
            #获取url地址
            url = "https://s.taobao.com/search?q=" + dir +"&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&sort=sale-desc"
            getPage(url,dir)
            #print(url)


if __name__ == "__main__":
    main()
