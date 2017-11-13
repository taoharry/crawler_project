#!/usr/bin/env python
#coding:utf8

__Auther__ = "harry"
__Createtime__ = "2017/11/12 21:36"
__Version__ = 1


import xlrd,xlwt


def writeXl(filename,dt):
    data = xlwt.Workbook(encoding='utf8')
    worksheet = data.add_sheet(u'My Worksheet')
    lt = ["name,location,area,tier,usearea,traffic_distance,icons,subway,balcony,publish,price,price_way"]
    n = 0

    for i in lt:
        worksheet.write(0, n, label=i)

    n = 0
    for i in dt:
        n +=1
        a = 0
        for l in i:
            worksheet.write(n, a, label=str(l))
            a +=1

    data.save(filename)
