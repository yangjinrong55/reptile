import urllib.request
import urllib.parse
from lxml import etree

def loadPage(full_url,file):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    request = urllib.request.Request(url = full_url,headers = headers)
    response = urllib.request.urlopen(request)
    print(full_url)
    print("正在下载" + file)
    contents = response.read().decode('utf-8')
    lxm = etree.HTML(contents)
    print(lxm)
    titles = lxm.xpath(".//*[@id='fm5792635636']/li/div")
    print(titles)
    #解码为utf-8的字符串，bytes转换为str类型
    # content = contents.decode('utf-8')
    # #写入进行编码
    # with open(file,'w',encoding='utf-8') as f:
    #     f.write()
    # print("正在保存" + file)

def fullUrl(b_url,starPage,endPage):
    for page in range(starPage,endPage+1):
        pn = (page-1)*50
        full_url = b_url + "&pn=" + str(pn)
        file = "第" + str(page) + "页"
        loadPage(full_url,file)




if __name__ == "__main__":
    url = "http://tieba.baidu.com/f?"
    name = input("请输入要搜索的贴吧名字：")
    starPage = int(input("开始爬取的页面："))
    endPage = int(input("结束爬取的页面："))
    a_url = urllib.parse.urlencode({'kw':name})
    b_url = url + a_url
    fullUrl(b_url,starPage,endPage)
