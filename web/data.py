#coding:utf-8
import xlrd

def read_data(name,row,col):
    path = 'D:\\测试代码\\web\\test_data.xlsx'
    excel = xlrd.open_workbook(path)
    sheet = excel.sheet_by_name(name)
    values = sheet.cell_value(row-1,col-1)
    if type(values)==float:
        return int(values)
    else:
        return values

