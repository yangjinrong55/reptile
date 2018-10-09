import re
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
def get_img_url(url,headers):
    content = requests.get(url,headers=headers).text
    text = json.loads(content)
    data = text.get('data')
    for i in data:
        url = i.get('share_url')
        get_url(url,headers)


def get_url(url,headers):
    try:
        content = requests.get(url,headers=headers)
        soup = BeautifulSoup(content.text,'lxml')
        #获取图集名称
        title = soup.find('title').get_text()
        images_pattern = re.compile('gallery: JSON.parse\("(.*?)"\)', re.S)
        result = re.search(images_pattern,content.text)
        # 替换不需要的数据

        json_images = re.sub(r'\\{1,2}', '', result.group(1))
        j = json.loads(json_images)
        for i in j.get('sub_images'):
            img_url = i.get('url')
            down_load(img_url,title)
    except Exception:
        pass

def down_load(img_url,title):
    img = requests.get(img_url).content
    name = img_url[-5:]
    print(name)
    path = r'C:\image\戴墨镜'
    path1 = path + '\\' +title
    path2 = path1 + '\\' + title + name + '.jpg'
    if not os.path.exists(path1):
        os.mkdir(path1)
    if not os.path.exists(path2):
        with open(path2,'wb') as f:
            f.write(img)




if __name__ == "__main__":
    for i in range(0,141,20):
        #url = 'https://www.toutiao.com/search_content/?offset=' + str(i) + '&format=json&keyword=%E5%8F%A3%E7%BD%A9&autoload=true&count=20&cur_tab=3&from=gallery'
        url = 'https://www.toutiao.com/search_content/?offset=' + str(i) + '&format=json&keyword=%E6%88%B4%E5%A2%A8%E9%95%9C&autoload=true&count=20&cur_tab=3&from=gallery'
        get_img_url(url,headers)