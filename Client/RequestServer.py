#!usr/bin/env python
# coding:utf-8

import urllib2



def GetTask( url, clientData, headers={}):
    request = urllib2.Request(url, data = clientData, headers = headers)
    response = urllib2.urlopen(request)
    return response

def AffirmTask(url, data, headers={}):
    request = urllib2.Request(url, data=data, headers=headers)
    response = urllib2.urlopen(request)
    return response

