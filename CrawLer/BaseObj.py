#!usr/bin/env python
# coding:utf-8

import urllib,urllib2
import re,random
import sys

from utills.monggoSql import MonggoUtils
#reload(sys)
#sys.setdefaultencoding('utf-8')


UserAgent = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
             'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0 Safari/537.36",
             }

class BaseObj(object):

    def __init__(self,url,keyword):
        pass

    def getPageContent(self,url):
        header = {'User-Agent':random.choice(UserAgent.values())}
        req = urllib2.Request(url,headers=header)
        #req.add_header(random.choice(UserAgent.keys()))
        html = urllib2.urlopen(req).read()
        if isinstance(html,unicode):
            html = html
        elif type(html).__name__ == 'utf8':
            html = html.decode('utf8')
        elif type(html).__name__ == 'GBK':
            html = html.decode('GBK')

        return html

    def getPostData(self):
        pass

    def getResponse(self):
        pass

    def reSearch(self,partten,content,num=1):
        resault = ''
        com = re.compile(partten)
        if com.search(content):
            resault = com.search(content).group(num)
        return resault

    def saveSql(self,content):
        if isinstance(content,dict):
            MonggoUtils().insertOne(content)
        elif isinstance(content,list):
            MonggoUtils().insertMany(content)
        elif isinstance(content,object):
            con = content.__dict__
            self.saveSql(con)
