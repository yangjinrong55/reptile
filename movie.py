"--*--utf-8--*--"
#json解析库，对应相应的lxml
import json
#json的解析语法，对应到xpath
import jsonpath
import requests
import xlwt

def openPage(url):
     headers = {"User-Agent":"Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0"}
     response = requests.get(url,headers = headers)
     response.raise_for_status()
     html = response.text
     #把json形式的字符串转换成python形式的Unicode字符串
     unicode = json.loads(html)
     moviceNameList = jsonpath.jsonpath(unicode,"$..title")
     actorsNameList = jsonpath.jsonpath(unicode,"$..actors")
     regionsList = jsonpath.jsonpath(unicode,"$..regions")
     imgList = jsonpath.jsonpath(unicode,"$..cover_url")
     typeList = jsonpath.jsonpath(unicode,"$..types")
     scoreList = jsonpath.jsonpath(unicode,"$..score")
     urlList = jsonpath.jsonpath(unicode,"$..url")
     #返回数据
     return moviceNameList,actorsNameList,regionsList,imgList,typeList,scoreList,urlList
def writeExcel(moviceNameList,actorsNameList,regionsList,imgList,typeList,scoreList,urlList):
     j = 1
     for i in range(0,len(moviceNameList)):
         try:
             moviceName = moviceNameList[i]
             actorsName = actorsNameList[i]
             regionName = regionsList[i]
             imgName = imgList[i]
             typeName = typeList[i]
             scoreName = scoreList[i]
             urlName = urlList[i]
             #.write（行，列，数据）
             ws.write(j,0,moviceName)
             ws.write(j,1,actorsName)
             ws.write(j,2,regionName)
             ws.write(j,3,imgName)
             ws.write(j,4,typeName)
             ws.write(j,5,scoreName)
             ws.write(j,6,urlName)
             j +=1
             print("写入成功！")
         except Exception as a:
             print("写入失败！",a)

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=5000"
    moviceNameList, actorsNameList, regionsList, imgList, typeList, scoreList, urlList = openPage(url)

    # excel 保存路径
    name = r'D:\python\第7章 爬虫' + '//' + '豆瓣电影2.xls'
    # 创建Excel文件，声明编码为utf-8
    wb = xlwt.Workbook(encoding='utf-8')
    # 创建表格
    ws = wb.add_sheet('豆瓣电影')
    # 表头信息
    headData = ['电影名称','演员','国家','图片地址','类型','评分','详情地址']
    # 写入表头信息
    for colnum in range(0, 7):
        ws.write(0, colnum, headData[colnum], xlwt.easyxf('font:bold on,height 240'))
    writeExcel(moviceNameList,actorsNameList,regionsList,imgList,typeList,scoreList,urlList)
    wb.save(name)