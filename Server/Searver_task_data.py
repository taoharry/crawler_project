#!usr/bin/env python
# coding:utf-8

import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
import time
import hashlib
import traceback

from utills.check_fields import checkFileds



class TaskData(checkFileds):

    def __init__(self,version='',taskType="",jobId="",channel="",
                 priority=0,duration=0,data={}):
        if jobId == '':
            self.jobIdId = hashlib.md5(time.time())
        self.jobIdId  = jobId
        self.version = version
        self.taskType = taskType
        self.priority = priority
        self.duration = duration
        self.data = data
        self.channel = channel


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

