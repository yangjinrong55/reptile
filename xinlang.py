import requests
import json
from bs4 import BeautifulSoup
import os
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'Keep-Alive',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
def get_url(url,headers):
    text = requests.get(url,headers=headers).text
    content = json.loads(text)
    data = content.get('data')
    html = BeautifulSoup(data,'lxml')
    img_urls = html.find_all('img')
    ps = html.find_all('p',{'style':'padding-top:5px;padding-bottom:0px;line-height:18px;color:#333;'})
    #获取名字和url地址
    for p,img_url in zip(ps,img_urls):
        name = p.get_text().split()[0]
        name1 = name.replace(':','：').replace('！','；')
        print(name1)
        url1 = img_url.get('src')
        save_img(name1,url1,headers)

def save_img(name,url1,headers):
    img = requests.get(url=url1,headers=headers).content
    url_name = url1[-9:]
    path = r'C:\images2\墨镜'
    path1 = path + '\\' + name
    path2 = path1 + '\\' + name + url_name
    if not os.path.exists(path1):
        os.mkdir(path1)
    if not os.path.exists(path2):
        with open(path2,'wb') as f:
            f.write(img)



if __name__ ==  '__main__':
    for i in range(1,66,1):
        url = 'http://search.sina.com.cn/?c=img&q=%C4%AB%BE%B5&page='+ str(i) +'&num=10&format=api_html&sort=rel'
        get_url(url,headers)
    # url = 'http://search.sina.com.cn/?c=img&q=%C4%AB%BE%B5&page=1&num=10&format=api_html&sort=rel'
    # get_url(url, headers)
