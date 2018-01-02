#!usr/bin/env python
# coding:utf-8


import schedule
import time



class scheduleUtils(object):
    """
    第一个是函数,第二个是执行时间
    """
    def minutesJob(self,job,time=10):
        """"""
        if isinstance(time,int):
            schedule.every(time).minutes.do(job)

    def hourJob(self,job,hour=1):
        if isinstance(hour,int):
            schedule.every(hour).hour.do(job)

    def dayJob(self,job,day=1,hour="00:30"):
        if  isinstance(day,int):
            schedule.every(day).day.at(hour).do(job)

    def mondayJob(self,job):
        schedule.every().monday.do(job)

    def wednesday(self,job):
        schedule.every().wednesday.at("13:15").do(job)

    """
    while True:
        schedule.run_pending()
        time.sleep(1)
    """