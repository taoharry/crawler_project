#!usr/bin/env python
# coding:utf-8

import Queue,traceback


from CrawLer.ziru import Ziru
from utills.shceduleUtils import scheduleUtils


scheduleUtils = scheduleUtils()
ziru = Ziru()



def Schrun():
    zr = ziru.main(url='',keyword='北京')
    scheduleUtils.dayJob(zr)

if __name__ == "__main__":
    Schrun()

