#!/usr/bin/env python
#coding:utf8

__Auther__ = "harry"
__Createtime__ = "2017/11/12 11:49"
__Version__ = 1


import sys
reload(sys)
sys.setdefaultencoding('utf8')



def formatUrl(url):
    url = 'http:%s'%url if url.startswith("//") else url
    url = url.split('?')[0] if '?' in url else url

    return url

def pageUtils(num,pagenum):
    p = divmod(num,pagenum)
    if p[1] != 0:
        p = p[0] + p[1]
    else:
        p = p[0]

    return p