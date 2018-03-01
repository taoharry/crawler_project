#!usr/bin/env python
# coding:utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import time
import hashlib
import traceback

from utills.check_fields import checkFileds

class TaskData(checkFileds):

    def __init__(self,taskId = '', duration = 20, channel = '',interval = 1800,
                 path = '',descript = '', priority = 0,data = [],taskType='',
                 clientType = '', version = ''):
        self.taskType = taskType
        self.taskId = taskId
        self.chanenl = channel
        self.descript = descript
        self.interval = interval   #下次执行间隔
        self.duration = duration   #执行时长,超过这个时间杀死任务
        self.priority = priority
        self.clientType = clientType  #容器数量
        self.version = version
        self.data = data
        self.path = path
        self.createTime = int(time.time())

class Newclass(object):
    def __init__(self):
        pass


def dict2obj(d):
    try:
        obj = Newclass()
        if "__class__" in dict:
            class_name = d.pop('__class__')
            obj.__class__.__name__ = str(class_name)
        if "__module__" in dict:
            class_module = d.pop('__module__')
            obj.__module__ = str(class_module)
        for k, v in d.items():
            obj.__setattr__(k, v)
    except:
        print traceback.format_exc()
        obj = d

    return obj

def obj2dict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

