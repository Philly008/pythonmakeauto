# -*- coding: utf-8 -*-
import xlrd, xlwt
from datetime import date, datetime

def read_excel():
    # 打开文件
    workbook = xlrd.open_workbook(r'E:\workspace\pythonmakeauto\pythonmakeauto\人员信息.xlsx')
    # 获取所有 sheet
    print(workbook.sheet_names())
    sheet2_name = workbook.sheet_names()[1]
    # 根据 sheet 索引或者名称获取 sheet 内容
    sheet2 = workbook.sheet_by_index(1) # sheet 索引从 0 开始
    sheet2 = workbook.sheet_by_name('Sheet2')

    # sheet 的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)





    # 获取整行和整列的值（数组）
    rows = sheet2.row_values(3) # 获取第四行内容
    cols = sheet2.col_values(2) # 获取第三列内容


    if (sheet2.cell(2,2).ctype == 3):
        date_value = xlrd.xldate_as_tuple(sheet2.cell_value(rows, 3), workbook.datemode)
        date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    print(rows)
    print(date_tmp)

    # 获取单元格内容
    print(sheet2.cell(1,0).value)
    print(sheet2.cell_value(1,0))
    print(sheet2.row(1)[0].value)

    # 获取单元格内容的数据类型, 0 empty, 1 string, 2 number, 3 date, 4 boolean, 5 error
    print(sheet2.cell(1,0).ctype)

if __name__ == '__main__':
    read_excel()
