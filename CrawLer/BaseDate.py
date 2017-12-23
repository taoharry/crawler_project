#!usr/bin/env python
# coding:utf-8
import sys

from crawler_project.utills.timeUtils import formatToday,exposeTimeNow

class BaseData(object):
    '''
    需要增加类型检验，还未做
    '''
    def __init__(self,keyword='',channel='',taskType='daliay',image='',name='',location='',innerUrl='',
                 area='',usearea='',traffic_distance='',
                 tier='',icons='',subway=[],balcony='',
                 price=0,publish='',price_way='',timeIn=formatToday,timeNow=exposeTimeNow):
        self.keyword = keyword
        self.channel = channel
        self.taskType = taskType
        self.timeIn = timeIn
        self.timeNow = timeNow #字符时间
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

