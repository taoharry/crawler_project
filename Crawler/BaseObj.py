#!usr/bin/env python
# coding:utf-8

import urllib,urllib2
import re,random
import sys
reload(sys)
sys.defaultencoding('utf-8')


UserAgent = {'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:56.0) Gecko/20100101 Firefox/56.0",
             'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0 Safari/537.36",
             'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/56.0 Safari/537.36",
             }

class BaseObj(object):

    def __init__(self,url,keyword):
        self.url = url
        self.keyword = keyword
        self.req = urllib2.Request(url)
        self.req.add_header(UserAgent[random.random(0,len(UserAgent))])

    def getPageContent(self):

        html = urllib2.urlopen(self.req).read()
        if isinstance(html,'utf8'):
            html = html
        elif isinstance(html,'utf8'):
            html = html.decode('utf8')
        elif isinstance(html,'GBK'):
            html = html.decode('GBK')

        return html

    def getPostData(self):
        pass

    def getResponse(self):
        pass

    def reSearch(self,partten,content,num=1):
        resault = ''
        com = re.compile(partten,content)
        if com:
            resault = com.group(num)
        return resault