import xlwt

#excel 保存路径
name = r'D:\python\第7章 爬虫' + '//' + '智联招聘岗位结果.xls'
#创建Excel文件，声明编码为utf-8
wb = xlwt.Workbook(encoding='utf-8')
#创建表格
ws = wb.add_sheet('智联招聘岗位结果')
#表头信息
headData = ['url','职位','公司','发布时间','职责描述']
#写入表头信息
for colnum in range(0,5):
    ws.write(0,colnum,headData[colnum],xlwt.easyxf('font:bold on,height 240'))
wb.save(name)