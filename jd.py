# -*- coding:utf-8 -*-
import glob
import os
import xml.dom.minidom
from  xml.dom.minidom import Document
import bs4
import requests
import re
import csv
from urllib.request import urlretrieve

#获取分类的函数
def gethtml(url):
    h = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
    r = requests.get(url,headers=h)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    soup = bs4.BeautifulSoup(r.text,'lxml')
    menus= soup.find_all('ul',{"class":"J_valueList clearfix"})
    #main_menus = soup.find_all('span',{"class":"text"})
    #种类列表
    name_list = []
    #每个种类的链接列表
    url_list = []
    for a in menus:
        s_class = a.find_all('a')
        for i in s_class:
            name = i.get('onclick')
            class_url = i.get('href')
            mainname = name.split("'")[-2].split("::")[0]
            s_name = name.split("'")[-2].split("::")[1].replace('\\','')
            name_list.append([mainname,s_name])
            url_list.append(class_url)
    return name_list,url_list

#获取单个商品的链接
def get_sampleurl(url):
    h = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
    r = requests.get(url,headers=h)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    soup = bs4.BeautifulSoup(r.text,'lxml')
    sampleurl_list = []
    sample_1 = soup.find_all('li',{"class":"gl-item"})
    for i in sample_1:
        sample_url = "https://item.jd.com/" + i.get("data-sku") + ".html"
        sampleurl_list.append(sample_url)
    return sampleurl_list

def get_sample(url):
    h = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome"}
    r = requests.get(url,headers=h)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    soup = bs4.BeautifulSoup(r.text,'lxml')
    #获取属性
    attr_list = []
    sample_attr_1=soup.find_all('ul', {"class": "p-parameter-list"})[0]
    sample_attr_2 = sample_attr_1.find_all('li')[0].get("title")
    attr_list.append(['品牌',sample_attr_2])
    sample_attr_3 = soup.find_all('ul', {"class": "parameter2 p-parameter-list"})[0]
    sample_attr_4 = sample_attr_3.find_all('li')
    for attr in sample_attr_4:
        attr1 = attr.text
        attr_name= attr1.split("：")[0]
        attr_info = attr1.split("：")[1]
        attr_list.append([attr_name,attr_info])
    #获取样例图
    sample_pic_1 = soup.find_all('ul', {"class": "lh"})[0]
    sample_pic_2 =sample_pic_1.find_all("img")
    pic_list = []
    pic_list.append(url)
    for pic_url in sample_pic_2:
        pic_url_1 ="http:"+pic_url.get("src")
        pic_list.append(pic_url_1.replace("s50x64","s350x449"))
    return attr_list,pic_list


if __name__ == '__main__':
    #地址
    path = "D://女装//"
    if not os.path.exists(path):
        os.mkdir(path)
    #京东上直接搜索女装的网址
    url = "http://search.jd.com/Search?keyword=%E5%A5%B3%E8%A3%85&enc=utf-8&wq=n%C3%BC%27zhuang&pvid=4584e7e37f5347bfad87f8e7dbe4900e"
    #print(get_sampleurl(url))
    #分类的列表 如上市时间（2018.。。。。） 和 那个分类所链接的列表
    name_list, url_list =gethtml(url)
    for num in range(len(name_list)):
        #判断该文件夹是否存在
        if not os.path.exists(path+name_list[num][0]):
            os.mkdir(path+name_list[num][0])
        if not os.path.exists(path+name_list[num][0]+"//"+name_list[num][1]):
            os.mkdir(path+name_list[num][0]+"//"+name_list[num][1])
        sampleurl_list=get_sampleurl('http://search.jd.com/' + url_list[num])
        sample_num = 0
        for sample_url in sampleurl_list:
            path1 = path + name_list[num][0] + "//" + name_list[num][1] + "//" + name_list[num][1] + "_" + str(sample_num)
            if not os.path.exists(path1):
                os.mkdir(path1)
            attr_list, pic_list=get_sample(sample_url)
            attr_main_list = []
            attr_last_list = []
            for attr in attr_list:
                attr_main_list.append(attr[0])
                attr_last_list.append(attr[1])
            attr_main_list.append("链接")
            attr_last_list.append(sample_url)
            with open(path1+"//attr.txt", "a+", newline='', encoding="utf-8") as cs:
                c_w = csv.writer(cs)
                c_w.writerow(attr_main_list)
                c_w.writerow(attr_last_list)
                # cs.write(str(attr_main_list))
                # cs.write(str(attr_last_list))
            o =0
            for pic_url in pic_list[1:]:
                try:
                    urlretrieve(pic_url, path1+"//images_%s.jpg" % o )
                except:
                    urlretrieve(pic_url, path1 + "//images_%s.jpg" % o)
                o+=1
            sample_num+=1