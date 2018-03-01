 #!usr/bin/env python
# coding:utf-8

import time,copy
import sys,os
reload(sys)
sys.setdefaultencode('utf8')
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


from Content import client_version,client_ip,u_gettask,u_affirmtask,waite_to_doing,doing_to_finish
from ClientData import ClientData, obj2dict
from RequestServer import GetTask,AffirmTask
from CourseExecu import Dispatch

class Heartbeat(object):

    def __init__(self):
        self.heartbeat = 15
        self.execute = False
        self.hasData = []
        self.confirmTask = {'affirm':"",'data':[]} #任务数据
        self.clientData = ClientData(client_ip,client_version)
        self.dispatch = Dispatch()
        self.__start__()


    def GetTaskData(self):
        #api接口,调用接口获取数据
        clientData =  obj2dict(self.clientData)
        datalt = GetTask(u_gettask,clientData)
        return datalt

    def CheckServerTaskData(self,dataLt):
        #api接口,推送过去接收到数据,在服务端waite库删除这一组数据,并在doing库添加本组数据
        #可以扩展如果doing库中一个字段为删除任务则在执行过程删除掉任务
        data = copy.deepcopy(self.confirmTask)
        data['affirm'] = waite_to_doing
        data['data'] = dataLt
        resault = AffirmTask(u_affirmtask,data)
        if 'Check' in resault and resault['Check'] == 'sucess':
            self.hasData = []
            return True
        else:
            return False


    def AddToQuene(self,task):
        #把要执行任务压栈
        self.dispatch.AddTask(task)

    def __start__(self):
        while not self.execute:
            if self.hasData:
                self.CheckServerTaskData(self.hasData)
            else:
                task = self.GetTaskData()
            if task:
                self.AddToQuene(task)
                del task
            if self.JuageQueue: #在加入任务队列判断
                time.sleep(5) #大约1秒钟处理20个网页
            else:
                time.sleep(self.heartbeat)

    def CancelTask(self):
        self.execute = True

    def JuageQueue(self):
        length = self.dispatch.QuenueLen()
        if length != 0:
            return True
        else:
            return False

if __name__ == "__main__":
    Heartbeat()


