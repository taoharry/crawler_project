#!usr/bin/env python
# coding:utf-8

import urllib,urllib2
import re
import sys

from BaseObj import BaseObj
from BaseDate import BaseData
reload(sys)
sys.defaultencoding('utf-8')

HostList = '<ul id="houseList">[\s\S]*?</ul>'
LI = '<li class="clearfix">[\s\S]*?</li>'

class Ziru(BaseObj):

    def __init__(self):
        #暂且保留留作任务模块
        pass

    def getPage(self):
        html = self.getPageContent(self.url)
        ul = self.reSearch(HostList,html,0)
        lis = re.findall(LI,ul)
        for li in lis:
            pass

