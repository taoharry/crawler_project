#!usr/bin/env python
# coding:utf-8

import sys,os
execPath = os.path.dirname(os.path.abspath(__file__))
serverPath = os.path.dirname(execPath)
appPath = os.path.dirname(serverPath)

from pymongo import MongoClient


from utills.timeUtils import formatToday
from Content import monggoHost,monggoPort,monggoUser,monggoPwd,dbTask,\
    tableWaite,tableDoing,tableFinish,removeTime,tableClientType,\
    taskId,createTime,clientType

class MonggoSql(object):
    #查询结果是一个迭代器

    def __init__(self, host = monggoHost, port =monggoPort, user = monggoUser,
                 pwd = monggoPwd, db = dbTask):
        #默认是存储数据库
        self.client = MongoClient(host,port)
        self.db = self.client.admin
        self.db.authenticate(user,pwd)
        self.usedb = self.client[db] #sele.client.db



    def InsertOne(self,dt,tableName):
        try:
            if isinstance(dt,dict):
                self.usedb[tableName].insert_one(dt)
                return True
            return False
        except:
            return False

    def InsertMany(self,lt,tableName):
        try:
            if isinstance(lt,(list,tuple)):
                self.usedb[tableName].insert_many(lt)
                return True
            return False
        except:
            return False

    def GetTask(self,client_type,tableName):
        dt = []
        resault = self.usedb[tableName].find({clientType:client_type}).limit(100)
        if resault.count() == 0:
            return []
        for i in resault:
            dt.append(i)
        return dt

    def GetTable(self,tableName):
        dt = []
        resault = self.usedb[tableName].find()
        if resault.count() == 0:
            return []
        for i in resault:
            dt.append(i)
        return dt

    def FindTaskInALLTAble(self,taskid):
        for table in [tableWaite,tableDoing,tableFinish]:
            resault = self.usedb[table].find_one({taskId:taskid})
            if resault.count() > 0:
                return resault.next()
        return False

    def FindOneTask(self,taskid,tableName):
        resault = self.usedb[tableName].find_one({taskId:taskid})
        if resault.count() > 0:
            return resault.next()
        return False


    def GetClientType_or_version(self,tableName):
        dt = []
        resault =  self.usedb[tableName].find()
        if resault.count() == 0:
            return {}
        for i in resault:
            dt.append(i)
        return dt

    def RemoveData(self,data,tableName):
        #data是个字典
        if isinstance(data,(list,tuple)):
            for d in data:
                self.usedb[tableName].remove(d)
        elif isinstance(data,dict):
            self.usedb[tableName].remove(data)
        else:
            #不要抛出异常,写到日志里
            raise TypeError,"Need list or tuple or dict Not %s"%type(data)
            return False
        return True

    def DropTimeOutTask(self):
        try:
            for table in [tableWaite,tableDoing]:
                resault = self.usedb[table].remove({createTime:{"$lte":removeTime}})
                if resault.count() == 0:
                    return True
            return False
        except:
            return False

    def DropTable(self,tableName):
        try:
            self.db[tableName].drop()
            return True
        except:
            return False

