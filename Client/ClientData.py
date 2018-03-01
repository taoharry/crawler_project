#!usr/bin/env python
# coding:utf-8

import traceback

class ClientData(object):

    def __init__(self,clientIp = '',version = '',length = 100):

        self.clientIp = clientIp
        self.version = version
        self.length = length


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

