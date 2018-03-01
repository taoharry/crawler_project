#!usr/bin/env python
# coding:utf-8

import os,time
import socket
import urllib2

appPath = os.path.dirname(os.path.abspath(__file__))
configPath = os.path.join(appPath,'config')
#数据库
monggoHost = '39.106.58.20'
monggoPort = 29017
monggoUser = ''
monggoPwd = ''

dbTask = 'task'
tableWaite = 'waite'
tableDoing = 'doing'
tableFinish = 'finish'
tableClientType = 'clientType'
tableVersion = 'version'

#字段值
taskId = 'taskId'
createTime = 'createTime'
clientType = 'clientType'
version = 'version'

#过期时间
removeTime = int(time.time()) - 12 * 3600
#删表时间
zeroDrop = int(time.time() + (8 * 3600)) / 86400 * 86400 - (8 * 3600)


#确认值
waite_to_doing = 'wtd'
doing_to_finish = 'dtf'

#服务器地址
u_gettask = 'http://127.0.0.1:22222/getask'
u_showversion = 'http://127.0.0.1:22222/showversion'
u_showclient = 'http://127.0.0.1:22222/showclient'
u_canceltask = 'http://127.0.0.1:22222/canceltask'
u_addtask = 'http://127.0.0.1:22222/addtask'
u_affirmtask = 'http://127.0.0.1:22222/affirmtask'
u_ip = 'http://127.0.0.1:22222/getparasitiferip'


parasitiferIp = urllib2.urlopen(u_ip)
dockerIp = socket.gethostbyname(socket.gethostname())
client_ip = str(parasitiferIp) + str(dockerIp)

#version
client_version =  ''
with open(os.path.join(configPath,version.txt),'r') as f:
    client_version = f.read().strip().strip('\n').strip('\r\n')
