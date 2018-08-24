# -*- coding: utf-8 -*-
import scrapy
from douyu.items import DouyuItem
import json
from bs4 import BeautifulSoup
import re
import requests
import os
import time
class DouyumeinvSpider(scrapy.Spider):
    name = "dongman"
    #allowed_domains = ["http://www.mmonly.cc"]

    page = 1
    url = "http://www.mmonly.cc/ktmh/list_28_"

    start_urls = [url + str(page) + '.html']

    def parse(self, response):
        textcontent = BeautifulSoup(response.text,'lxml')
        textList = textcontent.find_all('div',{'class':'item masonry_brick masonry-brick'})
        for text in textList:
            item = DouyuItem()
            #item['imageUrl'] = text.find('img').get('src')
            item['imageName'] = text.find('img').get('alt')
            a = text.find('div',{'class':'items_likes'}).get_text()
            #匹配张数，输出多少张
            nums = re.findall(r'\d+',a.split()[2])[0]
            #详细图的初始化地址
            item['bigPageUrl'] = text.find('a',{'target':'_blank'}).get('href')
            #获取第一张图
            self.firstUrl(item['bigPageUrl'])
            #http://www.mmonly.cc/ktmh/dmmn/13544.html
            #匹配URL
            b = re.findall(r'(.*?).html',item['bigPageUrl'])[0]


            for i in range(2,int(nums)+1):
                #获取大图片所在的URL地址，除了第一张外
                bigPage = b + '_' + str(i)+ '.html'
                #回调函数传递参数
                time.sleep(0.5)
                #yield scrapy.Request(bigPage, callback=lambda response,startUrl=item['bigPageUrl']: self.xianImage(response,startUrl))
                yield scrapy.Request(bigPage, callback=self.xianImage)
            yield item

        if self.page <= 359:
            self.page += 1
        yield scrapy.Request(self.url + str(self.page) + '.html', callback=self.parse)
    def firstUrl(self,startUrl):
        '''获取第一张详细图的方法'''
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        html1 = requests.get(url=startUrl, headers=headers)
        html2 = BeautifulSoup(html1.text, 'lxml')
        c1 = html2.find('div', {'class': 'big-pic'})
        startImgUrl = c1.find('img').get('src')
        bigName = c1.find('img').get('alt').encode('latin1').decode('gbk')
        #print(bigName,startImgUrl)
        self.firstImg(startImgUrl, bigName)


    def xianImage(self,response):
        #获取其他图片的URL
        html = BeautifulSoup(response.text,'lxml')
        c = html.find('div',{'class':'big-pic'})
        item = DouyuItem()
        #获取真正的大图图片地址
        item['imageUrl'] = c.find('img').get('src')
        item['imageName1'] = c.find('img').get('alt')
        #取详细图片
        name = item['imageUrl'][-6:]
        #item['num'] = c.find('a').get('href').split('.')[0]

        self.saveImg(item['imageUrl'],item['imageName1'],name)


    def saveImg(self,url,imgName,name):
        print(url,imgName,name)
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        #获取图片
        img = requests.get(url=url,headers=headers).content
        time.sleep(0.5)
        #获取第一张详细图片
        #startImg = requests.get(url=startImgUrl,headers=headers).content
        #保存路径
        root = r'D:\python\第7章 爬虫\第2节 scrapy框架\images'
        path = root + '\\'+ imgName
        path1 = path + '\\' + imgName + name
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path1):
            with open(path1,'wb') as f:
                f.write(img)
    def firstImg(self,startImgUrl,bigName):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"}
        # 获取第一张详细图片
        time.sleep(0.5)
        img = requests.get(url=startImgUrl, headers=headers).content
        # 保存路径
        root = r'D:\python\第7章 爬虫\第2节 scrapy框架\images'
        path = root + '\\' + str(bigName)
        path1 = path + '\\' + bigName+'.jpg'
        if not os.path.exists(path):
            os.mkdir(path)
        if not os.path.exists(path1):
            with open(path1, 'wb') as f:
                f.write(img)






