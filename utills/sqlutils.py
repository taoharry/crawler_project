#!/usr/bin/env python
#coding:utf8

__Auther__ = "harry"
__Createtime__ = "2017/11/12 17:11"
__Version__ = 1

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,Date


engine = create_engine('mysql+pymysql://crawler:zufang@45.63.57.78:3306/crawler',echo=True)
Base = declarative_base()

class basicInfo(Base):
    __tablename__ = 'basicInfo'

    id = Column(Integer,primary_key=True)
    image = Column(String)
    tm = Column(Date)
    name = Column(String)
    location = Column(String)
    innerUrl = Column(String)
    area = Column(String)  # 多少平
    usearea = Column(String)  # 居室
    traffic_distance = Column(String)  # 交通距离
    tier = Column(String)  # 层
    zhenge = Column(String)  # 整租或者合租
    traffic = Column(String)  # []
    balcony = Column(String)  # 阳台
    publish = Column(String)  # 发布者
    price = Column(Integer)
    price_way = Column(String)  # 支付方式
    

    def __repr__(self):
        return self.name,self.price