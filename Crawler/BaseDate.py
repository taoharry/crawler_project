#!usr/bin/env python
# coding:utf-8

from utills.timeUtils import formatToday

class BaseData(object):
    '''
    需要增加类型检验，还未做
    '''
    def __init__(self,image='',name='',location='',innerUrl='',
                 area='',usearea='',traffic_distance='',
                 tier='',icons='',subway=[],balcony='',
                 price=0,publish='',price_way='',timeIn=formatToday):
        self.timeIn = timeIn
        self.image = image #照片
        self.name = name
        self.location = location
        self.innerUrl = innerUrl
        self.area = area   #多少平
        self.usearea = usearea  #居室
        self.traffic_distance = traffic_distance #交通距离
        self.tier = tier    #层
        self.zhenge = icons #整租或者合租
        self.traffic = subway
        self.balcony = balcony #阳台
        self.publish = publish  #发布者
        self.price = price
        self.price_way = price_way #支付方式

