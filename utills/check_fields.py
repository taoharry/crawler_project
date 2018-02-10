#!usr/bin/env python
# coding:utf-8

import inspect


class checkFileds(object):

    def __setattr__(self, key, value):
        arg = inspect.getargspec(self.__init__) #获得函数__init__的属性
        args = arg.args  #获得传进来参数,
        defaults = arg.defaults #参数设置默认值
        if 'self' in args:
            args.remove('self')
        kwargs = dict(zip(args, defaults))
        if key in kwargs:
            defType = type(kwargs[key])
            if isinstance(kwargs[key], (str, unicode)):
                defType = (str, unicode)
            elif isinstance(kwargs[key], (int, long)):
                defType = (int, long)
            elif isinstance(kwargs[key], (list, tuple)):
                defType = (list, tuple)
            if  not isinstance(value, defType):
                raise TypeError,"Need %s input %s"%(defType,type(key))

        super(checkFileds,self).__setattr__(key,value)

#example
if __name__ == "__main__":
    class t(checkFileds):
        def __init__(self,name='',number=0):
            self.name = name
            self.number = number
    t('',111)
