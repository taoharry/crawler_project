#!usr/bin/env python
# coding:utf-8

import time

from utills.MongoSql import MonggoSql
from Content import monggoHost,monggoPort,monggoUser,monggoPwd,dbTask,\
    tableWaite,tableDoing,tableFinish,removeTime,tableClientType,\
    taskId,createTime,clientType,version,tableVersion,zeroDrop

class TaskApi(object):

    def __init__(self):
        self.db = MonggoSql(monggoHost,monggoPort,monggoUser,monggoPwd,dbTask)

    def GetTask(self,clientData,tableName=tableWaite):
        #从waite数据库中读取clientdata.clientType数据
        #data 是一个列表
        if  hasattr(clientData,clientType):
            data = self.db.GetTask(clientData.clientType,tableName)
        else:
            data = []
        return data

    def AffirmTask(self,data,removeTable,insertTable):
        #一组数据 从waite中删除,写入到doing,传进来data是一个列表[{}]
        if not isinstance(data,(tuple,list)):
            return {"TypeErro":"Data type wrong"}
        flag = self.db.RemoveData(data,removeTable)
        if flag:
            r = self.db.InsertMany(data,insertTable)
            if r:
                return {"Check":"sucess"}
            else:
                #从waite中删除成功,插入doing失败
                return {"Check": "Failure insert table %s"%insertTable}
        else:
            # '从waite中删除失败'
            return {"Check": "Failure drop table %s"%removeTable}


    def FinishTask(self,data):
        #一组数据,从doing中删除,写入到finish
        if not isinstance(data,(tuple,list)):
            return {"typeErro":"Data type wrong"}
        flag = self.db.RemoveData(data,tableDoing)
        if flag:
            r = self.db.InsertMany(data,tableFinish)
            if r:
                return {"Check": "sucess"}
            else:
                #从doing中删除成功,插入finish失败
                return {"Check": "Failure insert table finish"}
        else:
            # '从doing中删除失败'
            return {"Check": "Failure drop table doing"}


    def ClearDead(self):
        #间隔清理僵死任务,从doing中移到fail库
        try:
            self.db.DropTimeOutTask()
            return {"Check": "Drop dead sucess"}
        except Exception as e:
            #记录日志
            return {"Check": "Drop dead failure %s"%e}

    def CancelTask(self,taskid):
        #查询waite数据库,删除这组数据,任务下发了或者没必要在处理
        if taskid == '':
            return {'InputErro':"Null value,need str"}
        resault = self.db.FindOneTask(taskid,tableWaite)
        if resault.count() == 1:
            self.db.RemoveData({taskId:taskid},tableWaite)
            return {taskid:"sucess"}
        else:
            return {taskid:"No task"}

    def ShowClientType(self):
        #显示所有容器版本,单独建库,返回是列表
        resault = self.db.GetClientType_or_version(tableClientType)
        return resault

    def RegisterClientType(self,client,version):
        #做判断如果数据库中有这个版本那么忽略,如果没有则插入值,字典计数{版本:num}显示出一共多少这个版本容器
        resault = self.db.InsertOne({client:version})
        return {"RegisterClientType":resault}

    def ClearClientType(self):
        #一段时间清空所有版本数据库
        r = False
        if int(time.time()) == zeroDrop:
            r = self.db.DropTable(tableClientType)
        return {"ClearClientType":r}

    def ShowVersion(self,):
        # 显示所有容器版本,单独建库
        resault = self.db.GetClientType_or_version(tableVersion)
        return resault

    def RegisterVersion(self, VERSION):
        # 做判断如果数据库中有这个版本那么忽略,如果没有则插入值,字典计数{版本:num}显示出一共多少这个版本容器,返回是列表
        flag = False  # 检查数据库中是否注册过该版本
        if not isinstance(VERSION, str):
            return {"typeErro": "Need str give %s" % type(VERSION)}
        f = self.db[tableClientType].find()
        for i in f:
            if VERSION in i:
                flag = True
                num = i[version] + 1 #每个容器都会注册一次
                r = self.db[tableClientType].update(i, {"$set": {VERSION: num}})
                break
        if not flag:
            r = self.db[tableClientType].insert({VERSION: 1})
        return {"RegisterVersion":r}

    def ClearVersion(self):
        # 一段时间清空所有版本数据库
        r = False
        if int(time.time()) == zeroDrop:
            r = self.db.DropTable(tableVersion)
        return {"ClearVersion":r}

    def DelTask(self,taskid):
        #从数据中删除本次任务
        r = self.db.RemoveData({taskId:taskid},tableWaite)
        return {'DelTask':r}

    def FindTaskStatus(self,taskId):
        #遍历查询各个库返回任务状态
        resault = {'waite':{},"doing":{}}
        waitelt = self.db.GetTable(tableWaite)
        doinglt = self.db.GetTable(tableDoing)
        def count(tablelt,tablename):
            for data in tablelt:
                resault[tablename][data.taskId] = 0
                if data.taskId in resault[tablename]:
                    resault[tablename][data.taskId] +=1
        count(waitelt,tableWaite)
        count(doinglt,tableDoing)
        return resault

    def InsertTask(self,data):
        if isinstance(data,(list,tuple)):
            r = self.db.InsertMany(data,tableWaite)
        elif isinstance(data,dict):
            r = self.db.InsertOne(data,tableWaite)
        else:
            return {"TypeErro":"Need list or dict not %s"%type(data)}

        return {'Check':r}
