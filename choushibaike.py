"--*--utf-8--*--"
import urllib.request
from lxml import etree
import json

def openPage(url):

     headers = {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0"}
     request = urllib.request.Request(url,headers=headers)
     response = urllib.request.urlopen(request).read()
     html = response.decode('utf-8')
     text = etree.HTML(html)
     #返回所有段子的结点内容，contains（）模糊查询方法，第一个匹配标签名，第二个参数的部分名
     nodeLists = text.xpath('//div[contains(@id,"qiushi_tag")]')

     for i in nodeLists:

         imgUrl = i.xpath('./div/a/img/@src')
         # print(type(imgUrl))
         #username = site.xpath('./div/a/@title')[0].encode('utf-8')
         username = i.xpath('.//h2')[0].text
         print(type(username))
         content = i.xpath('.//div[@class="content"]/span')[0].text.strip()
         # 投票次数
         print(type(content))
         vote = i.xpath('.//i')[0].text
         # print i.xpath('.//*[@class="number"]')[0].text
         # 评论信息
         print(type(vote))
         comments = i.xpath('.//i')[1].text
         print(type(comments))
         tem = {
             "imgUrl":imgUrl,
             "userName":username,
             "content":content,
             "vote":vote,
             "comment":comments
         }
         #保存为json文件
         with open("qiushi.json","a") as f:
             f.write(json.dumps(tem,ensure_ascii=False)+"\n")





if __name__ == "__main__":
    url = "https://www.qiushibaike.com/"
    openPage(url)
    tem = {}