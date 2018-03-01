#!usr/bin/env python
# coding:utf-8

import sys
reload(sys)
sys.setdefaultencode('utf8')

import os
clientPath = os.path.dirname(os.path.realpath(__file__))
appPath = os.path.dirname(clientPath)
sys.path.append(appPath)

import time,random
from multiprocessing import Process
from threading import Thread
from RequestServer import AffirmTask
from Content import doing_to_finish,u_affirmtask

class Execue(Process):

    def __init__(self,task):
        super(Exception,self).__init__()
        self.execTime = time.strftime("%y-%M-%d %H-%m-%s",time.localtime())
        self.task = task

    def run(self):
        #自定义内容,目前没有什么需要做
        fun = self.ImportMoudle()
        fun.start(self.task)

    def ImportMoudle(self):
        from CrawLer.ziru import Ziru

        if self.task.taskType == 'ziru': #后续需要在配置文件中静态变量
            return Ziru(self.task)


class Dispatch():#dispatch means 调度

    def __init__(self):
        self.queue = []   #waite 库中取出的数据
        self.doing = []
        self.finisk = []
        self.woking = []
        self.cancel = False
        self.limit_same_time_doing = 1
        self.__do__()

    def AddTask(self,data):
        self.queue.extend(data)

    def Cancel(self,taskId):
        for p in self.woking:
            if p.data.taskId == taskId:
                p.terminate()
                p.join()
                return True
        return False

    def QuenueLen(self):
        length = len(self.woking) + len(self.queue)
        return length

    def __do__(self):
        t = Thread(target=self.__start__())
        t.start()
        t.join()

    def __start__(self):
        while not self.cancel:
            try:
                #优先级排序,越大越靠前
                waite = sorted([data.priority for data in self.queue])
                if len(waite) > 0 and len(self.woking) <= self.limit_same_time_doing:
                    do_task = waite.pop()
                    p = Execue(do_task)
                    self.woking.append(p)
                    self.doing.append(do_task)
                    p.start()
                    p.join(timeout=do_task.duration)
                else:
                    time.sleep(random.random())
                for p in self.woking:
                    if p.is_alive():
                        self.woking.remove(p)
                        self.finisk.append(p.data)
                if len(self.finisk) >= 100:
                    resault = AffirmTask(u_affirmtask,{'affirm':doing_to_finish,'data':self.finisk})
                    if resault.has_key('Check') and resault['Check'] == "sucess":
                        self.finisk = []
            except:
                pass

    def Cancel(self):
        self.cancel = True
