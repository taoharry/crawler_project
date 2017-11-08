#!usr/bin/env python
# coding:utf-8


class BaseData(object):

    def __init__(self,location='',price=0,area='',tier='',icons='',
                 subway=[],balcony='',publish='',hourse=''):
        self.location = location
        self.price = price
        self.area = area
        self.tier = tier    #层
        self.zhenghe = icons #整租或者合租
        self.traffic = subway
        self.balcony = balcony #阳台
        self.publish = publish  #发布者
        self.hourse = hourse #几局
