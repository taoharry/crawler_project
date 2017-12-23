#!/usr/bin/env python
#coding:utf8

__Auther__ = "harry"
__Createtime__ = "2017/11/18 18:07"
__Version__ = 1

import sys
from pymongo import MongoClient

from crawler_project.config.config import monggoHost,monggoPort,monggoUser,monggoPwd,monggoDb
from crawler_project.utills.timeUtils import formatToday


class MonggoUtils(object):

    def __init__(self):
        self.client = MongoClient(monggoHost,monggoPort)
        self.db = self.client.admin
        self.db.authenticate(monggoUser,monggoPwd)
        self.Usedb = self.client[monggoDb]


    def insertOne(self,Dict):
        """
        传进来是类的字典，channel为数据库集合
        :param Dict:
        :return:
        """
        if not isinstance(Dict,dict):
            return 'type erro:need dict '
        collection = Dict.get('channel','')
        if collection != '':
            self.Usedb[collection].insert_one(Dict)


    def insertMany(self,List):
        """
        传进来是类的字典的列表，channel为数据库集合
        :param Dict:
        :return:
        """
        if not isinstance(List,dict):
            return 'type erro:need List '
        collection = List[0].get('channel','')
        if collection != '':
            self.Usedb[collection].insert_many(List)

    def updateSql(self):
        pass

    def getDataOne(self, collection, trem):
        resault = {}
        r = self.Usedb[collection].find_one({"price":trem,"timeIn":formatToday})
        if r.count > 0:
            resault = r
        return resault

    def getDataAll(self, collection, trem):
        resault = {}
        r = self.Usedb[collection].find({"price":trem,"timeIn":formatToday})
        if r.count > 0:
            resault = r
        return resault

    def getDataToday(self, collection, cha, sortid=1,sort='price'):
        resault = {}
        if sortid != 1:
            sortid = -1
        r = self.Usedb[collection].find(cha).sort(sort,sortid)
        #r = self.Usedb[collection].find({"timeIn": u"17-11-20"})
        if r.count > 0:
            resault = r
        return resault


if __name__ == "__main__":
    collection = 'ziru'
    cha = {"timeIn":formatToday,"location":{"$regex":"双井"}}
    print cha
    MonggoUtils().getDataToday(collection,cha)