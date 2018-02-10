#/usr/bin/env python
#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")


import os
from flask import Flask, jsonify
#sys.path.append("/home/harry/ENV/")
execPath = os.path.dirname(os.path.realpath(__file__))
appPath = os.path.dirname(execPath)
envPath = os.path.dirname(appPath)
sys.path.append(appPath)

from utills.monggoSql import MonggoUtils
from utills.logUtiles import logUtils
from utills.timeUtils import formatToday

app = Flask(__name__)
log = logUtils()


#输出接口
@app.route('/<channel>/<location>/<sort>/<int:sortid>/<int:ids>', methods=['GET'])
def hello_world(channel, location, sort,sortid,  ids):
    #return 'Hello World!'
    newResault = []
    ids = int(ids)
    sortid = int(sortid)
    lt = formatFind(location)
    log.info([channel,location,sort,sortid,ids])
    for cha in lt:
        #import pdb
        #pdb.set_trace()
        resalut = MonggoUtils().getDataToday(channel, cha, sortid, sort)
        for i in resalut:
            del i['_id']
            newResault.append(i)
    log.info('start flask_web')
    if ids == 0:
        ids =1
    elif ids+10 > len(newResault):
        return jsonify(newResault[-10:])

    return jsonify(newResault[ids:ids+10])

def formatFind(location):
    lt = []
    location = location.split('_') if location != 'NoneFind' else 'NoneFind'
    monggofind = {"timeIn":formatToday}
    if location != 'NoneFind':
        for l in location:
            monggofind["location"] = {"$regex":l}
            lt.append(monggofind)
    else:
        lt.append(monggofind)
    return lt



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=2018,ssl_context='adhoc')
